---
Date Generated: September 05, 2024
Transcription Model: whisper medium 20231117
Length: 6013s
Video Keywords: []
Video Views: 799
Video Rating: None
Video Description: Nathan Labenz discusses the latest developments in California's AI bill SB 1047 with experts Nathan Calvin, Dean W. Ball, and Steve Newman. In this episode of The Cognitive Revolution, we explore the updated version of the bill, its implications for frontier AI companies, and the debate surrounding its potential impact. Join us for an insightful analysis of this crucial legislation and its role in shaping AI governance.

Apply to join over 400 founders and execs in the Turpentine Network: https://hmplogxqz0y.typeform.com/to/JCkphVqj


RECOMMENDED PODCAST: 1 to 100 | Hypergrowth Companies Worth Joining
Every week we sit down with the founder of a hyper-growth company you should consider joining. Our goal is to give you the inside story behind breakout, early stage companies potentially worth betting your career on. This season, discover how the founders of Modal Labs, Clay, Mercor, and more built their products, cultures, and companies.
Apple: https://podcasts.apple.com/podcast/id1762756034
Spotify:https://open.spotify.com/show/70NOWtWDY995C8qDqojxGw

RECOMMENDED PODCAST: Second Opinion
A new podcast for health-tech insiders from Christina Farr of the Second Opinion newsletter. Join Christina Farr, Luba Greenwood, and Ash Zenooz every week as they challenge industry experts with tough questions about the best bets in health-tech.
Apple Podcasts: https://podcasts.apple.com/us/podcast/id1759267211
Spotify: https://open.spotify.com/show/0A8NwQE976s32zdBbZw6bv


SPONSORS:
Building an enterprise-ready SaaS app? WorkOS has got you covered with easy-to-integrate APIs for SAML, SCIM, and more. Join top startups like Vercel, Perplexity, Jasper & Webflow in powering your app with WorkOS. Enjoy a free tier for up to 1M users! Start now at https://bit.ly/WorkOS-Turpentine-Network

Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

CHAPTERS:
(00:00:00) About the Show
(00:00:22) Sponsor: WorkOS
(00:01:22) About the Episode
(00:07:03) Introduction and Recap of SB 1047
(00:13:40) Key Changes and Current Status of SB 1047
(00:19:51) Sponsors: Oracle | Brave
(00:21:55) Dean's Perspective on SB 1047
(00:33:30) Sponsors: Omneky | Squad
(00:35:16) Steve's AI Sensemaking Project
(00:39:03) Differing Views on AI Regulation Necessity
(00:46:34) Nathan's Case for SB 1047
(00:55:07) Dean's Response and Liability Concerns
(01:10:48) Potential Scenarios and Impacts of SB 1047
(01:29:29) Final Thoughts and Predictions on SB 1047
(01:38:16) Closing Remarks on AI Policy Challenges
(01:39:51) Outro


