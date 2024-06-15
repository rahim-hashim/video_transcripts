---
Date Generated: June 15, 2024
Transcription Model: whisper medium 20231117
Length: 5110s
Video Keywords: []
Video Views: 72
Video Rating: None
Video Description: In this episode of the Cognitive Revolution, join us as we dive into a compelling conversation with Josep M. Pujol, Chief of Search at Brave, about the complexities of developing a privacy-focused search engine. Explore how Brave maintains user data privacy while managing over 1 million searches per hour with an AI-powered system. Gain insights into the significance of human evaluation in AI and learn about the potential of the Brave Search API. Don't miss the shared Google collab notebook link in the show notes!

Google collab notebook : https://colab.research.google.com/drive/1AxQD-bDePl1l90A_gwvfAGXBIl92ERKy#scrollTo=WrhGZsvbxZy8

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Recommended Podcast:
Byrne Hobart, the writer of The Diff, is revered in Silicon Valley. You can get an hour with him each week. See for yourself how his thinking can upgrade yours.
Spotify: https://open.spotify.com/show/6rANlV54GCARLgMOtpkzKt
Apple: https://podcasts.apple.com/us/podcast/the-riff-with-byrne-hobart-and-erik-torenberg/id1716646486

CHAPTERS:
(00:00:00) Introduction
(00:05:46) Brave
(00:07:52) How Brave collects data
(00:10:45) The problem is not the data
(00:14:02) How Brave builds its index
(00:16:36) PageRank
(00:21:07) Sponsors: Oracle | Brave
(00:23:14) Brave Search
(00:26:26) Hardware improvements
(00:28:33) Language models
(00:34:17) Noise reduction in vertical search
(00:36:50) Fine-tuning models
(00:43:09) Sponsors: Squad | Omneky
(00:44:55) Ensemble approach
(00:58:00) The future of the web
(01:03:30) The business side of this
(01:09:22) Brave Search users
(01:14:21) Brave Search API vs. Google 
(01:20:00) Brave Search API Pricing
(01:23:26) Brave Search API Use Cases
---

