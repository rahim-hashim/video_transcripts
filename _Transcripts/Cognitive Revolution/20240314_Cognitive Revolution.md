---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 5317s
Video Keywords: []
Video Views: 1063
Video Rating: None
---

# AI and the Practice of Law: from CaseText to CoCounsel, with Pablo Arredondo, VP of CoCounsel
**Cognitive Revolution "How AI Changes Everything":** [March 14, 2024](https://www.youtube.com/watch?v=pfMCtu_ppno)
*  The first flickers of the power of this technology that I saw was suddenly the computer flagging
*  instances. And I was like, wait, how does it know that that means overrule? Because that is not
*  a normal way to say it. And it was because we had moved beyond literal keywords. My co-founder,
*  Jake and I were shown a demo of GBT-4. And within 12 hours, we had pivoted the entire company
*  around it. A lot of times you'll hear people say, all that will be automated is the menial work that
*  nobody wants to do anyway, right? But they can also help for things that are like deeply
*  substantive, like really, you know, finding inconsistencies so you can go do the like famous
*  cross-examination that destroys the witness. Hello, and welcome back to Turpentine AI.
*  If you're looking for the cognitive revolution, don't worry, it's not you, it's us. Turpentine
*  is developing fresh new AI focused shows. And this feed is set to become a best of show featuring
*  highlights from multiple sources. Meanwhile, we've created a new feed dedicated to the cognitive
*  revolution, which you can find and subscribe to at our website, cognitiverevolution.ai.
*  Just yesterday, we posted an interview with Andrew Lee, founder and CEO of email client
*  shortwave, which has the single best AI email assistant that I've personally used, and has
*  become the first email client to effectively replace the Gmail web app as my go-to email
*  experience. Definitely take a minute to visit cognitiverevolution.ai to subscribe for that and
*  plenty more original content, which will only be available on the new feed. Today, exclusively on
*  this feed, we're looking at how AI is impacting the practice of law with Pablo Arredondo, who helped
*  create and drive the adoption of AI and other advanced legal search tools as co-founder of
*  Case Text, and today is doing the same with large language models as VP of co-counsel at
*  Thomson Reuters, which acquired Case Text last year. We begin the conversation with a historical
*  overview of legal research from its pre-digital citation-based origins to the computerized,
*  but still fundamentally keyword driven search era through the last 10 years of Case Text and
*  the AI powered innovations that allowed attorneys to search no longer just by keyword, but by
*  meaning, dramatically improving their ability to locate relevant case law, and finally on to the
*  present day, in which large language models are beginning to fundamentally change how lawyers
*  perform an ever-growing range of high-value tasks, including document review and deposition prep,
*  contract review, and more. We talk about Pablo and team's first exposure to GPT-4, how they
*  immediately pivoted the company to take advantage of this new technology, and how they've designed
*  their product, and perhaps more importantly, their product development and quality assurance
*  processes with reliability in mind. We also discuss why co-counsel's price point, which is
*  a couple hundred dollars per attorney per month, is not really a problem given the high-value use
*  case that they serve, and why Pablo has remained a GPT-4 maximalist, at least as of the time that
*  we recorded a couple weeks ago, just before CLAWD 3 was released. Pablo also shares his thoughts on
*  the future of legal billing, the potential for AI-powered arbitration, and the evolving regulatory
*  landscape governing the use of AI in the legal profession. While he is, as you'd expect from a
*  VP at a major company like Thomson Reuters, extremely focused on responsible development
*  and deployment, his hope is that large language models can make legal services faster, less
*  expensive, more accessible, and higher quality for all. As always, we appreciate it when you take a
*  moment to share the show with your friends. This episode would be an obvious fit for the lawyers
*  in your life. And again, please do make sure to subscribe to our new feed, which you can find
*  at cognitiverevolution.ai. We'll have original content both here and there over the coming weeks,
*  so you'll definitely want to stay tuned to both feeds. Now, here's my conversation with Pablo
*  Arredondo, co-founder of Case Text and VP of Co-Counsel at Thomson Reuters. Pablo Arredondo,
*  co-founder of Case Text and VP of Co-Counsel. Welcome to the Cognitive Revolution.
*  Thank you so much for having me.
*  I'm excited about this. We've got what I think is going to be a really interesting and hopefully,
*  you know, it'll be a good mix of fast-paced and deep diving into all things legal AI. And,
*  you know, you've had a real front row seat in this business over the last 10 years,
*  since you founded Case Text. I would love to start if you would give us kind of a backstory
*  on just a brief history of the application of maybe technology more broadly, but obviously,
*  especially emphasis on AI in the legal profession. I realized that, you know,
*  while I've been into the product and played with it today, and we'll get into that in a lot more
*  detail, I don't really know that much about how things were before. If, you know, I kind of know
*  the Abe Lincoln story of like he had to walk a long way, I think, to borrow books and return them.
*  That's kind of all I know. Like, where are we coming from in legal research? And where have
*  you been over the last 10 years with Case Text? And you can take us all the way up to present.
*  Yeah, absolutely. So, you know, last sort of an interesting area, because you had some things
*  in law much sooner than you had them in other places. So like a citation graph, right? Things
*  citing to other things like that, that we now think it was like hyperlinks on the internet.
*  Not many corporate ministry had that in the same sort of like rigorous systematic way
*  that law had because you were constantly citing to earlier opinions, right? And citing specific
*  pages on earlier opinions, and it was always sort of building on itself. And, you know, very, very
*  quickly, especially in America, which, you know, had an explosion of lawyers and the kind of
*  litigation, there were quickly more judicial opinions than anyone could read in their lifetime.
*  And so you immediately started to have these sort of information retrieval problem and challenges.
*  How do you find the right cases? And not just finding the right cases? How do you know if the
*  case you're looking at is still good law? And, you know, one of the very earliest sort of legal
*  innovations was a guy named Simon Greenleaf. This was so long ago. So he was in the town of
*  Gray in the territory of Maine. So it wasn't a state yet. And it was so long ago that there
*  wasn't any American case letter reliant. So we decided to British case like, because, you know,
*  I didn't cite to something. And he cited a case that had actually been overruled by subsequent
*  courts. Essentially, the courts had later said that's no longer good law. And the judge, you
*  know, threw him around the courtroom and he was embarrassed. And he came up, I'm taking a little
*  artistic license here. But you know, he came back, he was really, he said, you know, I never want to
*  feel embarrassed like this again. But how do I know what cases have been overruled, right? Like,
*  I can't read every case and know them. And so he created this, this started to make a list of these
*  cases have been overruled by this case. And so this, I think, in the late 1800s, was the sort of
*  early example of a legal tool that then grew and grew and grew, and became this resource, the sort
*  of meta resource that lawyers could use to try to just better navigate the law and better represent
*  their clients. Later, we're going to see that our first use of large language models, like case text
*  was actually because we were putting our shoulder to exactly that challenge that was there in the
*  late 1800s. But I think a couple of things that in between that I think are worth noting, it used to
*  be that case law, you know, at first judges literally weren't even writing things down. It
*  was sort of be like, Hey, I think I remember Fred said something about that, you know, that that's
*  how common law was handed down. Then they started writing it down in very hodgepodge ways, you know,
*  you'd have like, crazy things like like an almanac, you know, and they like the guy doing the
*  almanac would also write, you know, reports, or see, like, then Judge Mansfield held that the by,
*  by the way, I think we'll have a great crop of poor, just complete mess. Until you had this West
*  publishing, and this guy, Jonathan West, who is now Thompson Reuters is sort of the continuation
*  of all of this, who first systematized the case law into these reporters. And so whenever you see
*  a lawyer doing his commercial, or kind of on TV, and he's got those books behind him, those are all
*  this sort of systematically, let's take all the case law, let's put it into one form, into one
*  series of books, and start to make it much more navigable. But of course, this was long before
*  computers. And so the question now is, how do I find the right case? And so you had this taxonomy
*  that was created by humans, who went and went thoughtically and said, Okay, we're going to
*  divide up law into all these different areas, and we'll create this sort of flow, this taxonomy,
*  you know, I'm looking for torts, okay, somebody's been injured, okay, now I'm looking for animal
*  attack, okay, now I'm looking for dog. And this was quite useful, because it could help you find
*  what you needed. But it was also a prison of sorts. Because however they divided up the law,
*  that was what the law was, right, you had to stick to whatever framework they had. And so that was
*  the governing paradigm for legal informatics for a while, until the very late 60s, early 70s,
*  when you started to see the digitization of case law. And so there you had a company now that is
*  Lexis, you know, this actually came out of, I think, a group in Ohio that started with just like the
*  Department of Agriculture, and I don't know, I'm blanking on the specifics, but essentially,
*  sort of small limited project became then suddenly, you now had everything digitized.
*  And so this was a huge step forward, in some ways, but also brought in other challenges. So now,
*  I could navigate the millions of opinions just by searching a keyword, right, whatever keyword I
*  want. And then you've gone into Boolean searching, you know, patent within sentence of computer.
*  And so you can now search using keywords. But as we all know, keywords are quite limited. They're
*  very literal. And you had issues of both precision, which is to say, things that came back just
*  happened to have that word, but weren't what you cared about. And you had more insidious was issues
*  of recall, there were things you did want to see, but you don't see because it happened to use
*  different language. And that was really the paradigm through when I was practicing, I was a
*  patent lawyer at Kirkland and Ellis, you know, that's what's kind of surrounded me during my
*  time practicing law. And so, okay, so now we're kind of starting to get closer to kind of case
*  text in these new sort of systems. And I'm going to be nerding out on this, because I'm assuming
*  your audience doesn't mind nerding out. I hope that's okay. Yeah, no, we're here for it. People
*  want the nuggets, you know, they want to a lot of them are building their own tools, obviously,
*  in, you know, many different areas. So they want to learn from the depths of your experience in
*  particular. All right. Yeah. I mean, you know, and so, you know, the early stuff that we were
*  doing with case text. So one of the issues we had was to remember, I talked about like knowing does
*  this case overrule this case, right? That became this very important tool called a citator. The
*  famous one was called Shepard's and then that got bought by Lexis. Thompson Reuters has theirs
*  versus Keysight, really essential system. But the issue with it with both of them at the time,
*  and case six got it started, is that it was only looking at the direct citation path. You can only
*  see cases that directly cited to your case to get a sense for that area of law and how things are
*  being treated. And the analogy I make is imagine you went to a video store, like some of you have
*  never heard of these, but there used to be a time when you'd go into movies. And you ask the clerk,
*  you know, I really am interested in the God, I love the Godfather. Can you recommend any other
*  movies? And imagine the clerk said Godfather part two, Godfather part three, that's the end of the
*  list. And you'd say, well, wait a minute, right? Like, that's a pretty impoverished list based on
*  that, right? What about Goodfellas? What about Meets? What about all these other movies? And so
*  one of the things early things we did at Case Tech this last decade was exploit the same patterns
*  that you had been seeing in Spotify and Amazon, which are these soft citation relationships, right?
*  When Spotify recommends a song, it's not because that song literally references this other song,
*  but you were like, it's that people who download this song tend to also download that song, right?
*  And so that sort of soft citation relationship was this big blind spot. And our first commercial
*  product was you could take the brief, right? The lengthy document that lawyers use when they're
*  trying to persuade the court. And we would analyze all the citate cases you do cite, and then run a
*  much more robust citation analysis. And then we could suggest cases that you had overlooked,
*  cases that weren't in the brief, but that you should have read these early moments where at
*  the top firms, firms that have no money, money, not an object relative to the stakes of the
*  litigation. I mean, right? They buy all the tools that they thought could help their clients.
*  They were saying, we were missing this case. How did we miss this case? We have the best attorneys,
*  et cetera. And it was just because the technology they were using had this blind spot. So we started
*  then selling these kind of specific technologies to the top firms, the very, the affluent firms.
*  But at the same time, we found that there were also a lot of attorneys who couldn't afford the
*  best, the West laws, right? And they were relying on like Google Scholar. They were relying on tools,
*  frankly, that could have been a lot better. And so we then decided we wanted to build out a full
*  fledged research system that they could use for all of the different things you need to do for
*  research. And so we ended up in this sort of bimodal place. There's this great Jack Daniels
*  commercial where it opens with them like serving Jack Daniels at the Ritz at some wedding.
*  And then it shows like a biker bar, you know, and all the bikers. And they're also doing Jack
*  Daniels. And it says like Jack Daniels served in fine establishment and questionable joints
*  since like 1870 or whatever. So K-Stick sort of was this sort of thing where we were at like the
*  Manhattan skyscraper firms, you know, representing antitrust, you know, eight-figure litigations.
*  But also increasingly, you could find this in like the street malls of Pasadena or wherever,
*  you know, solos were hanging their shingle, also doing very important work, of course, right?
*  Because it's also very important that folks who don't have deep pockets have representation.
*  Okay. In creating that full-fledged research engine, we needed to do what exactly what that
*  lawyer from the 1800s, Simon Greenleaf, did. We had to know does this case overrule this case?
*  Because then we can warn the attorney when they're reading it. And sometimes the court will be very
*  explicit. They'll say, we overruled Jack Daniels. Great. Easy to parse. But sometimes the court will
*  say, we regretfully consigned Jenkins to the dustbin of oblivion because judges can say it
*  however they want. And sometimes they like to get poetic. And so now we had this really profound
*  information challenge. How do you get a computer to detect that kind of overruling, that kind of
*  treatment where it's not using the normal words? And to be clear, this was part of a process that
*  involves humans. There was very much a human in the loop, but how do you triage? How do you identify
*  humans should take a look at this? Okay. So we're trying to do this. We're using kind of old
*  techniques and then rejoice. Here comes BERT. Here comes large language models. And our first
*  experience, the first flickers of the power of this technology that I saw was suddenly the
*  computer flagging instances. And I was like, wait, how does it know that that means overrule? Because
*  that is not a normal way to say it. And it was because we had moved beyond literal keywords,
*  because this language model was starting to actually understand. There's a whole debate
*  about understand versus not. And truthfully, when we're talking about things like BERT,
*  I think it was more just that we had encoded language in such a way that it would draw in
*  these examples. And so that was the beginning, I think 2018-ish, very, very early on of these
*  large language models. Hey, we'll continue our interview in a moment after a word from our
*  sponsors.
*  I'm
*  going to key uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button. I believe in Omniki so
*  much that I invested in it. And I recommend you use it to use cog rev to get a 10% discount.
*  Quick interjection, because I don't know the history on BERT. Did they open source it for you
*  or was it, were you just able to, so you were able to get a trained BERT to work from, from the
*  beginning? Yes. And we, so this is one of these great moments that really shifted, I think,
*  society in some ways. And unfortunately, and this is probably, there's better folks than myself to
*  talk about that sort of aspect of things, but less and less, I think, are people kind of putting out
*  there and open sourcing, at least certain aspects of it. I know there's a lot of open source movement
*  in AI, but you know, I don't think Google's open sourcing Gemini, let's put it that way, right?
*  But yes, they put out BERT as a paper, Jacob Devlin, the code was there, the techniques were
*  sort of just, it was all just, you can go do it. And what we did is we actually took that same
*  approach and just trained it on US common law, right? But basically took directly from Google,
*  the techniques, the approach, and then frankly, I think some of the code as well to kind of run it.
*  And that was a pretty, you know, just an incredible moment for us. And everything we're doing now is
*  really sort of just this evolution. Sometimes like punctuated equilibrium, right? It's not just
*  linear, it's like, whoa, right, but very much in sort of the same path that started with BERT.
*  And so once we saw that it could do this for detecting overruling treatment, we said, okay,
*  wait a minute, now we can do this for search. And so we created this engine called parallel search
*  where attorney could just enter a full sentence, could take a sentence from your brief, and it
*  would find relevant case law, even if there was no overlap in the keywords at all. Right? And so,
*  like we had a demo sentence we did about Miley Cyrus getting fired, or we used Cyrus as the name,
*  it wasn't Miley Cyrus, but you know, getting somebody being fired for not wearing a mask at
*  work. And suddenly it was finding cases where people weren't putting on safety helmets readily,
*  like it was finding analogous case law, right? Things about sartorial safety, right? Things
*  like that. And for lawyers who had basically been in what I theatrically call the keyword prison,
*  this was as seismic an event as you can imagine. At the time, I thought you will never get more
*  seismic than this. Boy, was I wrong, and we'll get to 2022 in a second. And so we released this
*  parallel search, and it just immediately was a huge hit. Courts were using it, firms big and small.
*  Amla, adoption Amla just means the biggest 200 firms. Getting lawyers to take time to adopt new
*  technology, it's a hard fight, right? They're busy folks, they're risk adverse, etc. Parallel search
*  was this example of one that you just saw kind of spreading, and it was absolutely beautiful.
*  But it was because it's so often lawyers are trying to find something, but they don't know
*  the exact words. And so we did it for case law first, then we expanded it so that you could
*  upload anything transcripts, e-discovery, right contracts, whatever you wanted, and apply these
*  these sort of early language models to them. GPT-3 happens, I think that's 2020. We see it,
*  well, wow, that's really neat. 10 minutes later, though, we know we can't use it for lawyers. It's
*  just not there, right? Amazing kind of, you know, kind of sense of like, oh, wow, but not reliable
*  enough, not nuanced enough, just not good enough to be something for attorneys. And so we, you know,
*  continued focusing on our search systems and kind of doing that stuff. And then one glorious day,
*  September 16, 2022, my co-founder Jake and I were shown a demo of GPT-4. And within 12 hours,
*  we had pivoted the entire company around it. It was just so much better than what we had used
*  before or seen before. And unlike our BERT systems, which were really just about search,
*  this tool was being used for like, you could summarize, you could create timelines, right?
*  We had this, we had this period where, and remember, this is before chat GPT came out.
*  And chat GPT was based on GPT-3.5. And at some point later, Sam said, like, you know, we broke
*  it up because we thought it would be too much to see chat and GPT-4 at the same time. Well,
*  we were the absolute privilege of being the small group that got both barrels. So we went,
*  you know, suddenly we were on a Slack channel where we could ask GPT-4 to, you know, create a
*  timeline or change this or chat. I mean, we just, the next 72 hours, I felt like I was going to
*  burn a hole in my brain from just how many things we tried and how many, you know, it was just
*  incredible to see what it could do. And so we pivoted the entire company around it. And we just
*  worked hand in hand with OpenAI, you know, giving them feedback from lawyers. We were like their
*  domain experts for law. What we realized though, of course, early on is you can't use this stuff.
*  You can't use GPT-4 as a chat bot for law because it hallucinates, because it's not up to date.
*  I asked it about a case I actually worked on. And its answer was so believable that I was
*  second guessing myself about a case I worked on. And then I kind of got mad and I was like,
*  no, you're wrong. I worked on this case. And I kid you not, it said, you can sit there and
*  brag about the cases you worked on if you want, but I'm right. And here's proof. And then it can
*  talk to the URL to nowhere. Right. And so you're wet. This is, you know, but you can't use it like
*  that. It will hallucinate. It will make things up. And so, you know, from the very earliest days,
*  we understood you had to use what now I think is, you know, very common. Everyone kind of, I think,
*  you know, becoming almost like, you know, just to retrieve a logmete generation, you have to anchor
*  the system in a search engine that will retrieve real results and then force GPT-4 to answer based
*  on what it's seeing in front of it, the real case law, not freestyling an answer.
*  I had a very similar experience. You know, I was in that same time frame as an early open AI customer,
*  you know, got a preview and had an uncannily similar experience where I was asking it about
*  chemistry research. I had been a chemistry student as an undergrad and asked about the research
*  agenda of the professor that I worked for and asked if she ever had a co-author, you know,
*  named the little Benz, namely, you know, meeting me. And it said yes. And what paper? And it gave
*  me the paper. And I was like, wait a second, did she put me on another paper that I don't even
*  recall being a part of? And then this was kind of the, you know, the entry point for me to
*  understanding hallucinations. Not that I necessarily thought it was infallible before, but it was like,
*  whoa, you really have to be careful because here I am. You know, and I think it was the middle of
*  the night as I'm kind of, because I was also, you know, like you just really floored and just wowed
*  and, you know, not sleeping a lot for a few days there at least really for a couple months. Yeah,
*  I remember being like, this is so believable. It's confused me as to whether or not I was
*  actually involved in this. I had to go, you know, look it up for real and kind of reground myself
*  on what was I actually a part of, you know, a few years back. So yeah, it's very uncanny similarity,
*  similar experience. I mean, we were fortunate that we got to get tricked by it very early on in like
*  the lab, you know, since later, you know, these horror stories of the lawyers who like went into
*  court, you know, relying on it. There were startups that were like putting out marketing
*  with hallucinations in it. Like they were putting out their screenshots and it's like, that's not a
*  real case. So it definitely took a lot of while to kind of get there. Right. So we put this out. So
*  then, you know, and the truth is like, it was so amazing that there was always this voice like,
*  is this real? Can this really be real? Right? Like it can't, all these things can't really be
*  happening, right? Because it's just, it was frankly so unexpected. I think even the really
*  enthusiastic folks weren't anticipating maybe somewhere, but I certainly, because I mean,
*  weren't anticipating the leap that was GBT-4. And for me, the, you know, I was a co-author of the
*  study where it passed the bar exam, right? We got kind of ran out with some colleagues I knew from
*  Stanford. But to me, what really drove home that it was real was when we brought it to legal research
*  and the law librarian community did not rip it to shreds. And in fact, you know, they would say
*  things like, this is solid. That is the most gushing praise I've ever heard from a law librarian
*  on anything. I mean, they live to tear things like this apart and to see them sort of say, wow,
*  it actually seems to be able to deal with the nuance, you know, of different areas of law and
*  it's understanding these queries. That's when I was like, okay, wow, this is actually happening.
*  And, you know, that really helped. So, you know, early days, so first we had six weeks before
*  CHAT GBT came out. So now we're getting to show very limited, I mean, you know, but I understandably
*  there was a very small group that we were allowed to kind of share it with. But, you know, this was
*  a time where you could just demo the poems and people were floored. You were showing them
*  everything. They'd never seen LLMs in any capacity. So you could just show them poems and show it
*  translating and things like that, even before you got into legal tasks. And they were kind of blown
*  away. They were, you know, is a cyber dime. There was all of that sort of angst, you know, and it,
*  you know, one of the unique perspectives that we got because we had this early access was seeing
*  a lot of people's first reaction to just LLMs as a whole. And that mix of excitement and sort of fear,
*  right, and confusion. And I think there's something kind of uniquely human about language.
*  So when you see a computer for the first time doing it, it's something, right. And even though,
*  like, obviously, it's just guessing the next word, but just having it even mimic language so well
*  was unnerving, I think, to a lot of people. And so then we started, you know, basically,
*  we built out these different skills. We just took use case after use case after use case,
*  packaged them all together as Co-Counsel was the name of the product, you know, obviously,
*  an homage to Co-Pilot. And, you know, that's been basically what has been going on. It's been so
*  different. The debut of Co-Counsel was on Morning Joe on MSNBC. The idea of a legal tech product
*  going on national TV for its launch, right, it would have just been absurd. Morning Joe wasn't
*  calling when we had the citation, you know, blind spot, the just the amplitude, just how much
*  fervor and excitement and suddenly, you know, I'm used to giving demos, you give it to one
*  law librarian and they go, that's kind of neat. You know, in three weeks, I'll let another law
*  librarian see it, right. That's your traditional legal tech. Here, you'd show it and like all the
*  partners would all assemble like in the room, like somebody's been in Bezeling or something,
*  you know, maybe like just completely different a sense of it. And what we, you know, really had to
*  focus on is being responsible with it, not having it claiming it can do things it can't,
*  really putting the guardrails to make sure that it wasn't hallucinating or at least like, you know,
*  de minimis amount of hallucination, you know, things like policing the results for quote checks,
*  like using old school tech to be like, does that quote actually appear in that case?
*  And then really creating a system that facilitates oversight because the danger, of course, is
*  attorneys over relying on this stuff, right. Because it's so seems so good and seems so,
*  oh, it's done when in fact, you know, it's not quite at human level. I shouldn't say not quite.
*  It's not near human level, ultimately, for like really important legal thinking and reasoning.
*  I think it has a ways to go. Let's get into the product in more depth. I mean, it's really
*  interesting. You obviously had very early start and, you know, I've had a chance to go in and
*  play with the product hands on. Now I'm not a lawyer myself and I also don't have like a lot of
*  legal documents, you know, lying around. So I couldn't necessarily push it to, you know,
*  the limits that your actual customers would. But definitely a number of things jumped out at me.
*  One is that you've kind of been building a lot of the same things that the community as a whole has
*  been building, but probably in parallel because being early to it, you didn't have the luxury of,
*  you know, a lane chain or a llama index or whatever, you know, at the time you're building,
*  right? So you're identifying these problems kind of in your own, you know, lane as the community
*  more broadly is also figuring out, you know, what are the complementary tools that the language
*  models need. I'm interested to get your kind of perspective on a number of different dimensions
*  of that. Maybe for starters, let's just kind of describe what the product experience is.
*  I think there's a couple of things about it that are notable. One is that it is just a lot more
*  structured than your typical chat. So it's not just, there's kind of two tabs as the main
*  interface. There's the chat tab where you're going back and forth and that will feel, you know,
*  very familiar to anyone who's used chat GPT. And then there is the results tab. And this is where,
*  you know, from the chat tab, you essentially can create tasks. And, you know, this is an interactive
*  experience where, you know, you're having dialogue, the system can kind of come back and say, okay,
*  here's what tasks I understand you to be asking me to do. And then you can say, yep, okay, go do
*  those tasks. And then those tasks actually get run, seemingly kind of in the background or in
*  parallel. And you know, you can elaborate a little bit more on the kinds of tasks and the volume of
*  tasks that people are putting through those. And then you can come back in a little bit and actually
*  look at the results. So that way it is a little bit more of a, I often talk about kind of copilot
*  mode being your real time interactive engagement with AI and then delegation mode on the other hand,
*  being, you know, if you're setting up like workflows, and you're trying to get to the
*  point where you're not going to check every single output, I call that delegation mode.
*  And that's like much more prompt engineering, much more systems integration, etc, etc. This,
*  I think lives in a kind of interesting space in between where you're in that chat real time
*  interactive mode, but you're able to kind of spin off these individual tasks. And then they
*  actually live somewhere else that you can come back to and review. What are the tasks, you know,
*  that people are doing and in what kind of volume, you know, where are people finding the most value
*  from this product experience today? Hey, we'll continue our interview in a moment after a word
*  from our sponsors. The Brave Search API brings affordable developer access to the Brave Search
*  index, an independent index of the web with over 20 billion web pages. So what makes the Brave Search
*  index stand out? One, it's entirely independent and built from scratch. That means no big tech
*  biases or extortionate prices. Two, it's built on real page visits from actual humans, collected
*  anonymously, of course, which filters out tons of junk data. And three, the index is refreshed with
*  tens of millions of pages daily. So it always has accurate up to date information. The Brave Search
*  API can be used to assemble a data set to train your AI models and help with retrieval augmentation
*  at the time of inference, all while remaining affordable with developer first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data
*  sourcing and more human representative data sets. Try the Brave Search API for free for up to 2000
*  queries per month at brave.com slash API. Hey, everyone, Eric here, the founder of Turpentine,
*  the network that produces the cognitive revolution. This episode is brought to you by
*  ODF, where top founders get their start. ODF has helped over 1000 companies like Traba, Levels,
*  and Finch meet their co-founders and go on to raise over $2 billion. Apply to the next cohort
*  of ODF and go from idea to conviction on what's next. Startups change the world. They can also
*  change your life. Is it your turn? Learn more at beyondec.com slash revolution.
*  When we started at first, it was just buttons for each skill. There wasn't basically a chat,
*  right? You had a button called legal research, you had a button called review documents.
*  And what we realized is that people like the chat flow. The chat is sort of just a more
*  intuitive and natural way to kind of do that. And so then we've switched maybe a few months ago
*  to having the first thing you interact with be chat. And that raises challenges, right? You have
*  to understand the intent, you know, what are they actually asking you to do, right? Whereas it's
*  simpler if you just hit a button. And then we sort of realized, well, wait a minute, okay,
*  sometimes you might want to go back a little bit to like more structured, right? So, hey,
*  I want to review some documents, have questions. Okay, then we kind of give you a more like form,
*  like ability to put in the questions if you want, right? So one of our challenges has been how do
*  you strike that balance between the kind of just wonderful flow of a chat and the intuitiveness
*  of a chat. But knowing that behind the scenes, we do have these discrete skills and these discrete
*  capabilities. And how you do that is something that I think will frankly be continuing to evolve,
*  right? I think we're still trying to find exactly the right balance. In terms of the skills,
*  loosely you can divide them into, there's two major flavors of lawyer, maybe three of you include
*  criminal folks who do crime, but for clients, there's litigators who are used to this person
*  in court and they're the ones that are constantly searching case law. And then there's transactional
*  law, which is, I want to merge companies, right? And there's a huge amount obviously of law that
*  goes into evaluating those contracts and the various due diligence and things like that.
*  And so case tags for 10 years had really been focused on litigators because we were
*  legal research. And that's, although it certainly can sometimes impact transactional law,
*  really litigators are the ones who are constantly searching case law to find cases to cite to the
*  judge. But even starting before GBT-4, when we had our sort of our BERT-based search, suddenly we
*  were being told by these firms, hey, can our contract, our transactional guys take a look
*  because they too sometimes need to search for something. So our first battery of skills during
*  the beta phase spanned both. So we had like, you can do legal research where it'll just run
*  right on legal research. We had things like deposition prep. So I'm going to go depose so and so,
*  and it could suggest a bunch of topics, let you alter the topics, then suggest a bunch of questions
*  to sort of jumpstart your ability to prep for a depo. We had things like timeline. So you can
*  upload a big messy corpus of documents and it would create a chronology, which is something that's very
*  labor intensive to go do as a, I remember as a first year associate, spending a lot of nights
*  just trying to map that stuff out. And then on the transactional side, we had the ability to ask a
*  question of a merger agreement, like what's the this or this term say. And then fancier things
*  like one called contract policy compliance. So basically, let's say you're a big Fortune 50
*  company and you say, here's how we do things for our contracts. We insist that it be governed by
*  Delaware law, right? Or we won't sign unless the IP has this or this, you know, what we could do
*  was basically give those policies to GBT four. And then anytime a draft contract came in, it would
*  police the draft. Now it would find the relevant clause, say, is it kosher? Does it actually comply
*  with how we do things? And if not, it would then suggest a red line for how to change the draft
*  to comport with how you do things. Right. So the sort of just it's like, you can almost think of
*  it like there was spell checker, then came grammar check. Now, thanks to GBT four, we have like
*  substance check, right? We have the ability to like, check it for like deeply substantive aspects
*  of things to see if it complies. And then we you know, there's things like what's market,
*  you know, you want to see how other companies handle this or this aspect of a transaction,
*  we could pull all the relevant data from the SEC, GBT four would sort of scan it, find relevant
*  stuff, and then synthesize a report for you. Right. So even though transaction law was not really our
*  wheelhouse, when you're with the power of GBT four, it's pretty fast, and you can start creating
*  pretty valuable skills. And then on the litigation side, I mentioned a few of them. Some of the more
*  interesting use cases actually, you know, during the beta phase, we're still we're having yet
*  productions. But one great example, we had a client, another fortune 500 company. And you know,
*  there's like certain expert witnesses, they make their living just testifying against the company,
*  right? Like the guy who just urine and you're out, I'm the one that the plaintiff calls to go say why,
*  you know, Monsanto or whoever you want to, you know, pick your company. And so they said to us,
*  Hey, if we gave you all of this extra witnesses prior extra reports and prior testimony from like
*  multiple earlier litigations, could co counsel, analyze and find contradictions that we could use
*  for cross examination. And to me, that was one of the most amazing use cases, because
*  that is the kind of thing that lawyers go to law school to do. Like a lot of times you'll hear
*  people say, all that will be automated is the you know, menial work that nobody wants to do anyway,
*  right? And look, the truth is, yes, you know, LLMs will help tremendously on that front.
*  But they can also help for things that are like deeply substantive, like really, you know,
*  finding inconsistencies. So you can go do the like famous, you know, cross examination that
*  destroys the witness, right? That is like at the heart of what being a lawyer is sometimes,
*  certainly being a litigator. And so what we found is that, you know, in just the earliest days,
*  the ability to point in that pedestrian things that are more just tedious than maybe intellectual,
*  but also to see how it can help with things that are actually quite intellectual, right?
*  Quite, quite such an issue. So in terms of how that is built, you know, it's crazy that we're,
*  you know, we're still not even a year into GBT four being public. And there's obviously been
*  many versions at this point. And, you know, enhancements in terms of new features, such
*  as function calling, and also just, you know, a better understanding of kind of how to do the
*  retrieval augmentation and all that kind of stuff. I wonder if you could maybe the best way to ask
*  it would be to give kind of a little bit of a history of where you started and how things have
*  evolved with the product. I imagine that in context, by the way, is another one that obviously is huge,
*  right? So first version, 8,000 token limit, you know, limited access to the 32. Maybe you're
*  using the 32 that obviously could get a little bit expensive. So imagine you're like in the early
*  days, highly structured, and, you know, big emphasis on managing context, perhaps it's
*  still that way. And you have like, you know, a bunch of kind of very discreet prompts, and it's
*  about kind of chaining them together. Or perhaps, you know, because the models are getting a little
*  bit better generally, and the context window is growing, you're able to just kind of push more and
*  more onto the models and, and rely less on your own structure. Yeah, so a few things there. I mean,
*  the context windows have sort of broken my heart a little bit, right? Because they turn into a
*  mirage, right? Which is, you know, they're missing stuff in the middle, right? They don't,
*  they're not as accurate when you fully utilize it. So I say it's like saying, my boat can seat 100
*  people. But if you put more than 10 people on it, it will sink. It's like, well, does that boat
*  really seat 100 people? So for what we do, where we're being right is so important, right? So far,
*  the longer context windows haven't really yet been there for us. Now it's getting better. I think,
*  you know, there's progress being made. And another limitation for us is, we do really rigorous
*  testing on a model. So OpenAI will come out with an improvement. It's not like we just swap that in,
*  and we're not just pointing to whatever their current one is, we have to go test the model,
*  because it might be better at one thing, but worse for what, you know, the lawyers are using it for.
*  And so there's always this lag, where we know there are these wonderful things yet, but we don't
*  yet have them in our system. You know, there's a process for that. I mean, I remember one of the
*  great examples is, you know, now there's a JSON toggle, right? Just JSON. We spent like weeks,
*  like, you know, trying, everyone begging you, please do JSON, please do, you know, like just,
*  you know, that's an example where, you know, OpenAI is like the evolution of just the field,
*  I think, is sort of what you're pointing to, like, things are getting better and better and easier
*  and easier for developers. And, you know, believe me, well worth it for the early access, like,
*  we're not complaining by any means, but we certainly, some of those, we were kind of
*  doing the hard way, and now there's easier methods. But in terms of, yeah, so I think
*  that's the main thing. I think that there's a lag for us because we have to go test and bet
*  everything. We can't just hot swap it in, even though I know there's a lot of great stuff that's
*  coming out, right? And then there's other aspects, like, you know, law gets really violent,
*  so there's often violent topics, there's often racist topics, there's often, you know, really,
*  you know, and so we had to have these filters removed so that gbt4 could interact with this
*  stuff in a way that the chatbot, you know, as an issue of alignment, they're basically like,
*  steer clear of that stuff. So there's a number of ways where like our system, which is on our own,
*  you know, dedicated instances, right, we have our basically our own kind of path that we're doing.
*  There's a number of instances where we had to deviate both to kind of protect our use cases
*  and are also just to ensure quality. Are you fine tuning gbt4 that I mean, it sounds like there is a
*  slightly different version that you are using as opposed to the normal public API?
*  Most of what we've done so far has been relying on just gbt4 without any fine tuning.
*  The retrieval engine for some of our rag, especially for case law, was using a home
*  build system that we trained on common law. But very much it was gbt4 that was doing the
*  heavy lifting. Now, I'm very proud to say that our team as part of our alpha testing, we got to do
*  some reinforcement learning for the actual gbt4. We had folks teaching you not to swear and folks
*  teaching you not to tell you how to build Molotov cocktails. We actually had some of our very
*  fantastic reference attorneys and you know, folks giving an input on you know, how best to describe
*  how a document is relying on a case. So I just like we got to put one tiny little
*  pile in the alumbre as you know, I mean, I just forever like talk about that. So, you know, but
*  that's the closest, you know, to sort of legal specific stuff. Now, gbt4 was trained on a lot
*  of case law, right? I think, you know, it's certainly seen a lot of this law, but we haven't
*  yet done any sort of find, you know, we don't have a variant of gbt4. That's fine, too. Yet,
*  certainly, as you know, like, that's something that increasingly opening eyes is looking for
*  partnerships and there well could be some things there. On the evals, it sounds like you have put
*  a lot into that. I think that's something that a lot of people are kind of coming around to now.
*  Even, you know, in the in my, you know, the main application that I have built is a video
*  creation app and the core language model task there is video script writing. So we don't need
*  to be, you know, nearly as rigorous in our testing. But one thing I have noticed is that the flywheel
*  is getting tighter, right? It's getting easier and easier to run and we use 3.5 turbo fine tuned.
*  It's getting easier and easier to to kind of rerun the fine tuning. Now you've got a new model.
*  We used to not worry too much about the evaluation process because we felt like we were just,
*  you know, up close and personal with it enough that we kind of would get a feel for how it would
*  go. And then we had a couple of spot checks that we would run. And, you know, that would be kind of
*  that. Now with the flywheel getting so much faster, it's like, geez, we do need kind of an automated
*  way to do this. Not to say that, you know, I'm always a big believer in not fully automating
*  this stuff. You may have a different opinion, but I'm always kind of like, there's no substitute for
*  still being at least somewhat hands on. But I'd love to hear about your system because, you know,
*  I think a lot of people right now are searching for what is the right balance to strike in
*  evaluations? How much should they be doing with like model based evaluations? How much should be
*  objective? How much should still be manual? What have you learned, built? Are there any good tools
*  that you love? I mean, everything about eval is I think is of interest. You know, some of the most
*  important stuff we did as a company, the users never see, right? And that was we built an
*  internal framework. So I mentioned we sort of pivoted the entire company within 40 hours of
*  seeing what GPT-4 was capable of. Part of that was creating these trust teams, who's just you wake up
*  and you try to find this thing messing up. And by messing up, I don't mean crazy hallucination,
*  although that too, but also, you know, is it just saying the wrong answer, right? Is it quoting the
*  wrong, right? Just sort of any and all ways that you can find this breaking. And we just, we built
*  the whole framework that had these series of tests that you could run. So it's like you said, it's
*  six mix, you want as much automated as possible, but then there is no substitute for also having
*  people using it. And in our case, you know, there's attorneys using it, right? And so,
*  you know, you hear very quickly if there's an issue. And so, you know, we erred on the side of
*  testing, right? Could we have moved faster? Probably. But we really thought that what it
*  means to be responsible with this is to just go overboard with testing. And so when we were first
*  beta, when we first had our beta, I think we had like 16, some much larger number, we actually
*  launched with a very small subset of that, because those were the only skills that we felt and met
*  like the rigorous testing we had done, right? And there were some that were close and that was
*  painful, right? Like actually our timeline scale was an example. You know, people were like, why
*  did you take that away? I love it. I love it. We said, well, our testing and stuff not there yet.
*  Right. So, you know, I think for it's use case specific, right? For law, for medicine, you know,
*  there's certain protection where like screwing up is got to have a really bad impact. And there's
*  other ones where maybe you have a little bit more wiggle room, right? Where like, okay, right. Like,
*  you know, so I think it's use case specific, but for law, it's just one of these ones where you can't
*  be testing enough, frankly, right? Because there's just, you know, the people get hurt or harmed if
*  you don't. So today you use your own framework. You have a suite of automated tools that kind of
*  confirm that you're getting the right, still getting the right answer on all the key questions.
*  We've merged with Thomson Reuters. So now with Thomson Reuters, we've like created like the
*  master skills factory, right? Testing, you know, the whole flow, because part of it is like the
*  velocity of creating these functionality, right? That's another kind of dimension of competition,
*  well, it should be, you know, how quickly can you go from the user, you know, need or right to
*  something that you can put out there and trust. And so, you know, one of the exciting parts of
*  collaboration with Thomson Reuters has been, I mean, talk about quality control.
*  Thomson Reuters is the absolute gold standard. And I've been doing it for far longer than there
*  were computers, right? In terms of really making sure like editorial excellence, you know, their
*  site, right? And nothing's infallible, but Thomson Reuters, part of why Jake and I were in Laura,
*  like, you know, these are the best partners we can have is because there's just nobody better
*  at ensuring that you can trust the output. And so that's one area where like our techniques and
*  approaches and our philosophy merges very well with theirs. And so I think we're still, you know,
*  so we've combined it and I think we're going to be amplifying it and magnifying it in terms of
*  all the things that we can do. Is model powered evaluations part of that framework like we use,
*  for example, GPT-4 to assess, you know, the 3.5 scripts on pretty subjective dimensions, you know,
*  and ask it to give us like a rating. And I'm always like, I don't really trust that. But I
*  think I at least trusted enough to say if the average rating takes a dive, then I should be
*  paying attention. We're almost entirely GPT-4. So you're not, you know, it's not like we have
*  GPT-5 to go police GPT-4. So when you have GPT-4 policing GPT-4, right, it kind of raises, right,
*  like this, right, it's possible that that, you know, it's a different calculus in terms of how
*  useful that could be. It may be that we're doing some experiments for that. So one of the things
*  we're doing behind the scenes is what happens when you apply GPT-4 to 3 million documents,
*  right, these like huge corporate where you have several doc review. And so, you know, you can have
*  it review the documents tell you which ones are relevant and describe why it's relevant and give
*  it a score. Then what happens is there's a lot of documents that get the highest score. And you look
*  at the descriptions and you're like, wait a minute, some of these, like are clearly palpably more
*  important than others. So then you say, well, what happens if GPT-4 gets involved again, and
*  reranks based on the descriptions, right, and suddenly you have a much more intuitive list.
*  So, you know, using GPT-4 to enhance the output of an earlier GPT-4 is certainly something I think
*  that has a lot of potential. And it may be as a complementary technique, using it to police for
*  quality control is important. I don't think I see a world where we completely turn things over to
*  GPT-4 to do quality control yet, although I would be surprised if we're not doing some experiments,
*  at least in limited ways that can help. Okay, let's do the same thing that we just did for
*  evals on the embeddings and rag side. Again, you've been kind of even 10 years before,
*  or close to 10 years before this moment working on that. Now, of course, there's a rush of,
*  you know, new embeddings options, opening eyes got them, other people have got them.
*  Sounds like you're still using your own core embeddings tech that predates the GPT-4 moment.
*  What could you kind of tell us about like, how do you chunk stuff? Yeah, I mean, I have so many
*  questions, but tell me everything about rag. Yeah, so chunking, okay, that's a great area,
*  right? Because one of the things you want to do is put domain expertise into it, right? Don't chunk
*  where the question from a transcript gets separated from the answer from a transcript, right? Those
*  are better kind of thought of in pairs, right? So we did have some kind of domain specific chunking
*  that went into it. With the embeddings, yeah, that was one of these rare moments where like,
*  our in-house thing, you know, it's a thing we built, we're like, wow, it does seem to be
*  up performing, at least, but again, this is late 2022, early 2023, which in this field is like the
*  decade, it's like a century, right? In terms of how things have progressed. So, but you know,
*  there isn't enough weird nuance with case law. It is a kind of strange fabric for some ways that
*  we did feel like our own home training system was working better than what we saw. We're constantly
*  evaluating that, right? I mean, our main thing is just the best user experience. So the moment we
*  think that there's embeddings that will create a better experience, we will. And then what's sort
*  of funny with RAG, I mean, this might be tendentially to what we're talking about, but one thing that's
*  been interesting is, you know, you have these firms, and they're very happy, they're very proud of
*  their legacy, and they're very proud of what they've collected and built, which they should, you know,
*  they've been around for 80 years. And there was this sense of like, well, can you create a GBT4
*  with just our data? And they're like, like, I know it's read all of the internet, but we do, it gets
*  a hold of our summary judgment motions. That'll really kick things. You're kind of like, no, I
*  don't think that's really going to prove a deal. What you want to do is RAG. You say, no, no, point
*  GBT4 at your documents. That's how you leverage what you have. But there was this sort of marketing
*  of sort of like, we'll make your own model just for your firm, which I think, frankly, there was
*  no evidence that that was actually going to have a better outcome, but it just fit to sort of the
*  ego of the firm, right? And their kind of natural desire to want to have a competitive edge. So that
*  was one thing we sort of encountered early on. I think now firms are kind of coming around to,
*  let's just use RAG, right? Let's just point it at our stuff and how best do we leverage what we have
*  as opposed to, I want to go spend a bunch of money to create a new model. That's everything
*  GBT4 saw plus, you know, our relatively paltry amount of content. So what happens when somebody
*  brings their own data to the table? Like I, you know, I created my account, I'm dropped in there.
*  It's like, okay, you can create databases. There's six different kinds of databases that you
*  can create. I assume that those are like pretty similar core underlying technology,
*  but perhaps with some different kind of processing or prompts.
*  Nathan, because, you know, listeners to your podcast deserve the unvarnished truth. I think
*  they might be absolutely identical. I think those six options were for education purposes to kind of
*  tell you, right? Like these are things you can do. I don't think we're switching up the embeddings.
*  Maybe for one of them, we might have something specialized, but yes, to your point,
*  working with law firms, security becomes just the number, you know, the immediate thing that
*  you're always talking about before, you know, you can be showing something that was the time machine
*  and the first question is going to be about their client's privacy, right? And, you know,
*  well, it should, right? This is important stuff. So, you know, we, you know, our philosophy has just
*  been, obviously it does go through GBT4, right? So it does leave, but then you can have it immediately
*  deleted. Or if you want to keep it in our system with our embeddings, you have that rights, but you
*  can have it deleted like every day. You know, we went through the SOC 2 compliance, you know, all of
*  the various rigorous security stuff you have to go through. And of course, we don't train any models
*  with your data. And there was this little window where that was a differentiator between us and
*  OpenAI, right? Because they're sort of like, why don't you just go to OpenAI? And so this little
*  period, it was at least ambiguous whether OpenAI was training on the data. They naturally came to
*  the same place that everyone working with enterprise comes to, which is, no, we won't,
*  unless, you know, you want us to basically, right? So I think that's your point is sort of how do you
*  deal with the security and privacy? Is that the main? Yeah, that's interesting. I was actually
*  even more thinking about just kind of the technology. Like, it sounds like you're taking
*  these documents, passing them through GBT4 to be chunked. Perhaps there's also like metadata
*  being extracted. And then I'm wondering kind of, everybody's looking for tips on vector databases,
*  or like a point of view on the future of vector databases. So I'd be curious, you know, which ones
*  you're using, if it's a hybrid structure, if there's like a graph that's being synthesized,
*  all these sorts of very practical lessons learned, I think are great. Right. So I'd say that we have
*  domain specific chunking when you want our ends before. So we sort of go there. I don't believe
*  that we're right now throwing in the latest vector databases on it. So I'm actually not a great person
*  to ask for that kind of stuff, because we've just sort of been sitting with our homegrown common law
*  specific one, which, at least last I checked has been for us, more performant than, you know,
*  a better accuracy than the ones that we've tried. You know, it's interesting, because we were doing
*  this stuff early, before GBT4, we kind of set up a bunch of stuff that we're still kind of sticking
*  with, right? In terms of those embeddings. Now, that could be something where we need to examine
*  that and say, no, no, like, just, you're doing it early, but now it's obsolete. But that's just
*  something we're, you know, testing constantly. And we so far, we haven't seen a real reason to switch.
*  We certainly have the case law citation graph going back to like our traditional research tool,
*  right? That when you're reading a case, you have to see who cites to it. And that's the whole thing.
*  We're not doing anything in the graphs with GBT4 specifically, right? We're not leveraging it that
*  way. I've always got a handful of different apps that I'm kind of thinking about this with. One
*  other one, just for context, is I'm working as an AI advisor to a company called Athena. We're in
*  the executive assistant business. And wait a minute, I think I use Athena for my executive assistant.
*  Yeah. So this is, you know, early, early days for us as well. But of course, you know, we want to be
*  more efficient. We want to bring AI to more things that we're doing. One of the experiments that we've
*  been working on is can we create some sort of retrieval, augmented chat experience that allows
*  the assistant to get kind of deep context on the client? Stuff that maybe they've never even talked
*  about before. Or, you know, certainly we don't want to be asking the same questions repeatedly
*  if we can avoid that. This is especially important in the early days of a relationship.
*  And a challenge that we've had in trying to build something like that is, okay, you get all this
*  information, right? And people can upload anything. And then we chunk it and, you know,
*  maybe we could be doing more just to like maybe use GBT4 to do the chunking a little more
*  intelligently than our approach that is straight away could be an improvement. But I think a lot
*  too about like, if I match on this chunk, but where did this chunk come from? You know, in kind
*  of your naive chunking strategies, that stuff a lot of times gets lost. And, you know, also,
*  what's the timestamp on that document? And, you know, if you go pure vector database, like sometimes
*  you do, you don't necessarily have all those features. You could go to like a Postgres,
*  you know, which certainly is not a native vector database, but is adding. And so I'm kind of
*  wrestling with all that sort of stuff, like how much pre-processing to do how much structure,
*  how much synthetic metadata. Such a great area. So I'm convinced. So right now, we're throwing
*  co-counsel at the raw text and chunking is basically the only favor we do for it. Right.
*  And the way I think about this is like, if you were an assistant at a law firm, you just started,
*  and they said the night before your first day of work, you can go into the office, open all the
*  files. What would you do to make your life easier? And it's things that you might create a cheat
*  sheet. These are the contact information for the attorneys in the current pending legacy. I'm going
*  to put that on this. I'm going to create a new document that's just for me to be able to more
*  easily pull that. Right. That's what humans do. That's what a Rolodex is. Right. I think there's
*  a lot there where you're looking at, which is like, can you land GBT-4 in a new sort of information
*  environment where at least it knows the general error for a lawyer? And can it go and like rename
*  files according to like what makes more efficient? Like, you know, look at the first page of each
*  document to then create a new layer that then it can interact with more quickly. I think there's
*  a lot there. I think there's going to be a lot of like sort of the art of doing this really well.
*  And hearing what you're saying, I think you're right. It completely makes sense for an assistant.
*  And then we're doing some experiments with it, right? Where we're doing things, you could like
*  type in the docket, which is just the number unique identifier for litigation. We pull the docket.
*  And now we're starting to parse out a bunch of information even before you run a skill so that
*  when you do run a skill, when you say send a letter to IBM's counsel, it can then go and kind
*  of do a more robust job of that than it would if not. It sounds like you are throwing GBT-4 at kind
*  of every problem as the first approach, which is something I've often recommended. Like don't get
*  too cute too quick. See if GBT-4 can do it. Try to make that work before you,
*  really before you try anything else. And I think one reason a lot of people don't do that is that
*  they worry that it's going to become too expensive and perhaps just not viable.
*  So I thought actually the co-counsel pricing was one of the most interesting aspects that I
*  encountered in my exploration of the project. There's a couple of different prices you can kind
*  of clarify, but basically it comes in at something like 200 bucks a month, which is obviously 10x
*  your retail chat GBT subscription. And people may balk at that a little bit, but I think
*  that's really smart. I've kind of been thinking more generally, why don't people just build the
*  very best thing that they can build with the very best models that they can possibly access
*  and charge whatever it takes to make that at least viable enough that you're not like outright
*  burning money. And then we've seen a pretty clear trend in the models getting cheaper. So presumably
*  some margin will kind of come back for you. I guess, first of all, is that the strategy?
*  And how have you been thinking about this question of pricing and how have people responded to it?
*  First, I mean, look, we were so spoiled. You get TBT for very early for free without talking.
*  We weren't charging for it and we were just swimming. I just love it. It's the equivalent
*  of somebody growing up like a Saudi prince or something. You don't even have a concept of it.
*  All you're doing is just the joy of how is it physically good in this model.
*  And the guidance we got from the folks at OpenAI too is that, look, first build the best and then
*  optimize. And so that has generally been our approach. But then, of course, the bigger
*  situation is it has to work and it has to work for law and has to work reliably.
*  And a lot of the times when we tried to test other models, it failed there. And so there you go.
*  It makes it easy in a way. So the truth is things are catching up. But for the majority of the last
*  year, and Nick, tell me if you disagree, TBT4 has been like kind of a big leap ahead of even
*  what was in second place. And tell me if you disagree. And for us, that leap meant the
*  difference between we can put this in lawyers' hands and we can't, with confidence, with reliability.
*  Now, are there sub-tasks within some of the flows that you could outsource to delegate to 3.4?
*  And a lot of our machine learning folks would be like, they're very annoyed with me for how
*  like TBT4 is such a guy. And they're like, you've got to start thinking about these other models.
*  But for us, again, it's like it has to work. It has to work reliably. And so that does often mean
*  for us, for the majority of tasks, TBT4 does it. The other ones we tried don't. End of discussion.
*  Again, as it evolves, we're constantly looking at this. Things are scaling up. So increasingly,
*  you're going to want to look at where you can. But yeah, basically, law itself demands that we
*  always focus on quality. And to date, by and large, that has meant TBT4 or nothing, frankly.
*  So how have people responded to that pricing? I mean, I can imagine, on the one hand, people
*  might feel like that's more expensive than other software products. I feel confused about maybe the
*  future of legal billing, because I'm like, if there's one thing that this tool is supposed to
*  do, it's supposed to save you time. But if you're charging for your time, how does that work out?
*  In any other business that I'm in, I would say, well, geez, 200 bucks a month, if it saves me one
*  hour, it allows me to bill one hour more, then great. But wait a second. Those are not the same
*  thing in the legal space, traditionally. So the market has responded. I say the market.
*  For me, it's always the profession. The legal profession, again, you've got to look at it like
*  there's a difference between your huge multinational firms and your solo practitioners. But the 200 a
*  month pricing generally is for solos, for smaller groups, they just want to buy it.
*  And I think a lot of it is like, if they think of it in terms of a legal technology tool, they're
*  like, wow, that is pricing. If they start to say to themselves, wait, I would have to hire a
*  paralegal to do that, suddenly it becomes quite a bargain. So I think part of why I think the price
*  has been well received is that they're getting that these are things that aren't, it's beyond
*  just having Thompson Reuters or Alexis, right? Or like a document management tool. It's really
*  getting into actually like tasks that you would have to hire a human and pay a lot for. We're
*  always trying to make it more affordable. And I read that in the early days of electricity,
*  only Wall Street and Madison Avenue got street lamps. And to some extent right now, there is
*  probably that going on, right? Especially if you want to do high throughput stuff,
*  these large firms that have much deeper pockets and the litigations are such that it makes sense
*  to go spend more money, given the risk of losing the case. They're right now able to do things with
*  GBT-4 that are probably impractical for your everyday attorney representing you or I, right?
*  But like you said, it's getting better. And we continue to try to design prompts in a way that
*  lowers the right intensity so that you can bring down the cost and things like that.
*  But on the whole, we were a bit worried too, because yeah, that is a lot. So we've seen them
*  bucket lower numbers when it came to traditional research tools. But here on the whole, I think
*  they just realized that this is so much more than just once you start thinking of it almost like
*  this weird college and not a tool, then it's been pretty positive. So one of my big theories in AI
*  in general is that we'll see a lot of consumer surplus, meaning in the classic economic definition
*  that willingness to pay will greatly exceed the actual price. Is that basically the trend that
*  you think you are enabling for your customers' clients? Are they just getting more for the same
*  bill or their bills are shrinking perhaps because it's just taking less time to do the job?
*  Right. It's funny with pricing. So Jake, Laura and I, we were lawyers by training.
*  We love legal tech, legal informatics. Pricing expertise was not necessarily what we were the
*  best at. And we've joined Thompson Reuters, which of course has a much more mature, sophisticated
*  understanding of how you go and test and measure these things, if that makes sense.
*  So I think there are a couple of things. First, there's going to be competition,
*  and well, there should be. This is one of the benefits. It's not like only one company has this
*  and therefore can just charge whatever they want. So that I think keeps you honest on it.
*  That said, Thompson Reuters, we trust. You trust us. When things matter, Thompson Reuters is who
*  you go with. And that does involve more testing. That does involve perhaps more expensive models
*  sometimes and things like that. And that will be reflected in the price. So I think first,
*  I would defer to like, there's probably like literally 50 people at Thompson Reuters who are
*  more qualified to talk about how they're going about thinking about the pricing. But generally,
*  just that sort of tension between, of course, there's competition, but at the same time,
*  there's a caliber of product that people expect from us and that people need from us.
*  And then that will always be reflected in the price.
*  How about just kind of on how you measure the reliability? Obviously, a huge theme of
*  your comments has been the critical nature of reliability. I think you said, de minimis,
*  hallucination a little bit earlier. Do you have kind of metrics that you watch or like a bar,
*  as long as we're below that hurdle, we're good? Could you be confident enough to say,
*  use our product and you'll never have one of those embarrassing moments?
*  You'll never. I mean, you can't say that about humans, right? You can't say that about hiring
*  a human and you'll never have it. And I think what's important too is that it's not just these
*  cartoonish hallucination problems, which we avoid not just from the rag architecture,
*  but we have the cases beneath with links and we police it. So if you see that link,
*  it can't not be a real case. So we are able to sort of give certainty under that stuff.
*  But even beyond just hallucinating, I mean, those kind of grotesque hallucinations, if you will,
*  there's like, it's not infallible. Sometimes it can misread what a judge is writing or misunderstand
*  kind of what the user intent is. And so that's a level of that. That's really where we're,
*  I think, the most focused, right? Is how can we get better and better there?
*  I was always adverse to having the thumbs up, thumbs down back when we were just a search engine
*  because I was like, we're supposed to be the professionals. Imagine if your doctor was like,
*  hey, Nathan, I recommend this prescription. Hey, how'd I do? What do you think, buddy?
*  It's like, you're the pro dude. You should do it. Boy, did I get over that when it came to
*  LLM stuff, right? So we have an ability to get real-time feedback. And then we just call it
*  follow up. We have a weekly meeting where we do nothing but talk about any complaints that came
*  up. And then we have our sort of systematic quality and control constantly running tests,
*  et cetera. You're never perfect. It's going to be something where you're continually striving
*  to get better and better. But I'm confident to say that nobody does more than we do to an in-law
*  to make sure that it's working. For somebody like me, so I have a couple of different ventures that
*  I'm involved with. At Waymark, we do not have an in-house counsel and we don't really, fortunately,
*  we don't have to often avail ourselves of external counsel either. I guess I don't even know if you
*  would sell this product to non-lawyers. It's just straight not available. You have to be licensed
*  to even become a customer. So, I mean, yeah, we made the early decision to not go to what's
*  called per se in law, which is it's a little bit different than corporations that don't have GCs
*  because it's so misleading because you think, look, I've got this memo, I'm done. Look,
*  it's just really just like a lawyer. Yeah, no, a lawyer can look at that and see that there's
*  more nuance, that there's certain exceptions that the lawyer knows about. So we thought it would be
*  dangerous. Now, to be clear, one of the most, probably the most important thing these large
*  language models are going to do, big picture, is provide services for folks that can't afford
*  lawyers. Or provide some form of services, some form of help in some thing. I think that then
*  there's a colleague of mine at Stanford, Margaret Hagan, who's working in there. I defer to her,
*  go study her work. She's fantastic. So to be clear, don't get me wrong, that is going to be
*  one of the most really important ways that we use LLabs. And I think as a society, we should be
*  judged by how well do we solve that really critical problem. From where we sit at Case Text,
*  we did not want to give folks the misleading interpretation like, oh, I have a lawyer,
*  it's called co-counsel and go in there and do it. And so we, you know, and separately from that,
*  there's this unauthorized practice of law issue, right? Where it's like, are you even allowed to
*  go report to be a lawyer? But frankly, even be, it wasn't fear of that reprisals from that so much
*  as like understanding that like we didn't feel comfortable doing it. So like, you know, look,
*  if your company wanted to use co-counsel, could you use it? Are there a lot of skills that are
*  sort of universal that you could like, you know, you could put in a hundred transcripts from
*  speeches or whatever you cared about. Yes, you could use it, but we're certainly not telling it
*  being like, you don't need a lawyer because you've got co-counsel, you're all set. It's just not,
*  it's just not there yet. I've had a few moments where I've had interesting experiences along
*  those lines where I'm like, even, and this is even just for personal stuff, you know, I get a
*  contract, you know, I'm going to do some 1099 work and, you know, I had one from a big tech
*  company that has a reputation for having, you know, a lot of kind of very restrictive causes
*  in their contracts, or at least that's kind of the sense that I had. So I just take them to
*  Claude and to chat GPT and say, Hey, anything jump out of you from this contract? If neither one
*  flags anything that seems meaningful to me, then I'll usually just kind of say, okay, that's good
*  enough. Let's roll with it. But I imagine I could do better with a co-counsel seat. But I also
*  understand why you would be reluctant to put yourself out there in that way. Yeah. I mean,
*  you know, it's certainly like, well, what jurisdiction are you in? Right? That can impact
*  whether some provisions aren't enforceable in some states, some are right. So it's just, it gets more
*  nuanced, right, than just what you're going to get from a chatbot, or even frankly, from a more
*  sophisticated co-counsel. So what we build is a tool for lawyers. It can make your lawyer bill go
*  down. It can make your attorney like, you know, help your attorney not overlook something. But it's
*  just not a replacement. And now there are many folks who believe that's the goal. And that's
*  where we're going to get. And, you know, we just, there's such debate about how far these LLMs will
*  go as we scale them up. And much, much, much brighter minds than mine are debating, you know,
*  like, where does this plateau? So I can't rule out that, you know, the further generations of this
*  will. But at least for right now, we're not there. We're not close to there. So yeah, that's maybe a
*  perfect transition to kind of the future of law section that I thought we might spend a little
*  time on as we get toward the end. For starters, yeah, I sometimes call that the $100 trillion
*  question. Where will the model's plateau that's, you know, inspired by the size of the global
*  economy? Because it's like, could very easily, you know, do the whole 100 trillion, you know,
*  with not too many more leaps. What are the things that you would say with GPT-4 are still the
*  weaknesses? You mentioned one is like missing things in the middle of context. I was going to
*  ask if you were using function calling at this point, or if you're still kind of, kind of custom
*  doing your own, you know, implementation of function calling? No, I think we're increasingly
*  folding in the function calling. Yeah, I think it's like porting some over and then but yeah,
*  again, all their great stuff we want to leverage is just we have a slower process,
*  but we have to make sure it's not, you know, screwing anything else up. But yeah, so you know,
*  look, where it is now, it lacks sort of the ability to understand a broader context of what it's
*  working on, right, which can sometimes, you know, lead to it. That's it can't give you like legal
*  and strategic advice, right, because it doesn't really understand kind of where these things play
*  in. I don't think it can write persuasively enough to really write briefs. And but let me carry out
*  that I have a bias, I give people some people accuse me of having like a romanticized view of
*  writing. But to me, writing is thinking like you as you write, you think and actually Paul Graham,
*  the great YC founder, has written I think on this is a I completely agree with him that like,
*  it's very dangerous to let the writing atrophy, right, we did we can't spell anymore, because the
*  red squiggly line will bring us home. Nobody can read a map because why would you when you have
*  GPS. But I think writing is qualitatively different. Like and so wrestling with that blank page,
*  I think is something that we actually should jealously guard, at least for the types of writing
*  that really involves substance. Look, there are certain types of legal documents, nobody
*  declaration, they're supporting documents, sure, of course. But for actual advocacy,
*  and the same thing for judges, we recently had a judge sort of raised the question of like, well,
*  could this thing start writing first drafts of opinions? I think that's very dangerous. I think
*  we lose something about the evolution of law, you know, like the sort of the way that it mutates and
*  then changes because of this originality going into it, you know, other folks will disagree.
*  So I think that's going to be one of the most important things in the future of law is like,
*  what what happens to that, right? Like, you know, are we letting AI kind of just generate a brief,
*  and then that just, you know, essentially with some oversight goes to the lawyer, and then the
*  judges using the two briefs and puts it into AI and, oh, here comes the opinion and there's
*  some oversight. That's one of the profound questions. I think you'll start to see more
*  like kind of AI arbitration, right? But you know, the truth is, there's a guy in England, Sir Richard
*  Susskind, he was like the sort of OG AI and law guy, like, you know, going back like 30 years, right?
*  And he says, you know, whenever there's a new medicine that comes out, the doctors only talk
*  about the patient. What does this mean for patients? You don't hear them. What does this
*  mean for our billables? Like, what does it mean? Like, and sort of exhorting us in law to have that
*  same, you know, professionalism, because ultimately, this is a profession, we owe a
*  zealous undivided duty to our clients. And if that means that we have less money at the end,
*  that's actually completely fine relative to our duties, right? Like, it's not. And so I think the
*  more serious lawyers among us are going to say, like, how can we, you know, better realize the
*  goals that we all set up for ourselves with this stuff? And the truth is, we're woefully behind
*  on this. So there's so much room for improvement that I think we'll see AI get a lot of adoption
*  and start to just make the process faster, less expensive. And again, if used correctly,
*  even increasing the kind of quality of the pursuit of justice.
*  **Matt Stauffer** Yeah, I appreciate that. And I think broadly, I really agree with you bringing
*  up the bottom and improving access to expertise for people that don't have it all too often is,
*  to me, one of the most exciting things about the AI moment. And at the same time, I think it is,
*  at least for now, really important that we do not cede control of the frontier and, you know, where
*  kind of critical aspects of society are going. So I would strongly agree, you know, that like,
*  it seems, I guess, very specifically, I was going to ask, do you think that there, you kind of
*  touched on it a little bit, but from the medical profession, as you noted, I've been very impressed
*  with how positive the reaction to AI has been and how kind of non-defensive it has been from
*  most corners. I would say the same thing broadly true of the legal profession, although I don't
*  maybe have as much data on that. So I'm curious as to kind of how you see that shaping up, like,
*  what reaction you do expect from the bar. Would we get to a moment in the near future where, like,
*  you'd be guaranteed some right to, like, legal AI advice as well as, you know, human advice?
*  Yeah, that's so interesting. So maybe I can contrast two essays, both written by the same person
*  who, Chief Justice Roberts, right, the Chief Justice of the Supreme Court. At the end of the year,
*  he writes an essay about the topic, you know, whatever topic he wants. And in 2016, he wrote
*  about legal technology. And, you know, I'm paraphrasing a bit, I recommend, you know,
*  go read the real thing as always. But, you know, he sort of almost brags the right word, but he
*  sort of says, like, we're really slow, and that's a great thing. And he actually points out, I don't
*  think most people know that, do you know that the tortoise in the hair is actually engraved on the
*  Supreme Court building? There's actually a turtle and a rabbit carved into that building, right? You
*  know, they got like Moses up top, and then below you've got this Esau table. And he sort of points
*  to it and says, yep, that's us the turtle. And I would say, like, there's more options in life
*  than a turtle and a narcoleptic rabbit that falls asleep five minutes before it's supposed to with
*  the race. Like, you know, like, let's, so that's 2016, you would, I wouldn't say like anti anti-tech,
*  but very much like talking about how like, like, we should be slow and that nobody, you know, it's
*  almost it's a feature, not a bug. How much we like. 2023, he writes an essay about generative AI and
*  LLMs, and says things, you know, things that I've been very much screaming for the mountaintops.
*  He says, the first rule of the federal rules of civil procedure, these are the rules that kind of
*  govern the protocol calls for the just, speedy and inexpensive resolution of matters. Like, surely AI
*  can help us better realize that and by us, he means the courts. And you know, he says at one point,
*  I think he says like, legal research will be unimaginable without this now, right? Very kind
*  of pro very much like, you know, not reckless, but and you know, I think at the end, he says,
*  judges will still have a job, but certainly the kind of exactly as you said, like,
*  pleasantly surprising in terms of being receptive, sort of like kind of acknowledging the fact that
*  this could bring a lot of value. And it's not just something to kind of be scared or contain to me
*  that that that bodes very well. And I think generally I've seen it in other parts of the
*  profession. I think there is a real willingness now to engage with this stuff and not just from
*  how do we destroy it or kneecap it, but you know, where are the ways that we can use it?
*  Yeah, you could almost put that excerpt right on your website. I'm not sure how that would.
*  Oh, no, I went t shirt website. I might, you know, I might even add the ink, you know,
*  just tattoo that. No, no, it's it's it's wonderful to see that. I think, lorries,
*  this is a time to rejoice if you're a lawyer. This is profoundly useful technology that will
*  help us do our craft and our profession much in a much better way, a much more sane way,
*  frankly, more enjoyable way. I mean, just like sort of. And so, you know, I know there are
*  certain billing structures that are built on, hey, that associate just for 12 hours just did basic
*  doc review and I was charging 600 an hour and only paying that associate 100. You know, I appreciate
*  that those sort of paradigms will probably have to be reworked. But I think that that pales in
*  comparison to the transformation that we're going to have with our profession to one that I think
*  frankly is in dire need of that kind of transformation. Yeah, you mentioned also
*  AI arbitration. That's something I've been kind of fascinated with, but surprisingly haven't seen,
*  I guess maybe not surprisingly, because again, the time months are all really short. So it's
*  going to take time to work this stuff out. But what if you could sketch that vision in a little
*  more detail? My con law professor was a great Larry Lessig, who, you know, has been done a lot
*  on cyber law and things like that. You know, he was one of the very few people that I showed
*  you the default to under, you know, the earliest days on it. And I was expecting, you know, he's
*  going to call me down, you know, tell me that like, you know, put some brakes on this thing.
*  And he immediately was like, for 35 years, I've been thinking about what we could do for like,
*  like this is great. I was like, Professor Lessig, that's like way more. That's, you know,
*  I guess I should have been shocked that he had even sort of more ambition for it. So this is
*  something I think predates large language models, this attempt, how do we code in rulemaking and
*  adjudication, right? And sort of legal logic. And it was all just, you know, like a lot of these
*  expert systems, it was just hopeless, like, right? Like laws just so fuzzy and messy, etc.
*  But now with the advent of GPT-4 and these sort of capabilities, the idea, you know, both sides
*  can sense, submit information. And what you've done on the background, either through rag and
*  through a lot of prompting, it's basically encode dispute resolution, such that it can spit out an
*  answer. And then, you know, both sides have agreed, then I guess that's the answer. Right?
*  If not, maybe there's some right to appeal to a human and things like that. Again, that to me is,
*  is, is, I mean, if you take like one very specific type of dispute, maybe that has very, you know,
*  maybe you could kind of get there, I'd be, I think it's among the more ambitious things that
*  people are going to be trying to do with GPT-4. And if it, I'll be honest, every time I think,
*  oh, GPT-4 is not going to do that, somehow it surprises me. But that's certainly now an area
*  I think you're going to see again, like you said, it's very early days, but folks who have actually
*  been thinking about this a lot, even before the LLMs, I think feel like this whole renewed sense
*  of it about what they can do now. Yeah, certainly one of the big lessons of the last few months is
*  that we keep finding new ways to advance the capability frontier, even just of the current
*  system. So that has been remarkable to continue to watch. I guess maybe last question is around
*  the law of AI. I wonder if you have any takes on kind of, you know, should we have standard product
*  liability for AI products? How should we think about, you know, who is responsible when AI
*  contributes to some harm? Also interested in your thoughts on any, if any, on things like
*  right to train, you know, should all the data that's out there be, you know, is it fair use
*  in your mind? And, you know, or should there be some sort of profit sharing? All right. So for fair
*  use, what I'd do is send your listeners to an article co-authored by Mark Lemley, who's a
*  professor at Stanford, along with, I think, Prithvi An, like with actual researchers at Stanford,
*  deep dive on the fair use issue. He's infinitely more qualified to talk about it than I am, you
*  know. So, and then, you know, I think the truth is like where I've kind of intersected with stuff,
*  like so courts are, I've given input to courts and to state bars that are wondering like,
*  do we need new rules to govern this, right? Or can we just use our existing rules?
*  I'm actually of a mind, at least for that aspect of things, that the existing rules, if properly
*  applied, get you 99% of the way there, right? There's a duty of technological competence that's
*  now in most states, right? There's a, you know, the duty of candor to the court, the duty, you know,
*  not reading the case before you session to the judge, like you didn't need or any of that to tell
*  a lawyer, like that's not gonna, that's not good, you know, being a proper lawyer. So, I mean,
*  really the area that I've focused has been sort of myopic, really just regulation of the bar,
*  et cetera. I look forward to taking a deep breath and diving into these really fantastic
*  rich issues, or antitrust and the right, you know, right, all of these things. And certainly,
*  Thompson Reuters, because we're international, right? We've just, you know, launched in, you know,
*  Australia and Canada, you know, we're increasingly like facing not just one, but multiple different
*  regimes on this. So, you know, what you might want to do is have my colleague Laura on, who's our
*  GC at Case Tech, she's one of our co-founders, and is now, I think, in global affairs, something
*  wonderful like that, who might dive into the policy stuff a bit more. It will keep lawyers busy for a
*  very, very long time. And actually, the folks at DLA Piper would be a law firm that is particularly
*  focused on, you know, making, being leaders in the space across a lot of areas. They were very early
*  with co-counseling, basically helped us co-develop it. But at the same time, you know, then they
*  finished helping us with the product, then they go down the hall and actually represent AI companies
*  that are facing these. So, let me defer to better folks than myself, and I'm happy afterwards,
*  offline, I can introduce you to some folks. Cool. Sounds good. I'll appreciate any connections. And
*  I certainly appreciate some intellectual modesty as well. It's not all about the hot takes.
*  I guess I said last question, but if I can sneak in one more, what's it been like
*  being acquired by a obviously much bigger, much older company? You know, obviously, that's a
*  highly individualized experience, but I'm particularly curious about how the acquiring company
*  is thinking about AI. Like, do you have people coming to you from everywhere saying, hey,
*  you're the AI guy, I need your help in my department, or are they still kind of waking up to it?
*  Being a startup guy and never having been, you know, acquired by a big company, I don't have that
*  story to tell myself. Right. Yeah. Well, one day, you know, maybe you will, maybe, you know,
*  maybe I'll just go right to the public markets either way. You know, Thomson Reuters, the reason
*  we were acquired is because they were awake to how important this stuff is. And, you know, although
*  they're a very long and storied company, you might think that they would be dragging their feet, you
*  know, and kind of just relying on their legacy stuff. It's been quite the opposite. Steve Asker,
*  the CEO, you know, just we announced, look, we want to bring this to bear across all of our
*  verticals and in a very deep way. And so, and this might be unlike other acquisitions, maybe where
*  you're kind of brought on and kind of siloed and you're just the old thing. We're brought on to
*  kind of join forces with what they're already doing, which is to just, how do we create as much
*  value as possible for our clients and our customers across all of the things that we're doing?
*  And so that's been very invigorating, right? I mean, it's perhaps unusual, and I don't want to
*  tell everyone, oh, every acquisition will feel like this. But in this instance, we've been just
*  really encouraged because we're coming, we don't feel like, oh, they don't get it or they're not
*  doing AI enough. You know, they call it, I think, their build by partner approach, right? Like where
*  they're already spending a ton of money doing their own stuff in-house, they're looking for
*  the right partnerships, and then they're making strategic acquisitions, like K-Stacks. And then
*  on a personal note, like, you know, law, there's a lot of content with law, and Thomson Road is
*  has the most like beautiful content. And so I like, and it's like, it's like you've been kind of
*  building with like sticks and mud. And then suddenly you have like the Roman Empire with all
*  of its like, you know, Phoenician dyes and Greek marble and like all these things. And so, you know,
*  a lot of the things that Jake and I really wanted to build were frankly limited because we didn't
*  have X content and you know, an X point content. With Thomson Road, you really have these just
*  amazing streams of content, there's dockets, or a lot of articles or practical law. So that's also
*  just feels great because now you can, you know, basically at this point, there's no excuses,
*  right? Whatever we do, it's on us because we really now have all the pieces, both from the content,
*  the support of the larger organization, and fantastic colleagues. I mean, here are some
*  really great folks that have been putting their shoulder to building tools for lawyers since,
*  you know, long before K-Stacks, before Jake and I were even, you know, part of the world.
*  So it's been really encouraging so far.
*  Cool. I love it. Anything else you want to touch on that we haven't got to?
*  I'll just, if you're out there and you're building LLMs, I consider you an absolute hero of justice
*  and I just hope that, you know, you appreciate that downstream from your efforts, we're putting
*  this to work to really make the world a better place. And I just, I applaud you guys. I know
*  it's not easy to do, to push these models forward, but just know that you are really, truly creating
*  a value, at least from my little neck of the woods, and nothing has been more important and
*  more valuable and we will strive to really deserve it and to keep, you know, making the most of it.
*  I love it. That's a great note to end on. Pablo Arredondo, co-founder of K-Stacks,
*  now VP of Co-Council at Thomson Reuters. Thank you for being part of the Cognitive Revolution.
*  Thank you so much, Nathan.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the
*  show. So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me
*  on the social media platform of your choice. Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Omniki so much that I invested in it and I recommend you
*  use it too. Use Cogrev to get a 10% discount. Turpentine is a network of podcasts, newsletters,
*  and more covering tech, business, and culture, all from the perspective of industry insiders
*  and experts. We're the network behind the show you're listening to right now. At Turpentine,
*  we're building the first media outlet for tech people by tech people. We have a slate of hit
*  shows across a range of topics and industries from AI with Cognitive Revolution to Econ 102 with Noah
*  Smith. Our other shows drive the conversation in tech with the most interesting thinkers,
*  founders, and investors like Moment of Zen and my show Upstream. We're looking for industry leading
*  hosts and shows along with sponsors. If you think that might be you or your company, email me at
*  erik.turpentine.co.