---
SOCIAL LINKS:
Website : https://www.cognitiverevolution.ai
Twitter (Podcast) : https://x.com/cogrev_podcast
Twitter (Nathan) : https://x.com/labenz
LinkedIn : https://www.linkedin.com/in/nathanlabenz/
Youtube : https://www.youtube.com/@CognitiveRevolutionPodcast
Apple : https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify : https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Final Analysis on CA’s AI Bill SB 1047 with Nathan Calvin, Dean W. Ball, and Steve Newman
**Cognitive Revolution:** [August 24, 2024](https://www.youtube.com/watch?v=G8BXft-PEXo)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  This episode is brought to you by Work OS. If you're building a B2B SaaS application,
*  at some point your customers will start asking for enterprise features like SAML authentication,
*  SCIM provisioning, role-based access control, and audit trails. That's where Work OS comes in,
*  with easy to use and flexible APIs that help you ship enterprise features on day one without
*  slowing down your core product development. Today, some of the hottest startups in the
*  world are already powered by Work OS, including ones you probably know like Proplexity,
*  Vercell, Jasper, and Webflow. Work OS also provides a generous free tier of up to 1 million
*  monthly active users for user management, making it the perfect authentication and
*  authorization solution for growing companies. It comes standard with rich features like bot
*  protection, MFA, roles and permissions, and more. If you're currently looking to build SSO for your
*  first enterprise customer, you should consider using Work OS. Integrate in minutes and start
*  shipping enterprise plans today.
*  Hello, and welcome back to the Cognitive Revolution. Today, we're revisiting California's AI bill
*  SB 1047, the Safe and Secure Innovation for Frontier Artificial Intelligence Models Act.
*  If you haven't been following closely, we first covered this topic back in May.
*  At that time, the bill required Frontier model developers to provide reasonable assurance that
*  their models would not contribute to causing large-scale harms. And it was designed in such
*  a way that it would have applied to a greater and greater percentage of AI development over time.
*  I was inclined to support it, as it seemed to be a genuinely good faith effort to focus the
*  burden on frontier players in a way that likely wouldn't have much slowed practical adoption today.
*  Well, a lot has changed since then, and we're here to unpack the latest developments.
*  I'm joined once again by Nathan Calvin from the Center for AI Safety Action Fund,
*  one of the bill's co-sponsors, Dean W. Ball from the Mercatus Center, who's become a prominent
*  critic of the bill, and Steve Newman, who's working to elevate the discourse around AI issues
*  generally. Their perspectives have evolved along with the bill, and I think you'll find
*  our discussion both nuanced and hopefully illuminating. The updated version of SB 1047
*  is less ambitious, but in my view, probably better overall. It now places less emphasis
*  on concrete implementations of safeguards, applies only to models which cost $100 million
*  or more to develop, and has the primary effect of requiring frontier companies to develop and
*  publish safety plans and protocols. Given where we already are with AI development, I believe that
*  forcing the companies who are developing never-before-seen AI capabilities to disclose
*  their safety plans and protocols is simply a prudent step. With so many leading AI luminaries
*  sounding the alarm, all surveys of broader groups of AI researchers showing extreme uncertainty,
*  and all popular opinion polls and plain common sense supporting more investment in safety and
*  oversight for developers, it's really not too much for the state of California to ask.
*  With a final vote likely this week and the governor's decision not far behind,
*  I will say it plainly. If I were the governor, I would sign the bill. To be clear, that's not
*  a stance I've taken lately. I never thought the bill would be the crazy chill on AI research that
*  some had claimed, but there was a point when certain revisions seemed to grant what seemed to
*  me to be too much power to the now entirely removed frontier model board, and at that point,
*  I was inclined to withdraw my tentative support, as a misguided board could easily have done more
*  harm than good. The legislative process, however, despite some counterproductive hyperbole and
*  vitriol, which you've probably seen online, has ultimately seemingly landed in a pretty good place.
*  In the final analysis, as a friend of the show, Zvi Maszowitz aptly puts it,
*  this has primarily become a transparency bill. Anthropics Open Letter, which everyone seems to
*  be reading as a tacit endorsement, offers solid, plain-spoken analysis. Things are moving extremely
*  fast. We need to create incentives to identify and address extreme risks. Being honest with the
*  public is good. And while there are no perfect solutions at this point, the pros probably outweigh
*  the cons. On the other hand, OpenAI's letter, opposing the bill and calling instead for
*  clarity and certainty for AI developers from federal AI regulations, given the massive
*  confusion they've directly caused in so many ways over the last year, including the recent
*  strawberry emoji hypefest, really does not move me at all. And I say this as someone who is super
*  hyped myself about the future of OpenAI's products, including their advanced voice mode,
*  which I just started using this week, but that's a topic for another day.
*  If I have one remaining criticism of the current bill, it would be that the $10 million threshold
*  at which responsibility shifts from the original model developer to the fine tuner seems too high.
*  That is extremely rare air for a fine tuning budget and will apply to a very small number of
*  fine tuning projects. This seems both potentially unfair to Meta and seems to let everyday
*  application developers off a bit too easy. I don't think that we want to require lengthy published
*  policies from small application teams, but I do think that application developers should share in
*  responsibility, especially to the degree that they are selling autonomous or agent style products
*  that can take real world actions. For now, I want to extend my appreciation to Nathan Calvin,
*  Dan Hendricks, the Center for AI Safety and Senator Scott Weiner for their hard work and openness to
*  suggestions for improvement. Everything I've seen suggests that this is a Herculean labor of public
*  service for Senator Weiner and that he's been trying really hard to find the right compromise
*  that balances all interests. I also appreciate Dean for recognizing how much better the bill is now
*  as we reach the end of the process than it was in the beginning. He and other critics of the bill
*  deserve credit for the positive changes too, even if they still don't support the final product.
*  Finally, it's worth noting for those who may know Dan Hendricks only from these policy debates
*  that he is actually a world-class researcher. His recent work on tamper-resistant safeguards
*  for open-weight language models while still early in development holds the promise of making it
*  possible for a company like Metta to remove harmful behavior in a way that downstream users
*  could not easily undo, which is unfortunately the case for today's safety techniques.
*  I hope to have Dan on for a technical research-oriented episode covering this
*  and other topics soon. As always, if you're finding value in the show, we'd appreciate it
*  if you'd take a moment to share it with friends. I always welcome your messages either via our
*  website, cognitiverevolution.ai, or you can DM me on any social network. Now, let's review the final
*  version of California's AI Bill SB 1047 with Nathan Calvin, Dean W. Ball, and Steve Newman.
*  Nathan Calvin from the Center for AI Safety, Dean Ball from the Riketa Center, and Steve Newman
*  from an AI Sense-Making Project, which might soon have an official name. Welcome back to
*  the Cognitive Revolution. Very glad to be back. Really, not much has happened at all since the
*  last time we spoke, so probably shouldn't be much to be able to dig into. No, I get it. But yeah,
*  happy to just chat a little bit with what has changed in terms of SB 1047 since we last spoke.
*  I think when we were last speaking, the bill was still in the Senate or maybe just past the Senate
*  and can give a brief overview about where we're at now and what ways the bill has changed and what
*  the weeks ahead could look like. Cool. Sounds great. Just as one more note of introduction,
*  I think last time we had a really nice, good faith and positive, constructive conversation,
*  which I think unto itself was really well received. So I would compliment all three of you
*  for making that happen. Look forward to more of the same. And I do think people are going to need
*  the recap because even I, as someone who basically tries to keep up with AI developments full-time
*  at times over the legislative process between the last episode, which wasn't that long ago and now
*  felt like I had kind of lost the thread. So definitely a little bit of what has happened
*  and where we've ended up now would be, I think, really useful starting context.
*  Yeah, absolutely. So I think the, just very briefly, so yeah, SB 1047 introduced by the
*  state Senator Scott Wiener from San Francisco. The bill is co-sponsored by our organization,
*  the Center for ASAPE Action Fund, as well as the Economic Security California Action and Encode
*  Justice. And since we last spoke, the bill has continued to move through the legislative process
*  and has been amended pretty significantly in my view in some different ways. I think some of those
*  amendments have come through the committee process. So just like in the process of a bill becoming
*  law in both federally and in California, bills are referred to different, both policy committees
*  as well as fiscal committees. And one of the committees that we referred to in the assembly
*  was the Assembly Privacy and Consumer Protection Committee, which is chaired by Chair Bauer Kehan,
*  who is quite interested in this bill and worked quite a lot with the committee consultants there,
*  as well as the committee consultants in the Assembly Judiciary Committee chaired by Ash Kalra.
*  In addition to that, the Senator also continued quite a lot of dialogue with different folks in
*  SF and parts of the business community. I think one really notable part of that was some of the
*  engagement from Anthropic and then also recently from OpenAI as well. I think when we last spoke,
*  those companies had each not really publicly weighed in on the bill. There were some conversations,
*  but not anything that we could talk about in detail. And since then, that's changed a bit. So
*  Anthropic submitted a supportive amended letter laying out kind of areas that they liked about
*  the bill and areas where they had concerns and wanted changes. And the Senator's office and the
*  co-sponsors worked with the committee staff around adopting a good fraction of those changes,
*  certainly not all of them. And some of them were in modified form. And I think some of the most
*  notable changes that came out of that process were there is no longer a new division of the
*  Government Operations Agency to be created. It was previously out of the Frontier Model Division.
*  Some of those functions have been incorporated now into the Government Operations Agency. I know
*  one area of contention I'm sure we'll get into is to what extent is the, for folks like Dean who
*  have concerns about the FMD, to what extent do those concerns still exist? To what extent are
*  they addressed? I think some other things, the bill previously contained provisions that submissions
*  to the government around this were, one thing was that they were both more private, but then also
*  under a penalty of perjury. And now those submissions, some of them are public and with
*  the ability for the company to insert redactions and then also no longer under penalty of perjury.
*  Another change that the bill had some non-discrimination and pricing transparency
*  requirements that apply to cloud computing providers and developers. Those have been
*  struck from the bill and are no longer present. I think another big change, which is maybe a little
*  bit subtle and vaguely in the weeds, but I do think is important is previously one of the signature
*  kind of lines in the bill was asking for companies to provide reasonable assurance that their models
*  won't pose risk of these critical harms. That language has been modified to saying that they
*  have to take reasonable care to prevent unreasonable risk. Reasonable care is the standard that
*  exists in the background law. And so it's something that companies have to do in general. And we can
*  talk about to what extent this modifying those obligations versus kind of reminding them of
*  obligations that already exist. Yeah, I think those are some of the big ones that come out.
*  And in part, as a result of those changes, Anthropic recently came out with a letter kind of
*  sharing their thoughts and they didn't go all the way to formally supporting the bill, but they did
*  say that they think that this is workable and they believe that their current best guess is that the
*  benefits outweigh the costs and that these risks are real and that compliance is feasible.
*  I think we've also seen since then some engagement on the other side of we've seen OpenAI come out
*  with a pretty strong opposition letter. We also saw today some of the former employees from OpenAI
*  who had left the company in part over disagreements with the company's approach to safety coming out
*  with then some criticisms of OpenAI's letter. We've also seen some engagement from federal
*  officials, including Speaker Emerita Nancy Pelosi, raising concerns with the bill. And so where this
*  all sits is everyone is it's all kind of ramping up to a head. The bill has passed all of the
*  committees and needs to be voted on by the assembly and then reconciled by the state Senate
*  sometime before August 31st. Assuming that it does pass the assembly and is reconciled by the
*  state Senate, then it will go to Governor Newsom for him to either sign the bill or veto the bill.
*  So it's where we've gone through the process, lots of changes, some concerns addressed, some
*  concerns not addressed, some people who are happier and some people who are more left happy.
*  Happy to dive into where that stands and kind of how people feel versus when we were previously
*  talking where the bill's final form was still much more in flux. So anyway, that's a high-level
*  overview. I'm sure we'll get into more of it, but hopefully that's helpful to people who have
*  not been following this full-time.
*  And it has approached, I know you've been in a full-time, it has been a full-time job for a few.
*  We're lucky to have a couple who've been full-time or nearly so on the call here. So let me try just
*  a short restatement of that and see if you agree with my summary. And then I'll ask Dee to give his
*  history or sort of the journey that he's been on as the thing has evolved.
*  And I'd definitely give credit to Zvi for, as always, the super comprehensive write-ups.
*  If you're not following Zvi, you should be, and you should go to thezvi.substack.com to subscribe
*  to his regular and very thorough AI roundups on all things AI, not just policy.
*  Okay. So here's my attempt. It seemed like the original version was raising the standard
*  that the model developers had to live up to relative to background law.
*  And I remember Senator Weiner saying, this is about minimizing risk. It's not about eliminating
*  risk, but it's at least about making sure that they're going to do what we think are light touch
*  things to minimize risk. And if they don't do that, then there are some consequences,
*  not extreme consequences. If you were both not doing your testing or outright lying about your
*  testing to the government, then you could potentially get into even perjury trouble.
*  But main effect, as I understood it originally, was to raise the standard of care in this model
*  development and release process. And then there was sort of a government mechanism that was going
*  to be created, which was this board that was going to be responsible for setting what the
*  standards were going to be and maintaining them going forward through time. That now seems to be,
*  and there were some other things, we'll leave the other things aside,
*  price and transparency, Cal compute, whatever, a little bit of a grab bag of other stuff.
*  Now it seems like, as you said, the standard has been returned basically to the normal background
*  standard of law, which is reasonable care, which my understanding, and I'm definitely no expert is
*  like basically any company that's creating and selling products in the market has that standard
*  as kind of the baseline. If they don't live up to that, regardless of what business they're in,
*  they could be sued. Now that's the standard. And what really seems to be the most important
*  thing that they'll be required to do, they wouldn't be required to do before,
*  is publish their safety plans and to at least some degree with some wiggle room for redaction,
*  the results of their testing. So Zvi ultimately calls this largely a transparency bill in as much
*  as right now, most of these companies have committed to doing something like this,
*  but the degree to which they are public about it is not so much the focus of their commitments.
*  They're sort of saying, we'll do it, but we may or may not tell you how much we're doing along the
*  way. The board meanwhile has been, I think this again might be somewhat contentious, but it seems
*  to be in its original form is just no longer there. There is still some government guidance,
*  I guess, to be provided on these standards and presumably like how liable you ultimately are as
*  a model developer depends on how well you've lived up to general market standards and the guidance
*  from the government. And then one of the things that seems like it really jumps out at me is
*  the thresholds now have these like firm dollar values where if previously it was like 20,
*  however many flops in 2024 dollars and that was all like, nobody kind of knew how that was going
*  to evolve. And now it's like a hundred million bucks, you're covered if you're doing it from
*  scratch, 10 million if you're fine tuning. And those numbers are like written in and theoretically
*  shouldn't change. I tried to be brief. That was still kind of a long summary. How did I do?
*  Yeah, I think that was a good summary. I think the couple of things that I would add some slight
*  modifications to, and I'm sure Dean has a lot of thoughts as well, kind of more on the merits here.
*  So one thing was that there was never formal, like previously the Frontier Model Vision was also
*  still promulgating guidance rather than mandatory rules. There actually is partially from the,
*  this was something that was added in by the Privacy Committee and then actually the Recent
*  Appropriations Committee further formalized is that in addition to the guidance from two model
*  developers, there are also guidance and intact rules for auditors. So companies starting in,
*  I believe 2026 have to use some third party auditor. They can pick what auditor they want to use.
*  And there are then rules that DevOps is putting out about how to do a good clean audit is the
*  idea. It's fairly narrow in terms of what those rules are about. And it's not meant to be rules
*  on the merits of system development, but more really like how you do a good and fair audit,
*  such that there's not like a race to the bottom here. But that's the thing I would add. I do think
*  there still is an aspect where the standard is reasonable care. That's a standard that exists
*  in background law, but it is necessarily both a bug and a feature. It is vague. And I think that
*  what it means for a Frontier Model developer to exercise reasonable care is unclear. And I do
*  expect that it will be part of what this bill is saying is that what that means is partially informed
*  by things like the NIST ASAP Institute, which is called out things like the guidelines that the
*  government operations agency will be putting out. So it's not again saying that you have to do it,
*  but it's starting to say that like the legislature is speaking and saying that, you know, part of
*  what it means to take reasonable care in this setting involves caring about cybersecurity,
*  doing testing, thinking about how others might misuse your models in really bad ways. And again,
*  to some degree, that's not necessarily like formally, you know, I think there are people
*  who effectively believe that is what the current law maybe already requires, that there may already
*  be suits under that. But this is kind of further adding additional detail to that is, I think,
*  the sense. And anyway, Dean can give his reactions are kind of different interpretation about how
*  the main ways in which he thinks this changes versus what the status quo is. I think one just
*  other thing I had thought, but I lost it. So I'll pass it over to Dean. Thanks for letting me talk
*  for a bit there. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry,
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing. And of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive of OCI at oracle.com.
*  That's oracle.com slash cognitive, oracle.com slash cognitive.
*  This episode of the Cognitive Revolution is sponsored by the Brave Search API. You may know
*  if Brave has an alternative to Chrome, but did you know that Brave has its own independent search
*  engine powered by its own 20 billion page index of the web? The Brave Search API gives developers
*  reliable and affordable access to programmable web search, auto suggest, spell check, and more.
*  With flexible plans for all types of use cases from rag search to automated business intelligence.
*  On top of that, it's up to three times cheaper than Bing, all without compromising on quality,
*  speed, or reliability. Over 700 businesses, including Cohere, Chegg, and Kagi, rely on the
*  Brave Search API. And a recent survey showed that 94% of customers would recommend it to their
*  peers. To start building apps with the power of the web, sign up at brave.com slash API and get
*  up to 5,000 free monthly calls. Cool. Yeah. So I think that the summary from both Nathan Calvin
*  and Nathan LeBenz is like, I think on a factual basis, it's all correct. So I have no knits to
*  pick with the summaries. I do still have knits to pick with SB 1047, but I would say broadly,
*  the bill is very much improved from where we started in February, I think quite significantly
*  improved. And it's improved, in fact, to the point that I would argue that there are other bills
*  being considered in California right now to regulate AI that I think would be worse in many,
*  many different ways. Up until very recently, there was a bill called AB 2930 that would
*  essentially require everyone and their mother to write an algorithmic impact study. Basically,
*  every time they used it, any time a business uses AI, your electrician would have to do an
*  algorithmic impact study if they wanted to use AI to write bids for customers or something.
*  It was a crazy, wild thing. That actually got walked back. But nonetheless, there were bills
*  and are still bills that are in many ways much more problematic than SB 1047. I think,
*  so I'll talk about my reaction to the current bill and I'll go from some of the smaller points
*  and then in increasing levels of macro perspective. So on a smaller level, yeah, I think the frontier
*  model division itself is gone. Some of its powers are walked back and others are maintained and
*  housed inside of this agency within California. It is worth noting, and this has been true
*  throughout the bill, and I actually did not fully realize this until recently in a Twitter conversation
*  with Jen Polka, but this is kind of like the agency of the California government that provides
*  back office internal functions, like HR, IT, things of this kind. At the federal level,
*  this is called the GSA, the General Services Administration, the sort of analog here.
*  That's not an entity that can appropriately regulate AI. They don't have the institutional
*  culture to do this. They provide IT, not regulate frontier technology. I know that there are some
*  technology regulation things that the Department of Technology does, which is part of GovOps.
*  Sorry, I'm getting into the institutional weeds here. But yeah, it seems like this agency is not
*  well positioned to do this. And it also seems to me that they have some pretty significant powers
*  still. Guidelines, these things often don't sound like a big deal because they're not binding and
*  things like that. The reality, though, is that very often, this is something called soft law.
*  And I think that soft law is a major part of how AI is going to be regulated. Soft law is really
*  informal, and it has some benefits because it gives you flexibility. So my mind's not made up. I'm not
*  saying soft law is good or bad. They're just trade-offs associated with it. It has some benefits.
*  It also lends itself to very arbitrary governance. Just as an example on open source stuff,
*  Lena Kahn put out a blog post in a tweet thread the other day a couple weeks ago now, maybe months
*  ago. She said, I like open source AI. And then she said, but if you go from open to closed,
*  we will look down upon that and implying that the FTC might bring an enforcement action against you
*  if you were a prominent provider of open source models and then you begin closed sourcing them.
*  It seems to me that, first of all, I think that when the FTC was being created, this is not
*  what the kind of policy decision that the Federal Trade Commission is supposed to be
*  making, but we're well past that. We're well past that with the FTC. They do a lot of things that
*  I think are beyond the scope of what they're supposed to be doing. But more to the point,
*  from a safety perspective, if meta all of a sudden, let's say that we go into a world where it's very
*  dangerous to release LAMA-5 and meta is of two minds about it, but they think that if they make
*  it closed source, the FTC is going to go after them. And you now have different parts of the
*  government saying different things. And so those are the kind of problems that softlock can lead
*  to. So I think that these guidelines are probably necessary to some extent from a group like the
*  AISI, AI Safety Institute, but I'm not sure that this agency in California can do them well. And
*  I think that they also could be abused. Same thing is true of the auditor rules. I think that
*  could in theory be abused in all sorts of different ways. For example, they could say in order to do a
*  good audit, you have to be able to look at the usage data for the model. You have to be able to
*  see what people are using, customers, users are using the models for. Well, an open source provider
*  can't do that. So all of a sudden now you can't get an audit, right? And you have to have the audit
*  to pass the bill. So like right there is like one way that you could in theory maybe do this,
*  right? I haven't thought like super detailed about this, but you know, that would be an example.
*  So then there's other nitpicks I have, which I'd be happy to get into. But then like moving up
*  another level, I think there are serious questions to me about whether or not the government of
*  California should be doing this. And to give you like my take on the last maybe five to 10 years
*  of technology regulation in the West is that policymakers in two important capitals realized
*  that there was a big opportunity to regulate technology on behalf of at least the entire West
*  and maybe the whole world, Brussels and Sacramento. They came to this realization. And so now we have
*  a lot of regulations that have been passed on our companies, American companies, that the American
*  federal government had essentially no hand in crafting. This is problematic from a sovereignty
*  perspective. And I'm not saying that SB 1047 necessarily does this. I think if we continue
*  going in this direction where like, I just don't think the rest of this country is going to submit
*  to Sacramento governing technology use throughout the entire country, I'm not saying that there's
*  no role for state governments in tech regulation, but I think that could be seriously problematic,
*  very, very deeply. I think America, people talk about national divorce relatively seriously,
*  about the idea of the country fragmenting. This is one avenue upon which this could occur. If
*  there's serious disagreements about different policy regimes, about how we're going to regulate
*  AI and Texas wants to do something different from what California wants to do, well, you could start
*  running into serious problems there because I don't think Texas wants to be regulated by
*  Sacramento. That's my thesis. I'm pretty sure I'm right about that. I don't know if Texas realizes,
*  I don't know if people have woken up to this, but I believe that they will. And I believe when it
*  does, it's going to be ugly. So not only do I think that there's a competence question with the
*  California government, but I actually think that at a structural level, how, and by the way, I
*  should have said this as a factual matter, SB 1047 applies to companies throughout the United States,
*  assuming that they do business in California, which means basically if the model is distributed
*  in the state of California. So I just think that is going to exacerbate a structural problem that
*  we have that our constitution just didn't anticipate. So the whole interstate commerce question,
*  and obviously the internet, the constitution just didn't anticipate how this would work.
*  And so I really don't think that California should be doing this. Obviously also it has
*  their national security implications of this bill. And California's government can't possibly
*  be well positioned to sort of grapple those questions in an educated manner.
*  And then the last thing I'll say before I stop talking is this is model-based legislation,
*  right? I've talked in my writing and in lectures and stuff about the different frameworks for
*  regulating AI. Do you regulate people's conduct with AI? Do you create normative standards for
*  their use of AI? Do you say like, well, if you're going to use AI in healthcare, here's the standards,
*  but if you're going to do it in banking, there's other standards. Or do you regulate the models
*  themselves? My thesis is that all three of these things are going to be necessary. But my thesis
*  is also that model-based legislation is very costly, potentially very costly. It's not the
*  way we've traditionally regulated software. So it's a big break from the status quo.
*  And it requires us to give up things about the status quo that we like. The permissionless
*  nature of innovation, for example, the fact that anyone can just make software and put it out in
*  the world. The lack of liability, right? Like it's pretty hard to sue someone who makes software,
*  even if they have a bug in their software that costs you money. Yeah, you will struggle to sue
*  them in like a lot of practical context. You will struggle with the company that made that software
*  for like negligence. So we are, with SB 1047, we're not like radically, I'm sorry, not aggressively
*  attacking these foundational aspects of the modern economy, but we are lightly attacking them. And
*  this is one of those things where it's like being a little bit pregnant. It is kind of a binary.
*  Once we step over into that world, we've made a radical step, even if it's a small step in the
*  like sort of magnitude, it's still a radical step because it's a totally different policy regime.
*  And I think that to justify that, for just generally applicable, like all frontier models
*  have to be regulated in this way. I think we need a lot of evidence that we're heading in a world
*  where short timelines to AGI, very dramatic increase in AI capabilities over the next
*  five years, let's just say five to 10 years, something like that. And I haven't seen that
*  evidence. I mean, I know some very smart people who think it, and I know there's very smart people
*  who are spending a lot of money on this thesis, on believing this thesis right now. So I'm very open
*  to the possibility that it's true, but there's also a lot of compelling arguments on the other
*  side. You had Martin Casado, Nathan, on your podcast a couple of maybe like a month or so ago.
*  And Martin Casado, I think, gave a really good explanation of sort of his perspective on this.
*  Basically, like, we're just curve fitting and there's going to be asymptotic progress as we
*  fit the curve a little bit better. And the world is heavy tailed, which means that a lot of novel
*  things happen a lot of the time. And because you're just matching a statistical distribution,
*  the models are going to struggle with that. That's empirically true with things like self-driving
*  cars, right? We have seen this for like, I think self-driving cars are like the closest that we've
*  come to AGI, right? Like to like an AGI-esque problem. And this is like an empirical truth that
*  we've observed. So there's like, I'm of two minds, I'm not convinced either way. And I think that
*  if it really is true that we're heading towards AGI in the next five years, then like the revolution
*  in human affairs that will constitute and the radical new kinds of governance institutions that
*  we will need to have a chance at keeping a handle on that technology will be profound. And like,
*  I spend a lot of my time doing work like that. But I'm not 100% sure it's necessary yet. And I
*  think we're going to have to make this decision under some degree of uncertainty. But I think we
*  just have too much uncertainty right now. So that's my shtick. Hey, we'll continue our interview in a
*  moment after a word from our sponsors. Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work customized across all platforms
*  with a click of a button. I believe in Omniki so much that I invested in it. And I recommend you
*  use it too. Use Cogrev to get a 10% discount. Hey all, Eric Torenberg here. I'm hearing more and
*  more that founders want to get profitable and do more with less, especially with engineering.
*  Listen, I love your 30 year old ex-fang senior software engineer as much as the next guy,
*  but honestly, I can't afford them anymore. Founders everywhere are trying to turn to global
*  talent, but boy is it a hassle to do at scale from sourcing to interviewing to on the ground
*  operations and management. That's why I teamed up with Sean Lennahan, who's been building engineering
*  teams in Vietnam at a very high level for over five years to help you access global engineering
*  without the headache. SQUAD, Sean's new company, takes care of sourcing, legal compliance, and
*  local HR for global talent so you don't have to. With teams across Asia and South America, we can
*  cover you no matter which time zone you operate in. Their engineers follow your process and use your
*  tools. They work with React, Next.js, or your favorite front-end frameworks. And on the back end,
*  they're experts at Node, Python, Java, and anything under the sun. Full disclosure, it's going to cost
*  more than the random person you found on Upwork that's doing two hours of work per week but billing
*  you for 40. But you'll get premium quality at a fraction of the typical cost. Our engineers are
*  vetted top 1% talent and actually working hard for you every day. Increase your velocity without
*  amping up burn. Head to choose squad.com and mention Turpentine to skip the wait list.
*  Thank you. Steve, you have observed, as I think many of us have outside of the friendly confines of
*  the cognitive revolution, that the discourse around AI is kind of coarsening and you're
*  aiming to do something about it. I'd love to give you the chance to just talk a little bit about
*  your motivation, what you're doing, and then you can kind of help guide the discussion from here.
*  I thought you had some kind of tips on how to do that. I'm going to start with you, Steve.
*  I think that's a good question. That would be a nice way to open up the conversation.
*  Yeah, thank you. So, yeah, you bring up the whole question around the conversation around AI.
*  And when I talk about the, when I refer to the conversation around AI, you know, there's a
*  thousand different questions and topics, right? The many of which we've touched on already in this
*  conversation. What pace is the technology progressing? How quickly are capabilities
*  of these models going to advance? What impact is that going to have on the world? Positive impacts,
*  who should control it? How should it be controlled? There's all these broad questions and it
*  immediately gets down into 10,000 specific questions. What are the implications for
*  biotechnology, for the job market, for cybersecurity? And, you know, so there's,
*  it's this huge thing. We talked, you know, somebody commented at the beginning of this
*  conversation that even just to keep up with developments in SB 1047 for people like us who
*  are pretty focused on AI is impossible, let alone that, you know, so there's so much going on.
*  It draws on all these different, not just AI and computer science, but biotechnology and
*  cyber technology and all these other topics. So there's all kinds of different expertise
*  that are relevant. It's all moving very quickly. It's all moving into kind of uncharted territory.
*  I think it's hard for all of us to keep up and the conversations that crop up around it,
*  especially conversations in the public sphere on Twitter and Substack and so forth,
*  it can get contentious. It can get fragmented. There's miscommunication, there's misunderstandings.
*  And that's the situation that I'm looking at and starting an initiative to try to do a little bit
*  something about. And briefly, the idea is to, there's a motto or mission statement I've been
*  playing with, which is modeled after Google's old mission statement, and which is to say,
*  so this version is to take the AI world's disagreements and make them use universally
*  constructive and accessible. So basically, there's all this, lots of people with thoughts and
*  opinions and ideas to share and things they're mad about and things they're happy about and
*  whatever. And, but this is all over the internet. Some of it is taking place in forums that are not
*  conducive to constructive discussion or just not conducive to, you know, it's in a private chat group
*  or something and other people can't find it. So the idea is to create a new place on the internet
*  where people go to have constructive conversations about all these different questions and then have
*  an editing process attached to that to create explainers. And okay, there's been this extensive
*  discussion of how feasible is it really? How much should we worry that an AI model,
*  FFLD4, will let someone create a super virus? Is that a real thing? Or, you know, it's not a real
*  thing because the people who might do what we don't want them to do can't get access to the
*  lab equipment anyway, or we can just screen it out in the DNA synthesizer or something. So a deep
*  dive on this very arcane topic, but an arcane topic that has important policy implications.
*  You know, we had some long discussion on within this forum that 99.9% of the population is never
*  going to want to follow that long discussion, but here's the one page explainer that we distilled
*  from that. And if you disagree with our one page explainer, come participate in the conversation.
*  And our commitment is that what goes on in the conversation then shows up in the explainer
*  website. So that's the idea, just getting started. But that's the project.
*  So one of the things that we have been discussing and I've been a minor participant in one is just
*  under what circumstances are these regulations needed and are they properly done at the model
*  level? I feel like one big fault, I think you might have even distilled this for me most
*  usefully at one point, which is just a lot of the different intuitions that we hear seem to be at
*  root a question of just how powerful is AI going to get how soon. People who think it's likely to
*  get very powerful tend to want to do stuff and they tend to be more willing to pay certain costs.
*  People who don't think that's going to happen obviously don't feel the need to pay the costs.
*  I'm not sure that's what's going on here though. I guess you guys could maybe each address this
*  for yourselves, but also maybe on a more meta level, like Anthropic and OpenAI both seem to
*  believe we're headed for very powerful AI quite soon. And they come out still on seemingly
*  different sides of this question of this bill. So would you guys say that this is the core
*  thing for you or Dean, if you were more confident in powerful AI or some early
*  AGI in 2027 as the profits are currently foretelling, would you say, yeah, okay,
*  fine, we'll have to take some risks with the GovOps, people perhaps go in rogue.
*  Is that like the central thing? And if it is for you, like, how do you account for the broader
*  landscape of disagreement? And actually, let me just throw in another aspect to that, which is,
*  it seems to me, and actually, I went and relistens to our previous discussion from a few months ago.
*  And something that came out of that for me is it seems like I feel like a lot of the disagreements,
*  and I'm talking about the broad conversation, not just the conversation we had a few months ago on
*  the podcast, there's a lot of different maybe intuitions as to what the impact of the bill
*  might be. Okay, we all can see the language of the bill, but there's a lot of, then, oh, you know,
*  that depends on how is it going to be interpreted by people in Sacramento, by lawyers, how are the
*  AI development labs going to react to that language and gets into questions of trust, you know, do we
*  trust the regulators to kind of take a light touch or sort of good faith spirit of the bill, or, you
*  know, we're really worried that this is going to be a slippery slope, a regulatory ratchet, which is
*  certainly something we've seen happen in other domains. Conversely, if we stick to more of the
*  voluntary regime that maybe is in effect today, we see a lot of the AI labs putting out responsible
*  scaling policies and so talking pretty good game and clearly walking at least some of that walk.
*  But do we trust that that will continue or under competitive pressures, will we see them, you know,
*  companies start even were very well intentioned today, maybe start to take shortcuts over time,
*  which is also a thing that so it feels like there's a lot of very legitimate room for very
*  different anticipation of how this will play out in practice with the passing or not passing the
*  bill would be and trust in the various actors in government and in industry for how they would play
*  their hand. Yeah, so I think the disagreement between open AI and anthropic is like actually
*  at a pretty fundamental level, jurisdictional. I mean, you could take a more cynical view,
*  but I choose not to do that. So yeah, I mean, open AI doesn't care about safety and they don't
*  want to be regulated, right? People could say that. I don't think that's true. But more like
*  if you look at open AI's letter explaining why they oppose the bill, it's they do they talk a
*  lot about how they don't think California is well suited to do this. They don't care my structural
*  political concerns about the country falling apart, but they should because they might play
*  a huge role in it if that does happen. So yeah, but I do think that the question of like jurisdictional
*  competence is a big one for them. But I think more broadly, Nathan, Calvin, I'd be interested
*  for your thoughts on this too. But I think that this is the fundamental question. Like for I mean,
*  I can't say what's in other people's heads. Certainly, it's for me, the fundamental question.
*  And I think for many other people, it really is a question of like, are we talking about massive
*  qualitative leaps in AI capabilities every 18 to 24 months for the next minimum six years? Like
*  is Leopold Aschenbrenner right? I'm not trying to say that everyone who supports 1047 thinks
*  that Leopold Aschenbrenner is right. But like, are we going to be building the trillion dollar,
*  you know, compute cluster with 50 nuclear reactors in what, four years, three and a half years? Are
*  we going to be doing that? Because that's got some work to do if that's true. But like, so I do think
*  it's a very deep and fundamental issue there. And oh, I want to say one thing about like, potential
*  impact of the bill. So I do have major political economy concerns with AI regulation. I mean,
*  this is a very tricky thing to regulate, like, just in general, and particularly for a centralized
*  office to regulate. Now, I don't really think that GovOps is like, they're not like the FDA of AI,
*  right? Like, that's not how that would work. I think there's two ways it could go, each of which
*  is concerning to me. Well, there's many ways it could go. But there's two I think about a lot.
*  One is kind of what I've described in a lot of my writing, where the political economy basically
*  concern is that AI threatens certain entrenched actors in our economy, the healthcare system,
*  the hospital system, many people in the knowledge economy, like lawyers, teachers, right? These are
*  very powerful interest groups in the state of California in particular. And government employees
*  themselves, by the way, are a major, like probably the most important interest group in California.
*  Is the government, which is part of why California has a lot of problems and a lot of America has a
*  lot of problems. That's a separate question. And that basically they will use this regulatory
*  regime, which will be expanded over time as well to, you know, restrict AI in a thousand different
*  ways and make it so that it can't be used for blah, blah, blah, blah, blah. And I think this
*  is already going to be a huge fight no matter what. And that giving more tools to the entrenched
*  forces of the status quo seems like not maybe a great idea. Another way it could go though,
*  is actually more like, you know, the AI Safety Institute and the DevOps people,
*  they write their guidelines and the guidelines are like 36 page memos that are like, you should do a
*  good job. And you should think about safety and you should think about risk and you should mitigate
*  risks. And there's flow charts and Venn diagrams and stuff like that. And the AI companies look at
*  that and they're like, cool, you guys, DevOps, don't have $10 billion compute clusters. We do.
*  We know what's going on. We're way ahead of you. And they're not really in a position to like
*  actually do a good job of this. And so instead they've released kind of generic box checking
*  exercises. Perhaps it even forms into a kind of regulatory capture. And but actually not really
*  to keep other players out, but more just like, oh yeah, generic stuff. And then it becomes a box
*  checking exercise and something really bad happens because everyone was asleep at the switch,
*  because we got complacent and we thought like, oh yeah, well, checking the boxes,
*  that's all you got to do. And then there were some unknown that we didn't consider in a way that maybe
*  we could have. So those are like two potential ways that it could play out. I don't really know
*  which one of those is likelier, but yeah, like I think the impact is definitely hard to game out,
*  especially with these revisions. Like with these revisions, I will say my political economy concerns
*  about what GovOps would do are meaningfully significantly lower than they were when I,
*  you know, in the first few months of analyzing the book.
*  I feel like there are a lot of things in what Dean and other folks are saying that I
*  wouldn't helpful for me to just kind of respond to if that works. Yeah, a high level just to like
*  lay out what I think. I think I talked previously about what has changed, but I do just want to lay
*  out and I think some of this has been mentioned about like what the central case in favor of the
*  bill is. And kind of there are a few parts of this argument. I think the first part is that
*  there is at least substantial disagreement and uncertainty about the extent to which
*  really severe catastrophic risks from AI could happen and whether they could happen on the order
*  of years rather than decades. There's disagreement within the scientific community. There's
*  disagreement within businesses. But when I speak with folks at the labs and again, folks who have
*  different perspectives on this bill, they very much believe that this is not something that is
*  just the same as software and email and social networks and previous technology. They believe
*  they're doing something incredibly significant. And when I talk to folks like Professor Jeffrey
*  Hinton and Professor Yasha Benjio, they very much share that view. And I think when people like that
*  are raising those concerns, it's worth taking seriously. I think the next part is that companies
*  have been agreeing to some of these voluntary commitments, saying that they do take these risks
*  seriously and that they're going to do safety testing and take mitigation seriously and take
*  cybersecurity seriously. But at the same time that's happening, I think we are seeing evidence,
*  including from people within those companies who've left, that when there is immense commercial
*  pressure and when this is something that is left to being completely voluntary, they are not
*  necessarily actually going to take those things particularly seriously. And that they will say
*  they're going to do this, but the extent and quality of which they're going to do that is very,
*  very unclear. And some of the main thesis of this bill is I think a few things. I think one part of
*  it is that it's very important to remind companies of the extent to which they have obligations
*  under existing law to take reasonable care. I think it's one thing for that to be something that
*  exists in the common law in a more conceptual way versus it to be like in a statute really
*  directly in front of the people in the C-suite reminding them of this fact. They also need to be
*  transparent about the effect to which they are actually taking these precautions and have
*  employees when they do have concerns being able to actually speak to someone, speak to folks and
*  raise those concerns. And then the last thing I think is just very important to say is that,
*  look, we are in a federalist system. If Congress wants to pass legislation in this space to
*  preempt this bill, that is something that they have every power to have. I know that Dean has
*  advocating for them doing so without even regulating in this space, but even in the absence
*  of that, just simply saying that this is not something that states should do. I agree that
*  there are advantages to doing this at the federal level. I worked in the US Senate for a year. I
*  think that it is an institution that has virtues, but I think one of those virtues is not necessarily
*  responding at the speed of exponential technology development. And also when you combine that with,
*  well, maybe you could say it should be handled at the federal level, but through agencies that
*  are more adaptable and can respond to things more quickly. But then at the same time, you also have
*  courts saying that agencies really can't legislate outside of very explicit statutory authority. We
*  saw a court strike down the FTC's rules on banning non-competes saying that exceeded their statutory
*  authority under local right, local right, which is like overruling the Chevron doctrine, which gave
*  more deference to agencies. So I agree there are advantages to doing this federally, but I think
*  that when we have these folks saying that these risks are pretty serious, I think that
*  waiting for them to get there, in particular for Congress to get its act together on this,
*  I think does not seem like a really credible plan to me. And one thing I will say is that there have
*  been, and I'm curious to see his stake on this as well, there are parts of this discourse around the
*  bill that I think have been pretty wonderful and great, and actually genuinely do make me more
*  optimistic about the virtues of a open and transparent and lengthy legislative process.
*  I mean, there have been things where it's like getting this bill that the Senator's office and
*  the co-sponsors worked on quite a bit, kind of red teamed in real time by smart people on the
*  internet, noticing things that we didn't notice. There are folks like Charles Foster, someone who
*  comes to mind, and this person on Twitter who just knows every part of the bill and is very
*  involved with it and suggested changes that there was a real thing between what some people who were
*  very online in the AI community were suggesting and some of the amendments that got adopted.
*  I think one of the really big ones is around the scope of the covered models and saying that, look,
*  if you have this flat compute threshold, as that becomes cheaper over time, that will affect a lot
*  of people and that that's problematic. And a bunch of other things too. And so I think a lot
*  are real virtues there. I think at the same time, there has also just been stuff that I think has
*  been pretty frustrating in terms of, yeah, I think folks really just using this as a thing of like,
*  yeah, just stuff that's kind of wild, where it's just pretty weird to me that when this bill was
*  initially becoming controversial in May, that there was tons and tons of discourse about,
*  obviously, this is a regulatory capture play, where OpenAI is doing this and they're the
*  ones supporting it. And I did not see a single one of those people who were saying that after
*  OpenAI came out in opposition say, oops, I guess I was wrong and that was not what the purpose of
*  this bill was. We're just like saying things about the bill that I think were just false.
*  I don't think Dean's at all has been in that camp, but I think there have been a lot of folks who
*  have and that's been, I think, challenging. I do want to say there are like just a few other
*  things I want to quickly touch on, which is, to what extent does legislation kind of in the shape
*  of 1047 require you to buy into specific arguments about the nature of AI as a technology and kind of
*  when specific risks might arise? And I think it really doesn't to the same extent that we are
*  maybe implying that it does. I agree that if you were doing like, certainly if you're advocating
*  for an international pause, like that's based on a very specific model of what we think the benefits
*  and costs of this technology are. And we're willing to accept a policy with tremendous costs and
*  table these benefits, even also like a licensing regime where you have to get permission from the
*  government before doing a training run, or even things also where it's like, is it an agency that
*  actually is issuing binding rules that all of these policies have pretty big costs? I think the costs
*  of like companies having to be more transparent and a government starting to think about this and
*  issue guidelines and whistleblower protections, it seems to me, and I think this has been true
*  a decent number of folks who talk about that, like those policies being good seems robust to quite a
*  lot of different possibilities about exactly how big a deal this technology ends up being and how
*  much is different. And if it's the case that test these models and these like really severe risks
*  do not manifest and the advantage of liabilities, then like they're not liable. And so I think that
*  is an advantage of I think, liability is an approach relative to something like a licensing
*  regime where it is more flexible that you are kind of, and I think you all are also recognizing,
*  like I agree 100% that these companies have a lot more expertise about this stuff than
*  folks in the government operations agency will. And I think that's to a large extent why the
*  bill is taking the approach of not having like government testers come in and test the models
*  and having that it is saying like companies, you're the ones who know how to do testing,
*  you can decide how you want to do these, you can decide how to do this, but we're saying that you
*  have to take it seriously and it can't just be voluntary. I think one thing where I do think
*  there is like some genuine disagreement that I do think is worth talking about is to what extent
*  any regulation at the model or development level is appropriate in this context. And I think A16Z
*  has been very, very direct and I think more direct than feels more strongly about this than Dean does
*  that there should be, I think in one of their blog posts, zero liability at the model level.
*  And they submitted a letter to the Senate or another folks in the legislature saying that like
*  this bill is unnecessary because there are already laws against cyber attacks on critical
*  infrastructure and laws against terrorism of like anything. And so basically saying that all of that
*  should be the bad person using the thing, not the person in any way developing the thing that
*  facilitates that. That is an area where again, I think that's a view that is, you know, there are
*  people with different views that I'm quite sympathetic to in the context of like social
*  media platforms and email and things like that. But I just think fundamentally that like there is
*  at least a very real chance that really advanced AI models are not a technology for which that scheme
*  of having it entirely just be on the people who are using the technology where that makes sense.
*  So anyway, realize I talked about a few different things there, but just wanted to kind of at a high
*  level talk about what the case is for the bill and respond to some of those points.
*  I think I would say, first of all, I agree with you on the discourse. I've had a lot of really
*  positive experiences, just like conversations, friends made, things like that. Good faith critics,
*  I think as far as these things go, it's been pretty good. There have definitely been inaccuracies and
*  stuff on both sides, right? Of course, it's like, it's an online debate in the modern era,
*  right? There's going to be polarization. But I think at the end of the day, also a lot of
*  people on both sides are making very good faith arguments. And I think it's just cool. I think
*  it's cool how this process went down on the whole, that like, a bunch of researchers and scientists
*  on Twitter, I know, like, as you said, red teamed the bill and had a real influence. And it was like,
*  Twitter and substack and places like that. Very cool. I like that. I haven't quite seen anything
*  like it. And someone should write a story about it. Anyway, to go more substantively to the points,
*  I think you kind of made my point actually, at the very end there, where you said, like,
*  I think AI is different from all these other things like email and the internet and all that stuff. And
*  I'm just not 100% convinced of that. Like, if we're actually not heading in the direction of
*  AGI, and we're kind of just like fizzling out asymptotically scaling, we can't really figure out
*  a way to bang these systems into... I mean, we're talking about solving the nature of intelligence
*  here. We're talking about building the everything machine. It's like, fair to say that there are
*  just significant unanswered questions about like, whether or not that is possible, right? In principle,
*  it's not... There's no law of physics that says we can't do it. But we don't know whether or not
*  it's possible. We don't know how close we are to doing it. And I think we'll have a better sense
*  as things develop. But to me, I just have quite a bit of uncertainty on that. And I think AI is
*  actually maybe not so different of a... I mean, very powerful technology I'm very excited for,
*  but maybe not so different, if the fizzling out thesis is correct. And in that case, liability
*  does concern me quite a bit. And I think one of the things to think about is just a little bit
*  practically, like, what happens if a cyber attack is perpetrated with the help of an AI model? How
*  often when a cyber attack without... That didn't involve AI. How often do we know the exact tech
*  stack of the cyber attacker? How often do we know what the analog of like, their chat transcripts
*  with a language model, let's just say like their prompts and stuff. How often do we know that? How
*  will we know that? What concerns me very much is that we might know a little bit. We might know like,
*  oh, GBT-4 was used, right? But we might not know the specifics. And there's going to be an aggressive
*  prosecutor in California, right? Proto Kamala Harris, who wants to make their big splash on
*  the national scene with a big AI bill, will come after someone with a novel case. We will not have
*  all the facts. It will be complicated. It will be a, you know, it'll be a great deal of uncertainty
*  about that. And I think like, in that world, it's up to a judge. One judge writes the standard for,
*  like, how do we decide whether this model materially enabled this harm or not? What counts
*  as evidence for that? What is good enough evidence for that? And like, the unpredictability of that,
*  like, that's just like a bomb. It's just sitting there. And you are leaving yourself liable to
*  a really stupid opinion that could be written. And then you're setting the national standard that way.
*  And I know that like, you have worked very hard and diligently to make that materially enabled
*  language like really specific and precise. And still, I think that it's just like because of
*  the nature of adversarial attacks that happen, I think it's just going to be very hard. And also,
*  just one other thing about like timing and stuff of legislation. I like don't really buy at a
*  fundamental level, the idea that we could be seeing AI models do terrifying things for three years,
*  and Congress just wouldn't pass a bill because they'd be like, we want to protect American
*  innovation. I just don't think that's gonna happen. Right? Like, I think that if GPT-5 comes out and
*  OpenAI shows it doing something that like makes people scared, like, that's gonna change.
*  Facts will change this conversation. We have already seen that happen. Right? I think that
*  one way to think of the narrative of this like last two years of AI policy is like, the safety
*  community really dominated at first because they had a lot of organizations, they were like first
*  on the scene, they've been thinking about this for a long time. They really dominated the conversation
*  and made policies written like, like an executive order. They were deeply influenced by them, the AI
*  Act, and a lot of things proposed and all this kind of thing. And it turned out though, when those
*  ideas were exposed to the light of day, and people had, we had to get down to brass tacks of
*  implementation, and it wasn't just vague talk about guardrails, but we actually had to talk about it,
*  it turned out that the safety community didn't have a good story about the implications of some
*  of their policy ideas. And so a lot of those policy ideas didn't succeed. And then like the sort of
*  whatever you want to say, like EAC, community effective acceleration, this, whoever, like the,
*  I don't want to say anti-safety, but like, the kind of like AI acceleration aside, had been really
*  big on open source AI. And all of a sudden, as kind of people started to realize that you saw
*  conversation, you know, policymaker buy in on open source AI increase fairly rapidly. And that's kind
*  of what we're living in right now. But the thing is that the acceleration is people don't have very
*  good answers. This is a concern I have, because I mean, like I am an accelerationist, right? So I am
*  part of this community in some sense, I wouldn't call myself EAC, but like, I love technology,
*  and I think it's good. We should have more of it. So like that community does not have good answers
*  on what the hell you do. If AGI is like coming soon, like we're going to open source it and
*  they're going to fight each other. That's the plan. Like we're going to be getting vaccines every day.
*  That's the plan. That can't possibly be the plan, right? That's not going to work. And if we're
*  lucky, the best outcome from that world is one in which is tyranny, right? One in which a strong
*  man comes in and says, you know, in an effort to create order imposes tyranny on us, right? That is
*  how that will happen. Or strong AI for that, right? So there are not good answers to this. That's sort
*  of like I would call myself a classical liberal. There is not a good classical liberal story on AGI
*  governance. And so I think that we're right now in the aftermath of policymakers deciding that the
*  safety community was a little bit of an unreliable narrator on some things.
*  But policymakers might decide the same thing about accelerationists. That could super likely happen.
*  And accelerationists could be looking real dumb in six months or not. Maybe they'll look really
*  smart and wise. They usually have throughout human history. I'll say that. They usually have,
*  but they could be wrong. And so let's let that play out a little bit.
*  Yeah, I guess one thing that I do want to say that I do just strongly agree with you on,
*  and I think is one of the reasons why I think proposals like this are good, is that I agree
*  that I think the default thing that I somewhat expect to happen, both in absence of 1047 and
*  even to a larger extent with 1047, is that there will, in the event that there are like really
*  powerful general capabilities that either become available to the public or that some people within
*  government see, that we will have effectively antibody response from parts of government.
*  And you will see things that are like the equivalent of the Patriot Act or of kind of
*  things that happened in World War II. And you will, instead of having this where we're having this
*  like kind of nuanced conversation with a lot of discussion of the costs and benefits and where
*  like random good faith people on Twitter can have like influence into the process of the bill over
*  a year long transparent process, you will instead just have a very small number of people kind of
*  dominated within the national security community just like make these decisions. And I do think
*  that this is really a thing. And I think there are some who like, I think folks like Jeremy
*  Howard, like I think Jeremy Howard has taken like a serious view in terms of saying, look,
*  it's not that I never think that AI risk could be real. It's just like even in worlds where I
*  think it's real, I think open source is the best way to fight it or something. And again, I think
*  that when you really drill down into some of the details of that, of like, I don't know, how does
*  offense defaults balance work again, like, is the idea that like, oh, they're open source, crazy,
*  terrifying bio weapons, but somehow we also have somehow that cancels out in a way that is good.
*  But yeah, I think the thing that is very important is that for people who do really strongly believe
*  in the virtues of like, open innovation and open technological progress, and like I do, you know,
*  this might be surprising, but like, I definitely count myself among those people. And I like am
*  very excited about it. Like, policymakers and the general public are freaked out. And look, like I
*  think that and again, I think the extent to which like, I think the general public right now is like
*  worried, but it's like not an incredibly salient issue. And I know there have been like debates
*  and back and forth about some of the specifics of different polling that's been done about and I
*  don't want to say specifically about 1047. But like, when you just look at polling, the public is
*  not super excited about this whole AI thing. I think also this is very true of conversation
*  with a lot of legislators as well. And I think for people who do want to like get all the benefits
*  of that technology, like I do think that you need to propose people alternatives, or else the
*  alternative might be like national security state nationalization, shut everything down. I just do
*  think there is that I feel like there's I'm reminded, this is like a weird analogy, but I'm
*  reading this book right now about US Iran relations. And like there was a period where,
*  you know, like the US was supporting the Shah's this dictator, and there was like lots of discontent
*  among the Iranian people. And it's like, let's not listen to that. Let's just like kind of keep going
*  with this. And eventually that exploded. And you get the Iranian revolution. And not really anyone
*  is very happy with this. And I do worry that like, there is this kind of like, you know,
*  Mark Andreessen and some folks have some views about this. And again, I think they're wrong.
*  But even in the world where you think they're right, those views are not necessarily the views
*  of the general public and politicians to just really embrace really chaotic change. And I do
*  worry that if you see such a strong reaction to I think even fairly modest things, you might
*  defer this and then later on, you're going to get something that is going to be a far more opaque
*  process that is far less attuned to the potential trade offs here. And so I just do think that's
*  something who people who are will celebrate if this bill dies that I think that they should
*  grapple with really seriously. I agree with you that that's a major risk of sort of like my
*  proposed approach here. It is the trade off. It's the major trade off of my proposed approach,
*  which is why I'm saying all the stuff I'm saying right now. And it's why I was like a little bit
*  more critical than I otherwise might be of like what my general view of the accelerationist
*  vision for the future is, at least with respect to AGI. I mean, a lot of them just kind of don't
*  believe AGI is like going to be a thing. But the ones that do are like, well, they're going to
*  fight. And I think that is potentially kind of true in some ways, right? Some like in a certain
*  sense, like we have like people have conflicts. How are we going to have all these different
*  people on earth? They're going to fight each other all the time. It's like, yeah, that's basically
*  what happens. That's what's happening. Like, you know, we are having a conflict right now,
*  intellectual conflict over legislation over economic institution design. So maybe that is
*  like it's reasonable and fair to think that in some ways, but I don't think that is the story
*  that you sell to policymakers. And I don't think it's the full story at all. I think there's like
*  all kinds of mechanisms that are going to be needed. But like nothing I've seen satisfies me,
*  right? Like nothing I've seen really works. 1047 is actually like, it's pushing in the direction.
*  I think it's like reasonably close at the federal level, a simplified version of it,
*  I think could basically get the job done for like the next few years of buying a security for the
*  next few years. But it's like, if AGI is coming in a few years, 1047 is just profoundly not
*  the long-term governance strategy. And I think you would agree with that.
*  But no, I agree. It's a trade-off, which is why I'm saying the stuff I'm saying, being a little bit
*  provocative about this, because I do think that that community needs more people thinking about
*  like really long-term, what do we do? And I also think that like, it's a matter of just like,
*  people like you and me who, you know, have disagreements about many things on the policy
*  side right now. But we do have a fundamental intuition and thought very bit carefully about
*  AGI, right? Like, this is the kind of thing like we should be collaborating on, right? I think it's
*  like a meeting of the minds a little bit. So yeah, anyway, I think both sides need a better
*  story on policy. I think the policy is just an underdeveloped field. I mean, I totally agree
*  with that. And I think very constructive. I think one analogy that I was just thinking about is like,
*  I feel like we are at a point where it's equivalent of like, we find some new virus
*  that's in some part of the world, and we think maybe it'll be a pandemic. We're not sure. Maybe
*  it's going to fizzle out. Maybe it really is going to climb a bunch up the exponential.
*  And I would argue in that situation, like, I think shutting down all of society would be an
*  incredibly costly thing, where I think the costs of that would be likely to exceed the benefits.
*  But I think like starting to work on a vaccine for that virus, in the event that it really does
*  exponentially take off seems pretty good. And I think you can disagree about to what extent,
*  like, you know, something like 1047 is, you know, the equivalent of working on a vaccine. But I
*  think like doing things that are robust across multiple worlds and taking like seriously that
*  there is like a real chance that it is this exponential thing. And that if you try to wait
*  until the moment where it is incredibly in your face, that you'll be far too late, because you
*  will have climbed all the way up that exponential. I just think I think people need to take that. And
*  again, I think you can like debate about whether 1047 is that thing. But I think trying to identify
*  policy that we can do that recognizes the fact that there is a ton of uncertainty that we don't
*  know whether, you know, this is going to asymptote or keep going up. And that in the worlds where it
*  does keep going up that we want to retain flexibility and retain benefits here. Like, I
*  think that should be the common mission between quite a lot of people and very happy to, you know,
*  talk about more things that hit that bill. And I think there is good stuff. Like, it makes me happy
*  when I saw some of like the people talking about being a fan of meter and AISIs like open source
*  as safety valuation. That made me happy. I think that was good. I think that's the type of thing
*  that is good along both of these worlds and is helpful. Similarly, I think I've even seen like
*  Mark Martin, because I don't spite him and I really not agreeing on very much at all. I do think I have
*  heard him say that he thinks that the virus is serious and that not he very strongly disagrees
*  that model level regulation is appropriate. But, you know, trying to prepare society for a world
*  in which just setting aside AI, like, and again, I don't want to put words in Martin's mouth, but I
*  do think it's a thing that like Dean and I talked about as well. Synthetic biology is going to bring
*  a bunch of benefits, also is going to have these risks of worse pandemics. And we should be preparing
*  for that in a way that, you know, is helpful. And so I think that like this, I mean, I do think
*  this is kind of like the thesis of like the defensive accelerationist stuff that like Vitalik
*  talks about. And again, you can disagree with how to apply this model to different situations. But
*  I really do think it's like a type of thinking that I think is quite good. And I think that
*  is something that I would like for folks who have very different views about this to be
*  collaborating more and engaging on. And so I'm glad that that's something that we do agree on.
*  Steve, I don't know if you have any burning questions. I was going to go more toward a few
*  possible scenarios or try to because I liked Dean's one, not that I like the scenario,
*  necessarily, but the concreteness of the idea that some prosecutor would be able to use this
*  as a mechanism to make their name in a world where maybe AGI is turning out not to arrive anyway.
*  And then that's just kind of is a bummer. I had a couple others to throw out there to maybe
*  spark some analysis or you could riff on them. But anything you want to throw in first, Steve?
*  Yeah, I had something to throw in, but it really kind of take us away from SB 1047 a little bit.
*  So maybe we don't want to go there. I think like the prosecutor thing under the theme of SB 1047
*  seems like a good thing to explore. But I'll just briefly share earlier. I think Dean, you commented
*  that if we get to the point where it's clear that the AGI tsunami is worrying in, then there would
*  be action. Congress would take action or whatever. And of course, we've seen many examples of this
*  over history as we touched on. I have less faith in that than I used to. And what really shook my
*  faith was watching that after the initial reaction to the coronavirus pandemic, all the follow-up
*  work that we haven't done around really prioritizing nasal vaccines and better monitoring to detect the
*  next pandemic. All this stuff that's been clearly called out would cost some money, but infinitely
*  less money than what responding to the pandemic, coping with the pandemic cost. And we're not
*  doing it because there's like COVID policy fatigue. And so I worry that we could get into a world where
*  maybe we passed SB 1047, maybe something happened at the federal level. There's been some action.
*  Maybe there's been some moderate good and bad things coming up of AI development. We're not
*  really at AGI yet. There's some controversy. Some policies passed. And then the really big thing is
*  happening, but we're at policy fatigue. And we take too long to act. Or we're on some path-dependent
*  direction where it's clearly the policy direction is this. And what it now needs to be is that,
*  but it's too late. We're locked into this. So I worry about relying too hard on the assumption that
*  if push really comes to shove, we step up and step up constructively. My only thought for what to do
*  about that is try to think, and I can't take this all the way to a specific policy proposal, but
*  to think strategically about how do we put ourselves on an incremental path toward the
*  policies we want down the road. And that might mean things like policies that bring more information
*  into the public domain. So we have a little bit less uncertainty about what's going on. But yeah,
*  I don't have a lot of specifics, but I just feel that it's important that we sort of study for the
*  test of eventually, if and when AGI gets really real, that we have put ourselves in a position to
*  face the policy challenge. I agree. Those are all super legitimate concerns. I guess the only thing,
*  very quickly, what I would say is, before we get into the scenarios is COVID, it's actually,
*  we took very different things from COVID, because in my mind, we did radical stuff,
*  absolutely wild. I remember sitting there, I was like, oh my God, we're nationalizing the whole
*  economy. There's planes flying in the air between cities that make no sense because the government
*  told them to, and that wasn't true a week ago, and it's true today. What? That's crazy. That happened.
*  So much happened. Obviously, we spent a lot of money, but quite radical. And that just happened
*  in a heartbeat. So I actually think America's ability to turn on a dime and be super schizophrenic is
*  underrated, both as a good thing and a bad thing. Our country is legitimately crazy.
*  And we are the craziest country in the world. That is why we're the only people in the entire
*  world who think they would even entertain the idea of open source AGI, which might be an amazing idea,
*  but it's crazy, right? It's objectively crazy. That's what America is. We're the only country
*  with the institutional chutzpah to do that kind of thing. Even AGI itself, I think, is a uniquely
*  American invention. I don't know that the CCP is technically, they're capable of developing,
*  but are they institutionally, do they really have the chutzpah to put AGI into the world,
*  to accept that level of a transformation? I don't know. I don't know about that. So I guess,
*  I do think that radical change is possible in both good and bad ways.
*  In the face of decisive strategic domination, I think they might be more willing to roll the dice,
*  which is part of why I'm always like, let's not frame it in those terms.
*  Right. Yeah, no, for sure. I mean, like they absolutely may be. It's hard to say. Anyway,
*  that's not the point of this. Yeah, it is also an interesting,
*  just one quick thing. And I can also talk about the prosecutor specific example. I know we're
*  jumping back and forth a little bit, but I do think it is wild that I saw Robert F. Kennedy Jr.
*  endorsed Trump today and his vice president, Nicole Shanahan said that one condition for that
*  endorsement is Trump publicly apologizing and stepping back from Operation Warp Speed and saying
*  that was a mistake, which is just really wild to me. And so I think there are just interesting
*  lessons from the, I think COVID pandemic response where on the one hand, I think it demonstrates that
*  government, when really stuff does hit the fan, that you can go from Congress doing nothing for
*  years to passing trillions of dollars of stuff in weeks. And even also to see really also smart and
*  complex stuff like Operation Warp Speed. But I also think I would not underestimate the degree
*  to which you can be confident that yet government, when stuff gets real, will do quite a lot of
*  things, but the extent to which they will do smart and measure things and things that are
*  trying to really get at things that are anything other than like directly immediately in their
*  face rather than something for even like a year or two from now is yeah, I think it's much more
*  unclear. Yeah. Anyway, would it also be helpful for me to just like turn and just like kind of
*  try to directly address like the concern about like you have a kind of ambitious prosecutor who
*  wants to like go after marginal cases? Let me throw out a couple scenarios and then you can
*  address whichever ones are most intriguing. I think the prosecutor one is really interesting.
*  Three other ones where I've been just kind of thinking, is there a real fork in the road here
*  or not? And how would we know? Because we're going to play out one version of history or another and
*  then we'll still have the potential to disagree. I'm like, well, if SB 1047 would have passed,
*  wouldn't have been vetoed, then we'd build a better world. Or if only it hadn't, then this
*  wouldn't have happened. And I'm really trying to think like, what really fits that bill where you
*  could actually say, you know, things would have materially been different. So a couple things
*  that have come to mind, meta in general, right? If I was meta, I don't think we've seen a meta
*  letter yet. But if I was going to write the letter on behalf of meta, and guess what they would say,
*  it would be, I'd love to see that 10 million threshold on fine tuning be lowered so that
*  we could put our open source stuff out according to our strategy. And other people would have to
*  take responsibility sooner than getting to the 10 million. Because that's a lot. Most fine tuning
*  bills are very small by comparison to $10 million. Like I go on OpenAI and fine tune something,
*  $5, $100. Like it's not, you know, we're not entering even thousands, let alone millions.
*  So that keeps a lot of stuff on meta. And then, you know, might they feel like they can't be as
*  free with their open sourcing in the future? That's one possible crux. Another would be,
*  does XAI or Grok refuse to serve California? Does Elon actually say, you know, as he has done with
*  other businesses to a certain degree, like, F you, I'm out. I have a hard time seeing that.
*  It seems like these burdens are low enough that they'll just bite the bullet and do it and continue
*  to be in California. But I'd be interested if anybody has a different opinion. And then third,
*  I do think like maybe things like meter sort of become like more prominent, more almost like
*  institutionalized normal. And maybe things also like fine tuning resistance techniques
*  become more developed and more normal. I've been really interested in this recently,
*  totally independently of, but there was one that came out of China. And then Dan Hendricks,
*  who we all know and love as being central to this debate has had a paper recently on,
*  they call it tamper resistant model training. But the idea is to essentially not just to have like
*  guardrails or sort of detection mechanisms, but literally to train into the core model weights,
*  not only fusel to do certain things, but to go so far as to make it hard to recover those abilities
*  or to retrain them in. I hope to do a full technical deep dive on that with Dan at some point. But
*  those are three things that I could imagine we might say, geez, the world is materially different.
*  Stand off on any of those or, you know, propose others.
*  Dan Hendricks I'm just going to jump in with one thought,
*  which is I have no idea whether the tamper resistant line of research is, you know, where
*  that will go and how successful that will be. But if that were to really be, you know, if work
*  were to continue to go into that and it really bore fruit, that in my mind would be the poster
*  child for the best thing that we could hope for from SB 1047. I'm not saying it will happen. I have
*  no idea. But that I think if you were going to paint the really positive scenario for SB 1047,
*  that would be the kind of thing that would be in it.
*  Dan Hendricks Yeah. So, okay, I'll go in order of the
*  scenarios. I'll make it really quick. The fine tuning thing, meta fine tuning, will they like,
*  yeah, I mean, meta is going to be responsible for under SB 1047, the vast majority, the vast majority
*  of fine tunes of llama that take place, llama four, not llama three, the llama four, that take place
*  will be meta's legal responsibility. Anything those models can do. Anytime they're deployed into an
*  app, you know, in some specific context, anything that they do, right? So there's a combinatoric
*  possibilities and misuse there are immense. And I have no insight as to like how meta would react
*  to that. But my guess is that they would probably try to find some way of geo fencing the open
*  sourceness of llama four. They're obviously already planning to do this, because they've said
*  that they're not releasing llama four in the European Union. But they also clearly intend
*  to open source it. Therefore, that makes me think that they have some sort of mechanism worked out.
*  It might just be a contractual mechanism, right? Like, this is not for people in the European
*  Union. There might be something that in llama four license, it says this is not for people in
*  California. So super possible, I think I don't know the legal details. But I'm sure there are people
*  inside of meta who are thinking about things like that. Second issue, which one was that? Can you
*  just give me a keyword to remind me? Grok leaves Texas or Grok leaves California. Oh, no, I don't
*  think so. In fact, I think Elon Musk wants this bill passed. That's speculation on my part. I
*  don't know anything. But I think so. He has said nothing about this bill, despite being extremely
*  online and despite being very interested in AI. And despite this being like a policy conversation
*  that took place on his platform, as far as I know, Elon said nothing. And Dan Hinberg, obviously,
*  is a safety advisor to XAI. And Elon has expressed lots of concern about AI existential and
*  catastrophic risk. So I think if anything, Elon Musk wants this bill to pass. And I think he would
*  be delighted to not have to open source Grok. I think he actually, I don't know, since he's not
*  super thrilled about having to do that, about feeling obligated to do this, I could be wrong.
*  And then finally, the question of, man, I keep forgetting them. I'm so sorry.
*  Institutionalization of standards and perhaps new techniques.
*  I love that kind of stuff. What concerns me about it is the tamper proof paper, it did seem to make
*  the models a little bit dumber, a little bit, not like hugely, but a little bit dumber. And I would
*  worry about like what the implications of that would be. Obviously, benchmarkers go hard anyway.
*  So I don't know enough about like qualitatively how that affects the performance of models.
*  And I would want to know much more about that. But is a general rule, things that push in this
*  direction could be like something very close to a silver bullet, right? And like, how great would it
*  be if we solve this, their technological ingenuity. So I love that Dan is doing this kind of research.
*  And I think it's great. And this is the kind of thing that like, you can pull it off, and we could
*  change the whole dynamic really quickly. Would it be helpful for me to go through and respond
*  to some of those scenarios? Yeah. So first on the point about meta, so I think there are a few
*  interesting things that I think would be helpful to add here to just do the sale of about in what
*  circumstances open weight models could be affected by the bill. So specifically, it's like,
*  you're training over $100 million model or then if $100 million model is trained, you're, you know,
*  modifying in excess of 10 million through fine tuning. And then it is that it is not that meta
*  has to guarantee or be strictly liable for things that have done with that, but they have
*  responsibility in some sense around like arguing whether they took reasonable care in light of what
*  it in a reasonable person would think about those risks. And I think exactly the balance of it,
*  this actually goes back to one other thing where I do think that Dean previously saying of like,
*  it's wild that we can live in a world where you can have a really big single case that decides law
*  for ages like that is just common law torts. And it is crazy. It's reasonable care, a judge interpreted
*  and will have very large things. And I think one of the things of this bill that I hope, and I think
*  I should have had some indication that it is actually moved some people within companies is
*  just like recognition of the extent to which like AI companies have an obligation to take reasonable
*  care. And there are ways where if a catastrophe does happen, where the extent to which they were,
*  you know, undertaking safety and other measures does exist, I think is a thing. Anyway, it seems
*  like Dean wants response. I'll let him respond to that as well. But just to quickly go through the
*  other parts of it, I do think that the situation in the European Union is a little bit different
*  with Subrector Meta. I think one interesting thing is that this bill applies to companies that are
*  either do business in California in that relevant respect, or are headquartered in California.
*  And the EU, Meta does business in the EU, but it's not headquartered in the EU. And so it would
*  require them to not only, you know, not release their model for commercial profit in California,
*  but also to relocate entirely out of Menlo Park to a new headquarters, which I think is a pretty
*  big ask. And I would be pretty surprised if that happened. And I think similarly on Grok, I have a
*  similar reaction of just saying that, look, if you look at what these compliance burdens actually
*  are, and what at least I think Elon's attitude towards wanting to take these types of risks
*  seriously, I think that would be quite surprising to me. And then on the third point, I do just very
*  strongly agree that I think one of the really big benefits of this bill, in my view, is trying to
*  accelerate the development and incentivize the development of some of these safeguards and having
*  companies effectively have like a race to the top to develop effective safeguards and to
*  invest in these things. And I think that this bill creating additional incentive for more research
*  in that area, I think is really good. And I think would be quite positive. And it's good that
*  Dean agrees that kind of, regardless of this bill incentivizing that, that he thinks, because I agree
*  that I feel like right now there's this really hard trade off that exists between transparency and
*  access and safety in certain circumstances. And I think making that less of a false
*  binary, I think would be really huge. I think we're still, you know, can talk with other folks who
*  have more of a deep technical understanding of it, including Dan Hendricks. I think there still is
*  ways to go on some of that, but I agree it's very promising. Anyway, so those are just some of my
*  thoughts on those things. No, and like it would be so great if something like that were true. Also,
*  that final, like the tamper proof example, because then it really reasonable care would make so much
*  sense in a world where that was true. Cause it's like, yeah, do this and like, yeah, okay. It's an
*  open source model. And someone could in theory spend like a ton of money to find, cause at the
*  end of the day they have access to the weights, right? They can change the weights. They can
*  change the weights. They can change the model. They change every single number. And like, you
*  know, you'd have to have access to an enormous amount. So it might not be literally tamper proof,
*  but you could make it so much so that like, okay, well you have to augment it and therefore you
*  fine-tuner are responsible for this. And that would make the reasonable care standards so clear.
*  Unfortunately, I'm just not confident that's what we look, but it might be the other thing though.
*  I just want to briefly mention the tort liability thing, because this is like an area of ambiguity
*  that I think that 1047 supporters have been misrepresented reality a little bit on. And
*  Scott Wiener in particular has done this, which is Scott Wiener goes and says AI developers
*  currently have enormous amounts. You know, he has described SB 1047 as having profoundly narrower
*  liability than existing law, right? It was his words, profoundly narrower, or maybe he said
*  profoundly broader existing laws, but anyway, profoundly was the adjective or the adverb. So
*  that is, we don't know that, right? Like software is actually like there's liability waivers in many
*  software licenses. The way that it's been interpreted in the common law is in such a way,
*  for the most part, that it's pretty darn difficult to bring these kinds of reasonable care,
*  you know, negligence cases to hold software developers liable for that. So I don't think we
*  know that is how that is going to play out. And it could very well be that AI gets interpreted more
*  like software in the absence of 1047. 1047 makes it a certainty. So I think it's like,
*  it's a little bit more complicated how that would actually play out. And I just think it's important
*  for anyone trying to be informed about this to like understand that is an uncertainty. Also,
*  by the way, great point about meta in the headquarters thing. You're right. I was just
*  transparently wrong about that. I was offering a first glance thought and I didn't think about the
*  fact that it would obviously apply to them because they're headquartered there. So my bad.
*  It's a lot of people to move. Yeah, they're not going to move headquarters because of SB 1047.
*  All of this uncertainty reminds me of the great Nancy Pelosi quote that we have to pass the bill
*  to find out what's in it. And as she stocks up on Nvidia and comes out opposed to it, I have to say
*  don't take her position too seriously on this particular matter. But it will be interesting
*  to see what happens. I don't know that there's a conclusion. Maybe one way to conclude would be to
*  offer any final thoughts that you have and maybe also handicap whether you think this thing passes
*  and whether it gets signed. Sounds good. Just to very briefly respond to just like the tort law
*  point super quickly. And I realize this is like a very weedsy weedsy issue and could talk about it
*  for quite a while. I think what I will just say briefly there is I agree that there is ambiguity
*  under current law that for a variety of reasons, there have not been very many successful
*  negligence theories of lawsuits against software developers. I do think that this is like for
*  different reasons than some of the non lawyers in those communities think. Like I think one thing
*  is they think that like, wow, these liability waivers are bulletproof. And that is not true to
*  the extent. One very important way is that like, that is at a minimum, even if you assume that
*  contract was completely bulletproof, that would be a contract between the developer and the user
*  of the model. It is not a contract between third parties who could be harmed. Like the bank who
*  gets hacked by it never signed that contract. Not about third party externalities.
*  Yeah. Yeah. And so anyway, this is also just like some people who I think should know better making
*  this argument. Like A16Z's chief legal officer submitted a 16 page thing that included like,
*  there is not liability because of these. I think that is a little bit sloppy. But I think there
*  are just different challenges in terms of like, what is reasonable, what is foreseeable, proving
*  causality, kind of all of these things that are very tricky. I do think that when you have
*  situations where like, really is a catastrophe, I think you could fairly look at something like,
*  you know, the lawsuits against Purdue Pharma over the opioid crisis. And prior to those lawsuits,
*  you might look like, oh, bringing those types of lawsuits is pretty hard. That would, you know,
*  bringing kind of that type of massive liability against drug manufacturers for misuse of their
*  products. That's like a pretty novel thing. But when a really bad thing happens, I do think that
*  there is like very much a thing among courts for them to say that when a bunch of people are harmed
*  to a very large extent, that there's a very strong thing to find someone responsible for that. And
*  that includes under just existing common law theories. Yeah. And I think that-
*  Oh, just real quick, I'll just say that like, the basic point here to like simplify this for me is
*  like, cyber attacks are a negative externality of the existence of software. And yet the people who
*  make software, they've caused enormous amounts, billions and billions of dollars of damage to the
*  world every year. That's an externality that like software as a general matter, software developers
*  do not like, they don't pay the price of that negative externality. We don't do that through
*  the liability system. And I think that there's a relationship between that and software, right?
*  Like why is software so successful? There's a relationship between those two things. And
*  there's a lot of academics, and some of them I know, who like think that this is like an interesting
*  legal problem and they'd like to do it for various reasons, because like maybe they don't like software
*  for some reason, or like maybe they just think it's an interesting intellectual problem. But like,
*  there are people that have been working on this for many, many years, who think that we need
*  liability because of cybersecurity risk for software. And I think those people have absolutely
*  disastrous ideas for how they- like, I think that's one of the worst ideas I've ever heard in my entire
*  life. And so in a broad sense, like I do recognize that AI could very well be different, but there's
*  a reason. There's a reason that those lawsuits don't exist. And that was like, that's what I mean
*  by existing law, being fairly protective. For sure. I agree. It's an interesting thing,
*  and I'd be excited to do some more back and forth on that at some point. So what were the other
*  things just in terms of, I guess like some of just like kind of concluding thoughts, and then we can
*  also do some of the odds, which I may have to exempt myself from, but I will let you all and
*  can maybe give some high level thoughts. Yeah, I do just want to, I think, really emphasize
*  some of the points that I brought up earlier, that there are a lot of things about this process
*  that I think have been frustrating or challenging, or have not necessarily brought out the best in
*  people. But I think there are other parts of it that I think really have. And I think there have
*  been parts of this discourse that have been like really good and led to a bill that meaningfully
*  improved over the process. And I think kind of even for folks who are opponents, I think are like
*  less realize that there have been real and significant changes that were made. And I do
*  also think that like this bill is quite important and will have real impacts. But I do think that
*  this is not going to be the thing that either saves us from rogue AGI or causes a, I think
*  what the thing that I think these high level questions of before, these ideas of like, to
*  what extent is model level development appropriate? To what extent do states have
*  a role to play? To what extent should we be thinking about AI as kind of just consistent
*  with the lineage of policy and software versus distinct that I view this as kind of like taking
*  a step on each of those things. And I think that initial step is real, but, and I think they are
*  good and important steps. And I think Dean disagrees, but I do think that kind of those
*  questions, regardless of 1047, are like very much not going away. And I think that one of the things
*  that I just like very strongly encourage folks who to, I think, grapple with the fact that like
*  the software industry and VCs are not going to exist in a bubble from the rest of government
*  regulation and the general public. And I really encourage folks to like, try to come up with more
*  concrete proposals that are grappling with these problems, because I think they're not going away.
*  And I'm happy that I think some of that grappling happened in a transparent and good fashion over
*  1047. And I really hope that that continues in subsequent debates, even as the, at least in,
*  if you believe some of the folks, even as the stakes get considerably higher.
*  So I've been in like a lot of policy fights in my life, right? I've done state and local policy
*  my whole career. And when I wrote my first, I was the first critic, public critic of SB 1047.
*  The day after the bill text dropped, I wrote my article about it. And when I wrote that article,
*  I was gearing up for a policy fight that was familiar to me. That was like, yeah, like I've
*  been in these kinds of fights before and I've been on the side, like I don't lobby for things, right?
*  But I've been in a part of intellectual bad, not as a writer, usually my previous career.
*  I thought it was going to be like that. And it turns out that it really wasn't at all.
*  It was much better, actually, in most ways. A lot of people disagree with me on that,
*  but I think it was much healthier in many ways. And also different in the sense that,
*  I mean, I really do feel like this is the first conversation, what will be like a generational
*  intellectual project that is, you know, if AGI is real, that project will be akin to the writing of
*  the Constitution. I believe that in my bones, that it is that complicated of a thing that has to be
*  done and that, you know, that's serious of a task. And I feel like a lot of things are changing
*  quite radically. And I just, I thought it was mostly pretty cool and pretty good. And it was
*  like, it was a real pleasure to be a part of it, you know, come what may with the bill.
*  The other thing I would say, though, just on the substance, you know, I would just like the arguments
*  I made at the beginning are pretty much like, I think still the core ones for me. But like,
*  you could also make a vibes-based argument, right? It's really weird. The world, one of the things
*  that's happening is time does feel like it's moving faster. Event history is proceeding faster,
*  it feels right now. And that has made things actually like legitimately, maybe a little bit
*  more vibes-based than they used to be. Right? Like, it's kind of weird that that's true. But
*  like both political parties are now like fully vibes-based. And I think that is like an
*  evolutionary adaptation, just as much as it's a cynical one. It's a socio-technical reality.
*  There's a lot of reasons I think that this is true. And in a certain sense, SB 1047 is bad vibes.
*  The AI industry doesn't like it. There's not buy-in, like from a lot of people. The researcher
*  community, like for the most part, at least the ones I see seem to be like mixed on it and not
*  wild about it. And I think there's a world in which like, it passes and like the whole
*  vibes of American technology shift for a little while and we start feeling bad for ourselves.
*  That's not a substantive argument, but it's like at this point, kind of like true,
*  that that kind of thing matters. And but on a more substantive level though, I think we're
*  opening ourselves up with SB 1047 to quite a bit of uncertainty. And I think it might be necessary
*  to like open ourselves up to that first prosecutor in the first case, the uncertainty inherent in
*  all of that. It might be necessary for us to do that and to pay that price and to pay the various
*  other prices that I think we will pay in the long term if SB 1047 becomes law. But I just don't think
*  we have evidence that the benefit is worth the cost yet. That could change. And in terms of my
*  prediction, I believe the legislature will pass this bill. I believe the governor will veto it.
*  Steve, you want to bring us home? I don't have much to add after a great conversation,
*  those great summaries. I'll just, my one closing thought I'll throw in is something
*  I've really grown to appreciate watching the SB 1047 conversation unfold is this stuff is hard.
*  AI policy is hard and there are no good answers. There are degrees of bad answers.
*  And the fact that it's hard is not an excuse to say, let's just pass whatever. But it's also not
*  an excuse to just say, let's do nothing because nothing is one of the bad policies, I think. But
*  this is really hard. There's so much uncertainty about the technology, about what prosecutors,
*  just uncertainty at every level and conflicting goals and desires and technical limitations we're
*  wrestling with. And so that brings me back to, you know, that it was really great to see
*  that some of the conversation around the bill, not all of it, not everything people have been
*  saying on Twitter and whatever, but some of it was constructive and not just saying, I hate this bill,
*  but saying, here's how it could be better. Or, you know, I don't think it could be better. I think
*  we should do this other thing instead, but at least a constructive proposal. And so I just feel
*  like that's really important. Like this is so difficult that the only way we're going to both
*  get anywhere to any kind of good policy and the only way that we're going to have at least
*  a hope of collectively feeling good about the policy we passed is through those constructive
*  conversations. And so it was great to be part of this pair of podcasts. And it's been gratifying
*  to see this going on in the public sphere. Long may it continue. Nathan Calvin, Dean Valt,
*  Steve Newman, thank you all for being part of the cognitive revolution. It is both energizing and
*  enlightening to hear why people listen and learn what they value about the show. So please don't
*  hesitate to reach out via email at tcr at turpentine.co or you can DM me on the social media platform of your choice.
