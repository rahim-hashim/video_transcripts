---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 3602s
Video Keywords: []
Video Views: 509
Video Rating: None
Video Description: In this episode, Nathan sits down with Jon Noronha, co-founder of Gamma. Gamma is a new medium for presenting ideas, allowing you to focus on your ideas and receive beautiful, engaging content without the formatting work. In this episode, Jon and Nathan discuss the journey of building Gamma, how to coax AI to do things well, and the opportunity for AI A/B testing. If you're looking for an ERP platform, check out our sponsor, NetSuite: http://netsuite.com/cognitive

TIMESTAMPS: 
(00:00:00) - Preview
(00:01:23) - Nathan introduces Jon Noronha
(00:06:36) - Intro - Jon Noronha introduces himself and Gamma
(00:09:36) - Gamma's origin story: building the "anti-PowerPoint" pre-GPT-3
(00:13:15) - From using AI for onboarding to generating near-complete presentations.
(00:15:11) - Sponsors: Netsuite | Omneky
(00:18:01) - If Notion and Canva had a baby
(00:23:35) - Searching for the right structure for AI, landing on HTML
(00:28:16) - Degrees of freedom - developing a constrained vocabulary of semantic blocks
(00:29:30) - Choice of model(s) – weighing cost, speed, and quality tradeoffs
(00:35:18) -  Editing UI - getting AI to edit slides per user command
(00:38:04) - UI for gathering training data - following Midjourney's example
(00:40:00) AI A/B Testing: a big opportunity space
(00:43:22) - Image generation models - Baseten and Gamma's deployment of it
(00:45:37) - Pacing feature development - Trying to stay ahead of innovations like 3D, video, voice etc.
(00:47:45) Image generation for slidedecks and AI involvement
(00:50:29) Gamma's main building priorities and AI generated websites
(00:52:34) - Competing with giants like Microsoft and Google
(00:55:04) - Enterprise AI shipping challenges - Startups pioneer new patterns; giants will eventually follow.
(00:57:45) - Simplifying complexity - will models smooth over the complexity of bloated product suites?
(00:59:22) - Conclusion and final thoughts

X/TWITTER:

@thatsjonsense (Jon)
@labenz (Nathan)
@eriktorenberg
@CogRev_Podcast

LINKS:

Gamma: https://gamma.app/


SPONSORS: NetSuite | Omneky

NetSuite has 25 years of providing financial software for all your business needs. More than 36,000 businesses have already upgraded to NetSuite by Oracle, gaining visibility and control over their financials, inventory, HR, eCommerce, and more. If you're looking for an ERP platform ✅ head to NetSuite: http://netsuite.com/cognitive and download your own customized KPI checklist.

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off.

Music license:
INW5VAQ9LHPQNGRH
---

