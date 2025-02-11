---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5559s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 8156
Video Rating: None
---

# BI 098 Brian Christian: The Alignment Problem
**Brain Inspired:** [February 18, 2021](https://www.youtube.com/watch?v=-DHwFO9-cqY)
*  There's some mapping from human behavior to human desire slash values.
*  We don't really know what it is as you say our actions and our words often diverge.
*  One of the things that I take away from the history of the law is thank God it's an iterative
*  ongoing process.
*  You know, because every society looks back on the society of a century prior and thinks
*  of them as kind of moral barbarians and there's no reason to think that we've reached the
*  end of that process.
*  How many fundamental breakthroughs are needed between here and AGI versus just scaling up
*  the stuff that we have?
*  And the rough consensus answer is like...
*  This is Brain Inspired.
*  That's the sci-fi question.
*  Emphasis on the phi part of science fiction.
*  Hey guys, I'm Paul Middlebrooks.
*  Welcome to the show.
*  I am not particularly concerned with that question, but it is reasonable to ask as we
*  build better AI systems to make our lives better and easier, how would we build AI to
*  make our lives better and easier?
*  This is known as the alignment problem.
*  As Brian Christian states it...
*  The alignment problem is the problem in machine learning of whether the systems that we are
*  training by examples are really learning what we think they're learning or what we intend
*  for them to be learning and whether their behavior when we deploy those systems is going
*  to match what we had in mind or what we wanted the system to do.
*  Brian has a new book called The Alignment Problem, Machine Learning and Human Values.
*  This is his third book.
*  He wrote The Most Human Human, which is about the Turing Test competition and Brian's attempt
*  to convince people that he's human.
*  And he co-wrote Algorithms to Live By with Tom Griffiths, which Tom and I discussed back
*  on episode 56.
*  In Brian's latest book, The Alignment Problem, he lays out the issues confronting us now
*  with how to move forward if we want to build truly useful AI.
*  To do that, he relates the history of AI, many of the stories and words of the people
*  who have made and continue to make that history.
*  And he describes how modern machine learning works and how it relates to potential problems
*  and solutions for the alignment problem.
*  In this episode, we discuss how that progress is playing out, who is and who should be making
*  that progress.
*  We also discuss some of the techniques offered as solutions, like inverse reinforcement learning,
*  which is the idea of letting an AI agent infer what we're trying to do so that it can help
*  us do it.
*  So you have an AI agent that observes your behavior and does its best to form an objective
*  function that matches your desires.
*  We also talk about the dilemma of simply knowing what our own values are or what we want our
*  values to be so that the machines can help us attain those values.
*  And Brian tells many of the stories that he uses as examples throughout the book.
*  Show notes are at braininspired.co.
*  slash podcast slash 98.
*  If you value Brain Inspired, you can support it on Patreon.
*  So all the full episodes are posted through Patreon.
*  And you can also join our fledgling little Discord community where, for example, this
*  month we're discussing a talk about AI consciousness by Joshua Bengio.
*  Braininspired.co is the place to find the Patreon link.
*  Be safe out there and watch out for those killer robots.
*  I do realize that this is the moment in the movie where I get decapitated by the robots
*  that I'm making fun of.
*  I seem safe for now, at least.
*  Here's Brian.
*  Brian, I managed to create 97 podcast episodes before having to talk about AI.
*  Ethics, I say, having to talk or getting to talk about ethics in artificial intelligence.
*  So your hope that I know that you would hope that writing the book would generate more
*  conversations and inspire people to go into this field.
*  It seems to be perhaps coming true.
*  What do you think? It certainly has gone in a remarkably short time from being a sort
*  of fringe area or a kind of marginal and to some degree taboo area within computer science.
*  Itself to being one of the arguably the fastest growing part of the field.
*  And that's happened in about a five year span.
*  So it's been a very remarkable transformation of computer science itself.
*  You know, if you look at what people are writing their theses about or what sort of workshops
*  are happening at the big conferences, it's been a big transformation.
*  And that's part of the story that I wanted to tell in the book was kind of this this
*  first generation, if you will, of grad students coming up the ranks, sort of explicitly
*  focused on these questions.
*  Well, you you say it's been about five years, which I know is an approximation.
*  But do I have it correct?
*  Did you start working on the book about four years ago?
*  So if that's true, then you were really you really lived through this growth.
*  Yeah, that's that's true.
*  I mean, I I started thinking about some of these questions of, you know, safety in AI
*  going back to around 2014.
*  People like, you know, Stephen Hawking, Elon Musk were saying these things in the press.
*  There's a funny anecdote where I went to a Silicon Valley
*  investor book club and Elon Musk was there and he cornered me and, you know, made me
*  give him, you know, a good reason why we shouldn't be worried about AI safety.
*  And I was unable to provide a satisfactory response, which got me thinking about it.
*  And over the course of 2014, we started to see not just high profile people in general,
*  but people like, for example, Stuart Russell, you know, leaders within the theoretical
*  computer science community starting to come out and say, yeah, there is something here.
*  You know, we need to start thinking about this as computer scientists.
*  So that really got my attention.
*  But at that time, I was still finishing writing algorithms to live by.
*  So that was my primary bandwidth was kind of taken up by that.
*  That book came out in the spring of 2016.
*  And so I was starting to think about, you know, what was going to come next.
*  And by the summer of 2016, that's when we started to see a combination of things.
*  You know, on the one hand, you had really the beginning of this AI safety ecosystem
*  emerging. There had been the Future of Life Institute conference in Puerto Rico.
*  There was kind of an increasing focus at places like NURIPS and so forth,
*  places like Center for Human Compatible AI at Berkeley,
*  OpenAI, all getting founded in sort of the 2015, 2016 period.
*  And then you also had in the summer of 2016 an explosion of interest in the sort of FATML,
*  now rebranded to FACT, Fairness, Accountability, Transparency Community.
*  That was really kicking off.
*  You had the ProPublica article about the criminal justice risk assessment score
*  that came out in the summer of 2016.
*  So suddenly everyone's thinking about what's the proper objective function to measure
*  fairness and all these things.
*  So it really felt to me that those two those two sets of concerns,
*  the longer term technical AI safety or even the existential risk set of issues.
*  On the one hand, that was becoming increasingly grounded in an actual scientific agenda.
*  And on the other hand, you had these present day risks, these sort of ethical,
*  accountability, transparency risks that were galvanizing their own community.
*  And that community was becoming increasingly technical.
*  And so it felt like these these two sets of concerns and these two kind of responses
*  that were being mobilized in distinct but related communities were really on a collision course.
*  And so that's really what convinced me that there was a single story here that kind of
*  united those narratives together.
*  So, yeah, it was really the late summer, early fall of 2016 that I began working on the book
*  in earnest. And a lot has happened since then, as you know.
*  Yeah. Yeah. Well, in earnest, you did work on it.
*  So just to describe the book a little bit, much of it is devoted to describing the history of AI
*  with the stories of the people that have worked on it and are working on it, often in their own words,
*  which is just great.
*  Many of them have shifted from being experts just in AI, have shifted part of their focus,
*  or in some cases, a lot of their focus on working on this, this AI, the AI ethics issues.
*  And along the way, you also give that, you know, broad and sometimes pretty technically demanding.
*  I wouldn't say demanding because it well, it depends on who you are, I suppose.
*  But but descriptions of how the technology actually works.
*  And that sort of meshing of all these different elements really stood out to me.
*  But I hadn't seen someone tie in the the technicalities of the way that AI works
*  and tie that in to the ethics part.
*  So with skill, as you did.
*  So nice job there.
*  Nice job on the book.
*  I appreciate that.
*  I appreciate that.
*  Yeah. Yeah.
*  I mean, it was a major it was a major endeavor.
*  And, you know, I ended up doing something approximating a hundred formal interviews
*  and, you know, many, many hundred sort of informal conversations.
*  And it was also, you know, archival research.
*  I ended up going to the American Philosophical Institute in Philadelphia
*  and looking through Warren McCulloch's correspondence.
*  And I was working with the Bertrand Russell archives and all sorts of things.
*  And I wanted to pull together, you know, as you say, this deeply rooted historical story,
*  some of which was very surprising to me.
*  I did not know, for example, that Walter Pitts,
*  when he was working on that famous McCulloch and Pitts paper in 1942,
*  was a homeless teenager that Warren McCulloch had taken in as sort of a foster parent.
*  So there were all these little, you know, deeply human moments that jumped out of the history.
*  But as you say, also, you know, I wanted to paint a portrait of the field
*  as it stands today through the actual perspectives and words of the people on the front lines.
*  And I also, at the same time, wanted to give a kind of curriculum in machine learning
*  and in some of these open problems, because I do think, you know, there's a huge appetite for people
*  trying to get into this area, people who already have a certain technical background or,
*  you know, even people who are undergrads or high school students, you know, getting excited about
*  this. And I wanted to, you know, offer a little bit of a roadmap to that area for people who
*  want to get involved. And I also think there's a lot of room for people who self identify as
*  non-technical, who need some kind of intuition. You know, maybe you're a policymaker, maybe you
*  are a judge or something. You've been on the bench for 20 years. Now, suddenly,
*  a new regulation gets passed and now all of your, you know, arraignment hearings are being given
*  this algorithmic risk assessment score. And you're expected to have some kind of intuition about when
*  that score is more trustworthy than other times. But you've never really thought about machine
*  learning, you know, in your whole life. So I think this is becoming kind of a core part of the
*  curriculum for citizenship, you know, in the 21st century. So I think the technical grounding
*  is important. I want to come back to that actually, and just a couple minutes, you know,
*  how to actually enter in the field and who the right people are, etc. But just, I mean, just
*  before we kind of dive into the bigger issues. So much of the book is stories like you were just
*  talking about. And you excel at communicating those stories. So I have kind of a meta question
*  for you. So people like Patrick Winston have advocated that, well, in Patrick Winston's case,
*  it's called the strong story hypothesis. But there have been others that have advocated this idea
*  that storytelling itself is, you know, and understanding storytelling is central to human
*  intelligence. And I wonder how you feel about that, how important, you know, having written a book,
*  and you did this in the most human human as well, your first book, where you really embed the
*  narrative, well, the ideas within a narrative and within story, a story and many stories.
*  And that, as you know, that communicates, there's nothing like a good story that communicates ideas.
*  So I'm just curious what you think of that overall picture of storytelling as being central to
*  human intelligence. Yeah. I mean, I'm not I'm not familiar with the actual literature that you're
*  referring to. So I can't speak to a specific, you know, argument or claim there. But it must
*  feel right, though. It feels right. It feels right. I mean, I do think that, you know, narrative
*  making, there's something intrinsic to the experience of consciousness that, you know, to
*  turn experiences into a narrative and to give it a shape, give it a sense of, you know, meaning.
*  That's a big part of what brains do. And I think there's something, you know, arguably central
*  about that role in consciousness, you know, this idea of the interpreter, as some people call it.
*  I also think, I mean, as far as being a writer, someone recently said to me,
*  stories are the file system of the human brain. You know, that that is how the brain retains
*  information. And if you don't turn something into a story, your readers going to have to turn it into
*  a story themselves in order to retain it. And so you might as well do that work for them so that the
*  story they retain is the one that you intended. I think that's broadly right. And so, you know,
*  that's a big part of what I what I wanted to do in the book was not just to make an argument about
*  AI safety or something like this, but to offer people these vignettes that are hopefully both
*  more colorful, more engaging, but also stickier. And so, you know, people, people come up to me
*  years later and say, like, oh, yeah, it's the it's like that pneumonia thing, or, you know,
*  it's like this or it's like that. And I think that's a big part of what we do is we sort of
*  pattern match against these kind of prototypes. So you if you can furnish someone with these
*  prototypical stories, then their ability to recognize situations and map them back to that,
*  I think, is a really powerful asset. Yeah, I mean, even something as simple as the Walter Pitts,
*  you know, his sort of life that you describe of being homeless and then being taken in by McCulloch,
*  also being disappointed later on to learn that their logic units don't, you know, really map
*  on to what brains are actually doing. And then even to the point of becoming an alcoholic and
*  dying in his mid 40s. I don't remember the particular age, but those are those sorts of
*  things are just just for some reason make it so easy to lock in and open up. Oh, yes, that's the
*  key to like thinking about what he actually did. You know, these somewhat irrelevant things about
*  his life are somehow key to unlocking the knowledge of what he provided, you know, the knowledge that
*  he provided and things that he worked on. Just an interesting, interesting thing that you that you
*  exploit very well, sir. Alright, so thank you. Okay, so I'm going to have to, I'm going to have
*  to ask you this just just to get in. So, Brian, what is the alignment problem? The alignment problem
*  is the problem in machine learning of whether the systems that we are training by examples
*  are really learning what we think they're learning or what we intend for them to be learning
*  and whether their behavior when we deploy those systems is going to match what we had in mind or
*  what we wanted the system to do. And so that that is a fear that goes back to Norbert Wiener from
*  MIT cyberneticist, you know, in the 1960s, who articulated this very well in an essay from 1960,
*  and has more recently, I think, become an acute concern among the actual machine learning community.
*  Well, see, that's an interesting thing to me, because I guess it, you know, you kind of think of
*  ethicists as being a separate population from the people working in the trenches on the technical
*  details. But what you're saying is that, you know, these ideas about ethics and things like
*  explainability and interpretability in AI are becoming interesting in themselves to the to the
*  AI workers, or at least a subset of those. Is that really the case? Yes, certainly. I mean, with
*  interpretability and explainability, I mean, it's an interesting, to me, this is a very interesting
*  part of the field, because in part, a lot of the a lot of the scientific impetus is actually coming
*  from regulators. So you have the GDPR, which was passed in the European Union, and I think 2016,
*  it went into effect in 2018. I mean, we're still working out the actual case law. But it has this,
*  you know, so called right to an explanation. And at the time, particularly when the regulation was
*  passed, a lot of people in the field were saying, Well, wait a minute, you know, getting a
*  satisfactory explanation out of a deep neural network is, is an open scientific research problem.
*  And now you're saying this is a regulatory requirement, you know. And in particular,
*  I remember a lawyer for one of the big tech companies talking about meeting with EU regulators
*  and making this complaint. And the regulators were unmoved and said, Well, that's why the law doesn't
*  go into effect for two years, you have two years to figure it out. So, you know, get to work.
*  You know, science doesn't always work on schedule like that. But you had a similar thing was
*  happening in the United States. In the Defense Department, you had people, analysts in the
*  intelligence community, who would get these reports that would say, you know, based on
*  this convolutional net, you know, analyzing this grainy satellite photo, we're pretty sure this is
*  a, you know, ammunition depot and, you know, sign on the dotted line to strike it with some kind of,
*  you know, attack. And these people would have to actually authorize these things personally.
*  And we're saying, No, wait a minute, I don't, I don't really know what I'm signing here.
*  I don't necessarily feel comfortable with that. And so that's part of how DARPA got interested
*  in that. And so I think I mean, I think it's an interesting case study where we think of regulation
*  as, you know, typically having a purely stifling effect. But in this case, the regulatory
*  requirement was really generative for a lot of work to happen in a short period of time. But I
*  think this is, to my mind, one of the most interesting and exciting parts of the field
*  is we really are making strides into finding model architectures that are ideally interpretable and
*  explainable without sacrificing performance. And that's kind of the the holy grail.
*  I mean, do you think that it's important? Well, rather, how important do you think it is for
*  someone to understand, you know, the nuts and bolts, the technicalities of deep learning nets
*  and other AI endeavors to address the alignment problem or to work on the alignment problem? Do
*  alignment problem ethicists and workers need to be AI experts?
*  I certainly think some of them do. I don't think all of them do. I mean, I think part of the story
*  that I try to portray is that this is really going to draw on a wide range of expertise that no
*  single person has or there's no single path, you know, of training that's going to give you all of
*  those requisite skills. So I think it is going to take a little bit of everything. You know,
*  going back to this point about interpretability, I mean, part of what I think is exciting about
*  this area is that there are methods that can be developed by the people with the deeper technical
*  knowledge that enable people with less technical knowledge to still be able to understand what the
*  model seems to be doing. So I'm thinking about, you know, people like Chris Ola and some of his
*  former collaborators at OpenAI and Google Brain, you know, developing methods where
*  an image classification model, you can just show it a picture of static and say, essentially,
*  fine tune the static until it maximizes a category label. And so you can get it to
*  generate these kind of hallucinated super stimuli of, you know, what is the ultimate,
*  you know, the maximally banana-like image or the maximally dog-like image. And this is kind of
*  aesthetically fascinating. It's also a sanity check on the model and it can be used for things like
*  bias and fairness, right? So if you ask it to generate faces and all the faces are white men,
*  that tells you something might be weird. In their case, they used it to generate images of barbells
*  and all of the barbells had a disembodied muscular arm coming out of them. It looks very surreal.
*  But that tells you that the model might not generalize to barbells that are on the ground
*  or barbells that are on a rack. Now, in that particular example, it's hard to think of a high
*  stakes case of recognizing a barbell, but, you know, superimpose that onto a self-driving car,
*  not recognizing a cyclist or something like that. And it could be a real issue. And there's,
*  you know, there's a recent technique called TCav, which stands for testing with concept activation
*  vectors that was developed by Bean Kim at Google Brain. And this uses kind of high-level human
*  concepts. So under the hood, you are looking at the internal activations of a model.
*  Pete O'Loughlin The hidden units.
*  Ben Fisk Exactly. And you're trying to find patterns in the activation of the hidden units
*  when they recognize anything that a human could identify as a high-level concept. So it could be
*  a man, a coat, a car, the color red, whatever it is. And then you look at whether those hidden
*  activations are present when it makes another classification. And so you can determine the,
*  you know, to a rough approximation, the relevance of some of those more primary features to some
*  higher level classification. So you can say, you know, when it's classifying someone as a doctor,
*  how important is the white lab coat? How important is the stethoscope, etc. And if it turns out that
*  being male is very important, then you have sort of a bias issue. One of the studies that Bean Kim
*  did with some of Google's models involved fire trucks. And it turned out that in all of the
*  models she was looking at, the color red was intrinsic to something being categorized as a
*  fire truck. And this then becomes a safety issue because fire trucks are red in the US,
*  almost exclusively. But in Australia, they're white and neon yellow. So a model like that
*  probably wouldn't be safe on the streets to deploy in Australia. So I think some of those methods are,
*  you know, part of what's appealing about them is that they require technical expertise to actually
*  build, but then anyone can use them. You can say, you know, anyone can click on an image and say,
*  this is red, how important is the red in this other image, and it'll give you a score back.
*  And that's, that's useful even to someone without the technical understanding.
*  Yeah, I mean, this gets back to your, you know, saying that you wanted to sort of provide a,
*  you know, curriculum in the book. And I was actually going to ask you what would be the
*  right curriculum, you know, for someone who, you know, to get a degree in AI ethics or a degree in
*  the alignment problem, because we're, you know, we're going to go on to talk about ethics broadly
*  and human values and what that means. So there's that whole humanities side and philosophy side to
*  it. And then there's the technical side and the math side. People don't like doing all of that.
*  They kind of want to be one or the other. And maybe, maybe that's what you're saying is that
*  it's going to take a team anyway of various experts. But, you know, presumably there'll be
*  some degrees popping up in AI ethics. So maybe your book will be the first textbook.
*  Well, in some ways, you know, I would be very satisfied if that were the case. You know,
*  that's part of what I was trying to do is to lay out a rough curriculum, you know, but a curriculum
*  in the medium of storytelling largely. And I have, you know, begun to see certain universities
*  actually using this for their classes. And to me, that's immensely satisfying.
*  But I think we're going to see that we're going to see a lot more of that,
*  more of that meaning just a lot more interest broadly at in higher education
*  in trying to put some kind of curriculum together, whether that's for computer science majors
*  specifically or for philosophy majors who want to come at the material from the other side,
*  or, you know, people studying law. There's the whole intersection between the law and some of
*  these issues. So yeah. Yeah, that's interesting. I really think the team ideas. It seems like it's
*  always the right more and more the right answer these days, that you just need a broad diversity
*  of people who are deeply have deep expertise in a very certain thing, and then have enough
*  shallow expertise to go cross modal and talk with other experts. That's what seems like the answer.
*  Yeah, no, I think that's exactly right. I mean, there, there are, you know, specific case studies,
*  I could point to where having that kind of cross disciplinary team ends up being really important.
*  So for example, some of the work that's being done on de biasing word embedding models
*  involves, you know, going to actual people and saying which of these analogies
*  strikes you as an appropriate analogy versus a stereotype, you know, is man is to woman as
*  aunt is or as uncle is to aunt. Is that okay? Or is, you know, linebacker is to nurse? Is that not
*  okay? You know, like, it actually requires some methodology for extracting that information from
*  people. And you have to think very carefully about what population of people you're sampling,
*  what is the exact wording of the question, you know, so there was one team from Microsoft
*  research. And, you know, when you ask people, is this problematic, you get a different answer
*  than if you ask people, is it a stereotype versus is this prejudicial, there are these subtle
*  linguistic differences that then manifest in you get a different response to your question,
*  then you the model train slightly differently. So having a little bit of that social keying into
*  their sort of biases in their own judgments. Yeah, right. And, yeah, and it's really helpful
*  to actually work with social science, people who have experience asking these, you know,
*  wording these questions and knowing how the wording affects the response you get and
*  things like that. So in consciousness, in the consciousness literature, and if I suppose in
*  the philosophy of consciousness, there's this famous distinction between the easy and the hard
*  problem, right, where the easy problem is figuring out the neural activity that may be related or
*  underlies consciousness. And the hard problem is, is yoking that activity to our subjective
*  experience or coming up with an explanation, an explanation of what it feels like to be a bat,
*  or a human or someone. And another thing I thought about reading your book is that, you know, whether
*  to think of this in terms of an easy and hard problem for the value alignment problem as well,
*  the easy problem would be building the algorithms that function the way that we want them to function.
*  But the hard problem is knowing what to build. In other words, knowing our own values. And that
*  seems to be at the crux of perhaps an obstacle in moving forward, or at least a challenge.
*  One of the quotes you use in the book is from Roman Yampolsky. I don't know if I'm pronouncing
*  his name correctly. But he says, we as humanity do not agree on common values. And even parts we do
*  agree on change with time. And this is a, you know, this is, so this is like a fundamental issue. And
*  I had Chris Summerfield and Sam Gershman on a couple episodes ago, and, you know, they talked
*  about it. There's an anecdote. I like this anecdote about Stevie Ray Vaughan that I read in a comments
*  section, I think on YouTube. I'm not sure. I never read comments on YouTube. But anyway,
*  Stevie Ray Vaughan gave this advice to a kid learning guitar. And the kid had only realized
*  much, much later who was giving him advice. But Stevie Ray Vaughan said to him, who of course,
*  Stevie Ray Vaughan is a famous blues guitarist. He said, make sure that when you practice,
*  slow down and play accurately. Speed will come later. Otherwise, you'll just be practicing your
*  mistakes. And I wonder if that I mean, this is well, all of that is to lead up to this question,
*  I suppose. So, you know, how do we deal with this paradox that we define the values and problems for
*  AI we as humans do, whereas we get our values, they're somehow defined by the environment and
*  our need to survive. So maybe I'll just let you comment on that. Yeah, yeah, there's there's so
*  many different things there to just kind of jump off on. Yeah. I guess maybe working slightly
*  in reverse order. So starting with what you were saying at the end about evolution,
*  there is this really fascinating connection between AI alignment and evolution in exactly
*  the way that you've described, which is that there's some fitness function that comes from
*  the environment that has to do with how people actually survive, reproduce, etc. But the drives
*  that we have instilled into us by evolution have sort of a funny, non obvious relationship to
*  that fitness. You know, the actual things that people think about and care about on a day to
*  day basis are, you know, like having that second cup of coffee, or am I going to get that promotion,
*  or whatever it might be, you know, all these all these things that preoccupy us. And there's kind
*  of Yeah, this two two stage optimization, which is, you know, what what are the right drives to
*  give people such that their attempts to optimize those goals will produce this behavior that fits
*  the the higher level fitness function that comes from the environment. So this is something that
*  computer scientists like Andrew Bartow at UMass Amherst and Satinder Singh at University of
*  Michigan. There's a lot of interest in thinking about this from a reinforcement learning
*  perspective of if we want to see a certain behavior from a reinforcement learning agent,
*  we are now putting ourselves in the shoes of evolution, so to speak, what drive do we give
*  that agent what you know, utility function reward function, do we give that agent such that as it
*  starts learning in that environment, to maximize that particular reward function, we end up seeing
*  the behavior that we want to see. And the obvious answer, which is not necessarily correct, but the
*  obvious answer is just give the agent the goal, which is the thing that you really actually want.
*  And if the agent were kind of infinitely resourceful, infinitely intelligent, had infinitely
*  much time to optimize, then you really would want it to you really would want it to have the quote
*  unquote real reward function. But if it's bounded in some way, either computationally bounded or
*  bounded in lifetime or whatever it might be, then you might have to give it something else, either
*  that's kind of more learnable or whatever the case might be. And there's a totally non-obvious,
*  non-linear relationship between those things. So that's been a very fertile area where, you know,
*  things like evolutionary psychology and reinforcement learning are in dialogue.
*  And I think it also really connects deeply with this question of AI safety and, you know, what
*  what are the reward functions that we want our intelligent agents to pursue? And how do those
*  reward functions relate to the actual behavior we want to see? You know, so this is an area which
*  connects, you know, not just to the evolutionary stuff, but also to, you know, management science
*  and economics, like what are the ideal incentive structures to create in a company to get the kind
*  of behavior you want from your subordinates? Or how do you incentivize the other party in a contract
*  to do things that you want to do? And, I mean, etymologically, that that was the original
*  alignment problem. Like that's the computer science community is borrowing the term alignment from
*  the economists who have been talking about, you know, aligning values within an organization
*  or aligning incentives between two parties. So it's kind of it's a reminder that the alignment
*  problem was it was always a human problem first, and probably always always will be.
*  Forever will be.
*  Yeah, for better or worse. You know, if we and I think this is an important point, like if,
*  even if we are able to at some point in the coming century declare victory in the, you know,
*  the technical value alignment problem between the creator of a machine learning system and the
*  behavior of the system or the goals of the system, you're still left with it's kind of turtles all
*  the way down because, you know, the engineer that builds that system, they have incentives which
*  are, you know, might differ in certain ways from what their manager wants or for what that person's
*  executives want or the shareholders want. There are users that use the system that have their own,
*  you know, stake in it. And so the technical part of alignment is just one link in the chain,
*  so to speak. I think it's a critical link. But, you know, this sort of ramifies all the way through
*  society and, you know, we've been trying to develop good systems of incentives and good
*  governance, you know, for thousands of years. So I'm a little bit-
*  That's what laws are.
*  Yeah, yeah, that's well said. Yeah. And, you know, that's what political philosophy and political
*  science have been working on. And so I'm more, you know, in the short term anyway, I'm more
*  optimistic about the actual technical part, but I think it's a nice reminder that this is a
*  problem that goes just beyond the machine learning dimension.
*  I have trouble deciding any given night, like what to have for dinner, right, and what to make my
*  children. I feel so frequently out of touch with my own values. I wonder how important it is to
*  know thyself, to solve my own problems, you know, and what I value before asking it,
*  either programming my values, my quote unquote values into an AI robot, or even asking it to,
*  and we'll come onto this later, or asking it to learn my own values. And how important do you
*  think it is for us to solve this issue that we don't, there seems to be a fundamental
*  lack of understanding of our own values, even, you know, our actions speak differently than our
*  words, I don't know, 80% of the time, do as I say, not as I do, that sort of thing. I mean,
*  is that a fundamental obstacle? I think it is. Just for the sake of,
*  you know, the conversation, I'll also include the devil's advocate position, though, which is,
*  you know, the devil's advocate position would be something like, we shouldn't be that worried
*  about whether systems can solve things that we don't know what the right answer is, because,
*  for you know, it's not not any different from the status quo, you know, so people say this,
*  for example, about the trolley problem that like, why should we be worried about AI solving the
*  trolley problem if the entire point of the reason the trolley problem exists and is so discussed is
*  that people's in ethical intuitions diverge. So that's the arguably the least important thing
*  for us to care about in terms of the machine behavior is the place where we don't agree.
*  Like, surely we should make sure that the machine does what we want in the 99% of the time that we
*  can all agree on what is the right thing to do. Let's start there. And then we can worry about
*  all these corner cases where we don't even agree with each other. I think there's something to be
*  said about that. On the other hand, I broadly agree with you. I think there's a Norbert Wiener quote
*  here that sticks with me. He says, you know, there are many times in human history where the only
*  thing shielding us from the full impact of our folly was our own impotence. So if we and I mean,
*  there are machine learning analogies, I think maybe buried within that of, you know, things
*  like overfitting. We have techniques in machine learning to combat overfitting, which include
*  early stopping, you know, so just don't apply as much optimization pressure. That's a form of
*  regularization. More broadly, you know, I think there are many, many cases either
*  societally or in one's individual life where you say like, well, thank goodness, I didn't have the
*  power to get exactly what I wanted because I now realize I wanted the right, the wrong thing. Right.
*  And so I do think there's a real danger of amplifying our ability to get what we want
*  in such a way that, you know, we short circuit this process of feedback or of learning that happens,
*  or we make, you know, we make mistakes harder to recover from, etc. And so I think the way you
*  phrased your question for me was really provocative because you said something like, you know,
*  shouldn't I really go through this process of introspection before I train this AI,
*  you know, agent or whatever to infer my values and start taking actions on my behalf?
*  And I think that's a very interesting way of putting it because in the world as it exists,
*  you don't, you don't have the choice to give the okay about when that model should start being
*  built. Like YouTube has a model of what it thinks you want based on how you behave. Twitter has a
*  model, etc, etc. And that's happening now. And I think there's a huge problem in thinking about
*  some of these questions, both from an actual cognitive science perspective of, you know,
*  or behavioral economics perspective of there's some mapping from human behavior to human desire
*  slash values. We don't really know what it is. As you say, our actions and our words often diverge.
*  There was some study that crossed my timeline at some point, which I'm not going to be able to
*  cite, but it was basically just adding like one second of latency into a dialogue box about
*  resharing an article, you know, altered people's behavior, things like this, right? So that,
*  you know, if you take the kind of Kahneman thinking fast and slow approach, you know, then we have
*  this heterogeneous set of desires, the fast set of the fast agent and the slow agent are kind of
*  jostling around in our head. And, you know, a system that's doing inverse reinforcement learning
*  or whatever looking at us is going to infer different things based on which whether system
*  one or system two is in charge in that given moment. There's a lot of unsolved problems here.
*  I mean, there's a very interesting interdisciplinary conversation happening between computer science
*  and cognitive science around, you know, what's the right formal model to use for human irrationality.
*  So there's, you know, a very widely used model in a lot of systems called Boltzmann noise or
*  Boltzmann irrationality, which says, you know, humans do take action a in a given situation
*  with the probability proportional to the exponentiated reward. So it includes a little
*  bit of noisiness there. And that has become this widely used model for yes, sometimes people don't
*  do the right thing, but they do the right thing more of the time and relative to how much better
*  the right thing is than the next best thing, whatever. It's a pretty simple model. It works
*  in practice. But I think there's like a giant, you know, caution sign of like, this is just a
*  completely provisional like we this is an empty socket into which we need to plug in like a much
*  more, you know, fully articulated sense of like how the brain actually works.
*  Yeah, well, you mentioned that providing one second as a buffer, right? And that how much
*  of a difference that makes, I mean, just as another, a more chronologically longer
*  time span example. I mean, there's sage advice in the world of academia, and this applies to any
*  world where you're getting feedback authorship as well, where whenever you're getting feedback on
*  your manuscript on your paper on your on your book chapter or whatever, you read the feedback
*  immediately when you get it, and then immediately put it into a drawer and lock the drawer instead
*  of timer for like two days. And you can't look at it again until that timer goes off because
*  you need that two days for it to process to decompress to not send a pipe bomb through the
*  mail, you know, whatever. And so there are these practices that, you know, the our better, our
*  better angels would always implement, but I don't know that a robot would, for instance.
*  Yeah, and I think there's, you know, there's a lot of work to be done both in the theoretical side
*  of how do we extract from someone's, you know, fast behavior, slow behavior, you know, verbal,
*  you know, instruction, you know, they're, you know, one month later, what's their reflective,
*  you know, equilibrium of what they would have wanted to have done? How do we synthesize that
*  and integrate that into this kind of total picture of what the person's quote unquote real values are
*  right? I think that's there's a lot of really interesting work to be done there. But there's
*  also the like the practical, you know, applied business ethics of while they, you know, while
*  the theoretical community goes off and tries to work all that stuff out, you know, at a practical
*  level, what are these systems optimizing for? Do we need some kind of regulatory requirement that
*  says like, no, you must, you must, you have some kind of social obligation, or some kind of
*  fiduciary responsibility to optimize for people's reflective equilibrium, not their, you know,
*  fast twitch, you know, system one or whatever, or will will the market decide, you know, which,
*  which of those companies succeed or not? So I, there's like this long term intellectual project,
*  but there's also kind of like, there are systems out there making these inferences as we speak,
*  and, you know, we had hope, we had better hope that we don't go too far down the wrong path
*  in the meanwhile, while we're working on that, you know, the real answer out.
*  Yeah, I was gonna one of my questions to you was going to be, and is what what these sort of
*  automated systems, you know, have taught us thus far about ourselves? I mean, you know, there's
*  just like the evils of social media and appealing to our base, stereotypes, stereotypes and, and
*  instincts and that quote unquote value judgments and are, you know, how easy it is to manipulate
*  us. I'm including myself, we're all idiots, you know, when it comes to being super easy to
*  manipulate and having really tough biases to overcome. And, you know, are there examples
*  you know, and you would you talk about in the book also about, you know, the penal code essentially,
*  and using automated systems to help judges declare whether someone should be put up for
*  what is it called when you when they should be removed from jail and under probation, it is called
*  when you're up for parole, parole, yes, whether people should be paroled. Thank you. My my
*  vocabulary is escaping me. And you know, that makes me that made me think like, and I mentioned
*  earlier, like, aren't laws supposed to reflect our values? And haven't we learned about our values,
*  through the breaking of those laws and the adherence to those laws and jail time and recidivism
*  and all that, shouldn't that have been teaching us about our values all along? And I don't know
*  that it has. And maybe you have an opinion on this. And so then that leads into the this question of
*  whether, you know, automated, automated Facebook feed displays, you know, have that has that taught
*  us anything, you know, about our values? Or are we just completely blind to them? You know, I mean,
*  what do you think? Are there examples where we've actually learned something about ourselves
*  through these sorts of follies? That's a great question. I think, you know, one of the one of
*  the things that I take away from the history of the law is, thank God, it's an iterative ongoing
*  process. You know, because every society looks back on the society of a century prior and thinks
*  of them as kind of moral barbarians. And there's no reason to think that we've reached the end of
*  that process. And so this is, I think, something that's very critical in thinking about present
*  day AI systems, as well as kind of the future AGI, the sort of long term vision is just leaving the
*  door open for the ability to iterate. So one example that's, you know, more sort of a straight
*  up machine learning example. Well, I'll give you two. One is there's a tech company that will remain
*  nameless, but they released a new version of their app, and they started to notice that their ad
*  metrics were tanking. And they were trying to figure out what was going on. And to make a long
*  story short, the like, version number of the app was being fed into the ad targeting system as a
*  feature. And the model that was doing ad targeting essentially began to understand the concept of an
*  early adopter. And it said, Okay, these people that are on version 14, have like, strikingly,
*  you know, specific preferences, they're into tech products, they maybe have more money or whatever,
*  whatever, right? They're more open to trying new things, whatever it might be.
*  More likely to have that version.
*  Yeah. But that demographic attribute of people running version 14 became less true with every
*  hour that version 14 was out. And the ad targeting model was relearning, but it was always behind the
*  curve. And so for the entire duration of that rollout, it was always mistakenly thinking that
*  future users would have the same kind of properties as the existing install base. And
*  I think that's a great cautionary tale. You know, there's another one of a group of computational
*  linguists trying to reproduce a model that they'd read in a paper, and they couldn't
*  get the same accuracy of the paper. And they were trying to figure out, you know, was there
*  a bug in their code? No, was there some secret sauce that the original authors put into their
*  paper that wasn't disclosed? No, it wasn't that. It turns out that it was just these models were
*  being trained by scraping huge corpora off the web. And the things people were talking about on the
*  internet changed, you know, in the nine months or whatever since that paper was written. And the
*  model just wasn't as accurate now because now you're training on linguistic data that's kind
*  of moved on. People are using different expressions, the content is different and so forth.
*  So there are a lot of cases like that, where the accuracy of a model can erode on the scale of
*  hours in the first case or days and or, you know, months to years in the second case.
*  The Princeton computer scientist Arvind Narayanan has made this point where he said,
*  you know, we have this narrative that tech tech moves too fast for people to catch up.
*  But in some ways, it's the opposite, like think about how many Fortran and Cobalt systems there
*  are still in production doing finance and things like this. You know, imagine if some of the ML
*  systems developed in 2015 were still in production in the 2040s 2050s, like that would be terrifying.
*  So I think that's a really that's a really important point. Yeah, I mean, that's yeah,
*  I actually had to learn Fortran that tells you how old I am.
*  I was actually in college when they stopped teaching Fortran and started teaching C++
*  for the aerospace engineering program. So I guess that's a while ago. Well, so okay, so Brian, I
*  want to I'd like to go through like a couple specific examples, you know, in the book that
*  you talk about. And I have my own, you know, examples to ask you about. But I thought I'd
*  just start by asking you, I'm curious what you were surprised about that you learned about in
*  making the book or you know, that you didn't know about and were surprised about, or you know,
*  something that really changed your thinking or really directed your thinking in a new way or
*  something or, you know, because you use so many examples from the book, it's impossible to list
*  them all. So I thought I'd just ask you what you know, what some of your favorites are, etc.
*  Um, yeah, as you say, I'm sort of feel spoiled for choice. But the one that comes to the top
*  of my mind, in terms of one that both surprised me and also gave me a sense of hopefulness,
*  let's say, there was a paper a couple years ago now from it was a collaboration between
*  a group at OpenAI and a group at DeepMind. And the paper is called Deep Reinforcement
*  Learning from Human Preferences. And the idea to give a little bit of context, you know, there's
*  been a lot of progress in particular since the turn of the millennium, the early 2000s in what's
*  called inverse reinforcement learning, where rather than explicitly giving the system an objective
*  function and saying, you know, optimize your behavior against this, you sort of go the other
*  direction and you say, I'm going to provide you with a bunch of behavior. And I want you to figure
*  out what objective function I appear to be optimizing for. And then I want you to after
*  the words go and try to maximize that. This has been instrumental in a lot of areas, you know,
*  famously in the 2000s, it was Peter Abbeel and Andrew Ng at Stanford with their helicopter doing
*  all these crazy helicopter stunts. And I think particularly significant was it could do stunts
*  that were too difficult for human radio controlled helicopter pilots to do. Merely by attempting the
*  stunt, the inverse reinforcement learning system could see, okay, I understand what you're trying
*  and failing to do, I'm just going to go do that because I have, you know, I can optimize the
*  controls on this thing, you know, better than any human actually could fly it. So there were a lot of
*  signature successes in inverse reinforcement learning, but they had this requirement that
*  you had to actually provide the demonstration yourself. And so part of what was going on with
*  this paper, Deep Reinforcement Learning from Human Preferences, they were saying this demonstration
*  thing is kind of a bottleneck. Let's think about situations where we don't want to require the
*  human to actually demonstrate the behavior, we just want them to be able to recognize it.
*  So the example that they came up with was having a virtual robot performing backflips
*  in this environment called Mujoko, which some people might recognize. So the idea was, it's
*  really hard for a human to do a backflip, obviously some can, but most can't. And it also wouldn't be
*  clear how that would generalize to a, you know, a body with different morphology. It's hard to even
*  get a virtual robot to do a backflip with a, you know, game controller. It's really hard to define
*  an explicit reward function that models a backflip if you have to put in coefficients for the
*  rotational, you know, momentum and the torques on the joints and all these things. But if you saw
*  the robot doing one, you would recognize it. And so what they did was they had the robot
*  initially starts just riding around randomly and they present the user with pairs of video clips
*  and they say, which of these video clips looks, you know, epsilon more like a backflip and say,
*  okay, well, this one is like somewhat riding to the right. So that's sort of closer than the other
*  one. And there would be this kind of inverse reinforcement learning process in the background
*  saying, okay, we're being fed a series of these, you know, head to head preferential judgments.
*  You know, the user liked the left clip in this case, but the right clip in this other case,
*  we're going to build a model of what we think you think a backflip is. And then we're going to
*  provisionally start optimizing our behavior for that and then show you another pair of video clips
*  and you can again tell us which one you think was closer to the mark. And it turns out, I mean,
*  this there was nothing intuitively obvious to me or to the researchers themselves that this was
*  going to work. But after about 900 comparisons, which takes about an hour, it's somewhat tedious,
*  but it's only one hour, the robot is doing these gymnastically beautiful backflips. It's sort of
*  tucking the leg in order to spin faster the way that you know, figure skater pulls their arms in.
*  It's sticking the landing. I mean, it's there's something actually beautiful about it. And
*  I guess the reason why that example sticks with me is a I mean, it's just this very, very visible
*  success story of something that was not obvious it was going to work. The amount of feedback is
*  fairly minimal and 900 bits is not a lot of information. And, you know, the instructions
*  that the mechanical Turk workers were given was select the video clip in which better things
*  happen. That it was that vague. And that to me holds the promise that, you know, obviously,
*  we have a lot of a lot of technical work to be done to actually scale this up. But
*  the idea of just indicate which, which world has better things happening suggests,
*  at least that you could generalize this, you know, all the way to thinking about the kinds
*  of societies that we want. Yeah, that's interesting that that overlaps with an idea
*  called open endedness, at least in my head, I had Ken Stanley on who, who talks about open endedness
*  and training agents in this way. And the way that he frames it is not necessarily you so you train
*  the robot or agent, not necessarily giving it feedback about what seems better, but what seems
*  more interesting, which is a subtle difference, right? Because what seems better kind of entails
*  a goal and a value, which which then iterates and the robot ends up doing the backflip. And I'm,
*  you know, I don't know that what seems interesting would get you there, but they're at least kind of
*  similar in in spirit. Yeah, his work is very interesting to me. And there's a lot of great
*  connections between research like his and sort of cognitive science of infant play and you know,
*  how do infants play with toys and which toys they play with? Yeah, I want to kind of Yeah,
*  I want to talk about that too. Yeah. Yeah. But yeah, I mean, part of the complexity of
*  interestingness is that the I think about these things coming from a computer science perspective
*  of like, what's the method signature? And interestingness seems to require
*  us to provide the existing set of behaviors as part of the method signature, like something
*  is interesting, right? relative to the other stuff that the agent is doing versus something is good.
*  You know, yes or no. So it is more complex. And I am part of what Stanley and his collaborator,
*  Joel Lehman. Yeah, part of their work is really interesting in terms of like developing a
*  portfolio of behaviors that are distinct relative to the other behaviors in the portfolio. So that
*  there is sort of like a kind of a contingency there or complexity there. Yeah. Well, let's talk
*  about a little bit more about inverse reinforcement learning before moving on to a couple other
*  examples. Because I mean, this is that surprised me to reading the book that I didn't realize that
*  the concept of inverse reinforcement learning was as old as it is. I mean, it's not old per se,
*  but it's been a couple decades now since it was originally formulated, I suppose. And and this
*  gets to like Stuart Russell's ideas about, you know, the way to fix AI and to make make value
*  aligned AI is, is through a process like inverse reinforcement learning, where it's the agents goal
*  to infer what your your reward function and and then interact with you either cooperatively or
*  based on inferring based on your behaviors, what what you must be inferring. So anyway, that's that
*  I didn't I hadn't realized that it had been around and been worked on for so long, because
*  these days you just hear about DeepMinds and OpenAI is reinforcement learning algorithms,
*  you know, killing it in in all sorts of games. And I don't I don't know that they're using any
*  that any inverse reinforcement learning is even necessary in those in those tasks in games.
*  Yeah, no. I mean, that's part of what makes games such an attractive domain is that there is this
*  ready reward function that you can just kind of plug in. Although there have been some some very
*  interesting cautionary tales where, for example, OpenAI was training an agent to do these racing
*  games, in particular, this boat racing game called Coast Runners, and they were optimizing for in
*  game score, because it's very hard to parameterize like winning the race, because the you know, the
*  agent would need a representation of the track, what is a lap? What, you know, which are the other
*  agents? How do I know if I'm in front or behind or whatever? But you can always just tell it you have
*  4500 points, this action gave you 100 more points. Great. But it turns out that maximizing score
*  diverges in certain scenarios from actually winning the race. And so you end up just doing
*  these circles around this power up area forever while all the other you know, players pass you by.
*  So that's kind of a an alignment problem in its own right. But yeah, I mean, to your point about
*  the history of inverse reinforcement learning, it's very interesting, because, you know, the idea
*  goes back to Stuart Russell in the late 90s, I think, early 2000s late 90s. I think 98 is what
*  you cite, maybe 98. Yeah, yeah, thanks. Yeah, walking to the grocery store downhill and thinking
*  about how organisms optimize their gate, but optimize it for what do they optimize it for
*  caloric expenditure? Do they optimize it for stress on the joints? So this is, you know,
*  these are the kinds of thoughts that someone like Stuart Russell has on his way to Safeway.
*  It's like, oh, what is the objective function of the human gate? Oh, that's interesting.
*  If we knew it, then we could essentially put motion capture, the motion capture industry
*  out of business, because we would know what a realistic gate would be under all these
*  circumstances. But here it is, it's the end of the year 2021, and there's still a motion capture
*  industry. So indicates something about the complexity of the constraints that actual
*  organisms face, that we still don't really know the objective function of an animal gate,
*  which is a sober, sober note for the prospect of like, inferring all of human values,
*  suggests that we have a ways to go. Isn't it an easy answer just to look cool? Isn't that why
*  people try to look cool when they walk to attract mates? That's why I look so cool when I walk
*  downhill. Right. So yes, the same open AI deep mind team that did the backflips could could have an
*  agent that walks in a cool way. Right. We could discern what is your what's your platonic form
*  of cool walk? We could extract that. Objectively cool. Yeah. Yes. Yeah, exactly. Two things. One,
*  do you feel like we're just at the very beginning? How far do we have just in a very broad speculative
*  guess? How far until these things are solved? That's a very good question.
*  We'll come. Well, I'll let that stew. We'll come back to it at the end. I'll ask it. Sure. Okay.
*  I also wanted to ask you just quickly before we move on about the most human human book,
*  because you just mentioned TPT-3 and all of the interesting language models that have come. And
*  now your book is like a dinosaur. I'm just kidding. It's actually, it's still really valuable.
*  And I only read it fairly recently within last year and really enjoyed it for many of the same
*  reasons. But it really, you know, it's interesting because it takes you all the way through, you know,
*  to where you were, you know, from the history of language, you know, learning and the Turing test
*  and, you know, to when you're winning awards, pretending to be the best human, for instance.
*  And I'm just curious how you reflect now on that book, thinking about all that's happened since then,
*  and, you know, your kind of overall thought about that. That's a great question, right? So
*  the most human human describes a set of events that took place in late 2009. And the book itself
*  was published in early 2011. And yeah, to put that into perspective, I mean, to your, yeah,
*  it feels Jurassic because the spring of 2011 was six months before Siri, you know, became a thing
*  in the iPhone 4S, let alone, you know, Alexa, etc, etc, etc, let alone write giant transformer
*  networks that we have now. So in some ways, I think the book in a way had the misfortune of being
*  too far ahead of its time in terms of these questions of what is the end game of the Turing
*  test, right? What does it mean to inhabit an online world or a digital world where we really
*  don't know who or what we're dealing with? I think that was starting to become a question in,
*  you know, the early 2010s, but is now I think we're really bracing ourselves that I, for one,
*  am very curious and uncertain how online discourse withstands the impact of something like,
*  you know, GPT like models that can produce reasonable human statements with some kind
*  of valence with some kind of agenda at, you know, context specific statements that push a particular,
*  you know, attitude or worldview or propositional content at scale. I don't know what that's going
*  to do to, you know, civic discourse, like how does Twitter, how does Reddit survive that?
*  I think that's going to be a really interesting question.
*  – Well, are you pessimistic or optimistic? Or just mutual? You don't have to...
*  – I feel short-term pessimistic. I mean, it may be that... I really don't know, to be honest with
*  you. You know, I don't know if we're going to require some kind of cryptographic solution where,
*  you know, we need public figures' PGP key or something like this in order to determine that
*  this tweet really was written by them or what. I don't know. Something like there's the kind
*  of purely technical solution. There's a world in which everyone just feels super skeptical of online
*  discourse and we really only trust people face to face. And so then the world starts to look like
*  it looked, you know, in the 19th century or something. I don't really know. It feels
*  very uncertain to me. – I feel the same way, yeah.
*  – Yeah. Yeah, it's... There are so many reasons to feel sad that Turing didn't live longer
*  because I think we could really use the voice and perspective of someone like that now.
*  You know, the Turing test has gone from this thought experiment to being, you know, at the
*  point where I wrote The Most Human Human, it had become this hassle of online life that, you know,
*  you get these spam texts, you know, or spam email from your partners saying,
*  hey, click this link. I need your social security number or something. And you're like,
*  that's not how my partner talks. That's not how they write or whatever. And, you know, by the late
*  2010s, this was a matter of kind of existential threat to democracy of, you know, foreign
*  governments influencing, you know, political speech at scale. So I suspect that Turing would
*  have been stunned at the stakes, how high the stakes would be for thinking about some of these
*  questions. Yeah, and I'm honestly as curious as anyone, you know, what comes next.
*  – Norbert Wiener would not be stunned, I guess. This is the kind of thing he forewarned about.
*  – Yes. Yes. – But let's talk about... I know we're kind of running out of time here,
*  and there's just so many different examples. And I encourage people to just get the book and
*  read it because there are so many different facets to think about. One of the ones that you mentioned
*  a few minutes ago is that you think has a lot of promise is, you know, the study of the cognitive
*  science of children and infants and what they know and how they learn and how they go about developing.
*  I recently had Alison Gopnik on the show. We talked a lot about her work, you know, on
*  exploration and a little bit about how children build these abstract causal generative models of
*  the world and a little bit about how they learn through imitation. And, you know, you talk about
*  all this stuff also in the book. So I think it's in the section on unknown unknowns is when you
*  start or at least go into a little bit of depth about the cognitive science of infants.
*  And maybe I can just let you... I'll just give that to you to set up like what are unknown
*  unknowns, the famous Donald Rundsfeld phrase, and then what does the cognitive science of
*  children have to do with helping that along? – Yeah. Well, there's a number of places in the
*  book where, I mean, even Alison's research specifically comes up. So if I take this in a
*  direction that's different than what you have in mind, then feel free to redirect me. But
*  I think one of the places where developmental psychology comes in very explicitly into machine
*  learning is this idea of learning from sparse rewards. So there are certain Atari games,
*  for example, Montezuma's Revenge is one that are famously impossible for traditional RL algorithms
*  to master because the environment just doesn't give you very much feedback. You have to do
*  this huge string of tasks before you're presented with the very first hundred points in the game,
*  for example. And so how does any traditional RL algorithm that's using, you know, epsilon greedy
*  exploration or just kind of random button mashing, how are you ever going to string
*  together the correct sequence of actions to get the very first reward and even know that you're
*  on the right track? So this has been an outstanding challenge in machine learning. And computer
*  scientists, people like Mark Bellemare at Google Brain and Mila in Montreal, people like Deepak
*  Pathak at Carnegie Mellon, people at UC Berkeley are turning to these ideas that are coming out of
*  cognitive science of formal models for kind of self-directed play from infants. And people like
*  Alison Gopnik at Berkeley, people like Laura Schultz at MIT have done a lot of really interesting
*  work showing that, you know, children are very motivated by novelty. So if they see something
*  they've never seen before, that there's something intrinsically rewarding or intrinsically motivating
*  about that. If they take an action whose outcome is surprising, there's something kind of delightful
*  and motivating about that. And the computer science community, the machine learning community,
*  has kind of imported some of these ideas wholesale and said, okay, let's have this agent in a video
*  game environment and, you know, to up the ante a little bit, we'll just unplug the actual in-game
*  score altogether and just have this agent take actions with the reward function being, you know,
*  if I see something on screen that's kind of weird or unusual, that's cool. Let me treat that as
*  rewarding. If I do something and I don't anticipate what the outcome will be, let's treat that as
*  rewarding and we want to do more of those things. And it turns out in many cases that what you get
*  looks an awful lot like human play. And in fact, even just measured by pure in-game progress,
*  these methods are able to succeed in environments where kind of traditional
*  Epsilon greedy exploration cannot. And so, I mean, to me, that is one of the coolest areas of the
*  field because we are now confronting problems that are so kind of humanly recognizable that the best
*  place to turn for insights is developmental cognitive science. And when you plug their formal
*  models for exploration and play into these, you know, deep Q networks or whatever, these RL agents,
*  you're suddenly able to solve the problem. And then that in turn gives this kind of formal
*  model of behavior that can go back over to the psychology and cognitive science community and
*  offer them some new ideas. So, I mean, to me, that's one of the really exciting things about
*  the progress of AI is that we really are starting to see, you know, as these agents become more
*  human-like, you know, in certain ways, there is an opportunity for that dialogue to happen on both
*  sides, right? We take what we know about humans and make actual progress in ML and vice versa,
*  we can take these formal models from ML and learn something about ourselves and what motivates us
*  and how we learn. To me, I think that's thrilling. Yeah, yeah, I agree. I mean,
*  you mentioned Laura Schultz and one of the things she's sort of taken it a step further, I suppose,
*  and proposed that, you know, she's observed, you know, and we all know that children will invent
*  their own problems to solve, right? So, I mean, that's like extreme exploration, right, too.
*  And they'll invent their own rewards, fake rewards, and incur their own fake costs,
*  right, punishments within this made-up world where they invent the problem that they're trying to
*  solve. And Laura and her colleagues see this as a potential way that children explore what they
*  don't know, they don't know. By solving these made-up problems, they're actually inventing
*  ways that they will later use to these sort of novel solutions as, you know, something to
*  fall back on when they become adults or when they're growing up, and they need novel solutions to
*  problems that they don't understand. So, they're actually generating unknown solutions to unknown
*  unknowns almost by creating these worlds. It's pretty fascinating and that goes into the
*  exploration in machine learning literature as well. Yeah, absolutely. And, you know, there are
*  people like Jürgen Schmidhuber has this idea that he calls power play where, you know, these
*  agents are essentially, you know, finding their own objectives that are interesting in the
*  environment. And Ken Stanley also, I mean, he's done some work on, you know, developing this set of,
*  you know, this kind of portfolio of behaviors that have some interestingness or some kind of
*  diversity relevant with respect to one another. Then when you put that, you kind of pre-train
*  the agent on, you know, just developing a diverse portfolio of behaviors, then you put them in a
*  novel environment with a particular task and, you know, they can draw on one of those things
*  in order to solve that task more efficiently. So, I think that all kind of points back to a
*  similar story. Exciting times, I think. I completely agree. So, I mean, we didn't,
*  we just scratched the surface. I mean, there's a ton of other stuff to get to in the book,
*  obviously, like I said. I want to wrap up with maybe just a broad, I mean, so I'll quote you
*  from the book here. So, we are in danger. So, we've talked a little about robots and agents,
*  and we haven't really talked so much about what you, in this quote I'm about to read,
*  see as maybe even more critical. Quote, we are in danger of losing control of the world,
*  not to AI or to machines as such, but to models, to formal, often numerical specifications for what
*  exists and for what we want. So, I'll just ask you to unpack that. And then just a question on
*  top of that, you know, in all your hundreds of interviews and conversations, how would you
*  summarize the overall feeling that people have with regard to how much they worry about these
*  sort of issues that we've been talking about? Yeah. So, I mean, this quote, you know, the idea
*  of models, right? The book opens with three epigraphs that are about models. You know,
*  Peter Norvig recounting a conversation with someone who was on at NASA working on a Mars landing,
*  and they said, you know, our job was not to land on Mars, it was to land on the formal model of
*  Mars that we'd been given by this other team. We have Rod Brooks saying, you know, the world is
*  its own best model, and then the statistician, George Box reminding us all models are wrong.
*  And I think that's those epigraphs kind of hang over the whole book, because it's important to
*  think about the modeling assumptions that get made in any domain. And, you know, the other
*  epigraph that really rings through for me on this theme is Hannah Arendt saying that, you know,
*  the trouble with behaviorism is not that it's false, but that it could become true.
*  Yeah. And so, you know, to ground this in a real example of what am I talking about? I mean,
*  there are a lot of cases where we make certain modeling assumptions and the world itself actually
*  comes to conform to those modeling assumptions. You know, there are certain examples like there's
*  a book called An Engine, Not a Camera that's about financial models and showing how things like,
*  if I'm remembering this correctly, like the Black-Scholes was meant to predict option pricing,
*  but then it became the kind of standard way for pricing options, things like that.
*  In the quote of mine that you read, there's a bit of a sinister cast. And to help explain what I
*  mean by that, I think about, for example, the self-driving Uber in Tampa, Arizona in 2018 that
*  killed the pedestrian Elaine Hertzberg as she was crossing the street. I read the National
*  Transportation Safety Board analysis of that accident. And there were a couple of things.
*  I mean, there were many, many intersecting factors. We could probably talk for 30 minutes or more
*  about that one accident. But one of the things that was contributing to it was that the model
*  did not anticipate jaywalking. The examples of pedestrians that existed in its training set were
*  marked zebra stripe crosswalks. They were at intersections. They were at stop signs.
*  And so the idea that someone could be found in the middle of a street just crossing the street was
*  kind of not in the world view. It was not in this paradigm of the car. And the other
*  thing that was going on with the car was that, like most computer vision systems,
*  it was trained using these labeled examples that had specific categories. So something was either
*  a cyclist or a pedestrian or a vehicle or an inanimate object. This idea that this set of
*  categories is both mutually exclusive and exhaustive, that is kind of almost a metaphysical
*  or ontological assumption. And falsity.
*  Kind of implicitly. And false, right. And it's sort of implicitly baked into
*  most computer vision systems. And in this case, this woman was walking a bicycle across the street.
*  And so the model said, OK, I see the frame of the bike. I see the tires. See the handlebars.
*  That's a cyclist. No, there's no rider on top of it. The woman's feet are on the ground.
*  She must be a pedestrian. And it was kind of flickering between these two categories
*  like tens of times per second. And due to a set of other bugs in the code, every time it changed
*  the category, it would recompute the trajectory. So it was constantly losing its prediction of
*  where she was going to be in the future. But this idea of modeling assumptions that
*  are false but they can become true, there's a certain sinister way of thinking about a
*  model like this, which is that in a world where jaywalkers get killed, the assumption that jaywalkers
*  don't exist becomes true. It becomes true over time. In a world where you're either a pedestrian
*  or a cyclist or you get killed, then again, these false assumptions, the world comes to resemble
*  the simplified model.
*  You're going to stop jaywalking.
*  Yeah. And I think that's the kind of thing we really have to be on guard for. And there are
*  computer scientists working on it. There's something called the open category problem
*  that Tom Dietrich at Oregon, his collaborators working on. There are calibrated Bayesian
*  uncertainties. People like Yaron Gahl, Zubin Garamani are working on. There's some theoretical
*  work here, but I think there's this underlying point, which is that we don't want to mistake
*  the map for the territory. And that is broadly speaking, I think, one of the dangers of
*  machine learning in general is that you make certain modeling assumptions going in,
*  but then once that model enters into the environment, it could enforce the limits of its
*  own understanding on that environment.
*  That's the whole reinforcement learning challenge is that by acting in the world,
*  you change the world. And exactly right. So your actions are dependent on your
*  objective function. Your reward function is dependent on your own actions. And so there's
*  this cyclic thing.
*  Yeah. So there are computer scientists like Scott Garbrandt at the Machine Intelligence
*  Research Institute working on this model that they call embedded agency, which is how does an
*  RL agent countenance the fact that it itself is part of the environment that it's trying to model,
*  which will become the more powerful these models get, the more impactful their behavior,
*  the more important it will be that they have some notion of themselves as being in that
*  environment. So yeah, there's a lot of theoretical work, but I think this is something we can't lose
*  sight of. And the quote I keep coming back to is from Hamlet, of all places, which is,
*  there are more things in heaven and earth Horatio than are dreamt of in your philosophy.
*  Making something like that into our models, I think is an important step.
*  Yeah. Lastly here, well, two things, just to go back to the question I asked before,
*  through all your interviews and interactions with people, do you have a sense of how worried people
*  are about these issues? I mean, it's come to the fore now, but do people see, are people pessimistic,
*  optimistic? How big a deal do you feel is in the zeitgeist?
*  Opinions differ. So you get a little bit of everything, as you might imagine. I would say
*  broadly, there are people who think we're just not going to get to human level AI anytime soon.
*  This century, for example, it's just not going to happen. And therefore this is a bunch of
*  misplaced worry. There are people in what I would deem the slow takeoff camp that are saying,
*  oh no, we're certainly getting there, but it's going to be a kind of a boil the frog thing.
*  The universe will just start feeling weirder and weirder and gradually will realize like,
*  oh yeah, AGI is a thing. It's kind of crept up on us. There's the hard takeoff people
*  who think that the transition will happen abruptly enough to essentially blindside
*  society and suddenly we'll find ourselves in just an radically altered world.
*  So I would personally identify with the slow takeoff group. I think I haven't heard a single
*  convincing argument for why something like AGI can't or won't happen. I mean, I'm open to such
*  arguments existing, but I haven't heard any. But I don't particularly find the hard takeoff scenario
*  plausible. That being said, the actual impact of such a thing happening would be so great.
*  Catastrophe.
*  That it would be irresponsible not to have like at least 50 people thinking about it,
*  which is about how many people are thinking about it right now. I don't think that's too many.
*  Yeah, right. That's due to Nick Bostrom's book alone probably.
*  Yeah. Yeah. And groups like Miri have been thinking about this for a long time,
*  Nick himself has, and I'm glad they are. I don't see those outcomes as the most likely,
*  but we could probably spare a few more brains on that problem just given its kind of expected
*  value if it does happen. But my personal view, I mean, I think there has been an interesting
*  breaking of taboo where even the phrase AGI was very rare in my social circles
*  until about 2014, 2015. And now you see it used in a pretty nonchalant way by companies like OpenAI
*  and DeepMind. If you just look at their job listings page, they're like, we're trying to
*  build AGI, we're well on our way, join the effort. And it's just part of how these companies identify.
*  So yeah, I mean, I think the prospect of something like a kind of a general human
*  level intelligence I think is becoming a little bit more a part of people's
*  implicit or explicit projection for what the rest of the century is going to look like.
*  Certainly, I get a little bit of that spooky feeling when I interact with GBT-3. And
*  there's this question that has come up at some of the workshops and seminars that I've been a part of,
*  which is how many fundamental breakthroughs are needed between here and AGI versus just scaling up
*  the stuff that we have? And the rough consensus answer, now this is among people who are certain,
*  have a certain sympathy to AI safety consideration, but the consensus answer is like zero to two.
*  We're like zero to two fundamental breakthroughs away. And yeah, I'm hearing fewer people
*  say it's more than that. So that's a timeline thing, but that's maybe somewhat different from
*  this question of like, what's the vibe? Are people freaked out? Are they excited?
*  I'm seeing, this is just my particular vantage. And yeah, granted, I've met a lot of these people
*  and interviewed them, but I'm seeing a little bit of a tightening of the distribution where
*  I think there are fewer people saying, we're going to wake up one morning and everything we
*  know about the world is going to be different. I think there's less evidence that things are
*  going in that direction from my perspective and from the people who I know. There's also less
*  evidence for like, we don't have to worry about this, this is silliness. I think, and in some ways,
*  that's part of the story that the book tells is that the probability mass is starting to accumulate
*  around this sense of like, this is a real thing. We need to be thinking about it. But if we get our
*  ducks in a row, then we can kind of meet the challenge. And we're seeing that effort start
*  to happen. So is it enough? Is it fast enough? I think that's an open question. And that should
*  leave someone a little bit worried. I certainly see it as one of the great scientific priorities
*  of the decade. And part of my hope is that the book can be a kind of beacon for attracting people
*  to that area. And I think the more people who come, the better off we'll be.
*  Well, the book ends off where we are now basically. So with these beginnings and some promising
*  avenues, I've enjoyed your work quite a bit. Nice job. Thanks. Thanks for the material. Thanks for
*  the lessons and the education and keep it up. Thank you very much. It's been my pleasure.
*  Brain inspired is a production of me and you. I don't do advertisements. You can support the
*  show through Patreon for a trifling amount and get access to the full versions of all the episodes
*  plus bonus episodes that focus on the show. And if you're interested in the show, you can
*  click on the link in the description below. And if you're interested in the show, you can click on
*  the link in the description below. And if you're interested in the show, you can click on the link
*  in the description below.
