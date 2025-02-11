---
Date Generated: October 13, 2024
Transcription Model: whisper medium 20231117
Length: 8944s
Video Keywords: ['Cursor Team', 'alex friedman', 'lex ai', 'lex debate', 'lex freedman', 'lex fridman', 'lex friedman', 'lex interview', 'lex lecture', 'lex mit', 'lex podcast', 'lex transcript']
Video Views: 375786
Video Rating: None
Video Description: Aman Sanger, Arvid Lunnemark, Michael Truell, and Sualeh Asif are creators of Cursor, a popular code editor that specializes in AI-assisted programming.
Thank you for listening ❤ Check out our sponsors: https://lexfridman.com/sponsors/ep447-sb
See below for timestamps, transcript, and to give feedback, submit questions, contact Lex, etc.

*Transcript:*
https://lexfridman.com/cursor-team-transcript

*CONTACT LEX:*
*Feedback* - give feedback to Lex: https://lexfridman.com/survey
*AMA* - submit questions, videos or call-in: https://lexfridman.com/ama
*Hiring* - join our team: https://lexfridman.com/hiring
*Other* - other ways to get in touch: https://lexfridman.com/contact

*EPISODE LINKS:*
Cursor Website: https://cursor.com
Cursor on X: https://x.com/cursor_ai
Anysphere Website: https://anysphere.inc/
Aman's X: https://x.com/amanrsanger
Aman's Website: https://amansanger.com/
Arvid's X: https://x.com/ArVID220u
Arvid's Website: https://arvid.xyz/
Michael's Website: https://mntruell.com/
Michael's LinkedIn: https://bit.ly/3zIDkPN
Sualeh's X: https://x.com/sualehasif996
Sualeh's Website: https://sualehasif.me/

*SPONSORS:*
To support this podcast, check out our sponsors & get discounts:
*Encord:* AI tooling for annotation &amp; data management.
Go to https://lexfridman.com/s/encord-ep447-sb
*MasterClass:* Online classes from world-class experts.
Go to https://lexfridman.com/s/masterclass-ep447-sb
*Shopify:* Sell stuff online.
Go to https://lexfridman.com/s/shopify-ep447-sb
*NetSuite:* Business management software.
Go to https://lexfridman.com/s/netsuite-ep447-sb
*AG1:* All-in-one daily nutrition drinks.
Go to https://lexfridman.com/s/ag1-ep447-sb

*OUTLINE:*
0:00 - Introduction
0:59 - Code editor basics
3:09 - GitHub Copilot
10:27 - Cursor
16:54 - Cursor Tab
23:08 - Code diff
31:20 - ML details
36:54 - GPT vs Claude
43:28 - Prompt engineering
50:54 - AI agents
1:04:51 - Running code in background
1:09:31 - Debugging
1:14:58 - Dangerous code
1:26:09 - Branching file systems
1:29:20 - Scaling challenges
1:43:32 - Context
1:48:39 - OpenAI o1
2:00:01 - Synthetic data
2:03:48 - RLHF vs RLAIF
2:05:34 - Fields Medal for AI
2:08:17 - Scaling laws
2:17:06 - The future of programming

*PODCAST LINKS:*
- Podcast Website: https://lexfridman.com/podcast
- Apple Podcasts: https://apple.co/2lwqZIr
- Spotify: https://spoti.fi/2nEwCF8
- RSS: https://lexfridman.com/feed/podcast/
- Podcast Playlist: https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
- Clips Channel: https://www.youtube.com/lexclips

*SOCIAL LINKS:*
- X: https://x.com/lexfridman
- Instagram: https://instagram.com/lexfridman
- TikTok: https://tiktok.com/@lexfridman
- LinkedIn: https://linkedin.com/in/lexfridman
- Facebook: https://facebook.com/lexfridman
- Patreon: https://patreon.com/lexfridman
- Telegram: https://t.me/lexfridman
- Reddit: https://reddit.com/r/lexfridman
---

