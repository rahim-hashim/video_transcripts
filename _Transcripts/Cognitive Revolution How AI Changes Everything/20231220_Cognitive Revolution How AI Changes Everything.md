---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 4719s
Video Keywords: []
Video Views: 6341
Video Rating: None
---

# Using ChatGPT As a Copilot For Your Mind
**Cognitive Revolution "How AI Changes Everything":** [December 20, 2023](https://www.youtube.com/watch?v=qnzA9sMYEqI)
*  When I have an article idea, I'll often start with just this like really messy document full of quotes
*  and sentences and little like things that might go into it. And then I'll be like, I don't even
*  know where to start with this. This is crazy. And then I will just be like, can you put this
*  into an outline? And I'll just paste the entire document into ChatGVT and it'll often find an
*  outline. And like the, the outlines it comes up with are like really basic, but sometimes I think
*  one of the things it's really good at is like pointing out the obvious solution that you missed
*  because you're too like close to the problem. Hello and welcome to the cognitive revolution
*  where we interview visionary researchers, entrepreneurs and builders working on the
*  frontier of artificial intelligence. Each week we'll explore their revolutionary ideas and
*  together we'll build a picture of how AI technology will transform work, life and society in the coming
*  years. I'm Nathan LeBenz joined by my cohost Eric Torenberg. Hello and welcome back to the
*  cognitive revolution. Today we're sharing an episode of the new podcast. How do you use
*  ChatGVT? How do you use ChatGVT is hosted by Dan Schipper, founder and CEO of Every,
*  a daily newsletter that promises the best business writing on the internet. In just his first few
*  episodes, he's had guests on the show, including Sahil Lavendia, Matt Eliason, Linus Lee, and today
*  yours truly. This conversation is both extremely practical and a real exchange of ideas. Coming
*  into it, I had used ChatGVT mostly for unfamiliar tasks where I really needed help orienting myself
*  and getting started. And of course I've got great value from a wide range of different use cases.
*  But to be honest, I hadn't found ChatGVT super helpful for my own writing process. So I was
*  really interested to learn more about the methods that Dan has developed to use ChatGVT as a
*  thought partner and a writing assistant. Learning from him inspired me to do more of this for myself.
*  Toward the end of the episode, Dan asks me what I am most excited about next. And I mentioned the
*  new Mamba architecture and state space models more generally, which I honestly can't stop thinking
*  and talking about. We'll have a big episode on this coming very soon. And I'm glad to report that I
*  did use some of Dan's recommendations to help develop the strategy, the devices and the overall
*  structure for that episode in a way that I did find legitimately very helpful. One note before
*  we get started, there are a few points in this episode where we each shared our screens to show
*  off content visually. And while I think you will be fine with just the audio version, if you want to
*  see the visuals, you can check out the YouTube version of this episode. Of course, there's always
*  lots more to learn. So if you like this sort of content, I encourage you to check out How Do You
*  Use Chat GPT with Dan Shipper. Welcome to the show. Thank you, Dan. Great to be here. I'm excited
*  for this. I'm excited too. For people who don't know, you are the founder of Waymark. You are the
*  host of the excellent podcast Cognitive Revolution, and you are a GPT-4 red teamer. So you are
*  responsible or one of the people on a team of people who are trying to figure out how to make
*  GPT-4 do bad stuff before it was released, which you had a really interesting tweet thread about.
*  I don't know. I think a couple of weeks ago or two weeks ago, something like that.
*  So we're very excited to have you. I think you'll have a lot of insights that I'm excited to share
*  with everyone. I think one of the things in thinking about your work that stands out and
*  thinking about Cognitive Revolution, in particular, the podcast that you run, is I think you have this
*  idea that one of the values of AI is in helping us to offload cognitive work. So just like in the way
*  that machines, in the industrial revolution, we offloaded manual physical labor, AI will
*  augment or offload a lot of cognitive labor from humans. And I wanted you to just talk about that.
*  Tell me more about what that means and then tell me, is that a good thing and where is it a good
*  thing? Well, that's a big question. I would say I talk about AI doing work and helping us in a
*  couple of different modes. For starters, we will probably spend most of our time today in
*  what I call copilot mode, which is the chat GPT experience of you are as a human going through
*  your life and going through your work and encountering situations where, especially as you
*  get used to it, you realize, oh, AI can help me here. So you make a conscious decision in real
*  time to switch over to interacting with AI for a second or a minute or whatever to get the help
*  that you need and then you proceed. But you are the agent in that situation going around and pursuing
*  your goals. In contrast, the other mode that I think is also really interesting is delegation mode.
*  And that is where you are truly offloading a task. And I always say the goal of delegation mode is to
*  get the output to the point where it is consistent enough that you don't have to review every single
*  output. And if you can get there, then you can start to really shift work to AI in a way that
*  you no longer have to do it. And that can be useful in different kinds of ways. The copilot
*  mode is about helping you be better. That's your classic symbiosis or intelligence augmentation.
*  And then the delegation mode is more like we can save a ton of time and money on things that used
*  to be a pain in our butts, or we can scale things that are not currently scalable.
*  And there's a lot of that in the world. I think almost everybody has things where they would say,
*  if you just ask the question, is there stuff that you could be doing that would be really valuable
*  to have done, but you just don't have time to do it? There's a lot of that that can be quite
*  transformative. In the middle, and what's kind of missing right now still is between copilot mode,
*  where you're getting this kind of real time help and deciding how to work it into whatever you're
*  doing. And delegation mode on the other end in between is ad hoc delegation, where it's,
*  I'm going along, but I want to, ideally, I would like to delegate more and bigger sub tasks to the
*  AI on the fly. And that's where we're not quite there yet. The agents probably can't do much in
*  the way of a significant task. So you're still shoehorned into one of two scenarios where you're
*  engaging with it in real time and getting help, or you're going through the process of doing a
*  setup and doing a validation, setting up a workflow to where you can truly delegate.
*  And it's that in between that I think is probably that gap gets closed over the next year as agents,
*  begin to work. And then we can start to delegate bigger chunks of work on the fly.
*  The next question was, is it good? I don't know if I have a great answer to that. I think it's
*  largely good. I think it's good as long as humans stay in control of the overall dynamic. And I'm
*  definitely one who considers everything to be in play for the future, both on the positive side,
*  I don't think it's crazy to think of a post-scarcity world. And on the negative side,
*  to quote Sam Altman, I wouldn't rule out lights out for all of us. I think we are definitely
*  playing with a force here that has the potential to be totally transformative in good and bad,
*  and probably a combination of ways. I'm thrilled by how much more productive I can be. And that's
*  some of the stuff that we'll get into in more detail. I am thrilled by the prospect of having
*  infinite access to expertise. And especially for people who have far less means than I do,
*  to have that kind of access to expertise. I am a pretty privileged person who can go to the doctor
*  without really thinking twice about taking the time off from work or what that's going to cost
*  me or whatever. Obviously, a lot of people don't have that luxury. I think there is a real way in
*  which AI can cover a lot of those gaps, not fully yet, but already significantly and obviously more
*  and more over time. I think that kind of stuff is going to be potentially disruptive. It may be the
*  source of a lot of political debates and challenges. But anyway, yeah, there's so much upside,
*  but I think there is very real risk. And it's very easy to hold those two perspectives at the same
*  time, to be just thrilled by the capability, but also to be always keeping in mind a healthy fear.
*  I love that. I think that's such a rare perspective. And as humans, we just tend to collapse
*  on one. Either it's horrible or it's great. And then we have these camps. And I think obviously
*  the wise perspective is there's going to be some really amazing stuff about this. And there are
*  dangers. When technology changes society, it'll change our brains. We will adapt to this in the
*  same way that it is adapting to us. That will change things. And we'll need to deal with the
*  dangers that it presents. I think that's a very wise perspective. And I asked that question,
*  is it a good thing that cognitive work will be offloaded? Because I think that there's good and
*  bad. But one of the things that I feel is the fear scenario is quite dominant for a lot of people.
*  And I think the people who are anti-fear or presenting a hopeful view are a little,
*  but they're a little bit too like rose-colored glasses. And I think finding real ways and real
*  use cases for how offloading some of this cognitive work actually helps people is just a really
*  important part of creating a world where AI is a force for good or a force for creativity,
*  rather than a world where it just replaces people or it creates dangers or there's all the bad
*  scenarios. And one of the things that I've felt going back to your co-pilot mode versus
*  delegation mode point, one of the things that I felt is that AI reveals to me how much drudgery
*  there is even in highly valuable, highly creative knowledge work. And that we lie to ourselves about
*  the amount of drudgery because that work is so romantic compared to, I don't know, working in a
*  factory maybe or just any other kind of job. And it's easy to look at a lawyer and be like,
*  a lawyer's job is full of drudgery or whatever. But I write, I run a business, I have a YouTube
*  show now, I have a podcast. There's a lot of stuff that's just pure drudgery of that. And I find it
*  really interesting because using Chatchie BT, using AI tools more broadly, it has made me aware of how
*  many repetitive or overall brain dead things I have to do just to write something smart on the
*  internet on every. And once it's visible, I use AI for it. And then I don't have to think about it
*  as much anymore. And I think that's a really cool thing. Totally. For me, coding comes to mind
*  most there when you talk about the drudgery of high value and again, pretty privileged work to
*  be doing. But I'm not a full-time coder, have been for a couple short stretches in life, but
*  more often I've been somebody who's dipped in and out of it. And it is a real pain in the butt to
*  have to Google everything. And obviously different people have different strengths and weaknesses.
*  I do not remember syntax super well. Sometimes if it's been a while, I'm like, wait a second,
*  am I remembering JavaScript? Or am I remembering Python? What exactly is going on here?
*  And so to be able to just have the thing type out even relatively simple stuff for me is a
*  multiple X speed up often in terms of productivity improvements, often an improvement in just strict
*  quality too, compared to what I would have done on my own and makes it so much easier to get into
*  the mode in the first place. There's this kind of, I wouldn't even call this drudgery, but it's
*  gearing up just somehow getting my, people talk about in birdwatching, getting your eyes on,
*  really focusing on what are you seeing and trying to get that detector right. There's a similar
*  thing, at least for me, in terms of getting into code mode. And it also just streamlines that
*  tremendously because next thing you know, it's writing the code and I'm reading the code.
*  Reading the code is a lot easier than writing the code. So I do find just tremendous satisfaction,
*  pleasure in just seeing this stuff outputted for me at superhuman pace, better than me quality,
*  maybe not superhuman quality, but super Nathan quality. It's awesome.
*  Mad Fientist What you're making me think about is,
*  because I think in large part, not all of it, but in large part, what the current class,
*  especially of text models are doing is different forms of summarizing and how much summarizing is
*  involved in creative work and programming in writing, in decision-making. A lot of it is just
*  summarizing. In programming, you're summarizing what you find on Google. You have to decide what
*  to summarize and you have to summarize it in the right exact way for your specific use case. But
*  that's a lot of times what you're doing. Same thing for writing. A lot of the stuff in my pieces
*  are summaries of books that I've read or conversations I've had or ideas that I found
*  somewhere else that I'm stringing together in a unique way. Obviously, I still have to do the
*  overall management task of deciding which summaries to put in which order and how they work
*  or whatever, but a lot of it is summary. I think that's a way that using these tools,
*  you start to see the world a little bit differently and you're like, oh yeah, there's a whole
*  class of things I'm doing that are summaries that I don't have to do anymore. I really think that's
*  cool. Nathaniel Yeah, I should be one of the areas where I have not adopted
*  AI as much as I probably should have is in repurposing content, making more of what I do
*  with the podcast because I've put out a lot of episodes. There's a lot of stuff there
*  and we do use AI in our workflows to, for example, create the timestamp outline of the different
*  discussion topics at different times throughout the show. That's the most classic summarization
*  where I'm not looking for a lot of color commentary. It's literally just what was
*  the topic at each time. Get it right. We've got some stuff that we go to pretty regularly,
*  but I have not done as much as I probably could or should. Maybe this will be a New Year's resolution
*  to bring that to all the different platforms. I think it's actually an interesting, it's partly
*  a personal quirk and it is also, I think, a limitation of the current language models that
*  I never quite feel like I want them to write as me. I'm very interested to hear your thoughts on
*  how you relate to it in the writing process. When I put something out in my own name,
*  I basically don't use Chess GPT at all for it. I can use it, I find, for voice of the show if I want
*  to do that timestamp outline or just create a quick summary that's in a neutral voice where it's not
*  signed Nathan and isn't supposed to be representing my perspective. But I haven't been able to get a,
*  I haven't really had a great synthesis yet to help create stuff that I want to say in my own voice,
*  in my own name. If you have tips on that, that would be something I would love to come away with
*  a better plan of attack on because I'm not quite there. Hey, we'll continue our interview in a
*  moment after a word from our sponsors. Real quick, what's the easiest choice you can make?
*  Taking the window instead of the middle seat, outsourcing business tasks that you absolutely hate.
*  What about selling with Shopify? Shopify is the global commerce platform that helps you sell at
*  every stage of your business. Shopify powers 10% of all e-commerce in the US and Shopify is the
*  global force behind Allbirds, Rothy's and Brooklyn and millions of other entrepreneurs of every size
*  across 175 countries. Whether you're selling security systems or marketing memory modules,
*  Shopify helps you sell everywhere from their all in one e-commerce platform to their in-person
*  POS system. Wherever and whatever you're selling, Shopify has got you covered. I've used it in the
*  past at the companies I've founded and when we launch merch here at Turpentine, Shopify will
*  be our go-to. Shopify helps turn browsers into buyers with the internet's best converting
*  checkout, up to 36% better compared to other leading commerce platforms. And Shopify helps
*  you sell more with less effort thanks to Shopify magic, your AI powered all-star. With Shopify
*  magic, whip up captivating content that converts from blog posts to product descriptions, generate
*  instant FAQ answers, pick the perfect email send time. Plus Shopify magic is free for every Shopify
*  seller. Businesses that grow, grow with Shopify. Sign up for a $1 per month trial period at
*  shopify.com slash cognitive. Go to shopify.com slash cognitive now to grow your business no
*  matter what stage you're in. shopify.com slash cognitive.
*  I do. I definitely do. I love it. I think it goes back again to when you talk about being a co-pilot,
*  I think that the failure mode is usually trying to use it when it's a little bit more in delegation
*  mode. Just go do this whole thing. That's when it doesn't really work. But as a co-pilot,
*  it really works incredibly well for specific micro tasks in writing. So first example that like as
*  I just brought up, everything is a summary. I often have to explain an idea. I was writing
*  a piece a couple months ago where I had to explain an idea that I knew the idea was I was talking
*  about SPF and FTX's collapse and how utilitarianism and effective altruism, whether or not that
*  philosophy contributed to the collapse. And in order to write that article, I had to summarize
*  the main tenets of utilitarianism. And I studied philosophy in college and I've read a lot of Peter
*  Singer's work and I just generally know it, but I haven't written about that in a while.
*  Ordinarily, I would have had to spend three hours going back through all the different stuff to
*  formulate my three or four sentence summary. But I just asked Chachi BT and it gave me the summary
*  in the context that I needed it in three or four sentences. And I didn't use that wholesale,
*  but it gave me basically the thing I needed to tweak it and put it into my voice. And so that's
*  a really simple example, but I think you can use it in all different parts in the writing process
*  from at the very beginning. I'll often just record myself on a walk, just spewing ideas and
*  random thoughts, re-associating, and then I'll have it transcribe it and summarize it and pull
*  out the main things. And then I'll help me find little article ideas. When I have an article idea,
*  I'll often start with just this really messy document full of quotes and sentences and
*  little things that might go into it. And then I'll be like, I don't even know where to start
*  with this. This is crazy. And then I will just be like, can you put this into an outline? And I'll
*  just paste the entire document into Chachi BT and it'll often find an outline. And the outlines it
*  comes up with are really basic, but sometimes I think one of the things it's really good at is
*  pointing out the obvious solution that you missed because you're too close to the problem. Oh,
*  of course, the outline for this article is set up the problem and then talk about the solution to
*  the problem that you came up with or whatever. That's such a common format for an article,
*  but if you're in your head about it and you're being really precious, it can be hard to be like,
*  for this special article, it's going to be this basic thing that you've written a thousand times
*  before, the same basic structure. And then I think one of the other really great things is
*  it's just incredibly good for helping you figure out what you're trying to express, put into words
*  what you're going for, and then also going through the different options of how to express what you
*  want to express until you find something that exactly says the thing you want. For example,
*  like trying to find exactly the right metaphor. Okay. What kind of metaphor are you trying to
*  find? What's the idea you're trying to express? And then here's 50 different options of ways to
*  express that with a metaphor. And 49 of them will be trash and one of them will be amazing,
*  or one of them will push you in the direction of what the actual, like the one that you come
*  up with is. And I have like zillions of examples of that. So I find that ChatGBT, it's all over
*  my writing, but none of the stuff that makes it into the writing I publish is like wholesale
*  from ChatGBT. It's like doing some of those micro tasks for me all the time.
*  Yeah. That's interesting. Some of the stuff that you mentioned there, I have had some luck with
*  the talking to it on a walk is quite helpful in some cases. I've done a couple of things where
*  I tried to draft like a letter and do, as you said, talk my way through it. Here's what I want to say,
*  I'm writing here to this person. Here's a little bit of context. Here's the key points I want to
*  get across. Can you do a draft? And then iterating verbally on that draft, a lot of times I'll be,
*  I'll follow up and be like, okay, that's pretty good, but you can give it pretty detailed feedback
*  too. The transcription in the app is so good that it is again, point of privilege. It understands
*  me extremely well. So I can literally just scroll through its first generation and say,
*  on the first paragraph, I don't really want to say that it's more like this in the second paragraph,
*  more emphasis on this, add this detail, give it like eight things, but you could wish it
*  would do a little bit better on the revision. I've had a few moments there where at the end
*  of that process, I have something like, all right, when I get back to the desk, it's not that far of
*  a leap from that to the actual version that I'll use. It's probably still underutilized for me. I
*  should go on more walks, honestly, get more time away from the screen, get the blood flowing a
*  little bit and use a different modality. The micro tasks, I should do more though. I think that's the
*  tip that I'm taking here is, and there's a separation between like, sometimes where I feel
*  like it's hurting me is if I haven't, and this will even now start to happen in like Gmail or
*  anywhere where there's this like auto complete that's popping up. Sometimes I'm like, I'm on the
*  verge of a thought that is really the thought that I'm trying to articulate. And then this auto
*  complete comes up and it's, that's not right. But it can derail you at times where you're like,
*  don't guess for me right now. Let me get the core ideas down first. If you don't have those core
*  ideas, then for me, it's been a real struggle to get anything good. But I think I've probably not
*  done enough experimentation in the writing process of, okay, I do have some core ideas.
*  Can you help me order them, structure them, iterate on them? Interestingly, I also do use it at the
*  other end often, critique this. Here's an email, here's a whatever, here's an intro to a podcast,
*  critique it. That could be really useful if its critiques are usually worthy of consideration,
*  at least I would say. Yeah, it truly is good at that. And we have multiple editors who are like,
*  highly skilled. And I still use it to be like, what do you think of this intro? Because it's up at 2am
*  when I'm, the night before deadline. Yeah, it's real hard to beat the availability.
*  The responsiveness is clearly superhuman on that. I think the writing stuff is really fun. I would
*  love to, if you're ready for it, I would love to start just diving into how you actually,
*  how you use chat GBT. Sure. You sent me a doc with a bunch of historical chats, and this was the first
*  one. Give us the setup. What were you doing? And at what point were you like, oh, I need to go into
*  chat GBT and then, and take us from there. So I am working as the AI advisor at a company called
*  Athena, which was founded by a friend of mine named Jonathan. And is this the like virtual
*  assistant company, the Thumbtack, Thumbtack? Yes. He is one of the founders of Thumbtack. And this
*  is a different company, but founded on some of the lessons that he learned in the Thumbtack
*  experience. He legendarily built up like a really amazing operation powered by contractors in the
*  Philippines. And that included hiring an assistant for himself in his role at Thumbtack, who became
*  like almost another key partner in his life over a long time. And then Athena was built to
*  essentially try to scale that magic for startup founders, executives in general. They hire
*  executive assistants in the Philippines. They pay premium wage. They're really focused on getting
*  super high quality people. And the idea is to empower the most ambitious and most high impact
*  people by equipping them with this ability to delegate to their assistant in a transformative
*  way. Okay. Now we're working on what does AI mean for us, right? How do we bring that into
*  the assistance work? So one of the things I've done is train the assistants on the use of
*  AI. And that's been a fascinating experience, putting content together, examples, etc.
*  Another thing that I've done is just worked on building a number of kind of prototype demos for
*  what the technology of the future might start to look like. And this chat, which we call Athena chat,
*  is basically our own custom in-house chat GPT is built on an open source project. So I didn't have
*  to code every line of it, but it is amazing how quickly you can build things like this today with
*  a bit of know-how. So it's been me and one other person who have built a number of these prototypes.
*  In this case, what we wanted to do is say, can we create a long-lived profile that represents the
*  client that can assist the EA in all sorts of ways? So it's essentially a plugin, but with plugins,
*  you have some limitations, whatever we experimenting with this on our own. One of
*  the big things we wanted to enable is adding information to the client profile, updating
*  information that's already in there. So the hope is that this could be a hub where over time,
*  client preferences and history and even background context documents all can gradually find their way
*  in there. And you have this holistic view where the assistant can go query anything they need,
*  but again, also update, add to it's in theory supposed to evolve over time.
*  So we have this chat GPT interface. And one of the things that we've noticed is that we still see,
*  despite our attempts at education, it's not perfect. We still see that assistants sometimes need
*  coaching on how to effectively prompt a language model. So that was my motivation coming into this
*  little thing. I already had this react app, which is again, just a chat GPT like little app.
*  And I wanted to add a module to it. The module I wanted to add was a prompt coach. So I wanted to
*  take a, put in another little layer where it would look at what the assistant, the human assistant
*  put into the chat app and send that through its own prompt to say, are you applying all the best
*  practices? Are you telling the AI like what role you want it to play? What job you want it to do?
*  Are you specifying a format that you want your response back in? Are you, often these days we'll
*  do it by default, but are you setting it up in such a way where it will do some sort of chain of
*  thought, think out loud, think step by step reasoning before giving a final answer? That's
*  actually one of the most common things I see people do to shoot themselves in the foot with AI
*  performance is prompt in such a way where it prevents the, what is now the kind of trained in
*  default behavior of explain, analyze, think about it a little bit before getting to a final answer.
*  So you just have like a number of best practices. Let me stop you there real quick. What are people
*  doing that would prevent the model from doing the kind of chain of thought best practice that,
*  that makes it reason the best? Anything that just sets it up in such a way where it's got to answer
*  immediately with no ability to scratch its way through the problem is bad. And I see that very
*  often it's common. It happens even in like academic publications, not infrequently.
*  Often that's a hangover from the earlier era of multi-shot prompting. And obviously this is all
*  changing super quick, right? But if you go back, the first instruction model that hit the public
*  was open AI's text DaVinci O02 in January of 2022. So we're almost on two years,
*  but still not even two years since you could first just tell the AI, write me a haiku and it would
*  attempt to write you a haiku. At that point, it was not as like going to get the syllables right.
*  The earlier generations were, you would have to say a haiku by author name colon, and then hopefully
*  it would continue the pattern. That's the classic prompting. And with instructions,
*  now you can tell it what you want to do. And obviously that's gotten better and better.
*  But in the benchmarking, in an academic context that was developed before this instruction change,
*  typically you would have like question, answer, question, answer, question, answer, question,
*  and the AI's job would be to give you the answer. And so they would be measured off and on five shot
*  prompts or what have you. But a lot of that stuff was all that scaffolding was built before
*  people had even figured out chain of thought. And so now if you take that exact structure and
*  you bring it to a GBT four, you're often much better off just giving it a single question
*  with no structure, letting it spell out its reasoning. Because again, now it will do that
*  by default and then give you an answer versus if you set up question, answer, question, answer,
*  it will respect the implicit structure that you are establishing and it will jump straight to an
*  answer. Often these are like multiple choice or they could be a number or what have you. It will
*  jump to an answer, but the quality of the answer is much reduced compared to default behavior.
*  If you just let it think itself through it. And I've even seen this in Bard. I think this is
*  hopefully now fixed, but not too long ago, Bard would give you an answer before explanation by
*  default. And again, that's just like, you're going to have a problem. So that sometimes people do
*  that by mistake. They'll say, give an answer and then explain your reasoning. You're just hurting
*  yourself, right? Cause it will explain its reasoning for a wrong answer once the wrong answer is
*  established. So AAA is my, in the EA education, it's AAA for AAA results analysis before answer
*  always. I never heard that before. I like that. It's hopefully, hopefully they'll remember it
*  coming out. No, I like it. Hey, we'll continue our interview in a moment after a word from our
*  sponsors. If you're a startup founder or executive running a growing business, you know that as you
*  scale your systems break down and the cracks start to show. If this resonates with you, there are
*  three numbers you need to know. 36,000, 25 and one 36,000. That's the number of businesses which
*  have upgraded to NetSuite by Oracle. NetSuite is the number one cloud financial system,
*  streamline accounting, financial management, inventory, HR, and more. 25. NetSuite turns
*  25 this year. That's 25 years of helping businesses do more with less, close their books in days,
*  not weeks and drive down costs. One, because your business is one of a kind. So you get a customized
*  solution for all your KPIs in one efficient system with one source of truth, manage risk,
*  get reliable forecasts and improve margins. Everything you need all in one place. Right now,
*  download NetSuite's popular KPI checklist designed to give you consistently excellent performance,
*  absolutely free and netsuite.com slash cognitive. That's netsuite.com slash cognitive to get your
*  own KPI checklist netsuite.com slash cognitive. Amnaki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Amnaki so much that I invested in it and I recommend you
*  use it too. Use Cogrev to get a 10% discount. And just to summarize, I think basically what
*  you're saying is a previous generation of prompting really encouraged in your prompt to give multiple
*  examples of the kind of question and answer or kind of thing that you wanted the model to do
*  and then set up the last example such that the next thing the model would do is give you a
*  direct response. But what we found over time is one other really effective thing to do is rather
*  than have the model give a direct response or direct answer to a question or a problem posed
*  to it is letting the model quote unquote think out loud first by reasoning through the problem,
*  just like a human would do a word problem. And then at the end of its response, give an answer,
*  improves the quality of the answer that you're giving and improves the quality of the result
*  that you get from the model. And what has happened is open AI and other model providers have made
*  that more of the default behavior so that it'll pretty much always do that. But using previous
*  prompting techniques, a few shot prompting or multi shot prompting where you're giving examples
*  might lead it to just answer directly and you should look out for that and try to avoid that.
*  It's a great summary. Yes. If it is jumping directly to an answer, you are for sure leaving
*  performance on the table for all but maybe the most trivial tasks.
*  And just an aside, see how much our creative work is just summarizing.
*  Important because I tend to give you the long version by default. That's my default behavior.
*  This is one of those micro tasks that I'll just be handing off to an AI avatar version of me at
*  some point. Okay. So let's get back to this. You're working on an app and you want to add
*  a module to it that explains some prompting techniques. And it looks like the app itself
*  is something that you didn't build from scratch and you're trying to get the lay of the land.
*  So you know what to do. Exactly. Yeah. And the problem is I know how to code
*  generally and I've even coded in JavaScript quite a bit, but React is a JavaScript framework
*  that has a sort of hierarchy of best practices that if you know them and you can easily apply
*  them, then you can work quickly with the framework, right? That's the value of all these frameworks.
*  But if you don't know them and you're coming in cold like I was, then where do I even go
*  to? There's all these different folders and file structure and where exactly am I supposed to look
*  for the kind of thing that I want to do and where do I put a new module? And so that's where this
*  chat really starts. I have a working app. I have the code for the app, but I've never
*  worked with a React app personally hands on before. So I literally just set up the scenario
*  and I don't really use too much in the way of custom instructions or super elaborate prompts.
*  In my co-pilot mode work, certainly in delegation mode, then you get into a lot more detailed
*  prompts with if this, then that, cases, structured formats, et cetera, et cetera.
*  But I often just find a pretty naive approach is effective for things like this. And so I just
*  start off by telling it, I'm working on this React app project and I am a bit lost. Can you explain
*  the structure of the app? I give it a little bit more information and it starts giving me a tutorial
*  of what it is that I'm looking at. And then you've got React and you've got Redux and then you've got
*  these kind of additional slice JS toolkits and sagas and these frameworks. And in some cases,
*  take on a life of their own where there's whole conferences and companies. And it's like, you can
*  be very deep down this rabbit hole and whoever built this open source project that I'm trying
*  to modify, they're using a bunch of different things that are not even necessarily standard,
*  but are common or whatever. So there's just like five different things here that I have no idea
*  about. And without this kind of tutorial, I'd be like going off to search for, okay, what is this
*  saga JS? What does that even do? It's able to give me that entire rundown extremely quickly.
*  And then this I thought was a really interesting moment because I get a lot of value from things
*  like this where I feel like it's prompting me and it wasn't exactly that here, but it gives me this
*  general structure. And then I was like, oh, I find it as a general pattern. If you can give it
*  something in a format that it natively showed you, that's probably going to work pretty well.
*  So sometimes if I'm even in kind of the delegation mode, sometimes I'll be like, I don't exactly know
*  what structure this should have, but maybe if I have it suggests the structure, then we'll get a
*  structure that it can naturally work well with. Well, in this case, the structure is like dictated
*  by the world, but it's pretty well known that, okay, this is going to be your structure of a
*  project in this react framework. Okay, cool. But this got me thinking I should give it my
*  actual structure. Like I want to print this thing out for this project that I'm working on, because
*  I didn't make it. I don't know what it is. I don't want to have it help me interpret that full thing.
*  But then again, I'm like, how do I print something like this? I don't even know how to do that.
*  So then my next question for it is, can you write me the command to print out the file structure?
*  And this is where you're like, okay, this is magic, right? Because now again, I don't know how to do
*  this. This tree command, I don't know if it was installed for me or not, but okay, shows me how
*  to do it. And next thing, oh, there's another step here of installing some package that needed to be
*  installed. Okay. It was helping with that. So I'm just encountering all these. This is the classic
*  developer experience. Conceptually, I have a clear idea of what I want to do. But now I'm like
*  three levels, three nested problems down here, right? Where I'm like, oh, okay, I need to
*  understand this framework. Oh, okay. I need to print out the structure to better understand
*  the version I'm working with in this framework. Oh, now I need to install something so I can do
*  that print. And this is where people just time goes to die, right? It's like, you talk to
*  programmers and you're like, yeah, you didn't get anything done today, huh? But what happened was
*  I was on the way to the market to get my app together. And then I had to install this thing.
*  And then I couldn't install, but each of these things, like it's helping me get over.
*  And now finally I'm able to say, okay, here is my app. This is the app that I actually am working
*  with. And now we're really getting into something good because it can now break that down. And the
*  names of the things are like pretty semantic. I noticed I haven't even given it any code here.
*  I've just given it the file names, but the file names have a kind of an indication of what is what.
*  And it gets a sense just from that of what the app actually is. So let's go over to,
*  I think I just got a link to a working version of the app. It's pretty simple. It's a chat GPT
*  like environment. We can create these client profiles. We have our chats, we have our history,
*  a couple of different models, and there's function calling in the background that connects the chat
*  experience to the client profile. And what I'm trying to add is a module in the lower right-hand
*  corner, which I'm actually not sure if this version has, but the point of it is to take my prompts,
*  run them through this meta prompt as we discussed, and then show feedback warnings of, hey, you may
*  or may not be doing this quite right. So back to the thing I've given the file structure. It's now
*  able to understand the file structure. And now I'm saying, okay, here's what I'm trying to do.
*  I'm trying to create this prompt coach. I forget exactly how I had approached this. Yeah, this is a
*  different, this is a different file. Let me see exactly what I'm doing here.
*  It seems like maybe you had some sample code or something you'd written or.
*  Yeah, I did. I guess I took one stab at it myself and it didn't work. I see where I'm looking at,
*  you know, the human version that I was looking at the same file structure. And I'm like, okay,
*  I see that there's this module. There's like a sidebar here. And as you see these names, right.
*  So you've got sidebar and search and there's going to be like chat history here somewhere, chat.
*  I'm looking at this and I'm like, okay, I see all these different elements and I see all these
*  things. Let me just try to copy one and mess with it a little bit and hopefully get somewhere.
*  And then I'm not getting anywhere. It's not showing up where I want to show up. I'm not seeing it.
*  And so that's where I come to say, okay, now here's what I tried. Why isn't it working?
*  Yeah. And I explained my problem here at the end. The problem I have
*  is that it's being shown in the wrong place. So then it explains the answer.
*  Yeah. Next thing we're mod of it's giving me instructions with code, modify this, put it over
*  here. This is pretty cool too. Unfortunately, we can't share the old screenshots. I don't know
*  exactly what I used, but this is right as vision was being introduced to chat GPT as well. So
*  I was able to then say, here's my screenshot. Here's where it is showing up. And here's where
*  I want it to show up. And can you help me with that as well? So from the screenshots,
*  from the HTML structure, basically we just work through this entire thing. I continue to run into
*  issues. We're only 25% of the way through this whole thing. This probably took me, I don't know,
*  two to three hours total to get these suggestions, implement them, see what's going wrong, yada, yada,
*  it writes all the code basically. Cause again, I've never written a line of react code in my
*  life. So I don't know any of this syntax, there's a million ways to get it not quite right when you
*  have no idea what you're doing anyway. And so it's writing all the code and just bit by bit,
*  we're refining the experience. We're finding the interface here. We're creating some CSS. We're
*  using, we have a particular style pack that's already built into this. So again, that's just
*  another thing I'm not at all familiar with. This is the syntax for figuring out how to use that
*  style pack. Good luck making that up on your own. And then we go basically after a couple of hours,
*  I got to a working module where the prompt coach would intercept your call, do the meta prompt,
*  parse the response, identify, I had it giving suggestions and the urgency of the suggestion.
*  So we're color coding those suggestions as they come up. If it's serious, then you get it in red
*  and if it's not, you can get it in yellow or just a notice. And I would have, I would guess that
*  this would have taken me easily order of magnitude longer in a pre chat GPT era. If this was two to
*  three hours, it's probably two to three days of work to figure out all this stuff. And I know a
*  lot more frustration that is, because I'm not a super patient person. The feeling of a million
*  people have done something almost exactly like this. There's nothing differentiated or special
*  about what I'm doing. I'm just like in this phase of kind of not knowing what I'm doing and just
*  getting constantly stuck, constantly stumbling, constantly running into friction. I really don't
*  enjoy that. I think most people don't. This is none of that or almost none of it, right? Even just
*  that going back to the install, right? Or the command to print out the structure. Man, this is
*  so stupid. I know exactly what I want. I know that it is doable. I know that it's been done
*  a million times, a million places, and yet I don't know how to do it. And then liberating me from
*  that frustration is, and it turns out, your drudgery point, right? That was probably 80 to 90% of the
*  time in a world where I was doing this on my own. And now we're down to the two to three hours where
*  it was really about defining what I want. This could have been one hour if I really knew React,
*  but it taught me the ropes and did the task in probably, again, 80 to 90% time savings compared
*  to the unassisted version. I love this. I think this is such a cool example. I really appreciate
*  you bringing this because one, yeah, it's obvious that this kind of thing, which if you're not a
*  programmer, as a programmer looking at this, I'm like, yeah, this is so much of what you do as a
*  programmer, especially if you're a programmer working on startup stuff is this kind of thing.
*  This is doable. It's been achieved before. I just need to do it in my specific context. And
*  it's obvious that this would have taken you days or taken really anyone days to do from scratch.
*  But with ChatGBT, it makes it way quicker and takes away a lot of the drudgery. But I think
*  what's really cool and really beautiful, which is weird to say about this stuff, it's striking me
*  right now, is there's this dance happening in this chat where at the beginning, obviously you're
*  asking it to help you, but you are giving it what it needs and filling in the gaps that it needs
*  in order to help you. And it is filling in the gaps for you as well. So it is explaining,
*  react to you, but you are explaining, here is the project that I have and here are the specific
*  details that I want done. And then there's this dance back and forth where you're mutually filling
*  in gaps that both of you can't on your own fill in. And I think that is really cool
*  to just watch that evolve where at the start, you don't know React and you don't know where to put
*  your code and you don't know why it's not working. And at the start, it doesn't know who you are or
*  what you're trying to accomplish or what the specifics of your project is. But as you build
*  up this chat, you yourself are starting to understand things more. You didn't ask it,
*  just go do this for me. You asked, how does a React project work? And what is the structure?
*  And so you learned more about React and it learned more about you. And as your mutual
*  understanding increased, you were both able to accomplish the thing together. And I think that's
*  really cool. Yeah, it's awesome. The next generation, it's episodic. We're still only halfway through
*  this scroll for all the scrolling I've done. I just highlighted this. Okay, cool. This is working
*  because at this point I'm starting to get into refinements. Okay, now I want to dial in the
*  styling. And basically at this point, the core problems have been solved. And now again, it's
*  just going to do the drudgery of making sure that there's padding and things are centered and so on
*  and so forth. I try to be polite and encouraging to my AIs wherever I possibly can. But you can
*  envision a future. And I think that future is already starting to become visible through the
*  mist a little bit as more and more stuff gets published on the research side, where this
*  episodic relationship where I start a new chat, it now knows nothing about this. I can continue
*  this chat up to a limit and obviously superhuman expansive background knowledge, but zero contextual
*  knowledge. And we can't retain that from one episode to the next. But I do think that is also
*  coming soon too. And there's a couple of different ways it could shape up. But I think we will in a
*  year, certainly not that much longer than that. I can't imagine start to see things where
*  all this history is accumulated or maybe divided into different threads or whatever,
*  but where this kind of can follow you forward into different tasks as well in a history aware way,
*  I think will be another level of unlock. I think you're totally right. That's what
*  custom instructions is. It's a step in that direction. Unfortunately, custom instructions
*  is very hard to set up. But if you do set it up, it's really great. It's really nice for it to have
*  context on you. But I do think you're right. Chad GBT will definitely have a memory that it can
*  reference this stuff and reference the context of what you need and who you are. And that will make
*  it even with the same level of intelligence of the model will make it like 10X more useful and
*  10X faster to get to the right answer. How much do you put into custom instructions?
*  Because for something like this, it might be my profile, my writing sample, maybe whatever,
*  but I probably wouldn't have. By the way, Nathan's a React novice and doesn't know how to install
*  anything. Do you have a vision or a sort of recommendation for a custom instruction that
*  would help me with things like this? You're asking the right person. I have a very extensive
*  custom instruction and a lot of opinions about it. If you want, I can share it with you right now and
*  we can talk about it. Yeah, let's check it out. Okay. The first part of custom instructions is
*  what do you want Chad GBT to know about you? And I actually like really having it know a little
*  bit about who I am because there's enough about me on the internet that it knows my name. And that
*  actually helps. Same thing with every, there's enough about every internet that it knows my name.
*  And every once in a while, not having to explain who I am or what the company is that I run is
*  really useful. For example, I was thinking a couple of weeks ago about starting a course
*  and I was working with Chad GBT to decide how to do the course and whatever. And the first
*  prompt was, I want to do a course. Can you help me think about it? And with custom instructions on,
*  it knows that I'm a writer and entrepreneur. So cool, I'll help you build a course. Here's
*  how to think about it because it knows that I'm probably going to build one. But if I turn custom
*  instructions off, it will be like, cool, what course do you want to take? And it's those little
*  things that really make a difference for me. But basically, who serious relationships in my life
*  are, I have in here, like my sister, her husband, her son, I have my girlfriend up there,
*  who people are at every, because referencing their names is just much easier for me to be like,
*  okay, when I'm talking about something and not have to explain who she is every single time,
*  is really helpful. I think another really interesting thing is adding into custom
*  instructions. What are the things about you that you know that you're trying to work on?
*  For example, I feel like I have a fear of rejecting people, which causes me to be too agreeable.
*  I'm a little bit too opportunistic, and I would like to be more strategic. Stuff like that is
*  really helpful to put in custom instructions because it says little realizations that you have
*  every day. We're like, wow, yeah, I am a little too opportunistic. I think ChildGP is great for
*  being the thing that can help you as you're in the moment day to day, remember to pull back and
*  incorporate some of these insights that you have that everyone has about themselves.
*  Same thing for goals, having to know what your goals are and bring you back to those things
*  all the time as you're using it is really helpful. Cool. Thanks for sharing. I think I use it a lot
*  more for just very unfamiliar topics. I'm very, just looking at these examples that we had queued
*  up. There's an app in a framework that I've never touched and know nothing about, working on a
*  patent application and creating diagrams for a patent application. I don't really know how to
*  do that at all. Again, I'm starting with these very basic questions. What's a good syntax that
*  I might use to create a diagram for a patent application? I just come in so cold, but it does
*  suggest that you are doing a lot more thought partner brainstorming about your
*  core stuff, which is interesting. I'm much more on these kind of episodic things that
*  were like my history and this doesn't overlap almost at all in a lot of cases, but it just
*  goes to show how many different ways of using these tools there are too. This could be another
*  new year's resolution to try to bring it a little bit closer to the core of what I do. It's not to
*  say that it's not at the core of what I do, but not in this co-pilot way with things like Waymark,
*  I'm working very closely with language models to make an app work well. I feel like I have intimate
*  knowledge of the details of how it works in that respect and it's a big project for me.
*  But again, it's a different mode than the interactive dance kind of mode that you describe.
*  Fascinating. Yeah. That makes a lot of sense. I definitely use it for some of this knowledge
*  exploration stuff too, but yeah, it's totally a thought partner for me. I'd love to keep looking
*  through some of the other chats you brought. Cool. Here's this next one on working on diagrams.
*  We're going to have a combination of a provisional patent application and the supporting diagrams
*  for the patent application. This is something that I was doing for Waymark and we have this
*  ensemble method of creating advertising video for small business. Basically folks come in to
*  the site, they get to enter a website URL. Typically people will give the homepage of
*  their small business website. We have some code that goes in, grabs content off of that website,
*  and then we build a profile kind of synthetically, if your custom instructions so to speak,
*  within the context of our app. Who are you as a user? What's your business? What are you all about?
*  What kind of business? What images? And then to actually create the video, you give a very
*  specific, although it's a super short instruction, I want to make a video for my sale this Saturday
*  where I'm opening a new location and here's the address or whatever. It's like these very,
*  this is my purpose in this moment prompt. And then we've got a pretty complicated machinery
*  that takes all those inputs and it works with a language model to write a script. And then
*  it has computer vision components that decide which of the images from your library should be
*  used to complement the script or all these different points along the way. And that is,
*  it's a pretty cool experience now, really compared to, again, you think about pre-AI and now
*  what we had before was an easy to use template library. And what we have now is really the AI
*  makes you content. Like it's a phase change in terms of how easy it is to use, how quick the
*  experience is, how much you can just rifle through ideas. If you don't like the first thing, you just
*  ask it to do another. And it's qualitatively just way more fun. People used to have to sit there and
*  type stuff in and they were like, okay, what do I have, what do I say? And I'm not sure what to say.
*  And a lot of people are not content creators, but everybody always referred to the Mr. Burns
*  episode from the Simpsons a long time ago, but he goes to an art museum for reveals of some piece
*  of art and they reveal it. And he says, I'm no art critic, but I know what I hate. And that's,
*  I feel like exactly how our users operate. They ask for something, they wait 30 seconds,
*  they now get to watch a video featuring their business. And if they like it, they can proceed.
*  And if they don't like it, it's very obvious to them. And they can very quickly be like, no,
*  not that. Give me another one. And here's an alternate instruction. So anyway, this is the
*  app that we've built. And now we're like, okay, maybe we should think about filing a provisional
*  patent on that. Like most software companies, we're never going to prosecute our patents,
*  but we just want to make sure nobody can come in and give us a hard time. So how do I write a patent
*  and how do I create the diagrams? And I want to be able to update it. I want to have something
*  that's not like just a total mess. So this was a series of different interactions that ultimately
*  led me to these diagrams, but I provided initially basically what I just said to you,
*  which is a rambling sort of instruction on here is my app and here's what it does. Here's how it
*  works. Here's some of the parts behind it. The language model writes the script and the code
*  that's scraped from the website. And then the other part with the computer vision that figures
*  out what, what I just literally tell it the whole thing and say, now can you use some syntax to make
*  me a diagram that shows the structure of that app that I just word vomited to you.
*  And so there's like a bunch of different structures out there. So that's the first
*  part of that conversation as well. You could use the mermaid syntax or you could use graph vis,
*  or you could use a couple other things, but what are the pros and cons of those? And can they
*  represent certain different kinds of structures? We dialed it in on either mermaid or graph is
*  it started to make me a thing. And then you can see here too, this is interesting because I did
*  find in this one that at some point it got confused. I'd given it this thing and had
*  generated this syntax, asked for refinements on the syntax because I'm taking the syntax by
*  way, going over to another app. What's cool about the syntax is you drop in this pure text syntax
*  and it will render the app for you. Right? So you've got things like this graph is
*  diagram. What's a digraph? I don't even really know it's called this digraph is G and it has
*  these elements and they have these properties and they're connected in this sort of graph
*  structure, blah, blah, blah. You load it in half a second. You know, it renders it. You're like,
*  Oh no, that's not quite right. This point should be connected to this point and it's, it's skipping
*  one that it, so whatever. So you give it these kinds of iterations. It would make progress,
*  but then it would also get confused. It seemed after a number of rounds because there's just
*  maybe like too much syntax. So at some point I did say, okay, using the episodic memory to my
*  advantage or working around its working memory weaknesses by just wiping them and starting over.
*  I'm like, okay, here was the best one from that chat. It was closest to what I wanted it to
*  represent. Let me just go have another chat. And this time we're going to skip all the part about
*  which format do we use and skip all the word salad. And I can just be like, here's a diagram.
*  I want to make some changes to it and now have it do more localized edits for me. And again,
*  a lot of little details, a lot of nuance here, but it's happy to do that. We worked through a
*  number of rounds of it. And I believe I attached the thing for you. What I ended up with after
*  or a couple chats, you even get to the point where you're like color coding and really starting to
*  make sense of it. It's like the green in this diagram now is the things that the user does.
*  So the user tells us what their business website is. Then there's code to go scrape. Then there's
*  this fork where we have to grab all the images and we'll process them in various ways.
*  One of the big challenges is which parts of this can happen in parallel and which parts
*  depend on which parts. This is actually something that we didn't have until I did this even for the
*  technology team. And I'm not sure how well all the members of the technology team could have even
*  drawn this. So now we actually have a better reference internally also to be like, Hey, if we
*  get like, what depends on the image aesthetic step? Now we can go look at it and be like,
*  Oh, okay. Yeah. You can't select the best images until you have the aesthetic scores completed.
*  Just having that clarity is also, I think just operationally useful, but this is the sort of
*  thing that you can attach to a provisional patent application and at least begin to protect yourself
*  from future patent trolls coming your way. Again, how long would this take? If I had drawn it free
*  hand, I maybe could have drawn it in a somewhat comparable time to the amount of time that I
*  spent to exchange, but having the syntax and now having it in that kind of structured language way
*  also makes this like much more maintainable, can fit in other things, even can be like more readily
*  used in language models. The vision understanding is getting very good, but I would say it's probably
*  still better at understanding the syntax of the graph more than this visual rendering of the graph.
*  I think that's great. Obviously chat GPT has the dolly integration, so I'm familiar with that,
*  but I've been thinking a lot about sometimes I want to create something that looks like this,
*  like in a graph with texts and boxes and all that kind of stuff. And I didn't even think to do to
*  have it just write graph is markup or something like that and paste it somewhere else. So I think
*  that's a really cool thing to know it can do. And it's also pretty clear. I don't know in a year,
*  it'll probably just render the graph is stuff for you and you'll be able to like move it around and
*  do all that kind of stuff without even necessarily having to chat back and forth after the first round
*  or something like that. I think that would be a very cool next step for chat. GPT is jump into
*  an edit mode for something like this. Closest thing I've seen to that so far is diagram GPT.
*  This is a slightly different notation, but basically you can prompt in natural language.
*  It will then generate in this case mermaid syntax for you in response, and then it'll immediately
*  render your image. And you can then edit the syntax. You can't quite like drag and drop within
*  the interface itself. But I think this is a really interesting question around, or highlights a
*  really interesting question around like what things should be in chat GPT versus what things
*  should have their own distinct experience, even if there's still like a very AI assistant component
*  to it. This is one actually that I would expect lives outside of chat GPT. Who knows, right? In
*  the fullness of time, maybe you have like dynamic UIs getting generated on the fly. We're starting
*  to see that a little bit already, but I don't think open AI is going to say what we need to do
*  is create like a UI where people can edit these graph things. If possibly you could do that,
*  GPTs don't really give you the ability to create like custom editor experiences yet anyway.
*  So for now, if you want to have something like that, I have to bring it to a different app.
*  But increasingly these are out there as well. They just use chat GPT and just a renderer.
*  So I had the AI doing all the syntax and then the renderer showing me what it actually is. And then
*  going back and continuing the dialogue with chat GPT. I think you're right. Like I could see a world
*  where they let developers build their own renderers inside of chat GPT, not for like really serious
*  stuff. I think like dabble in half one time or make a little video or whatever that like having
*  something in the interface so that you can do it in there. Like a rough thing is really helpful.
*  But then, yeah, I think you're right. There will have to be other pro tools for people that all
*  they do all day is make graphs that are not inside of chat GPT. So here's another one.
*  This is recent episode in my life where I had to admit defeat after 10 years of swearing that I
*  would not replace my car until the replacement was self-driving. Wow. And we're not quite there. So
*  I finally and I've had three kids in the meantime, so I finally had to break down and get a mini man.
*  Like many parents of young kids, I'm like, what my kids do is they really depreciate stuff pretty
*  quickly. So I was like, I think I'll get a used mini man because if I get a new one, it's going
*  to be pretty used pretty quick anyway. So let me just look at what is out there. Now, anybody who's
*  ever shopped for a used car knows that it's a total jungle, right? And the car dealer websites
*  are terrible. What features they have is a huge question. And what you end up encountering very
*  quickly is these trim levels, which if you're not like a car head, you may not even know what that is,
*  but that is the sort of, you've got your make, which is the brand of the car, your Chevrolet or
*  your Toyota or whatever. You've got your model, which is the kind of car. And then the Dodge
*  caravan is the make and model. And then you've got this trim, which is often just like a couple
*  letters or whatever. It's like the XRT or the SRT or the L limited or whatever. They just have all
*  these like little, and these are packaged levels, right? What features, what upsells have been
*  included? Does it have a sunroof? Does it have a screen in the back that drops down out of the
*  ceiling for the kids or whatever, right? And it's just a jungle to even try to figure out
*  what those things have, what levels there are and what those things have. So this is perplexity,
*  which is a great compliment to Chatchie PT. It is more specifically focused on answering questions.
*  So in this way, it's a more direct rival to a Google search. It's not so much meant to be like
*  a brainstorming partner. They really aim for accurate answers to concrete questions, do a
*  phenomenal job on it. So here I had a number of runs of this as well, different kinds of questions
*  or whatever. But okay, these minivans that are like not super old, but old, pretty cheap. What do they
*  have? What do they not have? And this would have taken, I don't even know if I had really tried,
*  I wouldn't have done it, right? This is one of those things that you just, I wouldn't do. But if
*  you had set out to go collate, okay, here's all the makes and the models and the trims and what they
*  have, you're going to be in like user manuals or something. I don't even know really where that
*  information is stored in ground truth. But just in asking that question, I was able to get the
*  trim levels for all of the different brands for this window of time and just easily get a handle
*  now that I could reference back to, okay, this one on this dealer site, it doesn't have any pictures,
*  it doesn't say anything, but it does say for example, oh, it's an, it's a SXT. Okay, cool.
*  Now I can at least know that is the second of however many trim levels or whatever. So the SE,
*  that's your top one, your SXT, that's your, you can imagine, right? Trying to sort this out on your
*  own. And then you get the AVP slash SE. Who comes up with this stuff? It's ridiculous, but super
*  useful if you're like, I don't want to drive across Metro Detroit to go look at this minivan
*  if it doesn't have something that I really cared about. And the things that I were zeroed in on
*  were like fairly basic safety features. I wanted the blind spot detection and the backup camera.
*  So there were other questions too, like when did USB charging get introduced into
*  cars in general? I didn't know the answer to that. I'm old enough to remember when you had to plug
*  the thing into the lighter and I didn't want that. So I don't want a car that's that old where I have
*  to use the lighter outlet anymore. I want a car that's at least into the like USB charger era,
*  but when did the USB charger era begin for cars? That was another one that perplexity was able to
*  answer. And it is so good. I think this is about to be a huge trend if I had to guess,
*  because I've been a big fan of the SAP for a while. I had the CEO Arvind on the cognitive
*  revolution twice and they ship super fast. They win head to head comparisons for answer accuracy,
*  but product itself is super fast. It's got great UI with these sources and others starting to
*  become more multimodal with images as well, which is relatively new. We're just a great experience
*  all the way around. And I see it as like setting a new standard for answers that are like, I started,
*  I'm starting to use the term per perplexity to say, I'm not sure this is necessarily rock solid
*  ground truth. Like perplexity is not always right, but it's the most accurate AI tool.
*  It's usually right. In my experience, you might be able to find something here that is wrong,
*  but everything I ended up fact checking turned out to be true. And so I think there's this kind of
*  very interesting, good enough for practical purposes standard where I don't necessarily
*  need it to be a hundred hundred percent accurate for it to be very useful.
*  And I would make my decisions. Did I trust it enough, for example, to be confident that there
*  was in fact going to be a USB charger in the car that I went to go look at? Yes. And in fact,
*  it was correct about that. And so I have this kind of per perplexity standard of verification
*  in my mind now where I'm like, yeah, it's in many situations. It's like good enough to act on.
*  I wouldn't make life and death decisions without more fact checking, but I don't even need to
*  follow these links in most cases now for something like this. I'll trust it. And it's an emerging
*  standard in the family as well. My wife asks, do we really have to get a car that's that old?
*  Do they have this? Do they have that? And I was able to ask perplexity and send her like, yep,
*  it should have a backup camera per perplexity. It should have a USB charger. It should have the
*  blind spot detection. And it's an incredible time saver. I think a worthy alternative to even
*  something like a wire cutter, which has been the standard that my wife has used for a long time.
*  But obviously that's an editorial approach where you can't just ask any question you want to ask.
*  Here, you can ask any question you want to ask. And I think you do get something oftentimes
*  that is like a worthy rival even to a much more editorial product.
*  That makes perfect sense. It reminds me of wire cutter reminds me of there are all those sites
*  that are like Cora, but it's like for this new generation where no one had to think previously
*  to ask this particular question and it can just gather and answer the question for you
*  immediately. And I think that's so it's so powerful. Like it's really starting to click for me
*  when and how I might, I might use it. There are so many questions I have this for. I'm like,
*  I basically want to get to the best answer for a fact based question more or less.
*  And I'm so lazy. I really don't want to do all the research and chat GBT will kind of like,
*  it'll do one search and then sort of crib the first article. And this feels a lot better than that.
*  Yeah, it's really good. It's faster than chat GBT on the browsing side. So you're getting to answer
*  notably faster and marginally more accurate, just more the sort of answer that I want.
*  A lot of times, like I've had a couple of instances where I tried this same thing with chat GBT
*  and I was able to get there, but it was like slower on the browse. Didn't give me the full answer.
*  The first time I was like, no, but I need a little more. And then I was able to get over the hump and
*  get there. But this was definitely just a faster, cleaner experience that I do believe is a bit more
*  accurate as well. It goes to show that there are different roles that you want AI to play.
*  And I think there is, it's interesting. There's forces pushing both ways, right? What makes the
*  AIs so compelling is that they're extremely general purpose. And it seems like there is
*  something, there is like a fundamental reality that they get really powerful at scale and to
*  scale, they have to be the general purpose. And that kind of comes as a package.
*  But here the scope has been narrowed. And there are a lot of things that chat GBT does where people
*  that this is not trying to do for people. And in its specialization, it does seem to be achieving
*  higher heights in the domain that it really attempts to be best in. So I definitely recommend
*  perplexity a lot. And I'm just old enough to remember when people were for saying that they
*  were Googling it. And this has a similar vibe to me where it's a standard that I think people can
*  comfortably socially transact on and feel like they're pretty selling for us.
*  I love this. Like you're using it to build stuff. We're also really using it to
*  fuel your curiosity. And I'm curious, like, you know, before we wrap up, what are you excited
*  about now? What are you thinking about right now? Like what's on your radar that you think
*  people should be paying attention to in chat, chat, chat, maybe specifically, but like broadly
*  in AI over the next couple of years? Boy, broadly in AI over the next couple of years,
*  I think almost anything's possible. I take the leaders of the field pretty much at their word
*  in terms of being honest reflections of their expectations. And you listen to what Sam Altman
*  thinks might happen over the next couple of years. You listen to what Dario Amadei from Anthropic
*  thinks might happen over the next couple of years. And we are potentially looking at something that
*  is superhuman in very substantial and meaningful ways. I think there's a lot of kind of conflation
*  and talking past one another when people try to analyze this. And I do think it's important to
*  say you can be superhuman in very consequential ways without being like omnipotent or infallible.
*  And I think there's actually quite a lot of space right between like human performance and
*  omnipotence or infallibility. And I kind of expect that AI is going to land there
*  for a lot of different things over the next couple of years. So I think the value of the kinds of
*  things that we will be engaging with it for is only headed up just a recent result from
*  Google DeepMind on using their best language models for differential diagnosis was an extremely
*  striking result. This team has been on an absolute terror. It was only maybe like a year ago that
*  they first got a language model to like hit passing level on medical licensing tests,
*  which, hey, that's crazy. But you can just kind of say, well, it's a test. It's more structured.
*  The real world is messy and they're only passing. You wouldn't want a doctor that's just merely
*  passing. Okay, guess what? We didn't stop there. Next thing you know, it was hitting expert level
*  performance on the test. Next thing you know, it's, they've added multimodality and it can now
*  do a pretty good job of reading your x-rays and other tissue slides. And again, is it perfect?
*  No, it would be probably on the lower end of what the actual human radiologist could do.
*  Right. Although even there, it was like 60, 40, I think. I think it was like 60% to 40%
*  that the human radiologist was beating the AI radiologist. So it's okay. That's a pretty
*  narrow margin. Obviously we're not done. The current thing is taking case studies out of
*  medical journals, case studies being like extreme hard to figure out cases, right? When a case gets
*  reported in a medical journal, that's because this case is thought to be highly instructive,
*  right? It was a confusing situation. It's an unfamiliar combination of symptoms or what have
*  you. So they don't publish just the routine cold, right? In the journals. So they take these
*  case studies out of journals and they had a study of comparing AI's effectiveness at,
*  during the differential diagnosis versus human with access to AI. And AI was the best by like
*  a significant margin. The human alone was last. And so they, in their kind of presentation of this,
*  they're very modest and they take almost like a, in my view, almost like a two grounded, willfully
*  bearing the lead almost at times it seems. And what one of the main conclusions of the paper was,
*  we need better interfaces so that doctors can take better advantage of this. But it was like,
*  to me that's yes, that's one lesson I would take away from this paper. But the other lesson is that
*  the AI is getting it right like twice as often as the human clinician, like 60% to 30%. That's
*  another big lesson too, that I take away from a lot of these things. We don't often measure human
*  performance. We think because we've lived in a world for a long time, we're like a human doctor,
*  human, we know that like some are better than others, but we look at that as a standard that
*  there's a human doctor and their license and they're supposed to be good. But like, how often do they
*  get the right diagnosis on this? It turned out in this particular data set, it was in the ballpark
*  of 30%. So there's a lot of room for improvement. And you could perhaps say, what's the best doctor
*  in the world do? That best doctor in the world, I'm sure is a lot better, maybe even better than
*  the 60% that their language model was able to do. But you probably can't access that person.
*  We are apparently headed for a world where you should be able to access that AI doctor. And if
*  it's a 2x better performance on such a challenging task as differential diagnosis, that I think we're
*  headed for a world of radical access to expertise, which I think is going to be at unbelievably low
*  prices, which I think is going to be a transformative force in society, right? It's going to be one of
*  the greatest blows ever struck for equality of opportunity, equality of access in many ways.
*  It's also going to change a lot of market dynamics and change what wages can be commanded for
*  different kinds of services. I'm excited about that. I also think it probably is going to be
*  fairly disruptive and it probably is going to become more and more political. I think that the
*  upside of that, I think is pretty clear and really extremely compelling. So I hope we do get to
*  actually enjoy the fruits of that future. One other thing I'll say is just, I don't think we are at
*  the transformer is not the end of history. That's a chat GPT is not the end of history. This sort of
*  no memory AI, just this last week or two, we've seen a flurry of activity in the state space model
*  architecture. And again, it's been reported, the headlines, if you're on Twitter and seeing this
*  stuff, it's, Hey, there's a new thing that might even be better than the transformer. It might be
*  a transformer successor. It might be a transformer alternative. It might be a transformer replacement.
*  It has some nice properties that the transformers don't have better long-term memory, better scaling,
*  better speed, better throughput. Maybe we just all flip over from one to the other. And if the
*  transformer was the old thing, this is the new thing. But I strongly suspect that what we are
*  going to see is a mixture of these architectures where just like in the brain, we obviously don't
*  have just one single unit of the brain that gets repeated over and over again. We have a lot of
*  different modules, including some that do get repeated. It seems like we're almost for sure
*  headed for AIs that are like composites of different kinds of architectures that bring their
*  own strengths and weaknesses in information processing to the table, such that as much as
*  this has been a shocking amount of progress to get to GPT-4 from GPT-2 just four years ago,
*  I have to say, I think the next few years are going to bring at least as much more change.
*  And it's going to be a wild ride. It's exciting. It's inspiring. I'm excited for the future. And I
*  really appreciate you taking the time to share your thoughts and show us how you use ChachiBT.
*  And I'd love to have you back and see where we are, see what new stuff comes up on the horizon.
*  So, yeah, thank you. I appreciate the opportunity to end this. It's been a lot of fun and I
*  definitely learned some things and was inspired to go chase down a few more use cases as well.
*  So hopefully next time I'll have some better custom instructions and a little bit better
*  track record in the brainstorming department. I think it's been a great exchange. So that sounds
*  great. Yeah. Thanks a lot. It is both energizing and enlightening to hear why people listen and
*  learn what they value about the show. So please don't hesitate to reach out via email at tcr
*  at turpentine.co or you can DM me on the social media platform of your choice.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it and I recommend you use it to use Cogrev to get a 10% discount.
