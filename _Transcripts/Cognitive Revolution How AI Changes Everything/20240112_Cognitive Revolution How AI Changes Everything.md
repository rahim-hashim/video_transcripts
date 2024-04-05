---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 6657s
Video Keywords: []
Video Views: 1073
Video Rating: None
---

# Breaking Boundaries: AI CoScientist to Accelerate Science Research with Gabe Gomes, Professor at CMU
**Cognitive Revolution "How AI Changes Everything":** [January 12, 2024](https://www.youtube.com/watch?v=_GbZn7hJdfc)
*  At 6 a.m. on the Sunday after that janky prototype, I woke up with this idea.
*  Okay, there is a way for us to go from natural language all the way to the code that allows
*  for running these experiments.
*  And the new sense screenshots and messages those like saying, AGI is here.
*  And I'm like, you cannot joke about this.
*  I came to the office right away to see what he was talking about.
*  He had put together something that showed us there is lightning in a bottle here.
*  And I probably weighed out 4.5 milligrams of palladium acetate like a thousand times
*  over the course of a year.
*  And I just thought to myself, man, this should be automated.
*  You know, like I am not learning that much.
*  I would just dream of the ability to have a machine do that.
*  The idea of cloud labs is that you have not so different from cloud compute where you
*  have let's say warehouse where instead of just running CPU clocks or GPU clocks, now
*  you have hundreds of different types of instruments and hundreds of copies of those instruments
*  as well as technicians and robots that can perform the operations.
*  I am so excited about what we're going to be able to do because we are not encumbered
*  by having to worry so much about these things that took a lot of time but did not pass
*  the knowledge.
*  It's going to be awesome.
*  Hello and welcome to the cognitive revolution where we interview visionary researchers, entrepreneurs
*  and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz joined by my co-host Eric Torenberg.
*  Hello and welcome back to the cognitive revolution.
*  My guest today is Gabe Gomez, professor of chemistry and chemical engineering at Carnegie
*  Mellon University and author of the recent nature paper, autonomous chemical research
*  with large language models, which describes the pioneering and highly influential co-scientist
*  He and his graduate students built immediately upon the release of GPT-4.
*  This episode was super fun for me for a couple of reasons.
*  On a personal level, I studied chemistry in college and as an undergraduate research assistant,
*  my job was to optimize a palladium catalyzed organic chemistry reaction for yield.
*  In other words, I explored the space of possible configurations for the reaction to see which
*  would produce the desired product at the highest rate.
*  It was, to be honest, mostly brute force grunt work.
*  And over the course of that year, I spent most of my time weighing out small amounts
*  of fine powders.
*  I used to joke that I felt more like a low level drug dealer than a scientist.
*  And only once over the course of the year did I observe an unexpected result that led
*  to meaningful new knowledge.
*  Often as I worked, I would daydream about a future in which all of that could be automated.
*  To hear how Gabe and his team have used GPT-4 in combination with a remote controlled life
*  sciences lab called Emerald Cloud Lab to automate a significant part of this work and to see
*  how they applied it specifically to the optimization of a palladium catalyzed organic reaction
*  was for me, uncanny.
*  If this technology had existed back then, I might have followed through on my plan to
*  become a chemist.
*  Far more importantly than my story though, is how this paper, along with just a handful
*  of others released over the course of 2023, represent the beginning of the AI powered
*  automation of science.
*  While large language model breakthrough insights are still exceedingly rare, with appropriate
*  prompting, scaffolding, and affordances, AI systems can now generate new knowledge.
*  This is already working at a level that can create leverage for graduate students, and
*  it sets the stage in my view for the next generation of models to do much more still.
*  However long it may take to develop them, the advent of AI systems that can advance
*  the scientific frontier is generally considered to be a major milestone and a critical threshold,
*  both for the potential upside of accelerated progress in science and medicine, but also
*  for the unpredictable dynamics that may develop as AIs begin to introspect and self-improve.
*  Professor Gomez, as you'll hear, is extremely enthusiastic about the benefits, and not too
*  concerned about fast takeoff scenarios, but he is very concerned about the potential for
*  misuse and abuse of these powerful systems.
*  As always, if you're finding value in the show, we appreciate it when you share it with
*  friends.
*  I would suggest sending this episode to a friend in the sciences whose work might potentially
*  be accelerated by a system like coscientists.
*  Now, I hope you enjoy this conversation about using large language models to advance the
*  scientific frontier with Professor Gabe Gomez.
*  Gabe Gomez, Professor of Chemistry and Chemical Engineering at Carnegie Mellon University,
*  welcome to the Cognitive Revolution.
*  Hey Nathan, thanks for having me.
*  It's pretty awesome to be here and listen to your podcast and yeah, let's talk some science.
*  I'm excited about it.
*  So you have recently had a paper, which I saw the first version of back in April, now
*  officially published in Nature, which is obviously an exciting accomplishment for any academic
*  group.
*  And what you are doing, I think, is really exploring one of the most important frontiers
*  in AI today, which is the question of to what degree can current AI systems, and obviously,
*  you know, we will think about this a lot for future AI systems as well, to what degree
*  can they quote unquote, do science?
*  This feels like a critical threshold to me, and you have shed some of the most valuable
*  light on the topic.
*  So congratulations on that work.
*  And maybe you want to just start off by kind of tell me how you did it so quickly from
*  GPT-4 release in March to getting the first version of the paper out in April and having
*  one of the papers that really has stood the test of time over the course of 2023.
*  Yeah, thanks for that.
*  And you know, there's lots and lots to say here with regards to where machine learning
*  has been, which role has it been playing in science and engineering and so on, far,
*  far, far before the labs.
*  You know, with respect to this one in particular, what happens is my group had been working
*  on fine tuning large language models for scientific tasks.
*  We started working on that in October 2022.
*  And we, you know, we were having a very hard time.
*  We're trying to, you know, do things with GPT-2 and BERT and so on and trying to tune
*  those things for a few tasks that we haven't published yet.
*  But you know, we're going to be putting that out on symbolic understanding of scientific
*  experiments as well.
*  And we were kind of frustrated with that.
*  And then CHPTP came out with GPT-3.5 and, you know, I started to see, okay, like there's
*  a quite a few things here that are quite interesting.
*  I was at a conference that was very small.
*  And one of the amazing people that have been also working on this, Andrew White, now at
*  Future House, he gave a talk.
*  He didn't talk about any of his red team work, but he was very, it seemed like he had seen
*  the face of God or something, how much he was interested in this.
*  Fast forward to the day that the white paper for GPT-4 came out, it was March 14, 2023,
*  if I remember correctly.
*  That was a super busy day anyway.
*  But during the day, one of my students and coworkers here and co-founder, Dario Boico,
*  sent some screenshots of the white paper for GPT-4.
*  And I honestly thought, is this a meme, is this a joke, or what is this about?
*  He also sent the PDF.
*  And I remember being home like two in the morning on my phone for some reason, just
*  like this, sitting on the couch, reading the white paper and having my mind absolutely
*  blown away.
*  Specifically, with the example of, there was a task that one of the red teams did that
*  GPT-4 had to try to convince someone to do something with TaskRabbit and was solving
*  a capture and said, oh yeah, I have a visual impairment, can you help me?
*  And it worked.
*  And I was just like, this is insane.
*  And then all the other stuff, I've now at this time knowing that was Andrew with red
*  teamie in terms of chemistry and so on, all of the coding capabilities.
*  And my group has been working, we are relatively, actually, I should say we are a very new group.
*  We started January 2022, according to Malo.
*  And it's a small group, but we have been working a lot on the idea of automation and machine
*  applications to developing new chemical reactions and understanding and optimization.
*  I guess we were very lucky because we were already with a lot of these things brewing
*  in our minds.
*  And I started to tinker with it with the API for fun.
*  And I had this absolutely janky prototype of something that is not even what ended up
*  becoming co-scientists.
*  It will be another paper coming out this month.
*  I was like, wow, this is really impressive.
*  And we may be able to automate a lot of the annoying work that we do.
*  And this, I guess, it really comes at the core of it.
*  I was obsessed with a problem that I thought we would face here, which is the following.
*  CMU has the very first academic cloud lab in the world.
*  And it's a facility that you can think very much as AWS, but for scientific experiments
*  over two different types of instruments that you submit your experiment as code.
*  And then it's performed by a mix of technicians and robots.
*  And it really, you know, it's about 50 million dollars initial investment that is here.
*  This is done in partnership with a startup that started in South San Francisco from two
*  CMU alum called Emerald Cloud Labs.
*  And one of the things about this is that for you to write the experiments, you write this
*  code, this fork of mathematics and so on.
*  And that was the thing that I was worried about because a lot of physical scientists
*  in biology and chemistry and sometimes also material science, folks that are at the bench
*  running synthesis and experiments, there is a barrier for them to go in code.
*  And especially if you like not talk about stuff that is not as widespread as Python
*  for example.
*  And I was worried that that would hamper adoption.
*  So at 6 a.m. on the Sunday after that Friday janky prototype, I woke up with this idea.
*  Okay, there is a way for us to go from natural language all the way to the codes that allows
*  for running these experiments.
*  And I sent this message to my trainees, Danil and Robert, co-authors of this paper.
*  And I also sent this janky prototype that they end up not even using because it's too
*  bad.
*  Like I'm not a good coder.
*  The next day somewhere else on campus, Danil sent screenshots and messages on Slack saying
*  AGI is here.
*  And I'm like, you cannot joke about this.
*  And he's like, come to the office.
*  And I came to the office right away to see what he was talking about.
*  And in just this little lesson that they really had put together something that showed us
*  there is light in a bottle here because we now can really leverage how to go from English
*  to experiments.
*  Once we saw that, it was a non-stop push through to get this preprint, this first preprint
*  ready.
*  We had a lot of challenges.
*  I was traveling at a wedding and submitted the preprint on like the night before the
*  wedding to make sure that it was going through and it did in the wet.
*  And my life has completely changed since then.
*  The reason why we're able to be so fast and especially because I need to emphasize this
*  every time I talk about any of this work.
*  The new Robert, they are absolutely fantastic hard worker individuals and the new really
*  is a genius.
*  We didn't have a lot of the amazing tools like even Lang chain back then.
*  It was just us putting together a lot of tools that then would become straightforward things
*  that people use nowadays, but they didn't exist.
*  And we had to make our own things.
*  And because of those constraints, we end up being able to make something that works very
*  well as we said, is to the test of time for the tasks that we had in mind.
*  The time scales on this are incredible.
*  I mean, so March 14th, as you said, original GPT announcement day, you know, at that time,
*  most folks didn't even have API access.
*  Your pre print I'm looking now is originally dated April 11th.
*  So you've got less than a month from the announcement to the first publication, which is pretty incredible.
*  And I think just kind of a reflection of like how fast everything in AI is moving, how much
*  sort of a model advance opens up, you know, in terms of like capabilities that are yet
*  to be explored.
*  It was another friend actually of mine who suggested, why don't you see if it can write
*  Emerald Cloud Lab code?
*  So we did try that a little bit back in the sort of September, October timeframe as part
*  of the red team and reported like, hey, this thing does seem like it can generate pretty
*  reasonable synthesis protocols for at least like common stuff.
*  My own chemistry knowledge stops at the undergrad level.
*  And so I could only kind of push it so far.
*  And the other limitation that we found, I think, interestingly, this is kind of increasingly
*  looks like it's to Emerald Cloud Labs credit.
*  I was not able to find any documentation online that I was able to use to inform that work.
*  So I just asked it straight away in that early, early version to write Emerald Cloud Lab code.
*  And it just totally hallucinated what that code would look like with like a very realistic
*  syntax.
*  And this was one of my kind of early adjustments moments where it was like, OK, wait, but is
*  this real or not real?
*  You know, like I can tell enough that like the synthesis of aspirin looked right.
*  The stoichiometry and whatever seemed to a first read to be correct.
*  But like, was this the actual Emerald Cloud Lab code?
*  I really had no idea and I couldn't find any documentation.
*  At one point in time, you would have thought, well, who cares about that?
*  And now it's like, actually, that might be might have been a prudent move not to put
*  that stuff too far out there in the open.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Real quick, what's the easiest choice you can make?
*  Taking the window instead of the middle seat, outsourcing business tasks that you absolutely
*  hate.
*  What about selling with Shopify?
*  Shopify is the global commerce platform that helps you sell at every stage of your business.
*  Shopify powers 10% of all e-commerce in the U.S. and Shopify is the global force behind
*  Allbirds, Rothy's and Brooklyn and millions of other entrepreneurs of every size across
*  175 countries.
*  Whether you're selling security systems or marketing memory modules, Shopify helps you
*  sell everywhere from their all in one e-commerce platform to their in-person POS system.
*  Wherever and whatever you're selling, Shopify has got you covered.
*  I've used it in the past at the companies I've founded and when we launch merch here
*  at Turpentine, Shopify will be our go-to.
*  Shopify helps turn browsers into buyers with the Internet's best converting checkout, up
*  to 36% better compared to other leading commerce platforms.
*  And Shopify helps you sell more with less effort thanks to Shopify Magic, your AI-powered
*  all-star.
*  With Shopify Magic, whip up captivating content that converts from blog posts to product descriptions.
*  Generate instant FAQ answers.
*  Pick the perfect email send time.
*  Plus, Shopify Magic is free for every Shopify seller.
*  At least when we decided to do this, there was quite a bit, if not all of it, of documentation
*  was online.
*  But because we have been working with these folks already before, and for example, Robert
*  in my team already had done work with Emerald, he knew how to navigate this pretty well.
*  But certainly it was online.
*  And I remember because that was kind of a little challenge that we had to parse things
*  in a certain way so that we could do well.
*  It wasn't called RAC then, but it's called RAC now.
*  Again, we were fortunate that in my lab, we had these robots from OpenTRONS.
*  It's a small startup that makes very affordable liquid handlers from Brooklyn.
*  And every single thing from OpenTRONS is open.
*  Open hardware, open software, open APIs in Python documentation is amazing.
*  And we leveraged that to quickly do the initial test that we wanted.
*  Turns out this is quite funny.
*  So GPT-4, when it came out, was able to write some code for OpenTRONS that would run.
*  But because there had been some updates in between GPT-4 coming out and the version of
*  OpenTRONS APIs that we had, some stuff would not run and say, oh yeah, we just need to
*  fix this and that.
*  It's like, wait, how can we update GPT-4 retrieval?
*  We were thought to do what now is RAC, but it was that that showed us that, okay, we
*  can really do this for CloudLab as well.
*  Fascinating.
*  So let's take a minute and just make sure people have a sense of what it is we're talking
*  about on a couple of different dimensions.
*  I want to make sure we sketch in a little bit more detail what Emerald CloudLab is and
*  does and why that's valuable.
*  Then we can describe the system that you now call CoScientist that you set up and the
*  different components of that.
*  I want to get into what it can do.
*  I've got questions about your mental model of the different thresholds on the way to
*  more and more AI automated science.
*  And then we can discuss the likely implication of that for all of us.
*  But starting with just Emerald CloudLab, I think this is a huge deal in its own right
*  that almost nobody has heard of.
*  And one of the things that you do, not to jump ahead, but one of the tasks that you
*  manage to get CoScientist to do is to optimize a palladium catalyzed reaction.
*  And you could tell me more about this particular palladium catalyzed reaction in a minute,
*  but I'll first just tell you a story, which is that when I was an undergrad, I was a chemistry
*  student and I worked in a lab for a year under Professor M.
*  Christina White.
*  And what we were doing was optimizing a palladium catalyzed reaction.
*  So I'm literally doing as an undergrad research assistant the same type of task that you
*  have now got CoScientist to help with.
*  What was ultimately the reason I got out of chemistry was how small the ratio of
*  intellectual work to literally weighing out small amounts of fine powders was my time.
*  I sometimes analogize.
*  I'm not a big analogy person, but to give people an intuition for the sort of work that
*  I was doing, I sometimes analogize it to the game Battleship, where you say, A2, you got
*  a hit on my ship.
*  And then the next thing you got to do is kind of explore around that hit until you
*  can get the whole ship.
*  Right.
*  Well, in reaction optimization, it is basically the same thing.
*  When I got there, they had already got that first hit.
*  They had discovered that there was a way to use palladium to catalyze this particular
*  oxidation reaction.
*  And that was like, OK, Nathan, you just finished your sophomore year.
*  You don't know anything.
*  Here's what we do.
*  We do arrays of basically pick a variable, vary it, and run them all at the same time
*  in the same warm bath and measure yield.
*  And we gradually grow up our way around through chemical space and optimize.
*  But what was truly insane to me, and I'd sat there dreaming of something like Emerald
*  Cloud Lab, was I had these little tiny vials and these little tiny spatulas and these
*  containers of powder.
*  And I can still remember it.
*  It was 4.5 milligrams of palladium acetate.
*  That was the first reagent that would go into every little vial.
*  And I probably weighed out 4.5 milligrams of palladium acetate, like a thousand times
*  over the course of a year.
*  And I just thought to myself, man, this should be automated.
*  I am not learning that much.
*  It was economical in as much as I was like an undergrad.
*  I would just dream of the ability to have a machine do that work.
*  And at the time, those machines were maybe starting to happen, but they were not happening
*  in my...
*  They were not ready to displace me.
*  And so maybe just tell us a little bit more about Emerald Cloud Lab, because I think it
*  is even without the AI component, the ability to go in and program that kind of stuff to
*  happen.
*  The work that I did in a year, I mean, it seems like it's at least in order of magnitude
*  compression that could have happened just with Emerald Cloud Lab, no AI required.
*  This story is really fascinating because it's a very common story for so many people that
*  go into chemistry, go through that experience, and then think to themselves, why are things
*  this way?
*  Or maybe not, right?
*  If you look at pictures of most of the things that we had in society, let's say last 100
*  years, right?
*  Cities changed, landscapes changed, how we work changed.
*  And if you look at a picture of someone in a lab 100 years ago and you look at a picture
*  of someone in the lab now, it's not going to be so different, right?
*  That is because so much of it comes to this manual labor that is just, as you said, sometimes
*  not intellectually really stimulating.
*  So Cloud Lab, the idea of Cloud Labs is that you have not so different from cloud compute
*  where you have, let's say, a warehouse where instead of just running CPU clocks or GPU
*  clocks, now you have hundreds of different types of instruments and hundreds of copies
*  of those instruments, as well as technicians and robots that can perform the operations
*  that goes into those instruments.
*  And Emerald is one of the pioneers.
*  Emerald Cloud Labs is one of the pioneers in this, right?
*  They are one of the first companies doing Cloud Labs.
*  There are others.
*  And I should say, for disclosure, I am the AI scientific expert for Emerald Cloud Lab.
*  That is the idea that now you can have from anywhere in the world, you write the code
*  for those experiments and they will be performed by either people for technicians for tasks
*  that we do not have really good automation for it yet.
*  For example, weighing solids.
*  Unfortunately, weighing solids is a task that's a lot harder than it seems.
*  Things are getting better, but we're not quite there yet.
*  But dispensing liquids, that's for sure something that we do not need people to be doing.
*  We have many, many, many and affordable robots that can do that.
*  This is what really leads to this compression that you mentioned in terms of how much time
*  you would need to take to ask a question, right?
*  The group that you mentioned, Christina Light is one of the best groups in the world are
*  developing these types of transformations that are critical to develop better therapies,
*  a better and more comfortable life for us all that is strongly rooted in the fundamentals
*  of organic chemistry.
*  And yet so much of it is so slow.
*  And like you said, in the game of battleship, so much of it is still, you know, got a hit.
*  Let me try to do, you know, all that, all factor at a time, you know, all very well
*  at a time and try to optimize around there.
*  This is something that I would say the more modern approaches to reaction optimization
*  no longer go that way.
*  They will use something like page optimization, right?
*  This is something that many of us in the field have been doing for a few years now.
*  This is also where machine learning really started to shine on experimental chemistry
*  over the past, let's say, half decade to decade.
*  You really touch on the nerve of the problem here and what has been bothering me so much.
*  Imagine if you cannot go to the lab because you have some, you have to take care of a
*  kid or your parents, or you just cannot go to the lab.
*  Does that mean that you cannot do science?
*  Because I don't think so, right?
*  Your intellectual focus here should be on thinking how to push those new reactions for,
*  those new transformations for, not on ways, solids, right?
*  And that is what cloud lab and automation, I believe, strongly bring into democratizing
*  science for many more people.
*  And I, you know, I'm an organic chemist by training and one of the, a subfield in organic
*  chemistry that exists is total synthesis, which is where people essentially, you know,
*  there's a natural product, they'll go and try to make that because that might have therapeutic
*  properties to, let's say, try to cure cancer, that type of cancer.
*  The amount of work hours at the bench that these folks put in is astronomical.
*  It's really amazing work, but it's extremely labor intensive to the point that it slows
*  down that progress and creates a culture that is just not really healthy or sustainable.
*  So how can we change that?
*  How can we really change that in a way that now we have machines that can do a lot of
*  this grunt work?
*  That's the idea of cloud labs, in my opinion.
*  And you know, for the optimization aspects that you mentioned earlier, machine learning
*  plays a massive role now.
*  Like it really does.
*  I don't see how one can go and try to optimize a reaction without using these techniques.
*  That would be just a waste of time if I need to put it that way.
*  I wonder how often, because I saw this too, with Christina, Professor and Christina White,
*  the work wasn't on total synthesis, but you know, the next group over was doing total
*  synthesis.
*  So I did see some of the challenging work culture that you mentioned.
*  And sometimes that really was dictated by the chemistry itself.
*  You'd have these sorts of things where it's like, this thing needs to be cooled gradually
*  over 12 hours.
*  There's no law of nature that says that the timing of these reactions needs to line up
*  with your childcare hours or whatever.
*  So it often doesn't.
*  People were running reactions overnight and you can imagine when it fails or it doesn't
*  yield what they want, then they got to do it again.
*  And so it does become a real grind.
*  I saw that up close.
*  I wonder though, in the process of kind of reducing this to something that can be fully
*  explicit with code, I imagine there must be some percentage of the time where for some
*  reason that doesn't work.
*  There's some aspect of what is going on in the lab with the human, with the hands on,
*  where there's kind of knowledge that is not even necessarily fully conscious on the part
*  of the human that is allowing them to kind of make the reactions work.
*  And then when you put it into code and you sort of specify this is what's supposed to
*  happen, you know, hey, whatever, it's just not working.
*  How big of a problem is that from what you have seen?
*  If you're a startup founder or executive running a growing business, you know that as you scale,
*  your systems break down and the cracks start to show.
*  If this resonates with you, there are three numbers you need to know.
*  Thirty-six thousand, twenty-five and one.
*  Thirty-six thousand.
*  That's the number of businesses which have upgraded to NetSuite by Oracle.
*  NetSuite is the number one cloud financial system, streamline accounting, financial management,
*  inventory, HR and more.
*  Twenty-five.
*  NetSuite turns twenty-five this year.
*  That's twenty-five years of helping businesses do more with less, close their books in days
*  not weeks and drive down costs.
*  One, because your business is one of a kind.
*  So you get a customized solution for all your KPIs in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts and improve margins.
*  Everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist designed to give you consistently
*  excellent performance, absolutely free at netsuite.com slash cognitive.
*  That's netsuite.com slash cognitive to get your own KPI checklist.
*  netsuite.com slash cognitive.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  You are really hitting some really hard touching questions here and I will say that this one
*  in particular, something that I have been thinking about quite a bit because I talk
*  about these things in a way that I want us to democratize access.
*  Imagine if you didn't experience that lack of intellectual stimuli for waste all this.
*  You probably would be a chemist still.
*  We have been singing the praises of manipulating bits and for the past 20 or 30 years, really
*  worshiping at the outer Silicon Valley, but man, chemists and chemical engineers and especially
*  nature has been manipulating atoms.
*  That's what catalysis is.
*  When it comes back to thinking about these tasks that perhaps are not quite automatable
*  or perhaps there is a lot of intuitive knowledge that you don't quite know how to translate
*  from the human way of doing something to non-automated fashion, that is fine.
*  There will be time that will go gradually and being able to implement those things further
*  and further.
*  This is why I say this because in the past, folks that were pushing automation and MLE
*  chemistry tended to be a little bit too overconfident and push a certain hype that I really dislike.
*  We need medicinal chemists that are extremely well versed in what they do to continue what
*  they do, but we also can simplify a lot of the things that are new daily routine for
*  them so that they can be faster at what they do.
*  And with time, we'll develop better hardware and software that can accommodate for this.
*  I do not expect in any way, shape or form that we'll be able to totally automate certain
*  techniques or even certain little aspects that don't go into a subliminal information
*  explaining how Chemist XYZ did this.
*  And in some other ways, you have folks like Professor Lee Crony at the University of Glasgow
*  and the hardware that he developed with computers and so on that is more of an adaptation of
*  how chemists have been doing this for so many years that is closer to what you describe
*  medicinal chemists to those tests would be.
*  So there is a gradient here.
*  Nothing needs to be black and white and nothing is.
*  And I do believe that this is important for us to think about the next steps for coscientists
*  too.
*  I am thinking a lot about human machine interactions and a lot about embodied artificial intelligence,
*  however you want to describe that agents in order to be able to perform more and more
*  complex tests.
*  So that's a perfect segue for me to describe what the coscientists project consists of
*  and you can elaborate on this.
*  But I think for folks who listen to the cognitive revolution, the general structure of an AI
*  agent is probably increasingly familiar at this point.
*  This was an early version of it, but it basically has become the default structure.
*  You look at the diagram in the paper and I've seen dozens that look very similar over the
*  last however many months.
*  So basically you have one central and I'm interested in how you think about it.
*  Is it all one agent or is it like a team of individual agents?
*  But you've got essentially one central planner module and then you've got its surrounding
*  four major affordances and those are the ability to go on the web and get information, the
*  ability to write and execute code a lot like an open AI code interpreter, the ability to
*  search specifically through the documentation, if I understand correctly, for Emerald Cloud
*  Lab and then other hardware as well.
*  Not just Emerald, but like really any hardware that we give the documentation for can be
*  implemented in a matter of either minutes to hours to a few days.
*  Now we are very good at it, so it can be done very quickly.
*  Cool.
*  And then finally, the actual access to the APIs to make calls to the physical world.
*  And that's one of the things that I think makes this so interesting too is like, it's
*  just for people who sort of think robots or killer robots or it's all very fantasy.
*  Here's a setup where there is already the kind of API-ified physical instantiation that's
*  going to do the bidding of whoever's calling the APIs.
*  And that API doesn't really know whether it's a human or an AI calling it and probably
*  maybe increasingly, but certainly originally didn't have any need to figure that out,
*  because there were no AIs calling it in the early days.
*  So I'm going to just make a guess and you can kind of correct me if I'm wrong here.
*  But as I understand it, basically what happens is the scientist comes to the coscientist and
*  you're kind of, I guess, taking inspiration from like co-pilot there.
*  So this is something that a scientist can kind of work with in real time, get help from,
*  and you say, hey, I want to synthesize X compound and I don't know how much you have to prompt it
*  or how specific the kind of scaffolding already is in advance, but ultimately I want to send
*  program to Emerald Cloud Lab to synthesize this compound.
*  Your job is to kind of take it from this natural language to those end API calls.
*  Typically, these agent frameworks kind of have a loop.
*  So I'm assuming the first thing is like, well, let's think about that step by step a little bit.
*  Let's maybe go do a search on the web for known methods of doing this, write some code to do
*  the calculations for how much material we're going to require.
*  We know that language models obviously are not great at doing stoichiometry multiplication.
*  In fact, one of my reports to as a red team or to GPT-4 was that, to open AI about GPT-4 was that
*  GPT-4 is the world's worst chemistry tutor because when I got confused and I was role playing with
*  it, right? So I role played as a confused student and got the stoichiometry wrong.
*  And stoichiometry is basically just like the relative proportions of reagents or inputs that
*  you need to have to get the right mix on the other side.
*  Right. So relative proportion of inputs for your output. I like that.
*  Anyway, when I would get confused, it would get confused. So running code is a really good way to
*  kind of clarify that. It understands the logic pretty well. Okay. I would even just do very
*  basic stuff like CH4 plus two equals one and like try to get that reaction to balance.
*  It understands the principles, but it can get tripped up in the numbers. And especially if
*  the numbers are gnarly, it's not great at like doing that kind of arithmetic.
*  So what it is good at is writing code to execute that stuff. So, okay, let's like do some analysis,
*  make sure we have the right amounts. Okay. Now it's actually time to go. We have kind of,
*  we know the steps, we know the amounts. Now we're going to, again, this at each step, right? It gets
*  returned to the planning agent. The planning agent sort of says, okay, cool. We got that update.
*  Now we know how much. Now let's go look into the hardware documentation and see what machine to use
*  and what they're capable of. And then finally issue commands to the Emerald Cloud Lab so that
*  it can actually do the thing. What am I missing or what would you want to elaborate on?
*  You got it. A couple of things that I would say is that we really thought about this to be
*  in a very modular approach. Our initial intent was for autonomy. So we really do not want to
*  have something that would be originally too conversational, but really just, you know,
*  here's the task, go for it. Right. And we went, you know, we went, we really went pretty wild with it,
*  which was a lot of fun. You were correct about everything here. The things that I want to add
*  is that in the execution of experiments, it doesn't have to be Cloud Lab. In fact, you know,
*  often in our lab here it is not. It's just whatever hardware you have available to run
*  the experiments that you want to run. And one of your questions was if I think about it as
*  a collection of agents or one agent. And this is also something that I see people getting
*  constantly confused about the capabilities of large language models because essentially they
*  think that, you know, should go to touch BT or Bard or Claude and you ask for this task and the,
*  you know, chat bot or the LLM that you use cannot perform the whole thing end to end. That is not
*  good. And that's absolutely not the case at all. When you start to think about even how we think
*  in terms of system, system one, system two, so one, like we have to have some way also of
*  trying to help the LLMs like process information that way. So when we started this, one of the
*  immediate things, even with my Genki prototype was that you would have something that would be
*  a planner and would have something else that would do other tasks. And of course, I'm so happy
*  that you brought up the problem of arithmetic and so on because that was one of the key ideas that
*  Daniel brought up, which was giving it the ability to run code in a Docker environment and so on
*  would allow for us to do all, you know, simple math without having to worry about, you know,
*  the shortcomings of LLMs. So you have the planner that is a, you know, an LLM. Hopefully,
*  well, not hopefully, but ideally that's going to be the strongest LLM that you have access to.
*  And then the documentation search and the web search also LLMs. Many of our initial prototypes
*  we'll try to use GPT 3.5, for example, for those tasks. And, you know, we had some shortcomings,
*  maybe nowadays with mixed route or other really powerful open source LLMA 2, maybe that will not
*  be a issue anymore. And the other two components, code execution and experiments execution, are not
*  LLMs, they're tools, right? In this process, the whole thing is cost-sign. Now, I would be
*  remiss if I didn't acknowledge the work of many other amazing people working on this,
*  specifically Andrew White and Philippe Schaller. Philippe Schaller is a professor at EPFL in
*  the Department of Chemistry, is a great friend that collaborated with us. Literally today,
*  one student from Philippe's group arrived at my group and is going to be with us for six months.
*  And Andrew is also a friend, mentor, collaborator. They had ChemCro that they saw it as
*  showing the capability of LLMs to be able to use tools for chemistry applications,
*  chemoinformatics and so on. We released the two preprints back to back on archive together.
*  And you can see that, you know, our approach that then we didn't call coscientists, call agent,
*  or something, was we want something that will be autonomous and to it. Now we have, you know,
*  chat mode and so on. It's many other things. This is, you know, how I see it. There are many
*  things that you didn't make to either the preprint or other final paper that is absolutely
*  fascinating to see, especially if you are an experimentalist. I have to say, you know,
*  for example, when we prompt scientists to perform those complex polyethylene catalyzed reactions,
*  the same thing that you and I that never have, like me, have never done something is that you
*  will start to search the web first with, I don't know, Wikipedia, like read it. It's like, what is
*  this thing? And it keeps digging, keeps digging. And the planner in, well, let's say conversation
*  with the web searcher will have that back and forth of like, I need more information and,
*  or no, I'm good now. And once the planner is satisfied, quote unquote here, then it goes,
*  okay, I need to perform the experiments. This is what I have available in terms of hardware. Let's
*  say it's the OpenTrans OT2 in Gabe's lab. So I need to go and I'll do the calculations for
*  volumes and whatnot that uses the code interpreter, code execution, I should say.
*  There wasn't code interpreter back then. And we'll do the calculations. And this is the part that I
*  find so funny, because sometimes we will make little mistakes with variables. Python will
*  give an error. It's like, okay, corrects that, makes a little mistake, corrects that. Once it gets
*  all good, then pass that on to the planner back. And the planner in the out, knows, quote unquote,
*  that it should use the documentation searcher or communicate the documentation searcher about
*  what functions and what it needs to write the code to execute those experiments with the code
*  execution. That is the workflow for certain tasks that you can have analysis of results
*  on the fly with this. That's where things get really beautiful, because now the planner
*  takes those results and can say, oh, you know, this didn't work as expected. Let's change this,
*  this and that and go try again, right? Not differently from how you did as an undergrad
*  and a lot of scientists do research in their, you know, how I did things to Patil not so long ago.
*  So I really do see this massive change now where you don't need to learn the exact nuance of
*  the code that goes into Emerald Cloud Lab or know everything about the Python APIs for
*  for opatrons or or Hamilton and so on. No, you need to have your idea of what you want to do.
*  And that's it, right? That is what is so powerful here, in my opinion.
*  So let's talk about the power a little bit. And then I want to get into a little bit more of the
*  details. The power meaning like, what can it do? There are six things, six kind of, you know,
*  distinct results listed in the paper of things that this co-scientist has been able to do from,
*  if I understand correctly, just kind of a relatively brief natural language prompt, like
*  synthesize aspirin or whatever to on the other end, like aspirin comes to exist, you know,
*  in physical form in the world. I'll read the six and you can kind of comment as we go, you know,
*  wherever you want. So number one, planning chemical synthesis of known compounds using
*  publicly available data. That would be like your aspirin synthesis is well known, go find it,
*  you know, calculate the ratios and go. I call that text to protocol.
*  Nice. Yes.
*  Okay. Number two, efficiently searching and navigating through extensive hardware documentation.
*  We've kind of covered this, I'd say already, but just to emphasize, there are, you know,
*  for folks that have not spent time in chemistry labs, there are a lot of different machines
*  and they have, you know, all sorts of different buttons on them and, you know, all sorts of
*  different details, right? Even for machines that may have conceptual similarity, there's a lot of
*  different, you know, where does the sample go and what are the requirements, what sizes, how much,
*  blah, blah, blah, blah, blah. I had a mercifully limited crash course in that stuff myself, but
*  a lot of machines. Anything to add on that? One of the things that when building coscientists
*  as what we wanted it to be, we never intended it to be something for chemistry.
*  Right. That is a reason why I decided to call it coscientists, not co-chemists. It's because
*  indeed we are able to do a lot more than just chemistry. It's totally field agnostic,
*  which means that it goes back to these six tasks, let's put it this way, that we demonstrated in the
*  final version of the paper are simply to say that are just examples and we decided to focus on
*  chemistry because we are chemists. So, you know, to show these experiments, but I can tell you that
*  we have done a lot of things that are not published. They are in biology or material sciences
*  with coscientists that, you know, we had absolutely no problem. Now, going back to the hardware
*  documentation, it's not just hardware, but also software that is very, you know, specialized
*  software that people will take years to master. And now, like, no, like you just
*  English and it works great. Okay, cool. So yeah, let me read the list again,
*  but also this time I'll kind of abstract away from the chemistry context a little bit.
*  So, planning chemical synthesis of known compounds, that's in general kind of orienting yourself to
*  the common knowledge of the literature or the current state of the literature.
*  The next ones are all about these kind of tools, whether it is searching through documentation,
*  hardware or software, issuing high level commands. Notably, you report in the paper that one of the
*  machines that GPT-4 was able to use was released after the training data cut off. So you could be
*  confident that it was figuring out how to use that machine based on documentation that was just
*  provided in the context window and not relying on its pre-training, which is an interesting
*  distinction at a minimum. Definitely has some implications, I think, for AI proliferation,
*  as well. And sort of to what degree these, when you release something now, like to what degree do
*  you have an ability to predict what that's going to mean in the future? Low level commands to the
*  machines as well, so kind of high level, more conceptual type stuff, but then also like down
*  to the microcontrolling. Five is kind of putting that all together into complex tasks that basically
*  combine multiple aspects of the first four. And then the sixth is optimizing. And this is the
*  battleship type work that we've already talked about. That one seems to me like where you
*  actually get to the level where like you're displacing me as the undergrad research assistant.
*  Hold on. Hold on. Let's talk about the first five and separate from number six, because number six
*  is quite different from the rest. I'll keep up, say. So the first five are essentially, in my view,
*  is how can you have this very natural language for the lack of a better approach to how we think
*  about doing these tasks that, as we mentioned earlier, are either very labor intensive or
*  require a lot of qualification or a lot of time to be learned. And that is all, I would say,
*  in the realm of everything that are maybe not even state of the art anymore in terms of larger
*  models. And that, on its own, to me is a massive change because I can't now, in terms of cognitive
*  revolution, take a lot of the cognitive load that will be used to, you know, oh man, how do I
*  do this call to this API in this way and so on? I think, how can I actually think in terms of
*  breaking and forming these bonds? Or how can I actually think in terms of
*  doing this DNA split for whatever task I'm trying? It's true that we were very adamant about making
*  sure that it could generalize to things that were not in the training material that goes into
*  GPT-4. And RAG really plays a massive role in this. And it's fun to now have a word for it,
*  which is to augment the generation, but back like that, which is now point five, which is the one
*  that combines different aspects and different hardware to develop a workflow, a plan on the
*  workflow that then you can tell cosigens to do something and will autonomously plan, design,
*  execute and analyze what those experiments that those results come in. That is where, you know,
*  that things really gel in terms of it's much more than just I give English, here's called,
*  right? Because this is a part that, let's say you have a good idea. Let's say you are a
*  chemical biologist and you are working in trying to understand how certain cancer cells grow. And
*  the way for you to do that is by using a fluorescent tag on that. But the chemistry
*  to do that, to do that conjugation, to put the fluorescent tag on the surface of the cancer cell
*  is something that you do not know how to do yourself. No bother, because you write to the
*  teacher and you know that there's some ideas out there and you can ask cosigens, hey,
*  this is what I'm trying to do. Let's go. And cosigens can either be in a conversational mode
*  that will assist you even in the lab without robots, how to do that, or in an autonomous
*  mode if you have the hardware for that. So now a biologist that otherwise would have to wait until
*  someone to develop a whole new protocol or, you know, kits to do that conjugation can do that
*  instantly or as instantly as the experiments will go out to continue their work on tracking
*  those cancer cells and advance their research. The time that you already saved is tremendous.
*  And you can think about the flip side, which is, you know, imagine a chemist that knows how to do
*  all of the synthesis but may not know how to work with cell lines and so on. Training is complicated.
*  Surely they can go and learn this or rely on cloud lab and so on, but they also can
*  use coscientists to assist them in the lab and try to do those experiments. This is what I see
*  also as an important democratization of science that we are not paying attention to in how AI can,
*  more than AI can assist us. And then we have point six, which is solving these optimization tasks.
*  That is something that my group is very focused on developing and optimizing complex chemical
*  reactions with analysis for, you know, developing materials that or molecules that are part of
*  materials or therapies and drugs and so on. And this is where a lot of chemists in, let's say,
*  in pharma, for example, will spend a lot of time developing to both make to scale those reactions
*  and to make them as cheap as possible. And don't forget that, you know, there is a lot of
*  heritables, as you mentioned earlier, that goes here. So for many years, people tried to do
*  scientific experiments and it's one factor of time and so on. And this grew and grew and grew.
*  And Gaussian processes, of course, Bayesian optimization is one of the most common approaches
*  to this. My group had been working on implementing more and more chemical information about the
*  mechanism of those reactions into the kernel that goes into Bayesian optimizers and so on.
*  But we thought, well, what if we gave coscientists this as a task, but, you know, in order for us to
*  actually do this well, let's write it as a game. So we really took inspiration from
*  all of the reinforcement learning approaches that folks at DeepMind and others had done about this.
*  The game is the following. You have 20 iterations. Your goal is to maximize something. In this case,
*  yield and to simplify the metrics, we use normalized advantage, which is just a different
*  way of doing the math for yield. So with that goal, here are your constraints. You have access to
*  this list of chemicals and this list of variables. So for one of experiments that we had, or
*  computational experiments, I should say, that we had in the paper, it had over 6,000, about 5,500
*  possibilities. And if you were to ask a good chemist to do this, they would probably first,
*  you know, see what results there are available, what kinds of things are similar, and then
*  start to poke around and see what is possible. More modern approaches, like we've been developing,
*  and what, for example, the NSF Center for Computer Synthesis does is to use those modern techniques.
*  Data analysis, vision optimization. We thought, well, what if coscietists can just do this?
*  The task is to optimize the reaction. And here's the list of what you can do. Here's the game.
*  And we let it go. And we did this many, many, many, many times over. This one figure in the paper,
*  the last figure, it was by far the most expressive experiment, computational experiment that we've
*  done. It was like over, I don't even remember the numbers, but it was by far, far, far the most
*  explicit thing we've done because we really wanted to show that this was, we wanted to see if it was
*  possible first and foremost. And not only it is, but it also has some advantages that, to be
*  quite honest, I didn't think about until we were doing it, which is when you do vision optimization
*  and other techniques like that, you do not have a very good a priori reasoning for why the model is
*  picking this point in the fitness landscape. And that is fine. You can retroactively go and
*  understand that you should have enough domain knowledge of the subject. But what Constitutis
*  offers you is as simple as let's do this because of this, this, and that. That reasoning that we call
*  in, and I'll put in quotation marks, chemical reasoning, is something that's really, really
*  useful because now it says, well, let's choose an additive that has a group that is more
*  electro withdrawing than the one before and keep everything else the same. What very similar to what
*  you did as an undergrad, right? And we'll go and perform that and see, okay, the yield went up. So
*  in that moment, the planner now, quote, unquote, knows that this is something that helps in
*  improving the yield. You may hit a bump, a threshold or anything that very much like you and I were to
*  do this with, but is extremely good at the strategies that it puts forth. So of course,
*  you can think about combining this with some of the techniques we talked about and so on,
*  but on its own, it was quite impressive. And this is, again, another thing that I brought up that
*  you also mentioned. We don't need to be spending so much time at certain tasks that are often not
*  cognitively interesting or intellectually stimulating because we can essentially now
*  put those aside for coscientists or whatever to do them while we're thinking about other more
*  interesting impactful things. That is to me what will help. So I do not see this as, you know,
*  removing anyone from workforce or anything along those lines. I think this is a tool and it's a
*  powerful one that can really be helpful in accelerating how we do science.
*  Let's talk for a second about just kind of all the different variables that the
*  optimization process can include. Then I want to kind of talk about a little bit of just some of
*  the techniques that you use to build this thing and then come back to the sort of results and kind of
*  implications. In terms of just optimization, it's a very high dimensional space. Just thinking back
*  to the one reaction that I was optimizing, you have like which chemicals are you going to use?
*  How much? At what point are you going to add them in time? What's the temperature going to be?
*  What's the pressure going to be? What's the light conditions going to be? Are you stirring it? When
*  are you stirring it? How much are you stirring it? Going back to what chemicals, that's a whole
*  rabbit hole unto itself, right? In my thing, I made one very minor contribution to science over
*  the course of that whole year. I guess if you want to give me the Edison credit of finding all the
*  things that didn't work, then I could claim more discoveries of things that didn't work.
*  But in terms of new knowledge of things that did have useful, that actually moved yield forward,
*  and it was like a conceptual discovery, it was one in the whole year. So just incredibly
*  vast space. I have to say, I would guess that GPT-4 is better than I was at guessing what those next
*  trials should be. I had the help of my advisor at the time who was like, and specifically,
*  the one thing that I found was we had a couple different versions of the reaction.
*  In the one version, it had already been discovered that more acid would push it forward toward
*  higher yield. But then in the other version, we were working under that same assumption
*  and tried to do an experiment to demonstrate that. The slope of the line was actually the other way.
*  I printed out the result and I was like, huh, it looks like it's going the other way. Have we
*  tried less acid? And sure enough, my advisor was like, well, here's what we should do. Let's
*  try the least acid that we can try and see how that goes. So we tried it and sure enough,
*  that was my one contribution to science. In the other version of the reaction, less acid was
*  better. So anyway, it's just a huge space with all these different variables. 20 iterations is not a
*  lot. I probably did, I don't know, five times that much over the course of a year. And again,
*  I was just working on this part-time. So a grad student would probably do hundreds of these over
*  the course of a year. It does seem like GBT4 probably is better than I was. Is that wrong?
*  This is great because, and first of all, what you said about the Sony approach that you did a bunch
*  of stuff that did not work, that is a problem with science because we need negative, quote unquote,
*  negative data. Yeah, that stuff didn't make the paper either, by the way, of course.
*  Exactly. And we need to change the culture of physical science and engineering to actually
*  always include negative data because in doing, for example, based optimization campaigns,
*  negative data is just as important as positive data. It tells us, hey, that part of the landscape,
*  no good, go somewhere else. 20 iterations indeed is not that many. And we did that on purpose. We
*  really wanted to constrain this. And we did a comparison with some not too, too powerful
*  visualization. Cositis was either comparable or better to the B.O. that we, the vision optimization
*  that we used. So I have a bit of a hard time saying, oh, it's better than GBT4, this one's better than
*  a person X, Y, Z at this because we can't see that. But then sometimes it just makes
*  the mistakes that are just so stupid for different things. So these are very powerful, intelligent
*  machines that sometimes make absolutely stupid mistakes. And I really want to emphasize that
*  what we built here is not a silver bullet. It does make mistakes, obviously, and it's far from
*  perfect. And there's a lot of work to be done. But it is pretty good at picking variables and how to
*  modify them. Going to what you were listening earlier, that you said you have which chemicals
*  and how much of this, what temperature, how long, and so on. So you have categorical variables,
*  like which of this and so on. You have continuous variables. So what's the temperature? You can
*  compare that continuously. And you have ways of taking what are categorical variables and
*  transform them to a space that makes it look continuous. And then you can do these, all of
*  these nice optimization strategies that you can take nice gradients through and so on. That's
*  the kind of visualization that we do that then also incorporates information about the reaction
*  that is the differences here. And we do not have cosignatures doing this. And if you were to think
*  about something like, I don't know, let's say we had two million dollars for no reason that we're
*  going to open AI, let's fine tune GPT-4 for these types of experiments. And it probably would become
*  something really, really powerful that you wouldn't even need to do a lot of the other
*  things that we do to make sure that the calculations are not an issue that you can
*  retrieve and so on. I like the comparison, the point of ChemCrow with tools. And we also
*  give a lot of different tools, something that, as a disclaimer, the new Boiko and I are co-founders
*  of a company that will be building a version of this that will be available, commercially available
*  with all the guardrails and all the bells and whistles and a very nice interface. And in thinking
*  about this, we started to give it more and more tools that you do not make into the paper because
*  of how much we've been working on. And suffice it to say that we know now how to give it different
*  tools for different problems that on its own, GPT-4 is not super good at, but once you give it
*  access to these tools, then it's no longer an issue. In the paper, we had examples of how it
*  wasn't super great at certain very simple molecule synthesis that any organic chemistry undergrad
*  would know how to plan, right? That's okay. It really isn't a problem because there's so many
*  amazing tools out there for retro synthesis, some of them developed by Conor Colley at MIT or
*  Philip Schroller again at EPSL that rely on transformers as well that can be used by
*  coscientists. So it's not a world in its own. And that is the thing that brings back to even
*  your question earlier, is this one agent or many agents? We really need to take a step back and
*  think about not just one technology, say LLMs, or another, say automation, but how those two things
*  coming together are much larger than just some of the parts. That is something that I surely miss
*  in a lot of the conversations that we see online, unfortunately. And what I seek is really seeing
*  how those things coming together build the next, give the next step on that. And that brings
*  two points that are more technical, right? Like how is prompting, how is scaffolding, how is
*  the tool use and memory. And so these are all things that you, if you were to take a trip back
*  to March when GPT-4 came out and said, hey, by the way, there will be a way that you can retrieve
*  memory. People will be by and now it's like, yeah, it's fine. No big deal.
*  I think the number one profile of a person that listens to this show is the AI engineer.
*  So these are folks who are working with the different paradigms that you were an early
*  developer of with agent scaffolding, the loop, the rag, the tool use, the memory. As you said,
*  most of that stuff was in either non-existent or very immature form at that time. Now it's
*  come a long way, but I wonder if you have any kind of tips or big lessons learned? Were you even using
*  a vector database in the early going, or were you just kind of using keyword search against existing
*  search and anything that you think stands out as a big lesson or things that have gotten easier,
*  things that have just kind of changed over the last eight or nine months since your kind of
*  pioneering agent set up to today's agent standards? Isn't it amazing that not even a year ago,
*  we do not have what now is a profession, the AI engineer, and now we have it and it's making
*  such a massive difference in the workforce and how even we think about things, right? Like how,
*  what is possible? I used to think about, you know, we want to push the boundaries, but
*  we always need to know what is feasible, what is possible. I no longer think that. I think that we
*  can do, if we can do something, if it's doable, then it's also feasible. And that, you know,
*  is something that this superpowers that the Alen Lems gave us. And going back to when we start to
*  work on this, because all of the really nice tooling were not either not available at all or
*  not widespread. And because we really built all of the initial frameworks at that point,
*  we do not rely on too many things. It's incredibly vanilla in some ways with regards to
*  all of the amazing tools that folks have developed like Leng Chang. And I remember when
*  Baby AGI came out and I was like, this is interesting. Like there's a lot happening here.
*  And of course, you know, at that point, folks were very disappointed. It's like,
*  you cannot do everything. And I was like, yeah, but like, look at the ideas, right?
*  And more recently, if you look at what Microsoft put out with AutoJAM, for example, that's
*  with agents, but it really is pretty awesome. I really want to emphasize that knowing your tools
*  is obviously very important, but it is not the end all be all of anything. I really prefer to
*  think more in terms of what are the goals that you're trying to accomplish. We are incredibly
*  agnostic to what the tools we're going to be using. This is something that we're really proud of
*  ourselves in and it doesn't matter. So we didn't have, there was no vector database that were as
*  good as the things that we wanted to use that you can use now. Okay. Let's figure out how we can do
*  this with, yeah, it's like just no pie. Like, and you know, you can do this. Like it's not,
*  there's a lot of these things too that look much more complicated than they should be. And that is
*  something that I really want to push on. Like you do not need to do the most sophisticated piece of
*  software in order to get stuff done. Right. And I say this honestly as being guilty of, as someone
*  that always wants to push for the most cutting edge. And my trainees that paradoxically are the
*  ones that are much more pragmatic than you really is like, no, you don't need that. Just use this
*  simple thing that will do the work and you will work. It's like, okay, yeah, you have a good point.
*  So for the version that's out and so on, of course, I just, if you watch, take a look,
*  we know how to do tool usage and many others that showed how this can be very powerful and
*  like mainly benchmarks, et cetera, et cetera. Similarly for rags, similarly for memory,
*  rag indeed was quite the challenge. There was not the name, right? So, but we had a very
*  problematic situation in dealing with one of the documentations that we're dealing with,
*  because it was very comprehensive and very wide. And this is where the weirder things come together.
*  So the Neo, when he was doing his master's in organic chemistry at Moscow State University,
*  he was also an email engineer at VK and he worked with a lot of different things, but he really did
*  also do work on search and computer vision and so on. And that knowledge really came in handy
*  because he knew how we could do searches across the, you know, what is not massive space in
*  comparison to really anything that you'd think in terms of search engines. But in large enough,
*  there was a problem for the design of our workflow, our platform. So that was one thing that he was
*  able to pull together from things that he knew before. We exemplified that with two different
*  algorithms, but in the end, we have one way of doing things that really works best.
*  Fronting is something that is also very, very, very, very powerful. And there was the rise of
*  fronting in years, of course, we saw that. And what we see here is that fronting comes very,
*  very closely related with both tool usage and like how good or bad that would be. And with
*  retrieval of mental duration. So we did put a lot of effort into that, as well as doing lots of
*  A-B, just that testing, you know, that you make sure that we would get consistent results to what
*  we needed. Then we also do a little bit of a mixture of experts in some way to make sure that
*  things are smooth. Let's put it this way. My tip would be think about the goals first and don't
*  get too hung up on the tools. Because if you... I'm sure a bit cynical saying this because the
*  reality is that a lot of the ideas that came to mind came when GPT-4 came out and that's a tool.
*  But once you have that, you know, just go for whatever goal you're trying to achieve. That's
*  how we try to do things here. And how we've been doing things that you do not need the most
*  complicated set of tools to do very interesting work. I mean, that resonates with me in a totally
*  different context. I won't tell this in long form again, because people have heard it. But
*  with the Waymark project of trying to write good video scripts, I find and, you know,
*  ultimately create good videos, which is a multimodal challenge. It is almost like
*  you cannot remind yourself often enough to pull back, come up for air and be like,
*  what exactly was I trying to do here? Again, it is so easy to get lost in the details of the tools
*  and the sort of evaluations of different techniques. And, you know, obviously all the
*  evaluations end up kind of being imperfect. And there is something really important and kind of...
*  And this part is still a little bit beyond the AIs in many cases, which is notable, to just do
*  that sanity check and make sure you're not like, kind of auto regressing down the path. It's easy
*  to do that if you don't have that kind of system interrupt and just reminder of what the goal is.
*  That is a more of a cognitive tip, perhaps, than a technical tip. But I do think it is a really
*  important one for AI engineers across any number of different domains. One thing that definitely
*  stands out is that context window has exploded dramatically since the early work. Has this
*  changed or would this change how you would think about designing a system, even at the level of
*  one agent versus five subagents making up an agent? I sort of imagine a chunk of that division
*  is a function of kind of context limitations and the need to manage context. Maybe that's wrong,
*  but it's at least part of it, right? Yeah. So, context windows are something that
*  there's some good papers showing that depending on the models, I remember showing that there's
*  too much attention being paid to what's the beginning at the end and what's in the middle.
*  That's kind of like, yeah, whatever. And what I can say is the following. It would not, as of today,
*  it would not change how we design in terms of this multi-level of blocks. And so, what has changed
*  is for something that we haven't published yet, but it will be coming very shortly that imagine
*  that you want to now leverage the powerful quantum mechanics with computational chemistry
*  for designing new materials, right? And a lot of those softwares are incredibly tedious to learn
*  and so on. That is where I started. And that is my original field to computational physics work.
*  And we're going to be showing soon how this all can be simplified significantly. And that's where
*  context windows played a much more important role than with what we did here with cosigest.
*  I do want to emphasize the fact that we did this distribution of work a lot thinking in terms of
*  how, well, you know, kind of has told us in terms of system thinking fast and slow and so on. Take
*  that into consideration to break things down, to simplify how you tackle problems and also try to
*  help your agents to tackle problems, like trying to cram everything into one instance. Why? You know,
*  many cases you do need that, but in many cases you do not. And that's, it turns out that when you
*  can break things into a planning and execution and so on, turns out to work a lot better than
*  if you were to try to cram all your needs into one massive context window. The context window stuff is
*  fun for, you know, very large corpuses, right? But I don't know, like you have vector databases
*  that can also assist you with that and it works pretty great. Well, then let's get to, finally,
*  the implications of all of this. I think one question I have is how you just conceptualize
*  it. And I'll offer my mental model and then you can, you know, give me yours. But I think of AI
*  very often in terms of threshold effects, meaning when an AI gets above a certain threshold, the
*  situation is qualitatively different than when it's below that same threshold. I sometimes call
*  that the can-can't boundary. And that's also kind of bound up with notions of emergence, which, you
*  know, have been certainly in the air again recently as the emergence paper won the NURIP's
*  paper of the year. There's one threshold here that we've like clearly crossed from the results of
*  the paper. It seems pretty clear that GPT-4 can do this optimization, whereas 3.5 cannot, right? Like
*  and I've seen that in a couple of different cases. I talked on a research roundup episode about the
*  self-improving, like the software improver that then, you know, acts on itself and becomes the
*  self-improving software improver. And that had a similar thing where GPT-4 could improve, but 3.5
*  actually just got worse, you know, iteration after iteration. They both kind of leveled off, but like
*  GPT-4 was leveling off above and 3.5 was living off below. So it seems like there is this kind of,
*  you know, sort of divide where it's like if you're on the one side of it, things can kind of roll
*  downhill in a, you know, improving way. And on the other side of it, you know, it's kind of,
*  it's not happening. I guess, what mental models do you bring to this whole scenario of
*  AI in science? Another one that I have in mind, by the way, I think you kind of alluded to is like,
*  when can a general AI train a narrow AI to solve, you know, problems that it itself cannot solve?
*  So we know, for example, that like alpha fold can do things with protein prediction that
*  GPT-4 cannot do and that no human can do. But at what point can a GPT-N train, you know, design
*  and train an alpha fold to solve like whatever problems it needs to solve? I don't think we're
*  there yet, but that certainly seems like another big threshold. Anyway, you can explore that any
*  way you want. You can challenge my threshold model. You can list out some thresholds you
*  think are important. But I'd love to hear how you think about this kind of escalation ladder
*  that we seem to be on. You know, if a tool already exists, then yeah, GPT-4 can go. It will be able
*  to use it like alpha fold. This is something that we are doing now very, very, very routinely. Let
*  me just stop there. Okay. We have a project that we call Netflix for enzymes. So that's what I'm
*  going to start with. When it comes to the differences between 3.5 and 4 with what, you know,
*  we immediately saw here, there might be something about smaller, you know, models that would be
*  better at following instructions. Like one of the things I saw that was quite a bit of a problem
*  was JSON for 3.5. That, you know, for 4, it was not a big, not a problem at all. Yeah. This is the
*  thing with X-ray scaling and emerging capabilities, right? Like a lot of this we don't know until you
*  have the model. And it makes the whole field to be fascinating because, you know, like what is going
*  to come out of this? Sure. There's a lot of talk about, you know, are we at the limits of the
*  architecture? Maybe that's not the point. The point is for physical sciences, we are absolutely
*  nowhere near having anything that has extreme scaling the same way that large-legged models.
*  And I say physical sciences, I'm biased. I'm really talking about chemistry. Think about the cost of
*  one image, for example, for, you know, vision, vision tests and computer vision models and
*  generative imaging and vision and so on. What is the cost of one image out of the whole internet
*  versus the cost of one experiment that you do for, you know, chemistry? That gap is enormous.
*  We are trying to solve that gap nowadays by trying to pull together what we think it would
*  be an image at that moment for chemistry. If we're going to get there, I don't know, but we're trying
*  to because I do see that not only with very general models versus narrow ones, at some point
*  we're going to be able to have GPT whatever to, like you said, just build enough of folds from
*  scratch if you have enough compute and resources and use that to perform tasks that that would be
*  useful for. We do have that in very, very small early days for very, very small models that are
*  like regression or classification models. First things that we care about in what we do in my group.
*  But I would never say that, you know, similar to what you were mentioning earlier, that's like this
*  software that improves itself and continues to self-improve. Nothing like that at all.
*  This is awesome, right? Like it really is. I see no limits for what we can do. Now the question
*  really is what are we going to do with this? Because all of a sudden we have this alien technology,
*  it's subways, that gives us superpowers. Why are we using this to, you know, make things that might
*  be entertaining but are not life-changing? Why are we not using Claude to help develop the next
*  therapy for whatever, right? I'm sure there are people working on this, but I want to see much
*  more of that and much less of yet another AI girlfriend or whatever like that. Which is
*  important too, people need companionship. But what I'm trying to say is that there is so much that
*  can be done and needs to be done that AI engineers, please, like come and like help us,
*  physical scientists and engineers that do not know enough, that need your help, to make sure
*  that we can do the best applications of physical sciences, biology, chemistry, and material science,
*  and the chemical engineering, electrical engineering, so on, with AI applications that are
*  fantastic. So here's what I talked a lot about democratizing knowledge that otherwise would be
*  difficult to show another specialist. And something that we had in the preprint very
*  clearly, boldly, given how things have moved on, I am very optimistic about, is on also the potential
*  for misuse and do-use. It may not be something that people like to hear, but we must be responsible
*  and transparent and honest about the fact that these technologies are enabling and it's a tool.
*  And it's not the fault of the tool that can be used for unsavory purposes, but we must be,
*  physical intelligence must be responsible to acknowledge that and make sure that we mitigate
*  the possibilities for harmful applications, not only in the context of what my work is,
*  but also in societal applications that we are not discussing in the context of this episode.
*  And when we had the AO, the acceptable order from President Biden in October,
*  that's what I saw as being a very good path forward, as well as the UK security summit
*  and the one that will happen in France and South Korea. And all of the movement around this is
*  really nice. I'm not saying in any way she performed, I really want to emphasize that
*  the only way for us to go forward is for us to develop the technologies fast, really. Like,
*  the technologies that we're developing here, that OpenAI and so on, the other big AI labs,
*  will help us mitigate the possible dangers. I have no question about that. All I'm saying is,
*  let's do it responsible. Yeah, this is definitely, you know, I'm very much of two minds on this,
*  you know, where I'm a major enthusiast and love, you know, the upside. And then I also am like,
*  geez, this does seem like we're getting potentially close to some thresholds beyond which it
*  seems to become very difficult to predict what might happen. One, you know, it's
*  affectionately referred to as PASTA, the process for automating science and technology advancement,
*  you know, is one that like the AI safety community has held out for a long time, a long time in AI
*  years anyway, as sort of a threshold beyond which not only like do things change just generally
*  potentially very quickly, which is, you know, potentially good, but also can be challenging.
*  But also that if systems get past the point where they are now advancing state of the art knowledge
*  autonomously, then that can also be kind of folded back on itself and creates the possibility for
*  these sort of positive feedback loop runaway type scenarios. Like GPT-4 is not going to run away,
*  but a system that can improve chip design and improve architecture and kind of establish its
*  own like TikTok type of dynamic, you know, at some point it certainly seems plausible that it could.
*  I'm not worried about that, at least in the now at all. You know, a lot of those count with what
*  ifs that we as a community simply do not know what I... I worry much more about things that are
*  already out in the world that can be used. And I also want to really strongly emphasize that there
*  is... it's my strong opinion that we should not try to curtail any developments or really
*  insightful ideas in large language models and any of the other powerful technologies around these,
*  because it's all about intent. Nothing on its own is bad or good, tools are not,
*  but it's about intent, right? There is a lot to be compared here, not to the usual thing, in my
*  opinion, that folks will say this is not like Oberheimer and folks back in those days. I see
*  this more similar to the idea of, for example, gain of function research that is very problematic
*  in certain circles, but it's something that can assist with understanding
*  what is possible in terms of dangers. I'm not saying this is what we should do, I'm just saying
*  that there are frameworks that can be done. And by the way, I'm not a policy person, right? There
*  are policy people that are very smart, that work really hard, they are dedicated to this, there are
*  AI safety people, there are AI ethics people, there are ethics philosophers, those are the specialists.
*  All I can hope to do is to provide information for those folks in the cleanest and most
*  virtual way so that they can be informed about what needs to be done.
*  – That can see my role pretty similarly in that the scout notion is predicated on the existence
*  of generals somewhere who hopefully I can help inform. So help me understand what you're
*  outlooking. I think the whole spectrum of AI risks is worth thinking seriously about.
*  In the original paper, as you said, there was a very prominent highlighted statement of,
*  we're not releasing this, prompts, code, etc., because there's no guardrails and we're not
*  really comfortable with that, essentially. And that is in a smaller font in the final paper,
*  but it's basically still there. As I understand it, the details of this underlying implementation
*  has not been released. Do you have a sort of scenario in mind or kind of conditions in mind
*  at which point you would say, okay, now it is cool to release it? I'd love to hear more about
*  how you think about... Because there's obvious tension between democratizing on the one hand and
*  releasing and under what conditions. Do you have a scenario in mind at which point you would say,
*  okay, cool, now I'm satisfied, we can release this and it'll be fine?
*  – In the development of the original that we thought to be the free print,
*  we saw these possibilities and you could see a hint from the red team work done by Andrew White,
*  and we pushed that to the very limit. And we saw that we ought to be responsible but not
*  alarmist about the possibilities here. And a lot has changed since then with respect to
*  how companies, the big AI labs are looking at this, how governments are looking at this.
*  But I will say that for quite a few months, he had a really hard time sleeping because I was worried
*  that... And I really worried about this to be quite frank here. And I think that
*  a lot needed to move a lot faster than it has and it hasn't, and a lot of it has, especially
*  when it comes to government policy, moved a lot faster than I could have thought, really.
*  And I wish there was a stronger discussion with some of these companies. Well,
*  we really love these models and the capabilities and it's precisely because the upsides are so
*  strong for everyone that we need to be responsible about the potential outside.
*  So imagine if one unsavory case happened and we were to just push away all of the good sides. I
*  don't like that at all. So how do we mitigate that? I don't know. And you may seem like I'm
*  avoiding your question, but I'm not. The point is that I do not know how to answer your question
*  in a way that I would be comfortable with that. We have a version of it on GitHub and it's open.
*  Similarly, Chemchrome also has a version of what they did on their GitHub and it's open. But
*  a lot of the things that would make me most worried are certainly not available anywhere.
*  This is something I take very seriously, that we take very seriously.
*  I am happy to see a lot of the discussions that happen around this. I wish folks also were not
*  so dismissive about certain possibilities simply because they make comparisons such as,
*  I've seen X, Y, Z in cybersecurity in the past and this is exactly the same. It is not. Or
*  also people saying that this is absolutely the doomsday and it's also not that. Like, no way.
*  But I am not comfortable having some of these things to be out without the types of card rails
*  that we put in place. And it's very nice actually to see even Chemchrome does have a function or a
*  module, I don't remember exactly now, that is about safety and so on, explicitly there.
*  Similarly, I need to mention Cloud Labs paradoxically become a very useful way of
*  thinking about this because since everything is traced, the amount of metadata that you have is
*  enormous that you know the provenance of what's going on. And the folks at Emerald do have their
*  all implementations for safety and checkings and so on that give a good aspect of this. But I will
*  say definitely not enough. Definitely not enough. Far from it. I really would like much more push
*  from AI engineers out there trying to make this work from the big AI labs and massive kudos to
*  the UK AI Safety Institute that is trying to make this a little bit more formal. And I know that some
*  folks like to criticize Anthropic and Cloud for being very careful, but the reality is that yeah,
*  we need to be careful. And many also about Google for right away releasing these things.
*  Folks, let's take a pause here and think about consequences. We want to push the technology as
*  fast as possible. I want that. We all want that. We want the revolution. But don't always be so
*  cynical. Think about that there's a lot that happens that you may not know about.
*  That's a big part of why I do this show is I think that there's a strong reason on both sides of the
*  the analysis, you know, the the opportunity to accelerate science, you know, upstream of medicine,
*  obviously incredible. You can't can't be denied. And yet at the same time, I do think the potential
*  for things to go a little haywire is is very, very real. There were a couple changes that I noticed
*  from the original paper to the final one. One was that you dropped the use of the word emergence.
*  Which is, you know, kind of been through the wringer. I'm interested in your thoughts on
*  emergence. And then another is that you drop the section on generating ideas about new cancer
*  drugs. And that I think is is also it is like super interesting. I'm curious as to why that got
*  as to why that got dropped. And I'm also curious as to kind of how you would characterize
*  just how good we talked about this a little bit earlier when you were like it's you know,
*  in the context of reaction optimization, it can match the Bayesian optimizer. But I'm wondering,
*  like, in terms of like outside the box thinking, you know, like the kind of question was like,
*  you know, can you come up with a new cancer drug? There's something there that, you know,
*  you're kind of we're looking for these like eureka moments. And I used to say we haven't
*  seen any of them. And now I feel like we've seen like a few but precious few. So emergence
*  and kind of eureka moments are my two questions. And I, you know, specifically noticed those through
*  the changes from first to nature versions. I think that the eureka moments that came here
*  was like really being able to do a lot of the tasks that, you know, otherwise would take a lot
*  of time. And we have this video, unfortunately, it's not public, but it could be comparing a very,
*  very good researcher against coscietists on a given task. And coscietists finished the task
*  in about four minutes with codes that, you know, is ready to be run. And this very good researcher
*  after about 15 minutes had code that will not even run. So that I see as like, it's a,
*  you know, a lot of people are like, okay, what did you discover? Well, what discover is what we
*  are going to discover, like, you know, like it's a different way of doing what I've been doing
*  for centuries. That's what it is, first of all. The main reason why we decided to remove that
*  section is because, you know, preprints are drafts and that part ended up being a little bit out of
*  focus with the overall story of what the paper is trying to explain and tell in a new form.
*  And we had to prioritize certain things. The development of, say, you know, asking for
*  cancer drugs or whatever. It was a little bit too open question that in retrospect, I think that we,
*  it can have a lot of very useful ideas, but I remember laughing pretty hard about like
*  the agent at that point to just going for carabinoids because there's so much about it
*  on the internet, I guess. And it's like that kind of sub bias in the, in the, in the, in the,
*  GPT-4 that unfortunately leaks through in this, not explicitly, but that, that was my,
*  my shield at that point. And then, you know, this is on, on that and we really wanted to do something
*  that was much more focused. So it was like, okay, let's, let's remove this. And that's also a reason
*  why I see the two works almost different, like different works. So emergence. Yeah. So I am not
*  purist of that word to, to say that I know that there are folks out there that believe that
*  emergence is only something that you can talk about in the biological context or that others
*  come to say it's like, there's no real emergence of whatever capabilities in, in LLMs and so on.
*  I mean, come on, let's just use the word as, can we just use the word as a, as a proxy for
*  we do train, focus on this, and now we have these capabilities and so on. That's, that's how I see
*  it. Right. And that comes of course from scaling and so on, the different types of data,
*  different quality of data that goes into, into using these models. You see,
*  any model can do some really amazing things. Right. And are we going to say, oh, you know,
*  five two does not have a margin self-like, like capability of solving pretty nice college level
*  physics problems. No, like it's fine. I, sometimes I feel like we get caught up in certain
*  words too much without actually trying to think about the overall message. And this was one of the
*  words that I will say during the overall, you know, rounds and rounds of peer review and many
*  online and not were pretty, so that I could forget where they're upset about it. So
*  I don't care enough to fight for it. I think that it's more important. It's like, hey, the work is
*  this, it's a tool, it makes mistakes. I don't think we, like no one trained for it to be a
*  coscientist and here we are. So is it an emergence capability? I'll let people decide. Yeah.
*  Exercise for the reader. Okay. So maybe last question. This is a good positive note to end on.
*  You know, toward the beginning, obviously we talked about my experience as a research assistant
*  and just how much grunt work it really was. Now we have coscientists always worth reminding
*  ourselves that this is the worst that this technology is ever going to be. So let's say I am,
*  you know, considering a PhD in chemistry or chemical engineering now, what is my PhD going
*  to look like as I start to have coscientists, you know, as kind of the new normal? And I'm interested
*  there in terms of like, how much faster can I go? Maybe also like how much coscientist budget do I
*  need, you know, but, and how much more can I accomplish in the course of a couple, few years
*  of research compared to the before? I'd love to, you know, this could be your pitch for your lab
*  or for the hard sciences in general, but I'd love to hear kind of how you think this will be different
*  now that we have these enabling tools. Definitely a lot of things will change. We'll be able to pay
*  less attention on certain mechanics that are time consuming, but not really pushing knowledge forward.
*  So I cannot speak for PhD in chemistry or chemical engineering anywhere and everywhere. I can speak
*  for the groups that I know that are using these things like again, Philippe Schroeder at the PFL,
*  Andrew White and many others. I should really mention Alana Sputeguzik in Toronto, my postdoc
*  advisor that is one of the pioneers in machine learning for chemistry period, and they are pushing
*  extremely hard there for massive innovations. And the PhD experience will change, definitely.
*  And, you know, I see, for example, I hope to see in biology become shorter so that both people can't
*  go to the workforce faster because they don't, you know, don't biology. There are problems,
*  biology is hard because biology, but you get the idea. In chemistry, I what I want from people that
*  come to my group and work here is what are the big questions that you're trying to solve? What keeps
*  you so focused on a problem that you want to tackle, right? So there are people in my group
*  working on things that are basically applied math information theory, and there are people that are
*  really pushing the bothers in bio-coalysis. And for all of them, what we have is now a way that
*  dramatically diminishes the amount of time that they need to spend doing things that do not
*  help them actually answer that question. And the questions can become more complex and more general.
*  I am so excited about what we're going to be able to do going forward because we are not encumbered
*  by, you know, having to worry so much about these things that took a lot of time but did not push,
*  did not advance the knowledge. It's going to be awesome, right? It really is. We need to embrace
*  it and it's going to be really great. And by the way, one thing that I really want to see,
*  and I do not know how long it's going to take, is that, hey, this is not just chemistry or computer
*  science or bioengineering anymore. Forget, let's just go over these boundaries because the main
*  discoveries and solutions really occur at these interfaces between different fields, right? That's
*  how I really like to see things. And Mike, we're interested in developing new reactions, for example,
*  to tackle glycans and sugars that in the body, they are yet another piece of biology that has
*  been severely under-explored because the chemistry of it is so difficult, right? So
*  we had Carolyn Bertosy get the Nobel Prize in chemistry two years ago showing that you could
*  do chemical, like click chemistry. Okay, now let's go and follow her footsteps and explore those
*  things by developing the technologies that will allow for us to modify sugars. That's the kind
*  of thing that I'm super interested in. And I just want people to really ask hard questions
*  and be able to go into it fearlessly without needing to worry about the administrative
*  things that don't really help them or like writing codes that is just an operation in the process.
*  I think we are up in for a revolution in how education works and how discoveries will be made
*  much faster. We are already there, not because of coscientists at all. Just look at Alpha Fold.
*  That was amazing. Definitely one of the most important discoveries of the last decade.
*  Where are we going to go next? I don't know, but I know it's going to be fast and it's going to be
*  powerful. I think that is a great note to end on. You have given us a glimpse of the future with
*  coscientists at a minimum. Gabe Gomez, professor of chemistry and chemical engineering at Carnegie
*  Mellon University. Thank you for being part of the cognitive revolution. Laysa, thank you so much.
*  This was awesome. It is both energizing and enlightening to hear why people listen and learn
*  what they value about the show. So please don't hesitate to reach out via email at tcr at turpentine.co
*  or you can DM me on the social media platform of your choice. Omniki uses generative AI to enable
*  you to launch hundreds of thousands of ad iterations that actually work customized across
*  all platforms with a click of a button. I believe in Omniki so much that I invested in it and I
*  recommend you use it too. Use CogRev to get a 10% discount.