# The Presentation Revolution with Jon Noronha, Co-Founder of Gamma
**Cognitive Revolution:** [August 17, 2023](https://www.youtube.com/watch?v=d7dde4DMurY)
*  And I don't think we had any inkling of how powerful that idea would be or how well AI
*  could do the job. We thought it would just be an initial rough skeleton that you could use just to
*  show you what our product could do. It would mix in all the different bits. And we started working
*  on that. And the thing that we found was that it could do much better than we expected. It actually
*  generated a full presentation and fine images and create layouts. It became this really powerful way
*  of showcasing all of the building blocks we built up over the previous two or three years.
*  But then what amazed us was that many people considered that a finished product. They would
*  say, oh, you've basically made my whole presentation for me. And yes, I'll finesse it here or there, but
*  you've now taken this task that would have taken me 10 or 20 hours of preparation,
*  and you've done 90% of it. That is probably always the mission we wanted to achieve,
*  if you think back of your presentation through tomorrow, how do we solve it? But it never occurred
*  to us that AI could solve so many of the pieces of it along the way.
*  Hello, and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas, and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Torenberg.
*  Hello, and welcome back to the Cognitive Revolution.
*  Today, my guest is John Nerona, co-founder of Gamma, an AI-powered presentation and website
*  creation tool that invites users to just start writing, promising beautiful, engaging content
*  with none of the formatting and design work. Now, as recently as a few years ago, right up
*  until the point when John was starting Gamma, actually, it was generally agreed that AI would
*  first automate manual labor, then maybe knowledge work, and then maybe last of all, if ever,
*  creativity. But as it turns out, creative technology has actually been one of the very
*  first markets to be affected by generative AI, and I've been thinking a lot about why that is.
*  Reflecting on this conversation with John, a few things definitely jump out.
*  First, the blank page problem is real. People are often at a loss for creative ideas.
*  GPT-3 level LLMs were not super powerful, but they were capable of brainstorming creative concepts
*  at lightning speed, and simply helping people get unstuck and into the creative mode can itself be
*  super valuable. Second, no matter how hard you work on a software UI, many people find the process of
*  learning to use new software tools so frustrating that they'd rather not even try at all. Yet,
*  many of those same people are happy to simply say what they want in plain language,
*  and if the tool is smart enough to get them and to produce something decent that they actually like,
*  then you have an opportunity to draw them in. And third, it's okay in a creative context if the AI
*  sometimes gets things wrong. Even today, while AI tools have become more reliable for routine work,
*  they still rarely nail creative tasks on the first try. For example, I generated the first
*  version of this essay with Cod2, but then I ended up rewriting the entire thing myself.
*  That doesn't mean, though, that it was pointless to use AI. By getting the approximate structure
*  on the page, in the slides, or in the video, as the context may be, AI makes it anywhere from 2 to
*  10 times faster to accomplish the end goal. And what that means in practice is that AI empowers
*  people to make things that they simply couldn't and wouldn't otherwise make. As you hear, I invited
*  John on the show because I recently did a search for the best AI first slide maker, and I found that
*  gamma was the very best tool that I tried. And I had a ton of fun talking shop with John in this
*  conversation. As founders of creative technology companies in the generative AI era, we've
*  recognized and embraced many of the same opportunities, and we've also faced many similar
*  challenges. We get super practical talking about which models we use to maximize performance,
*  which tools we use to measure and monitor production results, which approaches we use to
*  collect user feedback, and what strategies we're betting on to ride the AI wave more nimbly than
*  our competitors, who just happen to be some of the world's largest companies. Whether you're a
*  builder or just curious about how the AI products you use every day are built, I think you're really
*  going to enjoy this episode. Of course, if you are enjoying the show, we always appreciate it when you
*  share an episode on social media with your friends or leave us a review on Apple podcasts, Spotify,
*  or a comment on YouTube. And we always welcome your feedback. You can email us anytime at
*  tcr at turpentine.co or you can DM me on the all new x.com where I am still at LeBence. Now,
*  here's my conversation with John Nerona, co-founder of gamma. John Nerona, welcome to the cognitive
*  revolution. Great to be here. So we're here because not too long ago, I was doing this little
*  workshop that I call savvy shopping for AI products with a group of, I'd say, 100 executive
*  assistants that I'm training to use AI tools of all sorts. And one of the things I try to teach
*  them how to do is identify like, which are the good products and which ones are kind of just
*  thin wrappers, whatever you want to call them, are just not good. So in front of this group,
*  I did a search for the best AI slide maker that I could find starting, as I often do these days,
*  with perplexity and asking it to tell me what the best, most highly rated AI slide makers are.
*  And then I actually just tested a bunch of them live in front of the group. And it was a pretty
*  unanimous agreement across the group that yours, which is gamma, was the most successful and most
*  likely to be adopted AI slide maker. So I thought that was pretty cool. And then I figured, well,
*  hey, let's do a podcast and learn more about it. That's awesome. Well, thank you perplexity.
*  And thank you to the army of EAs for reading us that way. That's great to hear. It's a cool
*  experience. It's at least getting toward what people sort of imagine the future to be like.
*  So I'm really interested to unpack some of the decisions that you've made and the way you've
*  got about building the product. Because for starters, though, just love to contextualize
*  where you are and kind of how the company and AI related to each other at the beginning.
*  If I understand correctly, just from kind of checking you guys out online and trying to
*  figure out the timeline, it seems like you started building this product before there was like clear
*  line of sight to it being a heavily AI driven product. Correct me if I'm wrong, but tell me
*  where you started, like what the original motivation was and what role AI played in that and
*  how things have changed as you've been building. Yeah, totally. It was really not our original
*  sort of goal or plan, mainly because when we started the company, AI was not all that good yet.
*  So we started the company in 2020, right in the depths of the pandemic. And we've kind of made
*  our own zigzag through the sort of idea maze deciding what our core focus would be. But always
*  sort of the meat of it was we wanted to build the anti PowerPoint. And what I mean by that is if I
*  tell you that, hey, Nathan, tomorrow, you have a huge PowerPoint presentation to present, it's
*  high stakes, get it ready. Do you feel a thrill of excitement? Or do you feel a cringe of it at that
*  thought? And for most people, it's the they feel and there's any number of reasons for that, not
*  all of them PowerPoint, the software's fault. It's the nervousness of public speaking and presenting.
*  It's having your work judged like a book by its cover rather than by the quality of your ideas.
*  All of those things are sort of part of the core presentation experience. But there's also a lot
*  that comes from the software and maybe more than that, the format or the medium of presentation,
*  it's visual communication, which is something that most of us don't really learn to do very much in
*  school or the rest of our career. I have to basically make a high stakes, good looking thing,
*  using tools I'm not super familiar with to drag boxes around basically. The format itself is
*  highly linear. So I have to really plan out and thoughtfully execute a story with the beginning,
*  middle and an end. And then basically I have to fill a bunch of rectangles and they're all kind
*  of the same size and shape. And so I often have to work my ideas to fit on that rectangle. That
*  might mean finding clip art to go on one side, or it might mean cutting down my text to fit on two
*  slides or whatever it is. And so our mission was like, let's see how we can just rethink all of
*  that by building both a better way to make presentations and also a new medium that was
*  an alternative to the typical slide deck. So combining elements of the document and the slide
*  together, combining interactive elements like a webpage we have into slides. It didn't even
*  really occur to us at the start that AI would have a major role to play here. In fact, I tried using
*  GPT-3 back in 2020, we started the company to do some pieces of this and it just couldn't,
*  the technology wasn't there. And I don't think any of us realized how far it would accelerate
*  in the last few years to be able to contribute until now when it does in a major way.
*  It's funny, I've kind of lived a somewhat parallel life, I think, in building my own company and
*  product at Weymark. Listeners know this, but just for your background, I was the founder and CEO
*  there for a long time and then became totally obsessed with everything AI about two years ago,
*  which I'd always been interested in, but hadn't really fully committed my intellectual effort to.
*  And now I'm just all AI. Unfortunately, I had a good friend and teammate who was able to take
*  over for me as CEO. But similar kind of thing where we were like, in our case, it's video.
*  People need to communicate with video. There's all of these different placements, our typical
*  audience is small business, sounds like your audience is more kind of general white collar
*  professional. But people have to communicate in this way and it's not something they really know
*  how to do. It's hard even for professionals, but it's basically impossible for amateurs in
*  the case of video. Well, TikTok shows that talented amateurs can do it, but that's still
*  a pretty small percentage of people. So it's hard and people don't, they just basically don't make
*  stuff most of the time because it's just insurmountable. So we had been also working,
*  and I want to hear your kind of take on this, we had been working on interface, a lot of UI,
*  trying to make things intuitive, trying to make it browser accessible. What were the big things
*  that you had kind of prioritized before AI came into the picture that you thought was going to
*  solve this problem? And then how did AI kind of layer on top of that and change it? Yeah,
*  it's a great question. So where we had really begun was thinking through what is the sort of
*  format that we're trying to create that you can present, but is not quite a presentation.
*  And so for us, what we really prioritized was building an experience that was a writing-based
*  experience for making a presentation. So we did a lot of inspiration from tools like Notion,
*  where you could just type on a page in a very sort of like freeing way, but then pull in all
*  these different powerful blocks and elements of multimedia and embedding things and all of that.
*  So we'd actually really been building this sort of like rich text editor. And we'd also really
*  been building in more sort of mobile responsiveness. We had this idea that a presentation isn't just a
*  thing you present live, it's also a thing that you send around ahead of the meeting for someone to
*  read or after the meeting for people to debrief on and discuss and comment on. So we wanted it to
*  work beautifully on a big screen when you present on a TV, but also be something that you can consume
*  on your phone when you send it around. So a lot of that sort of like responsive reading and viewing.
*  The irony of this is what we almost ended up creating was a web page builder for presentations.
*  It had a lot of the elements of, you know, wissy wig creation and everything. And it was in many
*  ways more limited than what a typical slide deck is. It wasn't about dragging rectangles around,
*  because it had to be responsive and reflowing in all these cases. And so we sort of like paired out
*  a lot of those elements to make it simple and writing based. Ironically, and I can't even say
*  intentionally, this turned out to be a brilliant decision in light of AI, because so much of where
*  AI came along is that it's this tool that can turn writing into anything, and it can also write
*  anything. So the fact that we had large language models come along means that we built this interface
*  for a human to make a presentation like they're writing a doc. And then we basically had AI come
*  along that can write a doc about almost anything. And so we sort of put those two pieces together.
*  And what that looked like concretely was we actually originally launched the product just
*  about a year ago, so August 2022, with none of the AI stuff. It was just, you know, our motto at the
*  time was write like a doc, present like a deck. We launched on Product Hunt. It actually went better
*  than I expected, to be honest. We did kind of win our first early adopters, people that just really
*  bought the vision and maybe had that grievance against PowerPoint format along the way where they
*  sort of bought it. And so we got our core early adopters, people who really believed and saw the
*  potential of what we were doing. But at the same time, I wouldn't say that we broke out beyond that
*  initial core. People who really bought our problem space were into it, but it was very hard to take
*  a new person and teach them what a gamma was. It was this thing that was kind of like a presentation,
*  but it's really didn't have all the feature parity yet. And it had these other ideas too, which
*  if you got it, you got it. But most people didn't. They would sign up for our onboarding. They'd watch
*  a real short video of what our product was all about. And then we dumped them into a blank page
*  where we would say, good luck, hope you figure it out. And, you know, let's say 2% would and 98%
*  wouldn't. So the funny thing is that where AI first kind of entered the conversation for us last fall
*  was really trying to solve the problem of onboarding. What we wanted to say was, what if instead
*  of you having to make your first gamma yourself, we could get AI to spit out a first gamma for you
*  so that you would actually see the power of what we were building. And I don't think we had any
*  inkling of how powerful that idea would be or how well AI could do the job. You know, we thought it
*  would just be an initial rough skeleton that you could use just to sort of show you what our product
*  could do. It would mix in kind of all the different bits. And we started working on that and working on
*  it more and more. And the thing that we found was that it could do much better than we expected.
*  It actually generated a full presentation and fine images and sort of create layouts. It became this
*  really powerful way of showcasing all of the sort of building blocks we built up over the previous
*  two or three years. But then kind of what amazed us was that many people considered that a finished
*  product. They would say, oh, you've basically made my whole presentation for me. And like, yes,
*  I'll finesse it here or there, but you've now taken this task that would have taken me, you know,
*  like 10 or 20 hours of preparation and you've done 90% of it. That is kind of probably always
*  the mission we wanted to achieve. If you think back of like, oh, your presentation through tomorrow,
*  how do we solve it? But it never occurred to us that AI could solve so many of the pieces of it along
*  the way. And now that we realize it has, it's kind of changed the whole way we think about prioritizing
*  and planning our product because AI can be at the core of almost every bit of it. Hey, we'll continue
*  our interview in a moment after a word from our sponsors. If you're a startup founder or executive
*  running a growing business, you know that as you scale your systems break down and the cracks start
*  to show. If this resonates with you, there are three numbers you need to know. 36,000, 25, and 1.
*  36,000. That's the number of businesses which have upgraded to NetSuite by Oracle. NetSuite is the
*  number one cloud financial system, streamline accounting, financial management, inventory,
*  HR, and more. 25. NetSuite turns 25 this year. That's 25 years of helping businesses do more
*  with less, close their books in days, not weeks, and drive down costs. One, because your business
*  is one of a kind, so you get a customized solution for all your KPIs in one efficient system with one
*  source of truth. Manage risk, get reliable forecasts, and improve margins. Everything you need,
*  all in one place. Right now, download NetSuite's popular KPI checklist designed to give you
*  consistently excellent performance, absolutely free, at netsuite.com slash cognitive. That's
*  netsuite.com slash cognitive to get your own KPI checklist. netsuite.com slash cognitive. Omniki
*  uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button. I believe in Omniki so much that I invested
*  in it, and I recommend you use it too. Use Cogrev to get a 10% discount. Yeah, it's fascinating. I
*  can relate to that so much. For us, we tried to use templates as kind of the way to get people
*  somewhat past the blank page problem. And in fact, with Waymark for the longest time,
*  there basically was no concept of a blank or kind of empty starting video. You would always start
*  with some template, and there would be content in there. And then our idea was like, you use this
*  content as inspiration, and then you make it your own by putting your own content there. And I think
*  that helped relative to showing people nothing, certainly. But it was still a big hurdle that a
*  lot of people were like, well, I don't really get or know how to project my content onto this template.
*  It's a little tricky still. Similarly, we had some people that really took to it and loved it. But
*  then there was definitely a lot of people who were like, I'm still not quite getting how I'm supposed
*  to make something with this. And interestingly for us, it was also not really about the interface.
*  I don't know if you've had this experience, but we would kind of look for interface solutions to
*  some of these problems. And then I think in retrospect, especially now that we have the AI
*  layer, it has become clear to me that it was not so much an interface problem in many cases
*  as just a conceptual problem of what am I even supposed to do here? It's not that I don't know
*  what the buttons do, but I don't know what to do writ large, right? Yeah. What is this for? What can
*  I make with this? Why should I even be here? This has been a hard thing for me to grapple with as
*  someone who's always been kind of a product manager by training and assumes that the solution to every
*  problem is product, better product, more product, different products. People often describe gamma as
*  like if Notion and Canva had a baby. And when we look at both those companies, they're companies
*  that sort of saw so much of their success through yes, great products, but also these incredibly
*  vast communities and marketplaces of templates. Everybody who sort of like came to Notion or
*  Canva came there because they saw someone else make something really compelling with it. And
*  they're like, Oh, I get it. I see the value. And you can think of those template libraries as these
*  incredible assets that those companies develop often quite painstakingly over a period of years.
*  So, you know, like, I don't know the numbers, but let's just say Canva has like 10,000 or 50,000
*  templates in it. And that is like a huge part of the reason why you sign up for Canva. That's a
*  very hard advantage for a small startup like ours to overcome. We do not yet have the resources to
*  create thousands of those things until AI comes along. And suddenly what we found was we started
*  using AI to make our own templates. And then we're like, wait, why are we even having AI
*  make templates? Let's just have AI make a perfectly tailored first draft for you and cut out the
*  middleman of the template. And in doing so, hopefully also cut out the advantage that a lot
*  of these established tools have over us in their large template libraries.
*  So I want to dig into that in just one second, but just to give listeners who haven't probably
*  seen the app a little bit more context on specifically what I thought was really
*  compelling about it. Biggest thing for me right off the top was, and I tried this, I have this
*  thing that I created, the AI scouting report. So I went back to my notes, which I had used before
*  making any slides. And it was just, you know, kind of as your use case envisions, right?
*  Write like a doc and present. That's what I was trying to do. I had my doc and, you know,
*  all these bullet point outline type content, drop it in there and say, hey, you know, here's
*  what I'm trying to do. Make this. I'd say two things really stood out against everything else
*  that I tried. One was that the slides or I don't know what you use as for the individual unit,
*  if it's not a slide within the broader context, but the individual units, they all just looked
*  really good. Like the theme was really nice, the colors, the layout. I'm not even super
*  aesthetically sensitive, to be honest. You know, folks on the Waymark team know, you know,
*  a hundred times more about how to make something really look good than I'll ever know. And that's
*  honestly a big part of the reason I was kind of interested in building this sort of thing,
*  because I can't do it, you know, without tool assistance, but I can definitely at this point,
*  you know, recognize that the slides just looked beautiful and they made a, you know, that sub
*  second impression on does this look pro? Does it look like it's worth my time at all? I think it's
*  really the only one that passed that test that we demoed anyway. And then the other thing that it
*  did that I thought was really effective was it took my raw stuff, you know, some of which was
*  like kind of notes and some of which was kind of paragraphy and definitely not like slide ready or
*  even particularly slide friendly. And it put that into a text format that for the most part
*  captured what I was trying to say without distorting it too much, but also put it into
*  a format that actually looked like something you would present. And again, other, you know,
*  things that we tried kind of went off the rails in various ways, either like changing my story
*  entirely, which was pretty weird to see, or just like not changing it enough and just kind of like
*  printing out my paragraphs, you know, and it was like, well, this, I could have copied, you know,
*  that didn't save me much, right? If I was just going to go copy my paragraph in giant text blob
*  form. So I thought you guys did a very nice job of striking the balance there between transforming
*  my content, you know, so that it is more suited to this purpose of presentation, but not distorting
*  my content too much. So that's my pitch. I don't know if you would add anything to that that you
*  think is like the big reasons to go try the product, but those are the reasons that I found
*  that seemed to distinguish it. Well, that was a great pitch. Thank you. Yeah. I mean, that's sort
*  of the core thing. We focused on it to give a little more context on it. My first real unlock
*  with this was like my first week using chat GPT and seeing what people were doing with chat GPT.
*  And I remember people were doing all these things like write a story about, you know, a grilled
*  cheese sandwich getting stuck in the VCR, but in the style of biblical verse. And what was amazing
*  about it was first of all, just the creativity of AI and like what it can do far beyond, I think,
*  what any of us thought. But also what was amazing was this idea of like transformation. And this
*  whole term kind of generative AI has maybe mastered that the way in which AI is so good at
*  transforming things from one shape to another. So this idea that you can like take this and now put
*  it in hip hop lyrics or whatever is a neat trick. It's like a cool toy. But for us, the actual
*  powerful application of it is take my sort of like written bullet points or my big notes and turn it
*  into like a structured, thoughtful presentation. And I think we were all blown away by how well
*  AI can do that if you at least coax it in the right way. And so, yeah, I would say that's
*  a big part of our sort of secret sauce is transforming your raw notes into something
*  that feels coherent, compelling, and also visual. That's a big part of it. We have kind of a lot of
*  the visual building blocks that we can drop this into. The other part of it, which I'm sure we'll
*  talk about as well, is not just that first generation that spit out a presentation from me,
*  it's done, but helping me edit and refine as I go. We've also put a lot of work into giving you
*  alternatives or letting you try out different variants on top of where you started to iterate
*  your way towards the right kind of visual output. Yeah, I think that's a really compelling
*  paradigm as well. You said kind of AI can do this well if you coax it the right way.
*  I'd love to get a little bit more into how you do that. And I can tell you a little bit about
*  Weimarkside too. Kind of want to just compare notes because I think you're totally right that
*  transforming one thing into another is, at least with the current quality of models,
*  often where a huge amount of the value is, as opposed to generating totally new stuff.
*  If I had asked it to write my AI scouting report for me, that would have been useless.
*  But having notes and being able to transform it, that is useful. And the models can really do
*  a nice job on that. Ultimately, you're producing something that's highly visual. It's got layout.
*  It's got image content along with the text content. It's got structure in terms of bullet points.
*  It has all of this kind of structure. How do you think about representing that structure
*  for the AI? Obviously, folks who listen to this show know enough about this that whatever I dropped
*  into the tool is combined with some instructions, maybe some fine-tune model, a lot of things there.
*  But you also have to tell the AI this is kind of the space that you can project into. So how do
*  you think about describing that space and finding the happy medium between... You want to have a
*  simple notation. It doesn't take up too many tokens. Hopefully, the AI can rock it. But it also can't
*  be too simple because you do have a pretty rich grammar, so to speak, that you ultimately output
*  to. I'd love to hear how you've approached that. Yeah. This was, I would say, the hardest problem
*  for us to get this off the ground from the idea stage to the reality. We tried so many things.
*  We started with just plain text. And true enough, they can generate plain text with
*  bullets in it. And then we said, but it needs to have visuals and layout. And so we went down a
*  whole path of trying to just do everything through JSON. Let's represent this as structured data.
*  I want to have a timeline that's going to have three steps in it. And these are the things
*  in those steps. And that, we frustratingly got to the point of working 85% well. It would work some
*  of the time. And your curly braces and your semicolons would end up in the wrong place. It
*  all followed hard. And we cycled through, oh, let's try YAML instead. Let's go through this.
*  Let's go through that. Or let's try just doing text and then generating the formats.
*  We even explored thinking through more of the PowerPoint model, which is just like,
*  draw me this. I need a rectangle here and a rectangle there. And that's where the AI really
*  falls down because even though the AI seems like it can see, it really can't. It just is getting
*  text input and output. And so generating things on a grid almost never goes well.
*  I remember trying to get it to draw a pyramid shape, like three levels of a pyramid,
*  like you would see on a slide deck. And it could not draw a pyramid of triangles to save its life.
*  And so actually the thing we ended up hitting on, which kind of ties to our whole story where
*  we came from, was HTML. I think we realized that we had to sort of work in a format that the model
*  itself knew really well. And these models are trained by scraping the web all over the place.
*  So they've just seen huge amounts of HTML and stuff that looks like it. And I kind of alluded
*  to, we had already built our presentation builder through the lens of website creation. So mobile,
*  responsive, kind of made up of these different blocks that stack on top of each other.
*  And so we realized sort of the gunlock was, could we actually generate the sort of input and output
*  as HTML and then convert that HTML into our format? And that had a lot of benefits in terms of
*  there's a lot we didn't have to teach the AI at all, because it already knew how to make stuff
*  bold or how to make things into a table or how to make bullet points. That all kind of came for
*  free in its training data. And then we could just teach it the specific kind of tags and custom
*  elements that are unique to us. And even more where it's come in handy is when it comes to
*  editing and refining, we can feedback our data kind of in that format and let it kind of riff on
*  it. You know, we basically prompted and say, you are the world's best web designer. You have a gift
*  for writing clean, structured HTML. Your client gave you this HTML, doesn't do quite what it's
*  supposed to do. They want you to change this thing about it. And then we can apply tweaks on
*  top of that. And that's going to have to be the Luma Franca that really made AI powerful at doing
*  this. Certainly some commonalities with Waymark where I just was kind of in pursuit of the most
*  natural seeming, all, you know, obviously text only representation that I could come up with
*  that still kind of deterministically, you know, could be rehydrated back into
*  the full video form, right? So we kind of said, this is the format that the AI has to generate.
*  And if it generates in this format, then, you know, again, we can map that back onto the full
*  visual video space. And for us, that did get pretty simple in the end, partly because
*  our templates are pretty well formed. So, you know, you're not in general, like,
*  choosing specific locations or whatever, like that's kind of all baked in on some level to
*  the template. So you're really mostly focused on just the content, you know, what's the copy
*  going to be, what are the images going to be, et cetera, et cetera. It seems like you have kind of
*  even more degrees of freedom, but as you say, you can't give it like infinite degrees of freedom.
*  You presumably are not like, you're probably not giving it the level of freedom to be like,
*  how many pixels something is, you know, from the top or from the left, right? So,
*  so do you have like a vocabulary that's like a set of classes that it can apply that are kind of
*  semantic, like left side, tall, right side, right upper corner, these kind of, I imagine,
*  a vocabulary here. We do. Yeah, we have very structural elements and they all correspond to
*  actually things in our interface. You know, that's kind of what led us add this AI layer on top is
*  that we built all of these kinds of semantic building blocks that were things like side by
*  side layout or, you know, a table or columns or timeline or whatever it was. We had those building
*  blocks. And so then we basically teach the AI using a lot of our precious tokens, every prompt,
*  here are the building blocks you're, you're allowed to use here. Examples of how they work now,
*  see what you can do with this problem. So what's the model journey that you've been on?
*  You're talking about prompting, you know, with pretty detailed instructions, which suggests
*  maybe not fine tuning. So you're able to use an off the shelf commercial model with a
*  developed prompt. Generally the GPT models from OpenAI, they have so far been the leaders for us,
*  although we are now at a scale and a point where I think we're going to start shifting back towards
*  something like fine tuning or maybe even train our own models. We haven't really made a decision
*  there, but when we were getting started, we didn't have a huge vein of data to begin with.
*  You know, we were starting from scratch. And so for us, like few shot prompting, which a few
*  examples worked a lot better than trying to fine tune. We also happened to be launching earlier
*  this year, right at the time that OpenAI made the jump from GPT-3 to GPT-3.5, which totally changed
*  the interface, also totally changed the cost curve by making everything 10 times cheaper.
*  And there was no fine tuning on it. And so in some ways it made a decision for us. It's like,
*  is fine tuning really going to be 10 times more effective for us? The answer then was no, but
*  something I'm really keenly watching is the evolution of open source models and a different
*  foundation model providers. And so I think the story is actually about to invert. I think we're
*  about to be able to take now this huge number of things we've sort of generated as input to say,
*  okay, how can we actually train our own custom model and start to use that scale as an advantage?
*  Yeah, this is a really interesting topic. Obviously everybody's watching the open source
*  developments and we're now in the llama two phase of history in the open source world. I'd love to
*  hear more about how you think about these trade-offs. People all the time are like,
*  this kind of line of thinking, I guess, went mainstream with the no motes Google memo. I
*  think that article certainly got a lot right about all the great things going on in open source.
*  I also say got some things wrong in terms of like, I still definitely think there are some
*  motes, but from an individual application developer standpoint, 3.5, as you noted, is cheap.
*  It is fast and it is scalable. They have obviously very nice parallelizability for you
*  and you only obviously get charged for what you are using in terms of tokens.
*  What's the other side of that look like for you and what would be the reasons to go toward the
*  open source? Where is 3.5 not doing it for you? Let's start there. What would you hope to make
*  better? Yeah. So I think there's a couple of areas or a couple of dimensions that you could think of.
*  One on the just overall intelligence. So GPT 3.5 is remarkable, certainly. GPT 4 is still better.
*  It's just sort of like hugely expensive and slow for what it does. And so the dream is,
*  can you get GPT 4 level performance while still getting all those qualities you named in 3.5?
*  And I don't know if we're there yet with any of the open source models that I've seen,
*  but I think fine tuning is one path for how to get there. I think the other thing is that
*  GPT 3.5 is really trained to be a chatbot. It really wants to be a helpful chatbot. And
*  many things in life do not fit the schema of being a helpful chatbot, including generating an entire
*  presentation. And so I think this is where the opportunity is to actually take other models in
*  different directions and have full control over that experience. And so for us, that might mean
*  training it for more specialized tasks, but it also might just mean really pushing the use case
*  of document generation and editing beyond what chat type tools we made for. But yeah, I'm also
*  curious about your experience on this and how you have sort of like weighted different models and
*  think about the open source stuff. I'm not sure. Right now we are still using a fine tuned
*  open AI model, very much like you kind of considering, is it time to move on to something
*  else? Our approach has historically been not too focused on the cost because we do have
*  very high value users. I think this is kind of just a more result of how we've gone to market
*  and the fact that we've sold to big companies. So you could move with a product like ours,
*  and it's probably similar with yours, right? You could go directly to users. We've done some of
*  that historically. We've actually found the most business success going to larger organizations
*  that need to scale this sort of video production and selling to them on like a license basis. With
*  that, our emphasis has always been maximize quality for them. The AI in terms of the overall
*  revenue and cost structure is not that big of a deal. So we've never shied away from kind of
*  paying top dollar for tokens. But I'm now getting to the point where I'm like, yeah,
*  maybe this fine tuned model could soon be eclipsed by something else. And maybe it's not
*  necessarily eclipsed in terms of like overall quality of output, but maybe latency, maybe
*  cost, not because we're trying to save costs, but maybe we want to, what if we could generate
*  multiple things at a time, you know, and now instead of one, you get to look at three different
*  things or whatever. So it just feels like there's a lot of possibility at 3.5 actually is one of the
*  things that I've been considering. I don't think it would probably work super well if we had a
*  hard coded, you know, like single prompt to rule them all. I think we would have a hard time
*  matching our fine tuned model. And I haven't proven this yet, but I'm pretty optimistic that if we
*  did a sort of dynamic prompt where, you know, we're bringing in more relevant examples for it to
*  borrow from that we might get there. I haven't really considered anything specific to the chat
*  modality. Are you seeing like specific weird behavior from the, that like is grounded in the
*  chat nature of the thing that is causing you trouble? Yeah, sometimes. I mean, what's funny
*  is, you know, we had this whole part of our product, we didn't talk about as much where in
*  gamma, once you generated your presentation, you can say, I want to work on, we call them cards,
*  not slides. That's just us trying to be sort of the anti PowerPoint and therefore not necessarily
*  borrow all the same language, but you can think of it as a slide. So I'm going off and I'm editing
*  slide three and I say, Oh, I want you to change the layout of this. I want you to make it look
*  more visual or make this more concise, or I want you to translate this into Spanish or whatever it
*  is. You can basically talk to your card and transform it. That's kind of my opinion, the
*  coolest part of our product. Although it's also the trickiest one to get right, because you mentioned
*  degrees of freedom. There's just so many degrees of freedom of what you could even ask for, what
*  your content looks like, where it can go. And so it's really doesn't work a hundred percent of the
*  time. If I'm being honest, I think it works well about half the time. The other half it doesn't.
*  There's multiple reasons why it doesn't work well that other half. But one of the reasons is that
*  we've sort of co-opted the chat interface to power this. And sometimes the chat interface just wants
*  to be so helpful to actually follow your instructions. It just wants to start chatting with you and being
*  your friend. And so I think that's a place where fine tuning or just using open source models that
*  aren't pushed in this direction could be really useful for us. Yeah, that's kind of related to
*  the recent GPT-4 is getting worse brief news cycle, where as it kind of later became clear,
*  the authors had run this coding benchmark. And what they didn't account for was the fact that
*  with the recent update, the model GPT-4 started returning basically just a markdown wrapper
*  around the code. And they were just executing the benchmark in kind of the programmatic way that
*  benchmarks are often executed at our peril, I would contend. And then they're like, well,
*  this code doesn't even execute. It's got syntax errors in it. What a terrible regression. When
*  you look at it and you're like, oh, well, it is actually responding pretty sensibly. I mean,
*  it feels like that's something you should be able to get under control. But it sounds like you're
*  seeing more kind of almost opinionated kind of responses where it's not just that it's a syntax
*  thing, but it's trying to take you in a different direction or suggest something else. Like,
*  what are those behaviors that you're seeing that you kind of haven't been able to corral?
*  Yeah. One version of this that we've encountered is you'll be working on a slide about rock music
*  and you'll say, I want a picture of a panda for this. And it'll say back to you, I don't think
*  a panda is a good idea. I think you want a picture of a guitar instead. But I want the panda. Like,
*  I'm in charge. Yeah. Well, that's going to be, when the co-pilot pushes back, it's going to be a
*  major phenomenon across a lot of different experiences in the years to come. I agree with
*  you, by the way, that I think the Edit with AI experience is one of the coolest aspects of the
*  product. Believe it or not, I didn't even get that far in my initial demo. But in preparing for this
*  conversation, I went back and spent a little bit more time with it. And I thought that was really
*  something that we could take some inspiration from also. We kind of have two layers where,
*  first, it's like, tell us what video you want, we'll make it for you. Boom. Then you have your
*  lower level controls where you can go change any of the copy and take it with colors and swap out
*  images and crop and whatever. A lot of interface there. But I do think we stand to improve the
*  product still with an intermediate layer. So I'm not exactly sure what our version of what you have
*  would be. At a minimum, I think just asking the AI to just make changes, even if it's just operating
*  on the whole video, I do think there's room for more verbal iteration before you have to get into
*  that nitty gritty of the UI. So I did take inspiration from that. I thought it was really
*  nice. The other thing I thought was really good, I'd love to hear what you've learned from this or
*  what you said, it only works half the time. It may be an actual quantified number because I also
*  thought it was really smart. And I really don't know why more products don't do this.
*  When you do the chat with AI, the product then shows you back original and suggested update.
*  And then you can click back and forth and be like before, after, before, after, which one do I want.
*  And presumably that is a really good feedback signal for you, which maybe you're not even really
*  fully able to take advantage of yet. As you have your eye on fine tuning, I imagine that is a
*  real source of intelligence about what people actually want.
*  Totally. This was inspired by Mid Journey, which I think is still maybe the most impressive AI
*  product I've ever seen, despite it's, in my opinion, enormously frustrating interface.
*  But what strikes me in kind of observing their product development is that so much of it seems
*  tuned toward gathering the data that you need to make the system better over time. So their
*  product is all about generating variations, upscaling the ones you want, and even liking
*  different parts of it, all in the interest of kind of creating that flywheel. And so
*  it's funny because the landscape of how do we use that data is not fully formed. We don't quite know
*  how it will be incorporated. But if you don't have that compass in the first place, you just
*  have no idea where you're going and where it even folks your efforts.
*  Do you use any system right now for kind of prompt testing, A-B testing? I use HumanLoop in some of
*  my activity for stuff like that. But do you have a tool that isn't, you know, obviously a lot of
*  people have just built their own homegrown stuff. But have you guys homegrown DIY that kind of stuff,
*  or have you found any tools that help wrangle this problem? So far, it's pretty much homegrown,
*  particularly for prompt evaluation. Like we built our own kind of little studio for editing our
*  prompt and seeing how it works on different examples. But it really feels like we're in the
*  stone ages of this kind of technology. If I consider how high stakes these prompts are to our business,
*  it feels like the equivalent of running a huge software code base with no automated tests in place
*  and just kind of like going based on vibes to know if the stuff you're changing make any improvements.
*  And maybe worth mentioning, my background, a lot of our team's background at Gamma is from a company
*  called Optimize League, which basically tried to make A-B testing a widely practiced practice across
*  kind of marketing and software development. And so that mindset of gradual rollouts, A-B testing,
*  measurement is like deeply in our DNA. We've looked for ways to incorporate it,
*  but the tech isn't there yet on the AI side. And I'm looking forward to see what does come out in
*  this space over the next couple of months to make this process better. Because it's ripe for,
*  I wouldn't even say disruption, but just personal innovation.
*  I definitely check out HumanLoop, but we had CEO Reza Habib on the show some episodes back. And
*  I think they are building some pretty good infrastructure
*  that is specifically focused on app developers as the target customer. Not to be doing BD live on
*  the show here, but I think that would be worth a look. Going back to just the fine-tuning thing
*  for a second, if you were going to go fine-tuning open source, right? Still with open AI, the reason
*  we have continued to use that fine-tuning is it also has very nice properties around,
*  just pay for what you use. You don't have to have dedicated resources. They kind of handle
*  the auto-scaling for you and they seem to do a very nice job of it, which is much appreciated.
*  When I've looked into what would it take for us to really bring to production a fine-tuned model,
*  actually doing the fine-tuning at this point, I think would work. I would have said that probably
*  as of the mosaic 7B release from maybe a month and a half ago or whatever. That seemed to be the
*  moment where it was like, okay, this is probably going to work for our use case now. Putting that
*  into production, having inference that auto-scales. I'm a big believer in the vision of the hugging
*  face inference endpoints. I've looked at replicate, even mosaics service, but the auto-scale up,
*  scale down, if you have any sort of bursty workload, which we do, and maybe I don't know
*  if that's a problem for you, but we do have quite bursty workloads where it'll be like,
*  even just as simple as a demo. We work with these big companies, now everybody's together,
*  they're all doing it at one time. We also have some things where we process images for users and that
*  because the images are many per user, we're often kicking off, can we process 100 or a few
*  hundred images at a time? We want to return that as quickly as possible. I haven't been able to get
*  over the hump that it would be worth it for us at this point to go with that open source approach,
*  just because it seems like the inference and the auto-scaling and all that stuff is not quite
*  there yet either. What's your outlook on all that? Yeah, I think you're generally right. This is one
*  of the factors that has held us back from going all in on AI image generation. We do have a lot
*  of images in our product, but we've mostly held off from using AI to generate them. The biggest
*  reason for that is mostly that they look like crap most of the time, although that is rapidly
*  changing and the quality is improving. For us, it's generally open source models that are the
*  leading ones in image generation, at least the ones that are available and solving that problem.
*  I'll do some BD back on you though, which is we're using a system called Base 10 that I think
*  actually solves a lot of the issues you brought up pretty well, which is they both integrate
*  fine tuning to their platform, so you can upload a lot of input output examples. They do pretty
*  fancy auto-scaling where you just figure out what kind of systems you run. You can handle bursty
*  traffic and bring up and down servers as needed. We're actually about to roll out our own AI image
*  generation serving powered by them. I think it's going to work pretty well. Hopefully, by the time
*  this podcast is out, people will be able to try it. That gives me some insight because I noticed
*  that, at least as far as my experience seemed to be, I didn't detect any generated images in
*  what came back. It seemed to be all searching through existing libraries. I guess the barrier
*  to that primarily, as you said, is that they just haven't looked that good until recently.
*  Is it now going to be stable diffusion Excel that's getting you over the hump into moving into
*  product? Yeah, a lot of these things to me come down to thresholds where it's like, it's not good
*  enough until it is, and then when it is, it goes super wide, super quick. It passes so fast from
*  being not good enough to good enough. Image generation is interesting because I feel like
*  we are right on that line. Actually, mid-journey already passed, I would say, but open source
*  models have just crossed that line. It's not clear if it will stop. I think it will keep on
*  going and become pretty breathtaking and incredible as well. Video generation feels like it's in a
*  similar place, and I'm not sure what new modalities are coming after that, but as a
*  developer of an AI-enabled product, what it feels like we're doing is just trying to put ourselves
*  in a position to benefit from these sudden sparks of innovation happening all around the ecosystem.
*  We really have to have a hole to put cool images in so that when cool images are ready,
*  that can just flip it on. It's hard to even think about a year ahead, what are all those new
*  opportunities that are going to be emerging that we can take advantage of? 3D models, voice,
*  all these things. It's almost staggering to think of all the places AI can plug in.
*  Yeah, there have been some really incredible voice releases just in the last week or so as well,
*  where I listened to, shout out to the AI breakdown, which we actually did a feed swap with not too
*  long ago and shared one of their episodes, but he just did one where he had a cloned voice from
*  11 Labs read an essay in his voice, and it was insanely good. I literally could barely tell,
*  and if he hadn't specifically called it out, even with him saying,
*  now I'm going to go to the AI voice, and then the AI voice takes over, it was like,
*  wait, that's the AI voice? That was the switch? I mean, it's crazy, and PlayHT just dropped
*  another one too in the last day or two that is looking or sounding phenomenal. So yeah,
*  it's wild. Do you think that this, as you move to AI image generation, is that a compliment to the
*  existing libraries? Does it become your primary go-to? Because there's a whole ball of wax too,
*  as you know perfectly well around how do you select images out of a library? I think you guys
*  did a nice job of that, certainly relative to most things I've seen, but it does remain a challenge
*  to figure out what out of, for example, Shutterstock's hundreds of millions of
*  images actually, not just make some conceptual sense, but actually look the part very tough.
*  It's a really hard one, and I think we're too early to say. I think we are still going to rely
*  on image libraries early on because we just know there's some level of quality bar on those,
*  and AI images are still uneven. They still feel like a toy much of the time, and our aspiration
*  not to just be a toy, but to be something much more than that. But at the same time,
*  there's a level of magic to them and also a level of control. Particularly thinking about a
*  presentation, we want to be tackling problems like I want to have 12 images throughout my
*  presentation, and they should all be stylistically in color coordinated. That's a problem that AI
*  images will go from being bad at to good at in the space of months. It's just a matter of us
*  stay on board while they do. So we take a somewhat different approach on this as well. Most of the
*  products out there have just embraced the AI image generation come one day. If it doesn't look
*  good, whatever, hey, we're in this moment, it's cool, whatever, we'll just do it. That seems to
*  be the prevailing approach. I think for pretty similar reasons, our companies have not rushed
*  in on that as much and have said, if the quality is not there, in our case, a lot of the videos
*  get put on TV as TV commercials. We're just like, people are not going to want to put this on TV.
*  And for you, people are not going to want to stand up in front of an audience that matters to them
*  and present this. So if it doesn't hit that bar, then it maybe doesn't work. The best approach
*  that we've taken so far has been, well, I guess it's complicated. There's a few, but we like to
*  use our users' own images wherever possible. We've had a lot of success with the blip family of
*  models, which is out of Salesforce, to try to figure out which of the images that they have
*  would make the most sense here. And then we've also had a lot of luck with Shutterstock's
*  computer vision API when we want to supplement their assets with other assets. I don't know if
*  you've used that, but it's actually quite good at bringing you back visually similar. You'll have
*  some nuances there because visually similar can return things that are not content similar.
*  But we've found, I think, a good way to kind of deal with that just by also looking at the metadata
*  of the image, which tells you what the content is. So once you apply the computer vision side
*  to get things that look the part and then kind of filter for things that actually relevant or
*  appropriate content wise, you end up in a pretty good spot. But you do need, in our case, we have
*  user images that we can put into the computer vision to kind of expand on their, we call it
*  their universe of libraries because it starts with their cluster, but then we kind of try to
*  build that out. You kind of said strategically, you are trying to put yourself in position to
*  benefit from ongoing advancements. That's like a mantra for me too. The waterline is always rising.
*  What are your main priorities right now that you're building toward?
*  Yeah. So we talked a lot about kind of the sort of AI portions of our priorities. I think the other
*  one is really anchoring back with our origin story is thinking about the medium and the format itself.
*  So how do we make gamma the best way to present your ideas across a range of different settings?
*  So some part of that is that to really go up against these titans like PowerPoint,
*  you just have to have a bunch of other features to do that well. Everything like export this as a
*  PDF or add speaker notes or all those things. But actually the kind of most surprising opportunity
*  that we're pursuing in the sense that I didn't really see it coming when it began was the number
*  of people that use our product to make the website or a web page or something that is like their
*  digital face on the internet. I think I mentioned that what we accidentally created was a website
*  builder for slides and it turns out it's also a big website builder for websites. In part because
*  it doesn't have all of the complexity of a big complicated website builder. It's write like a doc
*  and then share like a website is kind of the promise. And so we've actually been pulled by
*  our users in the direction of doing that. And so we're in the process of letting you support just
*  publishing these gammas to your own custom domain. And along with that comes, you know, like let's
*  set up the rest of the parts of the website. I want us to have a header and a footer and forms
*  on it and all those things. And so we are rapidly adding those kinds of capabilities.
*  And it's something that raises a lot of hard to questions for us. It was hard to be a great
*  presentation tool and a great website builder and a great document editor all at the same time.
*  Although AI makes it easier than you might think. I think it really changes a lot of our assumptions
*  about how a company competes in different spaces. But for us, what that really means is we are trying
*  to sort of forge our own path between these different media. We want to make a gamma a very
*  unique thing that is unlike what any other company creates, but hopefully well suited to a lot of
*  people's tasks. And so a lot of what we're doing is just trying to figure out all the different
*  design details of how to do that. Yeah, that's interesting. So I was going to ask also about
*  how you think about competing against these giants, right? Because I mean, the products that you're
*  taking on in being the anti PowerPoint or, you know, the anti by extension, maybe the anti Google
*  slides, you know, whatever deficiencies they have in terms of user experience, they certainly have,
*  you know, major advantages in terms of familiarity and just general distribution. So how do you
*  think about that? I mean, it seems like, you know, if you were going to go out and try to raise money,
*  I'm sure that the number one question would be like, what's going to happen when Microsoft
*  rolls out their AI slide maker? You know, do you think it's just going to continue to not be that
*  awesome? Or like, you kind of hinted at maybe like, we want to make different stuff, like, presumably
*  they're going to continue to make slides in their way. So how do you think about kind of carving out
*  a, is it carving out a space? Is it just being better at the core thing? Like, what's the strategy
*  for taking on these giants? That's a good question. Cause it's one that keeps me up at night thinking
*  about where these giants will evolve. You know, our main strategy has always been let's carve our
*  own path. Even before AI, that was it. We don't want to directly compete head on with these tools
*  in part because they're very good at what they do. We really like to do something different and use
*  AI to help us do something different. That said, every month that goes by without Google Slides AI
*  and PowerPoint AI actually being released is another month that I find the temptation of, well,
*  maybe we should compete head on though. I don't know. I think the jury's fell out on how good
*  these tools will be and also how accessible they'll be to different audiences. You know,
*  I think everyone's going to focus on their core. And for Microsoft, that core is very much just
*  sort of like big enterprise-y work setting. And so I don't know how well, for example,
*  the small business will be served by what they're building or how well education will be served.
*  I truly don't know. And so I'm eagerly awaiting where they take it. I think that Microsoft
*  particular is a pretty fierce competitor. They are like sort of the big oil tanker that doesn't
*  turn quickly, but when they are, they just relentlessly move. And so our best bet as a
*  startup is just to be nimble and try to carve our own path and also always stay ahead and do
*  something a little bit different than what those giants are doing. The website market is a bit
*  different though, where it certainly has incumbents, but it doesn't have any incumbents on quite that
*  scale. And so far, none of the incumbents in this space have really shown that much interest or
*  savvy in deploying AI. And so it's also a place we're looking at, like maybe this is even a bigger
*  opportunity to go after. And I think we'll just have to see. This has been obviously a hot topic,
*  of has Google lost its ability to ship or why aren't you can never change Gmail?
*  And certainly they're starting to ship stuff, but I would say the writing assistant experience that
*  I have in Gmail is still not actually useful in part because mystifyingly to me, they don't give
*  you the freedom to actually direct the AI. I don't know if you've used this particular interface,
*  but you have a few modes of change they allow, like shorten it, elaborate it, whatever. But it
*  never allows you to say, do this to it, which is just a kind of strange gap to me. Enterprises
*  are definitely not ignoring this and they are shipping stuff. But then other times you see
*  things like that from Gmail and you're like, that seems pretty half-baked. Do you feel like this is
*  just such a different discipline that it's actually going to be hard for these organizations or
*  do you think that they're on the verge of figuring it out? Or what do you make of what we've seen so
*  far from big companies rushing to ship AI products? I used to work at Microsoft and so I think I have
*  some sense of how these companies operate internally. And I think when you're not inside them,
*  it's easy to underestimate the sheer scale of the challenges that they face operating at the
*  scale they do. Many of these products like Gmail and even like Google Slides have hundreds of
*  millions of users in a wide variety of circumstances. All of them have their own
*  different contracts with how they use your product. Their different languages that they speak,
*  their different data privacy and sensitivity requirements. And so I don't envy the people
*  who are trying to juggle all of those different requirements and stakeholders when making decisions.
*  The sheer number of humans you have to convince internally to make even a relatively low risk
*  change is small and AI presents a huge number of risks that we're only beginning to understand
*  from hallucination and misleading people to like misuse and abuse. And so I think these companies
*  hands are just incredibly tied, much more so than startups are. And so for them, I think even though
*  they feel a lot of urgency internally, in many cases their best bet is to let startups establish
*  patterns, let smaller companies establish patterns and then they can follow and incorporate those
*  over time. And they have the distribution advantage that they won't be doomed by doing that.
*  They will take their time and get it right and they will do it. And so I think often to those of
*  us who are in these fast-paced environments, their behavior looks odd, but it's actually perfectly
*  rational, understandable, even where they're coming from. And I think what it means is if you want to
*  be on the cutting edge of where AI is, you almost have to be outside those ecosystems. And that will
*  give you a very good sense of what will be in tools like PowerPoint in one or two years.
*  One theory I've been kind of kicking around is the idea that these super complicated, over-featured,
*  over-built, you know, I can't find what I want in this system type of systems. And as you mentioned
*  too, like the language complexity, I mean, the complexity certainly is vast. You could kind of
*  tell two, you know, opposing stories. One would be all that complexity makes it hard to apply AI
*  because, you know, it's just even compounding the complexity. The other story would be like,
*  maybe the AI can kind of smooth over all that complexity somehow by, you know, kind of reducing
*  it all back to like, hey, now you can just, you know, engage with natural language and the AI will
*  be the one that has to deal with all that complexity. Which way do you think that that,
*  obviously it could be contextually dependent, but, you know, which of those stories do you
*  ultimately believe in kind of coming to predominate? So far, it feels like the tools
*  that have been successful with AI are the ones that have been able to pick off like narrow and
*  specific workflows and carefully craft, you know, prompts and examples to be able to tackle those.
*  But I would be a fool if I claimed that I could predict where these models are evolving, even
*  over the course of a year. And if anything, the trend in AI has been towards surprising
*  generalization of abilities. It used to be that you have one model for translation and one model
*  for search and one model for summarization. And now we see these sort of God models that can do
*  it all. And I think that might only accelerate. And so I wouldn't even dare predict how this
*  story is going to evolve. Well, your app is Gamma. It's at gamma.app. And it's a fun, for my money,
*  the market leading AI card presentation maker today. So great work on it. Keep it up. Anything
*  else you want to make sure we cover before we break? No, thanks so much. It was great, Chad.
*  I'm a big fan of the podcast and appreciate the plug. Thank you very much. Well, again,
*  keep up the good work. John Nirona from Gamma. Thank you for being part of the cognitive revolution.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike
*  so much that I invested in it and I recommend you use it to use cog rev to get a 10% discount.
*  you
