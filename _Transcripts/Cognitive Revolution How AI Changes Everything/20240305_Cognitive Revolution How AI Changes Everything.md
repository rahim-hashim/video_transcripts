---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 4014s
Video Keywords: []
Video Views: 1782
Video Rating: None
---

# The Example Engine: How Exa Is Creating the AI Librarian for the Web with Will Bryk, CEO of Exa
**Cognitive Revolution "How AI Changes Everything":** [March 05, 2024](https://www.youtube.com/watch?v=dT_RicoNSKM)
*  I think there's an interesting distinction between search and research.
*  Google is a search engine. You know, you kind of know what you're looking for,
*  but when you don't know what you're looking for, you're more doing research.
*  And I think that's where Exa shines.
*  What we're doing at Exa is we're kind of like trying to take all the world's knowledge and
*  putting it into a new type of database, like a neural database.
*  I like this database analogy because it's not really search. It's like you're kind of like
*  with every query, you're filtering the database of all the knowledge into just what you need.
*  There's a problem with search engines like Google is like you search something
*  and they say, you know, 33 million results at the top.
*  Like, what am I supposed to do with 33 million results?
*  There's no way all these results are actually what I'm asking for.
*  So it's just like you just feel overwhelmed.
*  From the product perspective, like not every query should require the same amount of compute.
*  Google has kind of made this assumption that no matter what query you type in,
*  it takes a few hundred milliseconds.
*  But certain queries are extremely complex and might require scouring the internet
*  for maybe even seconds or minutes.
*  Thinking of it as more the optimal trade-off is cool.
*  It's like you're always optimizing for exactly the amount of effort to put into the thing.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture of how
*  AI technology will transform work, life and society in the coming years.
*  I'm Nathan LeBenz, joined by my co-host Eric Thornburg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today, I'm excited to introduce you to Will Brick, founder of ExaAI,
*  a company building a new kind of search engine designed with AI systems and workflows in mind.
*  Noting that Google has limited people's imaginations about how to search the internet,
*  Exa aims to help people surface things that were previously impossible to find.
*  Now, if you've been following the show, you know that I've been exploring a variety of exciting
*  new information and knowledge retrieval tools over the last few months.
*  Today, ChatGPT remains my go-to workhorse for ad hoc coding and other random tasks,
*  though recently Gemini Advanced and now Clog3 are both gaining share.
*  Meanwhile, Gemini 1.5 Pro has become my favorite for all write-as-me tasks,
*  including creating the first draft of this introductory essay,
*  which I did edit quite extensively, but nevertheless saved me a lot of time.
*  Perplexity is still my go-to for quick and accurate answers to specific questions,
*  but U.com Research Mode has now taken the prize for deep-dive multi-page research reports.
*  And meanwhile, Elicit is the most useful for structured, systematic academic literature reviews.
*  So, in this increasingly crowded landscape, where does Exa fit in?
*  Well, for one thing, while most of these products are aiming to provide answers to questions,
*  Exa still returns links, like a more traditional search engine would.
*  After playing around with it for a while, I've realized that it's the quality, the controllability,
*  and the depth of results that really sets Exa apart.
*  And I've come to think of it as an example engine.
*  To understand how valuable this can be, consider that just about every company I talk to would like
*  to scale highly personalized communications, whether for lead generation, recruiting, or something else.
*  Today, language models make this dream realistic.
*  Given a list of leads or candidates and a bit of information about them,
*  a language model can personalize your outreach at roughly human quality
*  and far more scalably than was ever possible before.
*  But where does the list itself come from?
*  Where does the list itself come from?
*  If the inputs to such a process are low quality, then the whole process will be garbage in, garbage out.
*  And this is really where Exa shines.
*  Given a complicated multi-part query, which can be up to a full paragraph in length,
*  something that you wouldn't even bother to try with Google,
*  but which language models can very quickly generate,
*  and optionally an example of what you're looking for,
*  Exa returns lists of a certain type of result,
*  whether they be companies, people, how-to articles, you name it.
*  And then you can feed those examples into your broader AI workflows.
*  In this conversation, we get into not only how Exa supports previously impossible-to-scale use cases,
*  but also how it works under the hood, including the nature of their web index,
*  the reasons they are rolling their own vector database,
*  and how they are planning to extend their functionality
*  with knowledge graph-like structures in the future.
*  Will's ambitions for Exa are huge.
*  He aims to build a leader in the new information landscape.
*  And my experience with the product suggests that Exa's API business
*  is likely to be booming for the foreseeable future.
*  And also that the ways in which information is found and processed across the economy
*  may change even more dramatically than all the new web experiences suggest.
*  As always, if you're enjoying the show, we appreciate it when you take a moment to share it with friends.
*  I expect that everyone will find value in this episode,
*  but I would particularly encourage you to send it to anyone you know
*  who's building AI task automations and who would benefit from bigger, higher-quality input lists.
*  And of course, we always welcome your feedback.
*  I have accounts everywhere, so please feel free to DM me on the network of your choice.
*  Recently, a listener named Ashwin DMed me on Twitter to offer to send me a piece of original art.
*  And if you're watching the video on YouTube, you can see it right there.
*  He did not ask for any promotional consideration, and I certainly can't promise to promote everything that folks might send me,
*  but I was super flattered to get such an offer,
*  and I'm happy to point you to his website, ashwinsartstudio.com,
*  for more of his detailed and intricate drawings.
*  Now, here's my conversation with Will Brick, founder of Exa AI.
*  Will Brick, founder of Exa AI, welcome to the Cognitive Revolution.
*  How you doing? Glad to be here.
*  I'm excited to talk to you about what you are building with Exa.
*  It is an AI-first search product, and we're going to get into all the nuances and details of that,
*  and really a quite different one that has caused me to think deeply about how I think about
*  the different ways that I go about searching for, retrieving, and processing information.
*  So I think this is going to be a really fun conversation.
*  For starters, you want to just kind of give us a little bit of a background on what you're doing.
*  For starters, you want to just kind of give us a little bit of context on who you are, what Exa is,
*  and how you are thinking about the world of information and how that contrasts against knowledge.
*  So Exa is a search engine built for AI systems.
*  Really, we're trying to redesign the search algorithm itself.
*  People have been used to Google for a long time, but now we have technologies like GP3, GP4,
*  that understand text at the level of a human.
*  So the inspiration for Exa was, what if we combine the power of language models,
*  which feel like they understand text at a human level, with search, which feel like it hasn't
*  changed in a decade? That's what we set off to do. We've been working on it for a couple of years.
*  We're really a research startup, so we have our own GPU cluster. We train our own foundation
*  models for search, really trying to just ultimately solve the hardest queries, the most complex ones
*  that Google is really bad at. I read extensively through your website. One of the quotes that
*  jumped out at me there was, one thing we've realized is that Google has actually limited
*  people's imaginations when it comes to what you can find on the internet. And we are still expanding
*  our conceptions ourselves. I'd love to hear a little bit about that kind of intellectual journey.
*  Maybe you could start with, what are some of the queries or questions or information needs that
*  you think are not well served by Google or the last generation of search options? And then
*  maybe tell a couple of stories along the way of moments or use cases that have changed how
*  you think about it. It's funny. People think that search is solved, that Google basically solves
*  web search. When you start thinking about it more, you realize there are all sorts of types of queries
*  that are just completely unsolved. For example, you don't go to Google to find a list of startups
*  that are applying AI to law. Because when you search that on Google, a list of startups applying
*  AI to law, you don't just get a list of startups. And then certainly when you start adding more
*  modifiers like startups applying AI to law in the Bay Area, you don't just get a list of startups
*  applying AI to law in the Bay Area. You keep adding, making the query more and more complex,
*  you realize like wait, Google is just not doing that. And then more broadly, anytime you try to
*  get information and you're not using Google, it's because Google has failed you. So if you're going
*  to LinkedIn to find people or PitchBook to find startups or Twitter to find high quality
*  news, it's because you can't find that on Google. You don't know the right keywords to search.
*  Even if you're trying to find a date, you're not going to Google because Google is not a complex,
*  it's not a powerful enough search engine to filter all the world's information because a lot is out
*  there into exactly the knowledge you want. And so our vision is to be able to, in real time,
*  take the petabytes of information that's out there and filter to exactly what you ask for,
*  exactly the knowledge that you want as fast as we can.
*  So the example of startups applying AI to law in the Bay Area is one good example. What other
*  key queries or canonical use cases come to mind for you? Especially I'm interested in this process
*  of expanding your own conception. There are so many. So I want to find a designer
*  I know of one that has a really cool style. So I have a web page of a designer that I really like
*  and I want to paste it into Google and find similar designers. You can't do that. Similarity
*  search is just something that's really hard. When you don't know the right keywords,
*  Google fails you. And so when you try to do similarity search, it's like searching with
*  a huge web page as a search itself and Google just can't handle that whereas Exo can. Yeah,
*  searching for people, you want to find researchers in the Bay Area that have rust experience.
*  Google does not give you a list of researchers. So you want to find people, you want to find
*  companies, you want to find really high quality articles that have a certain argument. So
*  articles that really go deep into the power of rust over Python for multi-processed applications.
*  You don't think to type that into Google because you know it's just not going to work.
*  Yeah, it's really just like there's any sort of complex query that you might want to make.
*  Google fails. Yeah. Okay. Interesting. So I have been kind of on my own personal journey of trying
*  as many of the new information products as I can get my hands on over the last several months.
*  We've actually had a few founders of other notable companies on the show as well. So we've had Arvin
*  from Proplexity. We have an episode with Richard Sosher from u.com and we've had the founders of
*  Elicit on as well. And maybe I would just kind of compare and contrast a little bit my experience
*  with Exa against not just Google but against those. And I would try to come up with kind of
*  the right label or sort of category name for each of these products. They're all a little bit
*  different and it's quite exciting actually to see that there are just people going in
*  conceptually different directions and not just competing one for one.
*  So when I think of Proplexity, I think of kind of answer engine. It's like I go there if I have
*  a question, I want the fastest, most kind of clear, accurate answer to it. I think they do
*  really well with that. And they give you an answer in paragraph form. I go to u.com these days. I
*  think of that a little bit more as an autonomous research assistant where, especially in research
*  mode, which is my favorite mode from u.com, I can give it kind of a multi-part question and it'll
*  go out and do like multiple rounds of searching, processing the pages, trying to synthesize the
*  results. And then with Elicit, I think of that as more like a structured literature review tool
*  where it brings results back not in paragraph form but in tabular form. It's like here's all
*  these papers and here's these different dimensions and here's how, and they're very focused on
*  academic content, and here's how we sort of assess each of these papers on each of these dimensions
*  and you can kind of add columns. And you end up with something that's like a very structured sort
*  of layout of the information that you're engaged with. EXA, I am using the term example engine
*  so far. And I think what is really interesting about the EXA experience is that the input is
*  very different and the nature of the results are very different from what you would see with Google.
*  But the sort of presentation is actually maybe in some sense the most traditional in that it gives
*  you kind of a list. But I guess I have a number of questions like that about this. Like one,
*  how do you think about the example engine label? You can compare and contrast to the other ones
*  as much as you'd like. And I'm interested in kind of a number of the design choices,
*  but let me just let you react to all that first. The label is difficult because even
*  when you've been building it for a long time, don't really know the exact thing to call it.
*  I'd say it is particularly good for research. So maybe a research engine might work because
*  if you think about it, like Google and a lot of these, the tools you mentioned are built on top
*  of Google and they add some sort of post-processing stuff. But ultimately, the results they're using
*  are based on like a keyword like search engine that Google uses. And I think there's an
*  interesting distinction between search and research. Google is a search engine. You kind of know what
*  you're looking for. Taylor Swift boyfriend, you type into Google, you get that thing.
*  Or you search my name, you get like content surrounding my name, but you know what you're
*  looking for. But when you don't know what you're looking for, you're more doing research. And I
*  think that's where Exa shines. You type in like a natural language, prompt we call it, explaining
*  the type of thing you want. And you get a list of things that match that. So I think research engine,
*  it's kind of like Exa feels more like a library. You go up to the library and you say, hey,
*  I'm looking for startups applying AI to law. You don't know the right keywords to use there.
*  Some of the startups applying AI to law might not mention AI or law. They might say we take
*  a certain machine learning algorithm and apply it to legal documents or something even less
*  keywordy. And the librarian knows a lot, very smart and is able to point you to the things that
*  match that. It's more like a research experience. And yeah, in terms of the UI, we're really focused
*  on the API and the UI. We want people to just, you know, we always want people to be able to use
*  Exa. And we are figuring out the right user interface. Right now it's a list of links,
*  but that's not ultimately like the right user interface for consumer search. I certainly,
*  like certainly like LLMs will and are a huge part of the right consumer interface. And I think there
*  are really interesting things coming there that we're going to explore. But yeah, right now it's
*  just we want to like just show people exactly what the API returns. But I think more we're going to
*  move towards a consumer interface that is more like the products we want people to build with Exa.
*  So more like a researcher type type interface. Hey, we'll continue our interview in a moment
*  after a word from our sponsors. If you're a startup founder or executive running a growing business,
*  you know that as you scale your systems break down and the cracks start to show.
*  If this resonates with you, there are three numbers you need to know. 36,000, 25 and one.
*  36,000. That's the number of businesses which have upgraded to NetSuite by Oracle.
*  NetSuite is the number one cloud financial system, streamline accounting, financial management,
*  inventory, HR and more. 25. NetSuite turns 25 this year. That's 25 years of helping businesses
*  do more with less, close their books in days, not weeks and drive down costs. One, because your
*  business is one of a kind. So you get a customized solution for all your KPIs in one efficient system
*  with one source of truth. Manage risk, get reliable forecasts and improve margins. Everything you need
*  all in one place. Right now download NetSuite's popular KPI checklist designed to give you
*  consistently excellent performance, absolutely free and netsuite.com slash cognitive. That's
*  netsuite.com slash cognitive to get your own KPI checklist. Netsuite.com slash cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Okay. So that's maybe a great segue to what are some of the things that you have seen people
*  build or want people to build that you think are most exciting. And I can say, you know, in just
*  kind of testing this and working with a friend of mine who introduced us, who he and I are working
*  together on a number of different kind of prototype applications for this company,
*  Athena, where we're both advisors. He has done some really cool stuff with similar companies,
*  similar candidates, you know, similar articles kind of creating like synthetic thought leadership
*  or synthetic plans. He put, he uses it for, you know, if you want to, because the assistants a
*  lot of times don't have the expertise, but the theory is it's out there, right? So he showed a
*  great example the other day of I want to increase my oxygen capacity in my lungs and what do I do?
*  You know, that's one of my goals, but how can the assistant help? Unfortunately, the assistant
*  in general is not going to have a lot of expertise there, but what we're starting to patch together
*  is like, well, let's go find some expert content about that. That's where exit comes in. Like
*  here's a list of articles about how to improve your lung capacity and then, you know, further
*  processing downstream with language models. You can get to like practical steps or maybe we could
*  order, you know, this machine, or maybe we could sign you up for this, you know, online eight
*  exercise course or whatever, right? You can start to go from the goal to unpacking the goal with
*  hopefully expert content and then, you know, starting to create concrete actions that the
*  assistant can actually do for you and advance, you know, help you advance toward your goals.
*  That's the sort of thing that we've been experimenting with, but I'm sure you have
*  many more scenarios I'd love to hear about some of your favorites. Yeah, people build
*  all sorts of things from like the very business-like and, you know, professional to the wacky.
*  And so just an example, like one tool I'm particularly proud of is it's a paper writing
*  tool that helps people write papers. And it uses Chatch BT to present so many different ideas for
*  what to write next and can unblock you and inspire you to think of like new ideas.
*  And but Chatch BT, you know, it's not smart enough to do that on its own. So it needs to rely on a
*  search engine. And if it relies on, you know, a traditional search engine, it's pretty limited.
*  It's not, it can't search in all these powerful ways, but when it uses Exa, it's able to recommend
*  like really good papers that really exactly match the type of thing you're writing about or exactly
*  like follow the type, you know, you could, you could say like, what's a paper that follows this
*  idea and you could paste the idea like, you know, like that's a crazy type of search that you can't
*  do on Google. Like here, you know, here's a paragraph or two. And then like, what's that
*  idea that would naturally follow this. And you could do that with Exa for helping academics
*  learn about their field because they've for two decades been using a tool that was limited in
*  certain ways. And now we're like opening up the world's knowledge that that's, that's exactly what
*  I got into this for. And then, okay, so that's just one example. Like another tool that I'm happy
*  about is, you know, a tool for VCs to like source companies. So it's like, again, like a chat BT,
*  like product, like interface really took a chat bot, but the chat BT is recommending like startups
*  to go investigate. And the VCs would not find these startups if it weren't for Exa. So it's
*  kind of like we're connecting in a way. It's like we're enabling a marketplace of startups
*  to VCs. Like, yeah, so you could enable new marketplaces through better search.
*  And then wacky things, you know, like people have people have like made apps where they can meet
*  people in real life because of Exa, like, you know, thinking dating app, you know, you do like,
*  you know, you paste someone's profile, and then you get like, you know, 20 different people
*  who are similar. So like people search is very powerful. I know someone who has met several
*  people in real life, because of Exa. That's cool to see like the digital to the real. And like,
*  it's just very fun search engine. So people beyond just like tools people are building,
*  people are just finding like, they're seeing the world in a new way because of Exa, like,
*  at one point, we had rediscover the internet as the title on the consumer page, because that's
*  really what's happening is like, there was this internet, it was always there, there's all these
*  not like things like really interesting things that were there. And you just didn't know about
*  them. They were hidden because of the algorithm. And so and because we changed the algorithm,
*  those things are now revealed. And so someone described it as like uncovering like a hidden
*  temple of knowledge or something. Which, yeah, it's amazing. And there are like infinite insights
*  on the web from, you know, documents that you haven't already found, but also from combining
*  documents, Chatchviti can do the combining, but it needs the right inputs. And so really,
*  when you combine Exa to like find all those like 100 documents that are relevant, and then you have
*  you combine Exa with like an AI like GB4 or eventually GB5. That's when you get like absolutely
*  magical experience. We're the knowledge engine. Chatchviti is the combining engine. So I like why
*  a lot of our products like they use AI, right? Like, again, like we're a search built for AI.
*  So all these products I described, they're like Exa is being used by an AI system. That's when you
*  get like the most the most juice from what we're doing. So what does that mean? A search built for
*  AI? I mean, that's a very provocative phrase. And it definitely, you know, has a strong point of view
*  around where the world is going. I don't immediately know what that means, though, in terms of like how
*  that caches out, like how are the results different? Or how are you, you know, what are the demands of
*  AI as a consumer of search results? How is that different from the human needs as a user of search
*  results? If an AI is doing the searching, it's very different from a human doing the searching. So,
*  I mean, for a few reasons, one, like a human is lazy and types in a few keywords,
*  max, right? Like a human doesn't want to type in a few like a paragraph explaining exactly
*  the human wants, whereas an AI can instantly open a paragraph or two paragraphs,
*  depicting exactly what it wants. So you want a search engine that can handle the complex queries
*  that an AI can make. Like Google was optimized for very simple queries like Walmart homepage,
*  like things like that. And okay, that's one. Also, you know,
*  AIs can take 100 results and instantly gobble up all that information. Whereas humans, you know,
*  we search and then we click on a couple links and read them and move on. So that means like you want
*  a search engine that can return like not just a few links and a few quality results, but like 100.
*  You also like humans when they search something like, again, like Taylor Swift, we don't really
*  know what we want. And we kind of just want like a diverse array of things related to Taylor Swift.
*  Whereas when an AI searches, it knows exactly what it wants and it asks for that thing. So if it
*  wants a list of companies, it'll ask for that. And then it wants a list of 100 companies. It doesn't
*  want like one company and then another blog post about companies and then a LinkedIn post and then
*  some Reddit forum. It knows what it wants. You just want a search engine that is like controllable
*  and can return it exactly what it wants, exactly the number of results, handle complex queries.
*  And then the last thing is that guys, they don't want links and titles. They want like full page
*  content. They want like exactly the content itself because they don't want to get a links and then
*  have to like go wait in a browser and read that thing. They want to just like get all the information
*  at once. So you need all these features if you're going to be serving an AI like really well.
*  You could connect an AI to like Google, but now you're just connecting this like completely new
*  creature that has like all these different properties to something that was designed for
*  organic humans. And it's just like not a good pairing. Like this is such an important
*  part of the human experience, the way we find information. Why are we using some old technology
*  for some super new thing? So the three things that I heard there, Tim, if I missed anything, one is
*  because the language models are just so quick at generating text, they can do much deeper, more
*  robust queries, you know, with no effort, right? As opposed to humans just don't sit there and type
*  paragraphs. So you want to be able to handle that. Second, you can handle a lot more information
*  coming back. So you, you know, you want to return more. And third, instead of links, you want to
*  return actual content. You also mentioned something about types, basically controlling the type of the
*  response as opposed to just, you know, kind of whatever. So that's all really interesting.
*  How does that compare to in terms of like starting to get into a little bit of how it works?
*  I know that Google obviously has moved somewhat in this direction, right? I mean, the original
*  thing was PageRank. And I actually don't know if you're using any sort of like PageRank type
*  algorithm in your system, but they certainly have moved toward, you know, some sort of BERT,
*  whatever, you know, the successor to BERT, where they are embedding content, you can do at least
*  some amount of semantic querying there, right? But how would you contrast, you know, the, I guess,
*  on those key performance dimensions that you outlined, how would you contrast Excel against
*  Google today? I actually don't know what really it's an interesting point. I don't know what would
*  happen if I put in a full paragraph into Google. Does it just still say like, sorry, there are no
*  results for that. That's an interesting experiment that I've not done. It doesn't like do what you
*  ask it to do. Like, you know, if you type, if you paste like an abstract of a paper, for example,
*  and you say like, similar papers at the bottom, like, it's going to give you a bunch of results
*  that are the same paper. It's like, it's like finding like a bunch of examples on the web where
*  people have where that paper exists, as opposed to finding similar papers. So it's not like,
*  it's definitely not handling those kinds of queries. I mean, you could experiment with more
*  of those, but like, it's just not meant for that. In terms of how the Google algorithm, like contrast
*  with our algorithm, it is totally different. So with Google, I mean, no one knows exactly how
*  it works. But in terms of their BERT stuff, like, it seems more like a re-ranking at the end. So
*  it's like a post-processing step. So maybe you do an initial filtering of the entire web to like
*  some number of results and then you re-rank with some neural method. And that's very different from
*  going neural from the beginning, because, you know, you will just miss things that are not in that
*  first filter. So like you filter to 10,000 and, you know, if you miss things that are relevant,
*  it just, the re-ranking won't help. But yeah, I mean, their algorithm is, of course, like more,
*  when I say a keyword based algorithm, it's more complex than that. It's Google. I mean, it is
*  very effective for what it's trying to do. And they have like a knowledge graph that they, you
*  know, when you mention Obama in your query is going to like know about, it's going to take some
*  information from Obama from the knowledge graph and input that into your query. So it's more
*  complicated, but it's fundamentally like a keyword based algorithm. It's like looking at
*  keywords. And whereas our algorithm is we train like a transformer like model to predict links.
*  So the way it works is we find places on the web where people talk about links. So imagine,
*  imagine like a Reddit comment or someone says, you know, yo, check out this cool aerospace startup,
*  and they paste a link after. We hide the link and ask the model, you know, predict, take that text
*  and predict which link followed. And if you do that, like hundreds of millions of times,
*  you get a really good search engine out of that, because at search time, someone's like
*  aerospace startup, and the model predicts the most likely links to follow. And so in some senses is
*  like page rank. It's more like a like a neural page rank. It's like a it's like learned page rank.
*  You know, it's the if the model often sees people when people say a great fundraising essay,
*  they often refer to a Paul Graham essay, then the model learns, okay, when people talk about
*  great fundraising essay, when someone searches for a great fundraising essay, you know, let's
*  let's hit them with the Paul Graham one. So it is like a learned a page rank. But I mean, that's
*  just review one, you know, for v2 and v3, we have like, some really, really cool, exciting things
*  coming up. To the degree that you want to share more about that, I'm keen to hear but before we
*  even get to v2 and beyond, to just be a little bit more concrete about like exactly how it's
*  working. It's very interesting that you are starting with this conversation about links,
*  when you're actually you also said transformer like model, I'd be interested to know more about
*  that. And like, what exactly the like part of that transformer like means, you know, what sort of
*  deviations there are. But I imagine you're not like doing because you could do that in chat
*  GPT as well, or you could be like, complete the following here is a great essay on fundraising
*  https, you know, colon slash slash and see what it comes up with. And a lot of times there, you know,
*  we predict token by token www dot whatever.com slash whatever. And sometimes it might generate
*  real links. A lot of times it would generate made up links and link you to nowhere. So I assume
*  you're not doing like literal token by token link prediction that way. Can you give us a little bit
*  more on kind of what makes the model transformer like and sort of a little bit more concretely,
*  like what exactly is being predicted at runtime? Hey, we'll continue our interview in a moment
*  after a word from our sponsors. The brave search API brings affordable developer access to the
*  brave search index, an independent index of the web with over 20 billion web pages. So what makes
*  the brave search index stand out? One, it's entirely independent and built from scratch.
*  That means no big tech biases or extortionate prices. Two, it's built on real page visits from
*  actual humans collected anonymously, of course, which filters out tons of junk data. And three,
*  the index is refreshed with tens of millions of pages daily. So it always has accurate up to date
*  information. The brave search API can be used to assemble a data set to train your AI models
*  and help with retrieval augmentation at the time of inference, all while remaining affordable with
*  developer first pricing. Integrating the brave search API into your workflow translates to more
*  ethical data sourcing and more human representative data sets. Try the brave search API for free for
*  up to 2000 queries per month at brave.com slash API. Hey, everyone, Eric here, the founder of
*  turpentine, the network that produces the cognitive revolution. This episode is brought to you by ODF,
*  where top founders get their start. ODF has helped over 1000 companies like Traba,
*  Levels and Finch meet their co-founders and go on to raise over $2 billion.
*  Apply to the next cohort of ODF and go from idea to conviction on what's next. Startups change the
*  world. They can also change your life. Is it your turn? Learn more at beyondec.com slash revolution.
*  That's correct. We're not predicting a token by token. We're really, so we have an index of
*  documents and the model is trying to predict which documents. So it really ultimately,
*  instead of predicting a link, it predicts it's like a document ID. And so it's not generating
*  the link and it's transformer like because you can't just use us, you know, if you take a
*  transformer and try to do what you're doing with predicting the next token of the next token,
*  with predicting the next token of the link, like it's just not going to work because you're
*  forcing the model to memorize URLs and that just doesn't work. So you can't just naively take a
*  transformer and fine tune it for this objective. You have to create a new type of objective.
*  So we have, it's an embedding space approach. So like the transformer ultimately outputs an embedding
*  and you start using that embedding. But like doing that at scale and very precisely, that's where a
*  lot of the research that we did for like really like a year when we started this, what we could
*  talk about was like really exciting. Like I have a very few startups actually do like research into
*  what they're doing for a year before they, you know, ship product with helper.
*  Yeah. Google comes to mind as one that did at least some serious work before launching back in
*  the day. So it makes sense that, I mean, I think the embeddings, the future of embeddings, I think
*  is going to be extremely interesting in many ways. And, you know, I've had this kind of hypothesis
*  for a while that more and more communication is going to be mediated by embeddings as opposed to
*  being mediated by natural language. As systems come to talk to other systems, I think in many
*  cases, it's just not going to make a lot of sense for that to be reduced to, you know, a string,
*  a linear string of natural language tokens and then kind of, you know, reprocessed.
*  If on both ends, you have AI systems that natively work in, you know, some sort of embedding space,
*  then like some sort of translation from embedding space to embedding space seems like a lot more
*  efficient, a lot less lossy, also a lot more problematic in some ways in that it's like
*  becomes very hard to know what is going on, you know, and like, we can't interpret that always very
*  well or, you know, we can't interpret it in the same way that the systems are interpreting it,
*  certainly. So I think that's like really interesting. And this sort of feels like a
*  little bit of a glimpse of, you know, this aspect of the future that I've been kind of anticipating.
*  And embeddings actually feel to me like the past. I think embeddings are just the beginning. I
*  would be disappointed if embeddings are the way we're passing around knowledge in the future,
*  because embeddings really do lose a lot of information. You know, particularly,
*  it depends how many embeddings you obviously if you have, you take text and you output 100
*  embeddings, then you're not losing information. But if you're taking text and outputting an
*  embedding, and then doing a dot product with other, you know, the document embeddings you have
*  in whatever index you're talking about, that dot product operation is just like lossy, like
*  it's not going to be able to handle all the types of complex queries you might want to do.
*  So our thing is embeddings based right now. And it's really, really powerful embeddings,
*  like we really, you know, squeeze that as much juice as you can from embeddings. But embeddings
*  are still fundamentally limited, like they can't do complex operations. For example, like
*  startups applying AI to law in the Bay Area, where the founders, you know, have experience in
*  Rust and blah, blah, blah, you keep adding more modifiers, like you cannot expect a single
*  embedding and a single dot product to handle that kind of query. So when I talk about v2 and v3,
*  that's what we're talking about, like moving beyond embeddings. So embeddings are definitely
*  a step up from, you know, not a no neural, but and like, at least right now, the best systems
*  are probably going to combine keyword based approaches and embeddings approaches. But
*  ultimately, like you could do way more powerful things. Maybe you could think of it as like,
*  there's a spectrum between an embedding dot product and like a full transformer output,
*  like, you know, an embedding dot product is a very simple operation and like a full
*  set. Okay, imagine like that you take edge more specifically, you take the embedding of a query
*  and the embedding of a document, and you take a dot product, you get a score. On the other side
*  of the spectrum is like you put the query text and the document text in the context window of
*  the transformer. And it goes through all the weights of the transformer outputs a score.
*  This one took a huge way more compute than this one. So it's a much more powerful operation.
*  It's just hard to do this one over the whole web. This one you can do over the whole web.
*  So are there things in the middle of that are unexplored? I think so.
*  And it's probably worth kind of describing a little bit how X is best prompted, which I noticed
*  it's interesting to kind of have your best practices. And then you also have like an auto
*  layer that allows people to kind of use the sort of keyword search that they're used to using and
*  translates it into the best practices for exoprompting. Maybe just give a little account
*  of that first. And then that I think shed light on, you know, the underlying technology.
*  Sure. Yeah. Because the model was trained to predict that, let's say document ID. So like,
*  you know, check out this aerospace startup link. That means that the best way to search XO right
*  now is to search in a way such that a link follows your text. It's a little strange, but like, you
*  know, type of query type of prompt such that a link the link that you want follows. So if you
*  really want the model to output startups, the best thing you could do is like say like, at the end of
*  your prompt, do like parentheses startup, colon, like that is the end of your prompt, because what
*  follows that on the web when someone puts that obviously a link to a startup homepage. And so
*  you're like really biasing the model to return exactly what you want. This is something we were
*  actually considering putting on the homepage, just like that. It's a really powerful way to search
*  XO is to prompt it in that way. And there are all sorts of prompting tricks that make it that allow
*  you to squeeze out the model. We're in a very similar state to like GPD three before before
*  chat VT before our HF. It was a text completion model. And so you had to prompt it in these weird
*  ways. And it was hard to use. And then they you know, our HF did to make chat VT. And that's great
*  because it's easier to interact with and now my mom could use chat VT. But it also you lose things
*  because our HF makes it less controllable. And from our perspective, it is a little harder to use,
*  for sure. In this when it's you're using this model that requires like the text to you know,
*  it requires in this weird format. But it also like makes it a very powerful and controllable search
*  engine. So we haven't like put a huge amount of resources into our HF thing. The model. Yeah,
*  also a lot of our users are businesses who are happy to learn how to prompt well, or like they
*  might even not be prompting themselves. They have like you just tell chat VT to prompt it correctly.
*  And it does that. So I think chat VT made our weird prompting scheme less less of a negative.
*  Yeah, well, you certainly have to be willing to step outside what people are familiar with
*  to create something new. No doubt about that. So under the hood, then it is, if I understand
*  correctly, the input is this text prompt that sort of tees up here's the kind of thing that I'm
*  looking for. The model predicts an embedding that embedding is then through a vector database,
*  find the K nearest neighbors or whatever from your existing index. And then those of course,
*  correspond to source links. And that's how you ultimately bring links back.
*  It's prediction is in this like high dimensional embedding space. Is that basically how it works
*  today? So then in the future, you imagine kind of elaborating that in multiple ways, I guess,
*  just hearing your example of like startup law Bay Area, these sort of conjunctive composite queries,
*  my first like naive reaction to that would be maybe I want to kind of decompose that and have,
*  you know, multiple different embedding guesses, and then run multiple different
*  K nearest neighbors, and then maybe look for like the overlap in those resulting sets or,
*  you know, have some sort of, you know, some sort of post processing heuristic on like which of,
*  you know, how to combine those results at the end, I guess you could also just have language models,
*  you know, if you if you have language models get fast enough, they could start to, you know,
*  do the post processing for you. But how do you see that kind of evolving as, as we go? And what
*  are the bottlenecks? Like, is it just that we're still inventing this stuff? Is it that the compute
*  right now is not there to power all the things that you, you know, you maybe you know how to do
*  them, but you just can't either like afford it or you can't it takes too long. I've been interested
*  to hear, you know, both like, where you think we're going and you know, what, what are the hard
*  parts that we need to get over to get there? That was a great intuition. And we are hiring,
*  breaking down the query definitely is a way to do this. It's subtle how you break it down. But for
*  sure, that's, that's, I mean, certainly, I mean, that's how humans do it, right? Like, when you
*  have this very complex query with lots of modifiers in your head, you break it down into the right
*  components, and then you make sure everything matches each of those components. So yes,
*  that is a very good direction. Then there are other things that even that will not help with,
*  particularly if the knowledge is spread out across different documents. So, again, like just taking
*  that example, we've been working with like startups applying AI to law that are in the Bay
*  Area where the founders have rust experience. Now, on law and AI law websites, they don't usually
*  talk about the founders and their rust experience. So you need to combine information from other
*  parts of the web. And so doing that is where that's where you start unlocking like super high value.
*  And we have, you know, pretty clear ideas for how to do this. I don't want to get too deep into that.
*  But you basically you can imagine like a knowledge graph type approaches. And but like,
*  you don't want it to you don't ever want it to be a very discreet. You always want to be working in
*  like a neural like fuzzy world, because then it allows for like arbitrarily complex queries.
*  Whereas if you have like a knowledge graph that literally has Obama books that he's written,
*  those books have authors, like everything has like very discrete metadata, you're limited to
*  just that metadata where if everything is like, in like an embedding, you know, fuzzy space,
*  you could make complex queries over that graph. Training models to output things in embedding
*  space is I think just a there's like a massive set of unlocks they're coming for us. That seems
*  pretty clear to me. I still quite under explored. This is such a big unexplored space. Language
*  models have been explored for the generative in the generative area, generating text, generating
*  images, generating video, but really have not been explored too much in the improving the search
*  algorithm area area surprisingly, right, like there's a lot of value in it. And so it's just
*  like a lot of really, you know, like intuitive things like you thought of, like, haven't really
*  been fully explored. You don't get a lot of PhD students writing papers about web search anymore.
*  So it's just like, there's this whole space of possible solutions. You need a company with the
*  right incentives to go pursue it. Yeah, the best minds of our generation are elaborating chain of
*  thoughts still. So we've got to finish that up before we can get on to the next thing.
*  So the index is interesting in and of itself, right? The couple of things I've wondered about
*  as I've been researching the company using the product. One, from what I can tell online,
*  you've raised $5 million. I don't not trying to ask you to break any news here or share anything
*  new, but either you're managing to do a lot of indexing on a relatively small budget, or maybe
*  there's more funding behind that that is not public yet. But I was kind of just wondering,
*  how are you building a web scale index and doing what sound, you know, have a compute cluster?
*  Is it really on that small of a budget or is there are there more resources that you have
*  accumulated to make that possible? Yeah, we try to be frugal. And there are lots of optimizations
*  you can make that make this stuff not too crazy expensive. But yeah, we're not also we're not like
*  crawling the entire web right now. We're crawling a very high quality subset of the web,
*  the subset that our customers care about. And because we're not calling the whole web that
*  allows us, you know, as a lower resource startup to, you know, pursue algorithms that are more
*  complex, and to just do it all on a budget that makes sense. But yeah, like crawling like hundreds
*  of billions of web pages continuously, which is what Google has to do. That's quite expensive,
*  crawling, you know, a lot fewer and not on such a regular cadence. That's totally possible for
*  a startup. I think this is a problem that other startups have had in the past other search
*  startups, they've tried to, to early on like a be comprehensive, when you know, you're just going to
*  be okay at searching over everything, as opposed to really good at searching over a few things.
*  It's kind of like the advice of like, you know, do something that makes a few people love you as
*  opposed to do things that make a bunch of people like you for startups.
*  I've recently seen Brave, the browser company has an interesting offering where they basically have
*  a, I believe like a web index as well, but it's based on where people are browsing. I don't know
*  if you've seen that, but it kind of reminds me of what you are describing. And you could do
*  something much more heuristic based if you just said, Hey, let's look at Reddit and let's look
*  at archive and let's look at, you know, pick your favorite 50 websites and like the things
*  that people link to from there. I can see something like that also really taking you pretty far, but
*  if you've looked at the Brave thing, but it is specifically based on where people are going,
*  where they are spending their time. And, you know, that seems like a really interesting way to get
*  a view on what is actual real content that people value versus, and I imagine it's got to be,
*  you know, just given the proliferation of stuff in general, I imagine, you know, 90 plus percent
*  of time on the web must be spent on like under 10% of the pages, right? Yeah. Yeah. I don't know
*  the exact number there, but certainly the links that people share is an interesting metric for
*  what is high quality. So like our model is trained to predict what people share
*  and people often, no one shares SEO blog posts. People share like that really good recipe. They
*  don't share the SEO blog posts about a recipe that's like trying to, you know, that has all
*  sorts of ads on it. So our model is really trained to predict links that are just give you like raw
*  content as opposed to like putting all sorts of ads and like stupid information in it. So it's like,
*  yeah, it's like our model is trained to not predict SEO. And I like with Brave, it's like
*  people often spend time on the things that are not SEO. Let's talk about the business for a second.
*  I was initially kind of, I'm just looking at the pricing. It starts at basically $10 per 1000
*  searches. And that is if you want to get up to 25 results per, and then there's a higher price
*  if you want to get up to a hundred results, then you can, you know, things can go on and get more
*  elaborate from there. You've got the custom enterprise option for people that want to,
*  you know, to go beyond what the standard plans offer. My initial reaction to that was like,
*  it seems a little expensive. Like typically a API product these days is like one to $2 per 1000
*  calls. However, as I'm talking to you, and I'm thinking about this, I'm realizing that one thing
*  I've said, you know, in the context of Athena and the apps that we're building and the things that
*  we're trying to equip our assistants to do for their clients is almost every client that we have
*  has an opportunity, if not a pressing need to scale some sort of lookalike search.
*  Here's some good sales targets that we've sold to successfully. I want more like this. Not easy
*  to do. In today's world, you could go search LinkedIn, you could do a number of different
*  things, but definitely not easy. Similarly, here's a great candidate that we want more resumes like
*  this. Again, you can do that kind of on LinkedIn, but also not super easy. So I'm struck by those
*  two use cases being like super ubiquitous and imagining the more we talk, I'm like,
*  that sounds like a significant part of the business. And if the results are good, first of all,
*  for us at Athena with the assistance, it could really unlock their ability to do that effectively,
*  because a lot of times they struggle. It's like, yeah, we need an engineer with a certain
*  background and skill set or whatever. And it's like, a lot of times that flies right over the
*  head of the assistant when they're first getting started. They just don't know. And similarly,
*  sales target, what makes it good, what makes it not good. I imagine that there could be,
*  I wonder how you think about this when you're talking to customers about it, but it seems to
*  me like investing a little more on the quality of the results saves you potentially a lot in terms
*  of the iteration time to actually get something working and perhaps also the downstream language
*  model processing of the results. So anyway, that's all speculation. You can react to it,
*  but I guess, what are the kind of main business-wise, what are people really just coming back to and
*  doing over and over again? How are they reacting to the price and how do you think about your price
*  versus other kind of compliments in the overall systems that they're building?
*  One thing that's interesting is a lot of customers are searching over a particular domain of things.
*  So it's like, they're searching over only people or they're searching over only companies or
*  searching over only news articles. And so they want a search engine that just returns them those
*  things. So you just want a list of people that match your criteria. And it's just really hard to get
*  Google or Bing to do that. And so customers come to us because they use Bing, the Bing API or
*  wrappers on Google and they're like, this just doesn't give us what we want. And so we just,
*  we need you. And so a lot of the customers are coming to us because they just need this. There's
*  no other way to do it. And no one really complains about the price because it's just something they
*  need. We can always work something out at high volume with the enterprise plans and we've done
*  that. But yeah, it's just such a unique experience that we really see ourselves as like a premium
*  search, right? It's a search that you can't get anywhere else. So yeah, I mean, customers are
*  using us for those domains that I mentioned often, but in various ways, it's not just similarity
*  search. It's like, you know, all sorts of downstream use cases. They're like, it's too hard to,
*  to put them into one into particular patterns. Maybe you could put them into patterns of like
*  some retrieval, augmented generation use cases. Then there are automated analysis use cases.
*  And then there are even crazier ones like creating like, again, like hundreds of thousands of results
*  or even millions of results for fine tuning models. There are a lot of different types of
*  use cases of the same product. Yeah, interesting. I'm coming up with some more ideas. Just listening
*  to you describe that. And yeah, I mean, it's interesting, right? What's expensive? What's
*  cheap is where I think we're very much like getting used to a new regime here because on the one hand,
*  you know, one cent per API call could be considered expensive. On the other hand,
*  if you're comparing it to human labor, it's extremely cheap. So, you know, the quality is
*  obviously the real determining factor there. I'm not one, by the way, to emphasize the cost too
*  much. My general advice to people building apps is costs are coming down across the board. And
*  right now, the first question usually is, can you make something that meets your needs?
*  And I would do that using the very best tools, whether it's GPT-4 or XA, you know, whatever the
*  best tool is, like use that, maximize your performance first. And then later on, you can
*  upgrade to an enterprise plan for savings, or you can wait for savings to kind of just generally
*  secularly arrive, or you can optimize in any number of ways. But don't do that too early
*  because then you may miss the fact that like, maybe you could have actually built something
*  that worked and you, you know, you didn't even get there because you were too budget conscious
*  too soon. So I don't mean to suggest that I'd be too concerned about the price. My advice would be
*  to anyone listening, like, definitely use it if it is the best thing for you. And I think for a lot
*  of these use cases that we've been discussing, it seems, you know, like it very likely would be.
*  How do you handle evaluations? This seems like a challenge, you know, it's a challenge for every
*  AI startup. It seems like you have kind of a maybe a unique flavor of that challenge.
*  Yeah, this is a, this is a difficult problem because it's very subjective. So like, if you
*  evaluate XA on the types of queries that people use for Google, then obviously Google is going
*  to be better. And if you evaluate Google and types of queries that are great for XA,
*  then XA is going to be better. So like what distribution of queries are you sampling from?
*  And we have anecdotal evidence that, you know, a lot of our customers are, you know,
*  they're going to Google, it's failing them and then they come to us. But that's not a quantitative
*  metric. There are like, you know, web retrieval data sets, but again, they're often like, designed
*  for the old way of searching. So we really had to like come up with our own internal metrics
*  for comparing our search to other methods. And you know, one way to do it, one interesting way
*  is to break down instead of like, you know, just sampling queries and being like, is this good?
*  It's more you break down the model into different abilities that it could have that you want to have.
*  So like, for example, like you want it to be able to handle authorship. So if you say like essays
*  by Paul Graham, you get essays by Paul Graham, that's better because that's objective. Like
*  there's no subjectivity. Like does the result match that query, like authors by Paul Graham
*  or that part of the query? And so you could do other things like not just authorship, but topic,
*  you know, this is about space exploration and make sure it's about that. So if you break it down to
*  abilities, you've turned the subjective problem into an objective problem. There's, well, but
*  it's still like a lot of internal data sets. So nothing like, you can't find this kind of thing
*  on the web or sorry, on like, you know, open source data sets that you could then compare
*  benchmarks to. Interesting. Definitely a challenge. So internal, internal evals, basically.
*  How about the vector database technology? That's something that a lot of people are,
*  you know, one to two years behind you on where obviously you've been, you know, working on this
*  stuff for a while and have probably seen pros and cons and different trade-offs. A lot of people
*  right now are like, maybe are either about to or have just, you know, done their first vector
*  database prototype. How would you, I guess, you know, if you're, if you'd be open to sharing,
*  I'd be interested to know like specifically what are you using and you know, what are the kind of
*  most relevant trade-offs that you have encountered? If you don't want to go that deep, then I'd love
*  to just hear kind of what you have observed broadly, what you think people should be considering
*  when they're choosing a vector database and kind of where you think that class of technology is
*  going. Yeah, sure. So we build our own vector databases, just following the trend of building
*  vector databases. But I think we have a good reason because we're doing web scale search,
*  but it's particularly, we have all sorts of filters that we want to apply to the query. So
*  we're not just doing a simple, you know, nearest neighbor lookup. We're doing more complex things
*  than that. And so like these vector DBs were not designed for all the different types of filters we
*  want to apply. We, I mean, we, of course we have looked into the open source, vector DB, like
*  offerings and I just compared ours and you know, ours works way better for the type of
*  searches that we're doing. Definitely. Yeah. It's gone, it's gone through like multiple versions.
*  There is a, it's a really interesting problem. We've had a lot of fun with our own vector database.
*  One way you could think of what we're doing at Exa is we're kind of like trying to take all the
*  world's knowledge and putting it into a new type of database, like a neural database. I like this
*  database analogy because it's not really search. It's like, you're kind of like with every query
*  you're filtering the database of all the knowledge into just what you need. And so like when you
*  search for startups applying AI to law, you should get like 367 results. These are all the startups
*  applying AI to law. And when you add Bay Area, it's like a filter to the database. And now you
*  get like, instead of 367, it filters it to 54. And so just thinking about the world's knowledge as
*  a database, it makes it, it makes it feel like everything is actually like, like you have
*  comprehensive knowledge of what's out there. Cause a problem with, you know, search engines like Google
*  is like you search something and they say, you know, 33 million results at the top.
*  Like, what am I supposed to do with 33 million results? There's no way all these results are
*  actually what I'm asking for. So it's just like, you just feel overwhelmed. And then like,
*  the things that are returned are not actually exactly what you asked me asking for. So yeah,
*  anyway, so like we're trying to build like a new type of database that's like combines neural and
*  non-neural methods. And if you're, we're trying to do that, then it makes sense to build our own.
*  So combining a couple of the threads, it sounds like you're almost, if I had to guess it, it would
*  be like your vector database maybe has like multiple vector representations of each thing,
*  where there are like kind of projections in various directions. Like you have a certain
*  essay, but then you could project it in the authorship direction, or you could project it in
*  the, you know, you could project startups, you know, into a geographical direction. And then
*  that maybe starts to open up this like multi-dimensional query, but still staying
*  in like the fuzzy embedding space, as you said, is important earlier. Is that kind of the direction
*  that this is going? I think that would be, there would be a problem there because, you know,
*  there are a huge number of possible directions. So are you going to make an embedding for
*  authorship and embedding for topic? Like that would be like, that would be, that wouldn't work. So you
*  need to be, you need a more general method. But yeah, these are definitely the types of things
*  we think about all the time. And so let's say you did do it that way, then you now have like
*  multiple embeddings per document. And like, okay, so you want to search with the first embedding,
*  but then you also want to use the second embedding as a filter. Like a lot of these open source
*  libraries don't support that type of thing. So that's exactly the type of thinking that made us
*  want to build our own and have really have full control over, you know, okay, now we want to
*  introduce keyword filters and we want it to be, you know, just as performance. And we don't have to,
*  we don't want to have to deal with all like the problems that they face because they were building
*  a more general thing, like, or like the slowness that that introduces using an open source library,
*  because they're building a library that's meant for the very general use case. Whereas we have a
*  very specific type of use case. Like when you have a very specific use case, you're going to be able
*  to optimize your system more than the general use case. And in our case, optimizing it 2x or 5x has
*  massive returns. So, so do you think you would ever sell the database as a product? I mean,
*  there's obviously huge opportunity, you know, just in that element of the stack, right? So it's,
*  it's interesting to, obviously you guys have a high level of ambition for what you're doing.
*  And I wanted to ask a little bit about the company culture as well. But the, you know,
*  you're not that big of a team, not that many, you know, financial resources brought on so far.
*  And I guess I'm a little surprised you're doing your own vector database, although I understand
*  the rationale behind it. But you know, one might say like, geez, could that be a product unto itself?
*  I suppose. But I think our team is really focused on this mission, like this particular mission of,
*  we want to filter the all that information to the world to the knowledge you need. And we feel that
*  that's going to be magical and have huge implications for the world. And so we don't
*  want to get distracted by like, selling vector DBs or something like that. It is true that to
*  build what we're building, like we had to make some like super performance systems all across
*  the stack. You know, we crawl the web, we have really clever ways for calling the web, we parse
*  it well, we train, you know, again, train our own models for search, and then we serve it in production
*  extremely quickly. So all those parts are like valuable in their own way. But we just want to
*  focus on that, that mission, which is just like, oh yeah, allow all the world's information to be
*  filtered to the knowledge that you need as fast as possible. Companies our size have to focus
*  their product on one thing, like we can't be selling like vector DBs. And then also like doing
*  selling search and like selling the crawler or something like that. It makes sense to focus.
*  We are a small team. We work extremely hard. I mean, every startup is going to say that, but
*  we work very intensely. We're people who are just super excited about the technology. Like it just
*  doesn't feel like work, you know, it's just really fun. We have to be working on a problem that
*  requires very interesting technologies and very unexplored space. So yeah, it's just a great time.
*  And I think that's how small teams are able to move so fast is when they're just like having a
*  blast and like thinking about it in the shower. And you know, if you're a 50 person team and you
*  treat it like work, you're going to move way slower than a seven person team that treats it like clay.
*  Yeah, I can totally relate to that. I have probably never worked harder than I have
*  over the last couple of years. And it has felt much less effortful than various times in the past
*  because I just love learning about this technology and building stuff. And you know, there's always,
*  if I ever get tired of one, at least in the approach that I take, which is very kind of
*  interdisciplinary and I call it scouting. So I'm always kind of looking for new angles.
*  If I ever get tired of one angle, you know, there are plenty of different angles that I can
*  switch over to. And you know, there's always something interesting to discover. From the
*  careers page, interesting sentences. We are a growing family of highly technical idealists
*  on a very practical mission. And then you've got five core values as well. One thing that stands
*  out also is like you're a pretty young team. You guys even are like, some of you are living together
*  in a, you know, shared house, which is also, I guess, kind of the office. So that's interesting.
*  And that's like, maybe it was out of fashion for a minute, maybe it started to come back into fashion,
*  but you've heard Sam Altman say like, you know, the founders are getting older. So you're kind of
*  bucking that trend a little bit with this, like, let's do it in our twenties. Let's, you know,
*  be super intense and just like, you know, eat and breathe this stuff nonstop. You can talk more
*  about that if you want, but the two core values also that jumped out to me were perform with an
*  optimal speed, accuracy, trade-off, and also wield great power responsibly. You can correct it again,
*  any of that, however you'd like, but I'd love to know what is the optimal speed,
*  accuracy, trade-off, or do you have a framework for thinking about it? I'd love to know that for
*  myself. And I'm also curious about like the power, you know, what sort of power do you expect to have?
*  You know, what are the concerns that you're starting to prepare for?
*  Yeah. So you're referring to the values. So it was an interesting thing to think of values
*  for the company culture that match the product we're trying to build. Very effective. So yeah,
*  and that too you mentioned are interesting ones. So like compute speed trade-off is something that
*  matters a lot in our system because ultimately like not every, so from the product perspective,
*  like not every query should require the same amount of compute. Like Google has kind of made
*  this assumption that like no matter what query you type in, it takes a few hundred milliseconds,
*  but certain queries are extremely complex and might require like scouring the internet
*  for, you know, maybe even seconds or minutes. And so you want, you do, if you want to have an
*  optimal search engine, you will have to make this trade-off between speed and compute.
*  And then from, okay, but how does that relate to company culture? Well, I mean, constantly as a
*  startup, you're facing problems that, you know, you could spend a year on or you could spend a day on.
*  So you could like, there's a speed, compute in this sense is like how much
*  brain power effort you put into it. And often the right approach in a startup is just like,
*  you know, like let's, let's do that. Like it's just move fast. It's really the move fast,
*  break things type mentality. But I think thinking of it as more, the optimal trade-off is cool.
*  It's like, you're always optimizing for exactly the amount of effort to put into the thing,
*  as opposed to like always moving fast and breaking things. It's like, no, sometimes we need,
*  we do need to think for a day about the right approach. So I like, I like optimize the trade-off
*  better than like just move fast, break them, but it is the same type of idea. And then the
*  wield power responsibly. Yeah. I mean, we are as builders of a search engine, we are like,
*  we are the doorways to the world's knowledge for people. And, you know, imagine everyone was using
*  XR every business was using XR. We control the information, the knowledge they see that is like
*  extremely powerful. I mean, like people who control knowledge, control power. And so we have to think
*  very carefully about how do we do that in a way that isn't biased? How do we do that in a way that
*  doesn't like create a negative downstream effects? Because I mean, Google, Google has like huge,
*  that has had huge downstream effects on the web. It like influences the type of content people even
*  create. And much more important is like it influences the type of content people are aware of.
*  Our philosophy is give users full power to get what they want. So as opposed to like, you know,
*  biasing the web, biasing the results towards like, what we think is right, we want to give users the
*  power to explicitly say what they want. And so, I mean, there are interesting moral questions there,
*  but I do think that's, that's the right approach. And it's that's now possible, like, to with, you
*  know, transformer like technology, you can like actually just give people exactly what they ask
*  for. And you could like, you know, for every search, like recommend like, hey, like, by the way,
*  you know, you're searching for this thing, but like a lot of people have noticed that this has
*  all sorts of problems kind of like with Twitter and like the reader's suggestions or whatever,
*  whatever it's called, that's really helpful. But yeah, ultimately, like give users the power to
*  find anything they want, no matter how complex is, I think the best way to wield that power.
*  Do you expect there to be a dominant player in the future? Or do you expect kind of a
*  more multipolar information and knowledge finding ecosystem?
*  I think we're going to be the dominant. I think certainly the market is going to expand so that
*  the market for knowledge for information retrieval is actually going to get way bigger.
*  And so there's definitely room for more players in a way that there wasn't before. So I could see it,
*  I could see there being multiple players, but but still you do get benefits of scale.
*  I would say it's more likely than before that there'll be multiple players.
*  Anything else you want to touch on though briefly before we break?
*  If you're listening to this, you know, we're hiring for all sorts of super cool roles,
*  and we build some of the coolest technology in the world as a small startup. So would love to just
*  get the best people to join us and build the future of information review.
*  Love it. Will Brick, founder of Exa AI, thank you for being part of the cognitive revolution.
*  All right. Thanks.
*  It is both energizing and enlightening to hear why people listen and learn what they value about
*  the show. So please don't hesitate to reach out via email at tcr at turpentine.co,
*  or you can DM me on the social media platform of your choice.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki so much
*  that I invested in it, and I recommend you use it too. Use Cogrev to get a 10% discount.
