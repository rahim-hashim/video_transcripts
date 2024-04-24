---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4951s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 158
Video Rating: None
---

# BI 026 Kendrick Kay: A Model By Any Other Name
**Brain Inspired:** [January 30, 2019](https://www.youtube.com/watch?v=A4r_GHeNyek)
*  I think what's more likely is through non-brain-like tricks and algorithms and techniques, we can
*  create quote-unquote intelligent systems that will be for all intensive purposes, you know,
*  as good as a human.
*  And I think once that day comes, it'll be almost kind of an anticlimactic event.
*  This is Brain Inspired.
*  Good day, fellow interested humans.
*  I am Paul Milbrooks.
*  Welcome to the show.
*  So models, we use them in neuroscience to model our brains and cognitive processes,
*  including deep learning neural networks.
*  Our brains create models of the world so we can do things and experience the world.
*  A lot of people think I should be a model.
*  Well, okay, not so much.
*  But often we take models for granted, not thinking too much about how a particular model
*  fits in the universe of models.
*  What really is a model?
*  What makes a good model?
*  How do we understand models?
*  And so on.
*  Kendrick Kay thinks about these questions and has written about them.
*  Kendrick is a cognitive neuroscientist who runs the Computational Visual Neuroscience
*  Lab where he uses models and fMRI to understand visual processing in our brains.
*  We discuss his recent models that can predict brain responses in ventral temporal cortex.
*  It's a brain region associated with categorizing visual information like faces, etc.
*  And his models can account for the decisions people make and how another brain region
*  in the parietal cortex can scale the activity in ventral temporal cortex depending on the
*  demands of the task.
*  We talk about how his models compare to the deep learning networks increasingly being
*  used to model brain processing.
*  We also touch on a huge fMRI database that he's collecting to hopefully be used as a
*  common tool to compare different models visual processing.
*  Kendrick also co-founded and runs the Cognitive Computational Neuroscience Conference which
*  we discuss.
*  And as usual we just scratch the surface so if you are into this sort of thing you should
*  check out a few of his recent papers to dive deeper.
*  Show notes are at braininspired.co slash podcast slash 26.
*  This morning as I was doing my little gratitude practice I wrote to myself about feeling grateful
*  to my Patreon supporters.
*  This past week Alexander, Donald, and Al all became patrons of this little podcast and
*  it's a thrill to know that people are willing to part with a couple bucks a month to support
*  efforts like the Brain Inspired podcast.
*  I say this every week and I mean it.
*  Thank you.
*  Also I want you to know if you are a supporter or become a supporter I'm thinking of ways
*  to give you something extra for that support.
*  I have a few ideas forming and will continue to brainstorm.
*  I do plan to create a short course in the near future.
*  I will keep the topic under wraps for now but you will have access for free to that
*  course if you're a supporter when I release the first version of said course.
*  In the meantime if you have ideas you'd like to share with me in that realm send an email
*  to paul at braininspired.co or you can find me on twitter at pgmid.
*  I've been enjoying hearing from many of you and plan to invite multiple guests and
*  cover topics that have been suggested to me through email and twitter.
*  To become a patron and spend two or four dollars per month on the show go to braininspired.co
*  and click the red Patreon button there.
*  Alright enough already.
*  I hope you're having a beautiful day out there and I hope that you enjoy Kendrick as I did.
*  Kendrick Kay father of two dogs and I don't know how many cats.
*  Just one.
*  Just one cat.
*  Just one cat.
*  Okay thanks for being here and welcome to the show.
*  Thanks thanks for having me.
*  It should be fun.
*  Kendrick you run the computational visual neuroscience lab, the CVN lab at the Center
*  for Magnetic Resonance Research at the University of Cold Minnesota where you do human fMRI
*  and make models to understand our visual system among other things.
*  I know however that you did your undergraduate work, I guess you majored in philosophy and
*  the last episode I had John Krakauer on and we spoke a little bit about philosophy and
*  its usefulness in neuroscience and science in general.
*  Philosophy rather is what really drove me into neuroscience from the beginning.
*  I was really into philosophy and then realized how useless it was and then got really really
*  into science and now I guess we're all realizing how useful it still is.
*  So how did you transition from philosophy to psychology and neuroscience?
*  Good question although I'm not going to answer that for a minute because I'm going to do
*  a philosophical move on you or turn.
*  Oh my god I'm sounding like a philosopher now.
*  Which is you were saying something like oh you used to think it was useful but now it's
*  not but the question is what is philosophy because it's definition of terms maybe that's
*  really important.
*  What is the definition of philosophy that you're using right now that causes you to
*  say it was useless and there's at least two off the top of my head there's at least two
*  very different ways you could mean philosophy.
*  You can mean philosophy as it is traditionally done as an academic pursuit in your undergrad
*  or in graduate school etc etc or you could mean philosophy as a way of thinking and pursuing
*  about definitions and implications of definitions and making sure that we're clear on logic
*  and the kind of theories we come up with and blah blah blah about the brain.
*  Well see I think that's the more useful type of philosophy that is going to be useful moving
*  forward and it's you know it's interesting you're talking about definitions because we're
*  going to be talking about models pretty soon too but I was into the latter the latter kind
*  of philosophy in the beginning in fact I may have permanently borrowed a book on existentialism
*  from my high school library that really set me down that awful awful tract you know.
*  Wait but the latter definition is the one that you started to hate at some point in
*  your life.
*  No I'm sorry the former.
*  I meant the former.
*  The former right right the first it as an academic pursuit and certainly maybe we share
*  similarities there because I was a official philosophy undergrad and I was thinking about
*  doing a PhD in philosophy.
*  Wow.
*  And like to the point of I was about to send an application and I think I tell the story
*  often but basically I was about to and I was only held back by one of my favorite philosophy
*  professors and he I think had the judicious advice of like you know take some time to
*  think about it and like is this you know I was just a senior in undergrad like is this
*  really what you want to devote the next and years of your life to.
*  So I did step back and I guess ultimately decided not to apply.
*  As a philosopher would step back and think about it.
*  Yeah certainly.
*  So I did avoid your question how did I transition I guess oh that was the answer yeah I transitioned
*  by realizing there's a thing called a brain and that we can study it which is not that
*  much of an exaggeration I don't think.
*  I guess you know in undergrad I was interested in philosophy of mind so maybe not hugely
*  off base here and but my you know background in the study of well let's use blanket terms
*  psychology so behavior and kind of theories as to cognition stuff and neuroscience like
*  biology like I had very little background in either or I neither had background in either.
*  Right.
*  Whatever you want to say it and so the decision I guess on my part was sort of made with very
*  little information I really didn't know much about the brain or psychology and neuroscience
*  I just decided oh there are people do study it so maybe it might be fun and so that happened.
*  And fast forward to present day and now we know all about the brain right.
*  I think I mean these are you know topics you can shoot the shit over like do we are you
*  half empty or half full on the brain and I think I would fall on we're actually on the half full
*  side we do know we I think we of course you can have cranks who don't believe anything about our
*  current understanding of basic biology and brain stuff but I think on the whole if you ask people
*  that we there are a lot of quote unquote facts there are things that I think we all agree on and
*  I would say in general there's a lot that we know.
*  That's a good attitude so okay so we have a lot of stuff that we could talk about today I kind of
*  want to just spend a couple minutes talking about the cognitive computational neuroscience
*  conference so I had Nico Kriegesskorte on oh a couple months ago maybe and he participates in
*  that conference but you are a co-founder of it was it with is it with Thomas Nezorales that you
*  found in it. That's right well it depends on how you define the found haha but um but yeah he and I
*  kind of were drinking beer one night and bandied about this idea and I mean this was must have been
*  five years ago now um and yeah so maybe it kind of grew from there we kind of both thought it might
*  be worth doing and then exactly what form it would take is unknown at that time but we slowly grew the
*  group into um what it is currently. So what is it currently just to recap for people who maybe didn't
*  hear that episode? It is a relatively small conference I think last year there were 400 or 500
*  or maybe 400 um the the first year there was more maybe due to the location it was in New York City
*  I think we had more than 600 people come so I'm not sure that is small anymore but the second year
*  we did it which was just a couple months ago was a little bit on a smaller scale and it's it's stated
*  purpose is to try to attract people from different fields like actually different fields like people
*  from machine learning and artificial intelligence people and what you might consider neuroscience
*  which is of course a huge field in itself as well as what you might call cognitive science which
*  maybe you might want to term psychology or people who maybe primarily focus on behavior and
*  understanding cognition through behavioral careful behavioral uh experiments. So yeah it's trying to
*  bring different groups of people together which is hard but I think we've made some progress and
*  you know logistically the conferences is evolving a little bit in terms of like you know abstracts
*  and papers and posters and we definitely have tried to um include new types of way to interact
*  at conferences like little funny events and not just funny but uh hopefully productive and
*  interesting experiences of ways that people can kind of gather together in little groups and
*  exchange ideas and hopefully form collaborations over you know the next several years. So okay very
*  good so and this next year it's going to be in Berlin I know so that'll be interesting to see
*  what kind of turnout you get there. What does it take to start a conference? It seems like a really
*  big ordeal. It is but I was about to say it's not actually that fun. It's exciting at some level
*  but it's also very boring in terms of the mundane things you have to do. Right can't you outsource
*  those things though? Yes and no I mean it comes with the I think the usual downsides of involving
*  more people in an endeavor like the more people you involve yeah they can bear some of the
*  workload but unless they know exactly what you want and like the other the bigger picture like
*  there's an overhead to bring you people on you know too many cooks spoiled the broth that's
*  the thing. Yeah so yes too theoretically some of it can be outsourced but uh at least the first few
*  years maybe things will get more solidified and clear obviously there are conferences that are
*  bigger and more established that you know maybe they have their act together and can kind of
*  uh glide more than um it's been but it's been pretty it's been a lot of work I guess involved
*  in doing a conference well it's it's it's um it's it's communication in a sense like you have to
*  advertise and get people excited and kind of secure good keynotes to kind of guide the you
*  know this is the type of conference it's going to be and you know you hope the quality of the content
*  that these keynote people that you invite will be good and you know so you have to kind of network
*  and kind of think of a vision for what what type of conference you want this to be like the scale
*  like is this should be is it going to be extremely intimate it's going to be huge is it going to be
*  somewhere in between and then I guess that maybe the more exciting and fun part of it is
*  uh designing what it actually is and again alluding to like this is I mean the traditional
*  conference is like okay there's posters and talks and that's basically it and maybe a few long talks
*  but um I guess we have the freedom to kind of do what we like and so we did play with some other
*  types of events and thinking about how they might go and how we might design them but you just sit
*  around and think and do a lot of skyping none of the organizers were at this same low that's not
*  true there were two in uh university of Pennsylvania I think other than that we were all over the place
*  and there was one in europe too organizer um so a bunch of skype calls and emails and
*  interfacing with a you know administrative company to make the website that type of thing
*  so that I mean I think that answers your question what is involved in making a conference yeah
*  yeah it's you know it's kind of a mystery you know but to peek behind the curtain and just
*  personally I've never really thought about what it might
*  involve to to make a conference you know or had the idea hey uh I should make a conference you know
*  so that's just an interesting thought process but I'm I'm noting here advice point number one from
*  Kendrick K do not start conference okay got it unless you enjoy it like unless you enjoy the
*  logistics yeah I mean a lot of it is just figuring out logistics and getting people on the same page
*  well one of the really cool things that you guys do I know you try to do a thing a few things a bit
*  differently and I don't know if this is different but it's really uh beneficial to the rest of us
*  is that you put all the talks up on youtube um all the uh visitor the keynote speaker talks um
*  which is just a fantastic resource so thanks for doing that yeah no problem and I mean we're not
*  the only ones I mean they're nowadays I mean it's growing I think in general uh the talks being
*  online but but yeah I'm glad you enjoyed them okay so before we talk about modeling and your model
*  tell me just a little bit about this massive fmri data set that you're collecting uh I guess
*  you're collecting it with uh with thomas naza lares yeah um it isn't out of the blue and like
*  lately there's been a lot more kind of data sharing in the field although which field we're
*  talking about is neuroscience if that's the field um and specifically fmri data sets have been
*  especially large scale fmri data sets have been more prominent lately uh the connectome project
*  was I guess the one that's immediately comes to mind given that I'm here at Minnesota uh the human
*  connectome project I actually have you heard of it the human connectome project yes yeah yeah okay
*  you've heard of it yeah so large scale fmri collection projects makes a lot of sense and
*  data sharing many people argue is a good thing and etc etc um but that still begs the question of
*  exactly what type of data well type in terms of the type of device you use fmri is just one
*  of many devices as well as like the experiment if any of course you could argue resting state is not
*  really an experiment right it's like the anti-experiment but that that's a huge
*  space to play in what is it sensory is it cognitive is it both is it involved in
*  memory is it um resting state etc etc um and also another big knob to play with is like
*  amount of data so do you want lots of data on one person or a little bit of data on a lot of people
*  and who are these people are these people like your gung-ho you know cognitive they can participate
*  are what traditionally we do as cognitive experiments very well or are they more real
*  people not grad students and things like that so there's all these parameters to play with
*  any case yeah the effort we're in the middle of conducting is one of these large scale image
*  type of representational experiments where we sample many but of course it pales in comparison
*  to all possible the space of all possible images let alone movies where we sample a lot of somewhat
*  uncontrolled naturalistic type images and while measuring fmri responses there is a choice of task
*  and exactly the trial design and all of these important issues as well as mri acquisition
*  parameters which we could spend a whole hour talking about but it's one of these types of
*  large-scale image type data sets there was a recent effort actually very similar from cmu
*  they called it the bold 5000 so it's it's similar in spirit to that type of effort and it is
*  something that thomas and i did gosh a decade ago actually um 13 years ago we we kind of did
*  one of these data sets on our on ourselves and it was very different to the one we're doing now and
*  we hope this new data site will be many orders of magnitude better but that's something i've been
*  working on lately so anyway fmri bold responses measured at some you know spatial and temporal
*  resolution to we're trying to get 10 000 images per subject and we're using somewhat non-overlapping
*  images so across eight subjects the total number of distinct images will be 73 000 all right that's
*  the scale so 73 000 is not a million what it would take to get to a million uh that's harder
*  there's it's it's a matter of time and money and both the subject's time and your time right as
*  the person at the scanner operating and money in terms of paying subjects scan time money
*  uh terabytes of displace money that's all your money it's probably a lot of sleeping in the scanner
*  although i guess they're performing some tasks too right now we are we are paranoid about that
*  like that is one way in which efforts like this will yeah be a failure no but our i'll tell you
*  the you know every single stimulus trial trials we require a button press which is some indication
*  they're awake yeah um and trying to do the task hopefully there and we also have a tabs on there
*  is a right answer at least on the task that we um do so we do have some checks on that but yeah
*  response rate they're not falling asleep it's so far it's been 99 percent was the minimum
*  performance across the eight subjects so they are at least awake and looking at these images and
*  making a judgment so yeah i'm not that's not that's that that's good to go i'm not worried about that
*  okay so you're going to collect this huge data set that's uh you know it's a lot of data of very
*  good quality and then you're going to uh put on a competition right yes that was that's one of the
*  purposes and i guess the the point of this data is somewhat that it doesn't have one specific point
*  it's kind of this trade-off of you can do a whole experiment and get a lot of time and effort into
*  one experiment that does one thing and i am totally fine with that and in fact many of my most recent
*  papers are more in that direction but this particular data set the we're calling the natural
*  scenes data set which is not a super sexy name but it's nsd this thing is more of a general
*  data set that can support many different scientific directions and this this competition
*  type thing is one of the ways you could do that you could say like hey if this is a really high
*  quality data set that people trust and believe then you can use it to compare different
*  candidate models of say visual processing or visual representation and one of the strengths of fmri is
*  and the acquisition we are doing is a whole brain acquisition which is not like what we did 13 years
*  ago so it technically covers the whole brain so if there are you know hopefully we can find good
*  signals even in regions that are not super well studied like thalamus and subcortical structures
*  cerebellum hippocampus things like that or at least not well studied from the visual point of view
*  right right so people are going to be able to create models and this data set is going to be
*  open to the public so people will be able to create models and pit them against each other
*  and are you having the competition at the ccn conference that we just talked about
*  yes but exactly when and how we haven't really figured that out gotcha just just to acquire
*  this data set let me just tell you about the scale not that you need to get into all the details but
*  we are trying to get eight people to come back 40 times oh my god yeah so that's once a week
*  for 40 weeks which is essentially a year and so it requires a huge amount of commitment and
*  some of these people are you know in science not in my lab per se right so maybe they're
*  motivated just because they understand how valuable this is but not not not not all the
*  subjects are like that so you know just ensuring or maximizing the subjects happiness
*  is really important i think for this kind of endeavor back when we did you know tom and
*  somebody scanned ourselves and so obviously we were motivated and we were not worried that we
*  were going to drop out of our own study but nowadays you know that's not at least for this
*  effort it's not the same and to appreciate the scale of it it's pretty difficult to get an
*  undergraduate to come back even twice huh and for for what for any sort of fmri scanning experiment
*  i mean i know for eeg experiments when i was in at vanderbilt i was part of an eeg lab as well and
*  it's just like pulling teeth to get the subjects who are mostly undergraduates just to come back
*  you know once you know yeah i know you were asking i think me that question i don't really know
*  because i've never done that type of yeah but but i guess i'm learning from your experience that
*  you can't trust undergrads well right actually no um yeah i don't think it's uh
*  violating privacy yeah one of our subjects is i think undergroom or maybe even more than one
*  there may be they may be diamonds in the rough well good luck man good luck with that oh no don't
*  say that i gotta i i vacillate between extreme pessimism and optimism so you'll make it i know
*  you'll make it so that's great so that um you're collecting this this huge data set it's ongoing
*  and it's uh when when do you project it'll be collected turns out the scanner will be
*  decommissioned uh in november oh so even if it's not done it's done i mean of course we can port it
*  to another scanner but there are all sorts of reasons why the data may not be exactly
*  comparable so i really don't want to go down that route so the answer is it's got to be done by
*  november okay good well check back then and see how you're feeling if your optimism came through
*  so i also want to mention this recent manuscript that you've written it's a pre-print
*  called appreciating diversity of goals in computational neuroscience and this is all about
*  modeling goals and and just as it says appreciating different goals of of models
*  from different researchers you guys actually put a survey out and had lots of people respond to the
*  survey lots of modelers respond to the survey just one of the more interesting results is
*  people out of all the ratings the the most important facet of modeling for people is
*  interpretability whereas the least important is clinical relevance yes that that was yes a little
*  giggles yes yes i mean for me that's i you know i know i know we're in the business of helping people
*  and that's a lot of what science is about but for me it's also just it was mainly wanting to
*  understand things so the clinical relevance was pretty low on my list as well uh yeah in my
*  pursuits so it rings rings true yes i guess i mean why it is like that why is clinical relevance
*  weighted so low i mean but you guys didn't these aren't random selections so i don't did you send
*  the survey out to people that you knew right yeah it definitely wasn't randomized in any sense in
*  fact i don't even know how really how one would do that um but my guess is even if you did sample
*  everyone it would also be the loser probably but for no good reason other than it's almost like
*  how science it's the sociology of science it's like the people who want to pursue this type of
*  thing aren't quite the same labs or backgrounds that care unfortunately about clinical relevance
*  let's say so it wasn't like calculated on our parts like why am i not in the clinical setting
*  you know i just i started off doing this type of work and i kind of liked it so i continued
*  it wasn't like i started at the beginning and said like hey i actually don't care about clinical
*  work at all so i'm going to go down this other path no i mean so i it's unfortunate maybe and
*  things efforts like conferences and other grant writing and things like that i mean that grant
*  writing well that that's the thing is it's really important in grants but but maybe not in surveys
*  ah well there's what you say in grants and what you actually think sure sure i'll be sure to edit
*  that out can't drink this uh i don't mind everyone everyone everyone knows this everyone knows this
*  that's true so anyway are you are you guys gonna looking to publish that in a journal or yeah we
*  hope so i mean i mean it's kind of a semi-cute thing but we don't mean this as a joke like we
*  we truly mean what we say and we did do this survey it's obviously not a official randomized
*  whatever uh you know carefully crafted formal survey but it's it's it's not super informal it
*  was semi-formal and so i it makes it's not very long makes i think important point oh you got you
*  even do some principal component analysis analyses on the results pretty pretty uh in-depth
*  stuff actually yeah we're hoping it gets published somewhere but you know we all have our primary
*  research programs and so on you know right well let's let's talk about some of your research here
*  so we're gonna dive a little bit into the details not too deep but um some of the nuts and bolts of
*  of a recent model or trio of models really that that you published and then we're gonna bring it
*  back around and talk about models in general and compare it to you know the deep learning
*  networks that are so popular today okay so so in your 2017 eLife paper it's called bottom up and
*  top down computations in word and face selective cortex and this was with Jason Yeatman so what are
*  we trying to understand in the brain with this work here that paper was a bit of a it covered a
*  lot of ground but i would say the the main focus there was disentangling what you might consider
*  bottom-up driven responses in these particular brain regions versus what's more cognitive
*  and it isn't a completely novel you know general research direction there are many papers that you
*  know attention attention and how it impacts sensory responses is you know long been studied
*  but in terms of like the modeling world if you're a modeler and like you come from the traditions of
*  like neural networks or visual object representation whatever like you often ignore the kind of the
*  top-down stuff obviously i'm not saying people don't know know that it's there but maybe you
*  just for the time being just kind of ignore it and just don't worry about it so this paper i guess
*  tries not to ignore it and tries to say something about to what extent can we kind of understand
*  both aspects of how these you know sensory and both cognitive processes affect the data that
*  we record and we did focus i guess we did want to look at these high level visual regions specifically
*  but theoretically you could be interested in this topic in other you know sensory regions auditory
*  regions is the obvious candidate and hopefully i will come in someone somewhere to explore such
*  ideas but also in the auditory domain because i imagine it will be a similar story but of course
*  that's just speculation but an auditory domain gosh i mean i just thought about it but scanners
*  are so noisy does that affect an auditory experiment yeah certainly it's something that
*  they grapple with and in fact postdoc my lab is that's her primary research area does do auditory
*  fmri which is not as big as visual fmri and it does suffer from technical problems like yes the
*  scanner is beeping at you the whole time very loudly and hence you have to somehow present
*  your stimulus either in silent gaps which changes the mr acquisition and obviously that's not optimal
*  because you want the mr data or another approach is just full speed ahead and just play the sound
*  on top of the scanner noise and then think about whether or not you need to compensate for it in
*  the data that you get interesting so in this experiment you had people in the scanner and you
*  were showing them images of faces and words and you had a little fixation spot we can get to the
*  actual tasks in a second but but the idea is you're scanning them while they're performing one of three
*  tasks here and then you created a model to predict the bold response in a part of the brain called
*  ventral temporal cortex so that was the bottom up direction and then the top down direction is
*  studying signals from interparietal sulcus in the parietal cortex so those are the brain regions
*  and how the the task was set up so what were the people doing in the scanner so the common ground
*  all of these is they were looking at the stimuli as is typical in visual studies you we furthermore
*  ask them to fixate so keep your and not sleeping yes yes eyes open and converged on a little
*  fixation in this case dot so there's a little dot in the middle and that you know covers like 95
*  percent of visual studies we always ask subjects please fixate because a lot of the visual
*  responses in your visual pathways are relative to where you're fixating so if you don't control that
*  then all is lost anyway so um lie still lie on your back open your eyes look at the center of
*  the screen where there's this little dot here and then you know then the stimuli come and they're
*  centered on the screen and like actually right underneath where you're fixated on and uh yeah
*  so there were three different tasks that we wanted the subjects to do one was what we call a fixation
*  task and this is again not super this is pretty common we asked subject to essentially care about
*  the dot itself and not the stimuli the stimuli come up behind the dot but are completely irrelevant
*  and they're not asked to worry about the stimuli or attend to it they're just asked to make a
*  judgment about the small little dot and so the color of the dot changes fairly rapidly of course
*  you can make it harder or easier depending on how fast the color changes and how big the dot is and
*  such so forth but in this study we deliberately made it pretty hard and so this little dot would
*  be twinkling and you're trying to track its color and you're constantly monitoring its color and we
*  access this through a button box so they can press buttons and we know if they're doing the task or
*  not so that's one task and kind of the motivation there is it the stimuli that we actually designed
*  for the experiment are completely irrelevant from the subject's point of view and there were two
*  other tasks so the other tasks were done in different runs so like we would set up one run
*  like about five minutes long and we would tell the subject hey for this whole run just do the
*  fixation task and they would just do that for five minutes in a row the other tasks were done in
*  separate runs categorization task is what we called the second task and that is essentially
*  kind of a gross level categorization of the stimulus on the screen so as you alluded to
*  the stimuli were more or less faces of in words of various manipulations and then a few other
*  funny categories like there was a checkerboard and so I instructed the subjects for each trial
*  and they were grouped into four second long trials which is not super demanding that's fairly easy to
*  do as a subject for each trial you're just once the stimulus comes up you're just asked do you
*  perceive a word on the screen do you perceive a face on the screen or neither so it's a three-way
*  judgment and it's fairly easy and that task is not about the dot it's about the stimulus so now the
*  stimulus is of importance to the subject's brain assuming they're a compliant subject and then the
*  last task one back task which is again common and people use it all the time for various purposes
*  but it's really just is the current image i'm staring at the same image as what i was just
*  presented you know half a second ago or a second ago or the most recently presented image and
*  that's the third task they were asked to perform and so the common aspect of all of these was the
*  stimuli the stimuli were identical on the screen for all three tasks so so why why implement three
*  tasks well why not do all possible tasks but so yeah what is your real question in the experimental
*  design what were you what were you looking at the difference between the three tasks
*  one way to put it is if what you told the subject to do and what they were doing cognitively did not
*  matter to the data that you cared about from these high-level regions then the answer would be it's
*  irrelevant but it so turns out it has massive effects on the measured bold responses in these
*  regions and that's good because now there is some sort of effect that deserves explanation
*  and that's where the kind of that's the impetus for the rest of the paper like there are these
*  effects but why do these occur or how do we come to quantitative grasp as to why how to model or
*  describe these effects right i mean there's a bit of a tour de force here so you have three models
*  that i mean do you just do you think of it as one model with three parts or do you think of it as
*  three models i mean you can see it either way i guess personally i think of it more as three
*  separate models yeah okay that's the way i think of it as well yeah so there's a lot of moving parts
*  but in some sense i mean what constitutes a distinct model or not is you know completely
*  arbitrary but at least the three models do tackle very different bits of the neural machinery so
*  meaning you know if you're if you're only domain was sensory representation then you know you could
*  call your model of v1 different from your model of v2 different from your model whatever right but
*  in some sense that's all capturing the same type of stuff it's like sensory properties as they
*  manifest in the neural responses observed at different points in the back of the brain
*  whereas in this study the three models are describing very different things one of them
*  is a kind of sensory model the another thing is more of a model of how regions talk to one another
*  influence each other kind of a modulation type model and then the third model is a more in
*  lines with actually behavioral work a model of how you think or why you think reaction times
*  are what they are so a kind of a decision making type model right yeah it's actually the kind of
*  a famous model now the drift diffusion model which a lot of the listeners will probably recognize
*  let's okay let's just step through the models real quickly so what you call the template model
*  is deals with how the the visual stimulus generates sensory representations in in one
*  of the areas that we're talking about in the brain the ventral temporal cortex so what's special
*  about the ventral temporal cortex and and maybe you can just describe in broad terms maybe that
*  model what's special well i'm sure you've had people on the show about and talked about you
*  know the ventral stream so ventral temporal cortex is maybe just the human jargon that we'd like to
*  use as opposed to inferior temporal cortex which is the analogous region and macaque would be right
*  so this part of the brain i don't know the story book story or the common received wisdom is
*  you know it contained it's the last stage of processing they have representations that
*  are you know have great computational capacity because they now signify the content of what's
*  out there in the world blah blah blah blah object recognition categorization yeah so that's the part
*  of the brain and then you're i think asking like what's the nature of the model like how does it
*  work what what are the nature of the computations i think you can you can see both ways and maybe
*  this is the topic you want to talk about later which is like what how is this not like deep
*  neural networks or is it the same or why we could go ahead and get into it now and then come back to
*  it later too because it might be helpful to contrast it yeah sure so let me riff on that
*  for a little bit at some level and this is maybe one point of view it is more or less a quote-unquote
*  deep neural network model and it all hinges on the definition maybe this network come full circle
*  like what is philosophy yeah i was i was worried you're going to go down that road okay good that's
*  fine yeah and i i think it's it's really critical to uh say precisely the definition of quote-unquote
*  deep neural network model that we're using because if you make a claim about x without even clarifying
*  what you mean by x like it's almost nonsensical to argue about whether that claim is right or not
*  so from the point of view of the architecture so if we talk about the computations that happen from
*  you know the raw stimulus representation people say pixels but you know ganglion cells or whatever
*  it is a deep neural network in the sense that it is it consists of a cascade you know a series of
*  quote-unquote simple linear filtering type operations followed by quote-unquote canonical
*  nonlinearities and in this in the e-life model there's it's a two-stage one so there's two sets
*  of these so it's linear and then i'm not some nonlinearities and another linear step and then
*  some nonlinearities so at some broad level um it is one of course there's another way in which it's
*  not at all like one it's not at all like the extremely flexible many parameter uh very complex
*  neural network um in the capital n n sense that that you can train to and optimize the weights
*  to perform certain uh tasks it's not at all like that 40 layers deep yeah right so would you say
*  that it's less brain like that it resembles a brain less than a deep neural network superficially
*  you know because you have all these different network nodes the units and then you know
*  passing information forward along the cascading layers yeah actually that's you're bringing up a
*  subtle distinction which i think is really important when we're we're shooting the shit
*  about neural network models and whether they're biologically accurate and this and that um i think
*  what you're saying is given one of these you know multi-layer with many units and trained on many
*  images that flavor of deep neural network model there is certainly a sense in which you can point
*  to a layer and say like that is you know roughly like area v1 or you know you can you're in some
*  sense trying to model like create a artificial or in your computer instantiation of the constellation
*  of neurons that we know exists in your brain um so if you take that point of view yeah certainly
*  the e-life paper is nothing like that because i it's not a it's not formally um actually you
*  could argue one part of the model is like a whole layer of u1 neurons but but at least the way i'm
*  the reason i'm trying to develop this model is not really to propose as a you know in silico
*  replica of a brain at some level of abstraction it's more a claim about what the core
*  computations actually are specificity i guess is the key point here that makes the the responses
*  measure you know using fmri so the kind of mass activity we find in this high-level region
*  the point of the model is to kind of make specific claims about that as opposed to be a
*  full-fledged model of the entire visual system so that actually links with the modeling goals to
*  pre-print um it and and i guess the point of the pre-print is like it really depends whether it
*  has value or not well it kind of depends on what you were trying to do what were you when you
*  construct one of these computational models and they can come in all sorts of flavors like what is
*  kind of the ultimate purpose and the the e-life model shares architectural similarities certainly
*  to deep neural networks but it has a maybe a completely different purpose
*  maybe that's probably going overboard but a very different purpose well i should say also in that
*  the modeling goals paper i mean you suggest give advice to to people writing these papers that
*  they should just explicitly state the goal of their model so as so as not to confuse anyone and
*  so that then people can judge the merit of the model based on the goal in in light of the goals
*  of the model yeah certainly um and i think well i'm a fan of just stating what you mean and
*  admitting the limitations of what you're doing or like if you're not trying to do x then
*  i think it's totally fine yeah we're not trying to do x that wasn't what we're trying to get out of
*  this model and maybe it stinks at x and that's fine but it's really good at y and like that's
*  what we think in this study in this lab or whatever uh that's what we're trying to do i think just
*  being clear it i think it goes full circle back to the definition thing like let's just clarify
*  what it is we're talking about and what it is we're trying to optimize for when we spend some time
*  developing this computational model yeah okay so so this is this is the template model just to bring
*  it back to kind of where we are in your paper so this template model performs operations things
*  to throw some terms you know like divisive normalization et cetera and it can predict
*  the responses in ventral temporal cortex the fmri bold responses that are the observed data
*  are predicted by the model so that's the template model now why is it called template model oh it's
*  maybe to evoke some i think reasonably accurate intuitions so the filtering stage that's common in
*  convolutional neural air core models is you can think of as performing kind of a template match
*  in so far that the weights are the weights are the template and so the thing that drives the
*  downstream neuron that's using the afferent weights is most activated by a stimulus representation
*  that matches the weights so it's just designed to so the choice of word was just to evoke that type
*  of idea so i guess the intuition here a bit like for a face for a face selective region
*  if you believe this model it's as if it is computing a matched template of like is the
*  current how like how similar is the current stimulus to something that is canonically a face
*  so that kind of intuition is what i think the computations perform speaking of models that
*  are not mimicking the brain in silico the drift diffusion model which so i worked with stochastic
*  accumulators so i've done a little stochastic accumulating accumulator modeling and among
*  people who use these so i did research in frontal eye field and in frontal eye field you see a neuron
*  ramps up its activity and reaches a threshold and then once it reaches the threshold an eye movement
*  is elicited right and the drift diffusion model of decision making is not brain like at all at
*  least the the psychological version of it where i'm not sure if i can paint that picture very well
*  in a podcast but essentially the toy model you start off kind of in the middle with an upper
*  bound and a lower bound and then this variable can drift up to the upper bound for one decision
*  or drift down to the lower bound for another decision obviously neurons don't work that way
*  but it's a really good model that can predict response times and decisions quite well so you
*  want to just talk real briefly about how you guys implemented this in the in your work um sure that's
*  i guess i'm more qualified to talk about that i thought you were maybe going to ask me about your
*  my opinion on what you just said but i maybe withhold the opinion there anyway so in um
*  yeah so i guess we are a bit of a newcomers to the decision making literature so i um so we
*  did a very rudimentary uh version i guess what i'm saying is drift diffusion model comes comes in many
*  different flavors yes it is yeah i'm not denigrating the model by the way i'm trying to just describe it
*  so right so yeah so conceptually it's what it's beyond the sensory representation so stimulus
*  comes in your brain does some processing of the stimulus in order to extract something useful
*  in theory and then let's say that's the job of a visual cortex um but that's only the first step
*  theoretically your brain needs to like do something about it right that's the decision it needs to
*  make eye movement or press the button or or whatever so in the the version of what we did in the paper
*  proposed that very simple i don't think it's too objectionable what we what we said or
*  conceptually at least um it was basically saying the responses in these high level regions kind of
*  face selective ventral temporal cortex and word selective ventral temporal cortex presumably the
*  brain and i guess right now we're talking about the downstream like beyond the the areas that
*  receive information from the visual areas presumably the brain is going to use what is observed
*  neurally in these high level visual regions to make some decision that there was in fact a face
*  out there like it of course to the you know untrained non-neuroscientists it's obvious like
*  vision is so easy like the stimuli we use were not like super ambiguous it was super quote unquote
*  easy to be like oh obviously that's a face obviously that's important um but from the brain's point of
*  view it's got to do that and it's got to rely on what's within the box the the neural machinery
*  so anyway so what we did was we took the sensory responses observed in these high level regions
*  kind of the bottom up responses remember the fixation task there's some subtleties here
*  and then we we presume that what's happening is you're using in kind of a multivariate sense
*  you're using responses across multiple regions this word region face region and we also threw
*  in before there you use multi-dimensional neural activity and collapse that onto like a a vector
*  to kind of kind of extract a single number that represents evidence right now i'm going to use
*  some decision making there you go yeah so now you have some neural measure of evidence according to
*  this model and then that number is going to determine how long it takes you to decide hit
*  the threshold right the reaction time yeah so it's really an adaptation of this the basic ideas
*  behind evidence accumulation models but in this case we're using visual responses we're using
*  actual measurements to try to plug that in to be a proxy for evidence and we used we incorporated
*  it and we tried it and it seems to work pretty well as a predictor of the reaction lines that
*  the subjects may took to do the categorization decision so if you remember one of the tasks was
*  given the stimulus on the screen is it a word is it a face or neither we did have button brushes
*  so we have reaction time so that's some data to be predicted okay very good and and maybe should
*  we move on to the third top down attention model in interparietal sulcus so this was called the ips
*  interparietal sulcus scaling model so how does how does this model work so the name of the game
*  here was given that there are large effects of task and by task when we remind you i mean
*  when you ask the subject to categorize the stimulus or perform a one-back or perform one-back
*  judgments on the stimuli the fact that you got the subject to do that seems to cause responses in
*  these visual areas to go up a lot so it enhances the responses yeah so that's fine but that's
*  kind of a poor description of what's actually going on so there's two elements of the
*  ips scaling model one the scaling bit is one bit and the ips bit is the other bit so the name is
*  straightforward scaling is says something about the specific way in which responses are enhanced so
*  is it so to put it loosely like oh is it just additive effect or is it multiplicative or is
*  it some of both and you know what what does that do to the represent the visual representation
*  and so by looking and this is one of the figures in favor if you just look at the data it's very
*  obvious one of those things like oh you don't have to do further analysis if you can just plot it in
*  a way that reveals what the nature of it is but but basically this top down effect at least in
*  our hands when we measured it looks as if it's a scaling of the representation from the origin so
*  take the origin to be like no neural activity or baseline activity and you have for a given
*  stimulus that's like a point in the representational space and when you induce the subject to
*  have these top down modulations of the representations it's as if this dot kind
*  of scales away from the origin just like in the traditional linear algebra algebra sense
*  it didn't have to be like that there are other ways the top down modulation could have manifested
*  but in our data set it looked like a scaling and then the other element was the ips bit so
*  we say that the task scaled it but what is the task task is just some set of instructions you
*  told the subject so really it's the subject who's scaling it well which part of the subject well
*  somewhere in their brain there's some brain region that that's imposing this effect on the visual
*  cortex and so we did a little connectivity flavor analysis to kind of identify a candidate region
*  and that being the ips which itself is a actually a very large region and there's all sorts of
*  further more fine grain localization type questions of exactly which part of the ips and so forth but
*  for the purpose of the paper let's just treat ips as one entity and anyway so it looked like
*  we could use essentially the activation level of the ips as a proxy of how much top down
*  scaling or modulation is getting applied to these visual regions all right so man so that was a lot
*  so those three the three models from the paper which of course people can i'll link to it in the
*  show notes so there's obviously a lot more detail to describe but so that's great so you have this
*  template model where you determine how how a visual stimulus generates the cortical activity
*  in in in ventral temporal cortex via bold response anyway you have this drift diffusion
*  model which is the decision process itself from how the brain uses the sensory information
*  and the representations in areas like ventral temporal cortex to then make a decision on and
*  you have this ips scaling model to implement this kind of top down attention task based
*  activity what are we missing does that sum it up
*  uh that no that just about covers it that's a lot of work a tour de force you might say
*  it was a lot of work but that doesn't mean it's good work well sure but all work is incomplete
*  i know that right so i mean are you continuing to to hash out it is no so without being facetious
*  yeah i do think it's a bit expansive in its scope as i kind of alluded to before like i mean you
*  could do a whole study just on visual representation you could do all study but
*  just on attention you could do a whole study on decision making and people do this all the time
*  yeah but one of the i think one of the goals of modeling or at least the type of modeling i do is
*  like you want the most powerful and expansive model you can get and i guess in the z life paper
*  we were a little ambitious we wanted to kind of quote unquote explain it all of course we're not
*  claiming it's all explained but we did make some forays down to tackling many different
*  processes that your brain is doing even in a relatively simple experiment right this is just
*  images come up and you're just asking subjects to make a judgment and even that despite seeming
*  simple involves a lot of complicated machinery and a lot of modeling to be done can we can we
*  step back and talk about modeling in general now sure so you wrote this paper principles for
*  models of neural information processing and this is in neuro image first of all i think this is a
*  good paper for any modeler to read or anyone who reads modeling paper or basically you know any
*  scientist interested in neuroscience or or ai because you really step back and take a a bird's
*  eye view and a just a fresh perspective on modeling in general and you ask things like
*  what is cognitive neuroscience what is a model you know but was it this recent explosion in
*  deep learning networks that sort of spurred you to think about these issues and and fully
*  articulate them uh it's a mixture so i'd say yes and no so i'd say i mean if you're asking for the
*  history of this two strands one strand is as i have been doing more and more of this type of work
*  so over the last i don't know depending on how you count seven eight years whatever so in the
*  process of pursuing this type of research i kind of was i don't want to say making it up completely
*  because it clearly has a history of other types of papers like this but a lot of the details and
*  how i like pursued it like what to optimize for and like why am i doing this or what is the value
*  of what i'm doing so that has been a strand during the course of my research and i've kind of been
*  over the years collecting thoughts and maybe pet peeves and just making observations of a lot
*  a lot of this comes from like reactions like you present this to somebody either someone you know
*  or someone you don't know or a reviewer and you get reactions that i think in the end are
*  interesting even you know if someone says something negative that's also interesting
*  because you can then like psychologize about why are they thinking about that way or or if it's a
*  valid criticism that's that's fine and you can think about oh can i overcome that can i show
*  can i make progress on that right and in you know these interactions you kind of learn that people
*  think about modeling very differently maybe that was the seed for this paper and maybe a precursor
*  to the the osf you know modeling gold and computational work yeah and so over the years
*  i've noticed like people actually think about models extremely differently and so that's one
*  strand and the other strand is at the same time you know the deep the the rush to use deep neural
*  networks for everything yeah over the last several years and so that was a separate but
*  coincidental happenstance and so at some point i think the editor of this special issue contacting
*  me and he had seen my i gave a talk at bss essentially foreshadowing some of the issues
*  at least in this paper and he suggested oh this would be a good fit for the special issue so it
*  made a lot of sense so i was like okay i'll actually do some writing and you know formulate
*  my thoughts clearly and attempt to and put it down in writing well i think you succeeded i mean
*  so this really does bring us back to the philosophy and you know definitions right so so i mean maybe
*  a good place to start is the question you ask in the paper what is a model yeah i i gave a very
*  satisfying definition i heard from the reviewer my definition was it's a thing that describes
*  another thing yeah oh right well your verbatim it's a description of a system is your your
*  loosest definition of a model uh yeah and i don't mean that tongue-in-cheek i right i i like that
*  definition i don't know i mean it's very generic but i i personally believe that is what it is i
*  am doing when i do all this modeling work right it obviously has no specificity to the brain
*  let alone sensory type work whatever but um i think that's in the end all that models do
*  right i mean you go on to state a little bit more in detail what maybe a cognitive neuroscientist
*  means uh when you know when they're proposing a model um and uh in practice that models are
*  generally you know have precision quantitatively uh and and so there are a lot of these other
*  characteristics that get then get built on top of this original loose definition right um but
*  you know in the paper so you do things like ask why are models useful um you uh you differentiate
*  between functional models uh which deal with um how the input becomes output in the brain but not
*  necessarily how the neurons do it and mechanistic models which do address how neurons and neural
*  circuits transform the input uh into the output and and people can read the paper for more
*  but maybe what we could focus on here in terms of like the deep networks and the models that
*  you you create is what makes a model good and and your your two facets of this are accuracy
*  and understanding so maybe we can just talk about those for a second
*  it yeah so i guess i decided to break it down into just these two things but you can of course
*  slice up the pie differently and in fact not to not that we need to talk about the the modeling
*  goals paper but you know accuracy and understanding nowhere in that is there like clinical relevance
*  so maybe that's even which is obviously can be extremely important and you know um well but
*  you might argue that to be clinically relevant you need an accurate model and you need to be
*  able to understand it so i think it's arguable i i was actually going to say the reverse like
*  if you're optimizing just for clinical relevance you can use black boxes like totally fine and in
*  fact you know medical diagnosis like you have a neural network you train on tons of labeled
*  images that's fine and then if you trust it and you know check it yeah it can be extremely useful
*  that's true and you know the understanding is irrelevant and i'm totally on board with that and
*  it's totally a fine way to go i guess i was thinking in terms of treating the mechanisms
*  under you know of neural circuitry and treating disorders right yeah and i do try to elude at that
*  a little bit like um you know we we get our data and like we sit at our computers and like develop
*  our code but like are you actually going to go surgically resect this part of the brain based
*  on what you think based on your little computer code i mean that's a high bar yeah and um yeah and
*  i would agree to really reach that bar you gotta both be accurate and really understand the parts
*  of your model and that you know so that you can trust it okay so i mean so accuracy is pretty
*  straightforward so the model architecture you make the point that it might not actually map onto the
*  brain right and and that's fine you can still have an accurate model to predict experimental data
*  but understanding and wait hold on i want to yeah go ahead back up for a second um i guess of the two
*  yeah accuracy is maybe a little more straightforward but it is also it can be very tricky and i thought
*  that's where you're going with your example so if you have a you know multi-layered neural network
*  with tons of units in each layer etc etc one way to check the accuracy is uh i don't know let's call
*  it a large-scale regression problem so you just take all the units in one layer say and just like
*  use them as features and some kind of large-scale linear model and that's totally fine if that's
*  where the the way you want to go with that and certainly that can work well if your your goodness
*  metric is like can you find some linear combination of these artificial units that seems to match well
*  some actual biological data and so that's fine if you define the rules of the game to be that
*  but alluding to what you just said ago that goodness metric has nothing to do about the
*  architecture of your model in other words you could change the architecture the number of layers
*  exactly how they're wired together uh you know you could substantially change kind of the innards of
*  the model while still preserving this you know regression metric and so long story short i want
*  to say what counts as being accurate is could you actually have a long discussion about that do you
*  mean accurate in the architecture of your model do you mean accurate and just being able quote
*  unquote regress or predict data right you know and there's other ways of you know representational
*  similarity analysis is like a different way of quantifying a real system or a artificial system
*  and that's yet another different way in which you could mean a model to be accurate so so i don't
*  want to say the accuracy question is super straightforward in fact you could talk at length
*  on exactly how best to declare victory let's not complicate things here kendrick come on
*  me so okay but so so one of the things that you have uh mentioned and i think you mentioned this
*  in your vss uh talk on this topic and in the paper is that one of the things that uh deep neural
*  networks suffer from currently at least uh is in understanding is in knowing how they work now
*  there's a actually a lot of work being done now to attack this you know kind of black box problem
*  as it's called but a lot of people call them white boxes or you know glass boxes because you
*  can actually monitor every single unit right and you can't do that in the brain but i mean what are
*  your current thoughts on on our ability to understand what deep neural networks are doing
*  and and sort of the fallout from that i'm actually not super up to speed on the current uh literature
*  but i'd say great if people are working on um maybe more in the ai field uh ways to
*  visualize and or analyze and or understand the principles the general principles beyond
*  behind these types of convolutional networks or or the various other types of networks other i think
*  great yeah i mean that's what i want so maybe we can just talk about what it even means to understand
*  uh a model right so you go through a few topics um things like do you know how the model behaves
*  and do you know what happens if you tweak some of the parameters you know
*  the architecture have you can you identify the important parts in the model so there's all these
*  different levels of understanding that you uh point to um and i guess i'm just trying to get
*  a sense of what your here's the question why do you hate deep neural networks so much
*  that's that's not a real question but deep networks in some sense can be said to be accurate
*  in that they do great on predicting things right uh but like you said the architecture itself may
*  suffer some accuracy but then in our understanding is where you're where you seem mostly concerned
*  with deep uh networks uh is that right it is right one way i maybe i would informally describe it
*  since that's what this is uh is i guess it's just obsession with like the details of like
*  every little thing so either on the data side or the model side so on the data side i mean we get
*  data of all sorts of types but in the end of the day we can stare at like one or two data points
*  a lot and really worry about why is this neuron or brain area or you know neural population
*  exhibiting activity a little bit higher in this one in you know b than a commit and you could
*  spend all day thinking about that and coming up with possible explanations for these two data
*  points and maybe i'm obsessed with that kind of scale of of worrying about or you know understanding
*  the data of course two data points on the flip side is really boring really you don't want to
*  just know what's happening in these two data points these two stimuli or these two conditions
*  or these two subjects whatever you also want to know 9998 other conditions and you want to also
*  make sure that your model is doing a reasonable job for all the other ones
*  and and likewise on the neural like not just this neuron but is this a general model that works
*  really well no matter what so to achieve that kind of level of specificity well i like that type of
*  stuff on on the data end and but you can also apply that maybe on the model and so parameters
*  these numbers that have to get set in order for some model to actually do something you kind of
*  want to know like well if you want this level of specificity like what every parameter does and why
*  and how it actually interacts with the whole system the whole model to actually generate the output
*  that seems of interest maybe that's an obsession but um that's kind of how i think about it
*  it's a good obsession to have if you're you know doing science so i mean there's there's a
*  completely different let's say you're treating neural networks as a let's use the term statistical
*  non-parametric tool sure right there i mean especially if you choose them to use them instead
*  of a more structured method like logistic regression or linear regression or you know svm
*  if you're just saying okay i'm happy to throw in these hidden units they do non-linear things
*  because i put them as activation functions but at the end of the day i don't care because i'm trying
*  to say you know do a diagnosis or i have supervised labels and you know in that regime like it i don't
*  actually care about the parameters at all if i'm put on my statistician hat and i'm trying to
*  you know solve this kind of real world engineering quote unquote problem and that's totally fine so
*  again this kind of links back to the goals like but i don't think that's what let's say neuroscientists
*  who are interested in using deep neural network models for neuroscience i don't think that's the
*  goal that we should or do have but i just wanted to mention that because that is certainly a
*  reasonable research thing to do and in that regime i couldn't care less about understanding
*  the parameters right well there i mean they're great tools in neuroscience for those sorts of
*  things as well you know decoding decoding the brain and so but in terms of understanding the
*  brain that that is a different question using them as proxies for the brain for instance
*  so they're not going like deep learning isn't going away anytime soon you know so in in terms
*  of using them to understand underlying principles of the brain and how brain gives rise to mind and
*  all the big questions what is your outlook on that compared to models like that that you're
*  implementing right my outlook is maybe not as critical as you're imagining um there's some
*  happy medium like as we kind of alluded to earlier the e-life thing at least the stimulus part of it
*  it's technically a multi-layered neural network architecture so it is kind of like a deep neural
*  network and so it is just one point on a spectrum so i guess going forward if you're asking kind of
*  outlook i guess what i would like to see or maybe i'll do it myself um is to bring in more control
*  over the development and tuning and and bring in more specificity and like thinking about specific
*  and i kind of say this in the in the opinion paper as to like looking at very specific controlled
*  regimes of you know our traditional things visual people like to do like contrast and
*  you know orientation like looking at very specific effects and seeing you know which bits are
*  important for which bits and kind of constraining and simplifying the network architecture and
*  parameters and there's no reason that can't happen and with large data sets kind of like this this
*  natural scenes thing like once you have enough data on the biology end of things as opposed to
*  computer visiony type things you can start using the data to you know tune your complicated
*  many parameter model which is also fine and then you know what if you go down that route the name
*  of the game i think will be interpretation or understanding like understanding which you know
*  this data set is good because it provides information about these parameters and lo and
*  behold we can learn those parameters and you know understanding what those parameters do as opposed
*  to the untuned state right contrasting right the you know maybe pre-trained based on kind of
*  supervised learning computer visiony types things that's fine and then you can start there and then
*  you could quote unquote train it to become more biological of course there's many details there
*  and then it's a very interesting question like what changed obviously the parameters changed and
*  there are a lot of ramers but we want to know i think exactly in what way did those parameters change
*  so anyway that was kind of a rambling response that's what we do here on the show that's great
*  rambling yet somewhat coherent hopefully okay kendrick i've taken a lot of your time we've
*  come to the part of the show where that i'm now calling freeze fight or flight where i will kind
*  of ask you rapid fire type questions okay so what is thomas nazolera's favorite beer oh
*  he used to be a hop head but no longer i don't know that's my response okay that's that's
*  acceptable what is it like describing what you do to family and friends who aren't familiar with it
*  it's very difficult okay that's your response
*  it's very difficult all right that's going to be the the audio clip that i'll
*  advertise this podcast for it's very difficult what's one idea that you can't do or don't have
*  time or the resources you know to do that that you wish someone else might pursue you mentioned the
*  auditory work earlier oh yeah this whole sensory thing that a lot of people do it's interesting but
*  we can study pure thought that seems interesting close your eyes and do math or recall i mean
*  people do study this i'm sure right um but yeah the i mean we well often you hear we study sensory
*  systems because we know a lot about them but that seems i mean it's practical but it's not um a
*  really good reason to study it um but a lot of what we do like this whole podcast let's use that
*  as an example what the heck did we do i mean i'm staring at you because i have a skype window open
*  and whatever but like i could have done this holding without vision so there goes vision
*  we couldn't have done this without audition that's that's true um and our motor like me talking is a
*  motor help it so um okay there's the that aspect of it the auditory sensory and the motor talking
*  but i guess the holy grail will be the thought behind this not really the overt act of making
*  sounds or interpreting the sounds that you give me it's the it's it's pure thought or cognition
*  maybe cognition is too broad term but anyway if we could somehow tap into that uh that would be
*  good and come up with models of that and then you know download your brain to a hard drive that
*  type of thing well what do you think of the idea that um thoughts you know without a motor component
*  are sort of an internalization through evolution of motor behavior does that make sense first of
*  all and if so what do you think of it seems interesting i i think you're something like
*  you don't have to say the sentence that you're thinking but you're at least building up the
*  ability to say such sentence in the future kind of storing that away in your memory banks is that a
*  fair yeah i think that's yeah that would be one way to look at it people like uh daniel wolpert and
*  rudolfo ginás talk about these things um that that really movement is the central goal of cognition
*  and that our thoughts are in a sense internalized movement i like that idea a lot i mean i actually
*  didn't uh haven't heard about this theory or idea before but i think it makes a lot of sense
*  what what's something that you've been uh really wrong about oh that's easy so way back when
*  this comes full circle yet again so the first incarnation of this image representation as
*  experiment you know this large scale we did this like 13 years ago yeah and uh way back then
*  i was thinking uh who cares about behavior who cares about task let's just make them stare let's
*  just make them stare at this white dot i think that was a huge mistake ah oh i just had john
*  kraka on he'd love to hear you say that as well yeah a huge mistake like it's unless you're the
*  point of what you're studying is what happens in kind of a default state if you ask someone to do
*  nothing although that that actually harkens to a whole other field resting state the field but um
*  but in the context of this visual experiment asking not instructing the subjects to do something
*  specific i think from a kind of experimental control point of view and from the fact that top
*  down things can affect sensory responses a lot a la e-life the e-life paper i think it was a huge
*  mistake which doesn't say the data are useless and we published on it but um but that's why in
*  this new new incarnation of the data set we are going to other extreme we're trying to within
*  limits tightly control the cognition that subjects are doing while they're looking at these things
*  and this time you're going to get it perfectly right i'm sure right well scanners are always
*  getting stronger and analytic techniques will always get better and maybe one day you can
*  convince someone to come a thousand times in the scanner but we're trying to do the best we can
*  right now a la 2019 what is one trait of our intelligence or cognition that you think will
*  be especially difficult to build into ai systems i would have to say this is my naive opinion though
*  kind of linguistic reasoning i don't even know if that's a term it's really hard to do i think in
*  general for artificial systems and i think it's extremely interesting to study that and again like
*  what we just did over the last hour there was tons of that what's something that you think will come
*  out of neuroscience or ai that someone someone might think sounds crazy so so okay what is a
*  realistic outcome that i think might happen in the future that we may be shocked by or or that when
*  if you're telling someone over beers they might think oh you're crazy you know for thinking actually
*  well not to take your time either but i do have a response but it's not about neuroscience it's
*  about artificial system great great i think one day we may realize that it may be possible to
*  create things computers and computers with bodies maybe um and we may wake up one day and have a
*  thing you know it's kind of the train test like we yeah and i think you know one day i don't know
*  the time frame for this but yeah we can create robots that seem human-like in all respects and
*  i i think we should prepare for that because it won't actually be that it may come soon and it
*  i won't be shocked if it happens in some sense so i what i'm what i'm really this is a long response
*  but what i'm trying to say is i'm not claiming we will i think it's a much dimmer prospect of
*  quote unquote understanding the brain and then incorporating all of those principles into an
*  artificial system i think that's harder i think what's more likely is through non-brain-like
*  tricks and algorithms and techniques we can create quote unquote intelligent systems that
*  will be for all intensive purposes you know as good as a human and i think once that day comes
*  it'll be almost kind of an anticlimactic event because now we're going back full circle to
*  philosophy like what's the difference between you and a robot that seems like you well i don't know
*  you're just a thing on my skype window i've never met you in real life and if you're a you know robot
*  underneath what looks like skin i guess that's okay and i can treat you ethically and i can
*  interact with you and you know as long as you don't do something crazy in return like that's
*  okay i can coexist with you i think that's a perfect place to leave it kendrick thanks for
*  all the time today and uh and going going deep with me in your models and in deep network models
*  great this is really fun and thanks for having me on
*  so
*  brain inspired is a production of me you can support the show through patreon for a trifling
*  two or four dollars per month go to patreon.com brain inspired or go to the website brain inspired
*  co and find the red patreon button there your contribution will help keep this show going
*  without any annoying advertisements like you hear on other shows to get in touch with me email paul
*  braininspired.co the music you hear is by the new year find them at the new year dot net thank you
*  for your support see you next time
*  oh
*  you
