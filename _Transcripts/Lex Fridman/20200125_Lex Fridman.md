---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 5452s
Video Keywords: ['cristos goodrow', 'youtube', 'youtube algorithm', 'google', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 52466
Video Rating: None
Video Description: Cristos Goodrow is VP of Engineering at Google and head of Search and Discovery at YouTube (aka YouTube Algorithm).

This episode is presented by Cash App. Download it & use code "LexPodcast":
Cash App (App Store): https://apple.co/2sPrUHe
Cash App (Google Play): https://bit.ly/2MlvP5w

PODCAST INFO:
Podcast website:
https://lexfridman.com/podcast
Apple Podcasts:
https://apple.co/2lwqZIr
Spotify:
https://spoti.fi/2nEwCF8
RSS:
https://lexfridman.com/feed/podcast/
Full episodes playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

OUTLINE:
0:00 - Introduction
3:26 - Life-long trajectory through YouTube
7:30 - Discovering new ideas on YouTube
13:33 - Managing healthy conversation
23:02 - YouTube Algorithm
38:00 - Analyzing the content of video itself
44:38 - Clickbait thumbnails and titles
47:50 - Feeling like I'm helping the YouTube algorithm get smarter
50:14 - Personalization
51:44 - What does success look like for the algorithm?
54:32 - Effect of YouTube on society
57:24 - Creators
59:33 - Burnout
1:03:27 - YouTube algorithm: heuristics, machine learning, human behavior
1:08:36 - How to make a viral video?
1:10:27 - Veritasium: Why Are 96,000,000 Black Balls on This Reservoir?
1:13:20 - Making clips from long-form podcasts
1:18:07 - Moment-by-moment signal of viewer interest
1:20:04 - Why is video understanding such a difficult AI problem?
1:21:54 - Self-supervised learning on video
1:25:44 - What does YouTube look like 10, 20, 30 years from now?

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Cristos Goodrow YouTube Algorithm  Lex Fridman Podcast #68
**Lex Fridman:** [January 25, 2020](https://www.youtube.com/watch?v=nkWmiNRPU-c)
*  The following is a conversation with Christos Goodro, Vice President of Engineering at Google
*  and Head of Search and Discovery at YouTube, also known as the YouTube Algorithm.
*  YouTube has approximately 1.9 billion users and every day people watch over 1 billion hours of
*  YouTube video. It is the second most popular search engine behind Google itself. For many people,
*  it is not only a source of entertainment, but also how we learn new ideas from math and physics
*  videos to podcasts to debates, opinions, ideas from out of the box thinkers and activists on some
*  of the most tense, challenging, and impactful topics in the world today. YouTube and other
*  content platforms receive criticism from both viewers and creators, as they should, because the
*  engineering task before them is hard and they don't always succeed, and the impact of their
*  work is truly world-changing. To me, YouTube has been an incredible wellspring of knowledge.
*  I've watched hundreds, if not thousands of lectures that change the way I see many fundamentals,
*  ideas in math, science, engineering, and philosophy. But it does put a mirror to ourselves
*  and keeps the responsibility of the steps we take in each of our online educational journeys
*  into the hands of each of us. The YouTube algorithm has an important role in that journey
*  of helping us find new exciting ideas to learn about. That's a difficult and an exciting problem
*  for an artificial intelligence system. As I've said in lectures and other forums,
*  recommendation systems will be one of the most impactful areas of AI in the 21st century,
*  and YouTube is one of the biggest recommendation systems in the world.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  give it 5 stars on Apple Podcasts, follow on Spotify, support it on Patreon,
*  or simply connect with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N.
*  I recently started doing ads at the end of the introduction. I'll do one or two minutes
*  after introducing the episode and never any ads in the middle that can break the flow of the
*  conversation. I hope that works for you and doesn't hurt the listening experience.
*  This show is presented by Cash App, the number one finance app in the app store.
*  I personally use Cash App to send money to friends, but you can also use it to buy,
*  sell, and deposit bitcoin in just seconds. Cash App also has a new investing feature.
*  You can buy fractions of a stock, say $1 worth, no matter what the stock price is.
*  Broker services are provided by Cash App Investing, a subsidiary of Square and member SIPC.
*  I'm excited to be working with Cash App to support one of my favorite organizations called FIRST,
*  best known for their FIRST Robotics and Lego competitions. They educate and aspire hundreds
*  of thousands of students in over 110 countries and have a perfect rating at Charity Navigator,
*  which means that donated money is used to maximum effectiveness. When you get Cash App from the app
*  store or Google Play and use code LEXPODCAST, you'll get $10 and Cash App will also donate
*  $10 to FIRST, which again is an organization that I've personally seen inspire girls and boys to
*  dream of engineering a better world. And now here's my conversation with Christos Goodrow.
*  YouTube is the world's second most popular search engine, behind Google of course.
*  We watch more than 1 billion hours of YouTube videos a day, more than Netflix and Facebook
*  video combined. YouTube creators upload over 500,000 hours of video every day.
*  Average lifespan of a human being, just for comparison, is about 700,000 hours.
*  So what's uploaded every single day is just enough for a human to watch in a lifetime.
*  So let me ask an absurd philosophical question. If from birth, when I was born,
*  and there's many people born today with the internet, I watched YouTube videos nonstop,
*  do you think there are trajectories through YouTube video space that can maximize my average
*  happiness or maybe education or my growth as a human being? I think there are some great
*  trajectories through YouTube videos, but I wouldn't recommend that anyone spend all of
*  their waking hours or all of their hours watching YouTube. I mean, I think about the fact that
*  YouTube has been really great for my kids, for instance. My oldest daughter,
*  she's been watching YouTube for several years. She watches Tyler Oakley and the Vlogbrothers.
*  I know that it's had a very profound and positive impact on her character. My younger daughter,
*  she's a ballerina and her teachers tell her that YouTube is a huge advantage for her because she
*  can practice a routine and watch professional dancers do that same routine and stop it and
*  back it up and rewind and all that stuff. So it's been really good for them. Then even my son,
*  as a sophomore in college, he got through his linear algebra class because of a channel called
*  3Blue1Brown, which helps you understand linear algebra, but in a way that would be very hard for
*  anyone to do on a whiteboard or a chalkboard. So I think that those experiences, from my point of
*  view, were very good. So I can imagine really good trajectories through YouTube, yes.
*  Have you looked at, do you think broadly about that trajectory over a period? Because YouTube
*  has grown up now. So over a period of years, you just kind of gave a few anecdotal examples. But
*  I used to watch certain shows on YouTube I don't anymore. I've moved on to other shows.
*  Ultimately, you want people to, from YouTube's perspective, to stay on YouTube, to grow as human
*  beings on YouTube. So you have to think not just what makes them engage today or this month,
*  but also over a period of years. Absolutely. That's right. I mean, if YouTube is going to
*  continue to enrich people's lives, then it has to grow with them and people's interests change over
*  time. And so I think we've been working on this problem, and I'll just say it broadly as like,
*  how to introduce diversity and introduce people who are watching one thing to something else they
*  might like. We've been working on that problem all the eight years I've been at YouTube.
*  It's a hard problem because, I mean, of course, it's trivial to introduce diversity that doesn't
*  help. Yeah, just add a random video. I could just randomly select a video from the billions that we
*  have. It's likely not to even be in your language. So the likelihood that you would watch it and
*  develop a new interest is very, very low. And so what you want to do when you're trying to increase
*  diversity is find something that is not too similar to the things that you've watched,
*  but also something that you might be likely to watch. And that balance, finding that spot
*  between those two things is quite challenging. So the diversity of content, diversity of ideas,
*  it's a really difficult, it's the thing like that's almost impossible to define, right? Like,
*  what's different? So how do you think about that? So two examples is, I'm a huge fan of
*  ThreeBlueOneBrown, say, and then one diversity, I wasn't even aware of a channel called Veritasium,
*  which is a great science, physics, whatever channel. So one version of diversity is showing me
*  Derek's Veritasium channel, which I was really excited to discover actually, and I watched a
*  lot of his videos. Okay, so you're a person who's watching some math channels, and you might be
*  interested in some other science or math channels. So like you mentioned, the first kind of diversity
*  is just show you some things from other channels that are related, but not just, you know, not all
*  the ThreeBlueOneBrown channel, throw in a couple others. So that's maybe the first kind of diversity
*  that we started with many, many years ago. Taking a bigger leap is about, I mean, the mechanisms
*  we use for that is we basically cluster videos and channels together, mostly videos. We do
*  almost everything at the video level, and so we'll make some kind of a cluster via some embedding
*  process, and then measure, you know, what is the likelihood that users who watch one cluster
*  might also watch another cluster that's very distinct. So we may come to find that people
*  who watch science videos also like jazz. This is possible, right? And so because of that relationship
*  that we've identified through the embeddings and then the measurement of the people who watch both,
*  we might recommend a jazz video once in a while. So there's this clustering in the embedding space
*  of jazz videos and science videos. And so you kind of try to look at aggregate statistics where
*  if a lot of people that jump from science cluster to the jazz cluster tend to remain
*  as engaged or become more engaged, then that means those two are, they should hop back and forth and
*  they'll be happy. Right. There's a higher likelihood that a person from who's watching
*  science would like jazz than the person watching science would like, I don't know, backyard railroads
*  or something else. Right. And so we can try to measure these likelihoods and use that to
*  make the best recommendation we can. So, okay. So we'll talk about the machine learning of that,
*  but I have to linger on things that neither you or anyone have an answer to. There's gray areas
*  of truth, which is, for example, now I can't believe I'm going there, but politics,
*  it happens so that certain people believe certain things and they're very certain about them.
*  Let's move outside the red versus blue politics of today's world, but there's different ideologies.
*  For example, in college, I read quite a lot of Ayn Rand I studied and that's a particular
*  philosophical ideology. I found it interesting to explore. Okay. So that was that kind of space.
*  I've kind of moved on from that cluster intellectually, but it nevertheless is an
*  interesting cluster. I was born in the Soviet Union. Socialism, communism is a certain kind
*  of political ideology that's really interesting to explore. Again, objectively, there's a set of
*  beliefs about how the economy should work and so on. And so it's hard to know what's true or not
*  in terms of people within those communities are often advocating that this is how we achieve
*  utopia in this world and they're pretty certain about it. So how do you try to
*  manage politics in this chaotic, divisive world, not positive or any kind of ideas in terms of
*  filtering what people should watch next and in terms of also not letting certain things be on
*  YouTube? This is exceptionally difficult responsibility. Well, the responsibility to
*  get this right is our top priority. And the first comes down to making sure that we have good,
*  clear rules of the road. Just because we have freedom of speech doesn't mean that you can
*  literally say anything. We as a society have accepted certain restrictions on our freedom
*  of speech. There are things like libel laws and things like that. And so where we can draw a clear
*  line, we do and we continue to evolve that line over time. However, as you pointed out, wherever
*  you draw the line, there's going to be a borderline. And in that borderline area, we are going to maybe
*  not remove videos, but we will try to reduce the recommendations of them or the proliferation of
*  them by demoting them. And then alternatively, in those situations, try to raise what we would
*  call authoritative or credible sources of information. So we're not trying to... I mean,
*  you mentioned Ayn Rand and communism. Those are two valid points of view that people are going to
*  debate and discuss. And of course, people who believe in one or the other of those things are
*  going to try to persuade other people to their point of view. And so we're not trying to settle
*  that or choose a side or anything like that. What we're trying to do is make sure that the
*  people who are expressing those point of view and offering those positions are authoritative and
*  credible. So let me ask a question about people I don't like personally. You heard me. I don't care
*  if you leave comments on this. But sometimes they're brilliantly funny, which is trolls.
*  So people who kind of mock... I mean, the internet is full. We read it of mock-style comedy where
*  people just kind of make fun of... Point out that the emperor has no clothes. And there's
*  brilliant comedy in that, but sometimes it can get cruel and mean. So on that, on the mean point,
*  and sorry to linger on these things that have no good answers, but actually, I totally hear you
*  that this is really important and you're trying to solve it. But how do you reduce the meanness
*  of people on YouTube? I understand that anyone who uploads YouTube videos has to become resilient
*  to a certain amount of meanness. I've heard that from many creators and we are trying in various
*  ways, comment ranking, allowing certain features to block people, to reduce or make that meanness
*  or that trolling behavior less effective on YouTube. And so, I mean, it's very important,
*  but it's something that we're going to keep having to work on. And as we improve it,
*  maybe we'll get to a point where people don't have to suffer this sort of meanness when they
*  upload YouTube videos. I hope we do, but it just does seem to be something that you have to
*  be able to deal with as a YouTube creator nowadays. Do you have a hope that... So you mentioned two
*  things that I kind of agree with. So there's like a machine learning approach of ranking
*  comments based on how much they contribute to the healthy conversation. Let's put it that way.
*  And the other is almost an interface question of how does the creator filter? So block or...
*  How do humans themselves, the users of YouTube, manage their own conversation? Do you have hope
*  that these two tools will create a better society without limiting freedom of speech too much?
*  Without even saying that, people are like, what do you mean limiting, sort of curating speech?
*  I mean, I think that that overall is our whole project here at YouTube. We fundamentally believe,
*  and I personally believe very much, that YouTube can be great. It's been great for my kids. I think
*  it can be great for society, but it's absolutely critical that we get this responsibility part
*  right. And that's why it's our top priority. Susan Wojcicki, who's the CEO of YouTube,
*  she says something that I personally find very inspiring, which is that we want to do our jobs
*  today in a manner so that people 20 and 30 years from now will look back and say, YouTube, they
*  really figured this out. They really found a way to strike the right balance between the openness
*  and the value that the openness has, and also making sure that we are meeting our responsibility
*  to users and society. So the burden on YouTube actually is quite incredible. And the one thing
*  that people don't give enough credit to the seriousness and the magnitude of the problem,
*  I think. So I personally hope that you do solve it because a lot is in your hands.
*  A lot is riding on your success or failure. So it's besides, of course, running a successful
*  company, you're also curating the content of the internet and the conversation on the internet.
*  That's a powerful thing. So one thing that people wonder about is how much of it can be solved with
*  pure machine learning. So looking at the data, studying the data, and creating algorithms that
*  curate the comments, curate the content, and how much of it needs human intervention, meaning
*  people here at YouTube in a room sitting and thinking about what is the nature of truth?
*  What are the ideals that we should be promoting? That kind of thing.
*  So algorithm versus human input. What's your sense?
*  My own experience has demonstrated that you need both of those things.
*  You're familiar with machine learning algorithms, and the thing they need most is data. And the data
*  is generated by humans. And so for instance, when we're building a system to try to figure out
*  which are the videos that are misinformation or borderline policy violations, well, the first
*  thing we need to do is get human beings to make decisions about which of those videos are in which
*  category. And then we use that data and basically take that information that's determined and
*  governed by humans and extrapolate it or apply it to the entire set of billions of YouTube videos.
*  And we couldn't get to all the videos on YouTube well without the humans, and we couldn't use the
*  humans to get to all the videos of YouTube. So there's no world in which you have only one or
*  the other of these things. And just as you said, a lot of it comes down to people at YouTube
*  spending a lot of time trying to figure out what are the right policies, what are the outcomes
*  based on those policies, are they the kinds of things we want to see? And then once we kind of
*  get an agreement or build some consensus around what the policies are, well, then we've got to
*  find a way to implement those policies across all of YouTube. And that's where both the human
*  beings, we call them evaluators or reviewers come into play to help us with that. And then once we
*  get a lot of training data from them, then we apply the machine learning techniques to take it
*  even further. Do you have a sense that these human beings have a bias in some kind of direction?
*  I mean, that's an interesting question. We do sort of in autonomous vehicles and computer vision in
*  general, a lot of annotation, and we rarely ask what bias do the annotators have, even in the sense
*  that they're better at annotating certain things than others. For example, people are much better
*  at annotating segmentation at segmenting cars in a scene versus segmenting bushes or trees.
*  You know, there's specific mechanical reasons for that, but also because it's a semantic gray area
*  and just for a lot of reasons, people are just terrible at annotating trees. Okay, so in the same
*  kind of sense, do you think of in terms of people reviewing videos or annotating videos, do you think
*  of in terms of people reviewing videos or annotating the content of videos, is there some kind of bias
*  that you're aware of or seek out in that human input? Well, we take steps to try to overcome
*  these kinds of biases or biases that we think would be problematic. So for instance, like,
*  we ask people to have a bias towards scientific consensus. That's something that we
*  instruct them to do. We ask them to have a bias towards demonstration of expertise or credibility
*  or authoritativeness, but there are other biases that we want to make sure to try to remove.
*  And there's many techniques for doing this. One of them is you send the same thing to be reviewed
*  to many people. And so, you know, that's one technique. Another is that you make sure that
*  the people that are doing these sorts of tasks are from different backgrounds and different areas of
*  the United States or of the world. But then even with all of that, it's possible for certain kinds
*  of what we would call unfair biases to creep into machine learning systems, primarily, as you said,
*  because maybe the training data itself comes in in a biased way. And so, we also have worked very
*  hard on improving the machine learning systems to remove and reduce unfair biases when it's
*  goes against or is involved some protected class, for instance. Thank you for exploring
*  with me some of the more challenging things. I'm sure there's a few more that we'll jump back to,
*  but let me jump into the fun part, which is maybe the basics of the quote unquote YouTube algorithm.
*  What does the YouTube algorithm look at to make recommendation for what to watch next?
*  And it's from a machine learning perspective or when you search for a particular term,
*  how does it know what to show you next? Because it seems to, at least for me,
*  do an incredible job of both. Well, that's kind of you to say. It didn't used to do a very good job,
*  but it's gotten better over the years. Even I observed that it's improved quite a bit.
*  Those are two different situations. When you search for something, YouTube uses the best
*  technology we can get from Google to make sure that the YouTube search system finds what someone's
*  looking for. And of course, the very first things that one thinks about is, okay, well,
*  does the word occur in the title, for instance? But there are much more sophisticated things
*  where we're mostly trying to do some syntactic match or maybe a semantic match based on
*  words that we can add to the document itself. For instance, maybe is this video watched a lot
*  after this query? That's something that we can observe and then as a result, make sure that
*  document would be retrieved for that query. Now, when you talk about what kind of videos
*  would be recommended to watch next, that's something again, we've been working on for
*  many years. And probably the first real attempt to do that well was to use collaborative filtering.
*  Can you describe what collaborative filtering is?
*  Sure. Basically, what we do is we observe which videos get watched close together by the same
*  person. And if you observe that and if you can imagine creating a graph where the videos that
*  get watched close together by the most people are very close to one another in this graph and
*  videos that don't frequently get watched close together by the same person or the same people
*  are far apart, then you end up with this graph that we call the related graph that basically
*  represents videos that are very similar or related in some way. And what's amazing about that
*  is that it puts all the videos that are in the same language together, for instance. And we
*  didn't even have to think about language. It just does it. And it puts all the videos that are about
*  sports together and it puts most of the music videos together and it puts all of these sorts
*  of videos together just because that's sort of the way the people using YouTube behave.
*  So that already cleans up a lot of the problem. It takes care of the lowest hanging fruit,
*  which happens to be a huge one of just managing these millions of videos.
*  That's right. I remember a few years ago I was talking to someone who was
*  trying to propose that we do a research project concerning people who are bilingual.
*  And this person was making this proposal based on the idea that YouTube could not possibly be good
*  at recommending videos well to people who are bilingual. And so she was telling me about this
*  and I said, well, can you give me an example of what problem do you think we have on YouTube with
*  the recommendations? And so she said, well, I'm a researcher in the US and when I'm looking for
*  academic topics, I want to see them in English. And so she searched for one, found a video,
*  and then looked at the watch next suggestions and they were all in English. And so she said,
*  oh, I see, YouTube must think that I speak only English. And so she said, now, I'm actually
*  originally from Turkey and sometimes when I'm cooking, let's say I want to make some baklava,
*  I really like to watch videos that are in Turkish. And so she searched for a video about making the
*  baklava and then selected it. It was in Turkish and the watch next recommendations were in Turkish.
*  And she just couldn't believe how this was possible. And how is it that you know that
*  I speak both these two languages and put all the videos together? And it's just as a sort of an
*  outcome of this related graph that's created through collaborative filtering. So for me,
*  one of my huge interests is just human psychology, right? And that's such a powerful platform on which
*  to utilize human psychology to discover what people, individual people want to watch next.
*  But it's also be just fascinating to me. You know, I've Google search has ability to look
*  at your own history. And I've done that before. Just just what I've searched three years for many,
*  many years. And it's fascinating picture of who I am, actually. And I don't think anyone's ever
*  summarized. I personally would love that a summary of who I am as a person on the internet to me,
*  because I think it reveals I think it puts a mirror to me or to others. You know, that's
*  actually quite revealing and interesting. You know, just maybe the number of it's a joke, but
*  not really is the number of cat videos I've watched videos of people falling, you know, stuff
*  that's absurd. That kind of stuff. It's really interesting. And of course, it's really good for
*  the machine learning aspect to to show to figure out what to show next. But it's interesting.
*  Have you just as a tangent played around with the idea of giving a map to people
*  sort of as opposed to just using this information to show us next, showing them
*  here are the clusters you've loved over the years kind of thing?
*  Well, we do provide the history of all the videos that you've watched. Yes. So you can
*  definitely search through that and look through it and search through it to see what it is that
*  you've been watching on YouTube. We have actually in various times experimented with this sort of
*  cluster idea, finding ways to demonstrate or show people what topics they've been interested in or
*  what clusters they've watched from. It's interesting that you bring this up because
*  in some sense, the way the recommendation system of YouTube sees a user is exactly as
*  the history of all the videos they've watched on YouTube. And so you can think of yourself or
*  any user on YouTube as kind of like a DNA strand of all your videos, right? That sort of represents
*  you. You can also think of it as maybe a vector in the space of all the videos on YouTube.
*  And so now once you think of it as a vector in the space of all the videos on YouTube,
*  then you can start to say, okay, well, which other vectors are close to me
*  to my vector? And that's one of the ways that we generate some diverse recommendations is
*  because you're like, okay, well, these people seem to be close with respect to the videos
*  they've watched on YouTube, but here's a topic or a video that one of them has watched and enjoyed,
*  but the other one hasn't. That could be an opportunity to make a good recommendation.
*  I got to tell you, I know I'm going to ask for things that are impossible, but
*  I would love to cluster than human beings. I would love to know who has similar trajectories
*  as me, because you probably would want to hang out. There's a social aspect there.
*  Actually finding some of the most fascinating people I find on YouTube have no followers,
*  and I start following them and they create incredible content. And on that topic, I just
*  love to ask, there's some videos that just blow my mind in terms of quality and depth, and just
*  in every regard are amazing videos and they have like 57 views. Okay. How do you get videos
*  of quality to be seen by many eyes? So the measure of quality, is it just something?
*  Yeah. How do you know that something is good? Well, I mean, I think it depends initially on
*  what sort of video we're talking about. So in the realm of, let's say you mentioned politics and
*  news, in that realm, quality news or quality journalism relies on having a journalism
*  department. You have to have actual journalists and fact checkers and people like that.
*  And so in that situation and in others, maybe science or in medicine, quality has a lot to do
*  with the authoritativeness and the credibility and the expertise of the people who make the video.
*  Now, if you think about the other end of the spectrum, what is the highest quality prank video
*  or what is the highest quality Minecraft video? That might be the one that people enjoy
*  watching the most and watch to the end, or it might be the one that when we ask people the next day,
*  after they watched it, were they satisfied with it? And so we, especially in the realm of
*  entertainment, have been trying to get at better and better measures of quality or satisfaction
*  or enrichment since I came to YouTube. And we started with, well, the first approximation is
*  the one that gets more views. But we both know that things can get a lot of views
*  and not really be that high quality, especially if people are clicking on something and then
*  immediately realizing that it's not that great and abandoning it. And that's why we move from views
*  to thinking about the amount of time people spend watching it with the premise that, in some sense,
*  the time that someone spends watching a video is related to the value that they get from that video.
*  It may not be perfectly related, but it has something to say about how much value they get.
*  But even that's not good enough, right? Because I myself have spent time clicking through channels
*  on television late at night and ended up watching Under Siege 2 for some reason I don't know.
*  And if you were to ask me the next day, are you glad that you watched that show on TV last night,
*  I'd say, yeah, I wish I would have gotten to bed or read a book or almost anything else, really.
*  And so that's why some people got the idea a few years ago to try to survey users afterwards.
*  And so we get feedback data from those surveys and then use that in the machine learning system to
*  try to not just predict what you're going to click on right now, what you might watch for a while,
*  but what when we ask you tomorrow, you'll give four or five stars to.
*  So just to summarize, what are the signals from a machine learning perspective that the user can
*  provide? So you mentioned just clicking on the video views, the time watched, maybe the relative
*  time watched, the clicking like and dislike on the video, maybe commenting on the video.
*  All of those things.
*  All of those things. And then the one I wasn't actually quite aware of, even though I might have
*  engaged in it, is a survey afterwards, which is a brilliant idea. Is there other signals?
*  I mean, that's already a really rich space of signals to learn from. Is there something else?
*  Well, you mentioned commenting, also sharing the video. If you think it's worthy to be shared with
*  someone else you know. Within YouTube or outside of YouTube as well?
*  Either. Let's see, you mentioned like, dislike.
*  Yeah, like and dislike. How important is that?
*  It's very important, right? We want it's predictive of satisfaction, but it's not perfectly
*  predictive. Subscribe. If you subscribe to the channel of the person who made the video, then
*  that also is a piece of information and it signals satisfaction. Although over the years, we've learned
*  that people have a wide range of attitudes about what it means to subscribe. We would ask some users
*  who didn't subscribe very much, but they watched a lot from a few channels. We'd say, well, why
*  didn't you subscribe? And they would say, well, I can't afford to pay for anything.
*  We tried to let them understand, actually it doesn't cost anything. It's free. It just helps
*  us know that you are very interested in this creator. But then we've asked other people who
*  subscribe to many things and don't really watch any of the videos from those channels. We say,
*  why did you subscribe to this if you weren't really interested in any more videos from that
*  channel? They might tell us, well, I thought the person did a great job and I just want to give
*  them a high five. Yeah.
*  And so. Yeah, that's where I sit. I actually subscribe to channels where I just, this person
*  is amazing. I like this person, but then I like this person. I really want to support them.
*  That's how I click subscribe. Even though I may never actually want to click on their videos when
*  they're releasing it, I just love what they're doing. And it's maybe outside of my interest area
*  and so on, which is probably the wrong way to use the subscribe button. But I just want to say,
*  congrats. This is great work. So you have to deal with all the space of people that see the
*  subscribe button is totally different. That's right. And so, we can't just close our eyes
*  and say, sorry, you're using it wrong. We're not going to pay attention to what you've done.
*  We need to embrace all the ways in which all the different people in the world use the subscribe
*  button or the like and the dislike button. So in terms of signals of machine learning,
*  uh, using for the search and for the recommendation, you've mentioned titles
*  and like metadata, like text data that people provide, description and title and maybe keywords.
*  So maybe you can speak to the value of those things in search and also this incredible,
*  fascinating area of the content itself. So the video content itself, trying to understand what's
*  happening in the video. So YouTube released a dataset that, you know, in the machine learning,
*  computer vision world, this is just an exciting space. How much is that currently,
*  how much are you playing with that currently? How much is your hope for the future of being
*  able to analyze the content of the video itself? Well, we have been working on that also since I
*  came to YouTube. So analyzing the content, analyzing the content of the video, right? Um, and, uh,
*  what I can tell you is that, uh, our ability to do it well is still somewhat crude. We can
*  we can tell if it's a music video, we can tell if it's a sports video. We can probably tell you that
*  people are playing soccer. Um, we probably can't tell whether it's, uh, Manchester United or my
*  daughter's soccer team. So these things are kind of difficult and, and using them, we can use them
*  in some ways. So for instance, we use that kind of information to understand and inform these clusters
*  that I talked about. Uh, and also maybe to add some words like soccer, for instance, to the video,
*  if, if it doesn't occur in the title or the description, which is remarkable that often
*  it doesn't. Um, I, one of the things that I ask, uh, creators to do is, is please help us out with
*  the title and the description. Um, for instance, we were, um, a few years ago having a live stream
*  of some competition for world of warcraft on YouTube. And, um, it was a very important
*  competition, but if you typed world of warcraft in search, you wouldn't find it.
*  World of warcraft wasn't in the title. World of warcraft wasn't in the title. It was match four,
*  seven, eight, you know, a team versus B team and world of warcraft wasn't in the title.
*  Just like, come on, give me being literal, being literal on the internet is actually
*  very uncool, which is the problem. Oh, is that right? Well, I mean, uh, in some sense,
*  well, some of the greatest videos, I mean, there's a humor to just being indirect, being witty and so
*  on. And actually being, um, you know, machine learning algorithms want you to be, you know,
*  literal, right? You just want to say what's in the thing, be very, very simple. And in, in some sense
*  that gets away from wit and humor. So you have to play with both, right?
*  So, but you're saying that for now, sort of, um, the content of the title, the content of the
*  description, the actual text is, is one of the best ways to, uh, for the, for the algorithm to
*  find your video and put them in the right cluster. That's right. And, and I would go further and say
*  that, uh, if you want people, human beings to select your video in search, then it helps to have,
*  let's say, world of warcraft in the title, because why would a person, you know, if they're looking
*  at a bunch, they type world of warcraft and they have a bunch of videos, all of whom say world of
*  warcraft, except the one that you uploaded. Well, even the person is going to think, well, maybe
*  this isn't somehow search made a mistake. This isn't really about world of warcraft. So it's
*  important, not just for the machine learning systems, but also for the people who might be
*  looking for this sort of thing. They get a, a clue that it's what they're looking for by seeing
*  that same thing prominently in the title of the video. Okay. Let me push back on that. So I think
*  from the algorithm perspective, yes, but if they typed in world of warcraft and saw video that
*  with the title simply winning and, and, and the thumbnail has like a sad, um, orc or something,
*  I don't know. Right. Like I think that's much, it's it, it gets your curiosity up. And then if they
*  could trust that the algorithm was smart enough to figure out somehow that this is indeed a world of
*  warcraft video, that would have created the most beautiful experience. I think in terms of just the
*  wit and the humor and the curiosity that we human beings naturally have, but you're saying, I mean,
*  realistically speaking, it's really hard for the algorithm to figure out that the content of that
*  video will be a world of warcraft. And you have to accept that some people are going to skip it.
*  Yeah. Right. I mean, and so you're right. Uh, the people who don't skip it and select it are going
*  to be delighted. Um, but other people might say, yeah, this is not what I was looking for.
*  And making stuff discoverable, I think is what you're really, um, working on and hoping. So yeah. So
*  from your perspective, put stuff in the title of this. And remember the collaborative filtering
*  part of the system starts by the same user watching videos together. Right. So the way that they're
*  probably going to do that is by searching for them. That's a fascinating aspect of it's like ant
*  colonies. That's how they find stuff is so, I mean, what degree for collaborative filtering in general
*  is one curious ant, one curious user, essential. So just the person who is more willing to click
*  on random videos and sort of explore these cluster spaces in your sense, how many people are just like
*  watching the same thing over and over and over and over and how many are just like the explorers and
*  just kind of like click on stuff and then help, help the other ant in the ant's colony discover
*  the cool stuff. Do you have a sense of that at all? I really don't think I have a sense.
*  Okay. Relative sizes of those groups. But I, but I would say that, you know, people come to YouTube
*  with some certain amount of intent. And as long as they, um, to the extent to which they, they try to
*  satisfy that intent, that certainly helps our systems, right? Because our systems rely on,
*  on kind of a faithful amount of behavior, right? Like, um, and there are people who try to trick
*  us, right? There are people and machines that try to, um, associate videos together that really
*  don't belong together, but they're trying to get that association made because it's profitable for
*  them. And so we have to always be resilient to that sort of, uh, attempt at gaming the systems.
*  So speaking to that, there's a lot of people that in a positive way, perhaps, I don't know, I,
*  I don't like it, but like to gain, want to try to game the system to get more attention. Everybody,
*  creators in a positive sense want to get attention, right? So how do you,
*  how do you work in this space when people create more and more, um, sort of click baity titles and
*  thumbnails, sort of a very testing Derek has made a video where basically describes that it seems
*  what works is to create a high quality video, really good video where people would want to watch
*  it once they click on it, but have click baity titles and thumbnails to get them to click on
*  it in the first place. And he's saying, I'm embracing this fact. I'm just going to keep
*  doing it. And I hope you forgive me for doing it and you will enjoy my videos once you click on
*  them. So in what sense do you see this kind of click bait style attempt to manipulate,
*  to get people in the door, to manipulate the algorithm or play with the algorithm,
*  game the algorithm? I think that you can look at it as an attempt to game the algorithm, but
*  even if you were to take the algorithm out of it and just say, okay, well, all these videos happen
*  to be lined up, which the algorithm didn't make any decision about which one to put at the top or
*  the bottom, but they're all lined up there. Which one are the people going to choose?
*  And I'll tell you the same thing that I told Derek is, um, you know, I have a bookshelf and
*  they have two kinds of books on them. Uh, science books. Um, I have my math books from when I was a
*  student and they all look identical except for the titles on the covers. They're all yellow.
*  They're all from Springer and they're every single one of them. The cover is totally the same.
*  Yes. Right. Yeah. On the other hand, I have other more pop science type books and they all have very
*  interesting covers, right? And they have provocative, uh, titles and things like that.
*  I mean, I wouldn't say that they're clickbaity because they are indeed good books. Um, and I
*  don't think that they cross any line, but, uh, but you know, the, that's just a decision you have to
*  make, right? Like the people who, who write classical recursion theory by Piero di Freddie,
*  he was fine with the yellow title and the, and nothing more. Whereas I think other people who,
*  who wrote a more popular type book, uh, understand that they need to have a compelling cover and a
*  compelling title. And, uh, and you know, I don't think there's anything really wrong with that.
*  We do, we do take steps to make sure that there is a line that you don't cross. And if you go too far,
*  maybe your thumbnail is especially racy or, or, um, you know, it's all cats with too many
*  exclamation points. We observe that, um, users are kind of, uh, you know, sometimes offended by that.
*  And so, um, so for the users who were offended by that, we will then depress or suppress those
*  videos. And which reminds me, there's also another signal where users can say,
*  I don't know if it was recently added, but I really enjoy it. Just saying I don't, I didn't,
*  something like, I don't want to see this video anymore or something like,
*  like this is a, like there's certain videos that just cut me the wrong way. Like just,
*  just jump out at me. It's like, I don't want to, I don't want this. And it feels really good to
*  clean that up to be like, I don't, that's not, that's not for me. I don't know. I think that might
*  have been recently added, but that's also a really strong signal. Yes, absolutely. Right. We don't
*  want to make a recommendation that, uh, people are unhappy with. And that makes me, that particular
*  one makes me feel good as a user in general and as a machine learning person, cause I feel like
*  I'm helping the algorithm. My interaction on YouTube don't always feel like I'm helping the
*  algorithm. Like I'm not reminded of that fact. Uh, like for example, uh, Tesla and autopilot,
*  you know, I must create a feeling for their customers, for people that own Tesla's that
*  they're helping the algorithm of test the vehicle. Like they're all like a really proud,
*  they're helping the fleet learn. I think YouTube doesn't always remind people that you're helping
*  the algorithm get smarter. And for me, I love that idea. Like we're all collaboratively,
*  like Wikipedia gives that sense. They were all together creating a beautiful thing. YouTube is,
*  uh, doesn't always remind me of that. That's, uh, this conversation is reminding me of that, but,
*  well, that's a good tip. We should keep that fact in mind when we design these features. I'm not
*  sure I, I really thought about it that way, but that's a very interesting perspective.
*  It's an interesting question of personalization that I feel like when I click like on a video,
*  I'm just improving my experience. It would be great. It would make me personally, people are
*  different, but make me feel great if I was helping also the YouTube algorithm broadly say
*  something. You know what I'm saying? Like there's a, that I don't know if that's human nature, but
*  you want the products you love. And I certainly love YouTube. Like you want to help it get smarter
*  and smarter and smarter. Cause there's some kind of coupling between our lives together being better.
*  If YouTube was better than I will, my life will be better. And that's that kind of reasoning.
*  Not sure what that is. And I'm not sure how many people share that feeling. That could be just a
*  machine learning feeling, but on that point, how much personalization is there in terms of
*  next video recommendations? So is it kind of all really boling down to clustering? Like if I'm in
*  yours clusters to me and so on and that kind of thing, or how much is personalized to me,
*  the individual completely. It's very, very personalized. So your experience will be quite
*  a bit different from anybody else's who's watching that same video, at least when they're logged in.
*  And the reason is, is that we found that that users often want two different kinds of things
*  when they're watching a video. Sometimes they want to keep watching more on that topic or more in that
*  genre. And other times they just are done and they're ready to move on to something else.
*  And so the question is, well, what is the something else? And one of the first things one can imagine
*  is, well, maybe something else is the latest video from some channel to which you've subscribed.
*  And that's going to be very different for you than it is for me. Right. And even if it's not
*  something that you subscribe to, it's something that you watch a lot. And again, that'll be very
*  different on a person by person basis. And so even the watch next, as well as the homepage,
*  of course, is quite personalized. So what we met some of the signals, but what does success look
*  like? What does success look like in terms of the algorithm creating a great long-term experience
*  for a user? Or put another way, if you look at the videos I've watched this month, how do you know
*  the algorithm succeeded for me? I think, first of all, if you come back and watch more YouTube,
*  then that's one indication that you found some value from it. So just the number of hours is a
*  powerful indicator. Well, I mean, not the hours themselves, but the fact that you return on another
*  day. So that's probably the most simple indicator. People don't come back to things that they don't
*  find value in. There's a lot of other things that they could do. But like I said, I mean,
*  ideally, we would like everybody to feel that YouTube enriches their lives and that every video
*  they watched is the best one they've ever watched since they've started watching YouTube. And so
*  that's why we survey them and ask them, is this one to five stars? And so our version of success is
*  every time someone takes that survey, they say it's five stars. And if we ask them, is this the best
*  video you've ever seen on YouTube, they say yes, every single time. So it's hard to imagine that
*  we would actually achieve that. Maybe asymptotically we would get there. But that would be what we think
*  success is. It's funny, I've recently said somewhere, I don't know, maybe tweeted, but that
*  Ray Dalio has this video on the economic machine. I forget what it's called, but it's a 30 minute
*  video. And I said it's the greatest video I've ever watched on YouTube. It's like I watched the
*  whole thing and my mind was blown as a very crisp, clean description of how at least the American
*  economic system works. It's a beautiful video. And I wanted to click on something to say this is the
*  best thing. This is the best thing ever. Please let me, I can't believe I discovered it. I mean,
*  the views and the likes reflect its quality. But I was almost upset that I haven't found it earlier
*  and wanted to find other things like it. I don't think I've ever felt that this is the best video
*  I've ever watched. And that was that. And to me, the ultimate utopia, the best experiences were every
*  single video. Where I don't see any of the videos I regret and every single video I watch is one that
*  actually helps me grow, helps me enjoy life, be happy and so on. Well, so that's a heck of,
*  that's one of the most beautiful and ambitious, I think, machine learning tasks. So when you look
*  at a society as opposed to an individual user, do you think of how YouTube is changing society? When
*  you have these millions of people watching videos, growing, learning, changing, having debates,
*  do you have a sense of what the big impact on society is? Because I think it's huge,
*  but do you have a sense of what direction we're taking in this world?
*  Well, I mean, I think openness has had an impact on society already. There's a lot of-
*  What do you mean by openness?
*  Well, the fact that unlike other mediums, there's not someone sitting at YouTube who decides
*  before you can upload your video whether it's worth having you upload it or worth anybody
*  seeing it really. And so there are some creators who say, I wouldn't have this opportunity to
*  to reach an audience. Tyler Oakley often said that he wouldn't have had this opportunity
*  to reach this audience if it weren't for YouTube. And so I think that's one way in which YouTube has
*  changed society. I know that there are people that I work with from outside the United States,
*  especially from places where literacy is low. And they think that YouTube can help in those places
*  because you don't need to be able to read and write in order to learn something important
*  for your life, maybe how to do some job or how to fix something. And so that's another way in which
*  I think YouTube is possibly changing society. So I've worked at YouTube for eight, almost nine
*  years now. And it's fun because I meet people and you tell them where you work, you say you work on
*  YouTube and they immediately say, I love YouTube. Which is great, makes me feel great. But then of
*  course, when I ask them, well, what is it that you love about YouTube? Not one time ever has anybody
*  said that the search works outstanding or that the recommendations are great. What they always say
*  when I ask them, what do you love about YouTube? Is they immediately start talking about some
*  channel or some creator or some topic or some community that they found on YouTube and that
*  they just love. And so that has made me realize that YouTube is really about the video and
*  connecting the people with the videos. And then everything else kind of gets out of the way.
*  So beyond the video, it's an interesting, because you kind of mentioned creator.
*  What about the connection with just the individual creators as opposed to just individual video? So
*  like I gave the example of Ray Dalio video that the video itself is incredible, but there's some
*  people who are just creators that I love. One of the cool things about people who call themselves
*  YouTubers or whatever is they have a journey. They usually, almost all of them, they suck horribly
*  in the beginning and then they kind of grow. And then there's that genuineness in their growth.
*  So YouTube clearly wants to help creators connect with their audience in this kind of way. So how do
*  you think about that process of helping creators grow, helping them connect with their audience,
*  develop not just individual videos, but the entirety of a creator's life on YouTube?
*  Well, I mean, we're trying to help creators find the biggest audience that they can find.
*  And the reason why that's, you brought up creator versus video, the reason why creator channel is
*  so important is because if we have a hope of people coming back to YouTube, well,
*  they have to have in their minds some sense of what they're going to find when they come back
*  to YouTube. If YouTube were just the next viral video, and I have no concept of what the next
*  viral video could be. One time it's a cat playing a piano and the next day it's some children
*  interrupting a reporter and the next day it's some other thing happening. Then it's hard for me to,
*  to when I'm not watching YouTube say, gosh, I really would like to see something from someone
*  or about something. And so that's why I think this connection between fans and creators is so important
*  for both because it's a way of fostering a relationship that can play out into the future.
*  Let me talk about kind of a dark and interesting question in general. And again, a topic that you
*  or nobody has an answer to, but social media has a sense of, it gives us highs and it gives us lows
*  in the sense that creators often speak about having sort of burn, burnout and having
*  psychological ups and downs and challenges mentally in terms of continuing the creation process.
*  There's a momentum, there's a huge excited audience that makes everybody feel, that makes
*  creators feel great. And I think it's more than just financial. I think it's literally just,
*  they love that sense of community. It's part of the reason I upload to YouTube. I don't care about
*  money. Never will. What I care about is the community. But some people feel like this
*  momentum. And even when there's times in their life when they don't feel, you know, for some
*  reason don't feel like creating. So how do you think about burnout, this mental exhaustion that
*  some YouTube creators go through? Is that something we have an answer for? Is that something, how do
*  we even think about that? Well, the first thing is we want to make sure that the YouTube systems
*  are not contributing to this sense, right? And so we've done a fair amount of research to
*  demonstrate that you can absolutely take a break. If you are a creator and you've been uploading a
*  lot, we have just as many examples of people who took a break and came back more popular
*  than they were before as we have examples of going the other way. Yeah. Can we pause on that
*  for a second? So the feeling that people have, I think, is if I take a break, everybody, the party
*  will leave, right? So if you could just linger on that. So in your sense that taking a break is okay.
*  Yes. Taking a break is absolutely okay. And the reason I say that is because we can observe many
*  examples of creators coming back very strong and even stronger after they have taken some sort
*  of break. And so I just want to dispel the myth that this somehow necessarily means that your
*  channel is going to go down or lose views. That is not the case. We know for sure that this is not
*  a necessary outcome. And so we want to encourage people to make sure that they take care of
*  themselves. That is job one, right? You have to look after yourself and your mental health.
*  And I think that it probably, in some of these cases, contributes to better videos once they
*  come back, right? Because a lot of people, I know myself, if I'm burnt out on something,
*  then I'm probably not doing my best work, even though I can keep working until I pass out.
*  And so I think that taking a break may even improve the creative ideas that someone has.
*  Okay. I think that's a really important thing to sort of dispel. I think that applies to all of
*  social media. Like literally, I've taken a break for a day every once in a while.
*  Sorry. Sorry if that sounds like a short time. But even like, so email, just taking a break from
*  email or only checking email once a day, especially when you're going through something
*  psychologically in your personal life or so on, or really not sleeping much because of work
*  deadlines, it can refresh you in a way that's profound. And so the same applies.
*  And it was there when you came back, right?
*  It's there. And it looks different actually when you come back. You're sort of brighter-eyed
*  with some coffee, everything. The world looks better. So it's important to take a break when
*  you need it. So you've mentioned kind of the YouTube algorithm isn't, you know, E
*  equals MC squared. It's not the single equation. It's potentially sort of more than a million lines
*  of code. Sort of, is it more akin to what autonomous, successful autonomous vehicles today are,
*  which is they're just basically patches on top of patches of heuristics and human experts
*  really tuning the algorithm and have some machine learning modules? Or is it becoming
*  more and more a giant machine learning system with humans just doing a little bit of tweaking
*  here and there? What's your sense? First of all, do you even have a sense of what is the YouTube
*  algorithm at this point? And which however much you do have a sense, what does it look like?
*  Well, we don't usually think about it as the algorithm because it's a bunch of systems that
*  work on different services. The other thing that I think people don't understand
*  is that what you might refer to as the YouTube algorithm from outside of YouTube is actually
*  a bunch of code and machine learning systems and heuristics, but that's married with the behavior
*  of all the people who come to YouTube every day. So the people part of the code, essentially.
*  Exactly, right? Like if there were no people who came to YouTube tomorrow, then the algorithm
*  wouldn't work anymore. So that's a critical part of the algorithm. And so when people talk about,
*  well, the algorithm does this, the algorithm does that, it's sometimes hard to understand. Well,
*  it could be the viewers are doing that and the algorithm is mostly just keeping track of what
*  the viewers do and then reacting to those things in more fine-grained situations. And I think that
*  this is the way that the recommendation system and the search system and probably many machine
*  learning systems evolve is you start trying to solve a problem and the first way to solve a
*  problem is often with a simple heuristic. And you want to say, what are the videos we're going to
*  recommend? Well, how about the most popular ones? That's where you start. And over time,
*  you collect some data and you refine your situation so that you're making less heuristics and you're
*  building a system that can actually learn what to do in different situations based on some
*  observations of those situations in the past. And you keep chipping away at these heuristics over
*  time. And so I think that just like with diversity, I think the first diversity measure we took was,
*  okay, not more than three videos in a row from the same channel. It's a pretty simple heuristic
*  to encourage diversity, but it worked. Who needs to see four or five, six videos in a row from the
*  same channel? And over time, we try to chip away at that and make it more fine-grained and basically
*  have it remove the heuristics in favor of something that can react to individuals and individual
*  situations. So how do you, you mentioned, you know, we know that something worked. How do you get a
*  sense when decisions are kind of A-B testing that this idea was a good one, this was not so good?
*  How do you measure that across which time scale, across how many users, that kind of thing?
*  Well, you mentioned that A-B experiments. And so just about every single change we make to YouTube,
*  we do it only after we've run a A-B experiment. And so in those experiments, which run from
*  one week to months, we measure hundreds, literally hundreds of different variables and measure
*  changes with confidence intervals in all of them. Because we really are trying to get a sense for
*  ultimately, does this improve the experience for viewers? That's the question we're trying to answer.
*  And an experiment is one way because we can see certain things go up and down. So for instance,
*  if we noticed in the experiment, people are dismissing videos less frequently, or they're
*  saying that they're more satisfied, they're giving more videos five stars after they watch them, then
*  those would be indications that the experiment is successful, that it's improving the situation
*  for viewers. But we can also look at other things like we might do user studies where we invite some
*  people in and ask them, what do you think about this? What do you think about that? How do you
*  feel about this? And other various kinds of user research. But ultimately, before we launch something,
*  we're going to want to run an experiment so we get a sense for what the impact is going to be,
*  not just to the viewers, but also to the different channels and all of that.
*  An absurd question. Well, actually it's interesting. Maybe there's an answer, but
*  if I want to make a viral video, how do I do it?
*  I don't know how you make a viral video. I know that we have in the past tried to figure out
*  if we could detect when a video was going to go viral. And those were, you take the first and
*  second derivatives of the view count and maybe use that to do some prediction. But I can't say
*  we ever got very good at that. Oftentimes we look at where the traffic was coming from. If a lot of
*  the viewership is coming from something like Twitter, then maybe it has a higher chance of
*  becoming viral than if it were coming from search or something. But that was just trying to detect
*  a video that might be viral. How to make one? I have no idea. You get your kids to interrupt
*  you while you're on the news or something. Absolutely. But after the fact, on one
*  individual video, ahead of time predicting is a really hard task. But after the video went viral
*  in analysis, can you sometimes understand why it went viral from the perspective of YouTube broadly?
*  First of all, is it even interesting for YouTube that a particular video is viral? Or does that not
*  matter for the individual, for the experience of people? Well, I think people expect that if a video
*  is going viral and it's something they would be interested in, then I think they would expect
*  YouTube to recommend it to them. Right. So if something is going viral, it's good to just let
*  the wave, let people ride the wave of its violence. Well, I mean, we want to meet people's expectations
*  in that way, of course. So like I mentioned, I hung out with Derek Mueller a while ago, a couple
*  months back. He's actually the person who suggested I talk to you on this podcast. All right. Well,
*  thank you, Derek. At that time, he just recently posted an awesome science video titled,
*  Why are 96 million black balls on this reservoir? And in a matter of, I don't know how long, but
*  like a few days, he got 38 million views and it's still growing. Is this something you can analyze
*  and understand why it happened? This video and you want a particular video like it?
*  I mean, we can surely see where it was recommended, where it was found, who watched it,
*  and those sorts of things. So it's actually sorry to interrupt. It is the video which helped me
*  discover who Derek is. I didn't know who he is before. So I remember, you know, usually I just
*  have all of these technical, boring MIT Stanford talks in my recommendation, because that's how I
*  watch. And then all of a sudden there's this black balls and reservoir video with like an excited
*  nerd in the, with like just, why is this being recommended to me? So I clicked on it and watched
*  the whole thing and it was awesome. But, and then a lot of people had that experience, like why was I
*  recommended this? But they all of course watched it and enjoyed it, which is what's your sense of
*  this just wave of recommendation that comes with this viral video that ultimately people get enjoy
*  after they click on it? Well, I think it's the system, you know, basically doing what anybody
*  who's recommending something would do, which is you show it to some people and if they like it,
*  you say, okay, well, can I find some more people who are a little bit like them? Okay, I'm going to
*  try it with them. Oh, they like it too. Let me expand the circle some more, find some more people.
*  Oh, it turns out they like it too. And you just keep going until you get some feedback that says
*  that, no, now you've gone too far. These people don't like it anymore. And so I think that's
*  basically what happened. Now, you asked me about how to make a video go viral or make a viral video.
*  I don't think that if you or I decided to make a video about 96 million balls, that it would also
*  go viral. It's possible that Derek made like the canonical video about those black balls in the
*  lake. And so- Exactly, he did actually. Right. And so I don't know whether or not just following along
*  is the secret. Right. Yeah, but it's fascinating. I mean, just like you said, the algorithm sort of
*  expanding that circle and then figuring out that more and more people did enjoy it and that sort of
*  phase shift of just a huge number of people enjoying it and the algorithm quickly automatically,
*  I assume, figuring that out. That's a, I don't know, the dynamics of psychology,
*  that is a beautiful thing. And so what do you think about the idea of clipping? Like,
*  too many people annoyed me into doing it, which is they were requesting it. They said it would be
*  very beneficial to add clips in like the coolest points and actually have explicit videos. Like,
*  I'm re-uploading a video, like a short clip, which is what the podcasts are doing.
*  Do you see, as opposed to like, I also add timestamps for the topics, you know,
*  do you want the clip? Do you see YouTube somehow helping creators with that process or helping
*  connect clips to the original videos? Or is that just on a long list of amazing features to work
*  towards? Yeah, I mean, it's not something that I think we've done yet, but I can tell you that
*  I think clipping is great and I think it's actually great for you as a creator.
*  And here's the reason. If you think about, I mean, let's say the NBA is uploading
*  videos of its games. Well, people might search for Warriors versus Rockets, or they might search
*  for Steph Curry. And so a highlight from the game in which Steph Curry makes an amazing shot
*  of that is an opportunity for someone to find a portion of that video. And so I think that
*  you never know how people are going to search for something that you've created. And so you want to,
*  I would say you want to make clips and add titles and things like that so that they can find it
*  as easily as possible. Do you have a dream of a future, perhaps a distant future, when
*  the YouTube algorithm figures that out? Sort of automatically detects the parts of the video
*  that are really interesting, exciting, potentially exciting for people and sort of clip them out in
*  this incredibly rich space. Because if you talk about, if you talk even just this conversation,
*  we probably covered 30, 40 little topics. And there's a huge space of users that would find,
*  you know, 30% of those topics really interesting. And that space is very different.
*  It's something that's beyond my ability to clip out, right? But the algorithm might be able to
*  figure all that out, sort of expand into clips. Do you have a, do you think about this kind of
*  thing? Do you have a hope or dream that one day the algorithm will be able to do that kind of
*  deep content analysis? Well, we've actually had projects that attempt to achieve this.
*  But it really does depend on understanding the video well, and our understanding of the video
*  right now is quite crude. And so I think it would be especially hard to do it with a conversation
*  like this. One might be able to do it with, let's say a soccer match more easily, right? You could
*  probably find out where the goals were scored. And then of course, you need to figure out who it was
*  that scored the goal. And that might require a human to do some annotation. But I think that
*  trying to identify coherent topics in a transcript, like the one of our conversation,
*  is not something that we're going to be very good at right away. And I was speaking more to the
*  general problem actually of being able to do both a soccer match and our conversation without
*  explicit sort of almost... My hope was that there exists an algorithm that's able to find exciting
*  things in video. So Google now on Google search will help you find the segment of the video that
*  you're interested in. So if you search for something like how to change the filter in my
*  dishwasher, then if there's a long video about your dishwasher, and this is the part where
*  the person shows you how to change the filter, then it will highlight that area
*  and provide a link directly to it. And do you know if from your recollection, do you know if
*  the thumbnail reflects like what's the difference between showing the full video and the shorter
*  clip? Do you know how it's presented in search results? I don't remember how it's presented.
*  And the other thing I would say is that right now it's based on creator annotations. Ah, got it. So
*  it's not the thing we're talking about. But folks are working on the more automatic version. It's
*  interesting. People might not imagine this, but a lot of our systems start by using almost entirely
*  the audience behavior. And then as they get better, the refinement comes from using the content.
*  And I wish, I know there's privacy concerns, but I wish YouTube explored this space, which is sort
*  of putting a camera on the users if they allowed it, right? To study their, like I did a lot of
*  emotion recognition work and so on, to study actual sort of richer signal. One of the cool
*  things when you upload 360, like VR video to YouTube, and I've done this a few times, so I've
*  uploaded myself, it's a horrible idea. Some people enjoyed it, but whatever. The video of me giving
*  a lecture in 360, we have a 360 camera. And it's cool because YouTube allows you to then watch
*  where do people look at? There's a heat map of where the center of the VR experience was. And
*  it's interesting because that reveals to you what people looked at. And it's very-
*  It's not always what you were expecting.
*  In the case of the lecture, it's pretty boring. It is what we're expecting, but we did a few funny
*  videos where there's a bunch of people doing things and everybody tracks those people. In
*  the beginning, they all look at the main person and they start spreading around and looking at
*  other people. It's fascinating. So that's a really strong signal of what people found exciting in
*  the video. I don't know how you get that from people just watching, except they tuned out at
*  this point. It's hard to measure this moment was super exciting for people. I don't know how you
*  get that signal. Is there a way to get that signal where this is when their eyes opened up and they're
*  for me with the Ray Dalio video? At first I was like, oh, okay, this is another one of these
*  dumb it down for you videos. And then you start watching and it's like, okay, there's a really
*  crisp, clean, deep explanation of how the economy works. That's where I like set up and started
*  watch. That moment, is there a way to detect that moment?
*  The only way I can think of is by asking people to label it.
*  Yeah. You mentioned that we're quite far away in terms of doing video analysis, deep video analysis.
*  Of course, Google, YouTube, we're quite far away from solving an autonomous driving problem too.
*  I don't know. I think we're closer to that.
*  You never know. The Wright brothers thought they're not going to fly for 50 years, three
*  years before they flew. What are the biggest challenges, would you say? Is it the broad
*  challenge of understanding video, understanding natural language, understanding the challenge
*  before the entire machine learning community of just being able to understand data? Is there
*  something specific to video that's even more challenging than understanding
*  natural language, understanding? What's your sense of what the biggest challenge is?
*  Video is just so much information. And so precision becomes a real problem. It's like you're trying to
*  classify something and you've got a million classes. And the distinctions among them, at least from a
*  machine learning perspective, are often pretty small. You need to see this person's number in
*  order to know which player it is. And there's a lot of players. Or you need to see the logo on their
*  chest in order to know which team they play for. And that's just figuring out who's who. And then
*  you go further and saying, okay, well, was that a goal? Was it not a goal? Is that an interesting
*  moment, as you said? Or is that not an interesting moment? These things can be pretty hard.
*  Okay. So Jan Le Kung, I'm not sure if you're familiar with his current thinking and work.
*  He believes that what he's referring to as self-supervised learning will be the solution
*  to achieving this kind of greater level of intelligence. In fact, the thing he's focusing
*  on is watching video and predicting the next frame. So predicting the future of video.
*  So for now, we're very far from that. But his thought is because it's unsupervised,
*  or as he refers to it, self-supervised, if you watch enough video, essentially, if you watch
*  YouTube, you'll be able to learn about the nature of reality, the physics, the common sense,
*  reasoning required by just teaching a system to predict the next frame. So he's confident.
*  This is the way to go. So for you, from the perspective of just working with this video,
*  do you think an algorithm that just watches all of YouTube, stays up all day and night,
*  watching YouTube, will be able to understand enough of the physics of the world about the way
*  this world works, be able to do common sense reasoning and so on?
*  Well, I mean, we have systems that already watch all the videos on YouTube, right?
*  But they're just looking for very specific things, right? They're supervised learning
*  systems that are trying to identify something or classify something. And I don't know if predicting
*  the next frame is really going to get there because I'm not an expert on compression algorithms,
*  but I understand that that's kind of what compression, video compression algorithms do,
*  is they basically try to predict the next frame and then fix up the places where they got it wrong.
*  And that leads to higher compression than if you actually put all the bits for the next frame there.
*  So I don't know if I believe that just being able to predict the next frame
*  is going to be enough because there's so many frames and even a tiny bit of error on a per
*  frame basis can lead to wildly different videos. So the thing is, the idea of compression is,
*  one way to do compression is to describe through text what's contained in the video. That's the
*  ultimate high level of compression. So the idea is, traditionally when you think of video image
*  compression, you're trying to maintain the same visual quality while reducing the size. But if you
*  think of deep learning from a bigger perspective of what compression is, is you're trying to
*  summarize the video. And the idea there is if you have a big enough neural network,
*  just by watching the next, trying to predict the next frame, you'll be able to form a compression
*  of actually understanding what's going on in the scene. If there's two people talking, you can just
*  reduce that entire video into the fact that two people are talking and maybe the content of what
*  they're saying and so on. That's kind of the open-ended dream. So I just wanted to sort of
*  express that because it's an interesting, compelling notion, but it is nevertheless true that
*  video, our world is a lot more complicated than we get it credit for.
*  I mean, in terms of search and discovery, we have been working on trying to summarize
*  videos in text or with some kind of labels for eight years at least. And we're kind of so-so.
*  So if you were to say the problem is 100% solved and eight years ago was 0% solved,
*  where are we on that timeline would you say?
*  Yeah, to summarize a video well, maybe less than a quarter of the way.
*  So on that topic, what does YouTube look like 10, 20, 30 years from now?
*  I mean, I think that YouTube is evolving to take the place of TV. I grew up as a kid in the 70s
*  and I watched a tremendous amount of television. And I feel sorry for my poor mom because
*  people told her at the time that it was going to rot my brain and that she should kill her television.
*  But anyway, I mean, I think that YouTube is, at least for my family,
*  a better version of television, right? It's one that is on demand, it's more tailored to the
*  things that my kids want to watch. And also they can find things that they would never have found
*  on television. And so I think that at least from just observing my own family, that's where we're
*  headed is that people watch YouTube kind of in the same way that I watched television when I was
*  younger. So from a search and discovery perspective, what are you excited about in the five, 10, 20,
*  30 years? Like what kind of things? And it's already really good. I think it's achieved a lot of,
*  of course we don't know what's possible. So it's the task of search of typing in the text or
*  discovering new videos by the next recommendation. I personally am really happy with the experience.
*  I continuously, I rarely watch a video that's not awesome from my own perspective, but what's,
*  what else is possible? What are you excited about? Well, I think introducing people to more of what's
*  available on YouTube is not only very important to YouTube and to creators, but I think it will help
*  enrich people's lives because there's a lot that I'm still finding out is available on YouTube that
*  I didn't even know. I've been working YouTube eight years and it wasn't until last year that I learned
*  that, that I could watch USC football games from the 1970s. Like I didn't even know that was possible
*  until last year and I've been working here quite some time. So, you know, what was broken about,
*  about that, that it took me seven years to learn that this stuff was already on YouTube, even when
*  I got here. So I think there's a big opportunity there. And then, as I said before, you know,
*  we want to make sure that YouTube finds a way to ensure that it's acting responsibly with respect
*  to society and enriching people's lives. So we want to take all of the great things that it does
*  and make sure that we are eliminating the negative consequences that might happen.
*  And then lastly, if we could get to a point where all the videos people watch are the best ones
*  they've ever watched, that'd be outstanding too. Do you see in many senses becoming a window into
*  the world for people? I mean, it's, especially with live video, you get to watch events. I mean,
*  it's really, it's the way you experience a lot of the world that's out there is better than TV
*  in many, many ways. So do you see becoming more than just video? Do you see creators creating
*  visual experiences and virtual worlds? So if I'm talking crazy now, but sort of virtual reality
*  and entering that space, there's that, at least for now, totally outside of what YouTube is thinking
*  about. I mean, I think Google is thinking about virtual reality. I don't think about virtual
*  reality too much. I know that we would want to make sure that YouTube is there when virtual reality
*  becomes something or if virtual reality becomes something that a lot of people are interested in,
*  but I haven't seen it really take off yet. Take off. Well, the future is wide open.
*  Christos, I've been really looking forward to this conversation. It's been a huge honor. Thank you
*  for answering some of the more difficult questions I've asked. I'm really excited about what
*  YouTube has in store for us. It's one of the greatest products I've ever used and continues.
*  So thank you so much for talking to me. It's my pleasure. Thanks for asking me.
*  Thanks for listening to this conversation. And thank you to our presenting sponsor,
*  Cash App. Download it, use code LexPodcast. You'll get $10 and $10 will go to First,
*  a STEM education nonprofit that inspires hundreds of thousands of young minds to become future
*  leaders and innovators. If you enjoy this podcast, subscribe on YouTube, get five stars on Apple
*  podcast, follow on Spotify, support on Patreon, or simply connect with me on Twitter. And now let
*  me leave you with some words of wisdom from Marcel Proust. The real voyage of discovery consists not
*  in seeking new landscapes, but in having new eyes. Thank you for listening and hope to see you next
*  time.