# Cursor Team Future of Programming with AI  Lex Fridman Podcast #447
**Lex Fridman:** [October 06, 2024](https://www.youtube.com/watch?v=oFfVt3S51T4)
*  The following is a conversation with the founding members of the Cursor team,
*  Michael Trull, Swali Asif, Arvid Lundmark, and Aman Sanger.
*  Cursor is a code editor based on VS code that adds a lot of powerful features for AI-assisted coding.
*  It has captivated the attention and excitement of the programming and AI communities.
*  So I thought this is an excellent opportunity to dive deep into the role of AI in programming.
*  This is a super technical conversation that is bigger than just about one code editor.
*  It's about the future of programming and in general the future of human AI collaboration
*  in designing and engineering complicated and powerful systems.
*  This is the Lex Friedman podcast. To support it, please check out our sponsors in the description.
*  And now, dear friends, here's Michael, Swali, Arvid, and Aman.
*  All right, this is awesome. We have Michael, Aman, Swali, Arvid here from the Cursor team.
*  First up, big ridiculous question. What's the point of a code editor?
*  So the code editor is largely the place where you build software. And today, or for a long time,
*  that's meant the place where you text edit a formal programming language.
*  And for people who aren't programmers, the way to think of a code editor is like a really souped up
*  word processor for programmers. Where the reason it's souped up is code has a lot of structure.
*  And so the quote unquote word processor, the code editor, can actually do a lot for you
*  that word processors in the writing space haven't been able to do for people editing text there.
*  And so that's everything from giving you visual differentiation of the actual tokens in the code
*  so you can scan it quickly to letting you navigate around the code base,
*  like you're navigating around the internet with hyperlinks. You're going to definitions
*  of things you're using to error checking to catch rudimentary bugs.
*  And so traditionally, that's what a code editor has meant. And I think that what a code editor is
*  is going to change a lot over the next 10 years as what it means to build software maybe starts
*  to look a bit different. I think also a code editor should just be fun.
*  Yes, that is very important. That is very important. And it's actually sort of an underrated
*  aspect of how we decide what to build. Like a lot of the things that we build and then we try them
*  out, we do an experiment and then we actually throw them out because they're not fun. And so
*  a big part of being fun is like being fast a lot of the time. Fast is fun.
*  Yeah, that should be a t-shirt.
*  Fundamentally, I think one of the things that draws a lot of people to building stuff on computers
*  is this insane iteration speed where in other disciplines you might be sort of gatecapped by
*  resources or the ability, even the ability to get a large group together and coding is this amazing
*  thing where it's you and the computer and that alone you can build really cool stuff really quickly.
*  So for people to know Cursor is this super cool new editor that's a fork of VS Code.
*  It would be interesting to get your kind of explanation of your own journey of editors.
*  How did you, I think all of you were big fans of VS Code with Co-Pilot. How did you arrive to VS
*  Code and how did that lead to your journey with Cursor? Yeah, so I think a lot of us,
*  all of us were originally Vim users. Pure Vim. Pure Vim, yeah. No Neo Vim, just pure Vim in a
*  terminal. And at least for myself, it was around the time that Co-Pilot came out, so 2021, that
*  I really wanted to try it. So I went into VS Code, the only platform, the only code editor in which
*  it was available. And even though I really enjoyed using Vim, just the experience of Co-Pilot with
*  VS Code was more than good enough to convince me to switch. And so that kind of was the default
*  until we started working on Cursor. And maybe we should explain what Co-Pilot does. It's like a
*  really nice autocomplete. It suggests as you start writing a thing, it suggests one or two or three
*  lines how to complete the thing. And there's a fun experience in that, you know, like when you have
*  a close friendship and your friend completes your sentences, like when it's done well, there's an
*  intimate feeling. There's probably a better word than intimate, but there's a cool feeling of like,
*  holy shit, it gets me. And then there's an unpleasant feeling when it doesn't get you.
*  And so there's that kind of friction. But I would say for a lot of people, the feeling that it gets
*  me overpowers that it doesn't. And I think actually one of the underrated aspects of
*  get up Co-Pilot is that even when it's wrong, it's like a little bit annoying, but it's not that bad
*  because you just type another character and then maybe then it gets you or you type another character
*  and then it gets you. So even when it's wrong, it's not that bad. Yeah, you can sort of iterate
*  and fix it. I mean, the other underrated part of Co-Pilot for me sort of was just the first real
*  real AI product. So the first language model consumer product. So Co-Pilot was kind of like
*  the first killer app for LLMs. Yeah. And like the beta was out in 2021.
*  Right. Okay. So what's the origin story of Cursor? So around 2020, the scaling loss papers came out
*  from OpenAI. And that was a moment where this looked like clear predictable progress for the
*  field where even if we didn't have any more ideas, it looks like you could make these models a lot
*  better if you had more compute and more data. By the way, we'll probably talk for three to four
*  hours on the topic of scaling loss. Just to summarize, it's a paper and a set of papers and
*  set of ideas that say bigger might be better for model size and data size in the realm of machine
*  learning. It's bigger and better, but predictably better. Okay. That's another topic of conversation.
*  Yeah. So around that time, for some of us, there were like a lot of conceptual conversations about
*  what's this going to look like? What's the story going to be for all these different knowledge
*  worker fields about how they're going to be made better by this technology getting better?
*  And then I think there were a couple of moments where like the theoretical gains predicted
*  in that paper started to feel really concrete. And it started to feel like a moment where you
*  could actually go and not do a PhD if you wanted to work on, do useful work in AI. Actually felt
*  like now there was this whole set of systems, one could build that were really useful. And I
*  think that the first moment we already talked about a little bit, which was playing with the
*  early bit of Copel, like that was awesome and magical. I think that the next big moment where
*  everything kind of clicked together was actually getting early access to GPT-4. So it was sort of
*  end of 2022 was when we were tinkering with that model and the step-up capabilities felt enormous.
*  And previous to that, we had been working on a couple of different projects. We had been
*  because of Copilot, because of scaling odds, because of our prior interest in the technology,
*  we had been tinkering around with tools for programmers, but things that are very specific.
*  So we were building tools for financial professionals who have to work within a
*  Jupyter Notebook or playing around with, can you do static analysis with these models?
*  And then the stuff I've been doing before felt like, look, that really made concrete
*  the theoretical gains that we had predicted before. Felt like you could build a lot more
*  just immediately at that point in time. And also, if we were being consistent, it really felt like
*  this wasn't just going to be a point solution thing. This was going to be all of programming
*  was going to flow through these models. It felt like that demanded a different type of programming
*  environment, a different type of programming. And so we set off to build that sort of larger vision
*  around that. There's one that I distinctly remember. So my roommate is an IML Gold winner.
*  There's a competition in the US called the Putnam, which is sort of the IML for college
*  people. And it's this math competition. It's exceptionally good. So Sheng Tong and Amman,
*  I remember it sort of June of 2022, had this bet on whether the like 2024, June or July,
*  you were going to win a gold medal in the IML with like models.
*  IML is the International Math Olympiad.
*  Yeah, IML is International Math Olympiad. And so Arvid and I are both,
*  also competed in it. So it was sort of personal. And I remember thinking, Matt,
*  this is not going to happen. Even though I sort of believed in progress, I thought,
*  IML Gold, like Amman is just delusional. And to be honest, I was, to be clear, very wrong.
*  But that was maybe the most prescient bet in the group.
*  So the new results from DeepMind, it turned out that you were correct.
*  That's what the-
*  Well, it was technically not.
*  Technically incorrect, but one point away.
*  Amman was very enthusiastic about this stuff. And before, Amman had this like scaling loss t-shirt
*  that he would walk around with. It had the like charts and like the formulas on it.
*  So you like felt the AGI or you felt the scaling loss.
*  Yeah, I distinctly remember there was this one conversation I had with Michael where before,
*  I hadn't talked super deeply and critically about scaling laws. And he kind of posed the question,
*  why isn't scaling all you need? Or why isn't scaling going to result in massive gains in
*  progress? And I think I went through like the stages of grief. There is anger, denial,
*  and then finally at the end, just thinking about it, acceptance. And I think I've been quite
*  hopeful and optimistic about progress since. I think one thing I'll caveat is,
*  I think it also depends on like which domains you're going to see progress. Like math is a
*  great domain because especially like formal theorem proving, because you get this fantastic
*  signal of actually verifying if the thing was correct. And so this means something like RL
*  can work really, really well. And I think like you could have systems that are perhaps very
*  superhuman to math and still not technically have AGI.
*  Okay. So can we take it all the way to cursor? And what is cursor? It's a fork of VS code. And
*  VS code is one of the most popular editors for a long time. Like everybody fell in love with it.
*  Everybody left Vim. I left DMAX for it. Sorry. So unified in some fundamental way,
*  the developer community. And then you look at the space of things, you look at the scaling laws,
*  AI is becoming amazing. And you decided, okay, it's not enough to just write an extension for
*  VS code because there's a lot of limitations to that. If AI is going to keep getting better,
*  better, better, we need to really like rethink how the AI is going to be part of the editing
*  process. And so you decided to fork VS code and start to build a lot of the amazing features we'll
*  be able to talk about. But what was that decision like? Because there's a lot of extensions
*  including copilot of VS code that are doing sort of AI type stuff. What was the decision like to
*  just fork VS code? So the decision to do an editor seemed kind of self-evident to us for at least
*  what we wanted to do and achieve. Because when we started working on the editor, the idea was
*  these models are going to get much better. Their capabilities are going to improve,
*  and it's going to entirely change how you build software. Both in a, you will have big productivity
*  gains, but also radical and now like the active building software is going to change a lot.
*  And so you're very limited in the control you have over a code editor. If you're a plug-in to
*  an existing coding environment, and we didn't want to get locked in by those limitations,
*  we wanted to be able to just build the most useful stuff. Okay. Well, then the natural question is,
*  you know, VS code is kind of with copilot a competitor. So how do you win? Is it basically
*  just the speed and the quality of the features? Yeah. I mean, I think this is a space that is
*  quite interesting, perhaps quite unique, where if you look at previous tech waves,
*  maybe there's kind of one major thing that happened and unlock a new wave of companies.
*  But every single year, every single model capability or jump, you get model capabilities.
*  You now unlock this new wave of features, things that are possible, especially in programming.
*  And so I think in AI programming, being even just a few months ahead, let alone a year ahead,
*  makes your product much, much, much more useful. I think the cursor a year from now will need to
*  make the cursor of today look obsolete. And I think, you know, Microsoft has done a number of
*  fantastic things, but I don't think they're in a great place to really keep innovating and pushing
*  on this in the way that a startup can. Just rapidly implementing features.
*  And push, yeah, like and kind of doing the research experimentation necessary
*  to really push the ceiling. I don't know if I think of it in terms of features as I think of
*  it in terms of capabilities for programmers. It's that like, you know, as the new one model came out,
*  and I'm sure there are going to be more models of different types, like longer context and
*  maybe faster. Like there's all these crazy ideas that you can try and hopefully 10% of the crazy
*  ideas will make it into something kind of cool and useful. And we want people to have that sooner.
*  To rephrase it's like an underrated fact is we're making it for ourselves. When we started cursor,
*  you really felt this frustration that, you know, models, you could see models getting better.
*  But the COBOL experience had not changed. It was like, man, these guys, like the ceiling is
*  getting higher. Like, why are they not making new things? Like they should be making new things.
*  They should be like, where's all the alpha features? There were no alpha features. It was like,
*  I'm sure it was selling well. I'm sure it was a great business, but it didn't feel, I'm one of
*  these people that really want to try and use new things. And it was like, just there's no new thing
*  for like a very long while. Yeah. It's interesting. I don't know how you put that into words,
*  but when you compare cursor with Copilot, Copilot pretty quickly became, started to feel stale for
*  some reason. Yeah. I think one thing that I think helps us is that we're sort of doing it all in one
*  where we're developing the UX and the way you interact with the model. And at the same time as
*  we're developing, like how we actually make the model give better answers. So we're like
*  how you build up the prompt or like, how do you find the context and for a cursor tab,
*  like how do you train the model? So I think that helps us to have all of it, like sort of like the
*  same people working on the entire experience end to end. Yeah. It's like the person making the UI
*  and the person training the model like sit to like 18 feet away. So often the same person even. Yeah.
*  Often even the same person. So you can create things that are sort of not possible if you're
*  not, you're not talking, you're not experimenting. And you're using, like you said, cursor to write
*  cursor. Of course. Oh yeah. Yeah. Well, let's talk about some of these features. Let's talk about the
*  all-knowing, the all-powerful praise be to the tab, you know, autocomplete on stairways,
*  basically. So what, how does tab work? What is tab? To highlight and summarize at a high level,
*  I'd say that there are two things that cursor is pretty good at right now. There are other things
*  that it does. But two things that it helps programmers with. One is this idea of looking
*  over your shoulder and being like a really fast colleague who can kind of jump ahead of you and
*  type and figure out what you're, what you're going to do next. And that was the original idea behind,
*  that was kind of the kernel of the idea behind good autocomplete was predicting what you're going to
*  do next. But you can make that concept even more ambitious by not just predicting the characters
*  after your cursor, but actually predicting the next entire change. You're going to make the next
*  diff, next place you're going to jump to. And the second thing, cursor is pretty good out right now
*  too, is helping you sometimes jump ahead of the AI and tell it what to do and go from instructions
*  to code. And on both of those, we've done a lot of work on making the editing experience for those
*  things ergonomic and also making those things smart and fast. One of the things we really wanted
*  was we wanted the model to be able to edit code for us. That was kind of a wish and we had multiple
*  attempts at it before we had a sort of a good model that could edit code for you.
*  Then after we had a good model, I think there have been a lot of effort to make the inference fast for
*  having a good experience. And we've been starting to incorporate, I mean, Michael sort of mentioned
*  ability to jump to different places. And that jump to different places, I think, came from a feeling
*  of once you accept an edit, it's like, man, it should be just really obvious where to go next.
*  It's like I made this change, the model should just know that the next place to go to is
*  18 lines down. If you're a WIM user, you could press 1-8-jj or whatever. But why am I doing this?
*  The model should just know it. So the idea was you just press tab, it would go 18 lines down,
*  and then it would show you the next edit and you would press tab. So as long as you could
*  keep pressing tab. And so the internal competition was how many tabs can we make the one press.
*  Once you have the idea, more sort of abstractly, the thing to think about is how are the edits
*  zero entropy. So once you've sort of expressed your intent and the edit is, there's no new bits
*  of information to finish your thought, but you still have to type some characters to make the
*  computer understand what you're actually thinking. Then maybe the model should just sort of read your
*  mind and all the zero entropy bits should just be tabbed away. That was sort of the abstract version.
*  There's this interesting thing where if you look at language model loss on different domains,
*  I believe the bits per byte, which is kind of character normalized loss for code, is lower
*  than language, which means in general, there are a lot of tokens in code that are super predictable,
*  a lot of characters that are super predictable. And this is, I think, even magnified when you're
*  not just trying to autocomplete code, but predicting what the user is going to do next in
*  their editing of existing code. And so the goal of cursor tap is let's eliminate all the low entropy
*  actions you take inside of the editor. When the intent is effectively determined,
*  let's just jump you forward in time, skip you forward.
*  Well, what's the intuition and what's the technical details of how to do next
*  cursor prediction? That jump, that's not so intuitive, I think, to people.
*  Yeah. I think I can speak to a few of the details on how to make these things work.
*  They're incredibly low latency, so you need to train small models on this task. In particular,
*  they're incredibly pre-filled token hungry. What that means is they have these really,
*  really long prompts where they see a lot of your code, and they're not actually
*  generating that many tokens. And so the perfect fit for that is using a sparse model, meaning an MOE
*  model. So that was kind of one breakthrough we made that substantially improved its performance
*  at longer context. The other being a variant of speculative decoding that we built out called
*  speculative edits. These are two, I think, important pieces of what make it quite high quality
*  and very fast. Okay. So MOE mixture of experts,
*  the input is huge, the output is small. Yeah.
*  Okay. So what else can you say about how to make these caching play a role?
*  Caching plays a huge role. Because you're dealing with this many input tokens,
*  if every single keystroke that you're typing in a given line, you had to rerun the model on all of
*  those tokens passed in, you're just going to one, significantly degrade latency, two, you're going to
*  kill your GPUs with load. So you need to design the actual prompts used for the model such that
*  they're caching aware. And then, yeah, you need to reuse the KV cache across requests
*  just so that you're spending less work, less compute.
*  Again, what are the things that Tab is supposed to be able to do in the near term?
*  Just to sort of linger on that. Generate code, fill empty space, also edit code across multiple
*  lines. And then jump to different locations at the same file. And then like...
*  Hopefully jump to different files also. So if you make an edit in one file and
*  maybe you have to go to another file to finish your thought, it should go to the second file also.
*  The full generalization is like next action prediction. Sometimes you need to run a command
*  in the terminal and it should be able to suggest the command based on the code that you wrote to.
*  Or sometimes you actually need to... It suggests something, but it's hard for you to know if it's
*  correct because you actually need some more information to learn. You need to know the type
*  to be able to verify that it's correct. And so maybe it should actually take you to a place
*  that's like the definition of something and then take you back so that you have all the
*  requisite knowledge to be able to accept the next completion. So providing the human the knowledge.
*  Yes. Right. Can you integrate... I just got to know a guy named PrimeGen who I believe
*  has an SSH... You can order coffee via SSH. Oh yeah. We did that. We did that.
*  So can that also the model do that? Feed you and provide you with caffeine? Okay,
*  so that's the general framework. Yeah. And the magic moment would be if...
*  It is... Programming is this weird discipline where sometimes the next five minutes... Not
*  always, but sometimes the next five minutes of what you're going to do is actually predictable
*  from the stuff you've done recently. And so can you get to a world where that next five minutes
*  either happens by you disengaging and it taking you through, or maybe a little bit more of just
*  you seeing next step what it's going to do and you're like, okay, that's good. That's good.
*  That's good. That's good. That's good. And you can just sort of tap, tap, tap through these big
*  changes. As we're talking about this, as you mentioned, one of the really cool and noticeable
*  things about Cursor is that there's this whole diff interface situation going on. So the model
*  suggests with the red and the green of like, here's how we're going to modify the code.
*  And in the chat window, you can apply and it shows you the diff and you can accept the diff.
*  So maybe can you speak to whatever direction of that? We'll probably have like four or five
*  different kinds of diffs. So we have optimized the diff for the autocomplete. So that has a
*  different diff interface then when you're reviewing larger blocks of code. And then we're trying to
*  optimize another diff thing for when you're doing multiple different files. And sort of at a high
*  level, the difference is for when you're doing autocomplete, it should be really, really fast to
*  read. Actually, it should be really fast to read in all situations. But in autocomplete, it's sort
*  of, you're really like your eyes focused in one area. You can't be in too many, the humans can't
*  look in too many different places. So you're talking about on the interface side? On the
*  interface side. So it currently has this box on the side. So we have the current box. And if you
*  try to delete code in some place and tries to add other code, it tries to show you a box on the side.
*  You can maybe show it if we pull it up on cursive.com. This is what we're talking about.
*  So that box, it was like three or four different attempts at trying to make this thing work.
*  Where first the attempt was like these blue crossed out lines. So before it was a box on the side,
*  it used to show you the code to delete by showing you like Google Doc style. You would see like a
*  line through it. Then you would see the new code. That was super distracting. And then we tried
*  many different, you know, there was sort of deletions, there was trying to red highlight.
*  Then the next iteration of it, which is sort of funny, you would hold the on Mac, the option
*  button. So it would sort of highlight a region of code to show you that there might be something
*  coming. So maybe in this example, like the input and the value would get, would all get blue.
*  And the blue would to highlight that the AI had a suggestion for you.
*  So instead of directly showing you the thing, it would show you that the AI, it would just hint
*  that the AI had a suggestion. And if you really wanted to see it, you would hold the option button
*  and then you would see the new suggestion. Then if you release the option button,
*  you would then see the original code. So that's by the way, that's pretty nice,
*  but you have to know to hold the option button. Yeah. So by the way, I'm not a Mac user, but I got
*  it. It was a button, I guess, you people have. It's, you know, it's again, it's just, it's just
*  non-intuitive. I think that's the, that's the key thing. And there's a chance this, this is also not
*  the final version of it. I am personally very excited for making a lot of improvements in this
*  area. Like we often talk about it as the verification problem where these diffs are great
*  for small edits, for large edits, or like when it's multiple files or something, it's actually
*  a little bit prohibitive to review these diffs. And so there are like a couple of different ideas
*  here. Like one idea that we have is, okay, you know, like parts of the diffs are important. They
*  have a lot of information and then parts of the diff are just very low entropy. They're like exam,
*  like the same thing over and over again. And so maybe you can highlight the important pieces
*  and then gray out the not so important pieces, or maybe you can have a model that
*  looks at the diff and sees, oh, there's a likely bug here. I will like mark this with a little
*  red squiggly and say like, you should probably like review this part of the diff. And ideas in
*  that vein, I think are exciting. Yeah, that's a really fascinating space of like UX design
*  engineering. So you're basically trying to guide the human programmer through all the things they
*  need to read and nothing more. Yeah. Like optimally. Yeah. And you want an intelligent
*  model to do it. Like currently diff algorithms are, they're like, they're just like normal
*  algorithms. There is no intelligence. There's like intelligence that went into designing the
*  algorithm, but then there's no like, you don't care if it's about this thing or this thing,
*  as you want a model to do this. So I think the general question is like,
*  Matt, these models are going to get much smarter. As the models get much smarter,
*  the changes they will be able to propose are much bigger. So as the changes get bigger and bigger
*  the humans have to do more and more and more verification work. It gets more and more and more
*  hard. Like it's just, you need, you need to help them out. It sort of, I don't want to spend all my
*  time reviewing code. Can you say a little more across multiple files? Yeah. I mean, so
*  get up, try solve this right with code review. When you're doing code review, you're reviewing
*  multiple deaths across multiple files. But like Arvid said earlier, I think you can do much better
*  than code review. You know, code review kind of sucks. Like you spend a lot of time trying
*  to grok this code that's often quite unfamiliar to you. And it often like doesn't even actually
*  catch that many bugs. And I think you can significantly significantly improve that review
*  experience using language models, for example, using the kinds of tricks that are described
*  maybe pointing you towards the regions that actually matter.
*  I think also if the code is produced by these language models, and it's not produced by someone
*  else, like the code review experience is designed for both the reviewer and the person that produced
*  the code. In the case where the person that produced the code is a language model, you don't
*  have to care that much about their experience. And you can design the entire thing around the
*  reviewers such that the reviewers job is as fun as easy as productive as possible.
*  And I think that that feels like the issue with just kind of naively trying to make
*  these things look like code review. I think you can be a lot more creative
*  and push the boundary on what's possible. Just one one idea there is I think ordering matters.
*  Generally, when you review a PR, you have this list of files and you're reviewing them from top
*  to bottom. But actually, you actually want to understand this part first, because that came
*  logically first, and then you want to understand the next part. And you don't want to have to
*  figure out that yourself. You want a model to guide you through the thing.
*  And is the step of creation going to be more and more natural language is the goal versus with
*  I think sometimes I don't think it's going to be the case that all of programming will be natural
*  language. And the reason for that is, you know, if I'm programming with swallow and swallow is at the
*  computer and the keyboard, and sometimes if I'm like driving, I want to say to swallow, Hey,
*  like implement this function, and that that works. And then sometimes it's just so annoying to
*  explain to swallow what I want him to do. And so I actually take over the keyboard and I show him,
*  I write like part of the example, and then it makes sense. And that's the easiest way to
*  communicate. And so I think that's also the case for AI, like sometimes the easiest way to communicate
*  with AI will be to show an example, and then it goes and does the thing everywhere else. Or sometimes
*  if you're making a website, for example, the easiest way to show to the AI what you want is not
*  to tell it what to do, but you know, drag things around or draw things. And, yeah, and like maybe
*  eventually we will get to like brain machine interfaces or whatever, and kind of like understand
*  what you're thinking. And so I think natural language will have a place, I think it will not
*  definitely not be the way most people program most of the time. I'm really feeling the AGI with this
*  editor. It feels like there's a lot of machine learning going on underneath. Tell me about some
*  of the ML stuff that makes it all work. Recursor really works via this ensemble of custom models
*  that we've trained alongside, you know, the frontier models that are fantastic at the reasoning intense
*  things. And so cursor tab, for example, is a great example of where you can specialize this model to
*  be even better than even frontier models. If you look at evals on the task we set it at the other
*  domain, which it's kind of surprising that requires custom models, but it's kind of necessary and works
*  quite well is in apply. So I think these models are like the frontier models are quite good at
*  sketching out plans for code and generating like rough sketches of like the change, but actually
*  creating diffs is quite hard for frontier models from your training models.
*  Like you try to do this with sonnet with one, any frontier model, and it really messes up stupid
*  things like counting line numbers, especially in super, super large files. And so what we've done
*  to alleviate this is we let the model kind of sketch out this rough code block that indicates
*  what the change will be. And we train a model to then apply that change to the file. And we should
*  say that apply is the model looks at your code. It gives you a really damn good suggestion of what
*  new things to do. And the seemingly for humans trivial step of combining the two,
*  you're saying is not so trivial. Contrary to popular perception,
*  it is not a deterministic algorithm. Yeah, I think like you see shallow copies of apply
*  elsewhere. And it just breaks like most of the time, because you think you can kind of try to
*  do some deterministic matching, and then it fails, you know, at least 40% of the time. And that just
*  results in a terrible product experience. I think in general, this this regime of you are
*  going to get smarter and smarter models. And like, so one other thing that apply lets you do is,
*  it lets you use fewer tokens with the most intelligent models. This is both expensive
*  in terms of latency for generating all these tokens and cost. So you can give this very,
*  very rough sketch, and then have your small models go and implement it because it's a much
*  easier task to implement this very, very sketched out code. And I think that this this regime will
*  continue where you can use smarter and smarter models to do the planning. And then maybe the
*  implementation details can be handled by the less intelligent ones, perhaps you'll have,
*  you know, maybe a one maybe it'll be even more capable of models, given an even higher level
*  plan that is kind of recursively applied by sauna and then the apply model.
*  Maybe we should we should talk about how to how to make it fast. Yeah,
*  I feel like yeah, fast is always an interesting detail.
*  Yeah, how do you make it fast? Yeah, so one big component of making it fast is speculative edits.
*  So speculative edits are a variant of speculative decoding. And maybe it'd be helpful to briefly
*  describe speculative decoding. With speculative decoding, what you do is you can kind of take
*  advantage of the fact that, you know, most of the time, and I'll add the caveat that it would be
*  when you're memory bound in language model generation. If you process multiple tokens at
*  once, it is faster than generating one token at a time. So this is like the same reason why if you
*  look at tokens per second with prompt tokens versus generated tokens, it's much, much faster
*  for prompt tokens. So what we do is instead of using what speculative decoding normally does,
*  which is using a really small model to predict these draft tokens that your larger model will
*  then go in and verify. With code edits, we have a very strong prior of what the existing code will
*  look like. And that prior is literally the same exact code. So you can do is you can just feed
*  chunks of the original code back into the into the model. And then the model will just pretty much
*  agree most of the time that, okay, I'm just going to spit this code back out. And so you can process
*  all of those lines in parallel. And you just do this with sufficiently many chunks. And then
*  eventually you'll reach a point of disagreement, where the model will now predict text that is
*  different from the ground truth original code, it'll generate those tokens, and then we kind of
*  will decide after enough tokens match the original code to re start speculating in chunks of code.
*  What this actually ends up looking like is just a much faster version of normal editing code. So
*  it's just like it looks like a much faster version of the model rewriting all the code. So just we
*  can use the same exact interface that we use for for diffs, but it will just stream down a lot faster.
*  And then and then the advantages that wireless streaming, you can just also be reviewing start
*  reviewing the code exactly before before it's done. So there's no no big loading screen. So
*  maybe that is part of the part of the advantage. So the human can start reading before the thing
*  is done. I think the interesting riff here is something like, like speculation is a fairly
*  common idea nowadays. It's like not only language models. I mean, there's obviously speculation in
*  CPUs. And there's like speculation for databases and speculation all over the place.
*  Let me ask this sort of the ridiculous question of which LM is better at coding, GPT, Claude,
*  who wins in the context of programming? And I'm sure the answer is much more nuanced because it
*  sounds like every single part of this involves a different model.
*  Yeah, I think there, there's no model that Pareto dominates others, meaning it is better in all
*  categories that we think matter. The categories being speed, ability to edit code ability to
*  process lots of code long context, you know, a couple of other things and kind of coding
*  capabilities. The one that I'd say right now is just kind of net best is sauna. I think this is a
*  consensus opinion are ones really interesting, and it's really good at reasoning. So if you get it
*  really hard, programming interview style problems, or lead code problems, it can do quite quite well
*  on them. But it doesn't feel like it kind of understands your rough intent as well as sauna does.
*  Like, if you look at a lot of the other frontier models, one qualm I have is it feels like they're
*  not necessarily over I'm not saying they train and benchmarks, but they perform really well on
*  benchmarks, relative to kind of everything that's kind of in the middle. So if you tried in all these
*  benchmarks, and things that are in the distribution of the benchmarks, they're evaluated on, you know,
*  they'll do really well. But when you push them a little bit outside of that, so on, it's I think the
*  one that that kind of does best at kind of maintaining that same capability, like you kind
*  of have the same capability in the benchmark as when you try to instruct it to do anything with
*  coding. What another ridiculous question is the difference between the normal programming
*  experience versus what benchmarks represent? Like, where do benchmarks fall short? Do you think when
*  we're evaluating these models? By the way, that's like a really, really hard, it's like, like,
*  critically important detail, like how how different like benchmarks are versus versus like real
*  coding, real coding. It's not interview style coding, it's you're doing these,
*  you know, humans are saying like half broken English sometimes. And sometimes you're saying
*  like, Oh, do what I did before. Sometimes you're saying, you know, go add this thing, and then do
*  this other thing for me, and then make this UI element. And then, you know, it's just like a
*  lot of things are sort of context dependent, you really want to like understand the human and then
*  do do what the human wants, as opposed to sort of this, maybe the way to put it is sort of abstractly
*  is the interview problems are very well specified. They lean a lot on specification, while the
*  human stuff is less specified. Yeah, I think that this this benchmark question is both complicated
*  by what I just mentioned. And then also to what I'm on was getting into is that even if you like,
*  you know, there's this problem of like the skew between what can you actually model in a benchmark
*  versus real programming. And that can be sometimes hard to encapsulate, because it's like, real
*  programming is like, very messy. And sometimes things aren't super well specified, what's correct
*  or what isn't. But then it's also doubly hard because of this public benchmark problem. And
*  that's both because public benchmarks are sometimes kind of hill climbed on, then it's like really
*  really hard to also get the data from the public benchmarks out of the models. And so for instance,
*  like one of the most popular, like agent benchmarks, sweet bench is really, really contaminated,
*  and the training data of these foundation models. And so if you ask these foundation models to
*  do a sweet bench problem, you actually don't give them the context of a code base, they can like
*  hallucinate the right file pass, they can hallucinate the right function names. And so
*  it's also just the public aspect of these things is tricky.
*  Yeah, like in that case, it could be trained on the literal issues or pull requests themselves.
*  And maybe the labs will start to do a better job, or they've already done a good job at
*  decontaminating those things. But they're not going to omit the actual training data of the
*  repository itself. Like these are all like some of the most popular Python repositories, like
*  SimPy is one example. I don't think they're going to handicap their models on SimPy and all these
*  popular Python repositories in order to get true evaluation scores in these benchmarks.
*  Yeah, I think that given the dirts in benchmarks, there have been like a few interesting crutches
*  that places that build systems with these models or build these models actually use to get a sense
*  of are they going in the right direction or not. And in a lot of places, people will actually just
*  have humans play with the things and give quality feedback on these. Like one or two of the
*  foundation model companies, they have people who that's a big part of their role. And internally,
*  we also qualitatively assess these models and actually lean on that a lot in addition to like
*  private emails that we have. It's like the vibe. The vibe benchmark, human benchmark. You pull in
*  the humans to do a vibe check. Yeah. Okay. I mean, that's kind of what I do, like just like
*  reading online forums and Reddit and X just like, well, I don't know how to properly load in
*  people's opinions because they'll say things like, I feel like Claude or GPT has gotten dumber or
*  something. They'll say, I feel like, and then I sometimes feel like that too. But I wonder if
*  it's the model's problem or mine. Yeah, with Claude, there's an interesting take I heard where
*  I think AWS has different chips. And I suspect they have slightly different numerics than
*  Nvidia GPUs. And someone speculated that Claude's degraded performance had to do with
*  maybe using the quantized version that existed on AWS Bedrock versus whatever was running on
*  Anthropics GPUs. I interview a bunch of people that have conspiracy theories. I'm glad
*  you spoke to this conspiracy theory. It's not like conspiracy theory as much as it is.
*  Humans are humans and there's these details and you're doing like this queasy amount of flops and
*  chips are messy and man, you can just have bugs. It's hard to overstate how hard bugs are to avoid.
*  What's the role of a good prompt in all this? You mentioned that benchmarks have really
*  structured well-formulated prompts. What should a human be doing to maximize success?
*  And what's the importance of what the humans... You wrote a blog post and
*  you called it prompt design. Yeah, I think it depends on which model you're using and all of
*  them are slightly different and they respond differently to different prompts. But I think
*  the original GPT-4 and the original sort of pre-debate models last year, they were quite
*  sensitive to the prompts and they also had a very small context window. And so we have all of these
*  pieces of information around the code base that would maybe be relevant in the prompt. You have
*  the docs, you have the files that you add, you have the conversation history. And then there's
*  a problem like how do you decide what you actually put in the prompt and when you have a limited
*  space. And even for today's models, even when you have long context, filling out the entire context
*  window means that it's slower. It means that sometimes the model actually gets confused and
*  some models get more confused than others. And we have this one system internally that we call
*  preempt, which helps us with that a little bit. And I think it was built for the era before where
*  we had 8,000 token context windows. And it's a little bit similar to when you're making a website.
*  You want it to work on mobile, you want it to work on a desktop screen, and you have this
*  dynamic information, which you don't have. For example, if you're designing a print magazine,
*  you know exactly where you can put stuff. But when you have a website or when you have a prompt,
*  you have these inputs and then you need to format them to always work. Even if the input is really
*  big, then you might have to cut something down. And so the idea was, okay, let's take some
*  inspiration. What's the best way to design websites? Well, the thing that we really like is
*  React and the declarative approach where you use JSX in JavaScript. And then you declare,
*  this is what I want. And I think this has higher priority or this has higher z-index than something
*  else. And then you have this rendering engine in web design. It's like Chrome, and in our case,
*  it's a preempt renderer, which then fits everything onto the page. And as you declare,
*  we decide what you want, and then it figures out what you want. And so we have found that to be
*  quite helpful. And I think the role of it has shifted over time, where initially it was to
*  fit to these small context windows. Now it's really useful because it helps us with splitting
*  up the data that goes into the prompt and the actual rendering of it. And so it's easier to
*  debug because you can change the rendering of the prompt and then try it on old prompts,
*  because you have the raw data that went into the prompt. And then you can see,
*  did my change actually improve it for this entire evil set?
*  So do you literally prompt with JSX?
*  Yes. So it kind of looks like React. There are components. We have one component that's
*  a file component, and it takes in the cursor. Usually there's one line where the cursor is
*  in your file, and that's probably the most important line because that's the one you're
*  looking at. And so then you can give priorities. So that line has the highest priority, and then
*  you subtract one for every line that is farther away. And then eventually when it's rendered,
*  it figure out how many lines can actually fit in the centers around that thing.
*  That's amazing.
*  Yeah. And you can do other fancy things where if you have lots of code blocks
*  from the entire code base, you could use retrieval and things like embedding and re-ranking scores to
*  add priorities for each of these components.
*  So should humans, when they ask questions, also try to use something like that? Would it be
*  beneficial to write JSX in the problem? Or the whole idea is it should be loose and messy?
*  I think our goal is kind of that you should just do whatever is the most natural thing for you.
*  And then our job is to figure out how do we actually retrieve the relative event
*  thing so that your thing actually makes sense.
*  Well, this is the discussion I had with Arvin of Perplexity. His whole idea is you should let
*  the person be as lazy as he wants. But that's a beautiful thing. But I feel like you're allowed
*  to ask more of programmers. So if you say just do what you want, I mean, humans are lazy. There's
*  a kind of tension between just being lazy versus like provide more as be prompted almost like the
*  system pressuring you or inspiring you to be articulate, not in terms of the grammar of the
*  sentences, but in terms of the depth of thoughts that you convey inside the prompts.
*  I think even as a system gets closer to some level of perfection, often when you ask the model for
*  something, you just are not not enough intent is conveyed to know what to do. And there are like a
*  few ways to resolve that intent. One is the simple thing of having models just ask you, I'm not sure
*  how to do these parts based on your query. Could you clarify that? I think the other could be maybe
*  if you there are five or six possible generations, given the uncertainty present in your query so
*  far, why don't we just actually show you all of those and let you pick them?
*  How hard is it to for the model to choose to speak, talk back?
*  Sort of versus that's hard to sort of like how to deal with the uncertainty.
*  Do I do I choose to ask for more information to reduce the ambiguity?
*  So I mean, one of the things we we do is, it's like a recent addition is
*  try to suggest files that you can add. So while you're typing, one can guess what the uncertainty
*  is, and maybe suggest that like, you know, maybe maybe you're writing your API.
*  And we can guess using the commits that you've made previously in the same file that
*  the client and the server is super useful. And there's like a hard technical problem of
*  how do you resolve it across all commits, which files are the most important given your current
*  prompt. And we're still sort of initial versions rolled out, I'm sure we can make it much more
*  accurate. It's very experimental. But then the ideas we show you like, do you just want to add
*  this file, this file, this file also to tell, you know, the model to edit those files for you?
*  Because if you're maybe you're making the API, like, you should also edit the client and the
*  server that is using the API and the other one resolving the API. And so that will be kind of
*  cool as both there's the phase where you're writing a prompt and there's before you even
*  click enter, maybe we can help resolve some of the uncertainty.
*  To what degree do you use agentic approaches? How you inspire agents?
*  We think agents are really, really cool. I think agents is like, it's like you resemble sort of
*  like a human. It's sort of like this, like you can kind of feel that it like you're getting closer
*  to AGI because you see a demo where it acts as a human would. And it's really, really cool. I think
*  agents are not yet super useful for many things. They, I think we're getting close to where they
*  will actually be useful. And so I think there are certain types of tasks where having an agent
*  would be really nice. Like I would love to have an agent. For example, if like we have a bug where
*  you sometimes can't command C and command V inside our chat input box. And that's a task
*  that's super well specified. I just want to say like in two sentences, this does not work.
*  Please fix it. And then I would love to have an agent that just goes off, does it. And then a day
*  later I come back and I reviewed the thing. You mean it goes, finds the right file. Yeah,
*  it finds the right files. It like tries to reproduce the bug. It like fixes the bug.
*  And then it verifies that it's correct. And this is, could be a process that takes a long time.
*  And so I think I would love to have that. And then I think a lot of programming, like there is often
*  this belief that agents will take over all of programming. I don't think we think that that's
*  the case because a lot of programming, a lot of the value is in iterating or you don't actually
*  want to specify something upfront because you don't really know what you want until you've seen an
*  initial version and then you want to iterate on that. And then you provide more information.
*  And so for a lot of programming, I think you actually want a system that's instant,
*  that gives you an initial version instantly back and then you can iterate super, super quickly.
*  What about something like that? We think came out, Replicant agent that does also like setting up
*  the development environment and solving software packages, configuring everything, configuring
*  the databases and actually deploying the app. Yeah. Is that also in the set of things you dream
*  about? I think so. I think that would be really cool for certain types of programming.
*  It would be really cool. Is that within scope of cursor? Yeah. We aren't actively working on it
*  right now, but it's definitely like, we want to make the programmers life easier and more fun.
*  And some things are just really tedious and you need to go through a bunch of steps and you want
*  to delegate that to an agent. And then some things you can actually have an agent in the background
*  while you're working. Like let's say you have a PR that's both back end and front end and you're
*  working on the front end and then you can have a background agent that doesn't work and figure out
*  kind of what you're doing. And then when you get to the backend part of your PR, then you have some
*  like initial piece of code that you can iterate on. And so that would also be really cool.
*  One of the things we already talked about is speed, but I wonder if we can just linger on
*  that some more in the various places that the technical details involved in making this thing
*  really fast. So every single aspect of cursor, most aspects of cursor feel really fast. Like I
*  mentioned, the apply is probably the slowest thing. And for me, from, I'm sorry, the pain.
*  It's a pain that we're feeling and we're working on fixing it.
*  Yeah. I mean, it says something that feels, I don't know what it is, like one second or two
*  seconds. That feels slow. That means that's actually shows that everything else is just
*  really, really fast. So is there some technical details about how to make some of these models,
*  how to make the chat fast, how to make the diffs fast? Is there something that just jumps to mind?
*  Yeah. I mean, so we can go over a lot of the strategies that we use. One interesting thing
*  is cache warming. And so what you can do is if, as the user is typing, you can have,
*  yeah, you're probably going to use some piece of context and you can know that before the user's
*  done typing. So, you know, as we discussed before, reusing the KV cache results in lower latency,
*  lower costs, cross requests. So as the user starts typing, you can immediately warm the cache with
*  like, let's say the current file contents. And then when they press enter, there's very few tokens,
*  it actually has to pre-fill and compute before starting the generation. This will significantly
*  lower TTFD. Can you explain how KV cache works? Yeah. So the way transformers work,
*  I like it. I mean, one of the mechanisms that allow transformers to not just independently,
*  like the mechanism that allows transformers to not just independently look at each token,
*  but see previous tokens are the keys and values to tension. And generally the way attention works
*  is you have at your current token, some query, and then you've all the keys and values of all
*  your previous tokens, which are some kind of representation that the model stores internally
*  of all the previous tokens in the prompt. And like by default, when you're doing a chat,
*  the model has to for every single token, do this forward pass through the entire model. That's a
*  lot of matrix multiplies that happen. And that is really, really slow. Instead, if you have already
*  done that and you stored the keys and values and you keep that in the GPU, then when I'm, let's say
*  I have sorted for the last end tokens, if I now want to compute the output token for the N plus
*  one token, I don't need to pass those first end tokens through the entire model because I already
*  have all those keys and values. And so you just need to do the forward pass through that last token.
*  Then when you're doing attention, you're reusing those keys and values that have been computed,
*  which is the only kind of sequential part or sequentially dependent part of the transformer.
*  Is there like higher level caching of like caching of the prompts or that kind of stuff?
*  I see. Yeah, there's other types of caching you can kind of do.
*  One interesting thing that you can do for cursor tab is you can basically predict ahead as if the
*  user would have accepted the suggestion and then trigger another request. And so then you've
*  cast, you've done a speculative, it's a mix of speculation and caching, right? Because you're
*  speculating what would happen if they accepted it. And then you have this value that is cash,
*  this suggestion. And then when they press tab, the next one would be the next one.
*  And then when they press tab, the next one would be waiting for them immediately.
*  It's a kind of clever heuristic slash trick that uses a higher level caching and can give
*  the, it feels fast despite there not actually being any changes in the model.
*  And if you can make the KV cache smaller, one of the advantages you get is like,
*  maybe you can speculate even more. Maybe you can guess here's the 10 things that
*  could be useful. Like, predict the next 10 and then like it's possible the user hits the
*  one of the 10. It's like much higher chance than the user hits like the exact one that you show them.
*  Maybe they type in other character and we sort of hit something else in the cache.
*  There's all these tricks where the general phenomena here is, I think it's also super
*  useful for RL is, you know, maybe a single sample from the model isn't very good.
*  But if you predict like 10 different things, turns out that one of the 10,
*  that's right, is the probability is much higher. There's these pass it K curves. And, you know,
*  part of RL, like what RL does is you can exploit this pass it K phenomena to make many different
*  predictions. And one way to think about this, the model sort of knows internally has like,
*  has some uncertainty over like which of the key things is correct,
*  or like which of the key things does the human want. So when we RL our, you know, cursor tab model,
*  one of the things we're doing is we're predicting which like which of the 100 different suggestions
*  the model produces is more amenable for humans. Like which of them do humans more like than other
*  things? Maybe maybe like, there's something where the model can predict very far ahead versus like
*  a little bit and maybe somewhere in the middle and, and just and then you can give a reward to
*  the things that humans would like more and sort of punish the things that it would like and sort
*  of then train the model to output the suggestions that humans would like more you have these like
*  RL loops that are very useful that exploit these pass it K curves. Um, maybe can go into even more
*  detail. Yeah, it's a little it is a little different than speed. But I mean, like, technically you tie
*  it back in because you can get away with the smaller model if you are earlier smaller model
*  and it gets the same performance as the bigger one. That's like and it's why I was mentioning stuff
*  about KB about reducing the size of your KB cache there are other techniques there as well. They're
*  really helpful for speed. So kind of back in the day, like all the way two years ago,
*  people mainly use multi-ed attention. And I think there's been a migration towards more
*  efficient attention schemes, like group query, or multi query attention. And this is really helpful
*  for them with larger batch sizes, being able to generate the tokens much faster. The interesting
*  thing here is this now has no effect on that time to first token pre fill speed. The thing this
*  matters for is now generating tokens. And why is that because when you're generating tokens,
*  instead of being bottlenecked by doing the super parallelizable matrix multiplies across all your
*  tokens, your bottleneck by how quickly it's for long context, with large batch sizes by how quickly
*  you can read those cache keys and values. And so then how that's memory bandwidth and how can we
*  make this faster, we can try to compress the size of these keys and values. So multi query attention
*  is the most aggressive of these. Where normally with multi head attention, you have some number of
*  quote unquote attention heads. And some number of kind of query, query heads, multi query just
*  preserves the query heads gets rid of all the key value heads. So there's only one kind of key value
*  head, and there's all the remaining query heads. With group query, you instead, you know, preserve
*  all the query heads. And then your keys and values are kind of, they're fewer heads for the keys and
*  values, but you're not reducing it to just one. But anyways, like the whole point here is you're
*  just reducing the size of your KV cache. And then there is MLA. Yeah, multi latent. That's a little
*  more complicated. And the way that this works is it kind of turns the entirety of your keys and values
*  across all your heads into this kind of one latent vector that is then kind of expanded
*  inference time. But MLA is from this company called DeepSeek. It's quite an interesting algorithm.
*  Maybe the key idea is sort of in both MQA and in other places, what you're doing is sort of reducing
*  the number like the number of KV heads. The advantage you get from that is, is, you know,
*  there's less of them. But maybe the theory is that you actually want a lot of different,
*  like you want each of the keys and values to actually be different. So one way to reduce
*  the size is you keep one big shared vector for all the keys and values, and then you have smaller
*  vectors for every single token. So that when you can store only the smaller thing, there's some sort
*  of like low rank reduction. And the low rank reduction, and at the end of the time, when you
*  eventually want to compute the final thing, remember that like your memory bound, which
*  means that like you still have some compute left that you can use for these things. And so if you
*  can expand the latent vector back out, and somehow like this is far more efficient because
*  just like you're reducing like, for example, maybe like you're using like 32 or something,
*  like the size of the vector that you're keeping. Yeah, there's perhaps some richness in having a
*  separate set of keys and values and query that kind of pairwise match up versus compressing that all
*  into one. And that interaction, at least. Okay, and all of that is dealing with being memory bound.
*  Yeah. And what I mean, ultimately, how does that map to the user experience?
*  Trying to get the Yeah, the two things that a map is, you can now make your cash a lot larger,
*  because you've less space allocated for the KV cache, you can maybe cash a lot more aggressively
*  and a lot more things. So you get more cash hits, which are helpful for reducing the time to first
*  token for the reasons that were kind of described earlier. And then the second being when you
*  start doing inference with more and more requests and larger and larger batch sizes,
*  you don't see much of a slowdown in as it's generating the tokens, the speed of that.
*  What it also allows you to make your prompt bigger, for sure.
*  Yeah, yeah. So like, the basic the size of your KV cache is both the size of all your prompts
*  multiplied by the number of prompts being processed in parallel. So you could increase
*  either those dimensions, right, the batch size, or the size of your prompts without degrading the
*  latency of generating tokens. Arva, you wrote a blog post shadow
*  workspace, iterating on code in the background. Yeah. So what's going on?
*  So to be clear, we want there to be a lot of stuff, stuff happening in the background. And
*  we're experimenting with a lot of things. Right now. We don't have much of that happening other
*  than like the cache warming or like, you know, figuring out the right context to that goes into
*  your command key prompts, for example. But the idea is, if you can actually spend computation in
*  the background, then you can help help the user maybe like, at a slightly longer time horizon than
*  just predicting the next few lines that you're going to make, but actually like in the next 10
*  minutes, what are you going to make? And by doing it in the background, you can spend more
*  computation doing that. And so the idea of the shadow workspace that we implemented, and we use
*  it internally for like experiments, is that to actually get advantage of doing stuff in the
*  background, you want some kind of feedback signal to give back to the model. Because otherwise,
*  like you can get higher performance by just letting the model think for longer. And so like,
*  O1 is a good example of that. But another way you can improve performance is by letting the model
*  iterate and get feedback. And so one very important piece of feedback when you're a programmer is
*  the language server, which is this thing it exists for most different languages. And there's like a
*  separate language server per language. And it can tell you, you know, you're using the wrong type
*  here, and then gives you an error, or it can allow you to go to definition and sort of understands
*  the structure of your code. So language servers are extensions developed by like, there's a
*  TypeScript language server developed by the TypeScript people, a Rust language server developed
*  by the Rust people, and then they all interface over the language server protocol to VS code.
*  So that VS code doesn't need to have all of the different languages built into VS code, but rather,
*  you can use the existing compiler infrastructure. For linting purposes?
*  It's for linting. It's for going to definition. And if we're like seeing the right types that
*  you're using. So it's doing like type checking also?
*  Yes, type checking and going to references. And that's like when you're working in a big project,
*  you kind of need that. If you don't have that, it's like really hard to code in a big project.
*  Can you say again how that's being used inside Cursor, the language server protocol communication
*  thing? So it's being used in Cursor to show to the programmer just like in VS code. But then the idea
*  is you want to show that same information to the models, the AI models. And you want to do that in
*  a way that doesn't affect the user because you want to do it in background. And so the idea behind
*  the shadow workspace was, okay, like one way we can do this is we spawn a separate window of Cursor
*  that's hidden. And so you can set this flag and electron is hidden. There is a window,
*  but you don't actually see it. And inside of this window, the AI agents can modify code however they
*  want, as long as they don't save it because it's still the same folder. And then can get feedback
*  from the lenders and go to definition and iterate on their code. So like literally run everything
*  in the background, like as if, right. Yeah. Maybe even run the code. So that's the eventual version.
*  Okay. That's what you want. And a lot of the blog post is actually about how do you make that happen
*  because it's a little bit tricky. You want it to be on the user's machine so that it exactly
*  mirrors the user's environment. And then on Linux, you can do this cool thing where you can actually
*  mirror the file system and have the AI make changes to the files. And it thinks that it's
*  operating on the file level, but actually that's stored in memory. And you can create this kernel
*  extension to make it work. Whereas on Mac and Windows, it's a little bit more difficult,
*  but it's a fun technical problem. So that's why. One maybe hacky, but interesting idea that I like
*  is holding a lock on saving. And so basically you can then have the language model kind of hold the
*  lock on saving to disk. And then instead of you operating in the ground truth version of the files
*  that are saved to disk, you actually are operating what was the shadow workspace before in these
*  unsaved things that only exist in memory that you still get linter errors for and you can code in.
*  And then when you try to maybe run code, it's just like there's a small warning that there's a lock.
*  And then you kind of will take back the lock from the language server if you're trying to do things
*  concurrently or from the shadow workspace. If you're trying to do things concurrently.
*  That's such an exciting future, by the way. It's a bit of a tangent, but like to allow a model to
*  change files is scary for people. But like, it's really cool to be able to just like let the agent
*  do a set of tasks and you come back the next day and kind of observe like it's a colleague
*  or something like that. Yeah. And I think there may be different versions of like runability
*  where for the simple things where you're doing things in the span of a few minutes on behalf of
*  the user as they're programming, it makes sense to make something work locally in their machine.
*  I think for the more aggressive things where you're making larger changes that take longer
*  periods of time, you'll probably want to do this in some sandbox remote environment.
*  And that's another incredibly tricky problem of how do you exactly reproduce or mostly reproduce
*  to the point of it being effectively equivalent for running code, the user's environment,
*  with this remote sandbox. I'm curious what kind of agency you want for coding.
*  Do you want them to find bugs? Do you want them to like implement new features? Like
*  what agency you want? So by the way, when I think about agents, I don't think just about coding.
*  I think so for the practice of this particular podcast, there's video editing and a lot of,
*  if you look in Adobe, a lot of there's code behind. It's very poorly documented code,
*  but you can interact with Premiere, for example, using code. And basically all the uploading,
*  everything I do on YouTube, everything is you could probably imagine. I do all of that through code
*  and including translation and overdubbing all of this. So I envision all of those kinds of tasks.
*  So automating many of the tasks that don't have to do directly with the editing.
*  So that, okay. That's what I was thinking about. But in terms of coding, I would be
*  fundamentally thinking about bug finding, like many levels of kind of bug finding and also
*  bug finding, like logical bugs, not logical, like spiritual bugs or something.
*  One's like sort of big directions of implementation, that kind of stuff.
*  Let's go pine and bug finding.
*  Yeah. I mean, it's really interesting that these models are so bad at bug finding
*  when just naively prompted to find a bug. They're incredibly poorly calibrated.
*  Even the smartest model.
*  Exactly. Even 01.
*  How do you explain that? Is there a good intuition?
*  I think these models are really strong reflection of the pre-training distribution. And I do think
*  they generalize as the loss gets lower and lower. But I don't think the loss is low enough such that
*  they're really fully generalizing in code. The things that we use these things for,
*  the frontier models that they're quite good at, are really code generation and question
*  answering. And these things exist in massive quantities in pre-training with all of the
*  code on GitHub on the scale of many, many trillions of tokens and questions and answers on things
*  like Stack Overflow and maybe GitHub issues. And so when you try to push into these things that
*  really don't exist very much online, like, for example, the cursor tap objective of predicting
*  the next edit, given the edits done so far, the brittleness kind of shows.
*  And then bug detection is another great example where there aren't really that many examples of
*  actually detecting real bugs and then proposing fixes. And the models just kind of really struggle
*  with it. But I think it's a question of transferring the model. Like in the same way that you get this
*  fantastic transfer from pre-trained models, just on code in general to the cursor tab objective,
*  you'll see a very, very similar thing with generalized models that are really good at
*  code to bug detection. It just takes like a little bit of kind of nudging in that direction.
*  Like to be clear, I think they sort of understand code really well. Like while they're being
*  pre-trained, the representation that's being built up, almost certainly, somewhere in the stream,
*  the model knows that maybe there's something sketchy going on. It sort of has some sketchiness,
*  but actually eliciting the sketchiness too. Part of it is that humans are really calibrated on which
*  bugs are really important. It's not just actually saying there's something sketchy. It's like,
*  is this sketchy trivial? Is this sketchy like you're going to take the server down?
*  Part of it is maybe the cultural knowledge of why is the staff engineer a staff engineer?
*  A staff engineer is good because they know that three years ago, someone wrote a really sketchy
*  piece of code that took the server down. And as opposed to maybe there's like, you just,
*  this thing is like an experiment. So like a few bugs are fine. You're just trying to experiment
*  and get the feel of the thing. And so if the model gets really annoying when you're writing
*  an experiment, that's really bad. But if you're writing something for super production, you're
*  like writing a database, right? You're writing code in Postgres or Linux or whatever. Like your
*  Linus Torvalds, it's sort of unacceptable to have even in that case. And just having the calibration
*  of like how paranoid is the user? But even then, like if you're putting in a maximum paranoia,
*  it still just like doesn't quite get it. Yeah.
*  I mean, but this is hard for humans too, to understand what, which line of code is important,
*  which is not. Like you, I think one of your principles on a website says if a code can do
*  a lot of damage, one should add a comment that say this line of code is dangerous.
*  And all caps repeated 10 times.
*  No, you say like for every single line of code inside the function, you have to,
*  and that's quite profound. That says something about human beings because the engineers move on,
*  even the same person might just forget how it can sync the Titanic, a single function. Like you
*  might not intuit that quite clearly by looking at the single piece of code.
*  Yeah. And I think that one is also partially also for today's AI models, where if you actually write
*  dangerous, dangerous, dangerous in every single line, like the models will pay more attention to
*  that and will be more likely to find bugs in that region. That's actually just straight up a really
*  good practice of labeling code of how much damage this can do.
*  Yeah. I mean, it's controversial. Some people think it's ugly.
*  Swallow.
*  Well, I actually think it's like, in fact, I actually think this is one of the things
*  I learned from Arvid is, you know, like I sort of aesthetically, I don't like it,
*  but I think there's certainly something where like it's useful for the models and,
*  and humans just forget a lot. And it's really easy to make a small mistake and cause like
*  bring down, you know, like just bring down the server and like, you like,
*  of course we like test a lot and whatever, but there's always these things that you have to be
*  very careful. Yeah. Like with just normal doc strings, I think people will often just skim it
*  when making a change and think, oh, I know how to do this. And you kind of really need to point it
*  out to them so that that doesn't slip through. Yeah. You have to be reminded that you can do a
*  lot of damage. That's like, we don't really think about that. Like, you think about, okay,
*  how do I figure out how this works? So I can improve it. You don't think about the other
*  direction that until we have formal verification for everything, then you can do whatever you want.
*  And you, you know, for certain that you have not introduced a bug if the proof pass,
*  but concretely, what do you think that future would look like?
*  I think people will just not write tests anymore. And the model will suggest, like you write a
*  function, the model will suggest a spec and you review the spec. And in the meantime, smart
*  reasoning model computes a proof that the implementation follows the spec. And I think
*  that happens for most functions. Do you think this gets at a little bit some of the stuff you were
*  talking about earlier with the difficulty of specifying intent for what you want with software?
*  Where sometimes it might be because the intent is really hard to specify, it's also then going
*  to be really hard to prove that it's actually matching whatever your intent is. Like you think
*  that spec is hard to generate? Yeah, or just like, for a given spec, maybe you can, I think there is
*  a question of like, can you actually do the formal verification? Like that's like, is that possible?
*  I think that there's like more to dig into there. But then also, even if you have the spec,
*  if you have this, but how do you have the spec is the spec written in natural language?
*  No, the spec would be formal. But how easy would that be?
*  So then I think that you care about things that are not going to be easily well specified in the
*  spec language. I see. I see. Yeah. Yeah. Maybe an argument against formal verification is all you
*  need. Yeah. The worry is there's this massive document. Replacing something like unit tests.
*  Sure. Yeah. Yeah. I think you can probably also evolve the spec languages to capture some of the
*  things that they don't really capture right now. I don't know. I think it's very exciting.
*  And you're speaking not just about like single functions. You're speaking about entire code
*  bases. I think entire code bases is harder, but that is what I would love to have. And I think
*  it should be possible. And because you can even, there's like a lot of work recently where you can
*  prove, formally verify down to the hardware. So like through the, you formally verify the C code,
*  and then you formula verify through the GCC compiler and then through the very log down to
*  the hardware. And that's like incredibly big system, but it actually works. And I think
*  big code bases are sort of similar in that they're like multi-layered system. And if you can
*  decompose it and formally verify each part, then I think it should be possible. I think the
*  specification problem is a real problem, but how do you handle side effects or how do you handle,
*  I guess, external dependencies, like calling the Stripe API?
*  Andriy Vassilov Maybe Stripe would write a spec for the API.
*  Tim Cynova But like you can't do this for everything.
*  Can you do this for everything you use? Like how do you do it for, if there's a language model?
*  Like maybe people will use language models as primitives in the programs they write,
*  and there's like a dependence on it. And like how do you now include that?
*  Andriy Vassilov I think you might be able to prove that still.
*  Tim Cynova Prove what about language models?
*  Andriy Vassilov I think if it feels possible that you could actually prove that a language model is
*  aligned, for example. Or like you can prove that it actually gives the right answer.
*  Tim Cynova That's the dream.
*  Tim Cynova Yeah, that is. I mean, if it's possible,
*  that's your, I have a dream speech. If it's possible, that will certainly help with, you know,
*  making sure your code doesn't have bugs and making sure AI doesn't destroy all of human
*  civilization. So the full spectrum of AI safety to just bug finding. So you said the models
*  struggle with bug finding. What's the hope? Andriy Vassilov You know, my hope initially is,
*  and I can let Michael chime in too, but it was like this. It should first help with the stupid
*  bugs. Like it should very quickly catch the stupid bugs. Like off by one editor is like, sometimes
*  you write something in a comment and do the other way. It's like very common. Like I do this, I
*  write like less than in a comment and like I maybe write the greater than side or something like that.
*  And the model is like, yeah, you look sketchy. Like, dude, you sure you want to do that?
*  But eventually it should be able to catch harder bugs too.
*  Tim Cynova Yeah. And I think that it's also important to note that this is
*  having good bug finding models feels necessary to get to the highest reaches of having AI do more
*  and more programming for you, where you're going to, you know, if the AI is building more and more
*  of the system for you, you need to not just generate, but also verify. And without that,
*  some of the problems that we've talked about before with programming with these models
*  will just become untenable. So it's not just for humans, like you write a bug, I write a bug,
*  find the bug for me, but it's also being able to verify the AI's code and check it
*  is really important.
*  Michael Sink Yeah. And then how do you actually do this? Like we have had a lot of
*  contentious dinner discussions of how do you actually train a bug model. But one very popular
*  idea is, you know, it's kind of potentially easy to introduce a bug than actually finding the bug.
*  And so you can train a model to introduce bugs in existing code. And then you can train a reverse
*  bug model then that can find bugs using this synthetic data. So that's like one example.
*  But yeah, there are lots of ideas for how to.
*  Tim Cynova You can also do a bunch of work, not even at the model level,
*  of taking the biggest models and then maybe giving them access to a lot of information
*  that's not just the code. Like it's kind of a hard problem to like stare at a file and be like,
*  where's the bug? And you know, that's hard for humans often, right? And so often you have to
*  run the code and being able to see things like traces and step through a debugger.
*  There's another whole another direction where it like kind of tends toward that. And it could
*  also be that there are kind of two different product form factors here. It could be that you
*  have a really specialty model that's quite fast, that's kind of running in the background and
*  trying to spot bugs. And it might be that sometimes sort of to Arvid's earlier example about,
*  you know, some nefarious input box bug might be that sometimes you want to like there's you know,
*  there's a bug. You're not just like checking hypothesis free. You're like, this is a problem.
*  I really want to solve it. And you zap that with tons and tons and tons of compute. And you're
*  willing to put in like $50 to solve that bug or something even more.
*  Jeff Sarr Have you thought about integrating money into this whole thing? Like I would pay
*  probably a large amount of money for if you found a bug or even generated code that I really
*  appreciated like Adam moment a few days ago, when I started using cursor or generated
*  perfect, like perfect three functions for interacting with the YouTube API to update
*  captions and for localization like different in different languages.
*  The API documentation is not very good. And the code across like if I Googled it for a while,
*  I couldn't find exactly there's a lot of confusing information and cursor generated perfectly.
*  And I was like, I just sat back. I read the code. I was like, this is correct. I tested it is
*  correct. I was like, I want to tip on a button that goes, yeah, here's $5. One that's really good just
*  to support the company and support what the interface is. And the others that probably
*  send a strong signal, like good job. Right? There's much stronger signal than just accepting the code,
*  right? You just actually send like a strong good job that and for bug finding, obviously, like,
*  there's a lot of people, you know, that would pay a huge amount of money for a bug, like a bug
*  bug bounty thing. Right? Is that you guys think about that?
*  Yeah, it's a controversial idea inside the company. I think it sort of depends on how much
*  you believe in humanity almost, you know, like, I think it would be really cool if like,
*  you spend nothing to try to find a bug. And if it doesn't find a bug, you spend $0. And then if
*  it does find a bug, and you click accept, then it also shows like in parentheses, like $1. As you
*  spend $1 to accept the bug. And then of course, there's a worry, like, okay, we spent a lot of
*  computation, like maybe people will just copy paste. I think that's a worry. And then there's
*  also the worry that like introducing money into the product makes it like kind of, you know, like,
*  it doesn't feel as fun anymore. Like you have to like think about money and you all you want
*  to think about is like the code. And so maybe it actually makes more sense to separate it out. And
*  like, you pay some fee like every month, and then you get all of these things for free.
*  But there could be a tipping component, which is not like it costs.
*  It still has that like dollar symbol. I think it's fine. But I also see the point where,
*  like, maybe you don't want to introduce it.
*  Yeah, I was gonna say the moment that feels like people do this is when they share it,
*  when they have a fantastic example, they just kind of share it with their friends.
*  There is also a potential world where there's a technical solution to this,
*  like honor system problem to where if we can get to a place where we understand
*  the output of the system more, I mean, to the stuff we were talking about with like,
*  you know, error checking with the LSP, and then also running the code. But if you could get to
*  a place where you could actually somehow verify, oh, I have fixed the bug, maybe then the bounty
*  system doesn't need to rely on the honor system to how much interaction is there between the
*  terminal and the code. Like how much information is gained from if you run the code in the terminal?
*  Like, can you use, can you do like a loop where it runs the code and suggests how to change the
*  code if the code and runtime gives an error? Because right now they're separate worlds
*  completely. Like, I know you can do Ctrl K inside the terminal to help you write the code.
*  You can use terminal context as well. Inside of checkman K kind of everything. We don't have the
*  looping part yet. Though we expect something like this could make a lot of sense. There's a question
*  of whether it happens in the foreground too, or if it happens in the background, like what we've been
*  discussing. Sure, the background is pretty cool. Like we do running the code in different ways.
*  Plus, there's a database side to this, which I highly protect it from not modifying the database.
*  But okay. I mean, there's certainly cool solutions there. There's this new API that is being developed
*  for, it's not an AWS, but you know, it certainly is, I think it's in PlanetScale. I don't know if
*  PlanetScale was the first one to add it. It's disability sort of add branches to a database,
*  which is like if you're working on a feature and you want to test against the prod database,
*  but you don't actually want to test against the prod database, you could sort of add a branch to
*  the database. And the way they do that is they add a branch to the right ahead log. And there's
*  obviously a lot of technical complexity in doing it correctly. I guess database companies need new
*  things to do. They have good databases now. And I think like TurboBuffer, which is one of the
*  databases we use, is going to add maybe branching to the right ahead log. And so maybe the AI agents
*  will use branching. They'll like test against them, branch, and it's sort of going to be a
*  requirement for the database to like support branching or something. It'd be really interesting
*  if you could branch a file system, right? Yeah. I feel like everything needs branching.
*  Like, yeah, yeah, sick. That's the problem with the multiverse, right?
*  Like if you branch on everything, that's like a lot. I mean, there's obviously these like super
*  clever algorithms to make sure that you don't actually use a lot of space or CPU or whatever.
*  Okay. This is a good place to ask about infrastructure. So you guys mostly use AWS.
*  What are some interesting details? What are some interesting challenges? Why did you choose AWS?
*  Why is AWS still winning?
*  AWS is just really, really good. It's really good. Like whenever you use an AWS product,
*  you just know that it's going to work. Like it might be absolute hell to go through the steps
*  to set it up. Why is the interface so horrible? Because it's just so good. It doesn't need to.
*  It's the nature of winning. I think it's exactly. It's just the nature of winning.
*  Yeah. Yeah. But AWS, you can always trust like it will always work.
*  And if there is a problem, it's probably your problem.
*  Okay. Is there some interesting like challenges to you guys, a pretty new startup
*  to get scaling to like to so many people? Yeah, I think that there it has been
*  an interesting journey adding each extra zero to the request per second.
*  You run into all of these with like the general components you're using for caching and databases,
*  run into issues as you make things bigger and bigger. And now we're at the scale where we get
*  like into overflows on our tables and things like that. And then also there have been some
*  custom systems that we've built, like for instance, our retrieval system for computing a semantic
*  index of your code base and answering questions about a code base that have continually, I feel
*  like been one of the trickier things to scale. I have a few friends who are super,
*  super senior engineers. And one of their sort of lines is like, it's very hard to predict where
*  systems will break when you scale them. You can sort of try to predict in advance, but like there's
*  always something weird that's going to happen when you add this extra zero. And you thought,
*  you thought through everything, but you didn't actually think through everything. But I think
*  for that particular system, we've, so for concrete details, the thing we do is obviously we upload,
*  when like we chunk up all of your code and then we send out sort of the code for embedding and
*  we embed the code and then we store the embeddings in a database, but we don't actually store any of
*  the code. And then there's reasons around making sure that we don't introduce client bugs because
*  we're very, very paranoid about client bugs. We store much of the details on the server,
*  like everything is sort of encrypted. So one of the technical challenges is always making sure
*  that the local index, the local code base state is the same as the state that is on the server.
*  And the way sort of technically we ended up doing that is so for every single file,
*  you can sort of keep this hash. And then for every folder, you can sort of keep a hash, which is
*  the hash of all of its children. And you can sort of recursively do that until the top.
*  And why do something complicated? One thing you could do is you could keep a hash for every file.
*  Then every minute you could try to download the hashes that are on the server, figure out what
*  are the files that don't exist on the server. Maybe you just created a new file, maybe you just
*  deleted a file. Maybe you checked out a new branch and tried to reconcile the state between
*  the client and the server. But that introduces like absolutely ginormous network overhead, both
*  on the client side. I mean, nobody really wants us to hammer their Wi-Fi all the time if you're
*  using cursor. But also like, I mean, it would introduce like ginormous overhead in the database.
*  It would sort of be reading this tens of terabytes database, sort of approaching like
*  20 terabytes or something database like every second. That's just kind of crazy. You definitely
*  don't want to do that. So what do you do? You sort of you just try to reconcile the single hash,
*  which is at the root of the project. And then if something mismatches, then you go, you find where
*  all the things disagree. Maybe you look at the children and see if the hashes match. And if the
*  hashes don't match, go look at their children and so on. But you only do that in the scenario
*  where things don't match. And for most people, most of the time, the hashes match. So it's a kind of
*  like hierarchical reconciliation. Yeah, something like that. Yeah, it's called the Merkle tree.
*  Yeah, Merkle. Yeah. I mean, so yeah, this is cool to see that you kind of have to think through all
*  these problems. And I mean, the point of like, the reason it's gotten hard is just because,
*  like the number of people using it and, you know, if some of your customers have really,
*  really large code bases to the point where, you know, we originally reorder our code base,
*  which is big. But I mean, it's just not the size of some company that's been there for 20 years and
*  sort of has such an enormous number of files. And you sort of want to scale that across programmers.
*  There's all these details where like, building the simple thing is easy, but scaling it to a
*  lot of people, like a lot of companies is obviously a difficult problem, which is sort of, you know,
*  independent of actually so that there's part of this scaling our current solution is also,
*  you know, coming up with new ideas that obviously we're working on. But then but then scaling all
*  of that in the last few weeks, months. Yeah. And there are a lot of clever things, like additional
*  things that go into this indexing system. For example, the bottleneck in terms of costs is not
*  soaring things in the vector database or the database, it's actually embedding the code.
*  And you don't want to re embed the code base for every single person in a company that is
*  using the same exact code except for maybe there is a branch with a few different files,
*  or they've made a few local changes. And so because again, embeddings are the bottleneck,
*  you can do is one clever trick and not have to worry about like, the complexity of like dealing
*  with branches and the other databases where you just have some cash on the actual vectors
*  computed from the hash of a given chunk. And so this means that when the nth person at a company
*  goes and events or code base, it's really, really fast. And you do all this without actually storing
*  any code on our servers at all. No code data stored. We just store the vectors in the vector
*  database and the vector cache. What's the biggest gains at this time? You get from indexing the
*  code base, I could just out of curiosity, like what, what benefit to users have, it seems like
*  longer term, there'll be more and more benefit. But in the short term, just asking questions of
*  the code base. What's the use, what's the usefulness of that? I think the most obvious one
*  is just you want to find out where something is happening in your large code base. And you sort of
*  have a fuzzy memory of, okay, I want to find the place where we do X. But you don't exactly know
*  what to search for in a normal text search. And so you ask a chat, you hit command enter to ask with
*  the code base chat. And then very often it finds the right place that you were thinking of.
*  I think like you, like you mentioned in the future, I think this only going to get more
*  and more powerful where we're working a lot on improving the quality for retrieval.
*  And I think the ceiling for that is really, really much higher than people get the credit for.
*  One question that's good to ask here. Have you considered and why haven't you much done sort of
*  local stuff to where you can do the, it seems like everything we just discussed is exceptionally
*  difficult to do. To go to the cloud, you have to think about all these things with the caching and
*  the large code base with a large number of programmers are using the same code base.
*  You have to figure out the puzzle of that. A lot of it, most software just does stuff,
*  this heavy computational stuff locally. Have you considered doing sort of embeddings locally?
*  Yeah, we thought about it. And I think it would be cool to do it locally. I think it's just
*  really hard. And one thing to keep in mind is that some of our users use the latest MacBook Pro.
*  But most of our users, like more than 80% of our users are in Windows machines, which,
*  and many of them are not very powerful. And so local models really only works on the latest
*  computers. And it's also a big overhead to build that in. And so even if we would like to do that,
*  it's currently not something that we are able to focus on. And I think there are some people that
*  do that. And I think that's great. But especially as models get bigger and bigger, and you want to
*  do fancier things with bigger models, it becomes even harder to do it locally.
*  Yeah. And it's not a problem with weaker computers. It's just that, for example, if you're
*  some big company, you have big company code base, it's just really hard to process big company code
*  base even on the beefiest MacBook Pros. So it's not even a matter of if you're just a student or
*  something. I think if you're the best programmer at a big company, you're still going to have a
*  horrible experience if you do everything locally. You could do edge and scrape by, but again, it
*  wouldn't be fun anymore. Yeah. Like at approximate nearest neighbors, and this massive code base is
*  going to just eat up your memory and your CPU. And that's just that. Let's talk about also the
*  modeling side where, as Arvid said, there are these massive headwinds against local models where,
*  one, things that seem to move towards MOEs. One benefit is maybe there are more memory bandwidth
*  bound, which plays in favor of local versus using GPUs or using Nvidia GPUs. But the downside is
*  these models are just bigger in total. And they're going to need to fit often not even on a single
*  node, but multiple nodes. There's no way that's going to fit inside of even really good MacBooks.
*  And I think especially for coding, it's not a question as much of does it clear some bar of
*  the model's good enough to do these things. And then we're satisfied, which may be the case for
*  other problems and maybe where local models shine. But people are always going to want the best,
*  the most intelligent, the most capable things. And that's going to be really, really hard to run for
*  almost all people locally. Don't you want the most capable model? You want Sonnet?
*  Also with O1.
*  I like how you're pitching me. Would you be satisfied with an inferior model? I'm one of those,
*  but there's some people that like to do stuff locally, especially like, there's a whole,
*  obviously, open source movement that resists. And it's good that they exist actually, because
*  you want to resist the power centers that are growing.
*  There's actually an alternative to local models that I'm particularly fond of. I think it's still
*  very much in the research stage, but you could imagine to do homomorphic encryption for language
*  model inference. So you encrypt your input on your local machine, then you send that up, and then
*  the server can use lots of computation. They can run models that you cannot run locally on
*  this encrypted data, but they cannot see what the data is. And then they send back the answer,
*  and you decrypt the answer, and only you can see the answer. So I think that's still very much
*  research, and all of it is about trying to make the overhead lower, because right now the overhead
*  is really big. But if you can make that happen, I think that would be really, really cool. And
*  I think it would be really, really impactful. Because I think one thing that's actually kind
*  of worrisome is that as these models get better and better, they're going to become more and more
*  economically useful. And so more and more of the world's information and data will flow through
*  one or two centralized actors. And then there are worries about there can be traditional hacker
*  attempts, but it also creates this kind of scary part where if all of the world's information is
*  flowing through one node in plain text, you can have surveillance in very bad ways. And sometimes
*  that will happen for... Initially it will be good reasons. People will want to try to protect against
*  bad actors using AI models in bad ways. And then you will add in some surveillance code, and then
*  someone else will come in and you're in a slippery slope, and then you start
*  doing bad things with a lot of the world's data. And so I'm very hopeful that we can solve
*  homomorphic encryption for language model inference.
*  Yeah, and doing privacy preserving machine learning. But I would say that's the challenge
*  we have with all software these days. There's so many features that can be provided from the cloud
*  and all of us increasingly rely on it and make our life awesome, but there's downsides. And that's
*  why you rely on really good security to protect from basic attacks. But there's also only a small
*  set of companies that are controlling that data. And they obviously have leverage and they could be
*  infiltrated in all kinds of ways. That's the world we live in.
*  I mean, the thing I'm just actually quite worried about is the world where...
*  I mean, so Entropic has this responsible scaling policy and we're on the low ESLs,
*  which is the Entropic security level or whatever, of the models. But as we get to
*  like, quote unquote, ESL 3, ESL 4, whatever models, which are sort of very powerful,
*  but for mostly reasonable security reasons, you would want to monitor all the prompts.
*  But I think that's sort of reasonable and understandable where everyone is coming from. But
*  Matt, it'd be really horrible if all the world's information is sort of
*  monitored that heavily. It's way too centralized. It's like really fine line you're walking where
*  on the one side, you don't want the models to go rogue. On the other side, it's humans. I don't
*  know if I trust all the world's information to pass through three model providers.
*  Yeah. Why do you think it's different than cloud providers?
*  Because I think a lot of this data would never have gone to the cloud providers in the first place,
*  where this is often like you want to give more data to the EIA models. You want to give
*  personal data that you would never have put online in the first place to these companies
*  or to these models. And it also centralizes control, where right now for cloud, you can often
*  use your own encryption keys and AWS can't really do much. But here it's just
*  centralized actors that see the exact plain text of everything.
*  On the topic of context, that's actually been a friction for me. When I'm writing code in Python,
*  there's a bunch of stuff imported. You could probably intuit the kind of stuff I would like
*  to include in the context. How hard is it to auto figure out the context?
*  It's tricky. I think we can do a lot better at computing the context automatically in the future.
*  One thing that's important to note is there are trade-offs with including automatic context.
*  So the more context you include for these models, first of all, the slower they are,
*  and the more expensive those requests are, which means you can then do less model calls and do
*  less fancy stuff in the background. Also, for a lot of these models, they get confused if you
*  have a lot of information in the prompt. So the bar for accuracy and for relevance of the context
*  you include should be quite high. But already we do some automatic context in some places
*  within the product. It's definitely something we want to get a lot better at. I think that there
*  are a lot of cool ideas to try there, both on the learning better retrieval systems, like better
*  embedding models, better re-rankers. I think that there are also cool academic ideas, stuff we've
*  tried out internally, but also the field is grappling with writ large, about can you get
*  language models to a place where you can actually just have the model itself, like understand a new
*  corpus of information. And the most popular talked about version of this is can you make the context
*  windows infinite? Then if you make the context windows infinite, can you make the model actually
*  pay attention to the infinite context? And then after you can make it pay attention to the infinite
*  context to make it somewhat feasible to actually do it, can you then do caching for that infinite
*  context? You don't have to recompute that all the time. But there are other cool ideas that are
*  being tried that are a little bit more analogous to fine tuning of actually learning this information
*  in the weights of the model. And it might be that you actually get sort of a qualitatively
*  different type of understanding if you do it more at the weight level than if you do it at the in
*  context learning level. I think the jury's still a little bit out on how this is all going to work
*  in the end. But in the interim, us as a company, we are really excited about better retrieval systems
*  and picking the parts of the code base that are most relevant to what you're doing. We could do
*  that a lot better. Like one interesting proof of concept for the learning this knowledge directly
*  in the weights is with VS code. So we're in a VS code fork, and VS code, the code is all public.
*  So these models in pre training have seen all the code. They've probably also seen questions
*  and answers about it. And then they've been fine tuned and RLHF to be able to be able to answer
*  questions about code in general. So when you ask it a question about VS code, you know, sometimes
*  it'll hallucinate, but sometimes it actually does a pretty good job at answering the question. And
*  I think like this is just by it happens to be okay. But what if you could actually like specifically
*  train or post train a model such that it really was built to understand this code base?
*  It's an open research question, one that we're quite interested in. And then there's also
*  uncertainty of like, do you want the model to be the thing that end to end is doing everything,
*  i.e. it's doing the retrieval and its internals, and then kind of answering the question creating
*  the code? Or do you want to separate the retrieval from the frontier model, where maybe,
*  you know, you'll get some really capable models that are much better than like the best open
*  source ones in a handful of months. And then you'll want to separately train a really good
*  open source model to be the retriever to be the thing that feeds in the context to these larger
*  models. Can you speak a little more to the post training a model to understand the code base?
*  Like, what do you what do you mean by that? With this synthetic data direction? Is this?
*  Yeah, I mean, there are many possible ways you could try doing it. There's certainly no shortage
*  of ideas. It's just a question of going in and like trying all of them and being empirical about
*  which one works best. You know, one one very naive thing is to try to replicate what's done
*  with the S code and these frontier models. So let's like continue pre training some kind of
*  continued pre training that includes general code data, but also throws in a lot of the data
*  of some particular repository that you care about. And then in post training, meaning in let's just
*  start with instruction fine tuning, you have like a normal instruction fine tuning data set about
*  code, then you throw in a lot of questions about code in that repository. So you could either
*  get ground truth ones, which might be difficult, or you could do what you kind of hinted at or
*  suggested using synthetic data, ie, kind of having the model ask questions about various
*  recent pieces of the code. So you kind of take the pieces of the code, then prompt the model or have
*  a model propose a question for that piece of code, and then add those as instruction fine tuning
*  data points. And then in theory, this might unlock the model's ability to answer questions
*  about that code base. Let me ask you about OpenAI 01. What do you think is the role of that kind of
*  test time compute system in programming? I think test time compute is really, really interesting.
*  So there's been the pre training regime, which will kind of as you scale up the amount of data,
*  and the size of your model get you better and better performance, both on loss and then on
*  downstream benchmarks, and just general performance, we use it for coding, or other tasks.
*  We're starting to hit a bit of a data wall, meaning it's going to be hard to continue scaling
*  up this regime. And so scaling up 10 test time compute is an interesting way of now,
*  you know, increasing the number of inference time flops that we use, but still getting like,
*  like, yeah, as you increase the number of flops use inference time getting corresponding
*  improvements in the performance of these models. Traditionally, we just had to literally train a
*  bigger model that always uses that always used that many more flops. But now we could perhaps use
*  the same size model and run it for longer to be able to get an answer at the quality of a
*  much larger model. And so the really interesting thing I like about this is there are some problems
*  that perhaps require 100 trillion parameter model intelligence trained on 100 trillion tokens.
*  But that's like maybe 1%, maybe like point 1% of all queries. So are you going to spend
*  all of this effort all this compute training a model that costs that much and then run it
*  so infrequently? It feels completely wasteful when it said you get the model that can that is that
*  you train the model that is capable of doing the 99.9% of queries, then you have a way of
*  inference time running it longer for those few people that really, really want max intelligence.
*  How do you figure out which problem requires what level of intelligence? Is that possible to
*  dynamically figure out when to use GPT-4? When to use like when to use a small model? And when you
*  need the the O1? I mean, yeah, that's that's an open research problem. Certainly. I don't think
*  anyone's actually cracked this model routing problem quite well. We'd like to we have like
*  kind of initial implementations of this for things for something like cursor tab. But at the level of
*  going between 4.0 sonnet 201, it's a bit trickier. There's also a question like what level of
*  intelligence do you need to determine if the thing is too hard for the four level model? Maybe you
*  need the O1 level model. It's really unclear. But you mentioned there's a there's a there's a
*  pre training process, then there's post training. And then there's like test time compute that fair
*  to sort of separate. Where's the biggest gains? Well, it's weird, because like test time compute,
*  there's like a whole training strategy needed to get test time to compute to work. And the really
*  the other really weird thing about this is no one like outside of the big labs, and maybe even just
*  open AI, no one really knows how it works. Like there have been some really interesting papers
*  that show hints of what they might be doing. And so perhaps they're doing something with
*  tree search using process reward models. But yeah, I just I think the issue is, we don't quite know
*  exactly what it looks like. So it would be hard to kind of comment on like where it fits in, I would
*  put it in post training, but maybe like the compute spent for this kind of forgetting test time compute
*  to work for a model is going to dwarf pre training eventually. So we don't even know if O1 is using
*  just like chain of thought or L, we don't know how they're using any of these. I don't know anything.
*  It's fun to speculate.
*  Like if you were to build a competing model, what would you do?
*  Yeah. So one thing to do would be, I think you probably need to train a process reward model,
*  which is so maybe we can get into reward models and outcome reward models versus process reward
*  models. outcome reward models are the kind of traditional reward models that people are trained
*  for these for for language models, language modeling. And it's just looking at the final
*  thing. So if you're doing some math problem, let's look at that final thing you've done everything.
*  And let's assign a great to it. How likely we think like what's the reward for this this outcome
*  process reward models instead try to grade the chain of thought. And so open AI had some
*  preliminary paper on this, I think, last summer, where they use human labellers to get this pretty
*  large several hundred thousand data set of grading chains of thought.
*  Ultimately, it feels like I haven't seen anything interesting in the ways that people use process
*  reward models outside of just using it as a means of affecting how we choose between a bunch of
*  samples. So like what people do in all these papers is they sample a bunch of outputs from
*  the language model, and then use the process reward models to grade all those generations
*  alongside maybe some other heuristics, and then use that to choose the best answer. The
*  really interesting thing that people think might work and people want to work is
*  research with these process reward models, because if you really can grade every single step of the
*  chain of thought, then you can kind of branch out and, you know, explore multiple paths of this
*  chain of thought, and then use these process reward models to evaluate how good is this branch that
*  you're taking. Yeah, when that when the quality of the branch is somehow strongly correlated with
*  the quality of the outcome at the very end. So like you have a good model of knowing which branch
*  you take. So not just this in the short term, like in the long term. Yeah, and like the interesting
*  work that I think has been done is figuring out how to properly train the process or the interesting
*  work that has been open sourced and people I think talk about is how to train the process reward models
*  maybe in a more automated way. I could be wrong here, could not be mentioning some papers. I
*  haven't seen anything super that seems to work really well for using the process reward models
*  creatively to do tree searching code. This is kind of an AI safety, maybe a bit of a philosophy
*  question. So open AI says that they're hiding the chain of thought from the user. And they've said
*  that that was a difficult decision to make. They instead of showing the chain of thought, they're
*  asking the model to summarize the chain of thought. They're also in the background saying they're going
*  to monitor the chain of thought to make sure the model is not trying to manipulate the user,
*  which is a fascinating possibility. But anyway, what do you think about hiding the chain of thought?
*  One consideration for open AI, and this is completely speculative, could be that they want
*  to make it hard for people to distill these capabilities out of their model. It might actually
*  be easier if you had access to that hidden chain of thought to replicate the technology. Because
*  that's pretty important data like seeing the steps that the model took to get to the final result.
*  So you could probably train on that also. And there was sort of a mirror situation with this,
*  with some of the large language model providers. And also this is speculation. But some of these
*  APIs used to offer easy access to log probabilities for the tokens that they're generating. And also
*  log probabilities for the prompt tokens. And then some of these APIs took those away. And again,
*  complete speculation. But one of the thoughts is that the reason those were taken away is if you
*  have access to log probabilities similar to this hidden chain of thought, that can give you even
*  more information to try and distill these capabilities out of the APIs, out of these
*  biggest models, into models you control. As an asterisk on also the previous discussion about
*  us integrating O1, I think that we're still learning how to use this model. So we made O1
*  available in Cursor because when we got the model, we were really interested in trying it out.
*  I think a lot of programmers are going to be interested in trying it out. But O1 is not part
*  of the default Cursor experience in any way up. And we still haven't found a way to yet integrate
*  it into the editor in a way that we reach for every hour, maybe even every day. And so I think
*  that the jury's still out on how to use the model. And we haven't seen examples yet of people
*  releasing things where it seems really clear, like, oh, that's now the use case. The obvious
*  one to turn to is maybe this can make it easier for you to have these background things running,
*  right, to have these models in loops, to have these models be agentic. But we're still discovering.
*  To be clear, we have ideas. We just need to try and get something incredibly useful before we
*  put it out there. But it has these significant limitations. Even barring capabilities,
*  it does not stream. And that means it's really, really painful to use for things where you want
*  to supervise the output. And instead, you're just waiting for the wall attacks to show up.
*  Also, it does feel like the early innings of test time, compute and search where it's just a very,
*  much of V0. And there's so many things that don't feel quite right. And I suspect
*  in parallel to people increasing the amount of pre-training data and the size of the models
*  in pre-training and finding tricks there, you'll now have this other thread of getting search to
*  work better and better. So let me ask you about Strawberry Tomorrow Eyes. So it looks like
*  GitHub Copilot might be integrating O1 in some kind of way. And I think some of the comments
*  are saying, does this mean cursor is done? I think I saw one comment saying that.
*  I saw time to shut down cursory.
*  So is it time to shut down cursor?
*  I think this space is a little bit different from past software spaces over the 2010s,
*  where I think that the ceiling here is really, really, really incredibly high.
*  And so I think that the best product in three to four years will just be so much more useful
*  than the best product today. And you can wax poetic about Moat's this and brand that. And
*  this is our advantage. But I think in the end, if you stop innovating on the product, you will lose.
*  And that's also great for startups. That's great for people trying to enter this market,
*  because it means you have an opportunity to win against people who have lots of users already
*  by just building something better. And so I think over the next few years, it's just about
*  building the best product, building the best system. And that both comes down to the
*  modeling engine side of things. And it also comes down to the editing experience.
*  Yeah, I think most of the additional value from cursor versus everything else out there
*  is not just integrating the new model fast like a one. It comes from all of the kind of depth that
*  goes into these custom models that you don't realize are working for you in kind of every
*  facet of the product, as well as like the really thoughtful UX with every single feature.
*  All right. From that profound answer, let's descend back down to the technical. You mentioned
*  you have a taxonomy of synthetic data. Oh, yeah. Can you please explain?
*  Yeah, I think there are three main kinds of synthetic data.
*  The first is so what is synthetic data first. So there's normal data, like non synthetic data,
*  which is just data that's naturally created. IE, usually it'll be from humans having done things.
*  So from some human process, you get this data. Synthetic data. The first one would be distillation.
*  So having a language model, output tokens or probability distributions over tokens.
*  And then you can train some less capable model on this. This approach is not going to get you
*  a net like more capable model than the original one that has produced the tokens.
*  But it's really useful for if there's some capability you want to elicit from some really
*  expensive, high latency model, you can then distill that down into some smaller task specific model.
*  The second kind is when like one direction of the problem is easier than the reverse.
*  And so a great example of this is bug detection, like we mentioned earlier, where
*  it's a lot easier to introduce reasonable looking bugs than it is to actually detect them. And this
*  is probably the case for humans too. And so what you can do is you can get a model that's not
*  training that much data that's not that smart to introduce a bunch of bugs in code. And then you
*  can use that to then train use a synthetic data to train a model that can be really good at detecting
*  bugs. The last category, I think is I guess the main one that feels like the big labs are doing
*  for synthetic data, which is producing text with language models that can then be verified easily.
*  So like, you know, extreme example of this is if you have a verification system that can detect if
*  language is Shakespeare level, and then you have a bunch of monkeys typing in typewriters,
*  like you can eventually get enough training data to train a Shakespeare level language model.
*  And I mean, this is the case, like very much the case for math, where verification is actually
*  really, really easy for formal formal languages. And then what you can do is you can have an okay
*  model, generate a ton of rollouts, and then choose the ones that you know have actually
*  proved the ground truth here and theorems and train that further. There's similar things you
*  can do for code with leacode like problems or where if you have some set of tests that you know
*  correspond to if something passes these tests, it is actually solved the problem. You could do
*  the same thing where we verify that it's passed the test and then train the model the outputs that
*  have passed the test. I think it's gonna be a little tricky getting this to work in all domains
*  or just in general, like having the perfect verifier feels really, really hard to do
*  with just like open ended miscellaneous tasks you give the model or more like long horizon tasks,
*  even encoding. That's because you're not as optimistic as Arvid. But yeah, so yeah, so that
*  third category requires having a verifier. Yeah, verification is it feels like it's best when you
*  know for a fact that it's correct and then it wouldn't be using a language model to verify,
*  it'd be using tests or formal systems. Or running the thing too, doing the human form of verification
*  where you just do manual quality control. But the language model version of that where it's
*  running the thing and it actually understands the output. Yeah, no, that's true.
*  Sort of somewhere between. Yeah, I think that's the category that is
*  most likely to result in like massive gains. What about RL with feedback side RLHF versus RLAAIF?
*  What's the role of that in getting better performance on the models?
*  Yeah, so RLHF is when the reward model you use is trained from some labels you've collected from
*  humans getting feedback. I think this works if you have the ability to get a ton of human feedback
*  for this kind of task that you care about. RLAAIF is interesting because you're kind of depending on
*  like this is actually kind of going to this depending on the constraint that verification
*  is actually a decent bit easier than generation. Because it feels like okay, like what are you
*  doing? Are you using this language model to look at the language model outputs and then prove the
*  language model? But no, it actually may work if the language model has a much easier time
*  verifying some solution than it does generating it, then you actually could perhaps get this kind
*  of recursive loop. I don't think it's going to look exactly like that. The other the other thing
*  you could do is that we kind of do is like a little bit of a mix of RLAAIF and RLHF, where usually the
*  model is actually quite correct. And this is in the case of cursor tap at picking between like two
*  possible generations of what is the better one. And then it just needs like a hand a little bit
*  of human nudging with only like on the order of 50, 100 examples to like kind of align that prior
*  the model has with exactly what you want. It looks different than I think normal RLHF for usually
*  training these reward models and tons of examples. What's your intuition when you compare
*  generation and verification or generation and ranking? Is ranking way easier than generation?
*  My intuition would just say yeah, it should be like this is kind of going back to like if you
*  if you believe P does not equal NP, then there's this massive class of problems that are much,
*  much easier to verify given a proof than actually proving it. I wonder if the same thing will prove
*  P not equal to NP or P equal to NP. That would be that would be really cool. That'd be of whatever
*  feels metal by AI who gets the credit. Another open philosophical question. I'm actually
*  surprisingly curious what what what like a good bet for when AI will get the Fields Medal will be.
*  I actually don't have a mod specialty. I don't know what a mod's bet here is.
*  Oh sorry, Nobel Prize or Fields Medal first? Fields Medal level. Fields Medal needs to solve.
*  Fields Medal comes first. Well you would say that of course. But it's also this like isolated system
*  you know verify and no sure. Like I don't even know if I don't need to do. I feel like I have
*  much more to do there. It felt like the path to get to IMO was a little bit more clear because
*  it already could get a few IMO problems and there are a bunch of like there's a bunch of low hanging
*  fruit given the literature at the time of like what what tactics people could take. I think I'm
*  one much less first in the space of theorem proving now and two yeah less intuition about
*  how close we are to solving these really really hard open problems. So you think it'll be Fields
*  Medal first? It won't be like in physics or in oh 100% I think I think I think that's probably
*  more likely. Like it's probably much more likely that it'll get then. Yeah yeah yeah well I think
*  it puts the like I don't know like BSD which is a Bird-Spinning Turn Dioconjecture or like
*  Riemann iPods or any one of these like hard hard math problems or just like actually really hard.
*  It's sort of unclear what the path to to get even a solution looks like. Like we don't even know what
*  a path looks like let alone. And you don't buy the idea this is like an isolated system and you can
*  actually you have a good reward system and it feels like it's easier to train for that.
*  I think we might get Fields Medal before AGI. I mean I'd be very happy. I'd be very happy but I
*  don't know if I think 2020 age 2030. Fields Medal. All right. It's uh it feels like forever
*  from now given how fast things have been going. Speaking of how fast things have been going let's
*  talk about scaling laws. So for people who don't know maybe it's good to talk about this whole
*  idea of scaling laws. What are they? Where do you think stand? And where do you think things are
*  going? I think it's interesting the original scaling laws paper by OpenAI was slightly wrong
*  because I think of some issues they did with uh learning rate schedules and then chinchilla showed
*  a more correct version. And then from then people have again kind of deviated from doing the compute
*  optimal thing because people start now optimizing more so for uh making the thing work really well
*  given a given an inference budget. But I think there are a lot more dimensions to these curves
*  than what we originally used of just compute number of parameters and data. Like inference
*  compute is the obvious one. I think context length is another obvious one. So if you care
*  like let's say you care about the two things of inference compute and then context window.
*  Maybe the thing you want to train is some kind of SSM because they're much much cheaper and faster
*  at super super long context. And even if maybe it is 10x worse scaling properties during training.
*  Meaning you spend 10x more compute to train the thing to get the same level of capabilities.
*  It's worth it because you care most about that inference budget for really long context windows.
*  So it'll be interesting to see how people kind of play with all these dimensions.
*  So yeah I mean you speak to the multiple dimensions obviously the original conception was
*  just looking at the variables of the size of the model as measured by parameters and the size of
*  the data is measured by the number of tokens and looking at the ratio of the two. Yeah. And it's
*  it's kind of a compelling notion that there is a number or at least a minimum and it seems like
*  one was emerging. Do you still believe that there is a kind of bigger is better?
*  I mean I think bigger is certainly better for just raw performance. And raw intelligence.
*  And raw intelligence. I think that the path that people might take is I'm particularly bullish on
*  distillation. And like yeah how many knobs can you turn to if we spend like a ton ton of money
*  on training. Like get the most capable cheap model. Right like really really caring as much
*  as you can. Because like the naive version of caring as much as you can about inference time
*  computers what people have already done with like the llama models are just overtraining the shit
*  out of 7b models on way way way more tokens than is essential optimal. Right but if you really care
*  about it maybe thing to do is what gamma did which is let's just not let's not just train on
*  tokens let's literally train on minimizing the KL divergence with the distribution of gamma 27b.
*  Right so knowledge distillation there. And you're spending the compute of literally training this
*  27 billion model billion parameter model on all these tokens just to get out this I don't know
*  smaller model. And the distillation gives you just a faster model smaller means faster. Yeah
*  distillation in theory is I think getting out more signal from the data that you're training on.
*  And it's like another it's perhaps another way of getting over not like completely over but like
*  partially helping with the data wall. Where like you only have so much data to train on let's like
*  train this really really big model on all these tokens and we'll distill it into a smaller one.
*  And maybe we can get more signal per token for this for this much smaller model than we would
*  have originally if we trained it. So if I gave you 10 trillion dollars how would you spend it?
*  I mean you can't buy an island or whatever. How would you allocate it in terms of improving the
*  the big model versus maybe paying for HF in the RLHF? Yeah I think there's a lot of these secrets
*  and details about training these large models that I just don't know and only privy to the large
*  labs. And the issue is I would waste a lot of that money if I even attempted this because I
*  wouldn't know those things. Suspending a lot of disbelief and assuming like you had the know-how
*  and operate or if you're saying like you have to operate with like the limited information you have
*  now. No no no actually I would say you swoop in and you get all the information all the little
*  heuristics all the little parameters all the all the parameters that define how the thing is trained.
*  If we look in how to invest money for the next five years in terms of maximizing what you called
*  raw intelligence. I mean isn't the answer like really simple you just you just try to get as
*  much compute as possible like like at the end of the day all you need to buy is the GPUs and then
*  the researchers can find find all the all like they they can sort of you know you can tune whether
*  you want to between a big model or a small model like. Well this gets into the question of like are
*  you really limited by compute and money or are you limited by these other things and I'm more
*  privy to Arvid's Arvid's belief that we're sort of idea limited but there's always that like. But
*  if you have a lot of compute you can run a lot of experiments. So you would run a lot of experiments
*  versus like use that computer to train a gigantic model. I would but I do believe that we are
*  limited in terms of ideas that we have. I think yeah because even with all this compute and like
*  you know all the data you could collect in the world I think you really are ultimately limited by
*  not even ideas but just like really good engineering like even with all the capital
*  in the world would you really be able to assemble like there aren't that many people in the world
*  who really can like make the difference here. And there's so much work that goes into research
*  that is just like pure really really hard engineering work. As like a very kind of
*  hand-wavy example if you look at the original transformer paper you know how much work was
*  kind of joining together a lot of these really interesting concepts embedded in the literature
*  versus then going in and writing all the codes like maybe the CUDA kernels maybe whatever else
*  I don't know if it ran on GPUs or TPUs originally such that it actually saturated the GPU performance
*  right getting Gnome's here to go in and do all this code right and Gnome is like probably one
*  of the best engineers in the world or maybe going a step further like the next generation of models
*  having these things like getting model parallelism to work and scaling it on like you know thousands
*  of or maybe tens of thousands of like V100s which I think GBDE3 may have been. There's just so much
*  engineering effort that has to go into all of these things to make it work. If you really brought that
*  cost down to like you know maybe not zero but just made it 10x easier made it super easy for someone
*  with really fantastic ideas to immediately get to the version of like the new architecture they
*  dreamed up that is like getting 50 40 utilization on the GPUs. I think that would just speed up
*  research by a ton. I mean I think if you see a clear path to improvement you should always sort
*  of take the low hanging fruit first right and I think probably OpenAI and all the other labs
*  did the right thing to pick off the low hanging fruit where the low hanging fruit is like sort of
*  you could scale up to a GPT-4.25 scale and you just keep scaling and like things keep getting
*  better and as long as like you there's no point of experimenting with new ideas when like everything
*  is working and you just sort of bang on and try to get as much juice out of the possible and then
*  maybe when you really need new ideas for it. I think if you're spending 10 trillion dollars
*  probably want to spend some then actually like reevaluate your ideas like probably your idea
*  limited at that point. I think all of us believe new ideas are probably needed to get you know all
*  the way there to AGI and all of us also probably believe there exist ways of testing out those ideas
*  at smaller scales and being fairly confident that they'll play out. It's just quite difficult to
*  quite difficult for the labs in their current position to dedicate their very limited research
*  and engineering talent to exploring all these other ideas when there's like this core thing that will
*  probably like improve performance for some like decent amount of time.
*  Yeah but also these big labs like winning so they're they're just going wild okay
*  Okay so how big question looking out into the future you're now at the the center of
*  the programming world how do you think programming the nature of programming changes in the next
*  few months in the next year in the next two years next five years ten years?
*  I think we're really excited about a future where the programmers in the driver's seat
*  for a long time and you've heard us talk about this a little bit but one that emphasizes
*  speed and agency for the programmer and control the ability to modify anything you want to modify
*  the ability to iterate really fast on what you're building and this is a little different I think
*  than where some people are are jumping to in the space where I think one idea that's captivated
*  people is can you talk to your computer can you have it build software for you as if you're
*  talking to like an engineering department or an engineer over slack and can it just be this this
*  sort of isolated text box and part of the reason we're not excited about that is you know some of
*  the stuff we talked about with latency but then a big piece a reason we're not excited about that
*  is because that comes with giving up a lot of control it's much harder to be really specific
*  when you're talking in the text box and if you're necessarily just going to communicate with a thing
*  like you would be communicating with an engineering department you're actually
*  advocating tons of tons of really important decisions to this bot and this kind of gets
*  at fundamentally what engineering is I think that some some people who are a little bit more
*  removed from engineering might think of it as you know the spec is completely written out and then
*  the engineers just come and they just implement and it's just about making the thing happen in
*  code and making the thing exist but I think a lot of the the best engineering the engineering we enjoy
*  um involves tons of tiny micro decisions about what exactly you're building and about really
*  hard trade-offs between you know speed and cost and just all the other things involved in a system
*  and uh we want as long as humans are actually the ones making you know designing the software
*  and the ones um specifying what they want to be built and it's not just like company run by all
*  ai's we think you'll really want the humor the human in a driver's seat um dictating these
*  decisions and so there's the jury's still out on kind of what that looks like I think that you know
*  one weird idea for what that could look like is it could look like you kind of you can control the
*  level of abstraction you view a code base at and you can point at specific parts of a code base that
*  um like maybe you digest a code base by looking at it in the form of pseudocode and um you can
*  actually edit that pseudocode too and then have changes get me down at the the sort of formal
*  programming level and you keep the like you know you can gesture at any piece of logic uh in your
*  software component of programming you keep the inflow text editing component of programming you
*  keep the control of you can even go down into the code you can go at higher levels of abstraction
*  while also giving you these big productivity gains it'd be nice if you can go up and down the
*  the abstraction stack yeah and there are a lot of details figure out there that's sort of like a
*  fuzzy idea time will tell if it actually works but these these principles of of control and speed in
*  the human in the driver's seat we think are really important um we think for some things like arvid
*  mentioned before for some styles of programming you can kind of hand it off chatbot style you know if
*  you have a bug that's really well specified but that's not most of programming and that's also
*  not most of the programming we think a lot of people value uh what about like the fundamental
*  skill of programming there's a lot of people like young people right now kind of scared like
*  thinking because they like love programming but they're scared about like will i be able to have
*  a future if i pursue this career path do you think the very skill of programming will change
*  fundamentally i actually think this is a really really exciting time to be building software
*  like we remember what programming was like in you know 2013 2012 whatever it was um and there was
*  just so much more cruft and boilerplate and you know looking up something really gnarly and you
*  know that stuff still exists it's definitely not at zero but programming today is way more fun than
*  back then um it's like we're really getting down to the the delight concentration and all the things
*  that really draw people to programming like for instance this element of being able to build
*  things really fast and um speed and also individual control like all those are just being turned up
*  a ton um and so i think it's just going to be i think it's going to be a really really fun time
*  for people who build software um i think that the skills will probably change too i i think that
*  people's taste and creative ideas will be magnified and it will be less about
*  maybe less a little bit about boilerplate text editing maybe even a little bit less about
*  carefulness which i think is really important today if you're a programmer i think it'll be a
*  lot more fun what do you guys think i agree i'm i'm very excited to be able to change like just
*  one thing that that happened recently was like we wanted to do a relatively big migration to our
*  codebase we were using async local storage in in nojs which is known to be not very performant and
*  we wanted to migrate to our context object and this is a big migration in effects the entire codebase
*  and swal and i spent i don't know five days uh working through this even with today's ai tools
*  and i am really excited for a future where i can just show a couple of examples and then the ai
*  applies that to all of the locations and then it highlights oh this is a new example like what
*  should i do and then i show exactly what to do there and then that can be done in like 10 minutes
*  and then you can iterate much much faster then you can then you don't have to think as much
*  up front and stay stand at the blackboard and like think exactly like how are we going to do this
*  because the cost is so high but you can just try something first and you realize oh this is not
*  actually exactly what i want and then you can change it instantly again after and so yeah i
*  think being a programmer in the future is going to be a lot of fun yeah i really like that point
*  about it feels like a lot of the time with programming there are two ways you can go about
*  it one is like you think really hard carefully upfront about the best possible way to do it
*  and then you spend your limited time of engineering to actually implement it
*  uh but i much prefer just getting in the code and like you know taking a crack at it seeing
*  how it kind of lays out and then iterating really quickly on that that feels more fun
*  yeah like just speaking to generate the boilerplate is great so you just focus on the
*  difficult design nuanced difficult design decisions migration i feel like this is
*  this is a cool one like it seems like large language model is able to basically translate
*  from one program language to another or like translate like migrate in the general sense of
*  what my grade is um but that's in the current moment so i mean the fear has to do with like
*  okay as these models get better and better then you're doing less and less creative decisions
*  and is it going to kind of move to a place where it's uh you're operating in the design space of
*  natural language where natural language is the main programming language and i guess i could ask
*  that by way of advice like if somebody's interested in programming now what do you think they should
*  learn like today uh you guys started in some java and uh i forget the oh some php objective c
*  objective c there you go uh yeah i mean in the end we all know javascript is going to win
*  uh and not typescript it's just it's going to be like vanilla javascript it's going to
*  eat the world and maybe a little bit php and i mean it also brings up the question of like i think don
*  knuth has a this idea that some percent of the population is geeks and like there's a particular
*  kind of psychology and mind required for programming and it feels like more and more that expands
*  the kind of person that should be able to can do great programming might expand
*  i think different people do programming for different reasons but i think the true maybe
*  like the best programmers um are the ones that really love just like absolutely love programming
*  for example they're folks in our team who literally when they're they get back from work they go and
*  work they go and then they boot up cursor and then they start coding on their side projects
*  for the entire night and they stay also 3 a.m doing that um and when they're sad they said
*  i just really need to code and i i think like you know there's there's that level of programmer
*  where like this obsession and love of programming um i think makes really the best programmers and
*  i think these types of people will really get into the details of how things work i guess the
*  question i'm asking that exact program let's think about that person when you're when the super tab
*  the super awesome praise be the tab is succeeds and you keep pressing tab that person in the team
*  loves to curse the tab more than anybody else yeah and it's also not just like like pressing
*  tab is like the just pressing tab that's like the easy way to say it and the catch phrase you know
*  but what you're actually doing when you're pressing tab is that you're you're injecting intent
*  all the time while you're doing it you're you're sometimes you're rejecting it sometimes you're
*  typing a few more characters um and and that's the way that you're um you're sort of shaping the
*  things that's being created and i think programming will change a lot to just what is it that you want
*  to make it's sort of higher bandwidth the communication to the computer just becomes
*  higher and higher bandwidth as opposed to like like just typing is much lower bandwidth than
*  than communicating intent i mean this goes to your uh manifesto titled engineering genius
*  we are an applied research lab building extraordinary productive human ai systems so
*  speaking to this like hybrid element uh to start we're building the engineer of the future a human
*  ai programmer that's an order of magnitude more effective than any one engineer this hybrid
*  engineer will have effortless control over their code base and no low entropy keystrokes they will
*  iterate at the speed of their judgment even in the most complex systems using a combination of ai
*  and human ingenuity they will outsmart and out engineer the best pure ai systems we are a group
*  of researchers and engineers we build software and models to invent at the edge of what's useful
*  and what's possible our work has already improved the lives of hundreds of thousands of programmers
*  and on the way to that we'll at least make programming more fun so thank you for talking
*  today thank you thanks for having us thank you thank you thanks for listening to this conversation
*  with michael swale arvid and aman to support this podcast please check out our sponsors in the
*  description and now let me leave you with a random funny and perhaps profound programming
*  code i saw on reddit nothing is as permanent as a temporary solution that works thank you for
*  listening and hope to see you next time
