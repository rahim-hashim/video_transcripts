---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 4151s
Video Keywords: []
Video Views: 20435
Video Rating: None
---

# Gavin Miller: Adobe Research | Lex Fridman Podcast #23
**Lex Fridman:** [June 10, 2019](https://www.youtube.com/watch?v=q0mokx-iiws)
*  The following is a conversation with Gavin Miller.
*  He's the head of Adobe Research.
*  Adobe has empowered artists, designers, and creative minds from all professions,
*  working in the digital medium for over 30 years with software such as Photoshop, Illustrator,
*  Premiere, After Effects, InDesign, Audition, software that work with images, video, and audio.
*  Adobe Research is working to define the future evolution of these products in a way
*  makes the life of creatives easier, automates the tedious tasks, and gives more and more time
*  to operate in the idea space instead of pixel space.
*  This is where the cutting edge deep learning methods of the past decade can really shine
*  more than perhaps any other application.
*  Gavin is the embodiment of combining tech and creativity.
*  Outside of Adobe Research, he writes poetry and builds robots,
*  both things that are near and dear to my heart as well.
*  This conversation is part of the Artificial Intelligence Podcast.
*  If you enjoy it, subscribe on YouTube,
*  iTunes, or simply connect with me on Twitter at Lux Friedman, spelled F-R-I-D.
*  And now, here's my conversation with Gavin Miller.
*  You're head of Adobe Research, leading a lot of innovative efforts in applications of AI,
*  creating images, video, audio, language, but you're also yourself an artist,
*  a poet, a writer, and even a roboticist.
*  So while I promise to everyone listening that I will not spend the entire time we have together
*  reading your poetry, which I love, I have to sprinkle it in at least a little bit.
*  So some of them are pretty deep and profound and some are light and silly.
*  Let's start with a few lines from the silly variety.
*  You write in Je n'ai vinaigrette rien, a poem that beautifully parodies both
*  Edith Piaf's Je n'ai vinaigrette rien and My Way by Frank Sinatra.
*  So it opens with, and now dessert is near.
*  It's time to pay the final total.
*  I've tried to slim all year, but my diets have been anecdotal.
*  So where does that love for poetry come from for you?
*  And if we dissect your mind, how does it all fit together in the bigger puzzle of Dr. Gavin Miller?
*  Interesting you chose that one.
*  That was a poem I wrote when I'd been to my doctor and he said,
*  you really need to lose some weight and go on a diet.
*  And whilst the rational part of my brain wanted to do that,
*  the irrational part of my brain was protesting and sort of embraced the opposite idea.
*  I regret nothing hence.
*  Yes, exactly.
*  Taken to an extreme, I thought it would be funny.
*  Obviously it's a serious topic for some people.
*  But I think for me, I've always been interested in writing since I was in high school,
*  as well as doing technology and invention.
*  And sometimes there are parallel strands in your life that carry on.
*  And one is more about your private life and one's more about your technological career.
*  And then at sort of happy moments along the way,
*  sometimes the two things touch, one idea informs the other.
*  And we can talk about that as we go.
*  Do you think your writing, the art, the poetry contribute indirectly
*  or directly to your research, to your work in Adobe?
*  Well, sometimes it does if I say imagine a future in the science fiction kind of way.
*  And then once it exists on paper, I think, well, why shouldn't I just build that?
*  There was an example where when realistic voice synthesis first started in the 90s at Apple,
*  where I worked in research, it was done by a friend of mine.
*  I sort of sat down and started writing a poem, which each line I would enter into the voice
*  synthesizer and see how it sounded and sort of wrote it for that voice.
*  And at the time, the agents weren't very sophisticated,
*  so they'd sort of add random intonation.
*  And I kind of made up the poem to sort of match the tone of the voice.
*  And it sounded slightly sad and depressed.
*  So I pretended it was a poem written by an intelligent agent,
*  sort of telling the user to go home and leave them alone.
*  But at the same time, they were lonely and wanted to have company and learn from what
*  the user was saying.
*  And at the time, it was way beyond anything that AI could possibly do.
*  But since then, it's becoming more within the bounds of possibility.
*  And then at the same time, I had a project at home where I did sort of a smart home.
*  This was probably 93, 94.
*  And I had the talking voice that reminded me when I walked in the door of what things I had to do.
*  I had buttons on my washing machine because I was a bachelor and I'd leave the clothes in there for
*  three days and they'd go moldy.
*  So as I got up in the morning, it would say, don't forget the washing and so on.
*  I made photographic photo albums that use light sensors to know which page you were looking at,
*  would send that over wireless radio to the agent who would then play sounds that match the image
*  you were looking at in the book.
*  So I was kind of in love with this idea of magical realism and whether it was possible to do that
*  with technology.
*  So that was a case where the sort of the agent sort of intrigued me from a literary point of view
*  and became a personality.
*  I think more recently, I've also written plays and when plays you write dialogue and obviously
*  you write a fixed set of dialogue that follows a linear narrative.
*  But with modern agents, as you design a personality or a capability for conversation,
*  you're sort of thinking of, I kind of have imaginary dialogue in my head and then I think,
*  what would it take not only to have that be real, but for it to really know what it's talking about?
*  So it's easy to fall into the uncanny valley with AI where it says something it doesn't really
*  understand, but it sounds good to the person.
*  But you rapidly realize that it's kind of just stimulus response.
*  It doesn't really have real world knowledge about the thing it's describing.
*  And so when you get to that point, it really needs to have multiple ways of talking about
*  the same concept.
*  So it sounds as though it really understands it.
*  Now, what really understanding means is in the eye of the beholder, right?
*  But if it only has one way of referring to something, it feels like it's a canned response.
*  But if it can reason about it or you can go at it from multiple angles and give a similar kind
*  of response that people would then it starts to seem more like there's something there that's
*  sentient.
*  You can say the same thing multiple things from different perspectives.
*  I mean, with the automatic image captioning that I've seen the work that you're doing,
*  there's elements of that, right?
*  Being able to generate different kinds of.
*  Right.
*  So one in my team, there's a lot of work on turning a medium from one form to another,
*  whether it's auto tagging imagery or making up full sentences about what's in the image,
*  then changing the sentence, finding another image that matches the new sentence or vice versa.
*  And in the modern world of GANs, you sort of give it a description and it synthesizes an asset that
*  matches the description.
*  So I've sort of gone on a journey.
*  My early days in my career were about 3D computer graphics, the sort of pioneering work sort of
*  before movies had special effects done with 3D graphics and sort of rode that revolution.
*  And that was very much like the Renaissance where people would model light and color and
*  shape and everything.
*  And now we're kind of in another wave where it's more impressionistic and it's sort of the idea of
*  something can be used to generate an image directly, which is sort of the new frontier in
*  computer image generation using AI algorithms.
*  So the creative process is more in the space of ideas or becoming more in the space of ideas
*  versus in the raw pixels.
*  Well, it's interesting.
*  It depends.
*  I think at Adobe, we really want to span the entire range from really, really good
*  what you might call low level tools by low level as close to say analog workflows as possible.
*  So what we do there is we make up systems that do really realistic oil paint and watercolor
*  simulation.
*  So if you want every bristle to behave as it would in the real world and leave a beautiful
*  analog trail of water and then flow after you've made the brush stroke, you can do that.
*  And that's really important for people who want to create something really expressive or really
*  novel because they have complete control.
*  And then a certain other tasks become automated.
*  It frees the artists up to focus on the inspiration and less of the perspiration.
*  So thinking about different ideas, obviously.
*  Once you finish the design, there's a lot of work to say, do it for all the different aspect ratio
*  of phones or websites and so on.
*  And that used to take up an awful lot of time for artists.
*  It still does for many, what we call content velocity.
*  And one of the targets of AI is actually to reason about from the first example of what
*  are the likely intent for these other formats.
*  Maybe if you change the language to German and the words are longer, how do you reflow
*  everything so that it looks nicely autistic in that way?
*  And so the person can focus on the really creative bit in the middle, which is what is the look and
*  style and feel and what's the message and what's the story and the human element.
*  So I think creativity is changing.
*  So that's one way in which we're trying to just make it easier and faster and cheaper to do so that
*  there can be more of it, more demand, because it's less expensive.
*  So everyone wants beautiful artwork for everything from a school website to Hollywood movie.
*  On the other side, as some of these things have automatic versions of them, people will
*  possibly change role from being the hands-on artisan to being either the art director or the
*  conceptual artist.
*  And then the computer will be a partner to help create polished examples of the idea
*  that they're exploring.
*  Let's talk about Adobe products, first of all, AI and Adobe products.
*  Just so you know where I'm coming from, I'm a huge fan of Photoshop for images, Premiere
*  for video, Audition for audio.
*  I'll probably use Photoshop to create the thumbnail for this video, Premiere to edit the video,
*  Audition to do the audio.
*  That said, everything I do is really manually and I set up, I use this old school Kinesis
*  keyboard and I have Auto Hotkey that just, it's really about optimizing the flow of just
*  making sure there's as few clicks as possible.
*  So just being extremely efficient, something you started to speak to.
*  So before we get into the fun, awesome deep learning things, where does AI, if you could
*  speak a little more to it, AI or just automation in general, do you see in the coming months
*  and years or in general, prior in 2018, fitting into making the life, the low-level pixel work
*  flow easier?
*  Yeah, that's a great question.
*  So we have a very rich array of algorithms already in Photoshop, just classical procedural
*  algorithms as well as ones based on data.
*  In some cases, they end up with a large number of sliders and degrees of freedom.
*  So one way in which AI can help is just an auto button, which comes up with default settings
*  based on the content itself rather than default values for the tool.
*  At that point, you then start tweaking.
*  So that's a very kind of make life easier for people
*  whilst making use of common sense from other example images.
*  So like smart defaults.
*  Smart defaults, absolutely.
*  Another one is something we've spent a lot of work over the last 20 years I've been at
*  Adobe or 19 thinking about selection, for instance, where with quick select, you would
*  look at colour boundaries and figure out how to sort of flood fill into regions that you
*  thought were physically connected in the real world.
*  But that algorithm had no visual common sense about what a cat looks like or a dog.
*  It would just do it based on rules of thumb, which were applied to graph theory.
*  And it was a big improvement over the previous work where you had sort of almost click everything
*  by hand or if it just did similar colours, it would do little tiny regions that wouldn't
*  be connected.
*  But in the future, using neural nets to actually do a great job with, say, a single click or even
*  in the case of well-known categories like people or animals, no click where you just say,
*  select the object and it just knows the dominant object is a person in the middle of the photograph.
*  Those kinds of things are really valuable if they can be robust enough to give you good quality
*  results or they can be a great start for like tweaking it.
*  So, for example, background removal.
*  One thing, in a thumbnail, I'll take a picture of you right now and essentially remove the
*  background behind you.
*  And I want to make that as easy as possible.
*  You don't have flowing hair like Rich.
*  At the moment, yes.
*  Rich sort of.
*  I had it in the past.
*  It may come again in the future, but for now.
*  So that sometimes makes it a little more challenging to remove the background.
*  How difficult do you think is that problem for AI for basically making the quick selection
*  tool smarter and smarter and smarter?
*  Well, we have a lot of research on that already.
*  If you want a sort of quick, cheap and cheerful look, I'm pretending I'm in Hawaii, but it's
*  sort of a joke, then you don't need perfect boundaries.
*  And you can do that today with a single click with the algorithms we have.
*  We have other algorithms where with a little bit more guidance on the boundaries, like you
*  might need to touch it up a little bit.
*  We have other algorithms that can pull a nice matte from a crude selection.
*  So we have combinations of tools that can do all of that.
*  And at our recent Max conference at OB Max, we demonstrated how very quickly, just by
*  drawing a simple polygon around the object of interest, we could not only do it for a
*  single still, but we could pull a matte, well, pull at least a selection mask from a moving
*  target, like a person dancing in front of a brick wall or something.
*  And so it's going from hours to a few seconds for workflows that are really nice.
*  And then you might go in and touch up a little.
*  So that's a really interesting question.
*  You mentioned the word robust.
*  There's like a journey for an idea, right?
*  And what you presented probably at Max has elements of just sort of inspires the concept.
*  It can work pretty well in a majority of cases.
*  But how do you make something that works?
*  Well, in majority of cases, how do you make something that works?
*  Maybe in all cases or becomes a robust tool?
*  There are a couple of things.
*  So that really touches on the difference between academic research and industrial research.
*  So in academic research, it's really about who's the person to have the great new idea that
*  shows promise.
*  And we certainly love to be those people too.
*  But we have sort of two forms of publishing.
*  One is academic peer review, which we do a lot of, and we have great success there as much as
*  some universities.
*  But then we also have shipping, which is a different type of peer.
*  And then we get customer review as well as product critics.
*  And that might be a case where it's not about being perfect every single time, but perfect
*  enough of the time, plus a mechanism to intervene and recover where you do have mistakes.
*  So we have the luxury of very talented customers.
*  We don't want them to be overly taxed doing it every time.
*  But if they can go in and just take it from 99 to 100 with the touch of a mouse or something,
*  then for the professional end, that's something that we definitely want to support as well.
*  And for them, it went from having to do that tedious task all the time to much less often.
*  So I think that gives us an out.
*  If it had to be 100% automatic all the time, then that would delay the time at which we
*  could get to market.
*  So on that thread, maybe you can untangle something.
*  Again, I'm sort of just speaking to my own experience.
*  Yeah, that's fine.
*  Maybe that is the most useful idea.
*  Absolutely.
*  So I think Photoshop, as an example, or Premiere, has a lot of amazing features that I haven't
*  touched.
*  And so what's the, in terms of AI, helping make my life or the life of creatives easier?
*  How this collaboration between human and machine, how do you learn to collaborate better?
*  How do you learn the new algorithms?
*  Is it something that where you have to watch tutorials and you have to watch videos and
*  so on?
*  Or do you ever think, do you think about the experience itself, the exploration, being
*  the teacher?
*  We absolutely do.
*  So we, I'm glad that you brought this up.
*  We sort of think about two things.
*  One is helping the person in the moment to do the task that they need to do.
*  But the other is thinking more holistically about their journey, learning a tool.
*  And when it's like, think of it as Adobe University, where you use the tool long enough,
*  you become an expert.
*  And not necessarily an expert in everything.
*  It's like living in a city.
*  You don't necessarily know every street, but you know the important ones you need to get to.
*  So we have projects in research which actually look at the thousands of hours of tutorials
*  online and try to understand what's being taught in them.
*  And then we had one publication at CHI where it was looking at, given the last three or
*  four actions you did, what did other people in tutorials do next?
*  So if you want some inspiration for what you might do next, or you just want to watch the
*  tutorial and see, learn from people who are doing similar workflows to you, you can without
*  having to go and search on keywords and everything.
*  So really trying to use the context of your use of the app to make intelligent suggestions,
*  either about choices that you might make,
*  or in a more assistive way where it could say, if you did this next, we could show you.
*  And that's basically the frontier that we're exploring now, which is, if we really deeply
*  understand the domain in which designers and creative people work, can we combine that with
*  AI and pattern matching of behavior to make intelligent suggestions, either through
*  verbal possibilities or just showing the results of if you try this.
*  And that's really the sort of, I was in a meeting today thinking about these things.
*  Well, it's still a grand challenge.
*  We'd all love an artist over one shoulder and a teacher over the other, right?
*  And we hope to get there.
*  And the right thing to do is to give enough at each stage that it's useful in itself,
*  but it builds a foundation for the next level of expectation.
*  Are you aware of this gigantic medium of YouTube that's creating just a bunch of creative people,
*  both artists and teachers of different kinds?
*  Absolutely.
*  And the more we can understand those media types, both visually and in terms of transcripts and
*  words, the more we can bring the wisdom that they embody into the guidance that's embedded in the
*  tool.
*  That would be brilliant.
*  To remove the barrier from having to yourself type in the keyword searching, so on.
*  Absolutely.
*  And then in the longer term, an interesting discussion is does it ultimately not just
*  assist with learning the interface we have, but does it modify the interface to be simpler?
*  Or do you fragment into a variety of tools, each of which has a different level of visibility of
*  the functionality?
*  I like to say that if you add a feature to a GUI, you have to have yet more visual complexity
*  confronting the new user.
*  Whereas if you have an assistant with a new skill, if you know they have it, so you know to ask for
*  it, then it's sort of additive without being more intimidating.
*  So we definitely think about new users and how to onboard them.
*  Many actually value the idea of being able to master that complex interface and keyboard
*  shortcuts like you were talking about earlier, because with great familiarity, it becomes a
*  musical instrument for expressing your visual ideas.
*  And other people just want to get something done quickly in the simplest way possible.
*  And that's where a more assistive version of the same technology might be useful, maybe on a
*  different class of device, which is more in context for capture, say.
*  Whereas somebody who's in a deep post-production workflow, maybe want to be on a laptop or a big
*  screen desktop and have more knobs and dials to really express the subtlety of what they want to do.
*  So there's so many exciting applications of computer vision and machine learning that
*  Adobe is working on, like scene stitching, sky replacement, foreground, background removal,
*  spatial object-based image search, automatic image captioning, like we mentioned, project cloak,
*  project deep fill, filling in parts of the images.
*  Project scribbler, style transform video, style transform faces and video with project
*  puppetron, best name ever. Can you talk through a favorite or some of them or examples that popped
*  in mind? And I'm sure I'll be able to provide links to other ones we don't talk about, because
*  there's visual elements to all of them that are exciting.
*  Why they're interesting for different reasons might be a good way to go. So I think sky replace
*  is interesting because we talked about selection being sort of an atomic operation. It's almost
*  like if you think of an assembly language, it's like a single instruction. Whereas sky
*  replace is a compound action where you automatically select the sky. You look for stock content that
*  matches the geometry of the scene. You try to have variety in your choices so that you do
*  coverage of different moods. It then mattes in the sky behind the foreground. But then importantly,
*  it uses the foreground of the other image that you just searched on to recolor the foreground
*  of the image that you're editing. So if you say go from a midday sky to an evening sky, it will
*  actually add sort of an orange glow to the foreground objects as well. I was a big fan
*  in college of Magritte, and he has a number of paintings where it's surrealism because he'll
*  like do a composite, but the foreground building will be at night and the sky will be during the
*  day. There's one called The Empire of Light, which was on my wall in college. And we're trying not
*  to do surrealism. It can be a choice, but we'd rather have it be natural by default rather than
*  it looking fake, and then you have to do a whole bunch of post-production to fix it. So that's a
*  case where we're kind of capturing an entire workflow into a single action and doing it in
*  about a second rather than a minute or two. And when you do that, you can not just do it once,
*  but you can do it for say like 10 different backgrounds. And then you're almost back to
*  this inspiration idea of, I don't know quite what I want, but I'll know it when I see it.
*  And you can just explore the design space as close to final production value as possible.
*  And then when you really pick one, you might go back and slightly tweak the selection mask
*  just to make it perfect and do that kind of polish that professionals like to bring to their work.
*  So then there's this idea of, as you mentioned, the sky replacing it to different stock images
*  of the sky. In general, you have this idea- Or it could be on your disc or whatever.
*  A disc, right. But making even more intelligent choices about ways to search stock images,
*  which is really interesting. It's kind of spatial. Absolutely.
*  Right. So that was something we called Concept Canvas. So normally when you do,
*  say, an image search, you would- Assuming it's just based on text, you would
*  give the keywords of the things you want to be in the image and it would find the
*  nearest one that had those tags. For many tasks, you really want to be able to say,
*  I want a big person in the middle or in a dog to the right and umbrella above the left because
*  you want to leave space for the text or whatever for them. And so Concept Canvas lets you
*  assign spatial regions to the keywords. And then we've already pre-indexed the images to know
*  where the important concepts are in the picture. So we then go through that index matching to
*  assets. And even though it's just another form of search, because you're doing spatial design or
*  layout, it starts to feel like design. You sort of feel oddly responsible for the image that comes
*  back as if you invented it a little bit. So it's a good example where giving enough control starts
*  to make people have a sense of ownership over the outcome of the event. And then we also have
*  technologies in Photoshop where you physically can move the dog in post as well. But for Concept
*  Canvas, it was just a very fast way to sort of loop through and be able to lay things out.
*  And in terms of being able to remove objects from a scene and fill in the background automatically,
*  so that's extremely exciting. And that's so Neon Networks are stepping in there.
*  I just talked this week with Ian Goodfellow.
*  Yes, the GANs for doing that is definitely one approach.
*  Is that a really difficult problem? Is it as difficult as it looks? Again, to take it to a
*  robust product level? Well, there are certain classes of image for which the traditional
*  algorithms like Content-Aware Fill work really well. Like if you have a naturalistic texture,
*  like a gravel path or something, because it's patch based, it will make up a very plausible
*  looking intermediate thing and fill in the hole. And then we use some algorithms to sort of smooth
*  out the lighting so you don't see any brightness contrast in that region, or you've gradually
*  ramped from dark to light if it straddles a boundary. Where it gets complicated is if
*  you have to infer invisible structure behind the person in front. And that really requires
*  a common sense knowledge of the world to know what, you know, if I see three quarters of a house,
*  do I have a rough sense of what the rest of the house looks like? If you just fill it in
*  with patches, it can end up sort of doing things that make sense locally, but you look at the global
*  structure and it looks like it's just sort of crumpled or messed up. And so what GANs and
*  neural nets bring to the table is this common sense learned from the training set. And
*  the challenge right now is that the generative methods that can make up missing holes using
*  that kind of technology are still only stable at low resolutions. And so you either need to then
*  go from a low resolution to a high resolution using some other algorithm, or we need to push
*  the state of the art and it's still in research to get to that point. Of course, if you show it
*  something, say it's trained on houses, and then you show it an octopus, it's not going to do a
*  very good job of showing common sense about octopuses. So again, you're asking about how
*  you know that it's ready for prime time. You really need a very diverse training set of images. And
*  ultimately, that may be a case where you put it out there with some guardrails where
*  you might do a detector which looks at the image and sort of estimates its own competence of how
*  well a job could this algorithm do. So eventually, there may be this idea of what we call an ensemble
*  of experts where any particular expert is specialized in certain things. And then there's
*  either they vote to say how confident they are about what to do. This is more future looking.
*  Or there's some dispatcher which says, you're good at houses, you're good at trees.
*  All this adds up to a lot of work because each of those models will be a whole bunch of work. But I
*  think over time, you'd gradually fill out the set and initially focus on certain workflows and then
*  branch out as you get more capable. You mentioned workflows. And have you considered maybe looking
*  far into the future? First of all, using the fact that there is a huge amount of people that use
*  Photoshop, for example, and have certain workflows, being able to collect the information by which
*  they basically get information about their workflows, about what they need, the ways to help them,
*  whether it is houses or octopus that people work on more. Basically getting a beat on what kind of
*  data is needed to be annotated and collected for people to build tools that actually work well for
*  people. Absolutely. And this is a big topic. And the whole world of AI is what data can you gather
*  and why. At one level, the way to think about it is we not only want to train our customers in how
*  to use our products, but we want them to teach us what's important and what's useful. At the same
*  time, we want to respect their privacy. And obviously we wouldn't do things without their
*  explicit permission. And I think the modern spirit of the age around this is you have to
*  demonstrate to somebody how they're benefiting from sharing their data with the tool. Either
*  it's helping in the short term to understand their intent so you can make better recommendations,
*  or if they're friendly to your cause or your tool, or they want to help you evolve quickly
*  because they depend on you for their livelihood, they may be willing to share some of their
*  workflows or choices with the data set to be then trained.
*  There are technologies for looking at learning without necessarily storing all the information
*  permanently so that you can sort of learn on the fly, but not keep a record of what somebody did.
*  So we're definitely exploring all of those possibilities. And I think Adobe exists in a
*  space where Photoshop, like if I look at the data I've created and own, I'm less comfortable sharing
*  data with social networks than I am with Adobe because there's a, just exactly as you said,
*  there's an obvious benefit for sharing the data that I use to create in Photoshop because
*  it's helping improve the workflow in the future, as opposed to it's not clear what the benefit is
*  in social networks. It's nice of you to say that. I mean, I think there are some professional
*  workflows where people might be very protective of what they're doing, such as if I was preparing
*  evidence for a legal case, I wouldn't want any of that phoning home to help train the algorithm
*  or anything. There may be other cases where people are, say, having a trial version or they're doing
*  some, I'm not saying we're doing this today, but there's a future scenario where somebody has a
*  more permissive relationship with Adobe where they explicitly say, I'm fine, I'm only doing hobby
*  projects or things which are non-confidential and in exchange for some benefit, tangible or otherwise,
*  I'm willing to share very fine-grained data. So another possible scenario is to capture relatively
*  crude high-level things from more people and then more detailed knowledge from people who are
*  willingly participate. We do that today with explicit customer studies where we go and visit
*  somebody and ask them to try the tool and we human observe what they're doing. In the future,
*  to be able to do that enough to be able to train an algorithm, we'd need a more systematic process,
*  but we'd have to do it very consciously because one of the things people treasure about Adobe is
*  a sense of trust and we don't want to endanger that through overly aggressive data collection.
*  So we have a chief privacy officer and it's definitely front and center of thinking about
*  AI rather than an afterthought. Well, when you start that program, sign me up.
*  Okay, happy to. Is there other projects that you wanted to mention that I didn't perhaps
*  pop into mind? Well, you covered the number. I think you mentioned Project Puppetron. I think
*  that one is interesting because you might think of Adobe as only thinking in 2D and that's a good
*  example where we're actually thinking more three-dimensionally about how to assign features
*  to faces so that we can, you know, if you take, so what Puppetron does, it takes either a still or
*  a video of a person talking and then it can take a painting of somebody else and then apply the
*  style of the painting to the person who's talking in the video. And it's unlike a sort of screen door
*  post-filter effect that you sometimes see online. It really looks as though it's
*  sort of somehow attached or reflecting the motion of the face. And so that's the case
*  where even to do a 2D workflow like stylization, you really need to infer more about the 3D
*  structure of the world. And I think as 3D computer vision algorithms get better,
*  initially they'll focus on particular domains like faces where you have a lot of prior knowledge
*  about structure and you can maybe have a parameterized template that you fit to the image.
*  But over time, this should be possible for more general content. And it might even be invisible
*  to the user that you're doing 3D reconstruction under the hood, but it might then let you do
*  edits much more reliably or correctly than you would otherwise. And, you know, the face is a very
*  important application, right? So making things work.
*  And a very sensitive one. If you do something uncanny, it's very disturbing.
*  That's right. You have to get it right. So in the space of
*  augmented reality and virtual reality, what do you think is the role of AR and VR in the content we
*  consume as people, as consumers, and in the content we create as creators?
*  Now that's a great question. We think about this a lot too. So I think
*  VR and AR serve slightly different purposes. So VR can really transport you to an entire immersive
*  world no matter what your personal situation is. To that extent, it's a bit like a really,
*  really wide screen television where it sort of snaps you out of your context and puts you in
*  a new one. And I think it's still evolving in terms of the hardware I actually worked on VR in the
*  90s trying to solve the latency and sort of nausea problem, which we did, but it was very
*  expensive and a bit early. There's a new wave of that now, I think. And increasingly those devices
*  are becoming all in one rather than something that's tethered to a box. I think the market seems
*  to be bifurcating into things for consumers and things for professional use cases, like for
*  architects and people designing where your product is a building. And you really want to experience
*  it better than looking at a scale model or a drawing, I think, or even than a video.
*  So I think for that, where you need a sense of scale and spatial relationships, it's great.
*  I think AR holds the promise of sort of taking digital assets off the screen and putting them
*  in the context in the real world on the table in front of you, on the wall behind you. And
*  that has the corresponding need that the assets need to adapt to the physical context in which
*  they're being placed. I mean, it's a bit like having a live theater troupe come to your house
*  and put on Hamlet. My mother had a friend who used to do this at Stately Homes in England for
*  the National Trust. And they would adapt the scenes and even they'd walk the audience through
*  the rooms to see the action based on the country house they found themselves in for two days. And
*  I think AR will have the same issue that if you have a tiny table in a big living room or something,
*  it'll try to figure out what can you change and what's fixed. And there's a little bit of a
*  tension between fidelity where if you captured, say, Nureyev doing a fantastic ballet, you'd want
*  it to be sort of exactly reproduced and maybe all you could do is scale it down. Whereas somebody
*  telling you a story might be walking around the room doing some gestures and that could adapt
*  to the room in which they were telling the story. And do you think fidelity is that important in
*  that space or is it more about the storytelling? I think it may depend on the characteristic of
*  the media. If it's a famous celebrity, then it may be that you want to catch every nuance and
*  they don't want to be reanimated by some algorithm. It could be that if it's really,
*  you know, a lovable frog telling you a story and it's about a princess and a frog, then it doesn't
*  matter if the frog moves in a different way. I think a lot of the ideas that have sort of grown
*  up in the game world will now come into the broader commercial sphere once they're needing
*  adaptive characters in AR. Are you thinking of engineering tools that allow creators to create
*  in the augmented world, basically making a Photoshop for the augmented world?
*  Well, we have shown a few demos of sort of taking a Photoshop layer stack and then expanding it into
*  3D. That's actually been shown publicly as one example in AR. Where we're particularly excited
*  at the moment is in 3D. 3D design is still a very challenging space and we believe that it's a
*  worthwhile experiment to try to figure out if AR or immersive makes 3D design more spontaneous.
*  Can you give me an example of 3D design? Just like applications?
*  Literally, a simple one would be laying out objects, right? So on a conventional screen,
*  you'd sort of have a plan view and a side view and a perspective view and you'd sort of be dragging
*  it around with a mouse and if you're not careful, it would go through the wall and all that. Whereas,
*  if you were really laying out objects, say in a VR headset, you could literally move your head to
*  see a different viewpoint. They'd be in stereo so you'd have a sense of depth because you're
*  already wearing the depth glasses, right? So it would be those sort of big gross motor,
*  move things around kind of skills seem much more spontaneous just like they are in the real world.
*  The frontier for us, I think, is whether that same medium can be used to do fine grain design tasks,
*  like very accurate constraints on say a CAD model or something. That may be better done on
*  a desktop, but it may just be a matter of inventing the right UI. So we're hopeful that
*  because there will be this potential explosion of demand for 3D assets driven by AR and more
*  real-time animation on conventional screens, that those tools will also help with,
*  or those devices will help with designing the content as well.
*  You've mentioned quite a few interesting sort of new ideas.
*  And at the same time, there's old timers like me that are stuck in their old ways.
*  I think I'm the old timer.
*  Okay, all right. But the opposed all change at all costs.
*  When you're thinking about creating new interfaces, do you feel the burden of just
*  this giant user base that loves the current product? And so anything new you do that,
*  any new idea comes at a cost that you'll be resisted?
*  Well, I think if you have to trade off control for convenience, then our existing user base
*  would definitely be offended by that. I think if there are some things where you have more
*  convenience and just as much control, that may be more welcome. We do think about not breaking
*  well-known metaphors for things. So things should sort of make sense.
*  Photoshop has never been a static target. It's always been evolving and growing.
*  And to some extent, there's been a lot of brilliant thought along the way of how it works today. So
*  we don't want to just throw all that out. If there's a fundamental breakthrough, like a single click
*  is good enough to select an object rather than having to do lots of strokes, that actually fits
*  in quite nicely to the existing tool set, either as an optional mode or as a starting point.
*  I think where we're looking at radical simplicity, where you could encapsulate an entire workflow
*  with a much simpler UI, then sometimes that's easier to do in the context of either a different
*  device, like a mobile device where the affordances are naturally different,
*  or in a tool that's targeted at a different workflow where it's about spontaneity and
*  velocity rather than precision. And we have projects like Rush, which can let you do
*  professional quality video editing for a certain class of media output that is targeted very
*  differently in terms of users and the experience. And ideally, people would go, if I'm feeling like
*  doing premiere, big project, I'm doing a four-part television series, that's definitely a premiere
*  thing. But if I want to do something to show my recent vacation, maybe I'll just use Rush because
*  I can do it in the half an hour I have free at home rather than the four hours I need to do it at
*  work. And for the use cases, which we can do well, it really is much faster to get the same output.
*  But the more professional tools obviously have a much richer toolkit and more flexibility in what
*  they can do. And then at the same time, with the flexibility and control, I like this idea of smart
*  defaults of using AI to coach you to like what Google has, I'm feeling lucky button. Right.
*  Or one button kind of gives you a pretty good set of settings. And then you almost, that's almost an
*  educational tool. Absolutely. Yeah. To show, because sometimes when you have all this control,
*  you're not sure about the correlation between the different bars that control different elements
*  of the image and so on. And sometimes there's a degree of, you don't know what the optimal is.
*  And then some things are sort of on demand, like help, right? Help, yeah. Where I'm stuck,
*  I need to know what to look for. I'm not quite sure what it's called.
*  And something that was proactively making helpful suggestions or, you know, you could imagine a
*  make a suggestion button where you'd use all of that knowledge of workflows and everything to
*  maybe suggest something to go and learn about or just to try or show the answer. And maybe it's
*  not one intelligent default, but it's like a variety of defaults. And then you go, oh, I like
*  that one. Yeah. Yeah. Yeah. Several options. Yeah. So back to poetry. Ah, yes. We're going to,
*  we're going to interleave. So first few lines of a recent poem of yours before I ask the next
*  question. This is about the smartphone. Today left my phone at home and went down to the sea.
*  The sand was soft, the ocean glass, but I was still just me. This is a poem about you leaving
*  your phone behind and feeling quite liberated because of it. So this is kind of a difficult
*  topic and let's see if we can talk about it, figure it out. But so with the help of AI,
*  more and more we can create sort of versions of ourselves, versions of reality that are in some
*  ways more beautiful than actual reality. You know, and some of the creative effort there is part of
*  doing this, creating this illusion. So of course this is inevitable, but how do you think we should
*  adjust as human beings to live in this digital world that's partly artificial, that's better
*  than the world that we lived in a hundred years ago when you didn't have a phone.
*  Oh, this is sort of showing off better versions of ourselves.
*  We're using the tooling of modifying the images or even with artificial intelligence,
*  ideas of deep fakes and creating adjusted or fake versions of ourselves in reality.
*  I think it's an interesting question. You're all sort of historical bent on this. So
*  I think we should do that.
*  I think it's an interesting question. You're all sort of historical bent on this. So
*  I actually wonder if 18th century aristocrats who commissioned famous painters to paint portraits
*  of them had portraits that were slightly nicer than they actually looked in practice.
*  Well played, sir.
*  Human desire to put your best foot forward has always been true.
*  I think it's interesting. You sort of framed it in two ways. One is if we can imagine alternate
*  realities and visualize them, is that a good or bad thing? In the old days, you do it with
*  storytelling and words and poetry, which still resides sometimes on websites. But
*  we've become a very visual culture in particular. In the 19th century, we were very much a text-based
*  culture. People would read long tracks. Political speeches were very long. Nowadays, everything's
*  very kind of quick and visual and snappy. I think it depends on how harmless your intent is. A lot
*  of it's about intent. So if you have a somewhat flattering photo that you pick out of the photos
*  that you have in your inbox to say, this is what I look like, it's probably fine. If someone's going
*  to judge you by how you look, then they'll decide soon enough when they meet you as the reality.
*  I think where it can be harmful is if people hold themselves up to an impossible standard,
*  which they then feel bad about themselves for not meeting. I think that's definitely can be an issue.
*  But I think the ability to imagine and visualize an alternate reality, which sometimes you then
*  go off and build later, can be a wonderful thing too. People can imagine architectural styles,
*  which they then have a startup, make a fortune, and then build a house that looks like
*  their favorite video game. Is that a terrible thing? I used to worry about exploration, actually,
*  that part of the joy of going to the moon when I was a tiny child, I remember it in grainy black
*  and white, was to know what it would look like when you got there. I think now we have such good
*  graphics for visualizing the experience before it happens that I slightly worry that it may take the
*  edge off actually wanting to go. Because we've seen it on TV, by the time we finally get to Mars,
*  we'll go, yeah, yeah, so it's Mars, that's what it looks like. But then the outer exploration,
*  I think Pluto was a fantastic recent discovery where nobody had any idea what it looked like,
*  and it was just breathtakingly varied and beautiful. So I think expanding the ability
*  of the human toolkit to imagine and communicate on balance is a good thing. I think there are
*  abuses. We definitely take them seriously and try to discourage them. I think there's a parallel
*  side where the public needs to know what's possible through events like this, so that
*  you don't believe everything you read in print anymore, and it may over time become true of
*  images as well. Or you need multiple sets of evidence to really believe something rather
*  than a single media asset. So I think it's a constantly evolving thing. It's been true
*  forever. There's a famous story about Anne of Cleves and Henry VIII where,
*  luckily for Anne, they didn't get married, or they got married and broke up in it.
*  What's the story?
*  Oh, so Holbein went and painted a picture, and then Henry VIII wasn't pleased. History doesn't
*  record whether Anne was pleased, but I think she was pleased not to be married more than a day or
*  something. So I mean, this has gone on for a long time, but I think it's just part of the magnification
*  of human capability.
*  You've kind of built up an amazing research environment here, research culture, research
*  lab, and you've written at The Secret to a Thriving Research Lab as interns. Can you
*  unpack that a little bit?
*  Oh, absolutely. So a couple of reasons. As you see looking at my personal history,
*  there are certain ideas you bond with at a certain stage of your career, and you tend to keep
*  revisiting them through time. If you're lucky, you pick one that doesn't just get solved in the
*  next five years, and then you're sort of out of luck. So I think a constant influx of new people
*  brings new ideas with it. From the point of view of industrial research, because a big part of what
*  we do is really taking those ideas to the point where they can ship as very robust features,
*  you end up investing a lot in a particular idea. And if you're not careful, people can get too
*  conservative in what they choose to do next, knowing that the product teams will want it.
*  And interns let you explore the more fanciful or unproven ideas in a relatively lightweight way,
*  ideally leading to new publications for the intern and for the researcher.
*  And it gives you then a portfolio from which to draw which idea am I going to then try to
*  take all the way through to being robust in the next year or two to ship. So it sort of becomes
*  part of the funnel. It's also a great way for us to identify future full-time researchers.
*  Many of our greatest researchers were former interns. It builds a bridge to university
*  departments so we can get to know and build an enduring relationship with the professors,
*  and we often do academic give-funds to as well as an acknowledgement of the value the interns add and
*  their own collaborations. So it's sort of a virtuous cycle. And then the long-term legacy
*  of a great research lab hopefully will be not only the people who stay but the ones who move
*  through and then go off and carry that same model to other companies. And so we believe strongly in
*  industrial research and how it can complement academia. And we hope that this model will
*  continue to propagate and be invested in by other companies, which makes it harder for us to recruit,
*  of course, but that's a sign of success. And a rising tide lifts all ships in that sense.
*  And where is the idea born with the interns? Is there brainstorming? Is there discussions about,
*  you know, like what... Where do the ideas come from?
*  Yeah. As I'm asking the question, I realize how dumb it is, but I'm hoping...
*  No, it's not a dumb question at all. It's actually a question I ask at the beginning of every summer.
*  So what will happen is we'll send out a call for interns. They'll... We'll have a number of
*  resumes come in. People will contact the candidates, talk to them about their interests.
*  They'll usually try to find somebody who has a reasonably good match to what they're already
*  doing or just has a really interesting domain that they've been pursuing in their PhD. And we
*  think we'd love to do one of those projects too. And then the intern stays in touch with the
*  mentor, as we call them. And then they come and at the end of two weeks, they have to decide. So
*  they'll often have a general sense by the time they arrive. And we'll have internal discussions
*  about what are all the general ideas that we're wanting to pursue to see whether two people have
*  the same idea and maybe they should talk and all that. But then once the intern actually arrives,
*  sometimes the idea goes linearly and sometimes it takes a giant left turn and we go, that sounded
*  good, but when we thought about it, there's this other project or it's already been done and we
*  found this paper, we were scooped, but we have this other great idea. So it's pretty flexible
*  at the beginning. One of the questions for research labs is who's deciding what to do
*  and then who's to blame if it goes wrong? Who gets the credit if it goes right?
*  And so in Adobe, we push the needle very much towards freedom of choice of projects
*  by the researchers and the interns, but then we reward people based on impact. So if the projects
*  ultimately end up impacting the products and having papers and so on. And so your alternative
*  model, just to be clear, is that you have one lab director who thinks he's a genius and tells
*  everybody what to do, takes all the credit if it goes well, blames everybody else if it goes badly.
*  So we don't want that model. And this helps new ideas percolate up. The art of running such a lab
*  is that there are strategic priorities for the company and there are areas where we do want to
*  invest and pressing problems. And so it's a little bit of a trickle down and filter up,
*  meets in the middle. And so you don't tell people you have to do X, but you say
*  X would be particularly appreciated this year. And then people reinterpret X through the filter
*  of things they want to do and they're interested in. And miraculously, it usually comes together
*  very well. One thing that really helps is Adobe has a really broad portfolio of products. So
*  if we have a good idea, there's usually a product team that is intrigued or interested.
*  So it means we don't have to qualify things too much ahead of time. Once in a while, the product
*  teams sponsor an extra intern because they have a particular problem that they really care about,
*  in which case it's a little bit more, we really need one of these. And then we sort of say,
*  great, I get an extra intern. We find an intern, he thinks that's a great problem.
*  But that's not the typical model. That's sort of the icing on the cake as far as the budget's
*  concerned. And all of the above end up being important. It's really hard to predict at the
*  beginning of the summer, which we all have high hopes for all of the intern projects, but
*  ultimately some of them pay off and some of them sort of are a nice paper, but don't turn into a
*  feature. Others turn out not to be as novel as we thought, but they'd be a great feature, but not a
*  paper. And then others, we make a little bit of progress and we realize how much we don't know.
*  And maybe we revisit that problem several years in a row until it finally we have a breakthrough
*  and then it becomes more on track to impact a product. Jumping back to a big overall view
*  of Adobe research, what are you looking forward to in 2019 and beyond? What is, you mentioned
*  there's a giant suite of products, giant suite of ideas, new interns, a large team of researchers.
*  Where do you think the future holds? In terms of the technological breakthroughs?
*  Technological breakthroughs, especially ones that will make it into product, will get to impact the
*  world. So I think the creative or the analytics assistants that we talked about where
*  they're constantly trying to figure out what you're trying to do and how can they be helpful
*  and make useful suggestions is a really hot topic. And it's very unpredictable as to when
*  it'll be ready, but I'm really looking forward to seeing how much progress we make against that.
*  I think some of the core technologies like generative adversarial networks are immensely
*  promising and seeing how quickly those become practical for mainstream use cases at high
*  resolution with really good quality is also exciting. And they also have this sort of strange
*  way of even the things they do oddly are odd in an interesting way. So it can look like dreaming
*  or something. So that's fascinating. I think internally we have a Sensei platform, which is
*  a way in which we're pooling our neural nets and other intelligence models into a central platform,
*  which can then be leveraged by multiple product teams at once. So we're in the middle of
*  transitioning from a, once you have a good idea, you pick a product team to work with and they
*  you sort of hand design it for that use case to a more sort of Henry Ford standard up in a standard
*  way, which can be accessed in a standard way, which should mean that the time between a good idea and
*  impacting our products will be greatly shortened. And when one product has a good idea, many of
*  the other products can just leverage it too. So it's sort of an economy of scale. So that's more
*  about the how than the what, but that combination of this sort of Renaissance in AI, there's a
*  comparable one in graphics with real time retracing and other really exciting emerging technologies.
*  And when these all come together, you'll sort of basically be dancing with light, right? Where
*  you'll have real time shadows, reflections, and as if it's a real world in front of you, but then
*  with all these magical properties brought by AI where it sort of anticipates or modifies itself
*  in ways that make sense based on how it understands the creative task you're trying to do.
*  That's a really exciting future for creative for myself too as a creator. So first of all,
*  I work on autonomous vehicles. I'm a roboticist. I love robots. And I think you have a fascination
*  with snakes, both natural and artificial robots. I share your fascination. I mean, their movement
*  is beautiful, adaptable. The adaptability is fascinating. There are, I looked it up,
*  2900 species of snakes in the world. Wow. 875 randomness. Some are tiny, some are huge.
*  I saw that there's one that's 25 feet in some cases. So what's the most interesting thing
*  that you connect with in terms of snakes, both natural and artificial? What was the connection
*  with robotics, AI, and this particular form of a robot? Well, it actually came out of my work in
*  the 80s on computer animation where I started doing things like cloth simulation and other kind
*  of soft body simulation. And you'd sort of drop it and it would bounce. Then it would just sort of
*  stop moving. And I thought, well, what if you animate the spring lengths and simulate muscles?
*  And the simplest object I could do that for was an earthworm. So I actually did a paper in 1988
*  called the Motion Dynamics of Snakes and Worms. And I read the physiology literature on both
*  how snakes and worms move and then did some of the early computer animation examples of that.
*  So your interest in robotics started with graphics.
*  Came out of simulation and graphics. When I moved from Alias to Apple, we actually did a movie
*  called Her Majesty's Secret Serpent, which is about a secret agent snake that parachutes in and
*  captures a film canister from a satellite, which tells you how old fashioned we were thinking
*  back then. Sort of classic 1950s or 60s Bond movie kind of thing. And at the same time,
*  I'd always made radio controlled ships when I was a child and from scratch. And I thought,
*  well, how can it be to build a real one? And so then started what turned out to be like a
*  15 year obsession with trying to build better snake robots. And the first one that I built just
*  sort of slithered sideways, but didn't actually go forward. Then I added wheels and building
*  things in real life makes you honest about the friction. The thing that appeals to me is I
*  love creating the illusion of life, which is what drove me to animation. And if you have a robot
*  with enough degrees of coordinated freedom that move in a kind of biological way, then it starts
*  to cross the Ancani Valley and to seem me like a creature rather than a thing. And I certainly got
*  that with the early snakes by S3. I had it able to side wind as well as go directly forward.
*  My wife to be suggested that it would be the ring bearer at our wedding. So it actually went
*  down the aisle carrying the rings and got in the local paper for that, which was really fun.
*  And this was all done as a hobby. And then I, at the time that onboard compute was incredibly
*  limited. It was sort of- Yeah. So you should explain that these snakes, the whole idea is that
*  you're trying to run it autonomously. Autonomously, on board power, on board. Right. And so
*  the very first one, I actually built the controller from discrete logic because I used to do LSI,
*  circuits and things when I was a teenager. And then the second and third one, the eight bit
*  microprocessors were available with like a whole 256 bytes of RAM, which you could just about squeeze
*  in. So they were radio controlled rather than autonomous and really were more about the
*  physicality and coordinated motion. I've occasionally taken a sidestep into, if only I
*  could make it cheaply enough, bake a great toy, which has been a lesson in how clockwork is its
*  own magical realm that you venture into and learn things about backlash and other things you don't
*  take into account as a computer scientist, which is why what seemed like a good idea doesn't work.
*  So it was quite humbling. And then more recently, I've been building S9, which is a much better
*  engineered version of S3 where the motors wore out and it doesn't work anymore and you can't buy
*  replacements, which is sad given that it was such a meaningful one. S5 was about twice as long and
*  looked much more biologically inspired. Unlike the typical roboticist, I taper my snakes.
*  There are good mechanical reasons to do that, but it also makes them look more biological,
*  although it means every segment is unique rather than a repetition, which is why most engineers
*  don't do it. It actually saves weight and leverage and everything. And that one is currently on
*  display at the International Spy Museum in Washington, DC. Not that it's done any spying.
*  It was on YouTube and it got its own conspiracy theory where people thought that it wasn't real
*  because I work at Adobe, it must be fake graphics. And people would write to me,
*  tell me it's real. They say the background doesn't move. And it's on a tripod.
*  But you can see the real thing, so it really is true. And then the latest one is the first one
*  where I could put a Raspberry Pi, which leads to all sorts of terrible jokes about pythons and
*  things. But this one can have onboard compute. And then where my hobby work and my work work
*  are converging is you can now add vision accelerator chips, which can evaluate neural nets and do
*  object recognition and everything. So both for the snakes and more recently for the spider that
*  I've been working on, having desktop level compute is now opening up a whole world of
*  true autonomy with onboard compute, onboard batteries, and still having that sort of
*  biomimetic quality that appeals to children in particular. They are really drawn to them. And
*  adults think they look creepy, but children actually think they look charming. And I gave
*  a series of lectures at Girls Who Code to encourage people to take an interest in technology.
*  And at the moment, I'd say they're still more expensive than the value that they add,
*  which is why they're a great hobby for me, but they're not really a great product.
*  It makes me think about doing that very early thing I did at Alias with changing the muscle
*  rest lengths. If I could do that with a real artificial muscle material, then the next snake
*  ideally would use that rather than motors and gearboxes and everything. It would be lighter,
*  much stronger, and more continuous and smooth. So I like to say being in research is a license to
*  be curious. And I have the same feeling with my hobby. It forced me to read biology and be curious
*  about things that otherwise would have just been a natural geographic special. Suddenly I'm thinking,
*  how does that snake move? Can I copy it? I look at the trails that sidewinding snakes leave in
*  sand and see if my snake robots would do the same thing. So out of something inanimate, I like
*  where you put it, try to bring life into it and beauty. Absolutely. And then ultimately,
*  give it a personality, which is where the intelligent agent research will converge with
*  the vision and voice synthesis to give it a sense of having not necessarily human level
*  intelligence. I think the Turing test is such a high bar, it's a little bit self-defeating,
*  but having one that you can have a meaningful conversation with, especially if you have a
*  reasonably good sense of what you can say. So not trying to have it so a stranger could walk up and
*  have one, but so as a pet owner or a robot pet owner, you could know what it thinks about and
*  what it can reason about. Or sometimes just a meaningful interaction. If you have the kind
*  of interaction you have with a dog, sometimes you might have a conversation, but it's usually one
*  way. Absolutely. And nevertheless, it feels like a meaningful connection. And one of the things that
*  I'm trying to do in the sample audio that will play you is beginning to get towards the point where
*  the reasoning system can explain why it knows something or why it thinks something.
*  And that again creates the sense that it really does know what it's talking about, but also
*  for debugging. As you get more and more elaborate behavior, it's like, why did you decide to do that?
*  How do you know that? I think the robot's really my muse for helping me think about
*  the future of AI and what to invent next. So even at Adobe, that's mostly operating in
*  digital world. Correct. Do you ever see a future where Adobe even expands into the more physical
*  world perhaps? So bringing life not into animations, but bringing life into physical
*  objects with whether it's well, I'd have to say at the moment it's a twinkle in my eye. I think
*  the more likely thing is that we will bring virtual objects into the physical world through
*  augmented reality. And many of the ideas that might take five years to build a robot to do,
*  you can do in a few weeks with digital assets. So I think when really intelligent robots finally
*  become commonplace, they won't be that surprising because we'll have been living with those
*  personalities in the virtual sphere for a long time. And then they'll just say, oh, it's Siri
*  with legs or Alexa on hoofs or something. So I can see that well coming. And for now it's still an
*  adventure and we don't know quite what the experience will be like. And it's really exciting to
*  see all of these different strands of my career converge. Yeah, in interesting ways. And it is
*  definitely a fun adventure. So let me end with my favorite poem, the last few lines of my favorite
*  poem of yours that ponders mortality. And in some sense, immortality, as our ideas live through the
*  ideas of others, through the work of others, it ends with, do not weep or mourn. It was enough the
*  little Adames permitted just a single dance, scatter them as deep as your eyes can see.
*  I'm content they'll have another chance, sweeping more centered parts along to join a jostling,
*  lifting throng as others danced in me. Beautiful poem, beautiful way to end it. Gavin, thank you
*  so much for talking today and thank you for inspiring and empowering millions of people
*  like myself for creating amazing stuff. Oh, thank you. Great conversation.
