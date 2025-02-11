---
Date Generated: May 18, 2024
Transcription Model: whisper medium 20231117
Length: 4388s
Video Keywords: []
Video Views: 5780
Video Rating: None
---

# The Book I Wish Every Policymaker Would Read
**The Ezra Klein Show:** [June 06, 2023](https://www.youtube.com/watch?v=hVXUYQ84Ww4)
*  In 2009, Jen Palkow founded Code for America.
*  The idea behind Code for America was to get the best technologists working on the public's
*  problems, not just private websites and e-commerce platforms and social networks.
*  Even then, it was clear that public digital infrastructure was going to be really important
*  and it was lagging far behind the private sector, and Code for America was built to
*  bridge that gap.
*  Then in 2013, Palkow became deputy chief technology officer in the Obama administration.
*  She was very deeply involved in the effort to rescue healthcare.gov and helping create
*  the United States digital service.
*  Then she went back to Code for America and then in 2020 was tapped by California governor
*  Gavin Newsom to help untangle the mess of California's unemployment insurance program
*  as it buckled under the weight of the COVID response.
*  I mention all that because Palkow's worked directly on and then helped oversee and advise
*  teams working on the digital delivery of government services really at every level of government
*  across much of the US.
*  So she's someone who badly wants government to do good in the lives of people and has
*  spent years now confronting the reasons it so often falls so short of its goals.
*  One of her big points, one I've come to appreciate a lot more in recent years, is that even liberals
*  who care a lot about government don't care enough or track closely enough how implementation
*  actually happens.
*  Delivery often happens out of sight, except for the people who need that delivery.
*  In our media, I mean we're part of this, I'm part of this problem too, there's a ton
*  of focus on politics, on elections, on big policy questions and fights and theories.
*  But then the bill passes and the nitty gritty of how that policy actually shows up in people's
*  lives is left up to someone, somewhere.
*  And when it doesn't show up in people's lives or even makes people's lives worse because
*  of how it is implemented, there's often no outcry because there's no attention and so
*  there are no fixes.
*  Now Paulka has written this book, Recoding America, and I want to say it clearly, this
*  is one of the best policy books I've read.
*  It's a book I hope future governments and current governments will absorb.
*  We get at a lot of it in this conversation, but not enough.
*  But one thing she really does is tell clearly the stories and tell clearly the lessons she
*  has seen and learned about why things go wrong, even when the people involved are trying to
*  make them go right.
*  So people who care about these issues really should pick it up and read it in full.
*  But this conversation is a really rich place, I think, to start.
*  As always, my email, Ezra Klein show at NYTimes.com.
*  Jen Paulka, welcome to the show.
*  Thanks for having me.
*  So I want to begin with a quote that feels in a way like the organizing thesis of the
*  book, which is, when systems or organizations don't work the way you think they should,
*  it is generally not because the people in them are stupid or evil.
*  It is because they are operating according to structures and incentives that aren't obvious
*  from the outside.
*  And I love that because for me, it's a bit of a credo and reporting on government, but
*  you've been inside government.
*  So tell me a bit about how you came to that view.
*  I've seen so many people frustrated with government services, and they make a lot of assumptions
*  about how that government service got to be the way it is.
*  One example I spent a lot of time on was SNAP in California, Supplemental Nutrition
*  Assistance Program, where the application form was over 212 questions.
*  It took a long time to fill out, and so people naturally assume that this is done on purpose,
*  that the people making the form must not want people to get SNAP.
*  And for example there, that's not really what was going on.
*  California is a very pro-welfare state.
*  There's a huge number of incentives for local communities to sign people up for SNAP.
*  It's great for their economy.
*  It's great for getting people out of emergency rooms, for instance.
*  But there are just so many stakeholders in this that they all got to pile on their questions,
*  and you ended up with something that was really, really burdensome.
*  And it's hard to see those incentives from the outside.
*  That's just one example of them.
*  But our public servants are incented to do things that if you look at them rationally,
*  don't make sense.
*  You have a great line in that section, which I'll probably get wrong in the paraphrase,
*  but you say something like, people often think it was designed this way, when the truth is
*  it wasn't designed at all.
*  I think that's true of so many things that we think are systems.
*  I also think it's true of the policy.
*  Take unemployment insurance, for example.
*  We've had layers and layers of changes on it over time.
*  Those changes come from federal government, they come from state government, they come
*  from executive, legislative, and judicial branches.
*  And so what you end up with 90 years later, almost, is something that's just sort of a
*  mess of changes, but not something like thoughtfully crafted by policymakers in DC that is now operating
*  in some rational way at the state level.
*  So I thought a lot about whether or not to do this, because there's probably a best practice
*  of podcasting, where you start in the examples that are going to be attainable, and people
*  already know, and we have a bunch of those, healthcare.gov and California employment insurance.
*  But I want to start actually with Weed's year one, which is, tell me about the enterprise
*  services bus.
*  Okay, you want to hear about the ESP.
*  Yeah, because I think it gets at this point of systems where clearly nobody was trying
*  to do something wrong here, and yet.
*  Yeah, I think everyone was trying very hard to do it right.
*  So a friend of mine, Matthew Weaver, was assigned to go help a team at Raytheon who had a contract
*  with the Air Force to do essentially the next generation of software for the satellites
*  that enable global positioning system, GPS.
*  So something that's pretty important to all of us, especially people like me who need
*  it all the time.
*  And when he got there, he found that one of the big things that was hanging them up was
*  that they had to get the data from the satellites to the ground stations, and there's a very
*  industry standard way of doing this.
*  It's the obvious way you would do it.
*  But instead, the team had inserted this thing called an enterprise service bus or ESP, which
*  technical people will know as something that was really popular in the 80s and 90s.
*  But it's a big clunky piece of software.
*  And it was kind of creating this Rube Goldberg machine that made the data go from the normal
*  the easy protocol into this crazy mess of code and then back out again.
*  And it would time out.
*  You couldn't get the data from one place to the other in time.
*  They'd spent months on this and they couldn't figure it out.
*  And he's like, why are we using this ESP when this other protocol would work fine?
*  It's a requirement in the RFP that the Air Force had put out.
*  An RFP being a request for a proposal.
*  So the RFP is how the Air Force ends up with Raytheon building this thing.
*  Exactly.
*  And we're going to talk about the contracting in a bit.
*  Yeah, we'll talk about the contracting.
*  So Raytheon can't take it out because they say, no, the Air Force is requiring us to
*  do this.
*  Why is the Air Force requiring it?
*  Because the Department of Defense requires it.
*  Why does the Department of Defense require it?
*  Because there's something called the Federal Enterprise Architecture that requires it.
*  The story of the Federal Enterprise Architecture goes back to this act called Klinger-Cohen
*  I think 1996, where Congress said, like, we need to get a better handle on digital.
*  We're not doing technology well in government.
*  Let's make every agency create a plan and then let's have those plans be coordinated.
*  And the Federal Enterprise Architecture was the attempt to coordinate those plans.
*  So one of the things they put in there was that things needed to be interoperable.
*  And they offered in there, as an example, this very common type of software at the time,
*  enterprise service buses, as an example of how you might get things to be interoperable.
*  They weren't actually a great idea at that time.
*  They were already kind of becoming sort of obsolete, like essentially application programming
*  interfaces, APIs that sort of run the internet now kind of took them over.
*  The problem really wasn't that they were specifying something outdated.
*  It's that because it was in this document as a suggested way of doing what the Federal
*  Enterprise Architecture said should happen, when it got translated down to the Department
*  of Defense Enterprise Architecture and the Air Force Enterprise Architecture, each layer
*  in that hierarchy interpreted it more and more rigidly until at the Air Force Enterprise
*  architecture level, it's assumed to be required in all software forever.
*  And so the team is saying, I can't take this out.
*  The law requires it.
*  In fact, the law does not require an enterprise service bus.
*  But the people who have made all of the documents that govern the creation of the software for
*  these satellites believe that it is.
*  When I was reading that story, it reminded me of a piece I just spent a couple months
*  working on about what I called everything bagel liberalism.
*  And that was a piece that was in part about affordable housing and part about semiconductor
*  contracting.
*  And it was a weird piece of work to be honest in its structure.
*  But when I was reporting on the basically request for proposal the Biden administration
*  put out for its semiconductor grants, one of the things that came up as I was talking
*  administration about all of the additional layers of requirements and asks and, you know,
*  having a childcare center and this and that that ended up in the bill, I would hear about
*  people say, look, we think those things are good.
*  You don't realize we actually fought a bunch of these battles and knocked a bunch of stuff
*  out that otherwise would have been there.
*  And then I would read the text.
*  And I would see the thing they told me was knocked out in the text.
*  But it was a suggestion.
*  We're not requiring this.
*  But you know, one good example of how you might achieve this goal we are requiring is
*  this.
*  And it was really striking to me that people were telling me on background that they had
*  fought and won this fight to not have X in the notice of funding opportunity.
*  And then I had read the notice of funding opportunity and X was there.
*  And it was true that it wasn't required.
*  But it seemed very likely that the semiconductor firms were going to think it was required
*  or at least think and this was a plain reading to me, too, that they would have a better
*  chance of winning the grant if they put it in there.
*  And so there is this way in which even when people seem to think they've created flexibility
*  in the actual language, once the lawyers get hold of it and the contractors get hold of
*  it, it's really not that flexible.
*  There's so much better safe than sorry thinking going on.
*  And I would say with contractors and with people who do the compliance, right?
*  And those bids that those companies give back, they know they'll be judged by people who
*  are really just checking boxes like does this meet this?
*  Does this meet this?
*  And they're going to check that box.
*  I think it's a good example of the sort of disjuncture between the thinking of policymakers
*  and the reality of how that policy plays out.
*  Another good example of it is FISMA.
*  It's the Federal Information Security Management Act.
*  Which I only know because I have your quote on this sitting here in my next paragraph.
*  I've gotten pretty good at remembering what all the acronyms stand for, but there are
*  a lot of them.
*  It can be hard.
*  So FISMA is a law that covers cybersecurity and it has these 300 controls in it.
*  So 300 different things that you, according to law, could do to secure an application.
*  So it's like a menu, not 300 mandates.
*  But in practice, if you ask pretty much anybody who does software in government, they have
*  to do all 300.
*  And it's because I think it's evolved such that in order for people to sort of cover
*  their butts, they have to explain why you didn't do numbers 138 through 192 or something.
*  And it's really hard to do that.
*  In fact, it's sometimes easier just to do the controls than it is to explain them.
*  But the people in the middle who are doing the compliance have no idea if for your application,
*  numbers 35 and 95 are the two really, really important ones.
*  And you should spend the rest of your time on the thing that's most important to security,
*  which is testing.
*  All they know is that they will be responsible if anything bad happens.
*  And if it was, you know, control number 96 that gotcha, it's their butt on the line.
*  So they will insist on all of them.
*  And if you go talk to the people who wrote FISMA, they will say we never intended that.
*  So this gets at, I think, a really important point you make about that incentive system,
*  how it is actually designed versus how it might look from the outside.
*  You write that public servants are trapped between two distinct systems of accountability.
*  So what are the two?
*  Well, you know, when things go wrong, we're very upset with public servants.
*  I mean, healthcare.gov is a famous example.
*  There were like 10 hearings in one month about this and they're televised and we're upset
*  because the thing doesn't work.
*  That's an outcome.
*  What public servants are actually hired for, promoted for, what their careers depend on,
*  is fidelity to process.
*  It's a compliance framework.
*  And so yeah, if you didn't do number 96 and something goes wrong, that's what the sort
*  of administrative state will focus on.
*  The people who do oversight focus on whether you checked all the boxes, not whether it
*  works.
*  It's quite true in people's careers that they are not punished for something not working
*  as long as they can say, I did what the procedure prescribed.
*  Something this gets at is that we have civil service protections, that politicians are
*  mad at the outcome of something civil servants did.
*  Might allow them to embarrass the agency.
*  They might even cut funding for the agency in the future, although often they don't.
*  But they can't fire anybody.
*  They can't really create that many consequences for the agency.
*  Whereas failing to follow process, you really can get fired.
*  You really can lose your promotion track.
*  There really are consequences.
*  And so in a weird way, the people who made the policy in the first place and in theory
*  are exposed to the voters who are supposed to be the judges of the policy, actually do
*  not have power really to hold the civil servants accountable.
*  And there are good reasons for that.
*  I mean, there are good reasons for civil service protections, but there is also consequences
*  to it, which I think, frankly, on the left are pretty underplayed.
*  Yeah.
*  I mean, I heard so many times when I worked in government, you could get fired for that.
*  In fact, you hear frequently you could go to jail for that.
*  It doesn't really match the reality.
*  People don't get fired that much and they certainly don't go to jail.
*  We used to have a joke about, really, I'm going to go to procurement jail?
*  Where exactly is procurement jail?
*  It's like such a nerdy piece of law and policy that certain people understand.
*  But there's this perception that a small violation of it is going to end you in jail.
*  It doesn't really match the reality, but the culture has definitely evolved to highlight
*  any deviance from process and make it very, very risky.
*  It can be risky on just a practical level.
*  You might not get demoted.
*  You might not lose your job.
*  But suddenly people are not wanting to work with you.
*  There can be sort of cultural consequences to it and just your ability to get the job done.
*  Tell me about the Paperwork Reduction Act.
*  So this is a great example of a law that sounds great.
*  And it sounds like something that's really important to me because it's supposed to reduce
*  the paperwork burden on the American public.
*  And I think the paperwork burden is a real problem in part because, as I say in the book,
*  paperwork favors the powerful.
*  The more paperwork that's required, people with resources will get through it and people
*  without them will not.
*  So this law said essentially something we all believe.
*  If you measure it, you'll be able to manage it.
*  So I always call it the comically misnamed Paperwork Reduction Act because it's designed
*  to measure the burden of any safe form that you have to fill out.
*  Your tax form, for instance, the 1040, that has an OMB number, which is required by the
*  Paperwork Reduction Act.
*  And it means that the Office of Information and Regulatory Affairs, known as OIRA, reviewed
*  the time it would take to fill out this tax form and stamped its approval.
*  And so it's got this measurement on it.
*  The problem is that it got interpreted very broadly to say anytime you speak to a member
*  of the public about a form like this, that has to get OIRA approval.
*  So in the tech world and consumer product world, we have something that's really important
*  to the usability of our services called user research.
*  The way we make a form easier, like that tax form, is that we watch people filling it out
*  and when they get stuck at a question like what were your last year's date taxes, we
*  go, okay, we've got to make that easier on that person and we redesign it.
*  So we have this very important discipline called user research that is how we streamline
*  forms and applications and make them a lot easier to use.
*  So it involves something like watching you fill out that tax form and seeing where you
*  get stuck, seeing where you have questions, asking questions like does this question actually
*  need to be on this form?
*  How do we make it easier for the user?
*  But when you assume that every single interaction with a member of the public needs to go through
*  OIRA, then your user research needs to go through an OIRA approval process.
*  And because that process can easily take nine months and sometimes longer, you essentially
*  can't do user research.
*  But this is weird because you point this out in the book.
*  It would seem from a plain reading of the law that user research is exempted.
*  Yes.
*  And yet?
*  And yet.
*  There are examples of this going on every day in federal government now.
*  There's also examples of people getting through it and not being required to get OIRA approval
*  for user research.
*  But essentially what happens is, in fact, a friend of mine whom you know, Erie Meyer,
*  who's at the Consumer Finance Protection Bureau, had this happen to her the other day, she
*  was already doing user research and they said, oh no, we're going to have to send this
*  through OIRA approval.
*  I mean, they were already doing it, which is the crazy thing.
*  And essentially the person in the agency decides that better is safe than sorry.
*  It's better to be safe than sorry.
*  And says, I understand your interpretation, but it's my butt on the line if someone else
*  calls a foul on this.
*  So we're sending it up to OIRA for their review.
*  Now OIRA could say, obviously this is wrong and silly, and there's no need to get our
*  approval, but they also take a better safe than sorry stance, again, because of the incentives
*  to them.
*  And the result of Erie's request was that they said, this will have to go up on the
*  federal register and we will have to get comments from the public about whether these people
*  can get comments from the public.
*  Oh, and in the meantime, there'll be no user research or no comments from the public happening
*  until this process is over.
*  I just want to note that everybody in this story is a liberal who wants government to
*  work well.
*  Yeah.
*  I just think that's important to say here because it's something you say towards the
*  end of your book that working in government is a really valuable thing to do in part because
*  it will change your view on what sometimes makes government work poorly.
*  And one of the almost spiritually difficult things about reading your book, if you're
*  somebody who does care about government, is knowing that this is a lot of people who are
*  doing their best, who have in many cases much more difficult jobs, who require much more
*  endurance and creativity to serve the public than anybody in the private sector does.
*  And yet we're getting this outcome somehow, right?
*  I've known a lot of people at the top of government, the people who work in offices in the West
*  Wing, and they're all very, in some conceptual way, aware that government is inefficient,
*  they don't want it to be, right?
*  Bill Clinton had Al Gore do reinventing government, Barack Obama hired the first CIO to look over
*  the government chief information officer, right?
*  Joe Biden is somebody who, when he was a senator, often talked about government inefficiency.
*  Their chiefs of staff are impatient, management-oriented people.
*  And yet somehow from the top, even though they talk about this all the time on the campaign
*  trail, like no Democrat wants to be a pro-inefficient government Democrat, this does not filter
*  down somehow.
*  Why?
*  I think you have to look not just at the executive branch and administrative agencies, though
*  you shouldn't not look at them.
*  I mean, I think it essentially comes down to you come in with a passion for cutting
*  the red tape and making this easier.
*  And two things happen, you get worn down and you have other priorities.
*  It's really, really hard to spend all your time on this and you're not in control of
*  it.
*  When I worked in the White House trying to stand up what became the United States digital
*  service, we were originally going to do it in GSA, which is the General Services Administration.
*  And the head of the GSA is a fantastic public servant named Dan Tagherlini.
*  And he really, really wanted this unit in his agency.
*  And he was actually blocked by a guy below him who kept calling out that sort of better
*  safe than sorry on some very obscure interpretation of how the money that we were going to use
*  to stand up the unit could be used legally.
*  I mean, he was wrong, but he could construe the language that way.
*  So you have to actually have some empathy for people at the top who are fighting as
*  hard as they can to get stuff done and are blocked by people not just above them, but
*  around them and below them.
*  There's another dimension here that you point out.
*  And it's a sociological observation about government that as soon as I read it, I realized
*  it's completely true.
*  That knowing a lot about politics is very high status in government.
*  If you're considered like a tactical political genius, that's great.
*  Knowing a lot about policy, having very big policy ideas, that's also very high status.
*  Implementation isn't.
*  No.
*  Why?
*  I think it goes back very deep in our culture.
*  I mean, I think that's not just true in government, let's be honest, right?
*  Big ideas people get a lot of status in our society.
*  Thank you for listening to my TED talk.
*  Well, yes, big ideas guy.
*  A friend of mine who worked in the government digital service in the UK pointed me to this
*  idea that's written about the British Civil Service, that it is literally divided between
*  the intellectuals and the mechanicals.
*  Now I think that the digital age has complicated this in a lot of ways.
*  If you look at say, metaphysical Silicon Valley, if coding is a mechanical task, it's the
*  way you implement something.
*  All those companies were founded by coders.
*  Mechanicals in that framework are sort of at the top.
*  Lots of interesting good and bad things have come out of that culture, which is really
*  distinct from the culture of government where the intellectuals are at the top and have
*  the power.
*  The people who write the code or do the designs that implement these programs are really,
*  really, really far down.
*  Like they're at the very bottom.
*  In a way, they're not even at the bottom, they're outside.
*  This is true.
*  Tell me about circular A76.
*  So a couple of decades ago, the federal government said, this is actually coming out of OMB,
*  the Office of Management and Budget, but it really derives from a long history of trying
*  to streamline government, said, if someone else can do your job in government, we're
*  going to outsource it.
*  It's the reason we have things like the concession stands in national parks are run by third
*  parties, like they're not run by the government.
*  That's all A76.
*  And there's a real valid justification for some of this.
*  There's a famous case in which I think during World War II, government decided to make its
*  own steel because there wasn't enough.
*  Well, by the time they finished that, it was wildly expensive and very bad.
*  And it's a commodity.
*  The market can provide us good steel.
*  That is the best way to do that.
*  We should not get in the business of steel.
*  And so on that basis, they sort of roped a lot of other things into that, like concession
*  stands in federal parks.
*  There's no reason that's inherently governmental, which is an important phrase that very few
*  people talk about.
*  Because the distinction between something that is inherently governmental, like a government
*  person must make this decision, i.e., most policy decisions, and something that is inherently
*  commercial is like, okay, well, we'll make the policy decision and then we'll contract
*  it out to somebody who just delivers on it.
*  And it creates this real separation between policy and implementation, which has a lot
*  of complications to it.
*  And I think over time has sort of snowballed into some really bad outcomes because we're
*  trying to do policy over here, implementation over here.
*  I have my hands very far apart since your listeners can't see.
*  And so much gets lost in the middle.
*  So that's in a way the guiding principle here.
*  You say it's gone now really far.
*  I mean, you go quoting someone else as far as really saying that civil servants manage,
*  they don't implement.
*  So particularly in the digital sector, tell me about what the government does and what
*  it contracts out.
*  What functions in your experience are done by somebody on a public payroll?
*  And what functions are done by somebody who is being paid out of public taxes but is on
*  a private payroll?
*  So let me speak to what's still pretty standard but changing.
*  But like when I was in government in 2013 and 2014 was really, really standard.
*  If you're trying to get, say, healthcare.gov built, and you're the digital person responsible
*  for it, what you will actually do is work with contracting officers, people to gather
*  a bunch of requirements, lawyers, and you will have to be master of an incredibly complex
*  apparatus of procurement rules and operations and forms that need to be filled out and processes
*  that need to be followed that actually is a very robust skill set and knowledge base
*  in its own in order to hire people who will actually do the digital implementation of
*  whatever it is you're doing.
*  So I talk about somebody in the book who's in fact a fantastic digital leader and gets
*  really good outcomes because he is a good digital leader.
*  But like 90% of his time is spent on procurement and legal.
*  So I want to talk about how procurement actually works because just like it is different to
*  hire and fire in the public sector because of civil service rules, it is different to
*  procure, to pay an outside vendor to do something in the public sector because we have a lot
*  of rules meant to clamp down on cronyism, on patronage.
*  We're trying to make the process fair and we make it cumbersome.
*  One of the things you talk about a bit is the way the system can get slowed down by
*  vendor protest that if you don't win a contract, you can actually protest the entire process,
*  holding it up sort of like if you are upset about people building something, you can bring
*  an environmental quality act objection.
*  Tell me about these protests.
*  Tell me about the ways in which the vendors actually have quite a lot of power in the
*  process.
*  Yeah, these rules were designed to make the process fair.
*  So for instance, an agency will announce a winning bid and if other companies who bid
*  on this think that either something genuinely went wrong or more likely that they can simply
*  take some advantage out of this, they can protest the bid.
*  And because these bids are so wildly complex, I mean, the paperwork required to bid on
*  a major government project, whether it's technology or anything else, is massive.
*  There's a lot to review and there's very little evidence of actual competency that are required
*  in this paperwork.
*  It's all evidence of compliance.
*  And so it's very easy to find something that's not compliant, but the result is easily six
*  months, often year or two delays in getting something done.
*  I think actually the first time we started talking, I became more aware of your work,
*  was in the healthcare.gov debacle.
*  And at the core of that debacle was procurement and who got chosen to build that.
*  So how did these rules end up affecting who got that contract?
*  If you look at the timeline in the ACA, and I'm going to forget the exact times, but essentially
*  they only had sort of three years.
*  The Centers for Medicare and Medicaid Services, CMS, had about three years to get healthcare.gov
*  up and running.
*  They needed to launch it by October 1st, 2013, if I recall.
*  And as I just described, the process of getting a bid together that's incredibly complex,
*  getting all your requirements, getting that contract out to bid, reviewing the bids and
*  then awarding it, and then potentially protests, that's easily three years right there.
*  So they had to do something else.
*  So CMS actually had some vendors on a very obscure vehicle, we call it, called IDIQ.
*  It stands for indefinite delivery, indefinite quantity, which is essentially a way of saying,
*  I've hired you to be around and do what I need.
*  Actually an IDIQ can be a very good thing to have someone just on board.
*  They're basically on retainer.
*  They're on retainer.
*  But like, yeah, for a wide variety of things.
*  And so CGI was one of the companies that was on an IDIQ already at CMS, so they didn't
*  have to bid certain pieces of it out.
*  Now, let me be clear, there were 60 different contracts to vendors to build healthcare.gov.
*  Some number, like 12 of them, went to CGI, which is considered the main contractor, and
*  others went to others.
*  So it's not like they had the whole thing.
*  But they really couldn't have done that full process where they bid it out, because if
*  anybody had protested, they would have had no hope of making their congressionally mandated
*  deadline.
*  I think it's worth spending a minute here, because I covered the drafting of the Affordable
*  Care Act really closely.
*  I covered how they were thinking about building the insurance.
*  Oh, and you missed this.
*  And not only did I miss this, but I can say with certainty that there was a lot of excitement
*  in Congress about, we're going to create these online digital marketplaces, and it's going
*  to be a next generation website, and you're going to be able to compare everything.
*  And I'm sure in Congress's mind, having talked to people, the way they thought about this
*  is the government would go for this unbelievably marquee project and get a really great website
*  design player.
*  I mean, Google doesn't do a ton of government contracting in this particular way.
*  They do other things.
*  But someone like Google, right?
*  Just whoever's the best.
*  And this would be a great project.
*  Instead, you end up with a pretty obscure contractor, and to me, this is important,
*  who I'm not saying this is their only competency, but across a bunch of these contractors, what
*  they have is a competency in contracting.
*  They know how to work with the government, which is a huge pain.
*  And this feels like another place where the procurement rules and the way different regulations,
*  etc. have been interpreted.
*  It's really not what the legislature was trying to do.
*  They wanted a great website.
*  What they got was a total disaster.
*  But they didn't think go back and change procurement rules either, really, to my knowledge.
*  Well, the legislators would say, we have given agencies, and I'm not sure about this particular
*  case at that particular time, but this happens in the Department of Defense all the time,
*  we have given you lots of exceptions that you can use.
*  There's something called an other transaction authority, which basically gets rid of a lot
*  of those rules and lets you sort of choose who you want to choose in a streamlined kind
*  of way.
*  But they just don't get used.
*  And that, again, goes back to people say better safe than sorry.
*  If something goes wrong, someone is going to come back and say, what justification did
*  you have for using OTA, other transaction authority, instead of the more robust way
*  that we know will ensure, quote unquote, fairness.
*  So it's really that culture that comes back to it.
*  I mean, it's a reasonable example, I think, of what I talk about in the book is culture
*  eats policy, right?
*  The policy that is designed by policymakers wants to get the outcome of flexibility for
*  the agencies because they know that rigidity is hurting the outcomes.
*  But the culture just goes back to, I see that you've given us that, I'm choosing not to
*  take it because I feel like it's going to make me safer.
*  So healthcare.gov was this huge project that had to be contracted from top to bottom.
*  But I also want to talk about the ways in which this kind of contracting makes it hard
*  to update systems as policy is changing.
*  And I want to use a pretty horrific example that you talk about in the book, which is
*  the child separation policy at the border.
*  So obviously, the actual policy there was terrible.
*  But one thing that made it much worse was the rigidity of the system being used.
*  Can you go through that?
*  When the Trump administration ordered that kids and parents be separated at the border,
*  the systems that tracked families could only assign one what's called a number, alien
*  number to a family.
*  That's how it was set up and had worked for years.
*  So just horrible. It's called an alien number.
*  It's called an alien number, though they call it a number, which is also really confusing.
*  So if a family of four comes through, they get one a number because in the past they
*  were treated as a unit.
*  This horrific and cruel policy comes down.
*  They separate them.
*  They now give you one a number, your partner one a number, and your kids get a number
*  separately. And there is no affordance for connecting your a number with your children's.
*  They were pinning sticky notes with a numbers on infants who had been taken from their
*  parents. And there were wonderful public servants who were writing down, keeping
*  spreadsheets, trying to track the connections between parents and kids.
*  It wasn't like there was no effort made, but there wasn't a systematic way to do it.
*  There was a lot of chaos.
*  The person who's trying to reunite them is not necessarily the person who separated them
*  in the first place. And so when, thankfully, that order was reversed, there was very
*  little capacity within the Customs and Border Patrol to fulfill the demand to reverse it
*  and reunite these kids because the software didn't have any affordance for making this
*  connection.
*  So something you then talk about is it would have been a fairly obvious move again,
*  without either of us endorsing a terrible policy, but would be fairly obvious move if
*  you're doing that policy to change the software so that the a numbers are tracked
*  together. Why didn't they?
*  What would that have taken?
*  So I should caveat by saying I don't know the specifics of the CBP contracts that govern
*  this software, and I've never seen this software in action.
*  But I do know that the way this generally works in government is if you want an update to
*  your software, you take it out to bid.
*  And that takes a really long time.
*  And yes, the company that may have originally written it will bid on it, but you're not
*  guaranteed to give it to them.
*  Maybe that's the right thing. Maybe that's the wrong thing.
*  But if you have a new vendor, they have to get up to speed on the code base.
*  But essentially, the way we think about software in government, it's a project.
*  Like you start it, you finish it, and then there's a little bit of money trailing along
*  for you to keep it up and running.
*  So when you have a change like this, that's frankly incredibly urgent.
*  You don't have people who work on that software day to day, week to week that are there
*  ready to change it and know how the code base works.
*  So in contrast, Google didn't create search and then lay off 95 percent of the staff and
*  keep just a skeleton crew around it to keep it up.
*  The way things that really work in the real world are staffed is on an ongoing basis, not
*  only to make sure that changes in some connecting database somewhere can be updated so the
*  thing doesn't crash, but also because we live in a dynamic world.
*  Like we can't expect there not to be policy changes that have to be incorporated.
*  And frankly, we should be constantly looking at the software and saying, is it doing what
*  it could be doing as well as it could?
*  There's constant improvements in the consumer products that we use.
*  So the curve of staffing in a consumer product is sort of like it starts really slow.
*  And then as the product becomes more and more clearly valuable and popular, the staffing
*  goes up and up and up. It's just this like constant curve up.
*  That's how the software is constantly better and more usable and more valuable to us.
*  In government, it's this weird sort of like there's nothing.
*  Then you hire all these people and then there's a couple year period where lots of people
*  are working on it and then it drops to almost zero.
*  So after almost zero, you have no capability to change that software.
*  You have acquired software, but you have not acquired the capability of doing what that
*  software is supposed to do, of performing the function on an ongoing basis that that
*  agency is responsible for.
*  I think this brings us back to healthcare.gov, which is a real, I think, before and after
*  moment for how digital is viewed inside the government, because it is built and broken
*  by this contractor or set of contractors.
*  And the rescue effort is a much more internal process.
*  It is built on now the idea that you actually need internal capacity and flexibility.
*  And because of the president is focused, there's a lot more ability to move quickly and
*  make decisions.
*  So tell me a bit about the principles and staffing that the rescue effort is built on.
*  The rescue effort came at a time when we were trying to prove the point that you need an
*  internal capacity.
*  So as disastrous and horrible as it was, it was actually really useful for me and others
*  who were saying, hey, we can't just have procurement competence in government.
*  We have to have some digital competence in government.
*  In fact, we need it in the halls of power in the White House and in OMB.
*  And I think one of the reasons it worked is that they could see through the rescue effort
*  that we could bring in people whose competence wasn't how do we contract with company, but
*  how is the software actually work and what's wrong with it?
*  So the people who came in were software engineers.
*  Many of them happen to have this title at Google and other companies called site reliability
*  engineers, SREs.
*  You've never heard of an SRE in government.
*  There literally never was one.
*  That was always the responsibility of an outside company.
*  So you had people who could actually look at the code.
*  And in fact, we found that oftentimes the people at the vendor who were supposed to
*  have done the coding didn't really even know how to code.
*  So you had all these people who knew how to work with government, but didn't actually
*  know how to make the site work.
*  And bringing in folks who could actually get in there in the weeds and was the thing that
*  changed it.
*  The process up to that point had relied a lot on planning.
*  There's this real focus on planning in government for lots of jobs.
*  If you want to get promoted, you have to have this thing called a PMP, a project management
*  professional, and it's all about upfront planning.
*  But it's really hard to plan in a situation like healthcare.gov where they are still
*  finalizing the regulations and rules that govern it right up to the launch of the site.
*  So the skill that was needed was not this very traditional plan everything then execute
*  to it.
*  You needed people who were basically good at sort of what's going on with users.
*  Is it working?
*  Just go find problems and solve problems at a very detailed technical level instead of
*  looking at project plans that were not actually connected to the experience that users have.
*  One thing you say about the healthcare.gov experience is that there were a lot of reasons
*  that went wrong.
*  And you know, there are GAO reports on it and I wrote a piece for Business Week about
*  it back at that time.
*  And you know, I mean, there's a huge amount of attention on this.
*  But you say if you could boil it down to one, it's that there was a lot of process
*  management, program management, but not a lot of product management, not a lot of people
*  willing to say, no, we're not going to do that, empowered to say, no, we're not going
*  to do that.
*  Can you talk about that distinction?
*  So project management is the art of getting things done.
*  It is hugely important.
*  I value good project managers very highly and everyone should.
*  Product management is the art of deciding what to do in the first place.
*  And if we don't do that, then the project managers just are overwhelmed with a sort of
*  undifferentiated, unprioritized mess of requirements that they have to fulfill.
*  And yes, healthcare.gov, there was a lot written in the law about what needed to happen.
*  It was probably over specified, but there was also not a willingness to sort of even imagine
*  that you might do less.
*  In fact, people were told you can't do less.
*  You can't not serve every single edge case from day one.
*  For instance, that's illegal.
*  There's reasons why they think it's illegal.
*  I do not think it's illegal.
*  And I think we've proven since then that it's not.
*  But that willingness to say it will launch serving the most common set of users because
*  that way we can handle the people who can just use a website to get their health insurance.
*  And then the people who have crazy exceptions or rare exceptions are going to go through
*  the call center.
*  They're going to go through those in-person service centers that they've set up around
*  the country, which makes sense.
*  Those people actually probably need a person walking them through it because of their
*  exceptions.
*  It doesn't mean that the website couldn't eventually serve all of those people.
*  It means that to get a site that launches and works on day one, you constrain what you're
*  trying to do.
*  Get those first people through the door, test the site that way, and then you add the
*  functionality later.
*  That's good product management.
*  And until recently, it literally hasn't existed as a discipline within government.
*  There's both product management as a discipline and I think there's also product management
*  or what in this case I would call prioritization as a political value, as something the
*  leadership values.
*  And you tell a story in there of a conference call while the site is in crisis with Marilyn
*  Taverner, who is head of CMS, the Centers for Medicare and Medicaid Services.
*  Could you tell that?
*  Mina Sheng was somebody who joined the what we'll call rescue effort, though I do try to
*  stay away from that term because there are so many great public servants who were part of
*  the rescue effort and they often feel unseen by that.
*  But Mina Sheng came in to help.
*  And one of her responsibilities was to staff a daily call with the administrator, Marilyn
*  Taverner, and others, including the main contractors.
*  And the site was in total disarray.
*  I mean, I don't remember exactly how long this was in, but this was before we were headed
*  towards, OK, it's starting to work again.
*  And one of the things that she brought up on this call was that in the original spec,
*  there was going to be a separate site in Spanish.
*  Makes sense.
*  I think government services should absolutely be in as many languages as we can to serve
*  people as well as we can.
*  But at that point, even the English language site was very far from being able to work.
*  So Taverner brings this up on the call and says, where's my Spanish site?
*  Now, there's all these vendors on the call.
*  So Mina knows that they're going to try to placate her and say, we're going to get to
*  that and then divert resources to the Spanish site.
*  So she gets ahead of them and just jumps in and says, I'm sorry, administrator, but you
*  can either have one site that works or two that don't.
*  And Taverner hangs up on her.
*  She doesn't want to hear it.
*  And God love Mina, she just kept persisting.
*  But her job at that point was to keep the team's eye on the ball, which is we have to
*  get this site to the point where it's operational and then we can use those resources to
*  make a Spanish version.
*  But it would be pointless to make a Spanish version when this is something that didn't
*  work.
*  One thing that is a worrying dimension of that story is that, and you see this in
*  government a lot, that when things are in crisis, people realize they have to bend
*  rules, they have to prioritize, you know, they can't do everything at once.
*  They have to make the first thing work first.
*  But a lot of things aren't in crisis or, and I think this is actually more often the
*  case, they are, but they're not in crisis for the right people.
*  Which is to say, I think there's a lot of attention to delivery and implementation
*  when the people being delivered to and implemented upon are middle class, are upper
*  middle class, are rich.
*  So healthcare.gov was affecting so many people simultaneously.
*  If you think about the unemployment insurance failures during the expanded unemployment
*  insurance during COVID, that was affecting a lot of middle class people who had
*  political power all at once.
*  There are obviously a lot of programs where they work very poorly for poor people in
*  an ongoing way, but they're not a crisis.
*  And so the ability to say the administrator or to the secretary or to the president or
*  whomever, if they even care about this, hey, we're just not going to do that because
*  this crisis is so big.
*  We have to do the first thing first, isn't there.
*  And so I worry a bit about that.
*  I'm curious to hear your reflections on how things work sort of in what you might call
*  implementation peacetime versus implementation wartime.
*  Yeah, we don't get as much done in peacetime.
*  And I think one of the tactics of people who I respect in this community is to make it
*  a crisis, right?
*  To make the crisis visible.
*  I'd argue that it was a crisis that very few people were getting enrolled in SNAP, but
*  it was not hitting the headlines for sure, for all the reasons that you mentioned.
*  And some great people at Code for America sort of made that a lot more visible and
*  change got to happen.
*  I talk in the book about what was certainly a crisis at the Department of Veterans
*  Affairs where veterans couldn't sign up for health care, but it was completely invisible
*  to the people inside the building because the form that was broken, if you tried to
*  use it from any computer at a library or at your home, wasn't set up with the same
*  combination of Internet Explorer and Adobe Reader that the computers inside the
*  building were set up with.
*  And so the form worked fine for them.
*  And the tactic that the team used to finally get this fixed was to record a veteran
*  trying to use the service and show the people in power how humiliating and
*  frustrating the experience was for veterans.
*  But until they were able to bring this veteran named Dominic's experience to life
*  inside the building at the Department of Veterans Affairs, they were literally told
*  there was no work to be done because the requirements in the contract had all been
*  fulfilled and all the boxes had been checked.
*  So you've got to sometimes make the crisis visible when it just won't be because the
*  people who it affects don't have a voice.
*  One thing that comes out of the veterans administration story you tell is the way
*  that what a crisis is to the people using government services and what a crisis is to
*  the people making them can be very different.
*  And I'd say throughout the book, you're very sympathetic even to people you're at
*  cross purposes with.
*  You're trying to get something done and they're kind of standing in your way and you
*  tend to see where they're coming from.
*  But in this particular story, in the veteran story, you talk about somebody you call
*  Kevin and so the attitude that he and his team have developed towards development,
*  towards keeping themselves out of hot water.
*  Tell me about Kevin.
*  Kevin was also at the Department of Veterans Affairs, but this is actually a separate
*  interaction.
*  I had started working with a small team to understand problems with the veterans
*  benefit management system, which is sort of the internal way that you would process
*  people's requests for benefits.
*  We had been told that there was terrible latency in the system.
*  Essentially, you can click on a link to start processing something and you'd wait for a
*  really long time before the page would load.
*  It's very frustrating.
*  We met with the guy the first day and he said, I'm so glad the White House decided to send
*  people to verify that everything is OK because latency has been solved.
*  Now we found out later he solved latency by defining it as over two minutes.
*  So if you clicked and had to wait two minutes or one minute and 59 seconds for that page
*  to load, you were not to report it as latency.
*  So that was the solution.
*  That was my first clue that this man I called Kevin was more interested in how things
*  looked than how they actually operated.
*  But as I asked him questions about this system, why had they decided to do X instead of
*  Y? What role did the claims processors have in this particular part of it?
*  He kept saying, that's not my call.
*  I don't know that.
*  And I asked him why.
*  And he said, look, I've spent my entire career training my people not to have an
*  opinion on the business requirements.
*  If they ask us to build a concrete boat, we'll build a concrete boat.
*  And I said, good Lord, why?
*  And he said, because that way it's not our fault.
*  And honestly, that moment for me, I was seven months into working in government then.
*  I worked at Code for America before I worked with government.
*  I was not new to the sort of dysfunctions of government and I shouldn't have been
*  shocked. But I really did take it as a gut punch.
*  I didn't blame him in a certain sense because I knew what he meant about the way we
*  structure responsibility in government.
*  But at the time, I think 18 veterans a day were committing suicide.
*  Many of them were still waiting for their benefits.
*  And it just seemed like such a callous thing to say when if he would push back a
*  little and say this concrete boat is never going to float, we could have gotten
*  more veterans their benefits.
*  When I finished the book, I had this note to myself that this book is about
*  personnel, capacity and autonomy, that it's about who works in government, what
*  kinds of things government does versus doesn't do.
*  And then the autonomy, the agency, the power we give these people to do the jobs
*  we ask them to do.
*  That's your TED talk.
*  There you go. My TED talk is summary of Jen Paulka's book.
*  But one thing that I have always worried about being close to a lot of people who
*  work in agencies and I think that you see in that story is when you make it really
*  hard and annoying to work in government, it's not that it pays a little.
*  You have a good section on this.
*  It's not the government pays so little, but it is often very frustrating work.
*  You have to deal with all these weird procedures and the lawyers tell you you can't
*  do it. I mean, working on code in
*  government and this is true in a lot of your stories, including the stories of
*  your heroes, often requires an almost superhuman level of persistence.
*  You're trying to get around a lot of very annoying things.
*  And sometimes you get a hero out of that.
*  But it also over time drives out a lot of good people who just don't want their
*  days to be annoying.
*  And it also selects for people who can make the internal compromise in that story
*  Kevin made, where you sort of shut off the part of you that says that doesn't make
*  sense and I'm going to argue you lose enough fights like that.
*  The lawyers tell you no enough times you get yelled at by your superiors enough
*  times and either you leave or you say, I'm going to stop fighting.
*  And that's where things can go.
*  I think really badly that it's not just that we need good people to work in
*  government. You hear that all the time, but we need government to be a good place
*  for people to work.
*  And for a lot of creative and patient people, particularly those at mid levels,
*  not those who are, you know, pointed to run an agency or run an office in the
*  White House or something.
*  It gets very frustrating.
*  I've seen a lot of really good people go in and particularly when they're in older
*  agencies that already know how they do things, I've watched them go right back out.
*  And I don't think they weren't committed.
*  I just think people it's hard to have a really irritating job.
*  I really think that we're so focused on getting these outcomes from a policy sense.
*  And to solve the problem you're talking about, we've got to really focus on just
*  basically the overall health of the civil service.
*  Yes, it's frustrating to fight these battles.
*  I think there's increasingly, certainly in my experience, like a community of people
*  who support each other around it that really makes it tolerable.
*  When people stay, it's because they've got someone's shoulder to cry on when they
*  need it and people to tell them keep going.
*  I have found that incredibly valuable and incredibly meaningful to me to be part of
*  that. But like, for instance, one challenge they face is they also really can't hire
*  other people quickly.
*  And there's a lot that we...
*  Or fire people.
*  Or fire people.
*  We could do so much.
*  And by we, I mean more our elected leaders and how we hold them accountable to making
*  that environment less destructive, less wearing you down and giving public servants
*  like those so high profile who are just persistent and heroic the tools they need to
*  succeed. But we just don't think of the tools of legislators or the legislative branch
*  as being good at that, right?
*  They have money, they have rules and they have oversight.
*  And those things aren't working very well.
*  But if they targeted them at sort of the health of the civil service and really focused
*  on it, I actually think we could make that a place that doesn't drive people away as
*  much.
*  Well, tell me what that would look like.
*  So, for example, there are bottlenecks in the system that are just sort of vestigial.
*  Like OPM requires that there be industrial organizational psychologists that approve
*  a bunch of things the same way that we have OIRA as a bottleneck to getting user research
*  out the door.
*  Remove it.
*  But nobody's on that.
*  Nobody's looking at these little things like that, that one by one could actually speed
*  hiring and make it easier for people.
*  But there's probably 7000 little things like that.
*  And one of my complaints since you started on the left, right, is that the right actually
*  has a lot of plans around this that are focused on firing people.
*  The left really doesn't pay much attention to this.
*  They're not obsessed with the details of making the civil service have greater autonomy
*  and freedom and hiring the right people.
*  And yes, probably firing the right people actually want the right and the left to say
*  this is actually more important than this, that or the other policy outcome that we're
*  trying to get because it'll enable all of those policy outcomes.
*  But it's real work that like somebody has to fund and somebody has to do.
*  I know probably half a dozen things that would go in that.
*  But somebody has to go find the other 36.
*  My impression of this area of politics is that it's become as many things do very
*  dysfunctional through a kind of crude polarization, which is to say that civil
*  service reform, by which I mean making it easier to hire and fire, giving the civil
*  service more autonomy, but also making sure there's more accountability, including
*  accountability from the political system itself, because that is often parts of that
*  have often been a feature of the right wing attacks.
*  And often they are attacks that also want to outsource a lot of functions of the civil
*  service and starved of money and so on.
*  They've been coded as right.
*  So the way to defend and show you care about government is to protect it from these
*  attacks.
*  But if you then cover government or you actually know people who work in it.
*  Even people in the civil service don't like how this works.
*  I mean, the difficulty of listing a job to get anyone in.
*  We're so worried about patronage.
*  We're so worried about corruption.
*  They've made the whole thing work really poorly and we drive people out because they
*  just cannot stand it over time.
*  And many of the people can rather asking against superhuman work out of them or
*  we're accepting people who maybe are not the people we wish were in charge of some of
*  these things. And that's not to take away from a lot of people doing hard work.
*  But it's also a kind of fallacy if you've ever worked in any kind of organization to
*  suggest that everybody in an organization is the right person, the right place.
*  I think the left has a lot of trouble with this kind of statement, but it is important
*  to be able to fire the right people to make organizations work.
*  It's not pleasant.
*  It's not what anybody should want to do.
*  But to not be able to do it is a way to guarantee organizational dysfunction.
*  I agree with that. I think the order of operations, though, should be first.
*  We make it easier to hire.
*  Yes. No, totally.
*  I think the reason this all gets stopped on the left is they're so afraid of the
*  firing conversation. That's why I bring this up.
*  They are. And there's some good reasons for that.
*  Right. So if schedule F comes back in second Trump administration, so with
*  schedule F, the schedule F was something that Trump instituted, I think in the last
*  couple of weeks of his presidency that would allow him to arbitrarily reassign
*  someone from a civil service position into a political position.
*  What's the difference? Obviously, you can fire a political position, a political
*  appointee with very little paperwork.
*  It's just it's quite easy, whereas civil service person, you're supposed to not be
*  able to fire unless there's you go through jump through a whole lot of hoops.
*  I guess what I would say first is both people on the left and the right who work
*  in government and of course, civil servants are meant to be nonpolitical, are
*  frustrated with the same thing.
*  And I think that polarization is really sad because we're actually responding to
*  the same frustration of this sort of demo sclerosis, things moving too slowly.
*  But on a very practical basis, like people I see working in government are now
*  trying to solve problems.
*  Yes, they have these obstructionists around them saying, sorry, this is how it's
*  always been done. The ESP has to stay in the software.
*  We're going to build a concrete boat.
*  But the first way to combat that is to get other people in to balance them out.
*  There's a concept always in government and much theory about government, which is
*  you're trying to balance between agility and stability and bringing in more people
*  with an agility mindset is a good way to balance that.
*  Whereas just firing everybody is a great way to potentially in another Trump
*  administration enable authoritarianism.
*  So there's a reason they're upset about it.
*  But I think that if the left doesn't start acknowledging that we have the same
*  frustrations with the civil service and the administrative state as the right,
*  we're never going to get anywhere.
*  And I actually spend a lot of my time with people on the right with whom I agree a
*  lot more than I thought I would.
*  I want to disentangle some thoughts here, at least for me, which is one, I think
*  people go too quickly to the idea that if you created a lot more autonomy and
*  flexibility within the civil service, made it easier to hire, easier to fire.
*  That has to mean it's easier for the political system to hire and fire, which I
*  do think is something we should be at least a bit careful with.
*  Yeah.
*  Whereas I'm talking really about the ability of the civil service to hire and fire
*  internally unto itself, which is a different question already because they're
*  just different rules.
*  That's why in schedule F Trump is trying to move people from civil to political,
*  but you could change the rules for what the civil servants can do internally and
*  still keep, you know, I think maybe you do want less wall than you currently have,
*  but a pretty good wall between politics and the civil service.
*  And then the other thing is I really am skeptical that the right and the left have
*  the same concerns here.
*  And there are places where procedures might converge.
*  There are places where some of the frustrations might converge.
*  I, for instance, see this a lot in a lot of the work I'm doing around permitting
*  reform and kind of supply side issues that often something that is important to
*  me now is deregulating the government.
*  And we're not supposed to call it deregulating.
*  I know, but that is what it is.
*  But that is what it is.
*  I want the government to deregulate itself oftentimes.
*  And deregulation is coded as a thing you do to make the government less powerful
*  on the right.
*  But oftentimes I think regulation is one reason the government is not able to
*  achieve its ends.
*  And so it kind of sounds to some people like I am saying the same thing that the
*  right is saying, but I'm not, I actually want a more active and capable government.
*  And there are things you might want to do from a deregulatory standpoint that
*  would get you there.
*  There are other things you would want to do from a deregulatory standpoint that
*  would not.
*  So many people on the right do not want the EPA to be able to regulate carbon.
*  That is a kind of deregulatory decision, but it isn't the one I would make.
*  I would like it to be easier when the government wants to build clean energy
*  for them to get the permits done.
*  That is a deregulatory decision that makes the government stronger.
*  So I just think that's also true sometimes within the civil service debates that I
*  would like to see a more capable, stronger, I'd like to see more people employed in
*  many cases by the government.
*  We've outsourced a lot of functions, which is not oftentimes what the right means
*  when they say they want to do civil service reform.
*  They often don't mean they want to bring a lot of these functions back into
*  government purview.
*  Let me say three quick things to that because it's a really important point and
*  it does get gnarly.
*  One is yes, but I also think change happens when people with different views do
*  have something in common, even if they're going to use it for different ends.
*  Right.
*  And I think we probably have some fertile soil in there to get change done, even if
*  people on the right want to do it, want that change for a different reason.
*  Obviously we need to be careful about that.
*  I agree.
*  We should definitely be regulating pollution.
*  Oh, it's sort of the last thing I was going to say on that, which is that there's
*  the right and there's Trump.
*  Yes, exactly.
*  And there are people on the right you really can have this conversation with.
*  It's just not Trump.
*  So that was my third point.
*  But my second point was it isn't regulation or not regulation.
*  It's how we do it.
*  And when we talk about competencies and capacities in government, I think one of
*  the main points I'm trying to make is that has to be a core competency in
*  government and we don't even recognize it.
*  I really take the big point of the book as saying there is politics, there's
*  policy and there's delivery.
*  And right now delivery is so subordinate to the people who run politics and the
*  people who run policy.
*  Then in addition to delivery being done poorly, the people delivering often don't
*  think they have any power.
*  They don't have power to interpret the language that they're given.
*  They don't have power to say no to the lawyers.
*  There's nobody empowered over a process to be flexible as it is ongoing.
*  They often don't have the power to change contracts quickly.
*  And that shift of power from policy or politics to delivery, that feels to me
*  like the great revolution you're trying to kick off here.
*  And I'm curious if you had two or three places you could start kicking it off,
*  right, aside from everybody reading your book and they should read your book.
*  What would you do?
*  Because yeah, culture can be policy, but policy can also create culture.
*  I think there's a lot of things that can happen that fall under the banner of
*  where we pay attention and where our elected leaders pay attention.
*  So one really practical thing, and I have an example of it at the end of the book,
*  is that when we're writing law and policy, who's at the table?
*  And I take very much your point about everything bagel liberalism, where you
*  already have too many people at the table, and that sounds like just adding someone
*  else on, but if we want to make law and policy that are implementable, then we
*  have to have implementers at the table when that law and policy is being written.
*  And those people are likely to be, and hopefully are much closer to the users
*  of the system, and they're going to provide insights that make your policy better.
*  But they're also going to start to shift that power balance that you talked about.
*  So like an example I talk about at the book is clearing of criminal records,
*  where the way a particular law was written made it kind of impossible to
*  implement at scale.
*  But in the aftermath of that, you've got people with technology skills who spend
*  time with the people who have these convictions and understand the constraints
*  in their lives and how they're going to interact with it.
*  At the table when decriminalization laws are being written, those decriminalization
*  laws are usually the ones that contain records expungement provisions.
*  That's a huge difference.
*  People can barely believe that this is happening, that you've got coders and
*  designers and user researchers at the table.
*  This is at the state level when laws are being written.
*  So that's one thing.
*  There's a saying, what we pay attention to grows.
*  So our elected leaders have this oversight responsibility as part of their toolkit.
*  And we also have the whole apparatus of oversight in the executive branch,
*  offices of inspectors general, the government accountability office, GAO.
*  And what do they focus on?
*  Failures.
*  What if they lifted up the public servants who were having success by
*  empowering themselves to have that flexibility and made half of their work or
*  more shining a light on them and saying, this is what we want public servants to
*  be like, and we're going to reward them.
*  I think it would make a huge change in the culture.
*  And I do have several sort of policy prescriptions in the book about things
*  like how money is allocated, I think are important to pursue, but in the end, I
*  keep coming back to those policies fail if the culture doesn't change.
*  So the ways we pay attention, what we talk about, who we elevate, I think those
*  are all kind of reasonable levers and good places to start.
*  So I think that's a good place to end too.
*  So what are three books that have influenced you that you would
*  recommend to the audience?
*  The first is a book from 1973 with the longest subtitle I have ever seen.
*  It is called Implementation, How Great Expectations in Washington are
*  Dashed in Oakland, or Why It's Amazing That Federal Programs Work At All.
*  This being a saga of the economic development administration as told to two
*  sympathetic observers who seek to build morals on a foundation of ruined hopes.
*  What do you think of that?
*  I love that because that's exactly how pamphlets in early American history and
*  kind of like 17th and 18th century Europe sound.
*  And I love those title formats.
*  Well, you're going to love this book.
*  It covers a project that started in, I think, 1967 where politicians and
*  bureaucrats went and made like a big announcement about investment that was
*  going to happen in Oakland, which is my hometown and somewhere I think you have
*  lived, and everybody celebrated and then goes into excruciating detail in the same
*  way I think some of my book goes into excruciating detail about why several
*  years later, essentially nothing had happened.
*  And they really conclude that this separation between policy and
*  implementation is the only reasonable explanation for the failure.
*  And they pull up all the other obvious reasons you would think that it failed
*  and really debunk them.
*  And it's just, it was sort of like they were reading my mail back in 1973.
*  So I really loved that.
*  The next one is Radical Help by Hilary Cottam, who is a Brit looking at the
*  social safety net, the workforce training system, the healthcare system.
*  And she takes that concept I have in the book of user needs over government needs
*  and just pushes them so much further in a way that is really inspiring.
*  And I think very critical of all of these government systems that we have today.
*  I mean, it's in Britain, but it's very similar to the US.
*  And I just think she moves the overton window about what it would mean to truly
*  meet user needs in government funded systems.
*  And I hope everybody who works in social services and healthcare would read it.
*  The last one is a bit controversial and it's not one I'm recommending in its
*  content, but I do think people of all political stripes should read.
*  Retreats are not endorsements here.
*  Exactly.
*  Definitely not an endorsement, but chapter three of this new report called
*  Mandate for Leadership, the Conservative Promise is essentially the blueprint for
*  what the Heritage Foundation thinks the next Republican president should do in
*  all areas, but chapter three covers civil service rules.
*  It's kind of hidden in there, but it does say that they would bring back schedule
*  F, which we can debate, but I think is a bad idea, but it's ultimately the way I
*  want to call attention to, they are paying a lot of attention to how to reform the
*  civil service and I would like there to be counter proposals on the table since
*  theirs is so thorough and detailed.
*  Jen Pauka, your book is called Recoding America.
*  I really, really recommend it strongly to people.
*  They really should read it.
*  We did not cover a lot that is important in it.
*  Thank you very much.
*  Thank you, Reza.
*  This was great.
*  This episode was produced by Emma Falgau, fact-checking by Michelle Harris and Kate
*  Sinclair, mixing by Jeff Geld.
*  The show's production team is Annie Galvin, Jeff Geld, Roche Karma, and Kristin Lin.
*  Original music by Isaac Jones, audience strategy by Shannon Basta, the executive
*  producer of New York Times Opinion Audio is Annie Rose Strasser, and special
*  thanks to Sonja Herrero and Kristina Samuelski.
