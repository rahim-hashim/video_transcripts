---
Date Generated: April 15, 2024
Transcription Model: whisper medium 20231117
Length: 6425s
Video Keywords: ['Descript']
Video Views: 82
Video Rating: None
---

# Interfacing with AI, with Linus Lee of Notion
**Cognitive Revolution How AI Changes Everything:** [April 15, 2024](https://www.youtube.com/watch?v=t8QJEGILYfA)
*  The kind of interface that I'm eventually building towards is a tool that lets you edit
*  text or work through ideas, not in the native space of words and characters and tokens,
*  but in the space of actual meaning or features, where features can be anything from,
*  is this a question? Is this a statement? Is this uncertain or certain? To like topical things like,
*  is this about computers versus plans? To probably other kinds of features that we don't really even
*  have words for. I'm generally a pretty optimistic person about technology, as long as the way we
*  package these things is more humanist rather than just kind of like automate all of the things.
*  You see companies situated at different points in the spectrum between you want models to
*  automate things in a way that takes away agency, i.e. replacement, or you want models that amplify.
*  Like I think OpenAI is very much on the replacement side. Literally their definition of,
*  I think, AGI is something like a thing that can take over a single like full human's job,
*  where if you look at a company like Runway, a lot of their framing of usefulness is about
*  extending that agency of what you want to express. Everyone is talking about chat GPT right now,
*  but are you actually using it to the max? How do you use chat GPT? It's an interview show where
*  the people at the forefront of technology show you how they use chat GPT in their work and their lives.
*  Host Dan Shipper talks to programmers, writers, founders, academics, tech executives, and others
*  to walk through all of their chat GPT use cases, including historical chats, step by step. They
*  even use chat GPT together live on the show to build apps, analyze their leadership qualities,
*  read more deeply, and do the best work of their lives. Listen to How Do You Use Chat GPT from Dan
*  Shipper and the team at Every, wherever you get your podcasts. Hello and welcome to the cognitive
*  revolution, where we interview visionary researchers, entrepreneurs, and builders
*  working on the frontier of artificial intelligence. Each week we'll explore their
*  revolutionary ideas and together we'll build a picture of how AI technology will transform
*  work, life, and society in the coming years. I'm Nathan LeBenz joined by my co-host Eric Torenberg.
*  Hello and welcome back to the cognitive revolution. Today my guest is Linus Lee,
*  AI product leader at Notion and AI explorer extraordinaire. I've followed Linus online for
*  a couple years now, fascinated by his many groundbreaking projects and his unique way of
*  thinking about AI systems. From creating novel interfaces that visualize and manipulate generative
*  models in their latent spaces to developing techniques for semantically editing text and
*  images, Linus has been a pioneering tinkerer. In this wide-ranging conversation, we dig into
*  the details of how Linus goes about his explorations. He shares his toolkit from PyTorch as a foundation
*  to the custom tools he's built over time for data visualization, model evaluation, and rapid
*  experimentation. We also discuss the importance of spending time with raw data and failure cases
*  and the value of building your own tools to deeply understand the problems you're trying to solve.
*  Linus also offers his perspective on the current capabilities of language models
*  and where he sees the biggest opportunities for improvement. Beyond the high level goal of
*  better general reasoning, he emphasizes hallucination reduction, better instruction following,
*  and cost efficiency. We also speculate about the future, considering scenarios like models
*  communicating with other models via high dimensional embeddings, techniques to connect latent spaces
*  across modalities, and the societal implications as AI capabilities continue to advance. Linus
*  articulates a vision centered on amplifying rather than replacing human intelligence, a principle he
*  believes should guide the development and deployment of AI-powered products. Throughout this episode,
*  Linus demonstrates the curiosity, resourcefulness, and thoughtfulness that have made him such an
*  influential figure in the AI community. His work inspires me to engage more deeply with these
*  systems, to build the tools I need to understand them, and to steer their development in a direction
*  that deepens rather than diminishes human creativity and agency. As always, if you find
*  value in the show, please share it with others who might appreciate it. Particularly right now as
*  we're establishing the new feed, a tweet or a comment on YouTube would be especially valuable.
*  And of course, we invite you to reach out with feedback or suggestions on our website,
*  cognitiverevolution.ai. Now, please enjoy this deep dive into the art and science of exploring AI
*  systems with Linus Lee of Notion AI. Linus Lee of Notion AI and general all-purpose AI explorer,
*  welcome to the Cognitive Revolution. Thank you. Thanks for having me. Excited to chat. I'm really
*  excited about this. I have followed you online for a couple years now and really been fascinated
*  by all your many projects and just the way that you think about AI systems. I really genuinely
*  think you're a one-of-a-kind thinker from which I've learned a lot. And so going back to when I
*  set out to do this a year ago, you were on the short list of guests that I maybe didn't want to
*  have right away because I kind of wanted to get my, you know, get things set up a little bit and
*  have a little bit more credibility, a little more comfort. But I definitely always knew that I wanted
*  to get you on the show and pick your brain. So I'm excited to get into it. Thanks. That's very
*  generous of you, kind of you to say. Likewise, I'm excited to talk about both AI and everything else
*  that I've worked on and kind of what I see coming up ahead. Well, very well deserved. The way I
*  thought we would maybe approach this is I wanted to give people at the top a little bit of a sense
*  of the kinds of things that you build and then try to kind of peel back some layers from that
*  to then understand like how you're thinking about that in kind of conceptual terms. Also, how you are
*  doing the work in very, very practical terms and then kind of a sense for where you think we're
*  going from here, as well as perhaps some very practical tips based on your experience at Notion
*  and elsewhere for people that are looking up to you as an AI application developer.
*  That sounds good to me. So for starters, you have built some of the most interesting novel interfaces
*  that folks have seen. And, you know, these can be found on your Twitter profile in various places.
*  And you've shown a few off in different talks that you've given. A few of them jumped out to me that
*  you've demoed recently, but I'd love to kind of just introduce a few of the unique interfaces
*  that you've created just to give people a very kind of tangible jumping off point to understand
*  the sorts of things that you put together. Yeah, definitely. I think we can kind of talk through
*  them. I think the more polished, the demo that I can do off the cuff right now is probably not as
*  good as the ones that are more polished online. So you can find them on YouTube, but I can talk
*  about what concrete these demos are. And then I can maybe later talk about my framing for them,
*  because I think that's a part that I view a part of my work is trying to figure out and evolve
*  exactly what the framing should be. And I think that'll come up later in our conversation. But
*  the concretely, there are a couple of directions that I've explored. And one that I've sort of
*  been on for the longest time is to try to visualize and control generative models in their latent
*  space rather than in the input space that we're familiar with. So if you take image generation,
*  for example, the common way of generating images is you describe an image like a cow sitting in a
*  grassy field with sunlight, long shot, 35 millimeter film, whatever, and then the model
*  generates an image. But another way you could imagine generating or improving upon an image is
*  you start with an image and then you find a different image that has another element that
*  you like. Maybe you like the lighting from another image, maybe you like the framing, or maybe you
*  have a character that you want to bring in from another image. And if there was some way to
*  tell the model, can you merge all of the attributes that you see in both of these images
*  into a single image and kind of blend it together in the semantic space rather than in the pixel
*  space? That could be an interesting way to kind of stretch together images. So a couple of my
*  demos are around combining images and text in this semantic space of an image model called clip to
*  generate, for example, start with a human face and then add emotion to it to make it smile or make it
*  frown or starting with like a photograph and then adding different kinds of style to it by just
*  adding vectors in the latent space of a model together. You could do something like this with
*  text as well. So I have a model that's capable of embedding text into a latent space and embedding
*  space, but then also inverting that embedding to go from the embedding to what that embedding
*  represents as text. And it turns out that just in that model, in a lot of embedding models that are
*  expressive enough, this transformation is like pretty, it is invertible with minimal kind of
*  meaning loss. And so I take that model and then I can start to manipulate the embedding itself
*  to, for example, combine two different sentences together semantically and produce a new sentence
*  or interpolate between sentences. So you have one that's maybe very optimistic and happy and bright
*  and another that's maybe a little more mellow. And I can take those two sentences and interpolate
*  between them to generate sentences that are in the middle. And I think that kind of thing
*  could potentially allow for other ways of controlling or editing or generating text or
*  even images that let people control output using levers that are hard to verbalize with text.
*  And there are more rigorous and precise versions of this that I've been working on more recently
*  that I can also talk about. But that's the general gist of things that I've been interested in.
*  And sometimes there are some pretty creative front end experiences on these as well. You want to
*  describe the one also where you have kind of little tiles of text on seemingly an infinite canvas,
*  and then you can kind of drag into different directions and create, like take that text,
*  but now move it in this direction. You're kind of making that a spatial computing sort of experience
*  almost. Yeah. So the two that I think are most interesting visually, the one that you just
*  described actually came out of a problem that I ran into where one of the initial prototypes of
*  this involves just having, imagine this high dimensional latent space of a model and you
*  want to visualize it and you want to visualize it on a screen. And so you cut a 2D slice through it
*  and you cut a 2D slice through this high dimensional space such that the two dimensions
*  that you see on the screen, the bottom edge of your screen, the left edge of your screen,
*  correspond to two different kinds of targets that you move towards. And so maybe the bottom right
*  corner of your screen is like a happy sentence about weddings and the top left corner is about
*  like dinosaurs or something. And you can pick any point in this plane and it'll be a sentence that
*  combines elements of those sentences. That works well for kind of demonstrating the seed of this
*  idea. But the problem that you quickly run into is there are actually way more properties that you
*  want to control when you're generating or editing text than just between two arbitrary anchor
*  sentences. And when you have this fixed plane, you quickly run out of directions that you can move in.
*  And so instead of fixing the directions, the levers that you can pull to just the top and
*  bottom edges of your screen, the next revision which you referenced involves kind of flipping
*  how the dimensions are presented. So the way I used to describe it is imagine you're playing
*  like an instrument and when you play an instrument with one hand, this is very crude,
*  but if you're playing like a string instrument with your left hand, you control the strings and
*  you control the pitches of the notes that you're playing. And with your right hand, you kind of
*  control the like the volume or the amplitude of the sound in a very crude way. And this is a way
*  to kind of transfer that in a spatial interface. So this is an infinite canvas where with one hand,
*  holding down keys on a keyboard, you can choose what specific attribute you want to
*  control for text, whether that's like a positive, negative emotion or whether it's written in fancy
*  English versus simplified English or what kind of topic it is, is it more about sci-fi or so on.
*  And then with your right hand, you can click down on a sentence that you've put down on this plane
*  and you can drag it out. And the further you drag out, the more you're kind of increasing the
*  particular attribute that you've picked. So for example, if you put a sentence down on this 2D
*  canvas and then you hold down the like make longer button and you pull the sentence farther from
*  where you clicked down on it, the farther you pull, the longer that sentence will be. And over time,
*  as you explore this latent space of sentences, you can see all of the branches that you took in
*  this exploration and where each variation came from. And it naturally forms a kind of a branching
*  edit history through which you can follow all of the different kind of movements that you made
*  through latent space and what the sentences that resulted from are. When you think of these
*  projects, are they, I mean, I can, I think they probably have multiple functions for you, right?
*  One is obviously you're learning by doing all this stuff. How much do you actually use these
*  tools versus doing them as kind of proof of concept for some further synthesis on top of this
*  later? Like, do you think these kinds of interfaces are ready for people to actually get
*  utility out of it? And do you personally? Most of the prototypes that I've built for
*  kind of like research purposes, I would say are not good enough to actually be useful. So the kinds
*  of edits that you can make by with this like kind of latent space canvas UI, the edits are very
*  crude and the models that I'm using are too small, I think, to let you make very, very precise edits.
*  And I think one of the kind of continued problem areas in which I want to do more research is to
*  try to improve upon that. There are other prototypes that I've made that have been more
*  useful. And so I think it just depends on how good the particular technology or technique that
*  I'm working on is and whether that is close enough to utility or not. Within the kind of
*  prototype set of build for working in this area of like building interfaces for AI, the eventual
*  goal is always to build something that is useful. And for any individual prototype, it may be,
*  the technology or technique may be too early to actually be useful. So it may be,
*  the prototype may be more about identifying incremental improvements or identifying problem
*  areas or identifying what directions to build more in. Or if the technique is more mature,
*  then it may be close enough to utility that I build it more as something that I can use day to
*  day and actually kind of get benefit from. But there's always an underlying element of it,
*  which is like, this is going to help me better understand what it's for, how it can be useful,
*  how to make it, how to improve on the technique, the quality of the outputs and so on.
*  An example of a prototype that I built a long time ago that I actually ended up using day to day for
*  a long time is kind of an obsidian or room research style outliner note taking out.
*  That was my daily note taking out for a long time where keywords would automatically kind of
*  identify themselves or entities would automatically identify themselves and connect them to other
*  entities in the graph. And that was using mostly not language models, mostly kind of
*  dumber techniques, but it was, the outputs were good enough that I ended up finding those
*  connections very useful and generative in my kind of creative thinking and I used it for a long time.
*  That's cool. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it and I recommend you use it to use cog rev to get a 10% discount.
*  The 2D canvas one in particular of the recent demos that I've seen has a sort of Xerox park
*  vibe about it where you're like, this feels like, especially after I went and tried the
*  Apple Vision Pro, it was like, I see something here and it feels like there is spatial computing
*  spoon fed to you and it's amazing. It's incredibly like a breathtaking technology experience to go
*  put the Apple Vision Pro on your eyes, but it's very much like a consumer experience that you
*  know you start off with, but seeing your 2D canvas imagining that becoming a higher dimensional
*  space that you could potentially move around in and then envisioning these sort of hardware
*  to actually make that feel very experiential starts to give me a little bit of a sense of
*  how some of these future spatial computing notions might be more than just like, oh look,
*  I've got my YouTube screen over here and I've got my email over here, but actually kind of using the
*  brain's spatial intuition to do things that are currently hard to do. Yeah, using all of the full
*  awareness of space and the awareness that we have how to move around. This is all very intuitive.
*  We learn it when we're a child and most of the ways that we work currently don't really take
*  advantage of that. I spent a long time iterating on and I like even still I every like few months
*  I get kind of a new version of exactly how to describe the motivation for building out these
*  kind of like weird spatial demos that are technically not quite there yet, but like
*  gesturing towards something interesting. The most recent version of this I think is actually
*  somewhat relevant to how humans interact with space among other things. The closest metaphor
*  that I found for the reason that this direction of research is so interesting to me
*  is that I think language models work so well because they work with kind of an alternative
*  better representation for ideas than humans work with. The closest analogy that I have is like
*  spectrograms when people are dealing with audio. So normally sound is like a wave in space. It's
*  just a single kind of, I imagine like a single string vibrating back and forth over time. And
*  if you work with audio, that's like the base thing that you work with. It's a basic representation,
*  but if you work professionally with audio, then you actually most of the time work in a
*  different representation space where you don't look at vibrations over time, but you look at
*  space of like frequencies over time or what's called a spectrogram, which is a visualization
*  of like there's still a time axis on the one hand, but the other axis is no longer amplitude of the
*  vibration. It's like the prominence of different frequencies. If you imagine like on the left side
*  of your kind of graph, every like the row is a different pitch and every row gets a little
*  mark when there's like a sound that hits that pitch. It's a little bit like Western music
*  notation kind of staff, but it's like a colorful gradients often appear in these spectrograms.
*  And what you can see because you've broken out the prominence of every different kind of picture,
*  every different frequency is you can see things like, oh, here's a musical pattern that repeats
*  for here is where the base comes in or here's where the tone shifts from this kind of very full
*  sound to this more mellow sound or all these things you can notice. And then you can start
*  to manipulate the sound in the frequency space. So you can do things like bring down the lows or
*  add reverb only to the human voice range of sound, all these kinds of transformations
*  that you're not really making to the sound waves themselves. You're making to this like
*  kind of projected out the version of the sound that exists in this alternative frequency space.
*  That makes sense. The kind of interface that I'm eventually building towards is a tool that lets
*  you edit text or work through ideas, not in the native space of like words and characters and
*  tokens, but in the space of actual meaning or features where features can be anything from
*  is this a question? Is this a statement? Is this uncertain or certain to like topical things like
*  is this about computers versus plans to probably other kinds of features that we don't really even
*  have words for because language models implicitly understand them. We implicitly understand that,
*  but we don't need to ever really verbalize it. So alternative way of like projecting or viewing
*  what's going on in language, and then maybe a way to start editing them. That's like the closest
*  metaphor that I've found for describing the kind of thing that I want. And then once we have that
*  representation, the one reason that spectrograms work so well is because humans intuitively
*  understand kind of color as a way of representing range and positions in space. So we have
*  we have this geometric intuition. And so maybe rather than looking at ideas as just kind of like
*  ink scribbles on paper, maybe we can also look at them in a spatial way. And the canvas was one kind
*  of way of exploring that. I think there are a bunch of other directions that we can go once we have a
*  better, more rigorous understanding of what's going on inside these language models. But eventually,
*  I think we should be able to interact with ideas by bringing them out into the physical space that
*  we occupy or as being as close to that as possible, because we want to bring our kind of
*  full senses and appropriate perception and sense of scale and sense of distance into how we work
*  with ideas rather than just kind of like eyeballs and pixels on the screen. Yeah, that's really
*  interesting. I'm just looking up to try to figure out was it refusion, which might have been the
*  project that people would know most of all that was a stable diffusion fine tuned right on these
*  spectrogram images. So definitely check that out for further intuition there, because it's also
*  an interesting kind of foreshadowing of one of the things I want to talk about a little bit later,
*  of just kind of how all these spaces seem to be very sort of bridgeable to one another in
*  off in many cases through like relatively simple adapters. Here you have a vision model
*  trained to generate these spectrograms. And then that is just converted to music like the AI part
*  stops at the generation of the spectrogram image. But at one point, this was like one of the leading
*  text to music techniques all working through this like vision backbone. So I was going to say that
*  the model is generating audio, but not in the typical space that we think of for presenting
*  audio, which is waves in space, but it's generating in this spectrogram space. But it's actually
*  a little bit more convoluted than that even because most like speech generation speech synthesis
*  models or even a lot of music generation models, they actually, a lot of them do operate in this
*  kind of like frequency space in this like spectrogrammy space. I don't know how the state
*  of the art is now, but until very recently, the way that you built like speech recognition systems
*  was also by feeding an input in this like frequency space rather than just kind of like waves in space.
*  And so not audio models used to naturally operate in this domain. And then what Refusion does is it
*  actually takes a model architecture that is meant for generating pixels in a 2D image using
*  convolutions and applies that to this like generating this thing that's supposed to represent audio.
*  So it's coming through kind of like two jumps in representation and it's still manages to work
*  quite well. It's amazing. That's one of my big kind of themes and takeaways from, you know, a few
*  years now of increasingly obsessive study of the whole space is just what an incredibly high hit
*  rate there is on ideas that actually turn out to work. And obviously, you know, not every idea
*  works, but as somebody who spent a little time in catalytic chemistry, once upon a time, I can say
*  it's definitely probably at least two orders of magnitude higher in AI right now than it is in,
*  you know, many more well-mined corners of the physical sciences. If you have a lot of data
*  and a lot of compute and you have a way of like efficiently putting that compute to work and like
*  squeezing a model through that process, the model architecture is kind of like a final kind of
*  corrective term or coefficient in how well this whole thing works. It turns out like if you can
*  make gradients run on a lot of numbers very quickly with a lot of data that's like high quality,
*  all most ideas will work within like an order of magnitude maybe of like efficiency. And so a lot
*  of these ideas I think are just I attribute to that. And then the recent advancements to
*  the fact that you have now built up kind of all of the open source infrastructure and know-how
*  of how to do this like model training thing at industrial scale rather than in like research
*  lab scale, which was maybe research lab scale to me is like a few GPUs, a few hours, maybe like a
*  few days. And then industrial scale is like thousands of GPUs, many, many weeks. And go from
*  one to the other is in the same way that you can want to like synthesize a little bit of chlorine
*  in a lab. It's very different than like building a chlorine factory. Running these models at scale,
*  I think is a similar kind of like huge qualitative jump in terms of the kinds of knowledge that we
*  have to have. But like we have a lot of it now. And so we can apply that compute to like any
*  arbitrary problem, given there's enough data and given there's an architecture that like doesn't
*  suck super hard. And I think the result of that is that we've suddenly seen an explosion of like
*  models that perform very well, all these modalities and cross modalities.
*  Yeah, compute you got to have data, the quality is critical, and scale is also
*  critical. And then the algorithm just kind of depends how it determines how much compute you
*  have to have to make full use of the data. That's like a, if I set my brevity to max,
*  that's about as brief as I could give, hopefully a decent account.
*  Yeah. As long as the architecture is not bottle necking, what information can propagate through
*  the network? Everything else is just kind of like how many floating part operations can you do?
*  So going back to your exploration of all this technology, so you've been at it for a couple
*  years now. I'm a little bit unclear on the timeline, but I have to say, I feel like I encountered
*  quite a few ideas first through some of your experimental projects. And then later,
*  it seems like they have become more formal as like mechanistic interpretability research
*  publications. A couple kind of canonical results from the last handful of months,
*  the representation engineering paper from Dan Hendrickson collaborators and the toward
*  monosemanticity paper out of Anthropic. I feel like you basically were doing that kind of stuff
*  with small models well before those things kind of hit mainstream. How would you describe your own
*  sources of inspiration for that? Or maybe I have it wrong and there were more academic
*  papers coming out that you were able to take inspiration from, but how did you get to this,
*  these kind of advanced, like middle layers, manipulations, concepts as early as you did?
*  So I don't come from academia. Like my actual technical background is in like product engineering,
*  building web apps, which is like the furthest thing you can be from training models. And so I
*  have to kind of step my foot in slowly into the research side of the community, the ML community,
*  and figure out not only how that side works and kind of how to engage people in that world, but
*  also how ideas propagate through both of these parts of the community. My old mental model of
*  how research works used to be that like researchers are always at the forefront and they try these
*  things and they come up with ideas. And if the ideas are good, they get written about. And then
*  eventually the industry picks them up. And then eventually it like percolates down to smaller and
*  smaller kind of like perhaps less resourced groups. And I think that's maybe that's true in
*  other fields like biology, where there's perhaps a larger gap in capability between what labs can do
*  and companies can do. Even there, I don't think it's actually perfectly true, but certainly in
*  machine learning, because all of the tools are so accessible, especially in the last few years,
*  my picture now of how ideas percolate is actually a lot more nuanced, which is that at any moment,
*  like there is a large group of people that kind of know all of the things that we know about models
*  and what you can do with them. And some of those people exist in the industry with the tools that
*  they have. Some of those people exist in academia. Some of these people are like hobbyists that are
*  just kind of like tinkering on the side, even when their day job is doing something else.
*  And different people might stumble upon the same techniques or the same ideas at the same time,
*  because like most of what results in the next ideas that get discovered is actually, I think,
*  a function of what is already known rather than the specific ideas that individual people have.
*  And so ideas like the intuition that there was a linearized kind of feature space in the latent
*  space of these language models that you could do edits in. I think there was an idea that was kind
*  of intuitively known for a lot of people working in this space. And some people like me, I think,
*  chose to kind of prove that out by doing what I personally enjoy doing the most, which is build
*  interactive prototypes on the web, because that's kind of my expertise. And then I think other people
*  perhaps took longer to be a lot more rigorous and theoretically robust and write things about it
*  and get it out that way. And there's a kind of different way you speak about ideas there versus
*  speak about ideas in the interface world. But I think most of the ideas that come about is just
*  a function of what was already known and different parts of the community, both in research and in
*  industry, that just happen to talk about them in different terms and perhaps reach other parts of
*  the community at different times. I mean, you've had to solve a lot of problems, if I understand
*  correctly. And this gets into the how you work section, I suppose. But if I understand correctly,
*  you are, for example, figuring out your own features. I think you've done a mix of things
*  where sometimes you can take a straight embedding, which is just kind of one hot lookup, and then
*  do that again and mash those up. And that's relatively straightforward to do. But then
*  as you get deeper into the network, you're also doing, at least in some of your projects, you're
*  making edits farther down through the layers of the model. And there you have a much more
*  conceptually challenging problem of, okay, I may have an intuition that I could probably steer
*  around in this space and kind of steer the outputs, but how do I begin to figure out what
*  direction is actually what? If I understand correctly, you've largely had to figure those
*  sorts of things out for yourself, right? You weren't able to really use too much in the way of
*  open-sourced GPT-2 or GPT-J or whatever. These things didn't come with mid-layer feature sets.
*  Exactly. My favorite mental model for research is actually related to the exact path that I followed
*  to hit that wall and then go past it, which is that when I first started getting into deep learning
*  models, most of what I did was read and try to understand things that were in the open-source
*  world. So I had a hard time reading academic papers in the beginning and deep learning because
*  I didn't have all of the kind of vocabulary and the way that people write about these things in
*  my head and in my hands. And so I would just go to the Hockingface Transformers repository,
*  and I would download GPT-2 and get the minimal version running. And I'd be like, oh, it's
*  generating text that recognizes it seems to work. Now that I have a live entity that's working on
*  my computer and I understand Python, and so I can put print statements everywhere and see exactly
*  what's happening. And so that's kind of what I did. I basically did model autopsy on the things
*  that were running on my computer because I felt like I could understand and wrap my head around.
*  And then I would try to understand things that way. And once I understood those models,
*  I would try to understand things were a little bit more on the frontier. And eventually what you hit
*  is you hit a wall where for a while you can get away with, oh, I hit this problem. I'm going to
*  Google how other people solved it. And you arrive at a Hockingface forum post. And then maybe you
*  get a little more esoteric and you arrive at a GitHub issue. And you're like, okay, this is
*  kind of like there's been consensus, but here are some things that people try and maybe they work.
*  And then at some point you hit a wall where you're like, there's nothing on the internet that's an
*  established consensus for how to solve this problem. And you have to go find a paper that
*  somebody wrote three months ago that reports to solve this. And then sometimes it's well-established
*  and well-cited and you can trust it. And other times you're like, well, this paper has two
*  citations and I don't even know if it actually works. And so you have to then find like an
*  implementation that has like one star on GitHub that tries to reproduce it and run it. Or oftentimes
*  those were broken too. And so you have to then like write your own implementation, which you're
*  not even sure if it's the correct one, that's the same one that the researchers used. So you hit a
*  wall at which point you're kind of at the frontier of what we know as a research community or as an
*  industry. And then, but there are still problems to solve. Like I still have things that I want to
*  do that I don't know how to do. And so in the same way that if you like hit a weird Python bug,
*  you keep digging and digging and then maybe you do some like debugging and eventually maybe you
*  have to like go into the Python interpreter. I hit a wall with like trying to find interesting
*  features in these models or trying to even like build models that I can use for these things
*  that were capable of being amenable to these edits. And I hit a wall and I had to eventually
*  read a bunch of papers and develop my own intuition and try to combine the things that I
*  found, to combine the pieces that I found to say, here's an approach that might work based on what
*  I know. There's no obvious consensus on it, but it might work and try it. And that's been the
*  process most obviously to me for first building the auto-encoder that I use for all of these
*  embedding space manipulations, the model that I talked about that lets you go between text and
*  embedding fluidly. And then second for the work that I'm currently most focused on, which is
*  more unsupervised kind of scalable approach of finding these edit directions, which builds on
*  top of a lot of the mechanistic interpretative work that organizations like Conductor and Anthropic
*  have done. But that's also quite on the frontier. And there are some techniques there, but they
*  haven't really been applied to embedding spaces yet. They've mostly been applied to kind of normal
*  GPT language models. And so I've had to take a lot of those techniques and adopt it as well.
*  And a lot of that is like finding weird, like literally I was doing this earlier this morning,
*  finding weird data repositories that have like three stars and try to transplant it over and
*  hope that I'm not messing up the implementation and see how it works.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The tech world turns to the Brave browser for its unbeatable privacy protections. But did you know
*  that Brave also has a private ad platform? Brave ads offers first party targeting and it's been
*  cookie lists since day one. So you can relax while third party tracking cookies disappear from the
*  web. Today, millions of people turn to ad blockers to avoid being tracked and pestered online.
*  But Brave's new ad model aligns incentives for users and advertisers. Users earn rewards for
*  viewing ads, which they can save, spend, or pass along to their favorite creators. And advertisers
*  score points for respecting user privacy, generating ROI without invasive tracking.
*  So whether it's high impact announcements on the new tab page or keyword targeted ads in Brave
*  search, Brave offers diverse private future proof ad formats for all your business goals.
*  Join the future of advertising at brave.com slash ads. Mention MOZ when signing up for a 25%
*  discount on your first campaign. Today's podcast is brought to you by Plum. You've probably noticed
*  by now that the AI features in your favorite products kind of suck. They're cool the first
*  time, but pretty soon you're underwhelmed. That's because truly great AI features require complex
*  pipelines and rigorous testing that most startups simply don't have the time or tooling to get
*  right. That's why Plum created a collaborative AI app builder that's purpose built for product
*  teams. Your users deserve better than a glorified GPT wrapper. Blow their minds with Plum. Check out
*  useplum.com. That's Plum with a B for early access. Hey all, Eric Torenberg here. I'm hearing more and
*  more that founders want to get profitable and do more with less, especially with engineering. Listen,
*  I love your 30 year old ex-fang senior software engineer as much as the next guy, but honestly,
*  I can't afford them anymore. Founders everywhere are trying to turn to global talent, but boy,
*  is it a hassle to do at scale from sourcing to interviewing to on the ground operations and
*  management. That's why I teamed up with Sean Lanahan, who's been building engineering teams
*  in Vietnam at a very high level for over five years to help you access global engineering without
*  the headache. Squa, Sean's new company, takes care of sourcing, legal compliance, and local HR for
*  global talent so you don't have to. With teams across Asia and South America, we can cover you
*  no matter which time zone you operate in. Their engineers follow your process and use your tools.
*  They work with React, Next.js, or your favorite front-end frameworks. And on the back end,
*  they're experts at Node, Python, Java, and anything under the sun. Full disclosure, it's going to cost
*  more than the random person you found on Upwork that's doing two hours of work per week but billing
*  you for 40. But you'll get premium quality at a fraction of the typical cost. Our engineers are
*  vetted top 1% talent and actually working hard for you every day. Increase your velocity without
*  amping up burn. Head to choose squa.com and mention Turpentine to skip the wait list.
*  So before getting into a little bit more detail on how exactly you go about that,
*  how would you characterize, you've obviously built up a lot of intuition over the last few years of
*  doing this, how would you describe what's going on inside a transformer or perhaps what's going on
*  inside a diffusion model? You can kind of break that down however you want. I don't just mean
*  describe the blocks, but how is the information being changed in more sort of... And I guess
*  another related question there is you said you think that the models have a better
*  representation of a lot of ideas than we do. I'm very interested to hear how, as you describe,
*  kind of what's going on in a model. Maybe you can contrast that against what you think is going on
*  for us. I feel like I have a pretty similar setup in some ways to a transformer where it seems that
*  maybe I'm just so prisoner of the AI paradigm now that I just see myself through that, which would be
*  a weird irony. But I do feel like there is this sort of non-verbal, high-dimensional,
*  only semi-conscious churning going on in some middle layers somewhere for me that then kind
*  of gets done and feels like, okay, I'm happy with that now. Now you can speak. And then it kind of,
*  in the last layers, so to speak, it gets cashed out into tokens. But yeah, so what's going on in
*  a language model at a conceptually descriptive level or representationally descriptive level?
*  My mental model for how humans work, I think, includes a really important piece,
*  a piece that I found to be more and more important over time, which is that I don't actually think...
*  I think that the default assumption, I think intuition for how we think we work,
*  our brains work, is that we think through things and then we draw conclusions and then we act upon
*  them. But I don't actually think that's true at all. And I think what happens instead is
*  our brain and our body takes actions and then observing those actions, our brains
*  retroactively build up a narrative for why we perform those actions in a way that seems
*  causally consistent with our understanding of the world, just a whole other interesting thing.
*  And maybe that's what you call consciousness. But on the model side, there are different levels
*  that you can look at this. And I think for transformer language models, the two levels
*  that are most interesting are how is the transformer processing information within a single
*  forward pass generating a single token? And then how are we sampling from the output of the
*  transformer? So I'll talk about the sampling first. The job of a transformer language or a job of any
*  language model is it's called a language model because it's a statistical model. And the statistics
*  that it's modeling is the probability distribution over all possible outputs. And in a lot of cases,
*  this is a conditional probability distribution. So the probability distribution that the model
*  is modeling statistically is here's some start of a sentence. Give me a probability distribution
*  over all possible ways that this input can continue. And this is kind of like a cloud over
*  a cloud of probability over every possible branch that the model can take. And obviously,
*  that's way too many outputs. If we had infinite resources, we would simply ask the model for the
*  probability rating of every single possible continuation and just take the one that the
*  model thought was the highest. But we can't do that because we just don't have a different queue.
*  And so instead, we have to randomly sample from this distribution, this cloud of possible
*  continuations. And there's a bunch of different ways to do the sampling. And I think the most
*  common one is to just sample every token and immediately kind of commit it. So ask the model
*  what's the most likely token to come next. The model says here are the top 50 most likely
*  continuations. And you randomly pick one of them according to probabilities. And you just do that
*  over and over and over again. But there's a bunch of other ways to sample from this. You could have
*  a kind of running buffer of n branches and then only set things in stone when you're n steps in.
*  And you think that that's the most likely continuation. There's a name for it, a
*  technique for that kind of beam search. There's other ways to try to take into account not
*  getting the model to repeat itself as much or taking the probability distribution and kind
*  of warping it in interesting ways to try to emphasize the... There's an interesting technique
*  where you have a small model and a large model, and you assume that the large model
*  improves upon the small model always. And so you take the gap in the distribution and you amplify
*  the difference. And then you try to kind of approximate like what would an even smarter
*  model predict. So there's a bunch of techniques for sampling from this distribution. But ultimately,
*  once you have a good probability distribution that the model outputs, you're trying to find the
*  continuation of a text that's most likely to maximize the likelihood. So that's like how we
*  sample from the distribution part. And then there's the how we get the distribution part,
*  which is what's happening in a single forward passive transformer. And this is very transformer
*  specific, but the best mental model that I have, which a lot of this I owe to kind of the excellent
*  setup that groups like Enthronomic have done, is a transformer takes in a bunch of tokens.
*  And a transformer is basically a stack of mini neural networks, a collection of mini neural
*  networks where each token gets its own little mini neural network. And within each little mini
*  neural network, there's a bunch of layers where there's a main kind of artery where the information
*  just flows down. And then every once in a while, there's an offshoot where the transformer can like
*  go off and do a little bit of computation to iterate on its understanding of what's going on,
*  and then merge that change back into this like main artery. And large, like small models have
*  like 12 to 24 of these kind of like branch and merge paths within each kind of mini transformer
*  in a token. Their large models can have up to like 100 of these little blocks, but you may
*  have a sentence and for each token in that sentence, you have a little mini transformer that
*  over time continues to iterate on the model's understanding of what the token represents.
*  And then after each like branch and merge back into this artery, all of the arteries of the
*  transformer, the mini transformers can exchange information with each other. And the way that
*  little like token level mini transformers exchange information with each other is they broadcast
*  some information about what information they contain and also what information they're looking
*  for from other mini models, mini stacks of the transformer. And then based on what they have and
*  what they're looking for, they learn to like fetch information from other like token stacks
*  in this transformer. And then they merge those back into the artery. And so a transformer is a
*  repeated cycle of here's some information I have, fetch more information from other tokens, and then
*  do some iterative computation on it. Get more information, iterate on that, get from the patient
*  iterate on that until you get to the bottom of the stack, bottom of the stack. And then that gets put
*  through this like thing called the softmax, which gives you the final probability distribution.
*  But ultimately, a transformer is a thing where for every token, you do a bunch of iterative
*  information processing, and then you exchange information with other mini transformers behind
*  each other. Does that make sense? Yeah, I think the anthropic work that you've alluded to certainly
*  been very influential for me too. I think when you say artery, main artery, synonyms for that
*  would include the residual stream and the skip connection. And I think, I don't know who all was
*  involved with this work, I'm sure multiple people, but I also definitely associate this with Neil
*  Nanda and watching some of his tutorials, where he'll say things like the residual stream, it's
*  really important, man. And you're like, if you say so, I believe you. The residual stream is the name
*  for the artery. And then within each transformer block, the attention is the mechanism by which
*  the little tokenized residual stream exchange information with one another. And then the MLP
*  layer is the thing that actually does the actual, in my mind, most of the actual computation and
*  meeting association happens within these MLP layers. There's a lot of other weird nuances about
*  this. When humans think of all computation step, we think of a discrete mapping from one input to
*  another, mapping from Paris to Eiffel Tower. But it turns out it seems as though a lot of times,
*  this meeting formation may be distributed across multiple blocks over time. And so there's a lot
*  of strange things about exactly what human interpretable computation happens and how it's
*  spread out across all of these mechanisms. But in terms of just the raw bits flowing through,
*  I think that the clearest picture that I've found is the one that I just described.
*  Yeah, that's good. So now let's go back to a little bit more of the practical,
*  how you actually do this work. And then we can go a higher order concept again and talk about some of
*  the capabilities and big questions around what they can actually do and where we're confused and
*  where we're confident about what's actually happening. So, okay, so you've just described
*  a sort of flow of information. You've got this main kind of path, and then you've got these
*  sidebars where the computation happens. There's this attention block, which is the
*  place where each of the mini streams, each token gets its own stream. They can put out a vector
*  indicating what information they contain. They also put out a vector indicating what information
*  they are looking to receive. Those all get crossed, and thus is the information passing from token to
*  token. And then they continue on, and each token kind of loads in various associations that are
*  encoded in the weights. And that's like where the information is stored in some way, some weird way.
*  Okay, cool. So now that has to get instantiated in code. What libraries, frameworks,
*  templates, tutorials do you use to have the right level of convenience and extraction,
*  but also kind of clarity on what it is that you're setting up?
*  Most of the time I'm working in PyTorch on GPU, like Linux instance that I have on AWS
*  PyTorch. I guess the main alternatives to it would be JAX and TensorFlow. It seems like
*  TensorFlow is in a bit of a maintenance mode at the moment from Google, and JAX I think is nice for
*  many other reasons. I guess I should describe a little bit my intuition for what these things are,
*  how they differ. So PyTorch in my example, or in my intuition, gives you the most concrete way of
*  interacting directly with the vectors and matrices. Like PyTorch, when you instantiate any tensor
*  or any matrix or any vector in PyTorch, you can look at the numbers and it's a thing that feels
*  like you can hold onto it. It's a concrete value. And the way you write a program or a model in
*  PyTorch is you have some concrete value and you apply operations to it, which is the way that
*  normal programs are written. The mental model that I have for writing programs in JAX or TensorFlow
*  is it's a little more like a compiler in that you describe the model as a series of computation
*  steps. So you're kind of describing a model as like a function with these 12 steps you apply to
*  the input, or these 96 steps you apply to the input. And then once you have a model, you can
*  compile it and then you can put an input through it and then out comes the output. But it's harder
*  to, there are some affordances for this now, but it's harder in libraries like JAX to just poke
*  inside of a model and say, okay, what is the actual matrix value here? Let me look at all the
*  numbers and let me poke inside of it and play with it because the libraries are constructed that way
*  for performance reasons. If you can describe a model, it's kind of like straight through
*  control flow graph or function way. It's a lot easier to apply complex transformations and
*  compilation steps to this to get higher performance. But the trade-off then is that you can't
*  concretely play with the values. And I think especially if you're doing lots of interpretability
*  work, it pays to just be able to look at a specific value, any random place in the network and say,
*  what does this number correspond to? What happens if I treat this number to be this other number?
*  And for that reason, I think in general, in the ML world, I think between JAX and PyTorch,
*  most researchers use PyTorch, I think. And then if you're from Google or ex-Google or using Google
*  Infra, you use JAX. And then I think in interpretability, things are a lot more skewed towards
*  Torch and these other tools that let you play directly with the values because it just pays
*  to have more observability into the values. My general understanding is PyTorch is basically
*  totally dominant outside of Google and has, for all the reasons that you mentioned,
*  won the open source battle. To what degree do you need to complement that with other
*  libraries? I know, for example, Neal Nanda has a library that is meant for these visualizations,
*  but I don't know how much visualization you're doing of activations as the forward pass is
*  happening versus how much you're able to just get by with the more human readable inputs and outputs.
*  Do you actually spend a lot of time visualizing what's going on inside?
*  I do. I try to. I would a lot more if the tools made it a lot easier. I think the kinds of
*  visualizations that are beneficial for studying autoregressive transformers are slightly different
*  than the ones that are useful for studying embeddings. Parts of the existing infrastructure
*  I can use, parts I have to create on my own. Thankfully, visualizing things is something that
*  I'm relatively better at compared to building models. It doesn't take me as much time to build
*  embedding space or graphically explore a bunch of outputs of a model that I can whip together
*  with some reactant front end pieces because that's mostly what I do at work. This is something that
*  I think holds true for both our work at NoShrim and also my work independently, especially when
*  you're early on in a field or early on in an investigation, which I think I would claim that
*  we are early on with language models in general. Nobody really knows exactly what they're doing.
*  The quality of the tools and how much you can iterate on the tools, I think bottlenecks how
*  much you can iterate on the thing that you're working on with the tools. It pays to be able to
*  quickly tweak the tool or add the functionality that you need to see something new, whether that's
*  a tool that's for evaluating models or running models or visualizing things either in the outputs
*  or in the training behavior. Because of that, I think I've mostly defaulted to building my own
*  little tools whenever I needed them. Then eventually, if I realize that I'm building the same kind of
*  tools a bunch of times and consolidate that into a little library or a little script or something
*  that I can reuse, to me that flow of quickly whipping up something that works and then once
*  you realize it's being repeated, then being able to smoothly trend that into a reasonable component.
*  In some sense, this is all software engineering is, but being able to do that really fluidly,
*  I think is the meta bottleneck. The speed at which you can do that, I think, is the thing that
*  bottlenecks the quality of the tools, which is then the thing that bottlenecks the actual quality
*  of research you can do. A lot of my own work is tools that I've built over time for myself.
*  When there are reusable pieces, obviously, I reuse, but I try not to adopt anything that is
*  very hard to see through. The Hockingface Transformers library is very hard to see through
*  because it's meant to serve a million different use cases and it's meant to host a billion different
*  models. Because of that, there's tons of interaction. It's very hard to just ask a simple question,
*  when the model is at this block, what are all the vector operations that are happening? It's
*  impossible to answer because the answer to the question depends on a bunch of different questions
*  and there's like 12,000 if branches in any single Hockingface function. The conclusion that I'm
*  trying to get to is that building my own tools that are much simpler and just fit for my use case
*  lets me iterate on them quickly and understand what's going on a little better.
*  Just to make sure I understand that correctly, I think I do. It's PyTorch and that is basically
*  a super rock-solid infrastructure foundation. Then after that, it's very little else aside from
*  things that you roll your own to address particular needs and then only selectively build to anything
*  more than just kind of an ad hoc problem-solving addendum. There are pieces that at this point,
*  I've reused enough and consolidated enough that they're like a staple part of my... When I create
*  a new folder in my personal model repo, there are a bunch of stuff that I import by default
*  because there are libraries for UI components that are reused, the look over ready evals on models,
*  training models. If I'm not importing them directly, then I'm certainly copying and pasting them over.
*  One of the things that I've learned in doing more research things over building products
*  is that in ResearchLand, I just do not feel guilty about copy-pasting code because you have no idea
*  how the thing is going to change. It may be that copy-pasting is just kind of like saving
*  you from not having to overgeneralize anything. There's a lot of pieces that I've ended up reusing
*  over time or importing over time, but those tend to be things that I built up over time rather than
*  someone saying, here's a library that helps you do interpretability research and then me importing
*  it and learning how to use that. Okay, cool. That's very interesting. What sort of models do you use
*  today? Obviously, when you started, the available models were interestingly probably much closer to
*  the frontier like GPT-2. I think you started in the kind of GPT-2 to GPT-J era, right? So at that
*  time, you had both way worse models than we have today, but way closer to frontier capability
*  than probably what you can manage to use in any sort of convenient way today. So what models are
*  you using now when you want to do a new experiment? Yeah, GPT-J was the biggest model, open source
*  model that was available when I first started doing this. And then since then, I've like parts
*  of my infrastructure that upgraded to like Mama 2 and stuff. So in general, I think most interpretive
*  research these days are using either like GPT-J. GPT-2 is just like the, there's so many interesting
*  things about GPT-2 is like placed in time and also GPT-3, but it's not open source. It's just harder
*  for people to work with. But GPT-2 and GPT-3 were trained at a time when you didn't have to do a lot
*  of data filtering over the internet because there was no existing language model data. And so it's
*  kind of like pre-radiation steel and that like, it's trained on things that are guaranteed to be
*  not AI generated. And there's a lot of other interesting things about both those models.
*  All of them have my favorite, well documented. It's a little bit like the fruit fly of the
*  language model world. And so GPT-2 is very popular in general. I think a lot of people
*  doing interesting work with Mama 2 or Mama models because they're also popular open source models.
*  I think a lot of serious, more academic interpretive work, especially more like theoretical ones have
*  moved on to this family of models called Pythia, which is specifically trained for
*  interpretability research. The way that it's specifically trained for that is that it has
*  many more checkpoints through the course of training that you can look at. So you can look
*  at how features evolve over time. It's fully reproducible, all the data is available,
*  all the training code is like well known. That's in general, what you find. A lot of my work,
*  because again, I deal a lot of the time with embeddings. I work with open source embedding
*  models, or if I need to do reconstruction specifically, I have a custom model that I've
*  trained for reconstructing text out of embeddings that's based on T5, which also was a cutting edge
*  model when I first trained this model. But obviously now it's not anymore. But T5 continues to be,
*  I think, a very rock solid model for if you want to fine tune or if you want like a medium-sized
*  model to do anything complex. And so I have a T5-based embedding model that I've trained
*  once for this embedding, going back and forth between text and embedding tasks. And then I
*  continue to use that for a lot of different things. And at this point, using that is easy
*  because again, I've built a lot of scripts and tools for working with this particular model.
*  And I have a bunch of data sets that I've generated with this model that take a bunch of time to
*  generate. And so again, I feel like when I sit down to work now, I have a kind of sprawling
*  workstation or little workshop environment where I've put all of the little tools and ingredients
*  exactly where I need them at arm's length. And if I pull in a new model, then I'd have to redo a
*  bunch of stuff. But now that I have a few stable set of models that I'm working with, I can just
*  kind of reach for them and put these together really quickly. And so my custom model is the
*  main one. And then just given the quality and the popularity of either open source embedding models
*  that are at the cutting edge or open-air embedding models, for example, sometimes I work with those
*  as well. How sort of exportable do you think that personal work environment is? Obviously, a lot of
*  people I think are very curious about this kind of exploration and would like to be able to do
*  some of it. And honestly, I include myself in this to a degree. I think I have a pretty good
*  conceptual understanding of most of these questions these days. But I'm not that facile with the code
*  to be able to go in and just run whatever experiment. It's definitely still a barrier
*  for me to have a hypothesis and then be like, I can go run that experiment myself. I would find
*  that to be broadly hard and slow. Do you think that everybody just kind of has no choice but to,
*  if they want to get there, you just have to slog through it and ultimately end up kind of creating
*  your own thing? Or do you think I could drop into your cockpit and learn to fly your plane, so to
*  speak? It's a balance, right? I think there are bits and pieces of my tooling that are in exportable
*  form. Some of them I designed that way from the start. Some of them I've found to be kind of an
*  isolated piece that I can now share. Some of them are under the notion umbrella, so I can't open
*  source them that easily. But some of them I might in the future. My mental model for this, again,
*  is if you're a watchmaker and you have an expert watchmaker and a watchmaking workshop set up,
*  or something, and even if it's an expert in an expert's workshop, you wouldn't expect to be able
*  to just drop into someone else's workshop and then immediately get to work. You either have to learn
*  the way that things are laid out or you have to customize the layout to fit exactly the way they
*  work. Not because the tools are that different fundamentally or anything like that, but just
*  because the things are not there when your hands is used for reaching for them. So more concretely,
*  what that metaphor means in terms of my working style is I have a local GP rig
*  on my desk where I am right now. I have a couple of rigs in the cloud. In those computers, there's
*  a specific folder layout with specific data sets in these places. And I have scripts that assume
*  that those things live where. And I have a script that when the model's trained, they upload it to
*  S3 and all this stuff. And it's kind of a spider web, but it's a spider web that works. The exportable
*  bits are more like if there's a specific problem to be solved. I wrote a little custom mini language
*  model training library for myself to make it really easy and efficient to run a lot of GPT-4
*  inferences in parallel. And those kinds of things are like solving an isolated problem so I can
*  isolate them and then package them and maybe share them. But in general, a lot of the tooling that
*  I've built over time isn't actually solving a particular hard technical problem. It's like,
*  I want this thing to be there when I reach for it, or I want to not have to worry about where exactly
*  my data set is. So it's very much about the ways that things are laid out. And I don't know how
*  much that is shareable. If I was at a company and I had to unify everyone under the same tooling,
*  maybe we could all agree to be like, okay, all the data sets go in this folder, all the model
*  outputs go in this S3 bucket. And then maybe there could be a shared spider web. But in public and
*  open source, I think that's much harder to achieve. How much do you use language models to assist in
*  your personal code writing these days? A lot. But I don't think any more than most other people
*  that I have copilot and have used Chatcha PT. I use GitHub Copilot. I've also tried Sourcegraph
*  Coding. Most of the time they're just useful for writing boilerplate code that you were going to
*  use anyway. And so a lot of times I'll just write things and it'll pause for Copilot to do its thing
*  and then it'll hit tab. They're never really useful for writing code that you're not sure
*  of the correct form. So a lot of time I'm doing complex matrix algebra and the code base and
*  a copilot would be like, hey, here's the exact five line operation that you need to do to finish
*  this function. I don't know if there's a bunch of arbitrary numbers in here. I don't know if
*  this is correct. And so for those, I'll either work it out on paper myself or I'll frequently
*  do this thing where I give some sample code to GPT-4 and I'll ask it, can you find the bug in this
*  code? And if there is, it'll find it. If not, it'll say, I don't see a bug in this code. That gives me
*  some confidence. But ultimately all of those are kind of an accelerant. And I think that you always
*  have to do the final verification of running the code and seeing that the output is exactly what
*  you expect, which again is where PyTorch is much better suited than other more opaque tools, because
*  when you're debugging things, especially you can print the outputs in every step and see exactly
*  whether the outputs matter to expectations. So let's zoom out again or go up a level and talk
*  about model capabilities. I mean, I guess maybe one little tiny follow up before we do that,
*  that definitely relates is what scale of models are you using? And do you have any concern
*  about needing, how concerned? I guess you have some, of course, but how concerned are you about
*  upgrading the core models that you work with to kind of make sure that the investigations you're
*  doing are on the most relevant systems? I mean, this is something that we've mentioned
*  Anthropic a couple of times. And as I understand it, a big part of the reason that they feel it
*  necessary to train frontier models, even though their founding ethos is very AI safety centric,
*  is that they feel like they can only do the frontier interpretability work if they have
*  frontier models and they just feel like they're qualitatively different. So I'm kind of
*  transitioning into the qualitative, potentially qualitatively different capabilities that the
*  latest systems have and wondering to what degree you feel like you need to run the latest models
*  to have those, whatever those may be, to make sure that they're happening on the system that
*  you're studying. Most of this is speculation based on the things that we know about smaller models.
*  And so that umbrella caveat applies to everything that I will say next. I think there are two kinds
*  of categories of facts that we can try to learn about models. One is things that we can learn about
*  how neural networks work in general, or how transformers work in general when trained under
*  a particular objective. So this is more like the physics of a neural network under training.
*  An example of something that belongs to this category is like the linear feature hypothesis,
*  where we generally, a lot of current interpretability work is happening under
*  the assumption that models represent specific facts it knows about the input as a kind of
*  direction in its vector space. That seems like the kind of thing that if you can
*  either theoretically demonstrate in a kind of like rigorous mathematical way, in a proof,
*  and if you can also observe in smaller models, it seems like you can make a pretty good assumption
*  and conjecture that it will generalize to larger models. And I think a lot of my work is mostly
*  predicated on that kind of thing, where it's about the physics of how these systems behave.
*  And so even as you scale systems up, the way that models represent things and the way that
*  information flows to these models are probably going to stay roughly similar. The other category
*  of things that we can try to know about models are for a given specific model, what are the
*  things that it's doing and what are the things that it knows? So for a specific model, what are
*  the kinds of features that it's recognizing in the input? What are the kinds of circuits that it has
*  that is used to implement? How large are these circuits? What is the distribution of features?
*  Are most features about topics versus most features about grammar? Things like that. And I think
*  that's something that that's the category of facts for like we have some of this, but we have very
*  little to go off of for projecting forward to say what would the distribution of features look like
*  for like a hundred billion primary scale model? There are interesting analogs and vision models
*  that I think where there have been interoperability work going on for a longer period of time,
*  where something that's interesting about smaller vision models is that there's a kind of a sweet
*  spot when you have very small models that are not super capable, the features that they use to
*  represent inputs tend to be very not interpretable. And then as you scale them up, there's a kind of
*  sweet spot where the features tend to be the most human interpretable. You can see features like,
*  oh, this is a cat, this is a dog ear, this is a wheel of a car. And then perhaps as you scale
*  the models up further, maybe it's possible that the models think in terms of even higher level
*  features that don't necessarily correspond to the way that we conceptualize the world.
*  And so that's the kind of thing that changes with scale. And that's the kind of thing that I expect
*  we'll see in language models also. But if we, so there's some interesting, like I think opening
*  has done some interesting work in this space of how do you supervise and interpret and understand
*  models, even under the assumption that they are using, they are thinking in terms of things that
*  humans don't have words for, but a lot of my current work is in terms of how information flows
*  through models and how models represent information. And I think for that, there
*  are pretty solid assumptions that I think will hopefully generate solution models.
*  So how do you think about some of the, I mean, here are some hot button topics or, you know,
*  kind of a flash point vocabulary words, things like reasoning capabilities in frontier language
*  models, how, you know, obviously the one extreme view is it's all just correlation and there's no,
*  you know, quote unquote real reasoning going on. It's just statistical association and, you know,
*  they're all stochastic parrots. My sense is to put my card on the table, I think that is not really
*  true at the frontier. And it seems like I've seen plenty of interesting examples of problem solving,
*  you know, that seem to be meaningfully outside of the sorts of token level correlations, you know,
*  that might be expected to be found even in like super broad training data to support that. How
*  would you give an account of like reasoning abilities or things like grokking or things
*  like emergence as we go to these frontier scales? When we talk about what models can do,
*  I think there are three levels at which you can ask this question. Level one is does there exist
*  a transformer? Is it possible to have a transformer model that accomplishes this task? In other words,
*  if you were on an omniscient being and you knew how to set every single parameter in a large
*  transformer, could you manufacture a transformer that did this task? That's level one. Level two
*  is, is it possible for like a reasonably randomly initialized transformer model to, through some
*  gradient descent based optimization process, arrive at a set of parameters that accomplish
*  this task with the model? And then the third level is when we are training language models
*  in the real world with limited precision floating point numbers on internet scale data,
*  will the resultant model be like sufficiently close to the ideal model that it performs the task?
*  And I think for most definitions of reasoning and like problem solving and generalization,
*  the answer to one, the part one is like almost always a yes. I think for any given
*  logical deduction problem or any given math problem, it is, I think it's generally possible
*  to like, given lots of parameters, write a program inside a transformer, manually engineer all the
*  parameters and have a model that's capable of doing it. My intuition, non-rigorous intuition,
*  is that given sufficient data and sufficient time and sufficient compute, it's probably possible
*  to also like train transformers in the infinite compute limit that do any arbitrary like confusing
*  task. I say that because for like non-trivial math problems, if you have enough examples,
*  you can train very small transformers to like fully solve them, not fully solve them just in
*  the sense that you can give it a bunch of unseen problems and it will solve them also, but fully
*  solve them in the sense that if you look inside a transformer, you can see how the algorithm is
*  implemented inside the transformer and you can show that that is like the correct algorithm that
*  always generalizes. So I think in a lot of cases, it's possible to have a transformer that through
*  grading set arrives at something that we would call like reasoning. The big question that I have
*  personally in my head is, do we have enough data to train on such that for these extremely large
*  models that have so many parameters, we could train them sufficiently long that they would go
*  from starting to memorize to eventually starting to like looking like something that we would call
*  like fully reasoning rather than relying on a mix of reasoning and showing correlation. I think that's
*  a big challenge. I think it's also very difficult to show in extremely large models currently that,
*  for example, a model solved this problem by reasoning it within a circuit in some way over
*  kind of like pattern matching because the diversity of the problems that we're going to show it for
*  is really large and because there's so many parameters and relative to the number of parameters
*  that we have, I think the data sets that we're using are so relatively small. And so it's very
*  possible for models to like mostly memorize and still do really well. And so I don't know if we'll
*  ever get to that point because data is really messy. And I think to get to the regime where
*  you train a model and you can show that the model is perfectly generalizing or perfectly reasoning,
*  I think you need extremely clean data that basically only does the correcting all of the time.
*  And you need that for a long enough period that the model to anthropomize it a little bit feels
*  comfortable forgetting its memorized solutions and only relying on this generalized solution.
*  And so there's a lot of issues, I think, in terms of like practically can produce models that
*  we would be able to show is reasoning. But I think it's in theory possible to have models that do
*  this. And perhaps with like research breakthroughs, we will get better at closing the gap between like
*  options two and three. I think one of the best, certainly the best thing I did and one of the best
*  conversations I've had about a topic like this was an episode that we did with the authors of the tiny
*  stories paper, which was out of Microsoft Research. And Ronan and Juanchu, they did something
*  where they observed kind of that the order of learning seems to be like syntax first,
*  like just part of getting the part of speech right from one token to the next, then kind of
*  facts and associations, and then reasoning. And so in order to like try to get to reasoning,
*  well, this is at least you could frame their work differently. This is maybe not their exact framing,
*  to be clear. But the way I've thought about it ever since is to get to that reasoning starting
*  to happen as soon as possible. And at the smallest scale possible, they created this vastly reduced
*  data set called tiny stories, which is like stories that are short and that like, you know,
*  I don't know if it was a three year old or a third grader, but whatever, like reduced vocabulary,
*  you know, pretty simple little universe. But because the vocabulary size was way lower,
*  and the like facts that you might encounter were also greatly reduced, then you could start to see
*  some of these like very early reasoning abilities starting to emerge, even with just like a few
*  million parameters. I think the biggest model they created was like 30 million parameters.
*  And by the time they got to like 30 million, which is still, you know, whatever,
*  3%, 2 to 3%, maybe the size of GPT-2, they were starting to see some of these like, very, you know,
*  simple but like negation, for example, you know, GPT-2 really struggles with it, but they were able
*  to observe it like somewhat consistently, at least in their very small models by just like reducing
*  the world. I have a big expectation that curriculum learning in general is going to be a big unlock
*  for this. And I kind of, you know, we've heard from OpenAI and others, I think, at this point,
*  too, that like training on code really helps with general reasoning ability. My sense is that
*  at this point, they're probably doing a bunch of stuff like that. And kind of, you know,
*  much like that paper we saw also recently from DeepMind on the geometry, where they like generated
*  a ton of just like provably correct geometry statements and said, okay, we're going to start
*  with this. And then you'll like kind of learn what a correct geometry statement looks like.
*  And then we'll like apply you to this problem. I sort of suspect that the data sets at the
*  Frontier Labs these days have a lot of just like pure reason, you know, kind of, especially in the
*  early going when they're trying to establish these like core reasoning circuits. But that's on, you
*  know, somewhat speculative authority for sure. I think it's something that's related to this that
*  I thought about recently is on OpenAI's new video model. This is purely observational speculation,
*  but sometimes you look at the motions in the videos that are generated, or the lighting or
*  the shadows, and it looks like a video game. And partly based on that, mostly groundless
*  suspicion, and partly based on this confidence that I think we both have about the importance
*  of synthetic data. I think they're probably training on at least early in training on a
*  huge amount of just like a game engine generated physics and motion and movement. That's another
*  example of synthetic data. Tiny stories is also super interesting. And I think it's an example of
*  like, in general, as you said, models are very lazy about what it has to learn. And it only learns
*  the thing that you want it to learn when it's run out of options. It's exhausted all the other
*  options that it has to try to minimize its loss. And the only remaining option is to like finally
*  learn the thing they wanted to learn. In language data broadly, I think it's so difficult to get to
*  that point. Even if you think about the math proofs that occur naturally in the internet,
*  for example, there are a bunch of proofs on the internet that are just incorrect. And so in order
*  for the model to perfectly learn how to solve a math problem, it has to first or at least
*  simultaneously also learn how to disambiguate whether the proof that follows some text is going
*  to be likely to be wrong or correct. There's a bunch of noise like this that I think either you
*  can have relatively small amounts of very high quality synthetic data, or you can have vast,
*  vast amounts of like in the trillions of tokens range of extremely noisy data that is only kind
*  of filtered. But to get to getting these very large models for reason in the way that I think
*  humans want to reason with natural language, I think it's going to require bridging the gap.
*  And that's a really interesting data problem for sure.
*  In lightning round. So we've just been talking about these kind of, you know,
*  what exactly are the current frontier capabilities, you know, exactly how much reasoning is going on.
*  I agree. It's hard to say. I think if I could summarize our relative positions, I think I
*  probably see more reasoning in it than you do today. Although it sounds like we're together in that
*  I definitely don't think of it as a binary. It is very, for me, like, it's not that it's all this or
*  all that. I always say AIs defy all the binaries we try to force them into. And instead, it's like
*  some mix, right? Like I would say, it seems that there are times when it can reason and there are
*  other times when it can't reason. And, you know, mapping that boundary, which, you know, by the
*  way, might be fractal from for some other results we've seen recently is like definitely a super
*  hard challenge to get practical on this for a second. So you're obviously working at Notion AI,
*  a product leader there and bringing frontier models to the masses. You've shared in detail
*  and in other places, you know, some of the functions and gone into how you're building it.
*  I really liked the podcast you did with Redpoint, by the way, for those that want to get into the
*  how Notion is made. I thought that was a really good one. So skipping over all of that kind of
*  stuff and now just saying, okay, for the stuff that it's not able to do yet, as well as you would like
*  and as well as you would hope to provide to Notion users. What do you tell the model developers
*  are the shortcomings? Like where do they need to improve to give the quality of experience that you
*  think, A, like they kind of should be able to get to next and, you know, would be most useful at
*  that intersection of like feasibility and value? I can run down a list, but you could just, you know,
*  respond freeform. This is a list that's always top of mind for me as well,
*  because I talk to all, everyone on the team talks to companies building models and they always ask
*  us this question. The main ones that are always top of mind are we want models that hallucinate
*  less. We want models that are cheaper and faster, lower latency, and we want models that follow
*  instructions better. And there's a fourth one, which is like a big one, but very hard one,
*  which is like we want models that are better at shit always. All three of these, so not
*  hallucinating, lower latency and following instructions more faithfully, following complex
*  instructions more faithfully are, I think they are all areas where, for example, Clotoo or GPT-4
*  have shown market improvements over the previous generation models, except for obviously they're
*  both more expensive. But I think those, the combination of those three or a couple of those
*  three have enabled entirely new kinds of products. So for example, Notion has a product called Q&A
*  that helps you answer questions based on all the information in your knowledge base. And to do that
*  requires both not hallucinating as much, not just from its own memory, but from information that it
*  has read in its context. But it also requires following extremely complex instructions because
*  we have massive books of instructions metaphorically that are just like dozens and dozens of like
*  bulleted lists of here is how you should format your answer. Here's what you should do. Here's
*  what you should not do. Here's exactly what you should do in this situation versus other situation.
*  And earlier models have had a lot of trouble following that kind of like a thousand, two
*  thousand, five thousand token long instruction. And so long instruction following, I think is like
*  an area where we've continued to see improvements even in the latest iterations of GPT-3.5.
*  And it's very essential. Pollutionation makes a lot of sense. And then just as instruction
*  following enables a bunch of use cases that were impossible before, I think latency, lower cost and
*  faster latency enables a bunch of use cases that were hard to pull off before. Notion also has
*  a feature called AI autofill where you can use a language model called kind of like an Excel formula
*  where you have a data table or a database of interviews or companies or customers or like
*  your classes or whatever. And then instead of filling in a column with like a formula,
*  you can fill in a column with like language model prompts. And to be able to do that at the scale of
*  tens of thousands of rows that some of our customers have in their tables requires models
*  that are both fast and late and also efficient because we want to be able to send OpenAI or
*  Anthropic thousands of these requests in a matter of like a few minutes and have them be
*  fulfilled reliably. And so that's an example of a use case where as the model is good to you to get
*  better at this like perimeter frontier of latency and cost versus capability, we're going to continue
*  to be able to make new kinds of products. I often have this debate with product people where I say,
*  you got, I think it was in your fourth or fifth spot before you got to general,
*  general reasoning ability, general kind of capability. I always put that first.
*  And I said that as somebody who's also like kind of scared of an AI that's smarter than me.
*  But definitely I feel like on my personal utility, you know, the results that I get day to day,
*  I'm always like, it's pretty fast, you know, and it's pretty cheap. It would be nice if it was
*  faster and cheaper. But like what I really want is for it to be smarter. What I really want is for it
*  to like, right as me better, you know, better in context learning or better kind of style
*  imitation on the fly. So it can kind of put something together in the way, you know, or at
*  least close to the way that I would want it. Why isn't that like the very number one thing? I mean,
*  if you had that, couldn't you charge like hundreds of dollars a month for notion AI? Is there
*  something I'm missing about that? Part of the reason why that's at the end of the list is because
*  it's, I think it's much harder to get to basically this again, obviously this is something that new
*  models continue to get better at. And I think like between going from GPT 3.5 turbo to GPT4,
*  for example, we saw improvements in how like how people were using it and the quality of feedback
*  that we were getting. Better reasoning is like, is obviously equal, but also if we go to like
*  Google and say, Hey, we want models that are better reasoning, their engineers are going to be like,
*  what do we do with this? What do we do with this piece of feedback? Like, obviously we're trying
*  to make models out of their reasoning, but how do we measure that? What exact kind of reasoning?
*  And so in some ways, following instructions and not hallucinating are facets of reasoning that I
*  feel is most tractable in like a few months to a year timeline. And also to have the unblock,
*  the most urgent current like problems with the existing products that we have. Another way to
*  look at this is I think a part of your desire for better reasoning is a function of the way that
*  language models have been packaged for you, which is you interact with it in a single threaded way,
*  one at a time as the model is generating the tokens in real time. And you ask it questions.
*  And I think there's a lot of other ways that language models can be used that isn't packaged
*  that way. So for example, the autofill feature that we mentioned, that's a bulk operation.
*  Someone might upload 2000 rows CSV and fill in five different columns. And wouldn't it be better?
*  First, wouldn't it be good if you could do that, which is a cost problem. And then wouldn't it be
*  good if you could write a prompt, run that in a few seconds later, have the entire table filled,
*  and you can filter it by category or feature or where people are. And those kinds of experiences
*  are not really bottlenecked by reasoning. Most of the time they're bottlenecked by things like speed
*  and latency. And especially if you're trying to do this at the scale of billions of tokens generated
*  per day, this is a huge, huge problem. There are categories of products that, for example,
*  smaller startups might be able to launch, but we might not be able to launch just because for us
*  to deliver that same thing would cost us enough money to not be feasible. And then I also think
*  there's a lot of useful work that I always kind of joke that most business documents that most
*  people write or most academic documents that most people write are just interpolations between other
*  business documents that have previously been written before. And so for a lot of the, I think
*  it's like 95% of all documents that are being written inside Notion, not because there's
*  nothing novel in there, but just because, you know, given enough information and diversity and
*  all the emphasis that these models have seen, most instances of like problem solving or doing
*  important work, communicating well are like within the training set. And so for those, I don't actually
*  think the biggest problems are like getting the model to reason outside of what's already seen,
*  but just being better at following instructions so that we can steer it towards the right space
*  and the space of components that are already seen. Perfect transition to my next question around the
*  next big model upgrade. You kind of alluded to it a little bit, but what does that look like?
*  And, you know, because one of the big theories I have right now is that we have as an industry,
*  as an AI app industry, if you will, we have been building a ton of stuff that basically
*  tries to compensate for the language models weaknesses, right? We're like, they hallucinate,
*  so we ground them in database access. They have very limited context, so we got to like
*  re-rank the results to try to make sure we're getting the right stuff into context. Obviously,
*  we have, you know, every part of that pipeline can fail. And then, you know, you might just have
*  something come along that like changes the game. And maybe it just did in the form of Gemini 1.5
*  with up to a million and maybe up to 10 million tokens of context and like some pretty
*  wowing recall demos. I guess, first of all, I'd be interested to hear like kind of what process
*  you plan to go through. I'm sure you have like a standard set of evaluations that you would,
*  you know, get like systematically comfortable that like, okay, we're not regressing. I'm interested
*  to hear what that's like. But then I kind of also wonder, do you see that the next model like a
*  Gemini 1.5 could perhaps lead to a significant leap in performance given all that scaffolding
*  or possibly even like make some of that scaffolding kind of not necessary anymore?
*  Like, do you think the system itself maybe gets simplified because the new model just like is more
*  tolerant of just, hey, just throw some more stuff in it. You know, we don't have to work so hard on
*  some of these previously hard problems. I'm very curious what use cases motivated million token
*  context window for the new Gemini models. My hunch is that it's actually mostly multimodal use cases.
*  I could imagine a long piece of audio, a long piece of video filling up the context,
*  but I think most of the time if you're purely in the text realm, I think it's difficult to imagine
*  there's a lot of benefits of retrieving limited context rather than just putting everything in a
*  model window. Some of them include observability. So if you give the model 10,000 inputs and it
*  gives you the right answer and it gives you the wrong answer, how do you debug that? Right? Maybe
*  you can look at things like attention maps and so on, but it's like that is an interpretability
*  problem in itself, where if you have a pipeline that gives you maybe that top 10 documents and
*  has a language model answer that, answer the right question, if you've got it wrong, you could ask
*  useful questions like did the answer exist in the documents that it saw? Was it at the beginning or
*  the end of the context? If you swap this out, does the model get a different answer? And so having
*  a more pipeline system, I think helps you debug. I think it helps with costs, obviously, and latency
*  for a given compute budget. I think it also lets you incrementally upgrade different parts of the
*  system. So having a better language model while keeping the same retrieval pipeline versus having
*  a better retrieval pipeline with the same language model, both improve the results. So I think there's
*  a lot of just structural benefits to having this pipeline model. And on the Gemini results in
*  particular, they have a lot of these tests that are kind of needle in the haystack test. So if I
*  have a million tokens, there's an example of an anomaly somewhere in the million. Can you
*  find it? And in the real world, a lot of the kind of complex retrieval that models have to do is
*  actually so much more nuanced. An example of something that more nuanced could be like a couple
*  of examples. One example is the model might have to not just find the information, but do some
*  reasoning to figure out which of the pieces of information to use. Like in Notion's case,
*  in the retrieved documents, some documents may be out of date. Some documents may be written by
*  someone who's not authoritative. Some documents may be written in a different language and it
*  might conflict with the information written in the canonical document written by the HR team
*  in a company or something like that. And we have instructions for how to deal with all of these
*  cases. And so the model has to do some reasoning over exactly what. And that looks very different
*  than just like find this word and some tokens. Another example of a more complex retrieval case
*  is when there needs to be synthesis. So if you ask a question, if you're in the Notion,
*  internal Notion, and if you ask a question like, has the AI team been productive this week?
*  That's a multi-step question that not just, first of all, that requires knowing not just a single
*  answer to a question, but in general what's been going on. And then that requires like maybe
*  reasoning through, okay, what does it mean when this person is productive? Who are all the people
*  in it? Maybe are there people that are out of office? And so again, a lot of problems there are
*  not just about like all the, what information is in the context, but actually how the model performs.
*  And the biggest challenges that we've faced so far in optimizing retrieval is mostly
*  those kinds of things, those kinds of more like reasoning related or edge case situations where
*  it's unclear exactly what the model should do based on our existing instructions. And the best
*  ways that we found to attack those problems involves a lot of like stepping through all of
*  the steps in the chain and saying, what's the answer found at this step? What's the answer found
*  at this step? And all of that debugging is just much easier when you have like 10 examples to look
*  at instead of 10,000. So at least for this particular use case, I think context-length is
*  not the most dire need, but obviously there are lots of other use cases, like for example,
*  audio, where I think it could be a little changer. Yeah. Very interesting. I'll be very keen to spend
*  more time figuring out exactly what I can do with a million tokens and totally agree with you that
*  the needle in the haystack results that we've seen are not enough of an answer to how it really
*  performs to be confident just dropping it in. Although I aim to find out exactly how far this
*  thing might have advanced. And it does hold a lot of promise for me just because first of all,
*  this podcast might be more than like GPT-4 Turbo or Clawed 2 can really handle. It probably would
*  fit, the transcript probably fits in the 128K or certainly would fit in the 200K, but it's getting
*  to the point where the recall isn't great. And just to be able to take my podcast transcripts
*  and throw them into something and get reliable answers that I feel are better than I could
*  delegate an answer pretty reliably, that alone is super exciting. And then it'll be really interesting
*  to see how the synthesis part of that works with those. Yeah. There's a part of me that wonders,
*  training a model of such long context requires probably architectural inventions,
*  probably some engineering work, definitely a lot of extra data work. There are only so many
*  examples that are high quality that are that long. And so there had to have been some good
*  use case motivation for Google to go ahead and train that model. And I'm very curious,
*  even just internally what they're using that context into work. Yeah. Agents, I think is going
*  to be one also super interesting application. To what degree can you just append your past failures
*  and continue to roll forward in a sensible way, learning from what happened today? Obviously,
*  you can't just drop all your API failures into a single context window. You'll run out,
*  just to run out even the 10 million eventually, but it could make a big difference for that sort
*  of thing. How much is any big tips that you have for AI app developers, things that you know to
*  work that you just don't see people doing enough of? This could be in the prompting domain. It
*  could be in the rag domain. It could be in how people set up their evals or even just the user
*  experience and the interface that are presented. Both of these are kind of boring things, but I
*  think they're not, you could always be doing more. The first is regardless of what exact kind of
*  model you're training or working with, obviously it always pays to spend time with data. And I
*  don't just mean like run an evaluation, look at the charts. I mean like- Read the logs.
*  Exactly. Make the table of like a hundred outputs and a hundred inputs and ask yourself,
*  for this input, what output would you, the human, generate? And then think about what all the steps
*  that you go through and reason through that and look at edge cases, look at what the models fail.
*  I've also found it just personally interesting, if a little dubious in value, to look at pre-trading
*  data, like raw pieces of text from the pile data set. There's a lot of stuff in it. Most of the
*  text on the internet is like quite garbage. And there's a lot of stuff in there that I think
*  gesture at, for example, the reason that language models are good at certain kinds of output
*  formats and not in other formats. But the general theme I think is spend a lot of time with your
*  data, in particular with your input data that you're giving the models and the tasks, and then also
*  with failure cases in the wild. In the beginning with Notion AI, we spent some time setting up a
*  system for us to have human annotated logs and a more scaled automated system for detecting errors
*  and fixing them. And eventually what we've settled on for a lot of our features is instead, we have
*  the engineers have scheduled time on our calendar every week where we go into our meeting room and
*  we just stare at a Notion database of all the bad cases, like individual outputs that were bad,
*  that were reported by our users. So we ask ourselves for each input, what is the exact
*  step in the pipeline where this failed? What category does this belong in? We kind of treat
*  it like a software bug and we say, is this already being fixed? Is this an instance of a new bug?
*  Is there a systematic issue in a pipeline that requires us inventing something new to fix this?
*  And so spending a lot of time with failure cases and data, I think pays off. And then on a similar
*  theme, I think investing early in internal tools to quickly run evaluations, quickly and easily run
*  evaluations, quickly and easily generate synthetic data sets, visualize outputs, sort through them.
*  I think that helps a lot. And there are a few companies out there doing stuff like this.
*  I think for working with your own data and visualizing it in particular, that generally
*  the tools shouldn't be so complex that you can't just have an engineer whip it up in a couple of
*  days. And I think that pays off in the long run by you being able to customize it over time,
*  as I alluded to before. So that's kind of what we've done at Notion. Obviously, your mileage may
*  vary, but I've found those two things to be particularly worth our time in terms of improving
*  the product. I think those are very solid tips. And I agree with you that while it may be sort of
*  not exactly what people are looking to hear the admonition or reminder at a minimum to
*  read the logs, just look at the raw data, look at the failure cases. I have certainly been served
*  extremely well by that over time too. There's just no substitute for looking at the raw inputs and
*  outputs. Once you understand the problem at a deep level, then you can start thinking about
*  like, we're running out of time during the week to do this. How can we scale this out?
*  How can we automate this? But the automation is not really possible until you have a solid
*  understanding of exactly what you're trying to monitor for or automatically fix or protect.
*  Yeah. Okay. Cool. All right. Last section of things that could possibly get weird.
*  Two big trends. I'd say one kind of predates the other a little bit, but both are increasingly
*  well-established at this point. One big trend is that it seems to me like all the latent spaces
*  can sort of be mapped on one to another. We saw this kind of, arguably first in a really powerful
*  way with Clip, where image space and text space were kind of brought together. Now we have text
*  image space, like amazing. But that was done in a high-scale way. Then it wasn't too long after that
*  that we got things like, for me, blip two was really a major moment. I'm sure it wasn't the
*  first, but it was one of the first that I really read and understood deeply and realized that,
*  holy moly, they've got a frozen language model here and a frozen image model trained totally
*  separately. Then just a small bridging connector model between them that just took a couple GPU
*  days to train is enough to unlock, even that was beyond clip level capability. But we just see so
*  many examples of this now, where one latent space to another, often just a linear projection,
*  sometimes a small connector model is kind of all it takes. Then another big trend has been the
*  realization that a lot of models can be kind of merged together in seemingly unprincipled ways,
*  or not very principled ways. We've seen some going back to, I think it was called relative
*  representations, was a paper that showed that models initialized differently, trained with
*  different shuffles of the data or whatever, still seem to converge on pretty consistent,
*  kind of isomorphic representations of data that are maybe a rotation away from each other,
*  or maybe a dilation and rotation away from each other, but ultimately look very similar in
*  visualization. Now we're getting to people saying, well, hey, what if we just train model A over here
*  on one data set and B over here and just add their weights together? It's like, wait a second,
*  that works? It doesn't maybe always work, but to a surprising degree, these sort of
*  things are starting to work. So you can comment on that in any and all ways, but the way that I'm
*  most interested to ask you about is, is there a risk or a concern, or maybe you would see it as a
*  good thing, that AI systems may start to communicate between each other in a higher dimensional, more
*  embedding mediated way or middle layer activation sort of way, as opposed to through
*  different forms of communication that we could actually read in a native way.
*  It seems like the models don't really need to generate text to send the text over to one another.
*  Instead, they probably are going to perform better with high dimensional vector communication,
*  but I kind of worry about that at the same time, even as it may boost performance in various ways,
*  I kind of worry that like, much like you said earlier, with the, how do you debug that?
*  You know, now it's like, well, I can't even read the messages that they're passing back and forth.
*  So how big do you think those trends are? Are you excited about those trends? Do you see,
*  you know, downsides with the upsides, you know, all things about kind of weird
*  embedding based communication and model merging? Yeah, model merging is like truly weird and I
*  don't have a good principle and understanding of exactly why it works so well the way it does.
*  I have a general intuition of like why it works decently, which is that a lot of these models are
*  fine tuned from a single base model. And when you fine tune these models, especially in tasks that
*  look similar to the original task, like mostly doing natural language continuation, the models
*  mostly tend to exist in a kind of like linear subspace of the original like model space.
*  And so when you merge them, you're mostly doing linear interpolation between weights of these
*  models. And so it makes sense that perhaps it makes sense that the resulting model will just
*  inherit behavior between a bunch of different models. It's still very weird, but when you view
*  it that way, it doesn't seem quite like black magic. It just seems like kind of something that
*  we have to understand. Relative representations and other kinds of projections between spaces,
*  I think are really, really cool. It's cool, obviously, at a theoretical level. I think it's
*  also really cool to observe it at a technical level, an empirical level. One of the other
*  experiments that I did late last year was to find mappings between embedding spaces. So I had a
*  model that was capable of inverting and finding features in one embedding model, and then I just
*  trained an adapter between OpenAI embeddings on my model, and it was a linear adapter, and I could
*  start to read out OpenAI embeddings, even without spending so many tokens like training an OpenAI
*  custom kind of inverter. So all of these things, I think, are super fascinating. I think
*  where I place this technique in the kind of like pantheon of all these different things you can do
*  with language models is a parameter efficient or compute efficient of fine tuning or of customizing
*  a model where instead of fully tuning a new image to text model or fully tuning a new way to go,
*  new way to invert an embedding, you could take in a model that's close enough in what it represents
*  and then maybe tune some few parameters to get to the final destination. To your question about
*  whether models will communicate in latent spaces, if you think about it, GBT3 is just kind of like
*  100 GPT2s talking to each other in activation space. Obviously, it's not quite that. The density
*  denser connections, but if we can manage to precisely understand exactly how different
*  layers in a transformer or different token residual streams in a transformer communicate
*  with each other, I think a lot of those techniques will definitely generalize to understanding like
*  mixture of experts models or understanding ways that fully tuned models like the two that you
*  mentioned communicate with each other through kind of like mapping a representation space.
*  In some ways, it's actually easier because unlike a transformer residual stream where the concepts
*  that it may be representing could be really weird, you can imagine a concept that's really
*  useful for predicting the next token in a Python program, but not really useful for humans in
*  general in life. A lot of times when you're mapping between kind of like fully formed representation
*  embedding spaces between like an image embedding space and a text embedding space, I think most of
*  those, I intuitively expect most of those concepts to be pretty human interpretable.
*  And so a lot of the kind of mechanistic techniques that I think people are working on today will
*  probably generalize to understanding them. And so I just view it as kind of an exciting, efficient
*  way to build more interesting systems. How weird do you think things might get over the next
*  couple of years in general? I mean, it seems to me like we're headed for at least one more and
*  probably more than one more notable leap in model capabilities. And I feel like I have a
*  sort of rough intuition for what GPT-5 would be, which I might broadly describe as like
*  smarter, to borrow a word from Sam Altman, better general reasoning capabilities and
*  probably more long-term coherence as another big aspect of that. They've seen how many people are
*  trying to make web agents and various kinds of agents on the platform and it's just not quite
*  working. So I would expect to see smarter and sort of more readily goal-directed
*  as kind of two big advances for the next generation. Beyond that, it starts to get honestly kind of
*  hard to figure out what would even happen and what it would mean. But do you have kind of a
*  sense for like, how big is your personal Overton window or kind of cone of possibility for the next
*  few years? Like how far do you think AI might go in a few years time? I mean, everything
*  monotonically improves from here, right? I think that's the scary part. MKBHD has this good video
*  on Sora where he hears this phrase of like, this is the worst that this technology is going to be
*  from here on out. And I think that's a really succinct way of expressing the fact that like,
*  okay, maybe you think GPT-4 is like not super, super, super smart, but like this is like,
*  if you look back at the history of smartphones, every phone when it came out is the worst that
*  smartphones are ever going to be from that point on out. And it's like only gotten monotonically
*  better. And I think when you think about that, I think language models monotonically improving
*  so rapidly from here and out, it's like as a trend line, I think it's interesting and scary.
*  Long-term coherence and I think goal-directedness in particular is really interesting.
*  Right now with every GPT iteration, I think OpenAI has done a little bit of not just making the
*  model, the base model smarter, obviously, but some opinionated tweaks to the final tuning objective
*  to make the model more useful for some kind of use cases. Obviously, the most recent one was
*  like API use before that it was chat, but I could imagine OpenAI or other model makers tuning their
*  models to be better at kind of not just having the model to expect the world to end after the
*  next turn in the conversation, but expecting that there's further turns and maybe planning for,
*  okay, if I assume that I'm given infinite trends into the future, what might I start to do? So that
*  kind of like long-term planning, I think some of that's missing in current models that make it very
*  hard to use for agents. So I agree a lot with that. And then beyond models themselves,
*  there's obviously lots of corners of culture that these models touch. And I think that's a much
*  harder, much more complex like dynamical systems. So I think it's much harder to predict exactly
*  what will happen like to the concept of copyright, for example, or even to our concept of exactly
*  what a single piece of creative artifact is. There's a really good TEDx talk by creativity
*  and HCI researcher, Dr. Kate Compton, where she talks about the idea of an image generation model,
*  not just like when a human produces a piece of art, you make the thing and then it's just like
*  that is the concrete object. But when you have a model that's capable of producing a bunch of
*  images to a single piece of text or like millions of images at once, one way to look at it is some
*  of the models just producing art faster than a human. But a different way to look at it is the
*  model is a tool to map out the space of all possible outputs of a certain style of art or
*  to a certain prompt. And so it starts to kind of change exactly what we imagine a single piece
*  of artifact to be from like a single blob of pixels to like, here's now a kind of subspace
*  of all possible outputs that as a bundle is a form of creative expression. So there's a lot of culture
*  stuff that I think it's just much harder to predict that I'm like frankly not equipped to.
*  I have too much smart commentary on, but I think it would be very interesting to watch
*  and probably have ripple effects beyond the molecule. Do you have a sort of positive vision
*  for the future for just like your own life? I find that this is in very short supply and certainly
*  you've been one who has been so up close and personal with the AIs as they've developed.
*  You might not, but if you do, I'd be interested to hear your sort of day in your own life,
*  three years from now, five years from now, what is AI doing for you? What are you able to do that
*  you couldn't do before? Who knows what Hollywood's doing or how the entertainment industry has
*  evolved, but what does the day look like for Linus as things really start to hit
*  the key thresholds for utility? The high-level concept that I gravitate towards
*  when I think about this is like, you can take a base technology and express it in a way that's
*  agency taking or agency expanding or agency amplifying. An example of a tool that takes
*  away agency from a human is like a dishwasher, but that's fine because I don't actually care about
*  creatively washing my dishes or exactly which order I wash my dishes. I just want them washed
*  or like a laundry machine or a car maybe. And then there's a bunch of technology,
*  ways of packaging technology where preserving agency really matters. A writing tool is an
*  obvious example, but maybe also more subtle things like which emoji show up first in an emoji
*  keyboard or predictive text keyboards or obviously social media algorithms. These are kind of like
*  somewhere in between agency taking and agency amplifying. And one thing that I'm kind of
*  concerned about right now is that I don't think people are thinking enough about whether the
*  ways that language models are packaged is amplifying human agency or taking away from it.
*  And that's something that I think I want to like talk and think more about and perhaps like
*  push other people building this space to do more, be better at. Assuming that we can steer
*  the way we package language models to kind of respect agency where it is acquired and only take
*  agency where we want the models to take agency, I'm generally a pretty optimistic person about
*  technology and I think I have a lot of optimism for where this leads as long as the way we
*  package these things is more humanist rather than just kind of like automate all of the things.
*  When you look at different kind of AI companies, you see companies situated at different points
*  in the spectrum between you want models to automate things in a way that takes away agency,
*  i.e. replacement, or you want models that amplify. For example, like I think OpenAI is very much on
*  the replacement side. Literally their definition of I think AGI is something like a thing that can
*  take over us as a single like full human's job where if you look at a company like Runway,
*  a lot of their framing of like usefulness or depth perhaps a lot of their framing of usefulness
*  is about extending that agency of what you want to express. So there's a healthy amount of diversity
*  here and I think it's just a matter of who where the winners sort of end up lying. Assuming we get
*  that right, I think I have a lot of optimism for where we're going. It's a big question,
*  but I agree that's a key one. We want to guard our agency probably increasingly
*  jealously, especially the more different AI systems might want to usurp it. That could
*  be a great note to end on. Anything else you want to touch on that we haven't? No, I think we covered
*  interfaces, capabilities, interpretability, all the things I spend my time thinking about.
*  How people can be more like you, of course, a key highlight as well. All right, I love it. Well,
*  thank you very much for doing this. You've been really generous with your time and insights and
*  definitely count you among the must follows in the space for all sorts of new and very generative
*  ideas. So it is my honor to have you and I will say in closing,
*  Lionel Slee, thank you for being part of the cognitive revolution. Thank you. It was my
*  pleasure. It is both energizing and enlightening to hear why people listen and learn what they
*  value about the show. So please don't hesitate to reach out via email or you can DM me on the
*  social media platform of your choice.