# Building Brave: Private Search, One AI Layer at a Time with Josep M. Pujol
**Cognitive Revolution:** [June 15, 2024](https://www.youtube.com/watch?v=S3y1R5f1hBc)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. Today I'm excited to share my
*  conversation with Joseph Pujol, Chief of Search at Brave. As regular listeners will know,
*  Brave has been a sponsor of the Cognitive Revolution for the last several months,
*  and that makes this our first sponsored episode. I think it's important to mention that right at the
*  top for the sake of transparency, though I did approach this episode in exactly the same way
*  that I always do, with a deep dive into the company's products and an earnest search for
*  insights that will be worth your precious time. And I can sincerely say that I believe this episode
*  maintains the quality standard that we always strive for. As you'll hear, Joseph was very open
*  and shared a number of fascinating details about how Brave has built their search product and
*  infrastructure over time, including the trade-offs that they accept to maintain the highest standard
*  for user data privacy. Some of the most interesting details center around the challenges of iteratively
*  improving an AI-powered product while operating at real scale. Brave handles over 1 million searches
*  per hour or roughly 300 searches per second. They do not want to take any steps backward,
*  and so their approach is generally to add to their system, making their ensemble of models
*  and techniques more effective, but also more complicated with each generation. I found this
*  approach really fascinating to learn about, as it's a perspective not often found in younger startups.
*  I also appreciated Joseph's candid perspective on the challenges they face in evaluating search
*  results. Brave has developed some scalable systems to assist in measuring quality,
*  but Joseph emphasized that there still is no fully automated substitute for hands-on human
*  evaluation, good taste, and judgment. I think this, too, is an important lesson for all AI
*  builders to keep in mind. Coming away from this conversation, I genuinely believe that the Brave
*  Search API is an excellent product. I've spent more time testing it since the recording, and for
*  the Weimark Small Business Profile Builder, which today relies primarily on scraping small business
*  websites, I did find it to be notably better than both Bing and Google. As such, I have
*  recommended it to the Weimark product team. My expectation is that, like Brave, we will augment
*  rather than replace our existing system, we'll use the Brave Search API to help us return results
*  faster, to cover URLs that our scraper fails on, and to surface valuable bonus context from
*  discussion and review sites that we simply aren't tapping into today at all. Overall, I think it
*  will be a really nice product win, and given the low cost and latency, I think it's something that
*  more AI builders should consider using. If you'd like to check it out for yourself, I've created
*  a simple Google collab notebook, which makes search API calls to Brave, Google, and Bing.
*  It's nothing fancy, but this is exactly what I've used to evaluate it for Weimark. We'll put the
*  link to that notebook in the show notes. Finally, before we get started, if your company is interested
*  in sponsoring the Cognitive Revolution and potentially being featured in an episode,
*  I invite you to reach out. We'll always be fully transparent about sponsorships, and we will only
*  produce sponsored episodes with companies that I personally judge to be worthwhile on their merits.
*  So my hope is that this will be a win-win for the show, for the sponsor, and most importantly, for you,
*  the audience. As always, we hope you'll share the show with friends, and we invite your feedback.
*  And with that, I hope you enjoyed this inside look at Brave Search and the Brave Search API
*  with Brave's Chief of Search, Josep Pujol. Josep Pujol, Chief of Search at Brave. Welcome to the
*  Cognitive Revolution. Nice being here, and thank you for having me. My pleasure. I'm excited to get
*  deep into all the exciting developments and AI technologies that you have assembled into the
*  Brave Search experience. I guess just as a quick prelude, regular listeners to the show will know
*  that Brave is a sponsor of the Cognitive Revolution, so we thank you for your patronage
*  in supporting us. I've obviously listened to the ad copy a few times, and I know the audience
*  member have as well. Do you want to start off by just giving us a little bit of a general background
*  on Brave, now my default mobile browser, by the way? Just tell us a little bit about the company
*  at a super high level, what the kind of motivations are, the ethos of the company, and then we'll dive
*  after that more deeply into the technology. Yeah, Brave, first of all, is a great company
*  founded by Brian Bundy and Brandon Eich. They started as a browser, especially with a focus
*  on privacy. Myself, I joined Brave three years and a half ago out of a company that was called Clicks
*  or Tailcut, Spinup, and we were developing a search engine from scratch. When a previous company went
*  belly up because of a lack of funding, COVID and whatnot, well, we had multiple potential places
*  to go, and the one that was more appealing was Brave because we share the same values, privacy,
*  preserving, and also they aim to be an alternative to big tech. It's not so much that what we try
*  to achieve is that to do something totally different, because at the end of the day,
*  it's a browser, it's a search engine, it's a talk software, like a video conferencing,
*  but the whole point is that, well, you can actually have the full technology suit without
*  having to rely on big tech with all the compromises that it entails. So that's very appealing.
*  It's very appealing to me personally and to the team. That's why we joined Brave, and I think
*  that's the best definition there is. Of course, there's a bunch of features that are pretty unique,
*  but to me, the biggest value proposition of Brave is that while you use Google,
*  while you can use Brave. I've been impressed actually by just how big the product line is.
*  When I started to get into it more, the mobile browser experience is really good, and the farther
*  I got, I was like, oh, there is a VPN that you can enable here, and there's a chat bot, language
*  model-powered experience, question answering, all that stuff. It really is a pretty, and an ad
*  network as well. There's a lot going on. How many people at the company? It's not that big of a
*  company. I'm impressed by how many different products. But people, Brave as a whole, and
*  people working on search, engineering and quality writers, like the core of search is about 20.
*  20. Wow. On search, right? There's a lot of, it's not just that search is run by 20 people,
*  whether it's marketing, communications, HR. There's a lot of shared resources, right?
*  But anyway, the search is 20 people, Brave as a whole, 200. So it's a very small company. And yes,
*  we do have a lot of reach. But anyway, that's the proof that you don't have to be big to provide
*  value. Yeah, it's impressive. We'll get into some of the head-to-head comparisons as we get a little
*  bit deeper into this. So as head of search, we're going to spend most of our time doing a deep dive
*  into the search technology, how it works. As I've said, our audience is very interested in
*  technical details. Many people that are listening are building stuff, and they are looking for
*  the hard one lesson. They were looking for shortcuts to the lessons that you've learned
*  the hard way. So maybe just for starters, you want to give a general overview of
*  how search works. One thing that definitely stood out to me again from the ad copy is that the
*  data is at least to some degree sourced based on pages that people are actually visiting.
*  And that was, for starters, an interesting data point.
*  Yes, actually that project, the use of browsing data, if you want, that starts from Brave,
*  starts from the previous company. That's how we actually gather enough data to
*  start developing the search engine. But it's a very controversial topic,
*  because there is a certain tendency to have this dichotomy with either data or privacy.
*  This dichotomy is actually false. It's as simple as that. I wrote extensively about it. People can
*  check it out. But basically, the whole point is not so much that data is a problem, it's how you
*  collect that data. I'm not talking about opt-in or doubts or the legal issue, those aside.
*  It's more like what kind of purpose the data will have and how the data is collected,
*  which makes it dangerous or not. For instance, like Brave, if you, people who want to contribute,
*  they can opt-in to something that's called the Web Discovery Project. And in there, they will
*  send us browsing data. That sounds dangerous, what do you mean? It's not that we collect
*  your browsing history or your search history. No, that would be dangerous. That would be like
*  privacy problem. What you will contribute is individual data elements that are anonymous.
*  Someone has visited this site and has engaged so much with it. Then any of those data elements
*  people send us, we have absolutely no way to know whether they come from the same person or not.
*  So we do not learn anything about you or about me. What we learn is that someone is anonymous.
*  There's a lot of technical details here. It's not that we do not use user IDs,
*  neither implicit or explicit. It's just like the data is basically sent using a mixing network to
*  remove network fingerprinting. The messages are homogenized so that they actually have to pass
*  a quantum. So more than X people need to send the same amount of data, the same data in order
*  to be actually received by us. That's like a direct approval. So there's a lot of technical
*  merit. But at the end of the day, what is important is that the data that we receive is anonymous. It's
*  not anonymized or it's pseudonymous. Those are dangerous. Those are the things that
*  they can later be anonymized. The data that we got is just anonymous and it serves a single purpose.
*  In this case, to know that this particular page is popular or not. Or that this particular page was
*  clicked after a particular query to build query logs. So that's the kind of data that we collect.
*  Without that, it would be actually very difficult to build a search engine. Google and Microsoft do
*  the same thing. Whether they admit it or not, actually there is a nice release of some documents
*  that happened yesterday or a couple of days ago where there is some private APIs at Google.
*  That's natural. These data are collected. And again, the problem is not the data.
*  The same way that the problem is not the advertisement. The problem is like,
*  if by doing the advertisement, you actually put your privacy at risk because it's tracking
*  is dangerous. Knowing your browsing history or your search history is extremely problematic.
*  And that's something that we do not want to know and we do not collect. One of the
*  attack vectors that we consider is that if we actually had to release our data,
*  either to a hacker or to a government agency of some sort, we could release it knowingly that
*  no particular person could be identified or profiled.
*  Mad Fientist Yeah, that's really interesting. So if you're in a country where you have reason
*  to be concerned about this sort of stuff, then this becomes an extremely valuable option.
*  Yeah, first, it's an option. Even though it's privacy preserving by design,
*  still we do it an option because it's something that people have to be aware of. But they could
*  enable it. We will not be able to. It's something that's basically technically called record
*  unlinkability. So any data element that we receive, we have no way to know if those two elements come
*  in the same person or not. That means that we only have individual data elements because even
*  if the individual data elements, if we had a way to link them, we could actually create a profile.
*  And based on that profile, it can always be anonymized because they will always be one of
*  the data elements that somehow probabilistically or deterministically can link to you. And then
*  basically the whole session is compromised. The whole point is that we have no technical means
*  to actually build a session so that there is like, yes, somebody visited this page,
*  but we couldn't know what happened afterwards. Of course, that data is much less useful than
*  profile data. Because profile data is not a profile data. It's not that the Google
*  engineers, the evil, say, I want to collect data or not. But basically what you want is that once
*  you collect data, you want to be reusable. You want the same data that you collect to be able to
*  count how popular the page is, but also how big how pages relate to each other or how popular
*  a particular restaurant is at what time. And you want the same data set to be able to answer all
*  those questions. And that's very powerful, but that's very problematic because it can answer all
*  these legitimate questions, but it can also answer illegitimate ones. Like give me the search history
*  of whoever was here at this particular time. So what we cannot do is answer these generic questions.
*  For every question that we have, we collect one particular data element that only answers this
*  particular question. So that's a bit different. How is that important? It's not so much about data
*  or no data. It's like the purpose of the data. So how does this compare or maybe you
*  combine, I guess you have a crawler too, right? So it's not that the index is entirely built from
*  the page visits, but more that it is informed by the page visits?
*  Yeah, I'd like to give specifics on that. We may learn about our URL through web discovery
*  project, right? And we know this URL is popular because it has to pass a portal. So more than
*  end people have to see that URL in order for us to receive that URL. So that means that URL
*  does not belong to you. It's not your login URL. Because there are not 100 people across the world
*  that access that URL. So when we receive that URL, we only receive the URL, right? We don't
*  receive the content because the content, there is no guarantees that the content does not contain
*  private information that belongs to you. So then we receive the URL, which is private information,
*  and then we actually go and fetch it. So that allows us to basically that our index
*  to be like small enough, but still because it's small because we do not crawl blindly.
*  We don't do like a blind crawl of everything. What we do is that we crawl what people
*  basically visit. And from there, and from the website, so we actually do some additional crawling.
*  But most of the crawling we do is not crawling. It's called fetching, right? Because we actually
*  fetch the content. It's not that we proactively crawl the whole web, because the whole web is
*  full of noise. There is like at least 10 different sites that are clones of GitHub.
*  As odd as it sounds, it is. There are sites that are clones of GitHub. So if you crawl blindly,
*  you just like increase by 10 your size, but only by adding noise. So that's like one of the things
*  that we use people for to become more efficient and to reduce the noise, which is like the ultimate
*  goal of any machine learning or AI. Yeah, I was just going to say the cleaning the data set is
*  often where the majority of the work goes. Absolutely. That's like the main realization.
*  Noise reduction is a single most important thing that you have to do ever. Because noise does not
*  only affect the quality of the output of your models, but it does affect the scalability of
*  those models and also the cost of running those models. Noise needs to be avoided as much as
*  possible. So do you have a sense for the relative size of the index compared to what either Google
*  is doing or the whole web? It's a tenth of what Google has. It's a tenth of what Google has,
*  and we can achieve 99.9% of what we call the Google has. Yeah, interesting. Yeah, power laws in action.
*  So a little bit about the signals that you're looking at beyond the behavioral. Obviously,
*  we've gotten from traditional search projects, we've got like keyword based indexing,
*  page rank. I assume you're still getting some value from like that sort of link hierarchy. No.
*  No, rank. No, no. How polemic can it be? As polemic as you want. Page rank is a myth.
*  You know that. Yeah, let me tell you what it means. Think about what I know and then you can correct
*  me. I thought it worked well at the beginning and then it became subject to a lot of adversarial
*  attacks with SEO of a million kinds. And now I would still assume that it has some power,
*  but that it has had to be updated a lot of times in a lot of ways to counteract all these SEO
*  optimizations. Okay. I already was an adult at the university. I almost started to do a PhD when
*  Google came out. I started using Google when it was not even Google.com. It was Stanford. They
*  released two papers. One was the page rank, which was like a proper scientific paper. And the other
*  was like a technical report, like the anatomy of a large search engine where it had the myth of
*  why Google was so good. Who was not good? Because of page rank. Page rank was a gimmick.
*  It was a gimmick that worked, of course, had a contribution, but was good because it had an
*  algorithm and it had a paper on it that was published. And it was something that journalists
*  love to stress, that the algorithm that changes everything. That's what people want to hear. People
*  want to hear a story. That there's like an invention that does, that there's like a straight
*  line. There is like something happened and we went from here to here. That's not what happened.
*  In reality, things are like a little bit more. The reason why Google was so good from the get-go
*  is because of anchor text. Larry and Sergey, through Stanford, were the first ones who,
*  using Stanford resources, were able to crawl the whole web. Crawl the whole web brute force.
*  And that's why you will see like there are some pictures having like hard drives on Lego structures,
*  because they had to buy so many hard drives to be able to store the whole web. That they
*  didn't have like iron to put it. So they actually had to create like Lego stands for it. So the
*  project was like that. They were able to like crawl the whole web. What does it mean to crawl
*  the whole web? That suddenly, unlike AltaVista, you had a much better representation of what the
*  page is. Because you have the backlinks. And the backlinks, what does it say? It really has the
*  anchor text. It's basically like everybody else's description of your site, as opposed to what we
*  had before, which was like your own description of what your site does. Remember, noise is everything.
*  Noise reduction is everything. What is less noisy? The content of the web page or the summary that
*  thousand different people do about your page. But it's much less noisy, the anchor text. And
*  that's why they were able to actually have much better recall with much better precision. And then,
*  you know, like what they want to have the anchor text, you have the backlinks and the backlinks have
*  the anchor text and the adjacency matrix. With the adjacency matrix, you can calculate the first
*  eigenvector, which is like the stationary state of random walk, yada, yada, yada, very nice paper.
*  But that's like cherry on top of the cake. The real myth was their ability to brute force
*  via something that was impossible a couple of years before, to actually brute force and crawl
*  the whole web in a single file system. And then the realization, very smart cake, we have a much
*  cleaner representation of what the page is than the page content. That's what makes Google.
*  That's fascinating. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure or OCI.
*  OCI is a single platform for your infrastructure, database, application development and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing. And of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber eight by eight and Databricks Mosaic, take a free test drive of OCI
*  at oracle.com slash cognitive. That's oracle.com slash cognitive, oracle.com slash cognitive.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages. So what makes the Brave Search
*  index stand out? One, it's entirely independent and built from scratch. That means no big tech
*  biases or extortionate prices. Two, it's built on real page visits from actual humans collected
*  anonymously, of course, which filters out tons of junk data. And three, the index is refreshed with
*  10s of millions of pages daily. So it always has accurate up to date information. The Brave Search
*  API can be used to assemble a data set to train your AI models and help with retrieval augmentation
*  at the time of inference, all while remaining affordable with developer first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data
*  sourcing and more human representative data sets. Try the Brave Search API for free for
*  up to 2000 queries per month at brave.com slash API.
*  How does that play into the Brave Search today? My sense is still that it still matters if a reputable
*  site links to you versus an unreputable site. It seems like there's some sort of authority notion.
*  There is authority, right? But it's not done on a page rank. Right? We can actually write it out of
*  the authority of the pages based on popularity. Just on traffic. Just on traffic. That's
*  enormous. Then you might do a one or two levels deep of calculations. But in any case, that's
*  again, that's a very small contribution to the end goal. What the takeaway message here is not so
*  much a history. It's a little bit more like that very often, like the real innovation happens on
*  something that is not as fashionable as an algorithm. It's more like it's on the methodology.
*  Right? And actually that happens on Brave Search too. Brave Search is as good as it can get.
*  It's because for example, we rely very heavily on query logs. Right? With a query log is in a way,
*  it's like a representation of what the page is about. That is not done on the anchor text,
*  but on the queries of another person. In a way, like Brave Search started being a recommender
*  system engine. And that allows us to keep building query logs, which are in particular same.
*  And as you grow, you have more query logs and then you kind of start to do like semantic
*  relationship with your queries. You've never seen like what is the age of Lady Gaga. Right? But you
*  have seen Lady Gaga's age. And then if you've seen the other one and you know that which is good for
*  this one, it's going to be good for the other query because semantically it's very special.
*  So you keep expanding the query semantically to do a semantic search on queries, not on content,
*  but on queries. Right? And then you start to be able to use like the models to generate
*  syntactic queries, not to try to index the content as a whole, but to create what would be queries
*  that would be answers to this page. Right? And then you do this and then you add it and then you
*  become a little better. Then you start to index content of the page. So you start to use algorithms,
*  right? Which is more conventional approach and more expensive than the other ones. So like the
*  cost to benefit ratio is worse, but now it makes sense, right? Because it's the next step that you
*  have to take. So you keep adding and what you end up is having something that actually works.
*  Does it make a nice history? No, because the story is boring. Your story is no, you just keep
*  building and keep iterating until there's a, you keep like doing 1% increments until you have
*  something that works. But that's like the only way that things typically work again. And that's why
*  I put so much effort into the example of the page rank, because that's like the story. And
*  you're like every step you keep adding and every step there are things that happen that were not
*  possible before. For instance, back before Brave, the same concept that we started was not possible
*  five years before we started. Why not? Because they were like, not because doing recommender system
*  means that you have to have everything on. That's a big cache, a big memory map. So at the time where
*  the servers had 16 gigs of RAM max to host something that has two terabytes, it takes a lot of machines,
*  a lot of machines means a lot of latency, it's not feasible. However, at that time, at clicks,
*  Amazon came, Amazon released a machine that had one terabyte of RAM. Suddenly, it was possible to
*  create a cluster of four machines to actually put everything on memory. And everything became very
*  easy. Right? Where before, one year before that, it would have required like 2000 smaller servers
*  and feasible from the engineering perspective. And those kinds of things happen all the time.
*  Another big hardware improvement that without this research wouldn't exist, NVMe's hard drives.
*  Without NVMe's hard drive, research wouldn't exist. It would not be cost effective. But NVMe's,
*  I guess you know what it is, right? It's like hard drives that are super low latency on lookups.
*  It's faster.
*  Is that the solid state disk as opposed to
*  spinning disk? Or is it even a more fine distinction than that?
*  No, it's actually faster than solid state. There is spinning disk, impossible to do what we do.
*  Flash, still not fast enough, but at least it's like a lot of money to get slower than RAM.
*  Gotcha. Interesting.
*  So suddenly you have what? 100 terabytes, a petabyte of NVMe's. Now you can actually do
*  what you want to do before. It was even the way of doing it would have to be done differently.
*  That would actually increase costs by an order of magnitude, increase everything by an order of
*  magnitude. And it's not global. So again, that's the thing. I think that's how Brave Search was
*  built. Incremental, always taking advantage of what the world had to offer in a way.
*  That history of the hardware enablement is really interesting. Can we do the same,
*  an equivalent history for the progression of language models or semantically enabling models?
*  Because going back to early days, you had literally just keywords and then n-grams. And then
*  now obviously we've got pretty amazing language models. But I would imagine that the best language
*  models are maybe an overkill for some of the use cases, if only because of cost and latency.
*  So what's that history like and where are you guys today in terms of the models that you use
*  for semantic purposes? Yeah. We want an example I thought of before, Lady Gaga, age versus whole
*  world is Lady Gaga. That's a semantic magic. We started to use embeddings, semantic embeddings
*  based on a model that was called a Star Space. I don't know if it's familiar.
*  Sounds familiar. I don't know it specifically.
*  It was in 2019. So a long time ago. And basically the relationship of being able to go from Lady
*  Gaga's age to whole world is Lady Gaga was done by embeddings, 200 dimensions, two bytes,
*  vector search. Back at the time, it was not called vector search. It was called like
*  nearest neighbors approximations. And that's what we built. So we actually took advantage of
*  these recent technologies. Again, there was no only semantic embeddings. There was also
*  like NGAMs based on queries. Remember, we were basically very heavily based on queries.
*  Just to give you a number, a nice number, our query similarity system has more than
*  nine billion unique queries. So the query hotmail is only one. So nine billion. So whenever you
*  actually get a new query, we're able to return a set of similar queries that we have seen in the
*  past out of these nine billion in 20 milliseconds. And that is done both using embeddings, but also
*  using NGAMs based on queries. Because we need both since you cannot be semantic 100%. And that was
*  true back then and it's true now. Why not? What's the limitation there? Or where does the purely
*  semantic approach fall short? Because purely semantic is purely semantic. Sometimes the queries
*  that people do are not set. It doesn't have a semantic meaning. It's like a more particular model
*  or a particular product. And that's what you want. Or like an error on a stack trace. Or like a name
*  of someone. My name is Josep Pujol. Right? It's not Josep Pujol. Semantically, it's very similar.
*  Spanish and Catalan will give you a very close distance in any semantic model, but it's not the
*  same. It's a different person. You need both. The takeaway message, if there is any takeaway message
*  that I could give people is that there is not a single bullet. There is no single anything
*  that solves a problem that is worth solving. Right? It's always a combination of multiple
*  techniques and models and then you do an ensemble on top of it. So can you do only embeddings,
*  semantic embeddings? No. You need to have both. So we do have everything on the ground. So for example,
*  on page content. So we have page content. We do have embeddings based on transformers,
*  bird-like transformers. Yes, we have those. But at the same time, those are what we call dense
*  embeddings. Because the dimensionality that we have is 384 dimensions with two bytes per dimension.
*  And each page has about one to five embeddings of those using different parts of the content,
*  et cetera. But that's like this on the semantic matching, but we still have what we call a sparse
*  embeddings, which is 16,000 dimensions, one bit per dimension, which are for little matching.
*  And when we search, we use both. Right? And it's good to have both approaches because you want to,
*  sometimes when you search for Trump Tower, you just want Trump Tower. You don't want Trump
*  something else. A lot of noise can come out of something else. So you want to combine
*  both approaches and that's what we have. So this mentality, I guess it is shared by many people,
*  including any person who comes to work for us out of university. But, oh yeah, I just like to embeddings
*  out of, I don't know, open AI, put them on a vector database and do a search. And that's it.
*  That doesn't work. It only works for very narrow use cases or for vertical searches when there is
*  like only one domain. But it will not work on a general purpose because it will bring up noise.
*  Statistically, you can't think of the following way. The embedding is not free of errors, right?
*  So let's say that once every 10,000, the embedding has an issue, right? It doesn't provide the right
*  embedding for whatever reason, right? If you are working on a database of 100,000 elements,
*  that will not affect you. It will show that it's working fantastically well. But if you have
*  20 billion, the chances that those errors correlate to your initial recall set are very large.
*  And then you're blind, right? Because you have a recall set of 2,000 documents and 10% of them are
*  nice. What else do I need? I need other things. I need other techniques. I need other models
*  to be able to pick up the noise, right? And that's always there. So there's no single thing
*  that works. It's always like a combination. Yeah, that's probably a really good takeaway for
*  a lot of listeners who are building all manner of rag apps in all kinds of different contexts. I've
*  got a project that I'm involved with that's trying to take old plumbing catalog parts manuals
*  and make that searchable. This is for a company that has a proprietary database of all these
*  old manuals. They literally have them in paper form in a giant bookshelf and they've embarked on
*  this. But this actually is... I can tell you another story. That might actually work because
*  in a way, the level of noise that you have on vertical search is artificially reduced.
*  I don't know if it makes sense. Yeah. Because the problem is always the noise, right? The
*  uncertainty. So when you're doing a vertical something, vertical search, or you're working
*  a particular vertical, noise is artificially reduced, right? Because in a particular domain,
*  a particular word has only one particular meaning or a particular token has only one particular
*  meaning. So when you work only on a vertical, it's very easy to work on. And actually, one of
*  the things that when we first started to tackle power of search, the initial thing to try was like,
*  hey, my search can be split into verticals, right? So if we are like plenty of people, why don't we
*  just do vertical? You do weather search, I do city search, you do famous people search, car search.
*  You come up with like 100 different verticals. So what ended up happening is that all the
*  100 verticals were vertical, right? But there was no way to put them together in a way that
*  made sense, right? Because what we actually did unintentionally is like we pushed the problem,
*  the real problem, we pushed it under the rug, right? On the module that, the mixing module that
*  we'll call in the future, the mixing module is a problem, right? Because on the movie vertical,
*  that has only one meaning, right? The movie that could be that one, two, three, right? But now
*  forget about that you're on the movie vertical, think on the whole web, but that what does it mean?
*  The movie, name of someone, the conference, a part, see, right? Which one it is. That's like the,
*  that's why search is complicated, because it's a general purpose. And I had the same issue, right?
*  The narrower the domain, the easier it is, because there is less noise.
*  Does that assume though, that you are working with enough data? Going back to this plumbing
*  example, and I think trying to generalize from that to what I think a lot of people
*  who listen to this show are working on. I think in a lot of scenarios, there's like a proprietary
*  data set that is like too big for people to like page through, right? So they do need some search
*  to access it effectively. But then at the same time, it's not so much data that they could train
*  a model from scratch on it. Maybe they could fine tune. And so I feel like a lot of people
*  find themselves in that in between zone where they're like, I need to use some sort of pre-trained
*  open source model, at least as a base. And those models, like in this plumbing scenario,
*  everything is in a very narrow section of the broad general purpose embeddings models.
*  And then things like parts numbers, as you said, are not even really semantic at all in a lot of
*  cases. So we are finding that we do need a hybrid search, if only to handle these things like parts
*  models. That's correct. And I think that's why in a way it links back to the point. And then you're
*  like on this particular use case and the first temptation of if you want to be like pure AI,
*  let's say, is I need to fine tune. Really? Perhaps you can use the genetic model of the shelf
*  and then have another system that does exact matching and then you combine it. So that is
*  the right approach. Perhaps you need to fine tune it, right? It depends on the use case.
*  But at the end of the day, what is important on engineering is not so much the tool. The important
*  thing is the problem. And you just use the tool that is most convenient and you combine different
*  tools. That's the most important thing. Do not fall in love on a particular framework or a
*  particular methodology. What you have to fall in love is with the problem. Yeah, totally.
*  With that in mind, how do you guys approach upgrading technology? I think this is another
*  thing that I'm only starting to get to the point where I'm encountering this in live apps. I have
*  a company called Waymark, which does video generation. And there we've been through several
*  rounds of upgrade of generative models. I haven't got to this point yet on a search,
*  a rag type product where, oh, look, there's a new embedding or there's a new vector database that
*  could support that embedding. I'm sure you've been through several rounds of this stuff over time.
*  How do you approach that challenge and try to tame it? It depends. For instance, on the
*  summarizer, we have this AI summarizer that people can check where we try to provide an answer
*  to a query. It figures for 25%, 30% of the queries. We do rack against ourselves,
*  as anyone would. We do put a lot of emphasis, we can discuss later on that, on the data selection,
*  which snippets we pick and we run narrower QA models on the snippets to fit. But ultimately,
*  we do have a prompt that we send to a large language model. This large language model has
*  changed many times. We had summarizer B1 that was released one year ago. I think we started with
*  plan T5 and then we upgraded to another model after a while. Then we did some fine-tuned version
*  of it. So we did three changes in the course of like two months. Summary B2 was even more extreme
*  because when we released the final model was mixture of 7B, 7-8 billion. Lambda 3 came out
*  two weeks after we tested. We saw that it's actually... We had tests where like compatible
*  quality using myslice resources. We switched it. It took us a week to switch. So on those components
*  it's very easy to switch because you have a test set and you basically change one component for
*  another one. But it doesn't mean that it's generic. For instance, like embeddings,
*  how we change the embeddings? No, not at all. The embeddings is like forever. We have embeddings that
*  the star space embeddings were trained in 2019 and they are still in place and they will never
*  be replaced. What we can do is to actually have more embeddings added to it. And we can have the
*  old system and the new system using new embeddings and yet another system using new embeddings.
*  And then do an ensemble of all. But something that's fundamental of the embedding,
*  you cannot change it. First of all, because the embedding depends on the data and the data
*  is massive, right? To give a concrete number. For example, the content embedding, the dense
*  vectors, which are based on transformers. It takes us, you can do about like 500 pages per
*  second. It means that we pass a page and we get the embedding in two milliseconds.
*  If you work with embeddings or with the formers, you know that actually that's pretty impressive.
*  Yeah, that's fast.
*  That's fast. So in two milliseconds, like fully optimized single GPU, 810G, I guess,
*  that takes one year and a half to do it for the whole data set. So even being extremely fast,
*  it's linked to the data. So you cannot redo it. You do it once and then you build narrower models
*  that are based on those embeddings, on the output of those embeddings. And you build heuristics
*  that combine your part numbers of your branding things. You have narrower models plus heuristics.
*  You cannot change that. What you end up doing is you create like versions of it. You have
*  embeddings V1, embeddings V2, embeddings V3, and you keep adding. And adding is never a problem,
*  right? Because at the end of the day, adding more embeddings is adding more features, adding more
*  distances for the final GVDT that will do the final ranking. So anything that is linked to the data,
*  at least at the scale of a search engine, you don't touch it. Anything that is stateless,
*  like the NLM that does the summary or that does the paraphrasing,
*  then change it then one day for the other. So, hey, we'll continue our interview in a moment
*  after a word from our sponsors. Hey, all. Eric Torenberg here. I'm hearing more and more that
*  founders want to get profitable and do more with less, especially with engineering. Listen,
*  I love your 30-year-old ex-Fang senior software engineer as much as the next guy, but honestly,
*  I can't afford them anymore. Founders everywhere are trying to turn to global talent, but boy,
*  is it a hassle to do at scale from sourcing to interviewing to on the ground operations
*  and management. That's why I teamed up with Sean Lanahan, who's been building engineering teams
*  in Vietnam at a very high level for over five years to help you access global engineering
*  without the headache. Squad, Sean's new company, takes care of sourcing, legal compliance,
*  and local HR for global talent so you don't have to. With teams across Asia and South America,
*  we can cover you no matter which time zone you operate in. Their engineers follow your process
*  and use your tools. They work with React, Next.js, or your favorite front-end frameworks. And on the
*  backend, they're experts at Node, Python, Java, and anything under the sun. Full disclosure,
*  it's going to cost more than the random person you found on Upwork that's doing two hours of work
*  per week but billing you for 40. But you'll get premium quality at a fraction of the typical cost.
*  Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose squad.com and mention Turpentine
*  to skip the wait list. Omniki uses generative AI to enable you to launch hundreds of thousands of
*  ad iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it too. Use Cogrev to
*  get a 10% discount. So I get a couple different follow-ups I want to chase down here. When you
*  say it can never change, do you mean that like outright literally it seems if nothing else,
*  as the world changes, you would need like a new embedding model to understand new developments,
*  right? Yes, but I said that you never change it doesn't mean that you don't add, you can add
*  new things. What I would say is that why do you need to replace one embedding for another one?
*  You actually want to have both of them because most likely they are uncorrelated,
*  and you want to actually build an ensemble of it. Why do you want to end up having like a query
*  document distance? Why do you want to have a distance when you can have two and then
*  use both of them to actually do the final ranking? Embedding features is basically like an additive
*  you don't replace, you just add. The cost of adding is just a matter of resources, right?
*  Because as I told you before, it might take like a month with like many GPUs and actually paying a
*  lot of money to run one embedding second dataset. That's not something that we might actually want
*  to do it every three months, right? Perhaps it will take another year until we have yet another
*  embedding type into the mix. Different products have different questions, that's very important
*  in your case or like the case of the audience. If they have a thousand documents or like 10,000
*  or a million documents, different questions require different solutions.
*  Yeah, definitely. In the plumbing case, I can rerun the whole thing without too much trouble.
*  But in any case, let me reiterate, it's better to have to try 10 embeddings,
*  different models and use an ensemble than to try to find only one embedding that does it perfectly.
*  And your ensemble approach is heuristic, right? It's not, or is that also a learned approach?
*  I can learn that, right? Because at the end of the day, you have, it's like features. At the end of
*  the day, there's essentially a mixture of experts in a way. Of course, a mixture of experts is like
*  another way. It's like another like, it's a really bad, which is the expert is because ensemble is
*  already like, it's already used. But the mixture of experts is just an ensemble of eight different
*  models where two are selected at the time. The same way on your case, which is the best embedding
*  that works for my use case. I would use like five of them. And if they are uncorrelated,
*  which is like the critical factor here, because if they are correlated, they are useless. I mean,
*  they just, they don't add anything, but if they are uncorrelated and if some of them are very
*  semantic, others are more literal, others are like multilingual, others are English, all combined
*  probably will give you a better ranking than using only one. So if I'm understanding the architecture
*  you have today accurately, you have a number of different embeddings that have been built up over
*  time plus a learned combination of those that either, does it like choose which ones to do
*  or does it weight them? Each one gets a scalar. We end up like having, it depends on which search
*  engine because we have multiple search engines depending on what stage you are in, but you're
*  kind of not half pictures, 200 pictures, 300 and then you learn with the gradient addition tree
*  and off you go. Cool. Okay. That's definitely interesting and good food for thought for mine
*  and probably a lot of other projects too. Going back to the topic of upgrading the language model,
*  you said that's like easy in the sense that you can easily swap one in for another.
*  I imagine this is true for both search and the summarizer. It seems much harder to evaluate
*  and actually determine which is the better result. So we've got obviously things like LMSys
*  doing head to head, ELO style, scale AI just came out with a new private thing that they're offering.
*  How do you guys determine which, if you're going to make a change to search, how do you determine
*  if it's an improvement or not? And similarly for the summarizer, how do you go about assessing
*  which is better? We do have a team of human assessors that their work is basically
*  assessed manually. It's not the majority of the search team, but it's a significant chunk of it
*  and their job is basically to have homogeneous methodology and homogeneous criteria to assess.
*  One thing that we don't want to have is intelligent assessments. So this team's work is
*  basically assess of course on the either summary outputs or rankings or FYZ. So that's kind of
*  in a way our ground truth. Of course the productivity is what it is. They cannot
*  produce a lot of assessments, but they are very high quality. And then on the other hand,
*  we have query logs, our own query logs or what we do collect from what discovery project so that
*  allows us to compare what Bing or what Google or what Yandex does. So we use comparison with
*  our competitors in the sense of NGCG or just comparing cardinality of intersection of
*  result set. So if for a certain type of queries we do not match what Google does, then what we do,
*  we check those results and then we manually assess those results, a sample of it, to see
*  what happened. Are we screwing up or we just have a different criteria for this particular set of
*  queries. So this is like the process. It's a combination of a lot of data from ourselves
*  and competitors, not a lot of type, but in a way watching what the others do. That's why also
*  engines can resemble each other in a way because we copy each other. It's not that we copy literally,
*  but we end up using... Your cross-referencing at least.
*  Yeah. Yes, we are cross-referencing. And if we do not return the same as, for example, if we
*  have seen a query empirically in Google on the discovery project, we also compare with ours. If
*  we see an intersection, everything is in the flag. It's odd that this particular query has to know.
*  Then the query is generalized and it's added to the test set. You keep building over time with a
*  lot of patience and a lot of effort. You end up building data sets that have thousands,
*  tens of thousands of high quality human assessment and hundreds of thousands, millions of
*  automatic assessments. Those are what you use as ground truth to evaluate, to see if we are going
*  on the right direction or not. Last and not least, what we also have is some of these queries,
*  we keep them aside from the engineering team in a way. Only the quality team knows them. They have
*  to avoid overfitting because it's a natural thing. Even overfitting is actually a very big problem
*  on machine learning because you can actually have overfitting even without knowing,
*  just by fine tuning the meta-parameter that you have, the cross-referencing.
*  We do have also reset and at the end of the day, it's best effort. We are not that many people
*  and we try to do this gradient descent. If the results are not worse and performance is not worse,
*  we just move ahead. If the performance is worse, then we have to do a juhntent call,
*  whether we actually go for it and optimize later or we just cancel the whole release.
*  How does that differ if at all for the summarizer type experience that comes out of the... Just to
*  set up the context there, the summarizer is... This is something that's both, you can experience
*  it in the UI of search, but then also we're going to shift in a second and talk a little bit about
*  the search API and it's available via both. This is basically, as you said, your rag style experience
*  where, okay, there's all these results, but now can we deliver a synthesis of these results that
*  gets delivered in paragraph explanatory form? Another additional challenge I would imagine there
*  is that there's probably a lot of taste elements to what would even be considered good. Do you have a
*  principle... It's interesting, we've seen the OpenAI model spec recently where they, for the first time,
*  have really started to articulate, this is what we want the model to do. Now we can at least know if
*  it's doing what it's supposed to be doing or if this is by design or not, but I imagine you have
*  to make a bunch of similar choices. Do we want it to be short? Do we want it to be long? That probably
*  varies on context. Do you have a constitution for the summarizer? Not yes, but it's a constitution of
*  one. It's like the person who actually does this and he tries to do the best. Of course, there's
*  some guidelines that are of good taste. We should not be biased. We should try to be as concise as
*  possible. There are certain things that are common sense, but other than that, we do not have
*  time enough to define guardrails or guidelines. We believe that it's more also an iterative process.
*  The fact that we do certain fine tuning from time to time, what helps us is that there are certain
*  results that we think that they are very good. The results will be used to fine tune the model
*  and the model should automatically learn what is the style that we want. Who decides what is
*  good or not, the quality assessment team. Again, we don't have any editorial criteria. That's
*  because we don't say it. We don't play politics. We do not do any censorship or anything like this,
*  but at the end of the day, it's a matter of personal taste of whoever does the rating.
*  But it goes for us. It goes for anyone else. It goes for you. Do you prepare the results from
*  Perplexito, from us, or from Google? The information is actually the same. It's just a style.
*  Yeah. As a power user of all of these things, I have to say, I do find myself going to different
*  services depending on the query. It seems like I've noticed, and I would say, I think Bravest in the
*  middle, I would say right now, between Perplexito gives me a lot of times the shortest, most to
*  the point answer. U.com research mode is on the other extreme where it will give me the two page
*  thousand word. Obviously, that is not suitable for every query. I don't know how you would
*  qualitatively describe where Brave sits in relation to those, but for me, it seems like it
*  would be certainly in the middle of those two. It's in the middle because Brave has an extra
*  complication compared to Perplexito, and we can discuss about that later. But it's a little bit
*  like it might sound very unthoughtful, what I'm going to say, but it's a little bit by chance.
*  Lama 3 is much more verbose than Mixtram. It comes out of being more verbose, period. When
*  we switched to Lama 3, we became more verbose than Mixtram. Of course, we can turn it down a little
*  bit, XYZ, but it's certain inherent things that come out of the tools that you use.
*  And in a way, we do not have the time or the will or know what is right in order for us to actually
*  act upon. And then in those cases, the best thing to do is not try to do nothing.
*  But it sounds stupid, but it's true. If you don't know what is the right thing to do,
*  I basically try to model, period. As simple as that. Once I have more data or I have more
*  resources to do proper assessments and proper judgment, I will try to influence the model.
*  But influencing just because someone on Twitter says something, which is very tempting. So that's
*  one thing. And then on the... It's very interesting what you said about that you use a different
*  system for different queries, because that's not what normal people do. Search is one stop shop.
*  And Brave Search is search. And when people search, they don't want to discover. People
*  search because they have a problem. They want to go to Hotmail or they want to go to porn,
*  or they want to know a recipe of mojito because they are doing the mojito right now. They don't
*  want to discover the two-page history of mojitos or a nice AI summary for mojito. They just want
*  to know the ingredients and how to put it together quickly because you are in the middle of something.
*  And that's important to realize that whenever we think of search, we always think of fancy
*  questions or complex questions that are thoughtful. But most of the queries are not like this.
*  Because we are the default search engine on many countries on the browser, we need to cater
*  to the common denominator in a way. And that's actually something that is tricky,
*  because we could be much fancier if we had no traffic.
*  That mojito example reminds me of... It's almost a meme at this point that all the recipe sites
*  have a long story at the top of the page now. And I'm sure you're familiar with this phenomenon.
*  Right. Why did that happen? Is that something that... Because I would agree,
*  if I'm looking for a mojito recipe, I'm not really looking to read your diary entry of the time that
*  you made these mojitos and how much fun you had. And everybody seems to agree. So where did that
*  come from? SEO. SEO. They run a walk that actually works better. Once somebody learns that, the others
*  copy. It's mostly SEO. But why did it work for SEO? Is that a... Is that sort of a
*  misgeneralization on Google's part? There must be something where more content of this sort is
*  useful and then maybe they overdid it and started to return recipes based on that criteria,
*  even though it's worse. Now you will have to say that. Never underestimate that things can
*  actually happen by accident. So if you do a page that has very good information, but you do it in
*  a format that the parser of Google doesn't like, your content is not going to be indexed in the
*  same way that if you do it on pretext, where the parser for sure gets it. Right. So what you end up
*  doing, again, notice the writer of things that want to be SEO optimized, what they do is an
*  ensemble approach. They try many different things to see what works better against the algorithm.
*  And the algorithm might not be something that is really has a strong rational behind it. It could
*  be that certain types of structure is penalized by accident, just by accident, because that particular
*  thing is not properly parsed. Or because that other thing is like between this tag and this tag
*  made it to the list of things that has an extra boost. And those, according to the leak, Google
*  has 14,000 features per page. I find it a little bit too much, but we have hundreds. So I wouldn't
*  expect that they have thousands. So how do you think this will evolve as we go into a future of just
*  language model generated content everywhere? There's a lot of talk right now about the web is sort of,
*  the hyperbolic take would be like the web is over. It's all going to be overrun by LLM spam.
*  And also people don't want to necessarily be included in training data. So walls are going up
*  in some places. How do you expect the web to change in general and specifically due to those
*  factors? The web has been changing for a long time. The upcoming of advertisement was a change.
*  And blocking has also changed. So everything that is like a change of incentives on the web.
*  And the fact that with AI, not only the economics, which are like pretty,
*  pretty even the reputational aspect of the web might actually go away. That's because if nobody
*  visits your site, you have your podcast. I guess that you make money out of it, but also like for
*  there's some reputational factor to it. If you lose both money and reputation is what, why should
*  they do content for? It's worrisome to say the least. I didn't know what will happen,
*  but certainly the web will change. And I'm a little pessimistic on it. Not only because
*  I like the web, right? I like the web. I'm old enough that I prefer YouTube over Netflix.
*  Even YouTube is full of crap, but it's also full of gems, right? And I like more YouTube than
*  Netflix. I like more MySpace than Facebook, even though, because I like this variety. And I think
*  the AI is not the one who's going to kill it, but is yet another turn towards like a version of the
*  web that is not what I had when I was younger. That doesn't mean that we are worse off as
*  collectively, not necessarily, but I mean, AI answers in a way they are very convenient.
*  And that's why Google is forced to implement them. And in a way that's why also we are forced to
*  implement them. Remember that for us it's not cheap to run a summarizer, right? Because we do
*  have about 27 million of these per day, 30 million. But 10%, 30% of that to be run through an RLM,
*  that's not, that's actually for a lot of places, right? So we are like not forced, but there is
*  pressure to it because people find it very convenient. But anything that is convenient has
*  a price. You sacrifice something for convenience. That's given. On the other extreme, I don't want
*  to like, I don't want to go to the river to fetch water, right? I want water to come out of my tap.
*  But how much convenient, but that's kind of, what is the threshold is, I do not know.
*  But anyway, convenience is king. And answers with AI are here to stay. They are actually very useful
*  and very powerful and very convenient too. But of course, you pay a price. Not only on the
*  ecosystem, but also the variety of answers that we get. Because I think that some of our
*  competition like that answers our knowledge. No, answers are not knowledge. Questions are
*  knowledge. Answers are just answers. So the fact that you have an Oracle kind of type of thing that
*  for anything you ask, it will give you this, that basically means that anything else does not exist.
*  And that's dangerous. Yeah, it does seem like it's going to be a tough time for a lot of the
*  content creators. I'll continue to do the podcast just so I get to talk to leading
*  thinkers like yourself, regardless of whether anyone listens. But it does seem like there's
*  a lot of people out there who are... Oh, and I don't know, like OpenAI had, because they have
*  big pockets they tried to pay. But I don't know if economics actually are, because they
*  call it economics of the advertisement. Yes, Google makes a lot of money. But if you have to
*  split that money equally among all the parts, everybody gets something that is not enough to live.
*  We've been by searching for endless convenience, we commoditized ourselves out of that. I don't
*  know what will happen, honestly. The business side of this work for Brave, I'm just doing a little
*  back of the envelope math and I'm imagining, okay, geez, if you're doing 30 million queries a day,
*  and I don't know how many tokens you're putting in per query, but we can get into a little bit more
*  specifically how much data is returned. But it's not an insignificant amount. It's got to be
*  thousands of tokens per query. It's 4,000 tokens per query usually. We usually max out our context
*  window, which is like 4,000. But it's also forced that we do not use any third party.
*  Not because of the independence part, which would also be because we value that we are independent,
*  but also costs. We would not be able to use OpenAI or do this cost-wise. So
*  everything that we do is self-hosted and we have to pay machines. I think that nobody will
*  complain if I say that, but for instance, right now I think we have 20 hundreds out of Amazon,
*  so that's our infrastructure for the big LLM, plus a lot of GPUs for smaller models, QNAs,
*  and cache files. So it's a big infrastructure, but it's not as massive as many people think.
*  So I guess for now, it's not so expensive that it forces a business model change,
*  because this is something Google's obviously going to be facing in a big way too, right? It's very
*  unclear how, even if you're doing pay-per-click advertising within search, it's very unclear how
*  that fits in with these AI answers. And then more broadly, it's just very unclear how to...
*  Do you guys think of a subscription model in the future for something like this? Or
*  do you have any idea for how this evolves business-wise?
*  It depends. If you enter into the chatbot domain, what you have for back and forth,
*  that is Hansard, then the economics might work differently, right? But if it's on the context
*  of search, where there is query, it may be query reformulation, but there is only one trip,
*  the cost... Let's say that the worst case scenario is double the cost of infrastructure.
*  People tend to over-digitize the new things over the old ones. Yes, running an LLM is very expensive,
*  no question. But it's not like a search engine is super cheap to get with.
*  That's my point. If Google doubles the infrastructure, I'm sure that they can do
*  any LLM, but they won without any issue. And they suddenly have the margins to double the
*  infrastructure. I think that's a cost problem. It's more like, well, we want to do that problem.
*  People actually want to have that. It's very unclear that the majority of people want
*  to have that. With search, it's very... Again, let me go back to the point I said before,
*  once you have traffic and you serve all use cases, right? When they search, they have a problem. They
*  don't want to be stopped because they are in the middle of something. And people don't usually
*  remember good cases. They only remember bad ones. So you don't go to that particular shop
*  because they treat you wrong once. You go to the other one because on average, they treat you right
*  most of the time. You avoid... You don't reward the place. You literally punish
*  the one that you don't like. So if you start to do certain experiments, if you have a lot of users,
*  you risk getting a lot of users because they don't like what you're offering because it's in the way.
*  You are annoying them. And that's why, again, without traffic, you can do many things.
*  Or with a very small traffic, or with a traffic that is of a very particular segment of population,
*  you can do many things. But once you have the general public and your service is like running
*  water, you open the tap and you don't have the luxury of doing a lot of innovation there. And
*  actually, Google is suffering. I pity them, honestly, in the sense that it's a very big thing
*  what they have to do. And we have a much easier program than Google has to react to LLMs. And
*  you don't know our complexity or tagging have a much better position than where we are, right?
*  Because they have less community. So like a blank slate for the wind. It's always okay, right?
*  What's your user base look like? I know that obviously we're speaking in English, but you're
*  from Spain and others are... The company's headquartered in Europe, correct?
*  No, Brave is headquartered in the US. Search is 100% Europe. There is only people in Europe and
*  some people in Africa. All the same time. But all search is EU based. But Brave is an American
*  company, but it's heavily remote. How the people... Maybe a more general purpose question would be,
*  again, where are Brave users? And I wonder if you see differences cross-culturally in how people
*  are responding to the AI moment? How would you characterize how consumers are reacting to
*  AI experiences in Europe as opposed to in the United States?
*  No, we have not done this analysis. Brave search users is actually a good sample of the
*  world population. About 30% of the people are in the US. The next big market is already in Europe.
*  So we are pretty well spread across all continents. They've got no odd countries or
*  behaviors. It's large enough to be statistically well distributed.
*  My intuition would be that I'd maybe be more interested in the summary just because less...
*  Fewer of the sites are mobile optimized and it's just more hassle to browse around.
*  It could be. But at the same time, when you're on desktop, you also would expect to have more
*  work related difficult queries. Because on mobile queries, usually they are very instrumental. They
*  are very like a phone number of restaurant. Or like a fan fact. Again, age of Lady Gaga.
*  If you like playing the trivia, come forward with friends.
*  Let's maybe turn to the search API. This is an area of the business where there is a very
*  natural business model. This has been the main subject of the ad as well that we've been running.
*  I went ahead and created a little Google collab notebook that allows a user to easily
*  show up and try the Brave API as compared to the Google Custom Search API and then also the Bing
*  Search API. I have a few observations that I would be happy to share. But maybe you should
*  start by just telling us how do you see the product as being differentiated from the other
*  options that probably a lot of people are more familiar with.
*  The reason why we released the search API is to provide an alternative to Big Tech. As far as we
*  know, there are only two APIs out there. The search engine, Google and Microsoft. Google is not
*  public. I think you used the Custom Search from Google. That's not meant to actually be used in
*  production. I think they have a cap of 10,000 queries. So if you actually want to use Google
*  API for something real, you actually have to go to talk to them and they might give you access
*  or not. It's their own decision. On the other hand, it's a little bit better in that respect
*  because they have a public API. Of course, you pay, but it's public. You go there, you accept the
*  term of service, which is a little conian, but that's a different topic. But you pay and then
*  you use. That's it. Brave says what we try to do is the same as being an API. It's a public API.
*  You pay, you can use it, no questions asked. We try to be less conian on the terms of service.
*  We do not require attribution. We allow for you to mix your results the way you want.
*  Things that Brave would not allow. But other than that, again, there is nothing else other
*  than before you only had Microsoft. Now you have Brave and Microsoft. That's not a small thing.
*  We did that the very moment we actually could launch the API, we did because we're not 100%
*  independent all the way. When we launched Brave Search, we were able to answer 87% of the queries.
*  For the remainder, 13%, we actually used Bing. We skipped that over the month. We went from 87,
*  three months after it was 90, 92, 93, 94, and a little more than a year ago, we went from 96 or 97.
*  We went back to there to be totally independent from Bing. At that moment, we could offer the API
*  because before it was not possible because of the terms of service of Bing.
*  Yeah, that's interesting. I would agree definitely with the idea that the Google
*  custom search API is not really a competitor.
*  It's meant to do site search.
*  Like your own site?
*  Yeah, actually, I'm pretty sure that you can do the trick and not pass
*  domains so that it doesn't do site search. It does global search, but I'm pretty sure that it
*  goes against the terms of service. In any case, it's limited to 10,000 queries per day.
*  The thing that stood out to me the most, and folks can go judge this for themselves with our
*  Collab Notebook, which I'll put in the show notes, is really more than anything else,
*  just more information being returned. In my case with Weymark, for example,
*  we have this flow where a new user shows up. I'm always amazed that so few products implement
*  something like this because it's worked really well for us. New user shows up, they want to make a
*  video for their business. They typically don't have a ready-to-go folder of all their assets,
*  let alone a good profile of their business.
*  Now we're going to use generative AI to put things together for them, but we need to know,
*  who are you? Tell us about your business. What do you offer? What makes you special? Do you
*  have any images that we can feature? People just don't have that stuff. Most products
*  just require you to make a profile and upload your images and whatever.
*  We have worked pretty hard over the years to create a good experience where we go grab that
*  content off the web for you. As you'd imagine, the generative AI era here has really improved
*  how well that works. We have used Google Custom Search for that. Our volume is not super high,
*  and we're mostly just trying to get their homepage or then we'll maybe bounce a few links off of that.
*  But I am going to look more deeply into using Brave for this use case in particular because
*  just more information really jumps out at me. We get a snippet from the Google Custom Search
*  and with the Brave results, you get often a much deeper cut with multiple snippets and even some
*  structured data for some results. I looked at this a few different ways, but in just raw characters
*  returned for a 10 result query, the volume of data was often a multiple higher than what I was getting
*  with Bing and Google. That also extends down. You could fill out characters with anything,
*  but a lot of that seems to come from these additional snippets, which for us are really
*  useful. We right now first run that query and then we go crawl ourselves and then we pull all that
*  stuff in and then we run our own language model to process it and turn it into a profile that we can
*  then feed downstream into the actual generation task. But I could definitely see us simplifying a
*  lot of things and that's always nice to take multiple steps and condense them into one
*  if we just could get that multiple snippets alone, I think would be a pretty notable enhancement.
*  That's before the summarizer too, which is something I also could see us doing because again,
*  we're doing that ourselves today and you've implemented that whole thing. I'll have to check
*  the coverage for our small businesses because some of our customers are pretty long tail.
*  They're generally not super famous businesses. But for me, a volume of information was the biggest
*  thing that jumped out. Would you expand on that anymore?
*  We did not have the motivation to provide more volume per se because again, remember that
*  the amount of data is meaningless. Sorry, the amount of data is very important as long as there
*  is no noise because if you actually just the risk of adding noise precludes any amount of data that
*  you can provide. So our rationale was the following is like we because we do the dynamic
*  snippet generation query depending, right? We end up having multiple candidates that we ran through
*  a Q&A model. That's a cost that will be paid. So as long as that is above a certain threshold,
*  which means that in principle there should not be noise, actually why we should not send it to the
*  user so that they can have the choice to decide which snippet they want to show or in the case
*  that they want to do an LN inference to have a little more data to fit the prompt or to cherry
*  pick because cherry picking is actually very important and the topic of summarizer.
*  The secret sauce of our summarizer is not the model, the LN. Again, we changed it from mixture
*  to LN in a heartbeat is a cherry picking of which data we feed the prompt. That's what we spent the
*  time on like only feeding like non-repeated non-procure vector information. So we do a lot
*  of pre-processing. Anyway, so hopefully like on the API, what we try to offer is we give you like
*  all the elements so that you can innovate on top of it. That's like our goal. Of course,
*  we want to make money out of it too, right? So if it has more value than being, also it's also good
*  because we will have more users. But anyway, it's not like one or the other. You can have
*  both reasons at the same time, right? It is notably significantly cheaper than
*  Bing as well. You have multiple different tiers of service for different amounts of data that get
*  returned and somewhat different like price points for different licensing as well. And there's
*  whether you're going to be able to store the data or not. So folks can get into the different price
*  points. But Bing also has a lot of different price points. And at least for me, when I was looking at
*  what I would naturally want to use, including the summarizer, that is a $9 per thousand queries
*  price point with Brave. And with Bing, I would say the most comparable thing, they didn't even
*  really have that summarizer feature at all, but the most comparable price point that returns like
*  the varied results where you might get like video results or different kinds of discussion type
*  pages is a $25 per thousand price point. So saving more than 60%. And I would say getting
*  more both in terms of the additional snippets, the extra information and the ability to tap into that
*  summarizer. Anything else that I should be conscious of as I think about the right option for my app?
*  No, the right option for your app is like whatever works and if you can afford all data combined and
*  do an example out of it. But no, it's like, I mean, we are very happy with the Search API and it's not
*  just that it's one of the, it's actually, it's a satisfaction from us when we talk to a customer
*  and they say that it's about time that there was an alternative to Bing. That's actually for us is
*  very, it's like very rewarding to be able to achieve that goal. You might use Bing, you might
*  use Google on our private deal, you might use whatever, right? But like the fact that
*  you have more and more to choose, that's a big deal for us.
*  You want to shout out any customers that are using the Search API that folks can go check
*  out if they want to see a good implementation?
*  Oh, we. I wouldn't be able to play favorites because actually there are two things here.
*  There is the vast majority of our customers do not allow us to mention them. It's a very
*  competitive space. Many of the big players do not want to admit or let others know that they have
*  or that they use a search or any other system. And then for the one who actually acknowledged
*  that it would be kind of unfair to single out one. But I can tell you like some nice
*  use cases. Of course, it is like plenty of rack use cases that are being done by names that have
*  been mentioned before. It has also been used by to train significant foundational models.
*  One use case that I find very interesting is that it's also being used to do grounding
*  of LLM outputs and LLM output. And you actually run it, you submit it, you run it against a search
*  engine to try to verify whether the output is legitimate or not. So there is like a lot of
*  and many other use cases that we do not know. Or because at the end of the day, we do not,
*  unless they ping us, we do not ask questions. We use it and hopefully it's beneficial for
*  both of us. Are there any favorite technology
*  compliments that you would almost like in a cookbook or demo showcase sort of way? Are there
*  things that patterns of development that you've seen where people have combined the Brave Search
*  API with some other framework, technology, user experience that you think is worth
*  sharing just to inspire people? Yeah, there is like this, I don't know how old it is.
*  There was one guy who actually did a YouTube video and I think it is on GitHub too. They like
*  to build a complexity clone using the Lanchain, Brave, Croc. So he did like a whole convolution of
*  APIs and he actually built like a very nice prototype. I think it's good to get the idea
*  of like why the things sit together and then people can decide what to do to go deeper.
*  Cool. You've been very generous with your time. Anything else that we haven't touched on that
*  you want to make sure we cover? No, I think that I really talked too much. So hopefully I did not
*  bore your audience with my ramblings. It's been a pleasure. Very nice course. I appreciate the chat.
*  Cool. The feeling is mutual. Joseph Pujol, thank you for being part of the Cognitive Revolution.
*  Thank you. Bye-bye. It is both energizing and enlightening to hear why people listen
*  and learn what they value about the show. So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media platform of your choice.
