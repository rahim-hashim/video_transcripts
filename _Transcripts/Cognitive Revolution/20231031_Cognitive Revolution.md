---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 5560s
Video Keywords: []
Video Views: 570
Video Rating: None
---

# Hardcore AI for History with Mark Humphries, History Professor at Wilfred Laurier University
**Cognitive Revolution "How AI Changes Everything":** [October 31, 2023](https://www.youtube.com/watch?v=IcIRbEXBjcQ)
*  The vast, vast majority of people are still at the stage of encountering chat GPT for the first time.
*  There's a huge learning curve between, wow, chat GPT can write a poem in the style of Bob Dylan,
*  to you can actually use this to do something very constructive, and I'm going to trust it with my
*  data. The tricky thing is I think it also scales up expectations. What AI is able to do with an
*  assignment is probably going to become the minimum. If you have someone who is unable to achieve kind
*  of the level of GPT 3.5 on a given task, it's unlikely that that person will be successful in
*  that job. What we need to do is teach people to use this in such a way that they exceed the baseline
*  level of the model. It's not going to be possible for everyone, just in the same way as not everybody
*  gets an A today, and that's kind of just how things work. But I also do really worry about the fact
*  that just, unfortunately, a lot of people cannot write at a GPT-4 level. One of the things I said
*  to the OpenAI team when I was doing the red teaming was like, for the vast majority of people,
*  this is super intelligence. It's just not super intelligence to you because you're really smart.
*  Yeah, I mean, I think that those are real problems that we have to contend with as a society and
*  that are much larger than just higher education. That's pervasive. Hello, and welcome to the
*  Cognitive Revolution, where we interview visionary researchers, entrepreneurs, and builders working
*  on the frontier of artificial intelligence. Each week, we'll explore their revolutionary ideas,
*  and together we'll build a picture of how AI technology will transform work, life, and society
*  in the coming years. I'm Nathan Labenz, joined by my co-host, Eric Thornburg. Hello, and welcome
*  back to the Cognitive Revolution. Mark Humphries is a professor of history at Canada's Wilfrid
*  Laurier University, where he has published widely on various aspects of Canadian history, including
*  the inter-civilizational fur trade of centuries past and the post-war experience of Canada's
*  World War I veterans. I invited Mark to do an episode after he reached out to me to tell me
*  that my tip to fine tune GPT 3.5 on GPT-4 reasoning had helped him get over some humps in his own
*  archival research. Along the way, he told me about all the things that he'd tried that hadn't worked,
*  and in the process proved himself to be one of the world's leading adopters of AI technology
*  in the field of history. A click to his blog showed that he's also been an early explorer of
*  how to use LLMs in classroom settings, having experimented with different policies and guidelines
*  over the course of two semesters already. In this episode, you'll learn a bit about how history is
*  done and hear about some of the idiosyncratic challenges that Mark has had to overcome on his
*  path to an AI agent for archival research. This is practically valuable knowledge that does at
*  least partially generalize to other domains. But beyond that, I think this conversation has a few
*  important things to teach us. First, the speed of AI diffusion really is different from anything
*  else we've seen in the past. Because it happened so long ago, it's easy to forget that the industrial
*  revolution unfolded over three generations from early steam engines to well-functioning locomotives.
*  Today, in contrast, while the physical build-out of GPU-loaded data centers is obviously a very
*  real and major investment, which is currently bottlenecking the field to some extent,
*  the distribution network for AI existed before the technology itself. And as such, we're seeing deep,
*  expert-quality applications pop up everywhere just months after the technology first became
*  reasonably useful. Second, the competitive advantage that Mark has recently gained in the
*  production of archival research is major and likely to drive continued rapid adoption even in such an
*  apparently unrelated to AI field as history. Simply put, Mark can now process a thousand times
*  more documents than he previously could, and the nature of the searches that he can perform has
*  qualitatively changed. Most historians won't have to implement their own systems, of course. They'll
*  wait for products to be built for them, but they'll have no choice but to use such tools to get the
*  same value from the historical record that Mark now can. Third, local leadership is often quite
*  out of touch when it comes to AI regulation, and this can be costly. Mark has accomplished all that
*  he has despite the fact that certain governmental archive rules prevent him from using commercial
*  APIs. And meanwhile, at the retail level, Claude is still not available in Canada for reasons that I
*  don't really understand, but am willing to guess based on the fact that Anthropic just launched
*  Claude in dozens of other countries has something to do with the Canadian government scoring an own
*  goal in its effort to protect its citizens. While I'm definitely not one to dismiss AI risks or the
*  need for oversight, the quality of decision making really does matter. By slowing down such a unique
*  AI success story as Mark and preventing access to what is arguably the most safety-focused AI
*  product effort in the world today, Canada's current policy provides what I consider to be unfortunate
*  support to reckless calls for uncritical techno-optimism. Finally, and perhaps most importantly,
*  the big picture perspective from history itself, which Mark offers at the end, reminds us that,
*  among other things, technology-driven economic restructuring always has winners and losers,
*  and the transaction costs throughout history have often been extremely high.
*  As always, if you find value in the show, we'd love it if you'd share it. I'd suggest that you
*  send this one to somebody in your life who you think has the potential to be like Mark, by which
*  I mean someone who can take up the mantle of figuring out how AI can drive 100x productivity
*  gains in their own corners of the world, while also keeping in mind that everything has pros and cons
*  and that the thoughtful application of technology is always critical to positive outcomes. With that,
*  here's Professor of History and AI and History pioneer, Mark Humphries.
*  Mark Humphries, welcome to the Cognitive Revolution. Thank you very much for having me. I
*  enjoyed the show very much. I'm excited to have you here as well. This is our first episode on
*  the use of AI in the practice of history and the teaching of history, and also an opportunity for
*  us to learn, I think, a little bit about what history may have to suggest for us as we try to
*  get ready for this AI wave to grow bigger and bigger. I guess, for starters, I'd love to hear,
*  because obviously you come from a background not typically associated with the latest technology.
*  How did it come to pass that you have gotten obsessed with AI and gone down this rabbit hole
*  yourself over the last year or two? Yeah, sure. It's funny. I mean, I hear a lot of people who
*  kind of get interested in AI do kind of come to it from strange kind of serendipitous kind of ways.
*  I started out being very interested in programming when I was young. I was interested in the whole
*  deep blue and Kasparov stuff in the 90s. When I was young, I built a computer game, Xs and Os,
*  right? Where you're playing against the computer visual basic built website. So I kind of had a
*  bit of an interest in tech in general, got into history as a student. And my first kind of foray
*  into machine learning was actually in translating German histories of the First World War. And this
*  was through a program called Abbey Find Reader. I don't know if you've ever heard of this, but
*  it's an early kind of OCR program. And you could kind of bootstrap it to also teach it to read
*  things that were kind of not conventional script. And a lot of the early German stuff is written in
*  a different kind of typeface. So I spent some time playing around with that. It worked okay,
*  not great. And then in the last 10 years, as part of a digitization project that I headed up where
*  we digitized about 12 million pages of records, the goal there was always to try and use AI to
*  do something with it, right? Because it's just too much material to go through. And it's in the
*  context of what's happening now. It's kind of the perfect example of what to do with this stuff.
*  Because it's a mixture of handwritten records, there's no standardization, like going through
*  it is just a nightmare. But obviously, the machine learning wasn't there a few years ago, it was just
*  didn't work, right? I mean, in terms of trying to train on all these things.
*  So when chat GBT came out last fall, like a lot of people became very excited and immediately began
*  to see, oh, here are all those things that have always been really interested in being able to do
*  with the computer that now seem to be a little bit more possible. And add on to that the fact that
*  you can actually get chat GBT to teach you how to do a lot of the coding that you need in order to
*  do these things. So it both brought about kind of the abilities that I needed for a long time,
*  or I was interested in, as well as the ability to learn how to do these things, right? Which
*  before would have been pretty prohibitive. Yeah, that's interesting. And just for quick context,
*  we'll circle back to this a little bit later, but we connected originally, you sent me a very
*  nice email that just shared the story of how you had tried the trick that I suggested a few episodes
*  back on fine tuning GPT 3.5 on GPT 4, or I guess any quality reasoning and getting it to kind of
*  mimic that reasoning, which is proof effective for me and also proof effective for you.
*  What stood out to me about that email, honestly, most was not that that had worked, although it was
*  definitely cool, but it was the many things that you had tried to get at this problem beforehand.
*  And I was like, man, this is somebody who has really, this is not a chat GPT user, but a chat
*  GPT user plus someone who's kind of explored a lot of different aspects of AI. So I thought that was
*  super cool. Before kind of coming back to the current techniques that are starting to work for
*  you. One thing I'm always really interested in is kind of what the state of AI was in a given field
*  up until pretty recently when these kind of generalist systems started to come online and
*  also how those are now interacting, if the old ones are just kind of falling away or if they still
*  are kind of state of the art because the tasks are narrow. So you talked about that a little bit with
*  the one program that you're using for the German work. I want to hear a little bit more about that.
*  You mentioned a program called, I guess it's Transcribe Us as well. But yeah, take us through
*  kind of AI and history pre-chat GPT just to set the stage.
*  It's interesting, right? I mean, myself and a friend and colleague of mine, John Maker,
*  were working on those German histories back in about 2007. So this is pretty early, right?
*  Nobody's talking really about, certainly not in the humanities, about machine learning and deep
*  learning is kind of still a little bit away at that point. And that was when historians started
*  to get kind of interested in the technology in the sense that what you can do is you can
*  begin to do OCR, right? And just for context for your listeners, in history, it's all textual
*  documents. So the biggest problem we have is to do anything digital, you have to convert
*  the material from text into obviously machine readable format. Handwriting has obviously been
*  the big problem for that. But early on, this kind of process of machine learning, you could apply
*  it to more and more text because again, typefaces are not as easy to use as they are to use in
*  the digital world. And so you could apply it to more and more text because again, typewriter
*  fonts change over time, right? And the ways newspapers were printed, if you ever look at
*  kind of those old Revolutionary War period newspapers, the typeface looks weird, right?
*  You've got F's that look like S's and that sort of thing, right? And so that was kind of the first
*  era. And I think when John and I were doing some of that back then, that was unbeknownst to us at
*  the time, kind of cutting edge in the sense we weren't thinking about it that way. But it was
*  like, oh, you could do this neat thing with this program. And then in the night, in the 2010s,
*  was that people got increasingly interested in visualization. So taking big data and creating
*  word clouds and things like this. That never really appealed to me all that much on a personal level.
*  I mean, you went through an awful lot of work to kind of produce, you know, something that might
*  translate into one sentence in an article. So not really worth your time. So that's where a lot of
*  the field went though, into that kind of what can you do with big data? And a lot of it was this
*  visualization kind of stuff, right? Transcrebus is an interesting program. It goes back a few years.
*  It's changed a lot in the last year, which is fascinating. It's the first kind of good program,
*  I think, that is able to accurately transcribe handwriting, right? And especially early handwriting.
*  I mean, your listeners are going to be familiar with, you know, chat GBT's or GBT four's ability
*  to read handwritten documents, right? But historical scripts are much different. They're very flowy.
*  They have a very different type of handwriting. They're often hard to read, right? So you can
*  imagine how much handwriting varies from one person to another. So trying to train these models
*  to read handwriting is very difficult. Transcrebus did a pretty good job. So back in the winter,
*  it was able to basically run a document. You could run a document through Transcrebus.
*  You'd get the typical kind of error rate you'd find with OCR software, maybe for
*  text that you'd get 10 years ago. So you might have a 96 to 97% accuracy rate, which is great,
*  but it does mean that three of every hundred characters are going to be wrong, right?
*  And what I found back in the spring, this is how quickly things are evolving. As we know,
*  you can take that document, take the text, put it into chat GPT. You can do it through an API,
*  or you can do it through a chat interface. And you could have chat GPT correct it, use the
*  predictive text function to basically go through and figure out, oh, no, this word was actually
*  supposed to be this. And it was really accurate. It was actually shockingly accurate how well it
*  did with that, right? Including with proper names and things like that, which are hard to predict.
*  Since then, Transcrebus has integrated AI into its model. And now since August, you've been able
*  to actually use a model that effectively, I think, it didn't really describe exactly how it works, but
*  I'm pretty sure this was happening. It's doing that in real time, right? So you're transcribing
*  the document, and then you have a large language model, which is checking the predictive text as
*  you go through, right? This opens up a whole new kind of field for historians. It'll enable us to
*  do things now that we could only kind of dream of maybe even three years ago, five years ago.
*  And so I think whereas digital history has always been kind of a side light of history,
*  I think that going forward, it's most likely that this is going to take center stage, right? Just
*  because of the possibilities that it offers. And again, just for kind of added context on this,
*  all historians for years have been taking digital images, right? So you go to an archive,
*  you bring a camera, you snap pictures, you might take 10,000 pictures in an archival trip.
*  And the big problem has been all that stuff, handwritten, textual, whatever, has been basically
*  locked in JPEGs. And what this does is unlocks a huge archive of material, right? And I suspect
*  we're going to see that being used not only by historians, but probably also used eventually to
*  train models as well, simply because it's this kind of other repository of text that isn't out
*  there. And all of it too is copyright free, right? Or most of it is anyway. So there's this whole
*  kind of synergy, I think, between what's going to happen in history, as well as the fact that
*  there's simply all of this massive material that's out there that hasn't been digitized before,
*  and what that represents as we need to feed more and more material to these large language models.
*  In terms of just kind of raw scale and just state of play right now, first of all, it's interesting
*  just to realize, in my lifetime, we didn't have a personal computer at home. So you don't have to
*  go that far back to where the standard, certainly domestic document production and not that much
*  farther back into even professional environments, you just didn't have all the individual people
*  creating stuff just weren't able to create it in a digital native format. It's amazing how
*  that's most unthinkable, but it's not that long ago. So it's certainly not just deep history that
*  this would apply to. I guess I'm at least bucketing the sort of historical records into maybe,
*  I see at least two kinds of things. One being the typeset, which presumably is easier, although
*  maybe not easy. And then the hammer and stuff, which sounds quite hard. And it's just coming
*  online with some of these transcripts and now more generalist models as you're mentioning.
*  My assumption would have been that Google Books or whatever would have effectively digitized
*  all the books. But I would imagine most of the handwritten stuff is just still kind of sitting in
*  bins or maybe has been snapped into JPEGs, but that's about it. Is that accurate or what would
*  the general state of the content be? Yeah, you're right in terms of Google Books and
*  the HathiTrust in the US as well, have digitized enormous amounts of printed material. And so this
*  is bound printed material. But what I'm talking about, what most historians tend to use the most
*  is archival material. So these are paper documents that are sitting in boxes. And it's kind of hard
*  to visualize how much of this material exists. But to give you an example, just in Canada, where
*  I'm operating out of, for the First World War alone, you're talking about if you set all of
*  the documents that were generated now stored in the archives, just in Ottawa, about the First
*  World War end to end, you have about a kilometer of records, which is about three quarters of a
*  mile. And so this is an enormous amount of material. And so none of that's been digitized
*  or some of it has been digitized, but we're talking tiny fractions of it, even all the war
*  diaries, which have been digitized, small little amount of that total. And so if you can then
*  extrapolate from there and think about the many, many, many, many miles, hundreds of miles of
*  records that exist in various archival repositories, that's what historians use. Right. So the big
*  problem is that going through that material, even if you digitize it, it's usually selective. It's
*  usually done kind of in an ad hoc way, and it's certainly not everything. And what AI opens up as
*  a possibility is going through everything eventually. Right. In the sense that, you know, in an ideal
*  world, you could, in theory, now begin to pump all of this material into a model. And for historians,
*  and this is going to be more broadly applicable in other areas too, but for historians, the big
*  problem is always processing. Right. You can't go and read a mile's worth of records in a lifetime.
*  So it's not going to happen. So you're always selective. You've got to choose where you look,
*  you've got to choose what you look at. You've got to choose how you spend your time. Right.
*  And that's why history is constantly rewritten. What we're talking about here then is at least
*  the theoretical possibility of being able to feed an infinite amount or close to an infinite amount
*  of paper into a model, which can then actually do that processing very quickly. And if you think
*  about what that opens up in terms of things that wouldn't have been feasible a few years ago
*  to do it manually and what's now feasible, or at least will be very soon, it really changes what we
*  do. That's relevant to history. But I think more broadly, if you think about the law and what
*  lawyers are already doing in terms of using models on legal documents, but the medical profession,
*  it's all part of the same thing. Right. We're scaling up what we can process and the volume
*  of material that you can go through, which allows you to be far more exacting and detailed. Right.
*  So just as, you know, a radiologist can look at a scan and detect a tumor or a lesion or something
*  like that on a scan, but you can also feed those scans into a model, which can see things that the
*  radiologist might not pick up on because there's, you know, something in the data that stands out
*  that you wouldn't necessarily notice that might be indicative of something. That's what we're talking
*  about here in all of these different fields. You feed more and more content into these models
*  and the odds are you're going to start to pick up on things you wouldn't have seen before because
*  you simply couldn't process the data. You couldn't have found the connections. We're not there yet,
*  obviously, but what you can see is, as you well know, is that the capabilities are there. It's
*  often getting to the place where you can scale them up or they become affordable and it's GPU
*  capacity and things like that. Right. So this is how it's changing what we do. And it's also,
*  I guess, worthwhile thinking about the fact you've got that textual component that's printed,
*  but then you've got this enormous amount of archival records out there that are not digitized or
*  that are not accessible through Google Books and things like that. Right. Hey, we'll continue our
*  interview in a moment after a word from our sponsors. If you're a startup founder or executive
*  running a growing business, you know that as you scale, your systems break down and the cracks
*  start to show. If this resonates with you, there are three numbers you need to know. Thirty-six
*  thousand, twenty-five and one. Thirty-six thousand. That's the number of businesses which have
*  upgraded to NetSuite by Oracle. NetSuite is the number one cloud financial system, streamline
*  accounting, financial management, inventory, HR and more. Twenty-five. NetSuite turns twenty-five
*  this year. That's twenty-five years of helping businesses do more with less, close their books
*  in days, not weeks and drive down costs. One, because your business is one of a kind, so you get
*  a customized solution for all your KPIs in one efficient system with one source of truth. Manage
*  risk, get reliable forecasts and improve margins. Everything you need all in one place. Right now,
*  download NetSuite's popular KPI checklist designed to give you consistently excellent performance,
*  absolutely free at netsuite.com slash cognitive. That's netsuite.com slash cognitive to get your
*  own KPI checklist. Netsuite.com slash cognitive. Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Omniki so much that I invested in it and I recommend you
*  use it to use Cogrev to get a 10% discount. Yeah, I was just trying to translate this with a little
*  mental math into tokens and then kind of cost. So, you know, you take a mile, 5,000, well, you know,
*  use round numbers, 5,000 feet. That is 50,000 inches. Probably could do more, but I'll say a hundred
*  pieces of paper per inch. So, 50,000, five million sheets of paper in a mile.
*  I don't know, you know, whatever called a hundred tokens, maybe 200. If it's 200 tokens,
*  probably 350 tokens a page would be my guess, but 300 and 300 words, 500 words, depending on the
*  writing. Yeah. So that gets us to basically a billion at 200. You go to a billion. So 350,
*  maybe two billion ish tokens. You said that is just the World War I archive that is in Ottawa. So,
*  yeah, I mean, it does start to get potentially quite material even on the scale of like
*  just data, you know, writ large, right? I mean, kind of for all of the use cases. I mean,
*  it's not like YouTube scale, but it's definitely pretty big and it certainly covers something that
*  YouTube is in no position to cover. It seemed like it's like a co-op on some level, but it also
*  has a commercial model. So I'm just kind of curious about that. But the pricing appeared to be
*  more than 10 cents per page, which, you know, going back to our mental math, if we're talking
*  about, what was it, 500,000 pages, right? 5 million pages, I'm losing track, but whatever,
*  some huge number of pages. Obviously, that's going to be tough on your grant budget, but maybe,
*  you know, with a three point, if we're talking about a billion tokens and it's $2 per million
*  tokens with GPT 3.5, then, you know, you're getting into like just a couple thousand dollars in theory
*  is kind of the price that we could sort of see our way to. So do I have that right in terms of
*  just kind of what it has cost? And do you think it's realistic that it seems like it's, you know,
*  going to drop now to the point where, you know, maybe your grant, your research budget actually
*  could cover sort of full processing of something on this scale? Well, is that I mean, right now,
*  I mean, it's not feasible today, right? But I mean, what we know is, is the pricing's dropping
*  constantly, right? I mean, AI or open AI is probably seems like going to open some kind or
*  announce some kind of a price drop on November 6th, right? And this is going to happen over the next
*  few years. We're just going to see it get cheaper and cheaper is what happens, right? We also got
*  to keep this in mind, right? The limiting factor before has always been you used to have to hire
*  someone to transcribe this material for you, right? And so when you got a research grant as an
*  historian at a university, and this would apply to English or whole other kind of any other kind
*  of field like that, you'd very often hire a student to come and do that transcription. Now,
*  that student would take maybe a week or two to screen to transcribe a couple dozen pages of
*  documents, right? You're paying them very often somewhere between 20 and $30 an hour.
*  Um, that's expensive. So then the 10 cents a page becomes much cheaper than the alternative,
*  which is why that pricing model looks the way that it does right now, right? But if we assume
*  that the vision capabilities of GPT-4 and whatever comes after it get better, um, and that the API
*  pricing follows in line with that, yeah, I mean, it's, it's going to get much cheaper. So I think
*  the reality for historians for context is that right now, even transcribing something through
*  Transcribus, a 10 cents a page is a tiny fraction of what it would have cost you to transcribe that
*  document with human input, not that long ago. And doing it through an API with OpenAI, once
*  that technology gets a little bit better at doing this stuff, which it will, that's going to get
*  even cheaper then, right? So again, it's one of these things where you can kind of see where this
*  is going to go with, I think, a fairly reasonable degree of certainty at the moment. Yeah, it's not
*  feasible this second, but I could say within the next few years, it will be quite feasible in order
*  to transcribe, if not, you know, that whole amount of records. Certainly you could take a big block
*  of them and, and do that relatively quickly and, and cheaply compared to what it would have cost
*  in the past. Certainly. Yeah, it's amazing. So what is the state today with GPT-4 vision,
*  if you just go drop in, you know, one of these things, you know, we don't have the API yet. I
*  think that's another good candidate for November 6th release, but we'll see. Pressure is mounting
*  on OpenAI to drop the prices because everybody's talking about it. And, you know, it's like, it's
*  going to be, if all of a sudden the prices stay the same, there, people are going to be a little
*  disappointed. But in any event, if you go take one of these historical documents today, again,
*  feel free to complicate this because I'm sure it varies depending on what era and, you know,
*  all sorts of conditions. But how does the kind of new baseline GPT-4 vision compare to
*  Transcribus head to head, just pure quality basis? Not well right now, which is interesting,
*  but it's interesting for, for why it doesn't. Right. And so right now, if you drop in a document
*  and I've tried it with modern kind of handwritten documents from say the 1950s versus
*  ones from the 18th century or whatever, it has a lot of hallucinations that were more common with
*  3.5 than they were with four, right? When you're doing textual based stuff, where it will just
*  start summarizing something versus transcribing it, right? And it'll change the language and you can
*  play around with the prompt and say, you know, you have to be exact and all these, but it,
*  it tends to go off the rails pretty quickly. Right. And when you play around, then one of the
*  things you realize is that I think there's a couple of things going on. One, I don't think it was
*  probably trained on that much old handwriting to begin with, which probably poses a bit of an issue
*  for it. It probably hasn't seen that many examples of 18th century handwriting compared to something
*  later on. So that poses an issue. But the other one is that it seems to kind of fall into these
*  troughs where it, what it wants to do is tell you about the document rather than transcribe it.
*  Right. And it does a pretty good job summarizing. So you get this weird kind of a, an output where
*  it can't transcribe a document exactly, but does a really good job telling you what's in the document,
*  which is kind of an interesting kind of a problem to have it. It clearly is able to
*  interpret what's there on some level, but getting it to actually output an exact transcription is
*  problematic. And that's kind of what I'm seeing now at the same time, depending on your use case,
*  maybe transcription isn't always necessary. We, we use, as historians, we used to think about,
*  we have to transcribe things in order to be able to use them. Right. And what I've been playing
*  around with, especially with some of these pension documents that, you know, I'm just curious to see
*  what you can do with them is very often what you want to do is ask the model, you know, I've got
*  this research question, is this document relevant to the thing I'm looking at? And if you got 12
*  million pages, you might not need to transcribe 12 million pages. You might just need it to tell you,
*  you know, here are the 2,500 pages out of here that are actually going to be useful. And it seems to
*  be better at doing that sort of thing already than transcribing. And that's certainly a very big shift
*  for how I've thought about digitization and what you do with, with digital records, right? The vision
*  capability may well short circuit the need to do some of that transcription if you're able to just
*  kind of work with these native JPEGs in that sense, right? Yeah, that's fascinating. I had occasion
*  to drop in a letter from, you know, a city official that my sister received the other day. And I did
*  notice a similar behavior where I didn't ask to transcribe this. In this case, I could read it just
*  fine. I only had one of them to deal with, but I did notice that similar behavior where, and I
*  didn't do any prompting, but just kind of by default, you know, literally just here's an image.
*  First kind of native behavior was, it appears to be a letter from, you know, whoever in this,
*  you know, township of whatever. And, you know, here's what it's about. And it was all very
*  apt. So it's pretty insightful. And I also really like your use of the word trough. Another word
*  that we've been hearing for these kinds of things is mode of behavior. But I like trough because it
*  does have a certain, you know, it evokes the topology. And then I do think of these kind of
*  paths through the language model as almost like they're circuits in some sense, but they almost
*  seem like they're like eroded, you know, through the ongoing process of training. So I like that
*  visualization quite a bit, just as an aside. Maybe you should have asked this even a little earlier,
*  but tell me a little bit more about what kinds of problems you're trying to solve, what kinds of
*  questions you're trying to answer. You know, you got these 12 million documents.
*  You ideally would like to ask a question over all of them. You can't, you know, but like, let's start
*  with what are the documents? What are the questions? You know, and how are you zeroing in,
*  you know, semi blindly today? And then you have this really kind of interesting idea of the
*  historical or the historian agent. And I kind of want to hear a little bit more about that as well.
*  So that's a lot there. But let's start with just kind of the stuff that you're actually trying to
*  to make progress on. I'll try not to get too pedantic about the history angle of it here,
*  but there are issues around any type of document you're dealing with, right? With
*  with sending it through an API or using chat GBT, because a lot of these documents are protected,
*  right? So in the case of the records that I'm using right now, we can't most of them, some of
*  them, but most of them we can't actually upload for privacy reasons because they're restricted,
*  right? And so this is where using something like a llama two model or something like that
*  is going to come in. So I've been trying to actually more play around with other documents
*  that we can actually use this way, right? In kind of a large, in a large group. But I'll give you an
*  example of just the type of thing you might want to do. So ideally, with these pension files,
*  the problem is that they're all completely non standardized. The forms change from one year to
*  another. Sometimes they're just handwritten notes. Other times are, you know, typewritten forms. And
*  it just varies all over the place, right? And so a very simple question like did individual X receive
*  a pension for disability after the first world war actually becomes fairly difficult to answer,
*  because sometimes that person might have received a pension, other times that pension might be taken
*  away for a period and then they might get it back again. And then, you know, they might have the
*  pension increased and then it might disappear and then come back again. So it becomes a very
*  difficult thing to go through on an individual level and requires a lot of time to just kind of
*  process. What you could do, though, is you can very easily ask these models to kind of answer
*  those types of questions and give you a very quick kind of summary about a case history, right? So
*  it's something similar to what you might do with medical records in that sense, right?
*  Just boil down this long, complicated series of records where there's a lot of avenues that we
*  don't want to go down and red herrings, irrelevant information, boil it down to something that's
*  relevant to this question of, you know, did this person receive a pension? And if so, tell me about
*  the dynamics of how that shift didn't change over time. That's the type of thing which you could do
*  right now very easily with this. If you were able to, you know, feed through an API a series of
*  these images. And that's something I've tried with some of the records we've redacted that we can
*  actually do is if you put them into GPT-4V, it does actually a pretty good job of looking at the
*  record and going, yeah, you know, here's the summary. And you do kind of, it's more like kind
*  of what it was like in the winter with it, I find, where you have to kind of pet it a little bit
*  more and tell it, you know, okay, you can do this, don't worry. Like you can, I know you think you
*  can't read this thing, but you can actually try and you'll be pretty good at it. And then it will
*  try again, right? And so it's odd kind of going back to that, which is behavior you see less of
*  with GPT-4 normally, right? What I've been really working on though lately is a completely
*  different project with my research partner, Leigh Ann Letty, and we've been looking at trying to do
*  fur trade records, right? And this came out of a whole other series of things that I became
*  interested in during the pandemic for other irrelevant reasons, but I became very interested
*  in the fur trade. And it's another kind of an area where you have this interesting combination
*  of records. You've got handwritten journals from fur trade posts, you have a series of fur trade
*  contracts. And one of the big problems that historians have had is how do you take somebody
*  from a fur trade contract that you have, and you know that they signed this in Montreal say in 1780,
*  and then find out what they did through all these handwritten records, through thousands and
*  thousands of pages of handwritten records, how do you find that individual, right? It's hard to do,
*  you have to manually go through and do this. And so what we've been trying to do is create an agent
*  that will effectively do this, take an individual, find identifying markers based on demographic
*  records that are in Quebec, and then use that information to then find that individual
*  through fur trade records, and be able to basically follow them through and do a life history.
*  And it's an interesting process, because what it involves from a training perspective is trying to
*  teach the model historical language, get around some of the safeguards that are there, because
*  again, there's a lot of documents that contain racist material, because they're historical
*  documents. And getting GPT-4 to think through that in a way that's useful then becomes a bit
*  of a challenge, right? You also end up with this kind of process of trying to find the documents
*  you need in order to feed them to the model. And it sounds pretty straightforward, right? Except
*  again, like so many of these problems, it's not when you drill down to it. So if you have an
*  individual, and I've come up with a few of these test cases that I've been using that are just edge
*  cases that are not uncommon edge cases, but are good ones for this. And you might have an individual,
*  and you want to ask it as an historian, open it a question about, tell me about Ferdinand Wenzel's
*  family. And Wenzel's kind of a mid-range fur trade figure. And he writes a number of post journals,
*  and he writes about his family, but he does it in very oblique ways. So he'll refer to his
*  indigenous partner as being my girl. He'll refer to his son as being my boy or the boy.
*  And it's often he writes in these kind of German, so he's writing in English, and he's writing often
*  kind of backwards, grammatically backwards sentences. And so, or he's Norwegian, I guess,
*  but there's still kind of grammatically backwards in that sense. And what you end up with at the end
*  is a real difficult process of not so much getting the AI model to be able to trace this guy through
*  and write the biography, but be able to feed it the records that it needs to do that. And I've
*  tried all the various techniques, right, which you can do embeddings and try semantic search
*  approach with this, right? That works reasonably well, except you very often miss some of the most
*  important documents because the pre-trained embeddings out there, like Attitude and various
*  hugging face, sentence transformer models, they won't recognize my girl as necessarily being
*  your wife, right? So then that doesn't show up. And if you simply have a question like,
*  tell me about Ferdinand Wenzel's family, that doesn't work very well in retrieving a lot of
*  the relevant documents either, right? Because there's not enough information in the prompt to
*  do that. I've tried the Hyde approach, right, which is you try and generate hypothetical
*  versions of these documents. And then again, you get some interesting behavior from the language
*  model. It won't write in the way that you need to historically to match the example to examples in
*  the database, right? And again, this has been kind of a funny process where if you tell it,
*  you know, to be succinct, to be short and to be choppy, and here's five examples of how to write
*  a diary entry like a fur trader, it almost always wants to write some kind of a flowery example in
*  which, you know, the fur trader pauses to reflect on the beauty of the morning or something like
*  that, right? And no matter how many times you tell it not to do that, it still wants to do that on
*  some level. And nobody ever wrote like that, right? And so this is another kind of a problem with
*  the documents don't really look the way that GPT-4 is expecting them to look, right? You might have a
*  two sentence entry in a diary that, you know, says fine weather this morning. My man died when a tree
*  fell on him this afternoon and we traded five kegs of rum later on in the afternoon, right? And so,
*  you know, the model is not thinking like that. It will want to know more about the death of that
*  individual and then become very reflective about, you know, how it feels about this. And that's just
*  not how these historical documents work. So there's that issue. You can certainly fine tune a model
*  that does a better job of that, but then you get into this problem of you end up fine tuning a
*  whole series of models, kind of a mixture of experts almost approach, right? Where you have
*  to fine tune models on different things. You've got to have a fine tuned embeddings model. You
*  have to have a fine tuned model to create the examples for semantic search, right? And then
*  you have to fine tune a model to actually determine what's relevant. GPT-4 does a fairly
*  good job at determining is this document relevant to that question? But again, it stumbles on
*  historical language very often. It stumbles on when it finds something in the document that
*  it perceives as being racist or as often racist or problematic for whatever reason.
*  It will also look at that and say, well, this isn't relevant sometimes, right? And so then
*  you got to fine tune a model to teach it that no, no, this is relevant to that, right?
*  And that's just for the semantic search approach. The other approach, of course,
*  is to use keywords and this sort of thing. But then you get into classification. You run the
*  exact same types of problems that I talked about a second ago. And as you start to try and classify
*  material historically, the model has to learn these things are relevant to this, right? And
*  there's a whole vocabulary that comes into it that is just not in the training data. And again,
*  it kind of presents some interesting test cases, which I often go down these rabbit
*  holes trying to figure out because you might have a term like Verang, for example,
*  which if you ask GPT-4 about it, it'll say it'll come up with a hallucinated response for what it
*  is. And then if you say, you're sure that's what it is, it'll say, no, I don't know what it is.
*  It's not a common English term. And it's not. It basically means the wooden ribbing of a birch
*  bark canoe. All right. Fairly specific, right? But you have to then train a model to know that,
*  or at least to recognize how this works in order to get it to properly classify things with keywords.
*  And once you do that, you can begin to do some keyword retrieval, combine it with semantic
*  search, and then you get your document retrieval. But you have to kind of ladder that into then
*  another model in which you're also feeding that up to try and get the model and some kind of
*  overarching model to pick and choose between approaches to be able to trace that individual
*  you identified back in Montreal through these documents, determine if they're relevant, and
*  then come out with a biography at the end. Now, if this works properly, you can then do take a
*  database like there's a Voyager's contracts database, which Nicole St. Augustine and some
*  others out of University of Ottawa did. They have 35,000 individuals in there. You could very quickly,
*  if you get this working, run through all 35,000 individuals and produce, you know, many biographies
*  of each of them and then begin to think about, oh, what are patterns we're seeing here we weren't
*  aware of before, right? And the big limiting factor now is context limits in terms of the
*  models you're dealing with as well as cost, right? Again, the cost of those recursive API calls begin
*  to add up very quickly. And so again, it's one of those things where what we know is the context
*  windows, I think, will continue to get larger and larger, at least I'm assuming that. And the cost
*  of those API calls will probably come down. And I mean, I've heard the rumors too, that maybe OpenAI
*  is going to release some kind of an agent kind of built an agent approach or something like that.
*  But again, this is stuff that you can see now, this is where it's going to go probably. And what's
*  going to be possible is just we're not quite there yet in making it feasible. But you can imagine
*  taking this very pedantic fur trade example, and then scaling that up not only to historical
*  applications to but to a whole variety of different things, right. And it raises issues about doing
*  this for living people, right, the ethics of being able to take social media data and trace
*  people, right. So there's a whole series of different things that come out of this, this
*  type of approach, which, again, is very new. This isn't something we could even talked about a year
*  ago in history. That's how new this is, right? That's really cool. I mean, you're you're
*  definitely doing all the, you know, all the latest and greatest stuff, which I think is
*  super impressive. So just one very small question on the comment that you made about not being
*  able to use some of the individual records for privacy reasons. My understanding of like the
*  OpenAI API Terms of Service is that they a promise not to train any models on your data and also
*  be promised to delete it all pretty quickly. I've, you know, in the past, I've kind of said,
*  Hey, why don't you guys have more like visibility into what I did in the API? They're like, yeah,
*  because we don't really want to save that stuff. Because, you know, people don't really want us to
*  have it. And so I guess that's not good enough for the Canadian government. Like what we think
*  is sort of the future of that debate. Is there anything they could do that would, you know,
*  would make it okay to use their API? It's hard to imagine, right? That this is, again, we're not
*  even a year out from GBT 3.5 coming out, right? So, I mean, this is all brand new. So when these
*  contracts that I had or agreements that I had with Veterans Affairs in Canada were negotiated,
*  you know, back in 2018, this wasn't even on the horizon, right? And so their concern is,
*  you know, we're not allowed to transmit the data effectively over the internet. We're thinking
*  email and stuff like that at the time. We're not future proofing this for sending it to an API,
*  which we didn't think would exist, right? So I think going forward, that's the type of thing that
*  that is going to become a huge point of negotiation for historians. But I think for
*  researchers more broadly, right? Is, can you send this? What type of material can you send to an API?
*  And so I agree. I mean, I think that OpenAI doesn't retain the material. And they're very
*  transparent about that. And as I try, people are often skeptical of that. And I say, well,
*  you know, if they're lying, they're going to get sued. And so I don't think they're lying, right?
*  This is obviously, I think you can trust people on these things, when they have them in the terms
*  of service. But I think it's building the confidence amongst researchers, as well as amongst
*  agencies that hold documents. This will be true for hospitals as well, right?
*  About what you can do with these types of records and what you can send them. There's also
*  legislation often that governs this. So for example, in Canada, material that contains
*  identifiable information for an individual that's owned by the government, an individual who's been
*  deceased for less than 20 years falls under the Privacy Act. And you can't actually transmit that.
*  So it doesn't matter if OpenAI actually retains that or not. You sign a researcher's agreement
*  saying, I won't transmit this in exchange for getting access to it, right? I think that kind
*  of thing will have to change, or at least we'll have to update those types of legislative documents
*  to deal with this world. And they'll either look like more restrictive in the sense that you
*  can't do this, or they'll be less restrictive or something in between. But they'll have to be
*  updated, right? I think that that's an important kind of component of all of this. I think the
*  other thing with data in general and data privacy is that for people who are using this, I think
*  as you said, you've used it, you're fairly confident in how it works. The vast, vast majority of people
*  are still at the stage of encountering CHATGBT for the first time. And certainly my colleagues
*  at university are kind of at that stage. And getting over the hump of them trying to explain
*  that, yes, there are ways that you can send this material that is more secure. And I mean,
*  that itself is a learning process, right? Because there's a huge knowledge, like huge learning curve
*  between, you know, wow, CHATGBT can write a poem in the style of Bob Dylan, so you can actually use
*  this to do something very constructive, and I'm going to trust it with my data. And I think
*  that gap is only growing as these models get more and more capable. And because everything
*  is evolving so quickly, I think in an unprecedented way, we're witnessing that
*  that gap just get larger and larger. So there's a trust gap and there's a legislative gap. And I
*  think that there's also just kind of the fact that people like me have research agreements we
*  negotiated before these things were even on the event horizon, right?
*  Yeah, a lot of dimensions to the capabilities overhang. And that's honestly one of the big
*  motivations I have for doing this show is to try to help close the capability overhang gap. You know,
*  I often say I'm an adoption accelerationist, not necessarily a hyperscaling accelerationist,
*  but to use what we have and to make the most of it and to understand what we have,
*  seems like we're currently still not even caught up to the pace of progress just in terms of
*  understanding and using what already is online and available. So that's an interesting and likely
*  historical challenge. I do want to cover your experience in experimenting with
*  GPTs and education and also kind of turn to the lessons from history. Before doing that, just to
*  kind of finish the discussion on the technical stuff and all this experimentation that you've
*  done on the agent, I think we're fairly kindred spirits, it seems, because we have both been
*  willing to work pretty hard to get AI to do something that in the grand scheme of the world
*  is fairly narrow, often when it was still kind of sucky at it. And so I'd love to hear what did the
*  3.5 fine tuning unlock and kind of what's the current state of play? And then also, are we
*  getting to the point now where it's actually adding value or are you still in the kind of
*  promise phase where you still need to turn one more corner before you'll actually be
*  accelerating the actual historical work that this is all geared toward?
*  Yeah, that's a great question. And let me kind of deal with the end part of it first. I mean,
*  it's such an iterative process, as you know, and I think most people listening to this probably
*  are aware as well, where it's a lot of trial and error, it's a lot of frustration. There are days
*  where I'm like, yeah, this model is not going to be able to do this. And then you have that moment
*  where suddenly you figure out, you know, if only I do this, you go great, this is now going to work.
*  And then you have the moments where the thing you've been working on for three months
*  suddenly gets released through an update in OpenAI. And now the model can actually do it. Or,
*  you know, something comes out and you're like, oh, this is, you know, this is really kind of
*  fighting with it to do this before or something like that. Right. So there's that kind of aspect
*  to it. What I've found is that fine tuning since it was released in August, I use the OpenAI API
*  the most for this in Canada. We don't actually have access to Claude, which is kind of a,
*  I'd like to try it with a hundred thousand context window. But
*  I think that just changed this week, by the way. Did it? Oh, I didn't even know that. Look at that.
*  90 some new countries. Vivian, shout out to Vivian, producer of our show is in Canada and had been,
*  we use Claude too, specifically for the timestamp transcripts of, of the show, like the outline,
*  right? So dump in a transcript and say, you know, give me a format of the discussion topics.
*  She couldn't do that from Canada until this week. She's finally able to use it. So I think you now
*  should have access. That's what I'll be doing this afternoon. But I think what's, what's interesting
*  is that since the fine tuning capability was released at the end of August, I've seen a lot
*  of the problems that I thought were going to be farther off in the horizon of solving become
*  solvable. Right. Because again, all those things that describe where you have to have essentially
*  a different kind of model to do all these things that wasn't possible before August.
*  And so, you know, we've we talked about this over email, but I think that the fascinating problem
*  was, it's what I find so interesting about this is how you get that information into the model.
*  Right. And I think there's some good information out there on fine tuning, but it's also an area
*  where I think that there's the least kind of good hard information on how to do it properly.
*  While there's also obviously a lot of misconceptions, right, the idea that you can use it.
*  You know, some people are you can use this to impart new knowledge, right? It doesn't really
*  do that, but it kind of does not really. And it's just about behavior. But yeah, behavior is also
*  a form of knowledge. Right. So there's this kind of gray area that's still in there, at least in my
*  mind. And so what I was originally trying to do is, you know, for one fine tuning example, I use I was
*  trying to teach it how to determine if a document was relevant or not, and use that kind of classic
*  approach where you give it three examples of the same document, you change a word in each one,
*  right? Where in the first document, if I'm trying to teach it that I'm asking you about Wenzel's
*  wife, right, and his family, and the document describes Wenzel saying, you know, today my girl
*  and I went somewhere in a canoe. Well, you have to teach it that my girl means wife. And so you do
*  that by in the first one saying it's relevant, right. And then in the second one, you take my
*  girl out, you put it with wife and you say relevant. And the third one, you say my dog and you say
*  irrelevant. Right. And it learns that these are different approaches that way. Right. And
*  it's an iterative approach again, that in that sense, that doesn't work quite so well when you're
*  dealing with something much more complicated, like keywords, right, trying to read a fairly long text,
*  break it into thematic sections, assign keywords, and then basically go from there. And what is what
*  is finding is, you know, my first run throughs with the the native like, basic models, my corpus
*  of documents I'm working with as a test here is about 650,000 words, which is, you know, pretty
*  significant, but it's not giant, right. In that sense. But in categorizing that you might come out
*  with 11,000 keywords, right. Just by using GPT-4 and saying assign keywords to this. And some many
*  of those keywords are overlapping and you can go through this kind of process, which I tried of,
*  you know, consolidating the keywords, it becomes very time consuming and it just doesn't eventually
*  work. Right. What do you effectively need is you need to be able to say when a user asks this
*  question, choose from this bank of keywords, keywords that are going to likely be relevant
*  to that question and then retrieve all the documents that contain those keywords in the
*  keyword section. Right. And so what I then tried to do was I tried different approaches of giving
*  it a bank of the keywords. Here are the 300 keywords you're going to use. Right. Well, that
*  doesn't really work because, you know, every once in a while GPT-4 doesn't stick to it and will pull
*  out some other random term. Right. It will also miss things. So then you try and put in these rules.
*  If this happens, always apply this keyword. If that happens, always apply that keyword. And then
*  you get these prompts that are 2000 tokens long. Right. And then you put your document into it and
*  it's hugely expensive. And so I heard on your show, actually a little while ago, you talking
*  about using chain of thought as a way of doing this. And I immediately thought, well, this would
*  be a really interesting approach to take. Right. Because I've been basically trying to show it just
*  before this document results in these keywords. Right. And changing this document a little bit
*  changes these keywords. And that just wasn't working. And what's fascinating to me, and I
*  think it's a really insightful kind of way of doing it. And I've been looking around, I haven't
*  seen that much written on it either, is that it's teaching the model of behavior. Right. So that
*  what you do is if you prompt it properly, you can basically say, okay, first break this document up
*  in thematic sections, then write a description of the theme below that, because you're teaching it
*  to think through that process. And then based on those two things, write a series of keywords,
*  do this sequentially through the document, working step by step. And then at the end,
*  reread everything. If you missed anything from this list of keywords, put it in and then have a
*  collate everything into a final list of keywords at the end. Right. And using that approach,
*  it worked quite well. I then generated a whole series of synthetic data about, well, it wasn't
*  fully synthetic, but you basically, the responses are from GPT-4 doing this for about 400 examples.
*  And then you use that as your training material. And that process has been really interesting,
*  right? Because you basically end up with this corpus of training material at the end, which
*  is about as good as GPT-4 gets on this. If you fine tune 3.5 on that, when 3.5,
*  if you just run the native model on say a test of a hundred examples, which is what I've been doing,
*  and you generate a list of ideal keywords you want to have come out at the end,
*  it gets maybe 50 or 60% of them. And GPT-4 will get maybe 70%, 72% accuracy against a human
*  at the end. If you fine tune 3.5, just on GPT-4's responses, you get about the same
*  accuracy as GPT-4. But if you then go through and you actually work through all of those fine
*  tuned examples, those examples for fine tuning, and you edit them and you correct them and you
*  fix all the mistakes and then you figure out, oh, no, I need more examples of this and less of that
*  and you really dig down your data set, you can get that number with a fine tuned 3.5 model up to
*  about 85%, which is significantly better than GPT-4. And I find that itself really fascinating
*  in the sense that that process of teaching 3.5 to think through sequentially and to do it the same
*  way every time results in that significant a change from GPT-4. And it gets it to the point
*  where effectively the model you end up with the fine tuned model at the end you end up using
*  is usable, right? In the sense that its results are at that point about as good as a human,
*  right? I mean, I've had a few students try to do this as well and just to see like, okay,
*  I have my list of ideal keywords, but if I hand this off to a student, like, what am I going to
*  get back? And it's in the same range, right? 78 to 80 some percent. And then you kind of go, okay,
*  this is actually at the top end of what humans can do with this because, you know, people are
*  going to have different opinions about what keyword fits as well and stuff like that. To me,
*  that's been the most fascinating part of this process. And I do think it all comes down to,
*  again, in fine tuning, what we're really doing is teaching behavior. And so as a result, if you can
*  teach it to think through that behavior and articulate that behavior, instead of just showing
*  it the ideal outcome, that seems to be a far more effective approach. And that to me is really
*  interesting. I've gone back now and I'm working on trying to improve those earlier models I did
*  looking at trying to determine relevance through the exact same process, right? And it's the same
*  thing where you're finding accuracy and success rates are increasing 20%. And that's really
*  important when you're dealing with something that's 50-50, like relevant, irrelevant, right?
*  It's now getting it right almost all the time. And that's really what you want to see on a model
*  that's like that. So to me, that's been a fascinating kind of a learning curve. And again,
*  we've gone from August where you couldn't this technology wasn't there to make this work to
*  now with the fine-tune model where yet you can begin to actually deploy this and to use it to
*  do something useful. I think when I first started looking at this back a year ago, I thought we were
*  probably two or three years away from that point when in reality we were less than a year, which
*  just tells you again, the pace at which this is moving. So ultimately, it seems like you've
*  kind of just crossed into the territory of like now you're actually accelerating
*  the object level work for the first time. Well, congratulations. That's a big threshold. I'm a big
*  constantly harp on the importance of threshold effects in AI where it's like,
*  you know, it's all kind of just noise until it works. And then when it works, you know, things
*  really are kind of qualitatively different. And that's true in terms of model capabilities and
*  individual workflows. It just kind of seems to be a huge theme. So you've since you've crossed a
*  big one there. I think so. Yeah. Well, yeah, it's awesome. And I do. Yeah, it's funny that
*  I don't know if I have anything else really too much to add on the fine tuning point. It sounds
*  like you've got a really good read on it and probably better than me. Honestly, my challenge
*  is probably a little easier than yours. Certainly more in the wheelhouse of what the, you know,
*  the models are met. I think they're intended to do everything, but these sort of, you know,
*  highly available use cases, you know, we're more in line with those. So it's cool to see that this
*  is working in other areas as well. Two kind of quick thoughts, one on the yes, no. I like to
*  band my kind of classifications out of this stuff in usually like a five band and also typically
*  try to label those. You could say like one to five, but I don't trust it to kind of translate
*  to numbers as well. So I usually go like, you know, in your case, it would be like highly
*  relevant, you know, somewhat relevant, you know, whatever, neither, you know, whatever, you got
*  to obviously come up with your own labels. How do you think about two versus say five? I feel like
*  I get better results from five because it's less like right and wrong and more kind of,
*  you know, kind of think of it as like, now I can kind of skim off the top. Like now I can only,
*  you know, I can look at the ones that were all labeled highly relevant, you know, and then maybe
*  go to the next tier if I need to, as opposed to a yes, no. Yeah, no, and that's a really good point.
*  And so when I was first trying that out, right, I mean, what I was finding when you're using just
*  four with without an untuned model was that I was using basically what you were saying, right, very
*  relevant, somewhat relevant, like unlikely to be relevant and then irrelevant, right. Or something
*  like that. And what I was finding with that was that the model very often wanted to say something
*  was likely relevant. And you could play with the language and try and change the actual semantics
*  of that to make that a less desirable input. But especially in historical documents, it seemed to
*  be really tentative about saying something was relevant. So as a result, if you wanted to take,
*  you know, if you got 500 results from your semantic search, and you wanted to take the ones that were,
*  you know, in levels three, four and five of those, you would probably have 75% of them. And most of
*  them would probably not be relevant at all. And so the fine tune model, though, seems to be much
*  better than I think that that's exactly what I'm actually trying to do right now, which is go back
*  to that first approach, and to try and fine tune a model that is much better at making that
*  determination. Because what I originally found with GPT-4 was that, again, when you, it worked
*  better to say irrelevant or not to give it that choice, it would, you were more likely to get the
*  relevant results by doing that, even though you might lose one or two ones to being irrelevant.
*  But you wouldn't get, you know, the 75% of examples that just weren't there at all, right. And so I
*  think that, again, to try and use that chain of thought, fine tuning process, I think that will
*  be far more effective. That's my hypothesis anyways, at getting these models to think through
*  what you're describing. But yeah, I think that that's, again, it comes down to teaching a
*  behaviour, right, and thinking with fine tuning about, you know, teaching in this behavioural kind
*  of way. And as you say, you know, there's different use cases, mine is very specific. And I think
*  that's what's fascinating about this is that I still have, I'm always amazed that there's these
*  things out there, you think this won't be able to do that. This is way too specific. This is way too
*  kind of niche and isn't going to work. And this model wasn't designed to do that. And then all of
*  a sudden, it can, right. I ran into one of these emerging capabilities the other day, which is
*  really interesting, which is like an example of this thing where you don't expect it to do this.
*  So we were dealing with indigenous names from these records, right. And we're trying to trace
*  indigenous people through and their name, indigenous people's names are spelled phonetically very often
*  in these documents. And they're very different from one place to another, one document to another.
*  And I actually tried to get the model then to take some names and say to come up with training
*  examples, spell this out phonetically. And the model started doing that. And what's interesting
*  is it didn't use the type of phonetics you'd find in a book, right. It was actually making the sounds
*  and writing out these names phonetically. And again, you kind of pause and you think that's
*  really an odd thing, right. In the sense that it doesn't know, it shouldn't know what these things
*  sound like. And yet it's not taking a direct kind of a phonetic approach where you would be using
*  the type of language you'd find in books that it might have learned. And so again, there's these
*  kind of, that was something I thought we'd run into as a wall with this as well with names that
*  were largely phonetic that it wouldn't have run into. But again, it seems to be able to think in
*  phonetics and recognize phonetics, which I'm still kind of processing how that would work and
*  how that training process would have worked, that it could actually think in terms of sounds and be
*  able to translate words into sounds and then back from sounds into words without using a whisper
*  approach. So, but that's an example again of something I thought would be not a possibility,
*  which then you're like, oh, it can actually do this while that opens up this, right. So it's
*  it's a, it's fascinating to watch how this evolves so quickly, I guess.
*  Yeah. Funny enough, one of the things that I've worked on might actually be related to that,
*  which is for voiceover script writing, often the talent needs the proper noun in, you know, kind of
*  not even like formal phonetic representation, but just sort of, you know, whatever's going to make
*  it, you know, least obvious or least likely for them to make a mistake in the pronunciation,
*  because that's like the probably the number one thing that ends up cycling voiceover work is you
*  say the name wrong, they can't write it, you know, they're just, it's just not going to work. So
*  you're back in the studio. So they really want to, you know, they really want to see something that
*  is super intuitive and super clear for how they're supposed to say it. And we've tinkered with that
*  a bit. And, you know, it's been kind of the object of some of our fine tuning as well. We're also
*  using that AI voice in our case sometimes. So it's like, we've kind of two levels of
*  idiosyncrasy, you know, the names can be weird and also the AI way that it pronounces can be weird.
*  If I had to guess like what sort of data, you know, it might've seen that is that may allow it to
*  kind of generalize to the historical version of that. There's at least something like that. It's
*  in the marketing realm that, you know, is very much kind of likely to be, you know, in the training
*  data. Let me give you one thing on Claws. You're going to spend the afternoon on that and let's
*  do the education and the, you know, the big picture lessons from history. The Clawed 100K,
*  I don't know where, I don't know, I wouldn't, of course, these things are never like super sharp
*  cutoffs, but in my experience, if I take a three hour podcast transcript, and that typically will
*  fit roughly speaking into the a hundred thousand, drop the whole thing in and ask it to do that
*  timestamp topic outline, like we mentioned earlier, it basically totally fails. Massive
*  hallucination, totally wrong. Up to about 90 minutes, it seems to be very good. So I don't
*  exactly know, you know, I haven't systematically explored, I've only done so many episodes and
*  certainly only so many three hour episodes, but you know, last where I've kind of come to for the
*  moment is it seems to be very reliable up to at least about half of the context window. So if I
*  do have a full a hundred thousand, I'll usually chop it into two and then just get dramatically
*  better results. So let me know what you find in that regard or, you know, watch out for that.
*  Something about hitting the upper end of, you know, what it can handle still sometimes takes it
*  in a weird direction, but you can still be, you know, well above like 32K and also a lot cheaper,
*  right? Compared to 32K, you're talking like, I don't know, whatever, it's maybe a sixth of the
*  cost. So it's a significant savings and can go significantly longer, but just not all the way I've
*  found to kind of, you know, the full published limit. So see what you find. Okay. So then let's
*  talk about education. So this has been something you've been kind of writing and blogging and
*  experimenting with, you know, much has been made and said of, you know, homework will never be the
*  same and you can't, you know, essays won't work. I think to your credit, you went out and just,
*  you know, looked at that where the rubber hits the road and gave students some interesting options
*  to try things, you know, with and without using AI and, you know, try to see how much it helped them.
*  Tell us what you've learned in, you know, kind of first two semesters of bringing AI to the classroom.
*  Well, I think most people in social sciences and humanities are still very much at worried about
*  plagiarism with this, right? And it does fundamentally change the types of assignments
*  you can offer in higher education. Because yeah, if you're offering, if you're offering a course
*  where the majority of your grading is going to come from short answer kind of responses that you
*  let students do at home, I mean, yeah, Chachi BT does a pretty good job at those, right? I think
*  what it does is it forces a lot of people to rethink what exactly it is that we're doing and
*  what we're trying to teach people. To me, I think we're probably heading into a world in which
*  the students who are starting today in university and college when they graduate,
*  the odds that they're going to be working in jobs where they are not using these tools are pretty
*  slim, right? Because they do speed things up. So I think, to me, the goal is to try and get students
*  to learn to use it effectively. And that's a motivational kind of thing more than anything
*  else, right? Because a lot of students, from my experience, come to it and they bounce off it
*  because, you know, it doesn't just do the thing for them immediately, right? Whereas if you can
*  motivate people to learn that what you can actually do, even through a chat window or something like
*  that, because that's the most basic version of this, right? Just using Chachi BT is that you can
*  actually use it to kind of help them level up their writing. So if you're a student who really
*  struggles to get your good thoughts across in a cogent, coherent way that is stylistically the way
*  that your professor wants to see it or whatever, Chachi BT is a pretty good job, right? Of obviously
*  helping you edit things. And I try and explain to people that in that scenario, if you give it a
*  paragraph and you try and say, make this more, you know, coherent or flow better, whatever, it doesn't
*  tend to even change your ideas. It's basically like having somebody be a writing coach or having
*  your mother or something like that, you know, help you edit your paper or a friend or whatever.
*  So there's that kind of level, right? And I think that the biggest problem is again, motivating
*  students to do that. And it's like anything with AI, right? If you become interested in it and you're
*  willing to try out and play around with it, there are benefits you're going to get from it immediately.
*  Other ones are things that we can see are going to come online in the next few years that aren't
*  there yet. There's a lot of promise there for students who are kind of struggling to get from
*  that kind of C range into that B and A range to simply help them get there with editing and with
*  just sometimes even understanding the material, right? I mean, you can, if you're having trouble
*  understanding a concept, as I tell people, if you're teaching math and you get tired of explaining
*  to a student why this certain concept works, or, you know, how this thing, this concept they need
*  to know, well, Chatchi BT will explain it nicely to the student until eventually they do understand
*  it or, you know, choose to not engage anymore, right? And I think that there are those types
*  of things using this as tutors and things like that, that we can start to do. But that's not
*  really being integrated yet in a systematic way in higher education. I think we're seeing people
*  talk about it. We're seeing the promise of this coming. We're seeing some companies begin to offer
*  some of these services, but like a lot of these early kind of AI services, they're, you know,
*  sometimes kind of wonky. Sometimes they work, sometimes they don't. And the expense is really
*  prohibitive for universities right now, right? I mean, doing it on a one-off student has a
*  Chatchi BT subscription, they're going to go use that. That's one thing. Trying to make this
*  systematically available to people, that's going to be much more expensive. And I think we're really
*  going to see things shift in academia when you begin to see it roll out in office in a way that
*  is available kind of more broadly, right? Copilot available in office. That's when things will change
*  and more people are just going to get exposed to it. And as a result, I think universities are in
*  this holding pattern right now of trying to avoid the issue oftentimes more than anything else. And
*  that's going to bring about a change where we're going to have to decide what we do with it and
*  how, right? The cost thing always kind of blows my mind. I mean, not to say it's insignificant, but
*  I remember when I paid for textbooks, you know, when I was in school and I'm like, okay, $20
*  Chatchi BT per month, you know, for the best available thing in the game right now.
*  You know, that's basically what one textbook would typically cost me. And so, you know,
*  for two textbooks per year, you know, one, one text, one cost, you know, would cost one textbook
*  per semester, you can basically, you know, have revolutionary technology in your pocket.
*  And yet, you know, it's deemed too expensive. Like, that must just be, I mean, that's got to
*  ultimately just be lack of appreciation for what it's good for, right? I mean, it's the budget
*  will shift, I think is that. Oh, yeah. And I mean, as I try and tell people, I mean,
*  that's a Netflix subscription, right? I mean, it's not, this is not in the grand scheme of things,
*  the biggest expense university students you can have by far, right? So yeah, I think it's a red
*  herring. But I think the larger cost is for institutions adopting it when you're doing
*  it, when you're talking about thousands of employees, right? And what often institutions
*  do is they will buy a piece of software for everybody, including all students. So if you
*  have an institution with 30,000 students, and you're going to have to make a decision,
*  are you going to buy the copilot version of office enterprise at $30 a month per person?
*  That's then where the expense gets, you know, prohibited for the institution,
*  an individual level, it's not. And so institutions are very concerned about some students who are
*  going to have it and other students who won't and these types of things, right? So I think there is
*  that kind of red herring cost of, oh, it's expensive on an individual level. And I agree,
*  it's not not in terms of the grander scheme of things and the people pay for it university.
*  But in terms of institutional adoption, it does actually become quite expensive if you look at
*  some of the pricing schemes that are out there right now, if you really wanted to dive into this.
*  And a lot of the applications that are going to come out that are going to be the most useful
*  for AI in the next few years, I think, require that institutional adoption. That's kind of,
*  I think, where we haven't gotten over that hump yet, right?
*  Yeah, it's again, the capabilities overhang, you know, by the time we get there, we're going
*  to have GPT-5 and then it's going to be like, you know, a whole new set of questions.
*  Two thoughts here. So you have written a bit about kind of what sort of assignments are good
*  assignments today. And I'd love to hear that, you know, riff and then also,
*  you know, how long do you think that that lasts? Like, it seems like we're on this trajectory now
*  where, you know, as you said, I think in a recent blog post, like, it's really good at five to
*  750 word essays. If you sign those, you're kind of, you know, playing right into the,
*  I can just have CHPT do this wheelhouse. If you sign something, you know, more expensive, then
*  it doesn't really do that as well. So at a minimum, I mean, I'm starting to give you a
*  riff for you based on the blog. So I should shut up and just let you do it. But then I do wonder,
*  like, we've come pretty far, pretty fast. It seems like we're headed to like ability to do
*  4,000 word essays, you know, pretty soon too, right? Yeah. And so, I mean, I think there's
*  two things going on. You talk about the capability overhang, right? I mean, well,
*  the reality is a lot of people who are teaching in university are still encountering AI for the
*  first time. The number of meetings, I mean, I do a number of these presentations about just what AI
*  is, because like, this is something I get asked to do around the university. And the number of
*  people who have never actually logged in and tried it out is still astonishing to me, right?
*  And I think that that's pretty common. I'm kind of a macro level still. And so you have a lot of
*  fear. And I think right now, yeah, if you're worried about AI, you haven't encountered it yet,
*  there are ways around it. You can do longer assignments. AI will not be as good at those.
*  That will most definitely change, as you say. Right now, it's not great at doing citations,
*  even GBT4. If you require certain types of citations, it does better than others.
*  But yeah, that's going to get better as well. And there's lots of programs that are out there too,
*  that are doing this for students now as well, Cactus and things like that, right?
*  I think that's going to change going forward. That's kind of this idea that there are chat GBT
*  proof type assignments is kind of a holding action for people who still are needing to kind
*  of experience this and figure out what they're going to do with it and are really nervous about
*  it in the meantime, right? And which is the conversation you're seeing an awful lot in
*  academia about this at the moment, especially in the social sciences and humanities.
*  That's going to evolve, right? I think what's going to happen is we're very soon going to
*  start to develop assignments that simply use chat GBT or whatever the version is that is like a tool.
*  There was a time when you one would take a course to learn to use a word processor.
*  That time is kind of passed. I think most people just learn that process through osmosis.
*  And that's going to be this right. And, you know, there was a time too, before I went to university,
*  that spelling and grammar and things like that were, you know, on an English essay, that might
*  be 20% of your grade. Well, with spellcheck, that became less important, right? Expressing
*  yourself grammatically in a grammatically correct way with correct spelling was still important.
*  But you didn't tend to assign grade points for that anymore in the same way as you used to. And
*  we're going to see the same thing evolve. I think the future of this is learning to write quickly
*  and effectively with AI in a way that kind of levels up your ability to process large amounts
*  of information. The tricky thing is I think it also scales up expectations, right? That
*  what I've seen happen is that what AI is able to do with an assignment is probably going to become
*  the minimum, right? If you think about the way that this is probably going to play out in the
*  job market, if you have someone who is unable to achieve kind of the level of GPT 3.5 on a given
*  task, and that task is doable in that job, it's unlikely that that person will be successful in
*  that job. And I think that that's kind of the lesson that I keep going back to, which is that
*  what we need to do is teach people to use this in such a way that they exceed the baseline level of
*  the model, right? That's going to be difficult. It's not going to be possible for everyone,
*  just in the same way as not everybody gets an A today. And that's kind of just how things work,
*  right? But that's kind of the real trick is figuring out a way to do that. And I think a
*  lot of that comes with experimenting and teaching students to kind of be open to new ideas and new
*  things, to really digging into this and playing with it and learning how to do that. And we're
*  still doing that again, because it's only been around for a few months, right? So teaching
*  something that you're still kind of learning yourself is not always the easiest thing to do.
*  And I think there's going to be this period in education where we're going to be adapting.
*  That's going to be sped up as certainly the various tech companies out there that produce
*  educational software start releasing out of the box solutions to some of these things and tools
*  that are going to be used to kind of help students do these things out of the box rather than kind
*  of through this kind of hacky way of saying, well, try this type of a prompt and chat GBT to do this.
*  Right. I mean, that's going to disappear when we start seeing things get integrated in things like
*  Google Classroom and my learning space and things like that. Right. We're not there yet,
*  but I imagine we're more months away from it if not even weeks or something like that at this point.
*  Yeah, we did an episode with Khan Academy and they've got plenty more work to do.
*  Of course, but they've really made a nice start at just at a baseline level. Their main approach is
*  the thing will not do the work for you. It's a Socratic approach. It'll kind of go back and
*  forth with you, but it will not do the, will not solve the problem. It will not answer the question.
*  So it will only kind of lead you there. So that's a pretty good start. And then they've got lots of
*  plans for personalization and all sorts more. I think your comment maybe jumps out to me most
*  there is, it seems very obvious, but I thought you framed it extremely well that the model
*  baseline output is something you have to exceed in order to be a value add in the very short term
*  future economy. And I do think that's going to be pretty tough. I mean, I think we're already
*  at a place where I wonder what you would say you see in terms of just like comparing today's language
*  models to your students, but like across the board, it seems like a good short summary of where we
*  are is, and I'll use GPT-4 here, the best models, you know, the GPT-4s are better than the average
*  person on most tasks and closing in on expert performance on very common tasks, still falling
*  short usually, but like getting pretty close on the most routine expert tasks and still well short
*  when it comes to the sort of breakthrough insight type generation that is sort of the non-routine
*  work that's, you know, kind of the most alpha. Like I don't see that really coming from AI
*  much at all yet, if at all. So if you would see that any differently or how you see that kind of
*  playing out for, you know, just GPT-4 versus your students on your assignments, but it does seem like
*  the bar for getting a job might go up quite a bit and, you know, most jobs are a lot of routine
*  stuff and AI can do the routine stuff. I mean, it does seem like we're headed for, this kind of starts
*  also get into the, you know, what lessons can we draw big picture wise from history for such a moment,
*  but it does seem like we're heading into a pretty disruptive period here. Yeah, I think so. I mean,
*  I have nihilistic days where I get very kind of worried about what this looks like. There are days
*  where I get the model to do something like, oh, that's very close to what I do. That's a little
*  frightening. And, you know, I mean, I think everybody uses these models has that kind of
*  an experience, right? At some point or another. What I think history teaches about a lot of this
*  is that jobs don't tend to disappear. They tend to evolve and change. I think what's true is that
*  I had a student ask me at the beginning of a class, at the beginning of a semester, when
*  I took a very permissive approach to using chat, GBT in class, I tell them you can use it and you
*  basically responsible for the content you submit if it's full of hallucinations and
*  made up citations and you can't talk about it. Well, you know, that's, it's probably going to fail
*  on its own, right? Having nothing to do with whether it's written by AI or not. Right. And so
*  I had a student say, well, why wouldn't I just get chat to BT to do this? And like, without trying to
*  engage with it, like, what's the point? I think the response is if you have a job where all you
*  have to do is input your job into chat to BT and it outputs it, I don't think that job will exist
*  in that form for very long because you're a lot more expensive than chat to BT. And so I think that
*  what we're seeing here is, is we're trying to, we're trying to look at what that's what that means.
*  Right. I think you're right. Right now, these models are very good on a whole range of different
*  tasks, but they aren't autonomous. Right. You can't just kind of set them loose and tell them,
*  do this job. That's not how it works. Right. But there are going to be tasks that increasingly
*  people will probably do less of. So if, if in a job where you might spend a lot of time summarizing
*  written documents, you might still well have that job. It's just that you might be expected to
*  summarize more of those documents faster. Right. And that's kind of what history tells us about
*  automation in general is it's not that that job disappears. It's that the expectations of production
*  go up. Right. And I think that that's probably true here. I do think that if you are producing
*  content, right. And, you know, I think quite rightly, there's a lot of artists and writers
*  who are worried about what this does. I think that the baseline becomes important to you, right.
*  That, you know, if you think about a job where you're producing content, that's kind of just
*  what you're doing. If you're producing something that is not as good as what you can get out of
*  GPT-4, that's going to be an issue going forward. Right. I think it's also true in terms of resume
*  writing. I mean, there's a big debate about, you know, whether you should get your cover letter
*  written by Chatchabee T or not. Does that help you or hurt you? Right. And you'll see these stories
*  around. But the reality is, is that if you're submitting cover letters that are full of errors
*  and things like that, you might well find yourself anyways, not getting at the top of the,
*  at the top of the pile. And as expectations kind of go up, because you might find less
*  stylistically awkward letters, you might find yourself further and further down that list.
*  And I think that this is, this is what we're seeing. I think a lot of people see this transition
*  as being an instantaneous one or something that's all or nothing. And it's going to be much more
*  gradual and gradated, right. You're going to see basically tasks being offloaded in people's jobs
*  to Chatchabee T gradually. And those jobs will evolve and change over time. There might be fewer
*  of these types of jobs because, well, now people are more efficient at doing them. And there'll be
*  more of those types of jobs because now we need people to, you know, herd AI or something like
*  that, where effectively you're going in there and your, your task is to get all these different
*  models to coordinate and do these different things, right. And produce all these different
*  outputs. That's kind of what history teaches. I think about how these things evolve, right. Is
*  that technology is constantly changing what we do. This is an especially fast revolution. So it's,
*  it's something that's unusual in that sense. But again, you're, if we look at past kind of
*  situations, the invention of the steam engine or various types of machines that automate production,
*  it, it's not a day and night thing. It's a gradual adoption. It's a process that begins. If you
*  think about the auto industry, that process begins in the fifties and sixties. And it's still evolving
*  today, right. Will this happen faster? Probably. But again, it's not going to be day and night,
*  right. And I think that that's why learning to use this is so important right now for people is
*  engaging with the technology is, is, is I think in many ways, future proofing yourself,
*  understanding what these models can do and having an understanding of, well, if I'm asked to write a
*  paragraph on this, this is what it looks like from GPT four. I should probably be achieving and trying
*  to aim for something like that. If I'm being asked to write a paragraph, I mean, that's the kind of
*  stuff that I think we're still at is, is that encountering phase with AI for so many people.
*  I've kind of mixed feelings on this because I think you're definitely right to say the general
*  pattern of, especially if you're in any sort of volume game, the pattern of doing it manually
*  evolving toward kind of maintaining monitoring, you know, fixing supervising the quality of the
*  machines that are doing the work is like pretty well established and likely to happen here too.
*  But I also do really worry about the fact that just, I think, you know, unfortunately a lot
*  of people cannot write at a GPT four level and that is going to be pretty hard to change.
*  And I don't know. One of the things I said to the open AI team when I was doing the red teaming was
*  like, for the vast majority of people, this is super intelligence. It's just not super intelligence
*  to you because you're really smart. And so I don't know how that part gets resolved. And I think,
*  you know, at the sort of, you know, high end of the sort of whatever, let's call it intellectual
*  or academic ability range, we're still just encountering just GPT. But then, you know,
*  for so many folks who are like, never been in the university setting at all, it's just like, man,
*  that's good. That's a really big chasm to cross. And I don't know how many people do it. So I
*  don't know. And I don't know that they're going to be able to like supervise to me before either,
*  it just seems very, seems very challenging for just a huge portion of the population.
*  I often find myself shying away from those types of thoughts simply because I agree. I mean,
*  I think that there in the sense that there is, there's a huge chasm between what this can do
*  well and what many people can do at their best. And I think that that's where I think some of
*  the obligation is going to fall on companies like opening. I know Altman's talked about this as
*  others have as well about trying to figure out a way of what this means, because I think what we
*  can learn from history is that what you don't want to have happen is have a situation where
*  technology displaces huge numbers of people from the workforce and leaves them disaffected and
*  worse off as a result. That's not a good thing for society. And it's not a good thing for culture.
*  And it's not a good thing for the workforce in general. And so I think that's something we have
*  to be acutely attentive to here. I do think the technology that we're dealing with is a very
*  different one than previous technologies that we've encountered. I think some of those patterns
*  will be similar, but this is the knowledge economy, right? This is people who are,
*  the people who will be most affected here are people who are professionals and do do things
*  like write for a living and analyze documents and things like that for a living, right?
*  This is very different than previous revolutions in that sense. We haven't figured out how to
*  handle that. And there's always turmoil when this happens. I think trying to tackle both problems
*  at the same time is really important, right? It's trying to figure out how do you adopt these
*  technologies and use them, but how do you also assume or make sure that in their adoption, you
*  are ensuring that people still have access to the types of at least incomes and living standards
*  that they traditionally had, right? And find meaning in work, right? And I think that that's
*  an important thing too. So yeah, I mean, I think that those are real problems that we have to
*  contend with as a society and that are much larger than just higher education. That's pervasive.
*  Are there any historical, you could take this in whatever way you want, but could be moments,
*  could be technology revolutions, could be moments when like the social contract needed to be updated,
*  or you could think about it in a totally different way, more conceptual or whatever. But
*  what would you recommend that folks who maybe don't have such a great grounding in history
*  like myself could look to to sort of learn something about what our forebearers either
*  did successfully or failed on when they were confronted with, you know, at least the most
*  analogous challenges that we've seen in the past. Sure. I think there's a couple of good examples
*  to learn about how societies adapt to this. It's the industrial revolution, right? It's the process,
*  especially in the late 19th century of what industrialization does to societies, right?
*  And it's where you do see the development of huge impoverished classes of people who
*  are put out of work by automation or find their work devalued for what they were doing before.
*  And that's what leads to in a lot of countries, the development of social programs in the early
*  20th century, right? And into the mid 20th century is trying to fill that gap essentially between
*  that has been created by urbanization and industrialization happening at the same time.
*  So that's an area to look at. I mean, again, it's a process that plays out over a very long period.
*  This is something that will be much more condensed, but I do think it will release some of those same
*  types of forces, right? Another one I think is a little bit more removed, but is kind of telling
*  as well as the enclosure movement. This is a period in the early modern period when you begin
*  to see people getting kicked off of farms in order to basically turn them into sheep pens, because
*  effectively it becomes more profitable to farm sheep than it does that people growing crops.
*  And this leads to a huge, again, kind of group of people who are simply dispossessed of land and
*  just sent off and they end up in urban environments and in hugely problematic situations, right?
*  And again, it's about in this case, not so much a technology displacing people as it is about
*  the emergence of a new kind of economic force, right? And a transition away from a subsistence
*  agrarian economy to the beginning of a manufacturing economy. I think there's parallels
*  again there, right? And the lessons really for us from history are that when this type of a
*  transition takes place, large portions of the population do typically become disaffected and
*  alienated from kind of the jobs that they would normally have been familiar with. And that this
*  is a real problem and that governments that have navigated this successfully, although albeit in
*  fits and starts over a very long period, have done so imperfectly, although that is, by coming up with
*  social programs that effectively bridge that gap. What that looks like, I mean, I think I'm better
*  talking about the history of it than I am the future of these things, which is my cop out on
*  these types of issues. But I think that it is true, right? Is that we know that that's going to
*  happen. We know that if this technology evolves the way that it seems to me to be evolving,
*  that we will be facing this type of situation. My daughter is seven, right? And I very often think
*  what will her world look like in 15 years, right? It's very much going to look different than I
*  thought it would look when she was born. And I know that much to be true. How you prepare for that,
*  I think is a very different thing. So I think as individuals, we have to prepare for that. But I
*  think governments and whole societies have to begin to think about how we do these things
*  collectively, right? And that's where I think some of that, those conversations around the long-term
*  consequences of AI that crop up every once in a while, that we get the congressional hearings
*  about or things like that. I think that's the much more immediate threat here probably than
*  machines taking over the world type of scenarios. I think that has its place to be talked about as
*  well. But I think we really do have to deal with that issue of how we deal with the effects of this
*  technology. Well, that's a good note and a good call to action for the audience to participate in
*  that conversation and maybe start with some historical reading to get some good context.
*  Mark Humphrey's fantastic conversation. I really appreciate just how far down the AI rabbit hole
*  you have gone and what a unique and interesting perspective you have brought to it. So thank you
*  for being part of the cognitive revolution. Thank you so much for having me. It is both
*  energizing and enlightening to hear why people listen and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine.co or you can dm me on the
*  social media platform of your choice. Amnaki uses generative AI to enable you to launch hundreds of
*  thousands of ad iterations that actually work customized across all platforms with a click of
*  a button. I believe in Amnaki so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
