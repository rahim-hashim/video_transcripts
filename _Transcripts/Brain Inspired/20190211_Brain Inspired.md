---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4805s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 6121
Video Rating: None
---

# BI 027 Ioana Marinescu & Konrad Kording: Causality in Quasi-Experiments
**Brain Inspired:** [February 11, 2019](https://www.youtube.com/watch?v=6lnKzPmqI4M)
*  Basically, I've been having dinner with causality every day of my life for the last 15 years
*  or so.
*  If it's not an experiment or it was an experiment, I don't even want to hear about it.
*  And you've been brainwashing me.
*  A little bit.
*  This is Brain Inspired.
*  Hello, friends.
*  This is Paul Middlebrooks.
*  Welcome to the show.
*  You just heard the fiery married couple, economist Iwona Marinescu and old friend of the show,
*  neuroscientist Conrad Kurding.
*  And they just published a paper with Patrick Lawler in Nature Human Behavior about ways
*  to infer causality in quasi-experiments.
*  So quasi-experiments are experiments in which subjects or conditions aren't randomly assigned
*  to groups, but we discuss this deeper in the show.
*  Iwona and Conrad are both professors at the University of Pennsylvania.
*  Iwona is an economist, and to get a flavor from where she's coming from, we chat about
*  two of her interests, universal basic income and monopsony.
*  This was my first exposure to the word and concept of monopsony.
*  The definition of which is a market situation in which there is only one buyer.
*  So thanks, Iwona, for expanding my horizons.
*  And Conrad, you may remember, is a neuroscientist.
*  He has done a lot of work in computational neuroscience, but recently has become really
*  interested in causality, hence this paper.
*  So we talk about causality in general and how economists have this quasi-experiment
*  process all figured out and have for quite some time.
*  And the fundamental problem of constructing a counterfactual in determining causality,
*  a counterfactual is something that would have happened under different circumstances.
*  We talk about the value of correlational studies and how they can complement causal studies.
*  We briefly cover two of the three methods described in their paper to determine causality
*  in these quasi-experiments.
*  And here's a little preview of one of those methods called the difference in differences.
*  So differences in differences comes from the following idea.
*  And a difference in differences.
*  Differences in differences.
*  The gap or difference.
*  Difference in differences.
*  The idea of different differences.
*  The difference.
*  A difference in differences.
*  This difference would stay constant.
*  Differences in differences.
*  Differences in differences.
*  So the difference between the two change.
*  That's one difference.
*  All right.
*  Got it?
*  So plenty of causality talk today.
*  And later I asked them both about the right balance between collaborating and exploring
*  other fields versus focusing deeply in one's own topic and field.
*  And they have insightful responses, as you'll hear.
*  They give advice on how to do Twitter.
*  Here's one tip.
*  Don't respond to the trolls.
*  And of course we talk about a lot more.
*  To learn more or connect with Ioana or Conrad on Twitter, you'll hear they have this Twitter
*  battle going on.
*  You can find Ioana at M-Ioana.
*  That is M-I-O-A-N-A.
*  And Conrad is at Kurding Lab.
*  That is K-O-R-D-I-N-G Lab.
*  Kurding, spelled with an O.
*  Or you can find those links and more in the show notes, braininspired.co slash podcast
*  slash 27.
*  If you're so inclined, you can support me on Patreon, like Zach, John, and Minsuk did
*  this past week.
*  Thank you, guys.
*  I am now up to about $2 per day so far, which sounds small, but it's awesome nonetheless.
*  You can find out how to do that on the website, braininspired.co.
*  Now, I forced these two lovebirds, Ioana and Conrad, to play the newlywed game toward the
*  end of the show.
*  And it's tough, because as you may know, I'm highly trained in marital counseling.
*  But these two, I mean, well, you'll see.
*  Ioana Marinescu and Conrad Kurding here with me today.
*  Welcome, guys.
*  And you're sitting right next to each other.
*  So welcome to the show.
*  Yay!
*  Hello, everyone.
*  Great to see you.
*  Good to see you again, Conrad.
*  So you've been on before.
*  You are a professor at UPenn.
*  And from the last time I spoke with you, some people do listen to the podcast.
*  I had an old friend who was in the administrative department at Northwestern, and she said,
*  oh, man, because she enjoyed the episode.
*  And she said, I was really sad to see Conrad go.
*  And she said, but I feel really happy for him, because I think that we didn't have
*  what it took here for his collaborative style.
*  So I'm glad that he's getting that at UPenn.
*  So anyway, she's happy for you.
*  So I can kind of reintroduce you.
*  Your research has gone from computational neuroscience through some degrees of change.
*  Now you're doing more of an engineering and data science approach.
*  And really, now you're interested in this question of causality in modern experiments
*  without randomized controls.
*  And Ioana, you're an assistant professor of economics at the University of Pennsylvania
*  as well.
*  And you're also a faculty research fellow at the National Bureau of Economic Research.
*  And you specialize in things like universal basic income, monopsony, which is the first
*  time I had heard of that word.
*  She gives two thumbs up.
*  Unemployment insurance, employment contracts, and on and on.
*  So this is a first for me that I have two guests on the show.
*  And this is a different kind of show.
*  So actually, you guys heard of my reputation.
*  And I understand that you sought me out for some marriage counseling.
*  Will we still be allowed to continue collaborating after you're through with it?
*  We'll see.
*  We'll see.
*  So I understand, Ioana, you don't think Conrad is good enough with money.
*  And Conrad, you don't think that Ioana collaborates enough.
*  And so we're going to get to the heart of these issues here today.
*  How long you guys been married?
*  15 years?
*  Almost.
*  That's twice as long as me.
*  So maybe if we get time for it later, we might do something fun.
*  Have you heard of the newlywed game?
*  No.
*  Yeah, it's an old program, I guess, from the United States.
*  We aren't exactly newlywed anymore.
*  So we may play the newlywed game to rekindle those spirits perhaps later.
*  Let's go for it later.
*  For now, we'll just ask one real marriage question here.
*  So Ioana, what is one special talent that Conrad has that most people might not know
*  about?
*  He's an excellent cook.
*  Oh, okay.
*  Very good.
*  Okay, Conrad, question goes to you now.
*  What's one special talent that Ioana has?
*  Ioana is an outstanding spousal dancer.
*  Oh, wow.
*  The hips.
*  Okay, good.
*  Maybe I can get a demonstration of both of those sometime.
*  So you've been married for 15 years.
*  That means you suffered from the two-body problem in academia.
*  Have you struggled with that?
*  Has that been easy?
*  Because I personally know some people that it's been a struggle for.
*  It's difficult.
*  I think it's extremely difficult and we've been extremely lucky.
*  So for example, in our first job search when we were both looking for our first faculty
*  jobs, literally Conrad had one job offer.
*  The only job offer he had was in the same city that I was in and it was independent.
*  There was no direct connection.
*  So what's the probability?
*  It's just something that shows you how hard it is because it's really not a given that
*  this would happen.
*  So I think it's extremely difficult.
*  But I will say once we were looking again more recently, it's been easier.
*  Still not easy, but once you're more established, you're a known quantity that departments have
*  some knowledge of and they're well aware of two-body problems and more willing to work
*  with you.
*  I feel as once you're established your career and your contribution to the field, it's
*  a little easier.
*  Still not easy.
*  We have some friends who have been living apart, have a kid and living apart for years
*  in two excellent universities very far away from each other.
*  So we've been very lucky.
*  That was my example too.
*  I know a couple and they have a child and they have multiple children and she had an
*  accident where her lower half was paralyzed and she was having to learn how to re-walk
*  and they were in separate cities.
*  So it's just a big mess.
*  What would you not sacrifice for the beauty of academia and science?
*  Back to the marriage counseling, I see.
*  Well, but the amazing thing is these people, these friends of ours, certainly make it work
*  really amazingly.
*  And I've got a lot of similar situations.
*  There are a lot of people who make it work, but for me being with you on this is very
*  important.
*  We just have to say gratitude to the universe.
*  Oh yeah, I bet there is a lot of gratitude when it works out like that.
*  Cool.
*  Well, so we're going to talk about causality in your newest paper, but we've never talked
*  about economic issues on the podcast.
*  Not that the podcast is about economic issues, but just to give people a sense of where you're
*  coming from, can we just talk for a moment about universal basic income and maybe monopsony?
*  So universal basic income, should we all just move to Alaska or what?
*  So I think for the audience here, you might have heard about AI and how potentially this
*  will make all jobs disappear.
*  I think this is highly uncertain and this is something that you can debate because we've
*  had a lot of other technological changes in the past that have ultimately led to more
*  work arguably for people and a higher standard of living.
*  So is this time different?
*  Who knows?
*  We are not experts at predicting big things like that, but it's certainly a risk, I would
*  argue.
*  So basically, in the face of that, someone like me who studies labor markets and also
*  systems of social insurance, the big question is how do we insure ourselves against some
*  bad outcomes that could happen?
*  And so basic income is one of the proposals that's been floating around in thinking about
*  what we might do if indeed jobs were becoming increasingly hard to find, at least for some
*  people.
*  And especially in this country, a lot of the benefits that you get are dependent on your
*  having a job.
*  So if you don't have a job, you might be disqualified from any benefits.
*  So what if it was really for no fault of your own, you couldn't get a job?
*  So that's why I became interested in looking at this basic income and the cost.
*  Economists, I'm interested in, okay, we're maybe using that to fix the labor market,
*  but some people say it could do harm because if you give people money for nothing, maybe
*  they won't be working.
*  Right.
*  Yeah, they can become lazy.
*  Exactly.
*  Do they become lazy?
*  Well, not really.
*  That's what we find by looking at Alaska that has had something similar to basic income
*  since 1982.
*  And this is where actually we're using a quasi-experimental method.
*  We haven't actually discussed this one explicitly in our paper, but it's one of those classes
*  of quasi-experimental methods that's kind of similar to what we do discuss, which is
*  difference in differences, sort of.
*  So anyway, we find that Alaska basically has an employment level that is similar to
*  other states that can plausibly be controlled and that didn't have this policy.
*  So therefore, in terms of the impact of a basic income style policy where every Alaskan
*  receives this payment every year, no strings attached, doesn't have an impact on the share
*  of Alaskans that work.
*  That's a big finding from my recent work about UBI and understanding what it could do to
*  the labor market, some of the unintended consequences, which in this particular case doesn't really
*  materialize.
*  Right.
*  And I understand that it's supported by both main political parties in the United States,
*  or at least in principle.
*  Right.
*  I mean, there's some support from both conservatives and progressives for slightly different reasons
*  in the sense that on the progressive side, it's obviously the idea of income security
*  is very important to progressives.
*  And the more conservative side, there's also, I think for everyone's idea of insurance,
*  it's quite important to give people some last resort level of income security.
*  On the conservative side, the basic income is especially attractive because of its simplicity
*  and its freedom enhancing qualities in the sense that it has no conditions.
*  So you don't need to be tracked.
*  You don't need to be checked.
*  We don't need to look at your income, your family situation, your health status.
*  You get it no matter what.
*  And that in a sense is very freedom friendly.
*  It's like you don't need to do anything.
*  You just get it and then you do anything you want with it.
*  So for the more pro-market libertarians, this is a very appealing proposition from that
*  perspective that it really very much fosters individual freedom.
*  It seems like I've heard more and more about universal basic income recently.
*  And what is your gut feeling on the trajectory of the possibility of this becoming a national
*  policy ever?
*  I know you think that it is better at the state level, right?
*  Right.
*  I think it's something that is sort of percolating through and obviously as often smaller is
*  more realistic.
*  So I think what can happen is that we get a basic income through the so-called carbon
*  tax and dividend.
*  So the idea is we're going to tax carbon, which is something that every economist of
*  no matter their party would strongly agree on.
*  And then we take the revenue and we return it back to everyone as a sum of cash, no strings
*  attached.
*  So it's very much like a basic income.
*  The amounts that we're talking about in plans that are currently on the table are not very
*  large.
*  But it's free cash for everyone.
*  And this is a plan that's been supported by both conservatives and progressives and basically
*  many of the former Fed Reserve Chairs, including Ben Bernanke and Janet Yellen have been signing
*  on to support this plan again, the carbon tax and dividend whereby we tax carbon and
*  we give the money back to the people in cash, no strings attached.
*  Including me.
*  Yeah, right.
*  And you.
*  Yeah, for our drug habits, right?
*  Anyone.
*  You know, there's no conditions.
*  And so that this is a way that it could happen on a small scale in terms of the amount.
*  But then we can take it from that.
*  I'm very much interested in gradualism because this is something that we can take it small,
*  see what happens, measure the effects, and then we can talk about whether we want to
*  expand something like that.
*  And I think the urgency also of the environmental problem commands also that side that maybe
*  we want to expand the kinds of essentially taxes on environmental harms in order to discourage
*  this kind of behavior and thereby raise more money, which we can also return back to the
*  people.
*  So there's some sort of double benefit on discouraging harmful behavior while providing
*  people with a source of income security.
*  Conrad, it looks like you're going to jump in there.
*  Are you going to say something?
*  You're going to ask your wife, she thinks that when we study the brain, we should also
*  start like very small and then only late build up a little bit.
*  Well, I mean, you know, who knows?
*  But certainly if you don't understand the small things, I guess it's like, how can you
*  I mean, obviously, this doesn't always apply.
*  Sometimes it's easier to understand the phenomenon at a more micro level.
*  And there can be a sort of no bridge.
*  It's hard to go from the micro.
*  The macro is just something I think Conrad has thought about in the context of the of
*  the brain.
*  And lots of listeners to Paul's podcast have heard about it.
*  Yes, right.
*  Yeah.
*  So I just want to put in a plug.
*  If you want to know more about basic income, check out my website.
*  I have a whole review of the literature that tells you all about it and all the different
*  tests that have happened that offer policies similar to basic income and all of their effects.
*  So for the interested listeners and direct them there.
*  Well, it'll definitely be a link in the show notes.
*  But just to say it here, is it marinescu.eu?
*  Right.
*  Exactly.
*  Exactly.
*  And follow me on Twitter.
*  Oh, yeah.
*  Well, yeah, yeah.
*  It's a little frustrating for me.
*  I used to be the one with the many Twitter followers and you know, just overtook me.
*  That's what happens when you do relevant research.
*  Well, thanks for being on the show, guys.
*  It's been fun.
*  So you want to do you want to what is monopsony and why are you interested in it?
*  And then we can we can move on here.
*  Right.
*  So that's another area that I've been working on a lot recently.
*  The idea there is just in thinking about how wages come to be what they are.
*  So you know, you might think, oh, surely people get a fair pay and intuitively, basically,
*  if you contribute more to your bottom line of the employer, surely you should be getting
*  paid more, more or less as a proportion of how much you contribute.
*  And that's basically what basic economic theory tells us that if markets are perfectly
*  competitive and this is the rub, meaning that many employers compete for your services,
*  then you're going to end up paying what you're worth because basically if you're underpaid,
*  some other employer would come and fetch you and pay you more.
*  So eventually you'll be fairly compensated for what you bring to companies.
*  And so the idea of monopsony now is that actually employers can underpay workers
*  because workers don't have that many opportunities.
*  It is not easy to move.
*  There aren't that many other employers that you could be working for.
*  For example, so many in our audience might be in the academic career.
*  If you think about how specialized you are, the various geographical constraints that
*  you might have in terms of where you'd be willing to live, there aren't that many options.
*  And so what my recent work shows is that just looking at the whole US labor market,
*  if you look at the market that is more concentrated, meaning that there's just a few
*  employers that are currently recruiting in that market, this is a market that is going to
*  tend to have lower wages as compared to a time where this market would have many employers
*  operating in it.
*  So, for example, you might think about a small town if they just have a Walmart in town.
*  Wages might be lower, says the theory, than if they had an equally many jobs in retail,
*  but are maybe broken down between five or six smaller mom and pop stores.
*  So because again, what you have to think about is the same number of jobs,
*  but it matters how many employers control those jobs.
*  You could have many jobs, but if all of the jobs belong to Walmart, there's not really
*  competition for workers because ultimately all the jobs are controlled by Walmart.
*  So that's sort of the idea of monopsony.
*  And so we find again that an increase in concentration, meaning fewer employers are
*  active in the market, is associated with people getting paid less and plausibly
*  getting paid less than what they deserve.
*  And so this is very important right now because there are ways to address that
*  through antitrust enforcement.
*  So basically there are all sorts of things that we can do legally to protect workers
*  against behaviors by employers that worsen this problem, such as, for example,
*  mergers. So if two employers merge with each other,
*  now they have greater power over workers because they've just reduced the options
*  that workers have in terms of what employers they could be working for.
*  And that constitutes a basis for potentially blocking a merger.
*  And mergers, big mergers have to go through review by the federal antitrust
*  authorities, and now they have an opportunity to block some of these mergers if we can
*  foresee really negative impacts for workers who will see reduced competition
*  for their services and therefore lower wages and lower opportunities for career advancement.
*  So you're increasing freedom with UBI and decreasing business freedom with your
*  work on monopsony.
*  So it's an increasing workers freedom and competition in the market.
*  Cool. OK, good.
*  So that gives us a real flavor for what you do.
*  OK, at my own peril here, I'm going to I'm going to tell a joke.
*  It's the joke of the week.
*  And don't worry, it's not designed to make you laugh.
*  So some some of my
*  listeners for some reason seem to like this.
*  OK, and then we're going to talk causality.
*  All right. So there's this married U-Penn professors, these married U-Penn professors,
*  and they're they're planning their vacation to go ski with this podcast
*  host in Durango, Colorado.
*  And the woman says, huh, you know, I I really hope it's going to snow right
*  before we get there so that the skiing is really good.
*  And the man says, yeah, but, you know,
*  in chaos theory, it's impossible to predict the weather that far in advance.
*  And and then their robot pipes up and says, oh, no, I've got it.
*  Let's see. Looks like it will snow a lot right before you get there.
*  So, oh, isn't that wonderful?
*  Man says, wait, wait a second.
*  Astounded. He says, wait a second.
*  Are you telling me you've become so advanced
*  in your deep learning algorithms that you can predict the weather that far
*  in the future? And robot says, no, no, no, of course not.
*  Ever since I had that bad fall last spring,
*  I can just feel it in my four hundred and twelve and four hundred and thirteen
*  hidden layers.
*  You've been doing too many deep learning people.
*  Well, this is the state of AI, so I get to put a little drum drum kick in there.
*  So. All right.
*  Hot off the press,
*  quasi experimental causality in neuroscience and behavior research in nature,
*  human behavior.
*  This is work with Patrick Lawler as well.
*  You both co-authored the paper as well.
*  So how did this collaboration come about?
*  So you honor has been my wife, as you know, for about 15 years.
*  Not that collaboration.
*  Well, actually, it was kind of the same one.
*  So in economics, people really worry about causality and for good reasons.
*  When they at the time when they weren't worrying about causality,
*  they said a lot of stupid things.
*  And then one day they say they basically told themselves that they wanted to get
*  causality clean. What do you want an economist to do?
*  You want them to tell you what a policy would do?
*  Would it increase GDP if we lower taxes?
*  Well, maybe it would.
*  But there's a question, there are real questions in economics.
*  And there's a true there's a correct answer.
*  And the wrong answer about it.
*  What's good in economics is we can find out if we are right, which is we
*  well, we do the experiment.
*  So they realized for decades how important it is to obsess about causality.
*  And for decades, they basically reworked the things they did to ask causal
*  questions in a clean way and therefore economists like my wife
*  constantly talk and worry and think about causality.
*  So basically, I've been having dinner with causality
*  every day of my life for the last 15 years or so.
*  So in that sense, it's not very surprising that they get into causality.
*  And then once I started seeing the things
*  that the economists talk about in neuroscience, it was really eye opening.
*  And that's why it was great to get a real expert involved and write a paper about
*  what opportunities there are to learn about causality.
*  I will add one more twist to this, which is that for economists, it's often very
*  hard to do a randomized control trial because of the sorts of policies that we
*  deal with, like no one gives you enough money to decrease taxes just randomly.
*  So it's very rare and to have an actual
*  randomized control policy experiment, that's not how it goes.
*  So we had to try to get creative to find ways of making causal inference as if it
*  were a randomized experiment, but by using different methods.
*  And I think in some of the scientific domains, because RCTs are
*  pretty common and well accepted method, you go for that and you don't necessarily
*  think about, hey, there's these other options that you could be using.
*  And so today, also, I think with big data,
*  that also offers the opportunity of exploiting those new options, because
*  many of them will do much better if you use a lot of data, which now...
*  But you still need something like causal experiments.
*  Obviously. But my point is, it's kind of a complementary
*  process where the two together are more than the sum of the parts, so to speak.
*  So but causal experiments is
*  what the economists call an experiment, is if they're randomized, they give like
*  the one treatment to half of the people, the other treatment to the other half of
*  the people. Causal experiments, if you aren't doing that, but something is doing it.
*  Maybe Texas gives them like low taxes at some point of time and maybe the next
*  state gives a higher tax and then taxes changes the tax rate and then the Kansas
*  changes the tax rate.
*  And by looking at these things that aren't really random, but that have a certain
*  random component, they like figured out techniques to tease apart how things
*  causally work.
*  Well, that was going to be my question, is what is a quasi experiment that you just
*  defined? So just to be totally clear for people.
*  So let's just talk about causality in general for a few minutes, I suppose.
*  I've been learning a little bit about causality through your paper, but also
*  Judea Pearl's work.
*  He's been at this for a long time.
*  His I think his most recent book is the book of Why.
*  It's a beautiful book.
*  OK, well, we'll come back to that, too.
*  It's interesting because he, speaking of artificial intelligence,
*  he thinks that there are hurdles in AI that just won't be surpassed until we build
*  causality into the systems. And, OK, this is a silent thumbs up.
*  That doesn't work on an audio podcast.
*  But I can I can at least I can at least say that you're doing it.
*  So so but I did read online.
*  There's an available lecture that he gave in 1996 called The Art and Science of
*  Cause and Effect, and it's kind of just an interesting take on the history
*  of causality. And he starts with Adam and Eve in the Bible
*  and makes the point that causality is manmade in the sense that person made,
*  let's say, you want to.
*  So I don't want to offend anyone so that God asked Adam,
*  what happened when Adam ate the apple?
*  And Adam didn't just say I ate the apple.
*  He blamed Eve. So he added explanation, added some cause.
*  Right. And then Eve blamed the serpent.
*  And God never asked them for explanation, just what happened.
*  So so in that sense, like man created this causal notion.
*  And so man started on this causality path.
*  And later on, there were natural events
*  that were considered to have natural causes that God was doing everything,
*  for example, and people would even their lives would sometimes be in peril
*  at the throw of a die or the casting of straws, right.
*  The picking of straws, because God was causing the, let's say, a die to come up six.
*  And that meant the sixth person gets thrown off the ship.
*  Right. That's that's how they determine their cause.
*  And so it goes on and on in this long train of entertaining lecture.
*  And it's just a couple of things.
*  It's interesting that it's a problem that as humans we don't we only infer causation
*  because we only experience and observe correlations.
*  Right. You know, when you hit the cue ball into the other ball,
*  we can infer that the cue ball is making the other ball move.
*  But all we see is like every time we do
*  that statistically, the probability is super high that one will follow
*  from the other and it makes the point that the word cause is not even in
*  probability theory.
*  And I won't go on and on about this particular track, but I just kind of wanted
*  to lay causation on the table and maybe ask you guys, you know,
*  your thoughts about causation in general and and the problems therein.
*  So I think, you know, in econometrics, in policy evaluations,
*  we try to evaluate something like a policy.
*  This notion of counterfactual is really
*  fundamental, as we call the counterfactual is the thing that would have happened if
*  the cause wasn't operating.
*  So basically to say that something is causal is to
*  make some assumption about the counterfactual and then measure.
*  So we are measuring, we're asking, you know, you have an outcome, let's say,
*  you know, employment because I'm an economist and we want to ask,
*  what was the effect of this policy on employment?
*  So then what we're asking is, you know,
*  to phrase it more formally, the meaning of econometrics, we're asking,
*  OK, so this policy happened.
*  This is the level of employment we observed with the policy that has happened.
*  What would have happened if the policy weren't there?
*  That's the counterfactual.
*  And then we measure the effect of the policy as the difference between what has
*  happened and that we observe versus what the employment would be like
*  without the policy, aka the counterfactual.
*  Therefore, the big problem of causality is to find a way to fill in for that
*  counterfactual for the state of the world that we actually don't observe.
*  That's why it's called a counterfactual,
*  where the policy wouldn't have happened so that then we can compare employment
*  with the policy and without the policy.
*  So that's sort of the fundamental problem
*  of causal inference is how do you construct the counterfactual again,
*  like, you know, to measure the outcome in the state of the world where the policy
*  whose inference you're trying to measure didn't happen.
*  And to do so, taking into consideration all the potential confounds as well.
*  Exactly. So, you know, obviously the experimental method.
*  So maybe, Conrad, you can...
*  Yes, so let's talk about confounds first.
*  So one of the big problems, the big problem in causal inference is confounds.
*  Let's say we look at medicine.
*  We might find that there's a treatment.
*  And let's say we look at some outcome, maybe death.
*  It's possible that people who are treated die less often.
*  But that could have multiple reasons.
*  It could be that the treatment makes people die less often.
*  Or it might be that rich people get the
*  treatment and rich people happen to be dying less often.
*  All of a sudden, socioeconomic status is a confounder for everything.
*  And to immediately bring that to neuroscience, we have that confounder problem.
*  Let's say I recall from two neurons, I find that many times when one neuron fires
*  a little bit later, the other neuron fires.
*  Well, that could be because that one neuron makes that other neuron fire.
*  Or alternatively, it could be that there's some brain state.
*  And when that brain state happens,
*  well, then one neuron fires at some early time and then the other neuron fires
*  somewhat later within that. In the first case, there's like a real
*  connection between them. It's like really one neuron makes the other
*  neuron do something. In the other case,
*  there's absolutely no interaction between the neurons.
*  So just to piggyback on what you just said, to get back to my counterfactual
*  with these two neurons, if the case is that the one,
*  you say neuron A causes the reaction neuron B, then you should see that if
*  neuron A does not fire, then neuron B does not fire, at least statistically
*  on average, over a number of observations.
*  You can see a difference between those two.
*  Whereas if it's like a state of the brain,
*  actually what's driving the behavior of both neurons has to do with that particular
*  state of the brain and it's not really that the one is influencing the other in
*  a direct way. But it's this other hidden so-called omitted variable.
*  We call it an econometrics that is causing both of them to fire.
*  But it's not that neuron A has a causal impact on neuron B.
*  But the important thing is that that reality exists.
*  Now, like Paul, the way you formulated it in a way made it sound as if causality is
*  kind of something that you can have an opinion about.
*  Like at some level, there exists reality.
*  So if I make a neuron fire or if I make a neuron not fire, it will have an influence
*  on other neurons and at some level causality therefore is perfectly clean,
*  the fine counter-effects.
*  It is if I now would have stopped the neuron from firing,
*  what would have happened differently.
*  And when we randomize things, we can actually read that out.
*  Like if we could say optogenetically activate the neuron or inactivate the neuron,
*  we can actually measure the true causal effect, which exists.
*  Yeah. And has a one of the interesting things about causality is that it has a
*  direction, whereas in mathematical equations and all the physical equations,
*  they're all symmetric in that
*  they you can run them forwards and backwards and you get the same outcome.
*  But causality, like time, seems to have a direction like entropy.
*  Right. If you make the light go on, the light search will not flick over.
*  And I also want to say that some questions seem hard to answer because there might be
*  no data, but it doesn't necessarily mean that it's not an answerable question.
*  So, for example, in history, that's a typical example.
*  You might ask, is it the case that the Second World War was caused by
*  the greedy powers that imposed huge financial sanctions on Germany?
*  So you can say, like, is it the financial sanctions that caused the war?
*  Now, you can't really make this a scientific study because there's not enough data.
*  It's like you have only one observation.
*  Well, thank God.
*  Yes. But hypothetically, you could imagine many journeys,
*  and in some cases the reparations happen.
*  In some cases, the reparations didn't happen.
*  We forgive them and didn't give them a financial penalty.
*  And if, you know, with this many parallel
*  universes, the war would happen more often in the cases where reparations were asked
*  from Germany, then you'd conclude that reparations have a causal impact on the
*  Second World War, except that in this case, it's a case where practically speaking,
*  you can't really do it, but hypothetically, you could.
*  Yeah. Well, so we're in a position right now
*  where we could impose a counterfactual potentially, right, and remove the alt-right
*  and remove the current presidential regime and see what happens, right?
*  Exactly. Hypothetically.
*  So we can have created many USs and in all these parallel universes, see what happens
*  without the alt-right.
*  I know eventually everything ends up with Hitler on the internet.
*  I just want to bring us back to neuroscience.
*  So at some level, the important thing, almost all the questions,
*  all the re-questions that we have in neuroscience have a causal connotation.
*  Like if there's a disease, the question I want to ask is, what should I change?
*  What could I have changed so that the disease wouldn't have happened?
*  When it comes to understanding the whole
*  language, the way we think about the brain is how does a part of the brain, maybe a
*  brain region, make something happen? How does it cause an effect?
*  I don't care that it's correlated to the effect.
*  I care that that brain region or the neuron or whatever, or the molecule is
*  involved in something, makes something happen.
*  So almost every real question that we have in neuroscience is of a causal nature.
*  But we have the old adage, correlation doesn't equal causation.
*  You hear that over and over and over in
*  neuroscience, and I don't know if you do in economics as well.
*  But we don't even need to say it anymore, though.
*  It's so absorbed.
*  It's so ingrained in economics that it's OK.
*  So Conrad, do you think that in neuroscience that it is still a kind of a problem,
*  a widespread problem?
*  You've got to be kidding.
*  It's a huge problem.
*  It's everywhere.
*  It's once you understand causality and the nature of causal infants, reading the
*  neuroscience literature is really, really difficult.
*  Every other paper claims causality without having a claim to that.
*  And there's like tricks that people use for that.
*  For example, when it comes to the analysis of networks in the brain,
*  what you do is you say, have LFP recordings.
*  So FMRI recordings from some areas.
*  Then you put it to an algorithm.
*  It gives you a network and all of a sudden.
*  And there is this thing where we allow ourselves to call correlation causation,
*  for example, through the trick of so-called Granger causality,
*  where all of a sudden correlations become causality.
*  And you find that in so many subdomains of neuroscience, for example,
*  in tuning curve mapping, lots of people characterize how does a neuron respond
*  to the outside world? That is a purely causal connotation.
*  It's like, what is the causal effect of the stimulus on something happening in the
*  brain? But there's no causal connotation of what that part of the brain does in
*  computing or something that's unsupported.
*  But we use this like funny wording
*  called representation or something where all of a sudden our correlational
*  finding, which is perfectly fine and interesting, becomes a causal role that
*  because it's correlated to color, this must be an area that specializes in the
*  causal role of extracting colors from from images.
*  The last time you were on the program,
*  Conrad, we talked about your paper where you guys developed an algorithm to look
*  at, try to detect image fraud.
*  Now, I'm wondering if in a few months I'm
*  going to see a paper with an algorithm to detect false causality statements in
*  neuroscience papers.
*  It turns out that we're actually working on that.
*  Get out of town. Are you serious?
*  Yes. Oh, my gosh.
*  Absolutely. Awesome.
*  OK, so what I mean with that is that
*  the questions we want to ask in neuroscience are all causal.
*  So there are papers that are humble about it that say, here's a correlational
*  finding. I think this is what it could causally mean,
*  but I don't have evidence to claim that.
*  And then there are other papers that use
*  interesting linguistic constructs to basically allow them to go all in on the
*  causal interpretation and basically ignore the problems that are there.
*  There's this cool concept.
*  Have you ever read that there was this recent article it's called Hatch Shifts?
*  OK, this is great.
*  So when people write a paper, it usually needs to make certain assumptions.
*  Not like you're basically here's what I find.
*  Here's the set of assumptions under these assumptions.
*  This is what it means.
*  But if I then cite your paper that has all those hedges, I will no longer use that.
*  And so that the idea of Hatch Shifts is that because the hedges erode away,
*  a whole field can basically move away from the truth
*  by virtue of the hedges in the future no longer being relevant.
*  By assuming and referencing the same assumptions or hedges.
*  That's exactly by assuming that the hedges must have been true.
*  Interesting. I'll have to look that up.
*  Is it it's a single article?
*  I'll link to it if I can find it.
*  I'll find it for you.
*  Yeah. OK, great.
*  Well, in the paper, you guys describe three main techniques on how to go about
*  doing this, and I thought maybe just to keep things kind of broad,
*  one of you could just choose one of the techniques or both of you can can talk
*  about it, maybe your favorite example and just describe it in a broad sense
*  and maybe give an example of how it could be used.
*  Yeah, let me start with regression discontinuity, which is my favorite.
*  So let's say we have a process that has a fixed threshold in medicine.
*  That could be I call you high blood pressure.
*  If your blood pressure is above one thirty or something in neuroscience,
*  that could be does a neuron spike?
*  A neuron has a certain input drive.
*  If that is above some threshold at some point of time, it will spike.
*  Otherwise, it will not spike.
*  Now, if we compare the times when a neuron spikes and the times where a neuron doesn't
*  spike, everything is different, the network state is different,
*  the stimulus is different, the response will be different and so on and so forth.
*  So the comparison of spiking versus non spiking is pointless in the same way in
*  medicine. If I have people that have low blood pressure versus high blood pressure,
*  while the high blood pressure people will be older and heavier and you name it.
*  Now, the comparison is pointless.
*  But here's the thing.
*  If I take people that are very, very close to the threshold,
*  let's say one twenty nine versus one thirty one, as I make that interval smaller
*  and smaller, they must become identical.
*  And the reason why they must become identical is because there's noise on the
*  measurement of blood pressure, say in the same way as there will be noise on the
*  measurement of what the drive to a neuron is.
*  So the important thing is those two groups, as we approach the threshold from
*  both sides, the groups become identical.
*  But if we have a difference, where could a difference be coming from?
*  Well, if you're above the threshold,
*  you spike or if you're above the threshold, you get the treatment for high blood pressure.
*  So these two groups are identical by all
*  other means, apart from the fact that one of them gets so-called treated.
*  The other one doesn't.
*  Like in economists speak, spiking is getting treated.
*  And then you can say, well, what is the downstream effect of that?
*  I could look at what another neuron does or what a behavior does.
*  And because of that construction, it gets a very harmless assumption,
*  provably a correct estimator of the causal effect, not of the overall causal effect,
*  but what's called the local average treatment effect, which is how much does
*  the spiking matter when we are in the state where we are really close to the
*  threshold, if you use the neuroscience term?
*  Or for blood pressure, for those people who are really close to the high blood
*  pressure threshold, how much does it help those kinds of people to take the medicine
*  that lowers blood pressure? It's local.
*  We can conclude about people who have super high blood pressure because these are not
*  comparable, just comparing people who are very close to the threshold on each side.
*  And same thing with the spiking, basically, we can't universally say what
*  the causal effect of a neuron is in the extreme case, where it's blatantly obvious
*  that it spikes based on the network state.
*  Well, it will spike in any case, and therefore we can't disentangle that.
*  So we can't know that.
*  And regression discontinuity could be broadly used in neuroscience,
*  if you say intracellular reconics, or if you're in a situation where you have
*  a threshold phenomenon in some brain area, you could figure it out to figure out what
*  the brain area does. Whenever you have threshold processes,
*  you can use those ideas.
*  Yeah, this was my favorite in the paper as well.
*  Kind of the most intuitive to me, I think, as well.
*  Do we want to talk about other ones or?
*  I think we should talk about differences.
*  Differences are easier to come by.
*  Like, RDDs can be hard.
*  So differences and differences comes from the following idea.
*  Let's say there is a time that is, in a way, randomly chosen where
*  where a subgroup is treated.
*  Let's say in economics, that could be that there is
*  January 30th of 2014, some country changes, some county changes its policy.
*  The idea of different diff is then you take you construct two groups.
*  You construct a group that randomly get that shock, that change,
*  and a group that didn't get that change.
*  When it comes to neuroscience, that may say that might say we have a local
*  perturbation with optogenetics at some point of time.
*  That is random by all or like maybe a
*  perturbation induced by some other brain area, something like that.
*  We can then compare those two groups and we can look if that one group
*  has a different trend than another group.
*  And that allows us to infer causality again.
*  The important thing here is we derive it from basically this perturbation happening
*  for no reason that is in the population that we're looking at.
*  So another example from medicine, you could imagine, for example,
*  one hospital introduces a new treatment at a certain date.
*  The neighboring hospital hasn't done it yet.
*  And then we compare the outcomes of patients in the two hospitals.
*  So we look at them before and after the new treatment was introduced.
*  And what in a experiment in a different and different setup that works well,
*  the key assumption is that if it weren't for the treatment, the trends in the
*  outcomes, let's say mortality for our patients would be the same.
*  So it's OK if one hospital has higher mortality than the other.
*  That's OK with this method.
*  What we want to see is that over time, they always track each other exactly.
*  So the gap remains the same.
*  The gap or difference tends to be the same over time.
*  And then if the new treatment had an impact, then after the new treatment was
*  introduced, the hospital that implemented it, the mortality went down,
*  let's say, if it worked well.
*  So then the gap narrowed.
*  So that's why it's called difference in differences, because it's the difference
*  between the two hospitals, that's one difference, compared after the treatment
*  versus before the treatment.
*  And I think a difference in differences
*  method is something that can apply decently in many cases.
*  So you're looking for a control group that is plausibly similar enough.
*  It doesn't have to be the same, but just similar enough.
*  But most importantly, it follows the same trends.
*  And the reason why it's useful that it's similar is that it's just that more
*  plausible that the trends are the same.
*  But really what we need is that the trends are the same.
*  In the absence of the policy, whatever gap in outcome there is between, say,
*  the two hospitals, in my example, I was saying earlier, it stays constant.
*  Maybe both mortality goes up or both go down, but the gap has to remain constant.
*  And again, if the characteristics of the two groups are very similar,
*  it's more likely plausibly that this difference would stay constant,
*  but for the treatment.
*  And that's where we get again to the counterfactual.
*  Now, what would have happened if it were in the treatment, the bodies in difference
*  in differences without the treatment, you want the difference between the control
*  and treatment group to stay constant over time.
*  And so that's sort of how you can make
*  conclusions that if something changed, so the difference between to change,
*  that's plausibly due to the new treatment that was introduced at the one hospital,
*  but not the other.
*  And I think this method is applicable in many cases, because if you're a bit clever,
*  you can come up in many, not all, with some plausible control
*  group for your group of interest.
*  OK, great.
*  So those are two of the differences and differences
*  with what you were just describing.
*  And then before that was regression discontinuity design.
*  And there is one other main one in the paper.
*  I'm going to let's leave it at that and I'll point to the paper so people can
*  learn more. And I should say there are nice diagrams in the figures in the paper
*  so that to illustrate this clearly for people and with causal graphs included as well.
*  So it's it's a well-written, of course, clearly written paper.
*  So these techniques and there are others, too.
*  The three main ones in the paper.
*  And I know that there are others available.
*  They can be used in a variety of situations.
*  Are there speaking of counterfactuals, I suppose.
*  Can you do you imagine situations in which they
*  techniques like this just don't have the reach, don't aren't going to cut it?
*  In the brain, there's lots of cases where it's hard to do any of them.
*  So let's say we're in that situation where we record not from all neurons in the brain,
*  but from a whole bunch of them.
*  In that case, every variable influences any of the others potentially.
*  And there are confounders.
*  In fact, there are 10 to the 10 confounders arguably.
*  And we currently don't usually record from more than 10,000 neurons or something.
*  So there's effectively an infinite number of confounders.
*  Now, under those circumstances, none of the techniques
*  from quasi experiments can work.
*  In fact, no technique for causal inference can work in that domain.
*  And the reason for that is simply that anything we do see among recorded
*  dimensions could be arbitrarily mediated by things that we don't see.
*  So we can never know it.
*  And arguably, much of what we are trying to do in neuroscience at the moment is
*  in that domain where we cannot get it causality like that.
*  And that's why it's so valuable that the
*  development of perturbation techniques that's really moving very quickly ahead.
*  All kinds of cool new optical perturbation techniques.
*  So I think part of the advancement of science is to get creative.
*  So, you know, there are domains that when questions are hard to answer, for example,
*  if you're asking what's the effect of a country's level of deficit on growth,
*  that's super hard because every country is different.
*  And if you compare one country with another country, there's many reasons why
*  the outcomes could be different, it's millions of people and companies and so on acting.
*  But, you know, for example, one way to make it a little bit better that people
*  have used is, for example, instead of countries looking at US states,
*  because there are various aspects of their
*  fiscal policy or the way they spend their money, because at least US states, there's
*  50 something of them and they're similarly, they are more similar than different countries.
*  At least, you know, they have the same legal rules and so on.
*  So we are putting ourselves in a better
*  situation to at least do, for example, difference in differences by comparing states.
*  And that's what I did, for example,
*  with Alaska, looking at the universal basic income style that they have,
*  comparing Alaska with other states, which was not difference in differences,
*  but a related method. So that sort of allows us to take it one step further.
*  But many questions are hard to answer.
*  So then it's about being clever and talking about the big question,
*  but finding a setting where you can reasonably give an answer that you can be
*  confident enough about your causal inference, because in that domain,
*  you can be sufficiently confident, even if it's hard to answer some of the very big
*  questions, because, again, there's a lot of variables that play at the same time in many of those big topics.
*  But I think we can explain to Paul how to very easily see it.
*  So if we randomize things, then figuring out causality is easy.
*  If we don't randomize things, if everything connects to everything else,
*  then we have no hope.
*  We do have hope if there is someone who moves the lever in a meaningful way.
*  At some level, the thresholds that we have is a way where someone,
*  which is that threshold, is moving the lever.
*  So quasi-experimental techniques will generally be useful if there's a small
*  number of actors of some generalized way that kind of somewhat randomly execute
*  their policy, where there's aspects that are locally as good as regular.
*  So when it comes to, say, how the news media work, it will be extremely difficult,
*  not like how Twitter works.
*  Like you economists aren't going to build
*  a model that predicts which celebrity is going to trend tomorrow.
*  But I do want to say about RCTs and the established causality,
*  the interesting thing is that they tell us that the policy has an effect,
*  but it doesn't tell us why necessarily.
*  So if the policy is a complicated policy that has many different aspects,
*  just from doing the experiment, we don't know which aspect of that policy did the
*  job, and so that's why I think there's a good complementarity between doing
*  correlation studies and more quasi-experimental or even experimental,
*  because the correlation studies, while to be taken with a grain of salt,
*  can allow us to have ideas to test out about certain mechanisms that might be at
*  play and then find a setting where we can reasonably establish causality for that
*  mechanism. So I don't think that correlation studies are at all to be thrown away.
*  It's just like you have to be careful that you cannot conclude to causality
*  from a correlation study, but it can suggest plausible causal mechanisms.
*  Like people who are careful will say so,
*  this suggests that this might be going on.
*  And then it's a first step that then you can take further and try to look for a
*  context where you can test that out in a more experimental or quasi-experimental way.
*  So correlation studies then could be seen almost as a roadmap to finding where you
*  can start probing causal, like the little local areas where you can start asking
*  causal questions. Right.
*  Yeah. But there's a problem, which is that can be a fig leaf,
*  like where basically everyone runs correlational studies
*  without much certainty about what they mean, but
*  but it's fine because it's just inspirational or something.
*  Right. But it's a matter of balance.
*  And I think to some degree in certain subfields of economics, we've gone so far
*  as to not accept very interesting correlational studies at all.
*  Like we don't want to hear about it.
*  And I think that's a mistake.
*  And I think that's a mistake because I think we can learn a lot from correlational,
*  especially when they're carefully and thoughtfully done, you know, without
*  overcleaning, we can learn a lot.
*  But my field in some sub areas of economics has gone so far as to say,
*  if it's not an experiment or a quasi-experiment, I don't even want to hear about it.
*  And you've been brainwashing me.
*  A little bit.
*  Well, so so so you guys will be the Hitlers of correlational studies in
*  neuroscience.
*  OK, OK, so I think that's a pretty good
*  summary of the work and gives people a lot to chew on.
*  One of the things I've been enjoying about doing the podcast recently is that what
*  I'm hoping that it's doing for people is just giving them another something else to
*  start thinking about and incorporating into their thoughts as they move forward
*  in their own scientific endeavors here.
*  So so I really appreciate it.
*  We're coming short on time, but would you guys mind answering a few sort of more
*  general broad questions here?
*  Sure. OK, I'm good.
*  OK, just at the top, what book or resource would you recommend to learn more about causality?
*  We talked about Judea Pearl's The Book of Why.
*  I love the Book of Why.
*  I love his older book called Causality, if I remember that right.
*  But it's one view on causality, right?
*  Very stats minded way of thinking about causality is beautiful.
*  I love it.
*  But I must say that the mostly harmless
*  econometrics book by Engrest and Inga Pishke is also beautiful.
*  So Joshua Engrest at MIT has two books that I recommend to people.
*  One is Mostly Harmless Econometrics and Mastering Metrics.
*  And they are both a good, pre-solid, mid-level introduction to these topics.
*  It's not intro intro.
*  So, you know, I would necessarily recommend if you never heard of statistics and so on.
*  So it's a good level if you know things and you want to tool up and understand
*  what's going on in econometrics.
*  I think that's my audience. It's a pretty educated audience.
*  Mastering Metrics, I think, is very readable.
*  Yeah, so Mastering Metrics is a little more accessible.
*  I think to start with the combination of Book of Why and Mastering Metrics is great.
*  OK, good.
*  So just to talk about causality, just a bit more, not really causality.
*  But like I said, Judea Pearl makes the point, and I won't say his name more often
*  in the podcast, but that AI is really hindered by not having causality built
*  into the systems, right, that it's all basically statistics and probabilities
*  right now, that it's all curve fitting and pattern matching.
*  So, for example, a machine would be able to correlate the appearance of fever
*  with malaria, but wouldn't be able to suggest that malaria causes fever.
*  Right. This one example that he gives.
*  So the question is, do you think that religion as a judging and creating
*  and causing God, that that aspect of religion, do you think that will ever go away?
*  That's an interesting question.
*  Why would it be a good thing?
*  Well, it seems the progress of increasing information and knowledge, human knowledge.
*  So we infer causes less and less to third parties, gods, deities, etc.
*  more and more to natural, natural events. Right.
*  So that's just it.
*  But, you know, I think to me, religion is less about causes and more about meaning.
*  And I think those things are different.
*  You know, it's one thing to know kind of mechanistically what causes something.
*  And this is something that current I work a lot on.
*  But it's a it's a different issue to talk about the meaning of things.
*  And that is intimately related with values.
*  So what we value causality is very much what you can call it.
*  The domain of the positive line of scientific line of inquiry about what is.
*  And I think a lot of religion has to do with what ought to be, what is meaningful
*  or valuable, and this is something that science has nothing to say about in any
*  direct way. And so therefore I don't really think that
*  certainly in the current state of affairs, there's any conflict between more causality
*  and the place of religion, maybe early on because religion was making all these
*  encompassing claims about what's going on.
*  But we've moved on from that very far away.
*  I think nowadays the religion is more about the meaning and the values and not so much
*  about explaining the world in that causal way.
*  Yeah. And the times where God was the
*  cause maker comes from the time of like the ancient weather religions.
*  It's still around, though, it's still present.
*  It might still be resonating a little bit, but
*  but I don't think for a lot of people today, God is the cause of physics anymore.
*  I think God is something much more human.
*  It's something about the way we think.
*  And it's something that has relations with us as as opposed to
*  something that makes the mechanics work.
*  See, I
*  well, this is this could really go into a long discussion here.
*  So we'll just curtail it, I suppose.
*  But
*  we'll be back.
*  I know.
*  I'll be back next week.
*  I just realized, too, that I think the last time we spoke, I must have been in
*  in a halfway between when I was living in an RV and in our new house.
*  So I don't think I had the studio.
*  So we've had a lot of change here.
*  I don't know what caused it, but we had a lot of change.
*  What's the counterfactual?
*  Oh, yeah. OK, I'm going to work this out after the after the show before
*  we speak next.
*  So what role do you think embodiment will play, if any, using A.I. to understand our brains?
*  So I think the bodies that we have have a huge influence on the kinds of problems
*  we need to solve and the kinds of problems we need to solve,
*  I think, have a huge influence on the way we think.
*  And when it comes to the role of bodies,
*  I can just mention Malcolm McIver's work, which is beautiful, where he's
*  conceptualizing the roles of animals as a function of how their sensory system works.
*  So he works with weekly electric fish and nicely highlights how for different
*  animals, the part of the world that they can sense is very different.
*  And therefore also the way they deal with information from the world is very different.
*  So if you can only sense the immediate vicinity of your body, then there's like
*  little reason to carry really complicated theories with you.
*  Right. So basically, the further you can see and the more there's reasons to plan
*  and think ahead because you can see those things.
*  So it's about seeing if you have only a very immediate perception,
*  arguably it is less useful or feasible to start to have planning thoughts.
*  Yeah, I've been thinking, been learning more about interoception and the role that
*  that plays in our moment to moment awareness and what it could mean
*  within the realm of consciousness and higher order cognition.
*  So, oh, very interesting.
*  Conrad, I know that you are a collaborator extraordinaire and this latest work was
*  a collaboration with somehow you collaborated with someone you know in economics.
*  And the last time you were on the show,
*  you talked about how important it is to play and to experiment with different
*  avenues of learning and topics.
*  What do you think? This is a question for both of you.
*  What do you think the right balance is
*  between collaboration among like minded and near topic and otherwise folks
*  between that and sort of solo deep focused study on the depth of a single topic
*  and exploring less related topics?
*  Is there a right balance there, do you think, that you would recommend for people?
*  I see the value of both of them.
*  So I have a good number of collaborators who choose a relatively narrow set of
*  topics, but they have this incredible, fantastic, deep knowledge of absolutely
*  everything happening there.
*  And these people in a really important way carry the knowledge of mankind.
*  They carry what is known in that area.
*  I think it helps for progress to also have people that are a bit like me and to some
*  whole young are just as well that are linked into these different traditions
*  and these different intellectual sources and can can highlight how certain
*  combinations are really promising for the future.
*  So in that sense,
*  I think what we have at the moment might be quite good that there are some people
*  who try to build the bridges, some people who really focus deeply.
*  But
*  my hunch is that the way the system is structured, it makes it harder for the
*  people who build bridges. So there are a couple of more senior super,
*  super successful bridge builders.
*  But if I see young PhD students who build bridges or postdocs, it's often career
*  ways harder for them than the people who take one field and focus on that.
*  And that might be holding us back from some
*  interesting bridges that could be built that aren't being built.
*  Yeah, I really agree.
*  I think part of it is a personality trait, like sort of what, you know,
*  what are you happy with as an individual?
*  If you're more collaborative, you know, as a personality,
*  et cetera, then it might be a good way to go for you to build those bridges.
*  And I agree with Conrad that when you're
*  starting out, it's often dangerous to, you know, for example,
*  write into many different topics, even worse disciplines.
*  And that's because of the and that's where I'm an economist.
*  I think of the incentive structure,
*  meaning the rewards that you get in the job as an academic.
*  And so for young people, ultimately, for example, they need to get tenure,
*  which means they're going to get letters from older experienced researchers
*  that testify to the importance of their work.
*  And usually, and that's in a way a good thing,
*  people want to speak to something that they understand well.
*  So if someone has a lot of work in very different areas and you ask another
*  scholar who specializes in one particular area to talk to you about the importance
*  of this person's work, they say, well, they wrote one paper in my area.
*  It's pretty good. I can only talk to that one.
*  So therefore it seems like their contribution is a little bit lost or it's
*  hard to get someone else to explain to you why this person's contribution is very
*  important. That's why it's very often times very risky as a young person to in
*  science to go to many different directions.
*  So I'd say if you're at least you want to have a core,
*  there might be a periphery of other things, but it's good to have a core of like
*  highly specialized work that is in the particular area.
*  Franti, I think you have been in.
*  Yeah. So basically up to tenure, I was running with this base in motor control
*  thing. I was like clearly the man for that.
*  And then once I passed that threshold, I was like,
*  well, so the I had John Crackauer on the show a few weeks ago.
*  And one of the things that he advocates is
*  even for graduate students and and everyone really is taking a day and just
*  going to the library and not randomly, but looking in different areas and exploring.
*  Right. So and I recently read a book called Make It Stick.
*  I'm not it's a book about the latest
*  John Heath and Keith Heath.
*  Yeah, a really good book.
*  And one of the things that they have that they say has improved learning is this
*  concept of interleaving, which is you sort of move on from topic to topic and come
*  back. So you have multiple strands going on kind of but slowly move between them.
*  And that actually improves the process of learning.
*  And I would imagine improves creativity as well.
*  I don't know what you think about that.
*  But I would also recommend judiciously use Twitter is also a great way to expand
*  your knowledge and come up with new ideas that are maybe a bit different from what
*  you usually do.
*  And just like it just so refreshes my brain and gives me new ideas and new
*  directions. So I really recommend sort of following other academics in your field
*  and related fields.
*  That's why it's easier on Twitter because the cost of interaction is so low.
*  You know, maybe you're not going to go to a conference that's in a field that's
*  too different from yours.
*  They can follow two or three really interesting people in that field.
*  And it gives you some idea of what they're doing and who knows, maybe an
*  interesting thought will pop out and you can think, oh, I can actually bring
*  something to this question that they're talking about and read that crazy
*  causality stuff by your own and Conrad, for example.
*  Yeah. So, OK, this is a great place, I think, to ask you just a few newlywed
*  questions and then I'm going to let you go because I don't want to take more.
*  So this is not specifically a newlywed question,
*  but who uses Twitter more judiciously?
*  Speaking of judicious use of Twitter,
*  I think we're both doing that pretty well.
*  OK, good. We have the same number of followers, more or less,
*  and we've been on it for a similar period of time.
*  I think we're kind of mirrors of one another.
*  Yeah, don't get into fights.
*  But yeah, yeah, exactly.
*  Don't feed the trolls.
*  Yeah, don't feed the trolls. Yeah.
*  So like, try to be measured in what you say.
*  And even so, sometimes people will complain.
*  But the more you come out with like, you know, crazy statements or not
*  necessarily crazy, but like very opinionated takes and the more you're going to get into...
*  I would never tweet something that I wouldn't feel comfortable saying at the next level.
*  Yeah, I don't think that's the average user experience.
*  OK, so the way the newlywed game worked, if I remember correctly, is so I ask,
*  let's say I ask Ioana a question about what Conrad's would think about something, right?
*  OK, so...
*  And then what do you guys say?
*  And then if you match, then you should get married or you should stay married.
*  OK.
*  What do you think?
*  So Ioana, I'll start with you.
*  So what do you think Conrad's weirdest quirk is?
*  I say it's his tendency to pick up his phone whenever there's even a second of that time.
*  It's a weird thing.
*  Well, I find it a little weird.
*  What would your answer be, Conrad?
*  And it's much weirder that I like playing with anything.
*  I like playing with ideas, I like playing with things.
*  I think relative to most other people, everyone's using their phones all the time.
*  That's not a distinguishing character.
*  OK, guys, let's keep it friendly.
*  I think I play with ideas more than other people.
*  So boo!
*  Maybe what I answered is what?
*  And what would be the most?
*  I didn't want to go down that road.
*  And you answered with your hate mouse.
*  I'm keeping it friendly here.
*  So
*  let's let's OK, so then we'll reverse this one and then I'll just ask one more about.
*  So then so Conrad, what do you think Ioana's weirdest quirk is?
*  What Ioana's weirdest quirk is?
*  I can see he's playing with this idea right now.
*  Yeah, that's that's all her quarks by now
*  are no longer weird.
*  Yeah, right.
*  Let's see, her weirdest quirk.
*  She for the listeners at home, you want us really eyeing Conrad hard right now.
*  Ioana really like anything we do together can be more meaningful if it can be
*  combined with at least three minutes of salsa in some way.
*  OK, does that match up with your with your answer to the question?
*  Ioana?
*  I don't know. Maybe.
*  I mean, again, for me, remember, it's even harder to answer this question
*  because of a counterfactual problem.
*  It's hard to imagine not being myself and asking myself what's weird about myself.
*  Of course. But that's the whole point.
*  Actually,
*  but you should think of game theory and think what would Conrad say is the weirdest
*  thing. That's that's how you win the game. Right.
*  Yes.
*  But he's in the same position having been with me for a while.
*  He no longer remembers the counterfactual.
*  You must say that that's kind of a totally tenable weird quark thing.
*  Sure.
*  Not necessarily super prominent, unlike your phone checking.
*  OK, this one will be more straightforward here.
*  OK, so maybe Conrad, I will start with you first here.
*  So who do you think Ioana's scientific hero is?
*  If she had to pick a scientific hero.
*  Ioana's scientific hero.
*  I think Ioana thinks Angrest is pretty damn cool.
*  True. Is that right?
*  Yeah.
*  High five.
*  High five.
*  Like number one on the not getting divorced.
*  It's definitely I don't have once and it's one of the therefore good answer.
*  So what is Conrad's?
*  This guy whose name escapes you because it's a rare name.
*  But in your ten or like your ten ethical rules, there's someone's rules.
*  And they don't work on something that someone else could come up with if only
*  they had the time. Oh, yeah, yeah, yeah.
*  That's Dijkstra. Right.
*  Yeah, Dijkstra is awesome.
*  Yeah, no, Dijkstra is definitely could be one of them.
*  All right. Congratulations, guys.
*  I'm I'm glad that I have caused your marriage to become stronger through this process.
*  Thank you.
*  Mine is the weird quark.
*  Yeah. Yeah.
*  Conrad, you should never lose an opportunity to to
*  incentivize your husband to do the right things by pointing out publicly.
*  Yeah.
*  Yeah, Conrad, you may now check your phone.
*  Now, just kidding.
*  He's actually the awesome as ever.
*  And I think every day I'm grateful to have him.
*  And you too.
*  What a note ended on OK, so I'll see you next week.
*  Thanks for being here this week.
*  Seriously, appreciate it, guys.
*  Appreciate the time.
*  Thank you.
*  Brain Inspired is a production of me.
*  You can support the show through Patreon for a trifling two or four dollars per
*  month. Go to Patreon.com slash Brain Inspired or go to the website,
*  Brain Inspired.co and find the red Patreon button there.
*  Your contribution will help keep this show
*  going without any annoying advertisements like you hear on other shows.
*  To get in touch with me, email Paul at Brain Inspired.co.
*  The music you hear is by The New Year.
*  Find them at TheNewYear.net.
*  Thank you for your support.
*  See you next time.
