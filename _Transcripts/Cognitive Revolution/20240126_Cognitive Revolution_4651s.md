---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 4651s
Video Keywords: []
Video Views: 1058
Video Rating: None
---

# The Pixel Revolution Part 2 with Suhail Doshi, Founder of Playground AI
**Cognitive Revolution "How AI Changes Everything":** [January 26, 2024](https://www.youtube.com/watch?v=89obYAu92oY)
*  I try to sometimes put myself in the shoes of, you know, let's say the artists or the people making these images, tar or whoever.
*  We were the first site ever, and I think the only site where if there was a prompt on our site and someone references his name, we directly link back to his page.
*  It might be generally okay to make things. You talk about many brands are perfectly fine with fan art or whatever.
*  There's kind of this question of commercial use. That's where things kind of like stop.
*  If this whole thing is very gradual, then I think probably society would find like some way to assimilate to it.
*  If it's vastly faster than that, then I think I think that we definitely need to do something about that.
*  I think that who it's impacting like very much needs to be considered some craft that they've been doing for a decade or two.
*  You can't ask people to evolve skill.
*  Hello and welcome to the cognitive revolution, where we interview visionary researchers, entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture of how technology will transform work, life and society in the coming years.
*  I'm Nathan LeBenz, joined by my co-host Eric Thornburg.
*  Hello and welcome back to the cognitive revolution.
*  My guest today is Suhail Doshi, founder and CEO of Playground AI.
*  This is a special episode for me because Suhail was our very first guest on the show almost a year ago.
*  And today he returns as roughly our 100th guest.
*  Of course, it's been a busy year for everyone in AI and Suhail and team have been hard at work building and releasing a huge number of new features designed to help anyone create and edit images like a pro.
*  Most recently, they've trained and open sourced a new foundation image generation model called Playground V2,
*  which is preferred to stable diffusion Excel some 70% of the time while being built on the same exact architecture.
*  A decision that Suhail made so that the open source community can easily adapt and apply all the surrounding tools that they've already developed.
*  If you're wondering how it makes business sense for a company like Playground to give the fruits of such a major investment away for free,
*  Suhail's perspective on the state of AI art in general and on image generation in particular might surprise you.
*  Because yes, of course, it's undeniable that the state of the art has continued to advance.
*  And today, not only mid journey and Dolly 3, but also stable diffusion Excel and Playground V2 can generate excellent quality,
*  merely photorealistic images with increasingly fine grained prompting controls.
*  And yet in Suhail's analysis, we're still only at roughly the GPT 2 stage of image generation AI development,
*  just scratching the surface of all the promise that AI based image manipulation still holds.
*  Most of the use cases, as Suhail has come to understand them in talking to Playground users, are not very well served by existing models.
*  And the leading AI artists use a mix of models and different complementary tools to achieve their best results,
*  meaning that things overall are still a bit too complicated for everyday casual users.
*  So what's missing from this picture? A unified vision model that can do it all.
*  Understanding, generating and also manipulating images in all sorts of useful, discreet ways.
*  This does not yet exist, and the leading large language model developers don't seem to be really focused on it.
*  So Suhail and team are setting out to build it over the course of 2024.
*  As always, if you're finding value in the show, we'd ask that you take a moment to share it with friends.
*  It has been incredible to see how the show has traveled and how the audience has grown entirely through word of mouth.
*  And I think this episode would be perfect for both the artists and the application developers in your life.
*  Now, I hope you enjoy this conversation about the state and future of AI vision and image generation with Suhail Doshi of Playground AI.
*  Suhail Doshi, founder and CEO of Playground AI online at playgroundai.com.
*  Welcome back to the Cognitive Revolution.
*  Thanks for having me.
*  Yeah, I'm excited. So you were our very first guest when we launched the show almost a year ago now.
*  And I think you'll be roughly our 100th guest.
*  So this is a cool way to celebrate having put out a lot of episodes and another trip around the sun.
*  And I'm excited to catch up with you on everything that's been going on in the world of pixels, both probably and at your company over the last year.
*  For starters, I just listened to another interview that you did with Swix and Alessio on the Late in Space podcast.
*  I thought that was really good and figured we'd try to cover.
*  Of course, there'll be some overlap, but try to cover largely some different topics today.
*  I guess for starters, I'd love to hear kind of what's new at Playground, what's new in image generation.
*  Yeah, I'm sure there's a lot and I'll have some follow ups.
*  But I would love to hear how you would kind of summarize the journey over the last year.
*  Yeah, I think the journey over the last year has had like some interesting highlights and some interesting kind of like low lights.
*  I'll start the lights because even though it may sound slightly depressing, actually think it's like the most exciting bit.
*  Of course, everybody knows that like, you know, things like Dolly 3 have come out, Journey B6 has come out,
*  Stability Eye released SDF cell back in June, July.
*  So there's been a lot of new foundation models that have kind of come out.
*  But I would mostly say that I have been fairly disappointed by the progress.
*  And one way that I would maybe articulate this is that mostly the models are used for art.
*  And art has some value and utility in the world.
*  But for the most part, we haven't really seen that like general model high utility that you get out of these language models.
*  Right. And so to kind of just like harken back a little bit, you know, maybe three, four years ago when we looked at language,
*  we sort of said, what are these, what do these AI models really do?
*  They might summarize something, hallucinate, maybe they have sentiment analysis was kind of like a use case that was touted a lot.
*  Many startups will build just doing sentiment analysis, those sorts of things.
*  Like the models couldn't rhyme, the models couldn't really write code, the models couldn't really do anything.
*  So there was like these very specific use cases.
*  And then as folks at either Anthropic or if any, I noted with scaling laws that they felt like maybe the models could get better and more generally useful.
*  And the only reason why I'm taking us through this like kind of hopefully well charted history that people know that are in the AI world,
*  but if you're not in the AI world, that's kind of like a rough snapshot of I think what happened with with tax and things like chat,
*  and it's writing code and you can ask the questions.
*  You don't have to go to Stack Overflow anymore and whatnot.
*  That really has happened. Vision at all.
*  You know, what we got out of this was I can make really amazing sort of like art.
*  I can make a meme, I can make something cool.
*  I can show it to my friend. Maybe I can make like a book cover.
*  Maybe I can make one use case for some of these models is making coloring books.
*  But the models and the models are really great at extrapolating like interesting characters or subjects or environments and and and making art,
*  but they're not very good at how to do anything else.
*  And they're not good at manipulating pixels in any other kind of way.
*  And so actually was maybe expecting last year that perhaps like the pace and momentum would be a lot faster.
*  But it just turned out that wasn't the case.
*  And so maybe the most the thing that I'm most excited about is that it kind of feels like vision.
*  It's like a year, like a year or two off from this big moment that language has had in this farm.
*  Huge quantities of vision data compared to text.
*  Yeah, no doubt about that. There's plenty of my dad has this crazy dad joke of, you know,
*  we're running out of pixels and the pixel minds are getting depleted.
*  And the reality is obviously there's there's plenty of pixels flying around if you can figure out how to use them.
*  That is an interesting perspective. Would you this is it's maybe so strange as to not be useful,
*  but would you say we're at like GPT-2 level, you know, relative to some inflection point that you're expecting for.
*  Yeah, it's funny. It's funny. Yes, I question that is exactly how I phrase it at our own company.
*  I or I'm talking to people that were trying to hire and I like, you know, I'm not even sure we're even GPT-3 level,
*  even though there's this feeling maybe last year that perhaps maybe we were.
*  I actually don't think I don't even think sorry that we were at like something greater than a GPT-2.
*  And I think the continuum of where we were two, three years ago, GANs and stuff, things have significantly improved.
*  But the overall utility hasn't really significantly improved.
*  You know, we've got our kind of like like text. We have our sort of three or four very simple use cases.
*  You know, you can make art, you can make you can remove something and objects with the pixel phones, removing things.
*  You can remove a background. And that's about it.
*  That's about roughly what you can do with images, whereas in the domain of text, it's like the long tail of what you feel like you can do.
*  The value that you get is just so much more significant.
*  And so I say that I say that this is like mildly depressing in some ways, but I'm very excited and I'm working on it because I feel very excited about the possibilities that actually it's this huge open feel of unsolved problems.
*  And now there's a lot of momentum, a lot of effort and a lot of desire to make it better.
*  Yeah, that's really interesting. I mean, I think for a lot of people that probably even who are in the AI space pretty deeply,
*  I think that would probably come as a bit of a surprise.
*  You know, as you were talking, like I have remarkably little information about who the cognitive revolution audience is, but we're definitely not like an AI art or, you know, image generation or like a pixel specialist show.
*  So I would imagine most people have a lot more experience with your chat GPTs and your quads as opposed to with image creation.
*  But from the outside, you know, and I use these tools like I'm not an artist, but I use them periodically.
*  It definitely feels like things have gotten a lot better, right?
*  I rewind to a couple of years ago when I was seeing this stuff start to bubble up on Twitter and, you know, seeing Rivers have wings.
*  The OG true legend, the counts Rivers have wings. If you're listening, check your DMs. I want to have you on the show.
*  But, you know, that stuff was pretty gnarly and it was like, wow, it's amazing that you can do anything, but it definitely was not passing any sort of visual Turing test equivalent or whatever.
*  It was sort of like swirling colors in backgrounds and abstract shapes.
*  And now we're getting kind of this like amazing photo realistic thing.
*  You kind of solved hands are starting to see models with like tax, tax synthesis and that kind of thing.
*  So it's definitely, definitely on an amazing pace.
*  It's definitely not like hitting some odd weird asymptote quite yet.
*  Given that progress, you said utility hasn't grown as much as you would have hoped.
*  Is it the case that we maybe naively misunderstand or kind of misconceive of what actually drives utility?
*  Like the fact that we're able to generate these photo realistic outputs today is just not enough for like a lot of the utility that you're looking for.
*  I generally think like from the most part, it's just like at the moment, mostly a lack of imagination is somewhat hard to imagine extrapolation from like these big models.
*  I think, you know, even at GPT three, it wasn't like they were huge.
*  I think it was like this massive audience thinking that like, I think if you had gone back in time to maybe when GPT three like came out maybe six months later,
*  I don't know that there was like this very, very big audience that thought for sure like what we were getting at a GPT four was coming.
*  I don't think that I thought at maybe even kind of like last year I had access to GPT four maybe in, I want to say like October of the year before last.
*  And the first thing I did with it was I wanted to see if it could find vulnerabilities in my computer programs.
*  It was like how good would this be at like finding security issues?
*  You know, that was like the use case I had in mind.
*  But I'm not sure that I fully like internalized even back that year that like this thing would be so instrumental in like writing code as good as it is.
*  And I wasn't sure that I, you know, I thought that it could answer like relatively difficult questions about my life or things happening in my life or if I have like a leak in a ceiling, how might I solve that?
*  You know, I don't think I don't think people thought that it could be not very many people thought that it could be that powerful.
*  And so I think like that's just like similar, true, similarly true in images.
*  You know, you're just sort of like, okay, it can make this like beautiful art.
*  It's like really fun and novel.
*  But we know what do I use this for day to day because you actually look at images, you know, it can't it's not it's kind of struggles making logos.
*  It sort of struggles with spatial reasoning.
*  It's certainly like things like in painting or editing are extremely difficult.
*  We're still sort of talking like eyes are still sort of like a bit strange.
*  Hands are always coherent.
*  Sometimes it adds kind of like an extra letter if you're asked, asked some protects.
*  So they're like these little things that we see are present in the models.
*  But there are some I think there are like much bigger things about vision just generally that are probably like can lead to like a very big general model.
*  Like one of the things that we tend to think about at Playground is how we might achieve a unified vision model.
*  Right. And there's like three three pieces to at least graphics, which is just a sub component of vision.
*  There's creating pixels, there's editing pixels, and then there's understanding them.
*  So GVT-4 means like a good example of like a very elementary model that's like getting better at understanding things.
*  Right now, it's quite good at captioning, but there's like other reasoning capabilities for vision or just like understanding an image or even a video.
*  You can't do video, for example.
*  Right now, we're kind of stuck on creating, but we're not very good at like editing things.
*  Like one thing that hasn't really happened yet is there hasn't been a very big effort on manipulating real pixels of real images.
*  Sorry, pixels of real images.
*  We're mostly dealing with synthetic images, but we're not doing a whole lot with real photographs where I think there's probably a lot more utility and a lot more value.
*  I'll give you an example.
*  If my son was smiling for a Christmas card that we want to send out late last year, it's really hard to get like a dog and the kid and everybody in the picture getting them smile appropriately.
*  But it'd be sure would be nice if I could just be like, hey, you know, highlight his face and just say, can you make him smile like you're or take two images, one where he's smiling, one where I'm not like kind of finding a way like merge those two things together.
*  That's like a very simple application.
*  And so you can kind of like imagine what the other kinds of general useful things that you could do with manipulating pixels.
*  And that's like maybe the tip of the very, very tip of the iceberg.
*  So I just imagine that there's a lot more provision, you know, understanding the context of like a video scene.
*  Another example, like if you asked a model to look at like three minutes of the video and what happened, could the model like reason about that?
*  So like just a bunch of like those kinds of things.
*  And so there's just like this general lack of, I would say, significant investment with regard to trying to make a great general vision model.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The Brave Search API brings affordable developer access to the Brave Search index, an independent index of the web with over 20 billion web pages.
*  So what makes the Brave Search index stand out?
*  One, it's entirely independent and built from scratch.
*  That means no big tech biases or extortionate prices.
*  Two, it's built on real page visits from actual humans collected anonymously, of course, which filters out tons of junk data.
*  And three, the index is refreshed with tens of millions of pages daily.
*  So it always has accurate up to date information.
*  The Brave Search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference, all while remaining affordable with developer first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data sourcing and more human representative data sets.
*  Try the Brave Search API for free for up to 2000 queries per month at brave.com slash API.
*  Real quick, what's the easiest choice you can make?
*  Taking the window instead of the middle seat, outsourcing business tasks that you absolutely hate.
*  What about selling with Shopify?
*  Shopify is the global commerce platform that helps you sell at every stage of your business.
*  Shopify powers 10 percent of all e-commerce in the U.S.
*  And Shopify is the global force behind all birds, Rothy's and Brooklyn and millions of other entrepreneurs of every size across 175 countries.
*  Whether you're selling security systems or marketing memory modules, Shopify helps you sell everywhere from their all in one e-commerce platform to their in-person POS system.
*  Wherever and whatever you're selling, Shopify has got you covered.
*  I've used it in the past at the companies I've founded.
*  And when we launch merch here at Turpentine, Shopify will be our go to.
*  Shopify helps turn browsers into buyers with the Internet's best converting checkout, up to 36 percent better compared to other leading commerce platforms.
*  And Shopify helps you sell more with less effort thanks to Shopify Magic, your AI powered all-star.
*  With Shopify Magic, whip up captivating content that converts from blog posts to product descriptions.
*  Generate instant FAQ answers.
*  Pick the perfect email send time.
*  Plus, Shopify Magic is free for every Shopify seller.
*  Businesses that grow, grow with Shopify.
*  Sign up for a one dollar per month trial period at Shopify.com slash cognitive.
*  Go to Shopify.com slash cognitive now to grow your business no matter what stage you're in.
*  Shopify.com slash cognitive.
*  Yeah, I would love to hear a little bit more about the use cases.
*  And also, I'm curious about what shortcomings you are finding in GPT-4V.
*  I have used it pretty successfully actually, at least for the use cases that I've tried.
*  One that was like a kind of mind blowing moment was I took my kids that I can definitely relate to the difficulty of getting them all to smile in a photo because we're up to three.
*  And, you know, two out of three feels like the best we could ever manage to do.
*  But I took them to Salem, Massachusetts leading up to Halloween because we were out there for an event that my wife was organizing.
*  And it was actually a fun little day.
*  But I came across this parking sign and this just at the time there was the famous one on Twitter where somebody was like, I'm never getting a parking ticket again because he took the picture of, you know, the eight different parking signs and said, can I park here right now?
*  My version of that was the Salem version where it had some message about like, you know, special parking rules for October.
*  And at the bottom, it said Salem PD.
*  And I was like, what's going on here?
*  And it was able from the Salem PD and the like special rules for October to infer that it appears that you're in Salem, Massachusetts, which has this like, you know, historical, you know, connection to witchcraft and whatever.
*  And now it's like a holiday, you know, destination leading up to Halloween.
*  And so it's probably that that you're dealing with.
*  And I was like, man, this thing, there's a lot of knowledge in there that, you know, it's kind of able to tap into.
*  And we've been really good luck with that at Waymark too, where we just use it to filter user images.
*  We've long had this product experience where we'll pull in a ton of images, like every image on your website, if you're a small business, just for your convenience.
*  So you don't have to go, you know, load them into our product manually.
*  So we kind of pull them in, but then we get all kinds of crap, right?
*  So like, how do we filter that to use the relevant stuff?
*  And GPT-4V is awesome at that for us, literally just saying like, here's the profile of the business, you know, which of these images would be good to use, which would not be good to use.
*  I've done a little bit with breaking video into frames and trying to get it to understand that as well.
*  I would say I've like fully characterized how well that can do.
*  But anyway, those have been my experiences.
*  What things have you seen or done that you feel like, you know, leave something to be desired in the GPT-4V performance?
*  I think like one small, you know, one easy one is that GPT-4V is not always great with like certain tasks like image segmentation.
*  It can be kind of weak at that occasionally.
*  And you need image segmentation or like finding the right value box for certain images tends to be extremely useful.
*  I mean, they're just better models than GPT-4V and arguably a lot faster.
*  And segment anything is a great example.
*  You can use Dino plus segment anything together to achieve really interesting state of the art results.
*  And that's like a very simple use case that's been going on for a long time in the AI that probably could greatly benefit from a general model.
*  So I think the promise of something like GPT-4V is really, really outstanding.
*  That task is so valuable for a whole bunch of use cases related to like camera.
*  Anything related to cameras is a really good example of that.
*  Sometimes I still think there are like some issues with hallucinations with its like descriptions of some of the images.
*  But I love GPT-4V. My favorite use case is like taking screenshots on my desktop computer and then asking me to like solve some problem of mine.
*  Like lately, I've been just doing this funny thing where I'll just like take screenshots of errors in my code and asking it to like basically help me fix whatever the problem is.
*  It's almost like I can be really lazy about things.
*  But I had been thinking that how valuable it would be to sort of like have it.
*  It surely would be valuable if there was a model that was able to just like stare at my computer with me and kind of help me along as I go.
*  And I hope someone at OpenAI is sort of working on some something that can like be like, hey, I might be able to help you with that.
*  You know, I'm kind of pairing with you as you're working.
*  But I think that's going to take like a lot of work.
*  And that's just that's just one domain.
*  I think of like pixels and images.
*  That's just understanding what it's seeing.
*  That's not even necessarily manipulating graphics in any kind of way.
*  Yeah, certainly the fact that it is all text out is a major limiting factor in terms of what it can do with images.
*  Because all I do is spend my time on vision.
*  I spend a lot of time about what are the major benefits of vision versus say language, not just in like the training data, but also in like the outputs.
*  And I'll give you another example of something.
*  You know, one thing that's like really challenging with text is it takes a lot of effort to read text.
*  It takes a lot of patience.
*  It takes a lot of focus.
*  And we kind of continue to live in a world where there's even less and less of that.
*  But one thing that vision is what your graphics division is really good at is just like a very amazing visual explanation of something.
*  Often there are circumstances where you want a visual visual explanation of something.
*  Right. We see this all around us.
*  Right.
*  We know when we read a book and we see a diagram or something that it can be very valuable or a graph.
*  Right. A graph can be extremely valuable.
*  But there are other modalities like a video that's explaining something to me is really valuable.
*  Audio is obviously valuable, but it tends to, you know, there are major areas where like things tend to lack in that regard.
*  You know, for example, there are a lot of people that are just kind of waiting around for these image models to figure out how to make diagrams, flow charts, diagrams.
*  Ways to like be able to understand something about the text.
*  That'd be one thing we all can very much tell when something doesn't look like us.
*  Like one thing we learned over the last year is that humans are really good at looking at faces.
*  It can really tell when something is off.
*  You might have 10 friends that tell you that that cartoon version of you looks like you.
*  But sometimes when you look at it, you're almost offended by it.
*  And so I think that there is all these different kinds of use cases that are just very unsatisfied.
*  And that and but I mostly think that like language doesn't accommodate as well as it could.
*  And it will never accommodate.
*  And it's totally reasonable.
*  Yeah, those are two good examples.
*  You know, I've tried to work around the graphic thing a little bit by asking GPT-4 to create a text base, you know, basically to follow.
*  There's like a bunch of as you're probably aware, there's a bunch of different flow chart and diagram kind of syntaxes that you can use.
*  So I've asked it to create some diagrams that way.
*  And there's one called Mermaid and there's a there's a, you know, viz graph, I think is another one that's worked OK.
*  But yeah, definitely. I did this for Weymark actually with the you know, the the AI system that has a bunch of different models that even for us, you know, on the development team, it's sometimes a little bit hard to remember.
*  Like, wait, which has to finish before the next thing?
*  You know, well, what are we paralyzing and what's the dependency on what?
*  So to just try to have that at a glance is something that we didn't have.
*  And I was able to get like a pretty decent version of it from this like syntax, you know, that then could render deterministically into the visual form.
*  But you're definitely right that it's like leaves a ton to the imagination compared to what, you know, a real infographic or, you know, proper designer would do it still work close.
*  Yeah, that's like one that like is commonly that, you know, people talk about.
*  I mean, one could be a simple as something like here's a picture of my my house, my room in my house, my bedroom.
*  I need to figure out a way I want to figure out different combinations.
*  If I put my bed on this side of the wall, what should I make?
*  Which my room look like if I put my bed on the other side of the wall, keeping all the same objects in place, how would you reorganize my bedroom?
*  Right. And you could copy and paste that you could put it in GPT-4B and it will sit something out.
*  Right. But it's very hard to imagine what you have to now read this thing is extremely hard to reimagine your bedroom.
*  But imagine if there were a an image model that could completely reorganize your bedroom and show you all the different ways that it could work.
*  Right. Imagine that you could like you could you could iterate with it.
*  You could say, hey, what if the dresser was made out of this other material?
*  What if it was a little bit bigger?
*  What if the nightstand was lower?
*  Right. There are a whole bunch of vision.
*  So I think you can try to imagine these little simple things that feel very hard today.
*  It's very hard. Like, where do I go? What website do I go to?
*  OK, I got to like start drawing like lines and stuff.
*  Forget it. I want to do it. Too much work.
*  So you can kind of try to imagine these circumstances where you're kind of iterating just like you are with language, but with something very visual,
*  whether it's your home or something else, I think you start to get more out of it.
*  You could do the same thing with like logos.
*  You could say I want my logo to be a little like this.
*  You get rid of like the little swirl.
*  Could you change it to like from circles to like rounded rectangles?
*  Like you're able to kind of actually work with something like an artifact together.
*  You know, that's virtually impossible to do.
*  That's like another example, something very hard to do with language.
*  I think that there are like there are even bigger use cases and vision, you know, whether it's like something understanding that it's like your face versus like an intruder and a camera system,
*  something that like learns that over time, there's just there is a whole limit to what we probably can do with language.
*  I think it's underappreciated with vision.
*  And I think it's just strictly because we're kind of trapped in like our world right now.
*  And I think that's going to change very significantly this next year.
*  I have kind of two lines of thought going in my head at the same time.
*  One is how is that going to happen?
*  You guys have just trained a foundation model from scratch yourselves.
*  You know, I'd be interested to hear kind of what you think the trajectory of foundation models in vision is going to be.
*  And then I'm also really interested in and it's a very general problem, although you have a particular form of it for product owners.
*  How do you build in a way that like balances the now and what people need to get utility for your product today versus like what is going to be needed or maybe no longer needed as the models themselves get better?
*  I went into the product and I was making some stuff in preparation for this and I haven't I have done it more than once between our episodes, but definitely was just catching up in the last couple of days.
*  I see that there's like a lot of new features.
*  I was going to ask, you know, what are some of your favorite new features?
*  What are people getting the most utility from?
*  And I still want to ask that.
*  But I also now kind of want to ask like, how are you thinking about what features to build that are like patches for sort of, you know, model weaknesses that may not be needed in the future versus what things do you think are kind of always going to be non model features?
*  So there's a lot there. I'll shut up and you can take it all apart.
*  No, no, no, that's great.
*  You know, I think I think the last year has kind of maybe see some of like the the community has done such an amazing effort at fine tuning models, finding fixes, being extremely clever.
*  And it is it's exactly kind of like how you describe it.
*  It's like for as amazing of these feats as they are, it is a lot of patchwork.
*  It's not a true it's not a true fix at a foundation model level.
*  You know, there are models that fix hands, fix eyes.
*  There are models that do ups scaling, try to get more detail out of them.
*  There's tons of amazing tools, but they're all they're all just actions.
*  I think maybe the more maybe more surprising thing is we've been thinking a lot about like what what what comes after just like text to image.
*  What else is left?
*  How do you get to a much deeper understanding of these kinds of concepts?
*  And so I think for the most part, we sort of think of it as like these three pieces around like, OK, how do we how do we create something from nothing?
*  How do we take existing pixels and manipulate that at a really high fidelity?
*  And how do we understand the images, kind of like GPT-4B?
*  And then how do we like bring the three together?
*  Because ideally that model understands a lot more and it's far less patchwork and it's far, far more general than what we have today.
*  We're planning to be very focused this year on editing.
*  So I think the first the first kind of thing is that I think the community and everybody involved, all the researchers involved made this wonderful way of like creating amazing art.
*  Sometimes it's very realistic.
*  Sometimes it's just fun, entertaining, fantasy art, what have you.
*  And I think that has driven some utility, but definitely not not enough.
*  I think the next thing is probably our kind of like not so secret plan.
*  What I'm happy to reveal is just that we're going to work on multitask editing and multitask editing is just kind of taking existing images and manipulating those pixels such that we can achieve anything.
*  There have been some kind of early versions of this that happened last year.
*  It should be anything from like, what would I look like if I were aged up, you know, at 65 years old, or my son?
*  What would I look like with a different hairstyle?
*  There are models out there from researchers that are trying to like replace, you know, clothes in a really high fidelity way.
*  That should really be encompassed in a general model as well.
*  Being able to do all kinds of things like that, being able to manipulate like some kind of interior design would be a good example of that.
*  And then it should be kind of like more difficult things.
*  So those would be some of those would be kind of like local edits.
*  And then there's like more global edits.
*  Global edits would be like you have a big scene that's clearly like a wintery scene that you might want to make a spring or summer scene.
*  And that means every object, everything in that scene has to be changed.
*  So that'd be a big global edit.
*  I think that we need to get better and better at those kinds of things because I think the utility will rise across customers who want to do more valuable things.
*  I think a lot of those things tend to be real imagery.
*  And then I think we're also going to work on a model that's trying to like understand everything that's going on in an image.
*  We need good understanding because that actually helps us train the other two models.
*  So hopefully by the end of the year, we're looking at something where we can kind of try to unify these three things into a single model that can kind of do more surprising things, more surprising use cases.
*  Just strictly for 2D images.
*  We've kind of moved on to video.
*  People have moved on to video and stuff.
*  And I think that's really wonderful.
*  It makes really amazing art.
*  But I think that we still haven't quite like, we kind of haven't shown how big things could be, even just an image, which is just even on its own a hard modality.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  If you're a startup founder or executive running a growing business, you know that as you scale, your systems break down and the cracks start to show.
*  If this resonates with you, there are three numbers you need to know.
*  Thirty six thousand, twenty five and one.
*  Thirty six thousand.
*  That's the number of businesses which have upgraded to NetSuite by Oracle.
*  NetSuite is the number one cloud financial system, streamline accounting, financial management, inventory, HR and more.
*  Twenty five.
*  NetSuite turns 25 this year.
*  That's 25 years of helping businesses do more with less, close their books in days, not weeks and drive down costs.
*  One, because your business is one of a kind.
*  So you get a customized solution for all your KPIs in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts and improve margins.
*  Everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist designed to give you consistently excellent performance, absolutely free.
*  And netsuite.com slash cognitive.
*  That's netsuite.com slash cognitive to get your own KPI checklist.
*  NetSuite.com slash cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it to use Cogrev to get a 10 percent discount.
*  So how do you think the experience changes over time?
*  Like today, again, I go in there, I can do the classical text to image prompt and get something out.
*  Now I can also bring my own image and ask for modifications that are kind of holistic.
*  You know, my one of my early semi viral tweets from last year was taking the ultrasound image of our now nine month old baby that was still in my wife's belly at the time.
*  And, you know, saying, what would this look like if it was a newborn?
*  And it did a reasonably good job of that.
*  I wouldn't say it was, you know, it was still in the uncanny valley, but it was like, you know, good enough that people were intrigued to see it.
*  And you got a lot more features, too.
*  Right now I can out paint.
*  I can mask and in paint.
*  I can start with like a line sketch.
*  I can start with a depth map.
*  I can start with, you know, probably a couple other things as well.
*  You have kind of pre rendering sort of features.
*  There's like the intensity of the guidance.
*  So there's all these kind of knobs and dials that have been added.
*  Do some of those go away?
*  Do we continue to add like all these sort of control elements or does it become more of a like just conversational UI again?
*  I think some of the elements go away.
*  Right.
*  I think some of the elements go away because the model should have an understanding of depth.
*  The model should have an understanding of edge lines.
*  The model should have an understanding of color lighting.
*  Right.
*  The models shouldn't shouldn't, you know, control net, for example, for these models is really great innovative thing that came out last year.
*  But the model should really understand that you should be able to erase a part of an image and the model should understand that like actually there is like a big depth component here and that I have to consider the shadows.
*  I consider what's in the foreground and the lighting related to a character or subject.
*  Right.
*  So I think definitely some of these things go away.
*  And I think that, you know, for the most part, we find that there are definitely a whole bunch of power savvy users that use these tools.
*  But a vast majority of people definitely struggle.
*  Definitely it takes like some time and expertise and and watching a couple of YouTube tutorials, perhaps to understand these things.
*  So I think those things kind of go away.
*  I don't think it ends up being just text.
*  I think text is great.
*  Text is a really great kind of like absolute way that humans can like compress a very high dimensional concept in their mind to something simpler that they can input into a model.
*  It's very hard to like imagine something like how would you take something that you're imagining and then giving it to the model?
*  Well, maybe the best answer for that would be like another image.
*  But one of my favorite examples is like the word, like the concept of like shattered glass.
*  Right. Shattered glass is like we could we all have a version of what we can imagine that looks like.
*  But actually, it's very difficult to both have the same concept of what that means, because there's so much entropy with shattered glass that you and I would have completely different imagination of how that would look and how the lighting would be and what color things would be like.
*  Right.
*  But maybe you maybe you gave the model something that you like.
*  Right. Maybe you give it a style.
*  It's really hard to describe to these things.
*  Style can be a combination of different things that you like together.
*  You know, if you're thinking about like your brand, you might like might be inspired by multiple things and wish that something could look like like all three of those things.
*  Right. So I think my sense is that it's probably going to be a combination of language, which gives you some sense of that.
*  But it's going to need something that's even higher dimensionality than that.
*  So that it gets closer to what you want.
*  A model that probably admits something visual probably should be very visual.
*  Right. It probably should be, you know, maybe it's using your finger on your phone and masking something.
*  Certainly, it's going to be typing something.
*  Certainly, it will be like I like this this this thing out there in the world.
*  I think it might be my guess is that vision models will probably have to be extremely multimodal compared to maybe the starting point of language.
*  Yeah. When you said the bit about language and just the the way that it allows us to compress what's in our head, my brain jumped to what about just direct brain reading?
*  I wonder if there is a because we've seen some pretty interesting results over the last year of and, you know, with still like fairly cumbersome hardware, but less cumbersome, you know, gradually over time.
*  Do you envision a future where somebody sits down and puts like the playground crown on their head and sort of like doesn't have to say a word, but can instead like the classic scene from back to the future, you know, suction cup the thing to your head and then just kind of focus on your own like mental state, you know, kind of commune with the system and get your ideas out that way.
*  I would have thought that was insane to ask, by the way, even a year ago, but it feels less insane today.
*  Somehow. Yeah, I mean, we can get we can first get words out of out of our brain and go from thought to word.
*  That would be amazing. I don't know if we can do that. I actually haven't studied anything about brain and trying to get like brain output to get to like any kind of accuracy.
*  I think I saw something maybe where like maybe maybe you can like move like an object like there's ways to like left, right, up, down or something like that. But I haven't seen. I don't know if there's any research that's like.
*  Thought to text. There's thought to text. There is also thought to image reconstruction. It doesn't necessarily work as well as it might need to work. But this is part of why I kind of have this AI scouting concept here.
*  I'll give you two links and you can check these out at your at your convenience. But one the first one we had a guy named to niche.
*  Yeah, it's an energy. What was really interesting about his was that it was low sample was required and they used existing foundation models and kind of figured out a way to with like a relatively small per user sample.
*  Map the brain activity into the kind of light and space necessary to then diffuse into the image. But the reconstructions are like really quite good. That one is an fMRI if I recall correctly, which is like far from consumer.
*  And then this other one from Facebook meta is magneto in cephalography, which is definitely still cumbersome, but like less so.
*  And also fast that this one you can kind of see the accuracy is lower. But but you know, if you can reconstruct what they're actually seeing, then you know if they close their eyes and just imagine stuff, you would imagine that could start to work as well.
*  And I also do wonder just about the degree to which people a big obsession in mind in general is kind of how the world begins to change in response to AI. And I definitely think that people can kind of train their own minds to like work with these systems and like these early results don't have any, you know, of that going on yet.
*  Yeah, I mean, I think I think like the ultimate multimodal model. At the end of the day, it just turned it's like not really about tokens and language, you know, like, like the vision transformers are just like, taking tokens of an image, they're like trying to create some kind of codebook of images by taking patches of an image and then the language stuff is also word stuff.
*  But it just seems like at some level, it's just going to be something very bite level. And and if you believe that it would just become bite level, or some something lower, something lower level than these two things, then then it starts to not matter so much, you know, whether it's like language or vision, then it becomes something else that none.
*  It's like the models have, it's almost like you've given the model like a representation, it's like very normalized across all of these different modalities to get to some kind of unification of them. And I do wonder, I do wonder where it's headed. I don't know. I don't know right now.
*  I don't necessarily know that like, actually, maybe maybe the transformer is not the right thing, or certainly not tokens of language are necessarily the right thing. It's probably too early to tell because maybe harbor is not even good enough yet.
*  You have to compute performance is not good enough yet. And there's still ways to go to scale text or vision. You know, my first thought with like the brain things, I was like, I wonder if it would be too high dimensionality. I wonder if it just be such a, yeah, like, like vision is already a lot of input data so that so people tend to
*  need to find a way to kind of like compress it down to something simpler, more encoded rather. So I mean, my first thought was like, I wonder if the brain has very, very high dimensionality because I don't know anything about this. I suppose you could encode it too.
*  But yeah, it certainly would be cool if you could like look at your, you know, your room and sort of imagine what if it was there and somehow it kind of like knew that you could do that.
*  Perhaps, perhaps text to, you know, whatever it's maybe not maybe not the ultimate like first input, maybe maybe it is thoughts or something like that. Let's see if you can do thought to text, then that's like the right primitive right then you can get from, you know, you can get to text to maybe anything, whether it's like audio or images or other texts, then you'd have the right maybe like quick to decode, like go from thoughts to like whatever you want to.
*  Yeah, I wonder if anyone is working on thought to text.
*  There are some thought to text ones as well. I wouldn't say, you know, they're kind of in the same general ballpark as the the thought to image where it's like, Whoa, that's striking, you know, and it is they do it a very similar way like you read a sentence or a paragraph.
*  And as you're kind of, you know, processing that language, they're kind of trying to reconstruct what you have been processing. And they do get like a decent reconstruction. It's not perfect in the same way that you know these image reconstructions are not perfect, but they're definitely directionally right.
*  You know, you look at it and you're like, you're not guessing. That's for sure. You know, the resolution is not there. But the that they are on to something is like, pretty clearly true.
*  I'd love to spend more time on brain interfaces. I have no idea.
*  When in doubt, go back and you know, see what Kurtzweil said in the 90s. And then, you know, we're like getting to the time when when it was supposed to happen. And, you know, that guy has been I've started to use the term Kurtzweil's revenge because I came across his work in like the mid 2000s.
*  At that time, it was like, you know, the exponential curve that he was projecting, we were still in the low part. And so it was like, you know, he said this five years ago, but not much was supposed to happen in these five years. So whatever, like maybe it'll happen.
*  Then 10 years went by and it was like 2015. It was like, wow, he was wrong about everything. And you know, this guy, what a dreamer. And then now here we are. It's like, actually, you know, exponentials are crazy. He's maybe a lot more right than than not.
*  So he's apparently he's got a new book coming and it's the singularities nearer or something I think is the metric that was the joke title or the real title.
*  We write for most of the time when I talk to people about a unified vision model, even features in the field have often struggle have often not thought about it.
*  A lot of people are sort of trapped in this kind of like, we just we're just trying to we're just trying to do text to image. And they haven't really thought too much deeper about that or or the other version of this is like a very narrow use case.
*  Right. Like e commerce product placement or swap, you know, changing clothes or filters like on Snapchat, that kind of computer vision stuff. But that kind of computer vision stuff was very, you know, 2000, you know, 2020 2019 style.
*  Right. That was pre generative AI pre kind of like big generative models that can I mean, the promise of these generative models foundation models specifically is that they generalize so well to these other kinds of things that we're surprised by every day that we use them.
*  We're like excited about GPT five because we're not because not we don't even know what it will do.
*  But because we're surprised by what we're we're we're we're excited by what we'll be surprised about. And I think that that same moment just hasn't happened with vision. So it's so I feel like I've kind of caught you a little bit off guard during this, this chat because but I just wanted to mention to you that most of the time when I'm talking to vision, they don't see it either.
*  There are a few people who hired those people that happen to that have like kind of the ambition or goal to try to do something a lot bigger. But we do not have a general vision model of any sorts. And you can tell you can tell by by its limited utility. Maybe maybe it will be clear towards the end of the year when we go well, I didn't know that we could do that.
*  Yeah, I think that is a good point of comparison, you know, that I would agree that the sort of surprising capability doesn't seem to have happened as much on the image side as it has on the language side. So it's a it's a good contrast.
*  But just consider if if everyone had open AI, and so like, there's this wonderful, huge language race. It's great. I love it on people to focus on that because we're focused on vision. But I think that but consider for a moment all opening I was doing this vision. You know, if we could imagine that there was actually a version of opening out I was super laser focused on vision. And right now there isn't as far as as far as I know. But I don't think there is, you know, what what would the model like what would these models look like? I think there would be
*  far superior than Dolly three vastly better than that. Yeah, what do you I guess one interesting question is like, what does and doesn't exist in the world that, you know, is kind of in text, like everything, you know, ish exists, right? You may not have access to all of it, but it's all kind of out there. It feels like in one way or another. With images and with the text image use case, you know, the images were never captioned with the intent of like allowing you to create images in a text to image sort of way. So it's sort of this like found
*  data set concept that, oh, hey, you know, look at all this web scale data, these captions are like super noisy. Obviously, we've gotten better at that, you know, filtering, etc. over time. But, you know, largely, it is still kind of derived from this, like, the fact that people happen to, you know, caption their images sometimes, I guess there's maybe just a lot of missing data where like you could say, here's an image and I want you know, reminds me of like,
*  the bad Photoshop memes online, right? Where people are like, Oh, I want my boyfriend to be over here, whatever, then the, you know, the person like makes a mockery of their request. But more generally, you know, more like productively, it seems like what's missing is that we just don't have those before and after transformations in image almost at all, right? Like,
*  kind of saying, is there a lack of training data, basically relative to say, like language where maybe there's like vast quantities of, you know, structured and good training data? Is that kind of what you're saying?
*  Yeah, like the transformations that you would want to do now that you're like, starting to imagine what a robust AI tool would look like, are just like, very hard for humans to do very rare online, you know, require like advanced Photoshop skills historically, and just just don't exist and just aren't posted all that much, I would guess.
*  It turns out with vision is perhaps more, more prone to being able to succeed with even synthetic data. You know, what would benefit of all these images is that, you know, you can make you, it's very easy to make lots, generate lots of them and annotate them and change things with them. So it turns out that like, actually, you can like, probably retrain a good model and ground treat stuff. But then there are a lot all these like wonderful other models that you can use.
*  To train on probably synthetic data to get really good new kind of like general model that's capable of new things. I really good example of this for for folks is that maybe the thing that like put me onto this most early was struck picks the picks like early I think last year, where so much of it is actually just synthetic data.
*  I think it's overall performance was not world changing or anything, but it gives you kind of a glimpse of what it could be given. I mean, this was just one researcher at, you know, Berkeley, I think under efforts. So I think like, given a given a team that really cares what what what could it be? How could it be? So I think that's one thing that might be surprising regarding like this debate around training data. The second thing I would say is that part because of the massive revolution with text, and in specific some of the things that we've been talking about, like,
*  I think one of these like text vision models is multimodal models that are kind of getting built now, whether that's at Google or open AI with GPT-4B or there's some really amazing open source ones by students in academia. I think this guy named I don't know sorry if I butcher the way to pronounce his name. His name is Haoshin Lin or something like that.
*  And so there's just this, I think going into this year, one thing that I think will probably be true is kind of a natural progression from where we are with language is yeah, and you probably need to augment language somehow is a multi this really great multimodal models. And it just turns out that if like you scale up these multimodal models, you know, with text understanding and vision, obviously, then you can even do more capable things might be surprising like how that can help you to get to the next level.
*  And that can help with vision more significantly, even not too surprising. But certainly the language part was very important for the for the voting for these multimodal models to be as powerful as they are, for example, you know, hopefully image things like image segmentation get better, but the passion gets better.
*  You know, one one thing everybody knows in the field for vision, or at least with graphics is that that lion data set is really poorly annotated.
*  It's sort of a best case effort, but it's very poorly done. Right. You know, I think the folks that made it did the best they could, but the data is not great. And instead, if you have a multimodal model, that's extremely good, you know, the dolly three paper talked about how that team just completely
*  recaption the data set to be more accurate. And then that's significantly improved prompt alignment for the image models. And now you get better you get better prompt alignment. And now suddenly, like, suddenly, like, if you ask the models to, you know, one little test that I like is
*  create an image where you've got four bottles that are numbered one to four but orbit backwards. Right, you try to do these little puzzle challenges for the model. And suddenly, like these kinds of spatial reasoning tasks become possible.
*  Or if you should do recaptioning on text synthesis starts to get better performance starts to dramatically increase. Now, now we're starting to see kind of like mid journey and dolly three be better at tax. So it just turns out that like actually, the overall progression of the entire AI field helps quite significantly with vision.
*  And so I think this is just going to keep happening. So if I'm understanding correctly how you are expecting things to develop, it's almost kind of a mirror image in some ways to language where the language progress, it's at least like the kind of canonical breakthroughs seem to be just
*  scale it up, you know, and then, oh my god, look at this, we've got few shot learning these kind of, you know, quote unquote emerging capabilities that we didn't train for. And, you know, now of course we're refining that and we're doing curriculum learning and alignment and a million things.
*  But it was kind of like first the brute force fact that you just dump all the text in run it and like amazing something amazing comes out and now what we're fine from there. On the vision side, it's insecure. The path is more of okay, let's have we have all these different specialist models.
*  And now those are going to help us kind of create the super general data set, which doesn't exist totally as needed in the wild. And then we can kind of go like Captain Planet with our forces combined. Like now we can sort of summon the truly generalists vision model that you're dreaming of.
*  They're kind of like these pros and cons, right? Like on one hand, like images are so rich in terms of information relative to language. Just look outside your window for a minute and try to really look at every object. You know, right now I'm looking at like plants and like even just this even just looking at a plant, you can kind of see like how do the leaves fall? How do they interact together? How does lighting react to the plant? And some of this is a graphic knowledge, some of this is just more of a visual.
*  And then we have a world knowledge, right? A plan on a roof or how buildings look or how they're situated, right? So images on one hand are extremely rich in terms of data. They're so rich, but then they sort of lack kind of like the right annotation and labeling.
*  And so on the other hand, like text perhaps maybe has really great rich, wonderful labeling inherently, right? That's like just inherent in language anyway. And but on the other hand, they're very lost. It's very language is very lost. We don't have that many words to describe things, right? And the words certainly are not descriptive enough. So on the other hand, there's kind of cons to this and they have different utilities in our in our life. I can't say that they're like, it makes sense that this happened, but it just so happens that they're not.
*  And so what happens to be that we've got these amazing text models that are starting to lead to amazing multimodal models with vision. And, and that's probably going to help us like fix some of our understanding of the images, like what's really going on in some of these images, where are things located? Why are they the way they are? And so my guess is like, you know, if you think of vision is, in my mind, I kind of like look at a vision, it's like maybe about a year to hide where we are with language. And it's wonderful, actually, that these multimodal models,
*  getting so powerful, because they're going to be very helpful vision, they're going to lead to faster, better use cases for vision than they do today.
*  That's a good guide to what the future might have in store for us. How are you thinking about building a business through this maturation of the technology? Like, are you trying to grow a lot of revenue today? How much do you care about adoption and your sort of relative position in the market, you know,
*  compared to other options, you know, from a funding standpoint, I know you had some capital already on hand when you pivoted into this. But, you know, I imagine more would be helpful. Like, how are you thinking about what do you need to do to raise more money if you need or want to do that? And just the timing of it. It's like very weird, right? Because we're, it seems like unlike previous technology waves, so much is in the future relative to what you can achieve today. And I wonder how you think about like, meta-mode,
*  metrics, milestones, you know, kind of proof points versus this like grand strategy, how you kind of balance those and try to make them work together.
*  Our overall main quest is to make like a unified vision model, you know, whether it's images, video, 3D, etc. Something that has true general understanding of pixels and such. But I think like a very simple thing we're doing this year is we're only going to be working on two things. We're going to work on making a really great
*  graphics model for just static 2D images, because a vast majority of the utilities still gone unsolved. And so, yeah, I mean, I think it's not that complicated, I think, in the sense that right now, if you want to do things with Photoshop or Lightroom or Illustrator or whatnot, I'm not an expert at these tools.
*  I, you know, there was a time where I was like doing Photoshop tutorials in high school, try like compete in logo contests and stuff. Since then, my skill has greatly at your feet. But, you know, I'm not an expert at this. And I think a vast majority of humanity is not. It seems it seems like there's clearly like, people that buy buy things and manipulate want to buy graphics or manipulate pixels and wish they could and just don't. You take the picture to get a better one. And then there's people that have like really amazing skill. They're expert color graders, they're experts at making things work.
*  They know how to get rid of like dangly hairs, your wedding picture, they make logos in Photoshop, whatever, or they're really amazing illustrators. And it takes a lot of skill to be that good. And so, you know, I think the extent to which we can kind of like, give more of humanity, the ability to do that kind of work, but kind of like own, like be the, you know, instead of going through a third party, be able to actually do.
*  Some of these things on their own very easily. I think that will open up doors for us. And so I think we'll be very focused on just creating images and editing throughout the year. And I hope that leads to a lot of the happy users for whom I think have no alternative right now, other than kind of asking a friend or going somewhere where there's someone that is talented, hiring somebody basically.
*  That feels like a little bit of a change from last year and maybe from kind of, you know, the usual advice of like fast iteration, talking to users, this feels a little bit more. And I've heard similar comments from Sam Aldman recently where he was like, you know, at YC, I told everyone, you know, launch super early, iterate super frequently, you know, and then in OpenAI, we took four years to launch anything. And, you know, we had like a massive, you know, capital outlay. And, you know, we didn't really know what the use case was.
*  It sounds like you're kind of shifting a little bit more toward that approach. We were like, build something truly awesome. We kind of know what that is in our gut. And that everything else will kind of follow from there.
*  We've had maybe we didn't talk about it last year too much, but kind of had the same plan since the company started. But I do want to say like over the last year, we shipped like 100 things.
*  Yeah, the product has changed a lot. No doubt about that. Every time I've gone in there, it has been notably more feature rich for sure.
*  You know, we have a Slack channel where we see every complaint from a user, you know, I don't like the hands, you change too much. How do you, you know, I get DMs from customers or even friends.
*  Hey, how do I make this character kind of consistent? And the kind of like combination of these things turns out like there's no like one, there's no quick fix.
*  Just all of these things. Some I think there are certain class of problems where you kind of you accumulate them and you go, well, actually, there is no quick fix for this.
*  The worst product that we could make is a product where we have a button that's like the fix hands button. And then there's like a fix the eyes button. And then there's like a, you know, the character consistency.
*  But like, nobody wants to use a product like that. That was a very complicated product to use. You have to know where everything is. And then people are confused and you have to figure out ways to train them.
*  You got to train a whole language model on top of that.
*  Right. And then you know your language models like choosing which model to use at what point. And then of course, like now your interest times are growing up because you're using each model the pipeline to fix one thing and this model fixes the thing.
*  But then it kind of made the other some other thing worse. Right. This is not a great experience. And so this is all patchwork stuff that's just not going to lead to a world class product.
*  And so I think my belief is that we actually distilled we know what users are frustrated about every single day with the current state of the art.
*  And, you know, we bought a lot of GPUs and we found a lot of really amazing researchers. And so it's not like I think we're going to go solve the every imaginable editing and graphics problem, you know, day one or even or we're going to wait three years and we're going to have something.
*  I think it's I think that like as long as we can make a few things very useful that are generally useful that attract a lot of users for whom like oh wow I didn't know I'm finally happy someone solve this problem.
*  I think that you can you can build like a great you can you can start from something kind of small that starts to become bigger. And I think a good example of this actually is like if you look at mid-jury and what it looked like kind of early last year compared to what it looks like this year.
*  It might seem surprising than anyone paid for the thing early last year, right? But nonetheless, you know, nonetheless, it was the best at the time. And then over time, you know, these things kind of grow and they sort of mature.
*  And so maybe what we'll have is something that's like a PS2 or a PlayStation one, but it's still very fun to play or use rather. And then like over time, you know, we'll certainly keep making our version of our models better and better.
*  One other big picture question I wanted to get your take on obviously we're in this moment of all this stuff is so new, you know, people are the fallout is just beginning.
*  Mostly positive, some negative, and we really don't have new kind of guiding rules or principles in many cases even for like how should we handle all this? Like what should the rules be?
*  I just did another episode on New York Times for OpenAI. And I guess my super big picture question to you is like, do you have any thoughts at this point as to what the rules should be?
*  Like that could be at the training data level, you know, should everything, you know, I think Japan is kind of going this direction where they're going to make everything available for everybody to train on.
*  You could imagine people should be, you know, compensated if they're included. You could imagine people should be able to opt out, but not necessarily be entitled to compensation.
*  You could imagine like I should not be able to ask for everything in the style of Greg Grudkowski, or maybe that's okay.
*  You know, can I make Mario and Luigi on Playground AI? There's just so many questions. I don't expect you to answer them all, but I wonder what your kind of emerging sense for what the rules of the road for the generative AI era should be.
*  I try to sometimes put myself in the shoes of, you know, let's say the artists or the people making these images, tarps, whoever, you know, because, you know, obviously we have a rational self interest on training on data like that.
*  You know, we were the first site. I read Greg Grudkowski's story, it's kind of op-ed and tried to like try to understand him better to the extent I can. I don't talk to him.
*  But, you know, I looked at his page on DeviantArt, I get his style. And I think there are like two things that are kind of happening. One is, nobody, people don't really want to make art like Greg Grudkowski.
*  It's not very exciting to make. The users that use these products are actually people that like think of themselves as artists in some ways.
*  And nobody, people that are artists don't really want to copy another artist, claim their art. There's no pride in that, right?
*  It's not like these people are making images and they're really selling them for thousands of dollars or anything. So they're not taking pride.
*  I don't think a vast majority of people are taking pride in that. And the other thing is, you know, after I read his article, we were the first site ever and I think the only site still to this day for whatever reason,
*  where if there was a prompt on our site and someone references his name, we directly link back to his page. We actually give him, we actually call it additional credit.
*  Literally say, it's an additional credit. Say Greg Grudkowski, link back. Because one of the things he said was that in Google search, now it's like people can't even find him.
*  And I thought, well, maybe one way that we could at least help him is helping people find his actual art, pay for it, whatever.
*  At least give him fame, some other way to evolve in a world where maybe if the pain was growing for him, maybe we could use that a little bit.
*  So I think there's small things that we can do. I'm not saying that that fixes and alleviates the issue for Greg in any shape or form. Just saying that I think there might be some small things that we can do.
*  I think some bigger things. The other reality is that it's not like you can't make Mario and Luigi in Photoshop or Illustrator.
*  And the rules around that are like, of course you and I can be in the skills that we can make Mario, Luigi, or Mickey Mouse or whatever.
*  But we can't just go run around starting to sell t-shirts with like Nintendo brandy either.
*  And so I think there's like another world where there's kind of a balance point where like it might be generally okay to make things.
*  In fact, many brands are perfectly fine with fan art or whatever.
*  But when there's kind of this question of commercial use, that's where things kind of like stop.
*  And I think that's like a fair area to say, oh, people are just kind of having fun.
*  But when they start selling t-shirts in the thousands with kind of like a bizarro world looking Mickey Mouse, maybe that's not okay.
*  Right. And so I think that that's like probably okay too.
*  I think it's going to be very hard, even if the model are not trained necessarily on like Mickey Mouse or Mario and Luigi.
*  I think it's going to be very hard to get these models.
*  At some point, like the models will have some representation of it, even if it hasn't necessarily strictly seen.
*  Even if you go to try your best to comb through the data set, there'll always be something missing or you'll just have like some way of like understanding concepts of it.
*  I think that's like a very impractical thing. I think the G is a little bit out of the bottle, but I think it's better.
*  It might be better to actually talk about like use as opposed to like strictly training data.
*  That's kind of my view. I feel like there is. I also think the last part of this is maybe how fast it goes.
*  If this whole thing is very gradual, then I think like probably society would find like some way to assimilate to it.
*  I think if it's vastly faster than that, if it's like a step function thing each time, then I think that we definitely need to do something about that.
*  I think that who it's impacting like very much needs to be considered. It cannot just be like thrown away and you can't ask people to evolve and upskill.
*  You know, something that they've trained on doing their whole like something, some craft that they've been doing for a decade or two and ask them to like kind of upskill and evolve and catch up to the times in a couple of years.
*  So I don't think that's like a real rational path. So that's kind of like my rough triangulation of things.
*  My feeling around like rev share on training data, it just seems like it's going to disappoint people more than it's going to be practical and helpful.
*  So I'm a little less sure on how we would really achieve that.
*  Yeah, it's tough, right? If you are the artist that used to charge however many or even just the PowerPoint technician that used to charge however many dollars for a job.
*  And now that can be done for a cent or whatever on a technology tool. The rev share on that cent is not going to buy too much.
*  Yeah, I make music so I sometimes think about like what if people would train on my music? What if I was a bigger artist and they trained on kind of how would I feel?
*  Like this sort of rev share model, like streaming revenues are really bad for music artists.
*  This like penny per thing always makes the artist feel like they're greatly undervalued. It leaves tons of resentment in the industry.
*  So, you know, I'm not so sure about that. On the other hand, though, I think artists very much crave like an audience, like ways that they can like it.
*  Making rubber house art is definitely not the same as like buying this art. I think that's a very different relationship people have with artists.
*  You know, if I make a song that's exactly like a Vici, people will be like, you just sound like a Vici.
*  But they're not. It doesn't mean my song will become big in the world because people have built the relationship with the artists.
*  And so, you know, I just I think that something that's really catering to helping kind of give kind of a spotlight to the artists, the real people involved in doing some of this stuff, I think would be very helpful because I think there's still a big audience of people that want that.
*  You know, if you can reproduce the same exact image or something like it.
*  So how fast do you think it's going to go? And do you think we are headed for kind of a new social contract?
*  I mean, I'm getting like UBI vibes a little bit from a couple of your comments there.
*  No, I don't. I don't have any strong opinions around how to solve it.
*  I think that there are much better minds, much better people are well versed in trying to understand what happens with technological change.
*  How do we retool people? How do we maybe it becomes like a tax.
*  I don't know. Yeah, maybe maybe it is kind of like a UBI tax sort of thing for certain for certain industries, certainly investing in helping people like upscale.
*  You know, one funny thing out of the art debate was I once talked to someone who really hated the AI art stuff like a year and a half ago.
*  And some of these people don't want to retool.
*  One of them said, I just enjoy drawing. You know, I don't want to reach out. I want to get new skills.
*  I just I enjoy this craft. And so I think there's like also a practical reality about that.
*  You can't ask people to retool when they don't enjoy the craft anymore because they enjoyed it the way that it was.
*  So I definitely think there'll be some version of this. I don't know how I don't know how you distribute my little like that.
*  I don't have any sense. I do think that I do think it's very it's going to be very fast, though.
*  I don't think it can be ignored. I think it would be I think we'll be making a very big mistake over technology industry.
*  We just sort of say, throw caution to the wind and kind of go, we're we're just going to do this very quickly.
*  We don't care who it impacts. I think that the last decade of technology and the tech industry in particular has showed that when we do that,
*  we really disenfranchise people and that creates kind of like a bad circumstance for our industry.
*  And I hope that we've learned that lesson. Yeah, I totally agree. OK, one one more little follow up because I can't resist.
*  I've been thinking lately not so much for the art side, but there's probably a lot of commonalities.
*  What are the minimum standards that AI application developers should be expected to uphold?
*  Meaning, you know, if you didn't do this, you are worthy of like shame within the industry, even if there are no laws yet on the books to control what happens.
*  I wonder if you have any thoughts as to, you know, kind of what AI developers should demand of one another.
*  Presumably there will be actual rules coming. But as we kind of ease into that and hopefully maybe even can inform what they might look like so they don't end up being dumb, which is a very real risk, I think.
*  You know, what would be a good sort of self governing, you know, maybe just the kernel of a self governing standard that we can all kind of say, hey, this is we got to do this, guys, at least.
*  There's already kind of like a pretty reasonable consensus around safety.
*  And unfortunately, safety kind of got wrapped around overloaded with like alignment and stuff.
*  But and so I try to come up with like a different word sometimes for situations.
*  Anyone operating these malls has seen extremely bad actors.
*  We all have like our version of the story that just extremely, extremely bad.
*  And so there's just general evil out there and people how they're using these tools.
*  And so, you know, we one of the things that we did at Playground is the existing state of the art kind of like safety filter that sort of stops, regardless of like your point of view, you know, we don't we don't personally want like new content on our site, for example.
*  And other forms of content like that.
*  And I think, you know, so we ended up like training and you sort of say the art safety filter that went went further.
*  Of course, like it helps us. We don't have to moderate as much, but also just like it just reduces significant evil that tends to occur in the world.
*  Not that nude images, in particular, evil, but like there are definite classes of images that are more evil or illegal in our country than than than other classes of images.
*  And so I think they're, you know, I just think like people using images for like deepfakes and using out of revenge and how we're going into like a new election year, how things are going to be manipulated, how how we're going to explain to our aunt or uncle or parents or a brother and sister.
*  That thing that they saw on the Internet was actually not real, even though maybe it's their narrative, it's actually technically wasn't real.
*  So I think just like combating just the sheer disinformation misuse evil that like might occur using these tools because the tools tend to be extremely powerful.
*  And so they have incredible amounts of value for the world.
*  But it turns out that that like can totally be used for like nefarious things.
*  And so I just think that that seems like the most basic thing that we can all do.
*  And I kind of wish, you know, one thing that I wish is that the safety parts of this business were probably I wish they were a lot more open, actually, you know, like, you know, opening has like a moderation model, we use it.
*  It's free. We use it. They don't charge you anything for unless you use too much of it.
*  But too much of it is a very high threshold.
*  And I just wish that maybe we'd have like a formal open collaboration around any of this kind of stuff because we all have different kinds of data and we would all do better if we worked a little bit better together on this and it would be better to have like a state of the art model.
*  It's not too easy. It's not that difficult for like nefarious actors to test these things and try to like work around them.
*  I think we could beat this cat and mouse race if there was more a larger set of companies working on an open set of safety models.
*  I don't think it would take away from anyone's core IP or anything like that.
*  I think the world would be better off for it.
*  And that one might be a very, you know, the model ends up the model's performance would end up being kind of like a definitive answer to your question around like what should we all be doing?
*  That is like a minimum standard. Well, actually the minimum standards high dimensionality to it could be encapsulated in small that we all work on together and all contribute together and the best researchers in the field work together.
*  It's a beautiful vision. The opportunity and the peril of generative AI, I think very well articulated there.
*  I think it's a great note to end on. I will say again, so hail Doshi. Thank you for being part of the cognitive revolution.
*  Thanks for having me.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me on the social media platform of your choice.
*  I'm going to key uses generative AI to enable you to launch hundreds of thousands of add iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it to use cog rev to get a 10% discount.
