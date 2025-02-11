---
Date Generated: December 03, 2024
Transcription Model: whisper medium 20231117
Length: 5088s
Video Keywords: []
Video Views: 11385
Video Rating: None
Video Description: Nathan explores the world of AI-powered design with John Milinovich, Head of Generative AI Product at Canva. In this episode of The Cognitive Revolution, we dive into Canva's innovative approach to AI integration, from task automation to human augmentation. Join us for an insightful discussion about fine-tuning foundation models, AI's impact on architecture, and practical tips for AI product development at scale.

Check out Canva: https://www.canva.com

Be notified early when Turpentine's drops new publication: https://www.turpentine.co/exclusiveaccess

SPONSORS:

SelectQuote: Finding the right life insurance shouldn't be another task you put off. SelectQuote compares top-rated policies to get you the best coverage at the right price. Even in our AI-driven world, protecting your family's future remains essential. Get your personalized quote at https://selectquote.com/cognitive

Incogni: Take your personal data back with Incogni! Use code REVOLUTION at the link below and get 60% off an annual plan: https://incogni.com/revolution

Shopify: Shopify is the world's leading e-commerce platform, offering a market-leading checkout system and exclusive AI apps like Quikly. Nobody does selling better than Shopify. Get a $1 per month trial at https://shopify.com/cognitive

Oracle Cloud Infrastructure (OCI): Oracle's next-generation cloud platform delivers blazing-fast AI and ML performance with 50% less for compute and 80% less for outbound networking compared to other cloud providers13. OCI powers industry leaders with secure infrastructure and application development capabilities. New U.S. customers can get their cloud bill cut in half by switching to OCI before December 31, 2024 at https://oracle.com/cognitive

Brave: The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

RECOMMENDED PODCAST:
Unpack Pricing - Dive into the dark arts of SaaS pricing with Metronome CEO Scott Woody and tech leaders. Learn how strategic pricing drives explosive revenue growth in today's biggest companies like Snowflake, Cockroach Labs, Dropbox and more.
Apple: https://podcasts.apple.com/us/podcast/id1765716600
Spotify: https://open.spotify.com/show/38DK3W1Fq1xxQalhDSueFg

CHAPTERS:
(00:00:00) Teaser
(00:01:13) Sponsors: SelectQuote
(00:02:26) About the Episode
(00:04:33) Introduction - Creativity vs Design
(00:08:39) AI-Assisted Experiences
(00:10:25) Automation & Augmentation
(00:15:27) Pixels to Objects to Concepts
(00:17:58) Sponsors: Incogni | Shopify
(00:20:40) Concept-Level Interfaces
(00:23:35) The Future of Design
(00:29:39) Human Element in Design
(00:32:49) AI Talking to AI
(00:35:52) Sponsors: Oracle Cloud Infrastructure (OCI) | Brave
(00:38:04) Purpose-Specific AI Experiences
(00:45:29) GPT-4 Image Editing
(00:51:17) Graduated Approach to Launch
(00:55:09) Fine-Tuning GPT-4
(00:59:10) Cost & Latency
(01:01:29) Hiring AI Engineers
(01:05:02) Engineering Best Practices
(01:09:00) Inspiration in the AI Space
(01:18:28) The Gen AI Application Layer
(01:24:26) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Designing the Future Inside Canva's AI Strategy with John Milinovich, GenAI Product Lead at Canva
**Cognitive Revolution:** [November 23, 2024](https://www.youtube.com/watch?v=onAFbxq21Ck)
*  At the highest level, there's automation and augmentation.
*  What people want from automation is to remove the ick from something that's just super annoying
*  to do. As a user, you know what you want the outcome to be, but you just kind of want it
*  done for you. The other dimension here is augmentation, which is I am fundamentally in
*  the driver's seat. I am working towards something that I can't quite see what it is in my head yet.
*  And I want a set of tools or a suite of capabilities that help me take that like fuzzy
*  feeling and make it into something that's more concrete. One of the real original innovation
*  at Canva was moving design from a world of pixels to a world of objects. When you look at what AI
*  is doing is we believe it's moving to a world from like object level manipulation into a world of
*  like concept level manipulation. I think generally our development flow is just like make it work,
*  make it good, make it fast, and then make it cheap. I think about that really as the problem
*  orientation versus the solution orientation. Oftentimes the outcome is like so clear that we
*  can see it, but being able to actually deliver on that is extremely, extremely difficult. If you're
*  topping out at 81 and we know we need to get to 98, like it probably means that you may need to
*  maintain the problem focus for such a solution. There are so many things in life we just never
*  get around to. Taking up that hobby, cleaning out the garage, you know, little things that don't
*  really make huge differences in our lives. Yet there's one thing that most of us have probably
*  been neglecting that can have a huge impact on our family's future. It's life insurance. And with
*  select quote, getting covered with the right policy for you is easier and more affordable than
*  you might think. As someone who tracks AI progress on a full-time basis and obsesses about its
*  potential impact nonstop, I know how tempting it can be to ignore more mundane, familiar risks.
*  There's always another paper to read, podcast to listen to, or product to try. And yet the smarts
*  people that I know in the AI space continue to save and invest money for the future, carve out
*  time for their relationships, maintain their physical and mental health, and yes, protect
*  their family with life insurance, just in case anything should happen before the singularity.
*  If nothing else, it's one less thing to worry about in a time of unprecedented change.
*  So get the right life insurance for you, for less, at selectquote.com slash cognitive. Go to
*  selectquote.com slash cognitive today to get started. That's selectquote.com slash cognitive.
*  Hello, and welcome back to the Cognitive Revolution. Today, my guest is John Milinovich,
*  head of generative AI product at Canva. For anyone who's not already familiar, Canva is an
*  online design platform with a mission to empower everyone in the world to design anything,
*  which has scaled to serve now more than 200 million users globally with its highly accessible suite
*  of design products. More recently, Canva has also become a leader in AI-powered design experiences,
*  with a mix of point solution features like their excellent image background removal tool,
*  more horizontal features like their magic write tool, which attempts to write in your
*  brand's voice across their entire product suite, and AI superpower features like their new DreamLab
*  text-to-image product, which was derived from their acquisition of Leonardo AI,
*  reportedly, although this is not confirmed, for some $320 million. In this episode,
*  John shares Canva's framework for thinking about task automation versus human augmentation,
*  Canva's approach to testing and evaluating AI features, insights on fine-tuning foundation
*  models, and a fascinating discussion on how AI might transform fields like architecture
*  where John began his career. We also dig into practical tips for AI engineering,
*  with John emphasizing the importance of maintaining problem orientation,
*  rather than getting too attached to any particular candidate solution.
*  This conversation was a super fun opportunity for me to trade notes with another generative AI
*  product leader whose expertise has been demonstrated at global scale. I think there's huge value here
*  for anyone who wants to level up their thinking about what sorts of experiences AI can unlock,
*  and also how best to go about developing and deploying them. If you agree, we'd ask that you
*  take just a second to share the show online, write a review on Apple Podcasts or Spotify,
*  or just post a comment on YouTube. Of course, your feedback is always appreciated too.
*  You can contact us via our website, cognitiverevolution.ai, or by DMing me on your
*  favorite social network. Now, I hope you enjoy this behind-the-scenes look at AI product development
*  at scale with John Milinovich of Canva. John Milinovich, head of Gen. AI product at Canva.
*  Welcome to the Cognitive Revolution. Thank you so much, Nathan. I'm really excited to be here today.
*  Big fan of the podcast, which you all are doing, Interpret Time Network.
*  Cool. Thank you. I appreciate that. Well, right back at you too. Canva obviously has been a
*  leader in the design software space and helping people who are maybe not creative professionals,
*  but still are at least a little bit creative to realize their visions for a number of years.
*  Definitely a company that I've watched closely. I don't know if you know about me, but I started
*  a company called Waymark that is doing a similar thing, but very much for video advertising for
*  small businesses. So a narrower scope, but very focused in on that one use case. We've obviously
*  looked at Canva quite a bit and always kept an eye on what you guys are doing and the product
*  leadership sort of speaks for itself. I wanted to start off with a big picture question about
*  creativity and how you think about helping people be creative or how creative they really
*  want to be. I'm wondering how many people really want to be creative versus want to
*  totally outsource that creativity and maybe were limited in the past by budget, but maybe in the
*  age of AI just want stuff done for them. How do you think about how the population breaks down
*  and what's your kind of framework for figuring out how to balance enabling their creativity versus
*  just getting things done that they need done? I love this question. I love these types of big
*  philosophical reflections as well. I think first order is important to delineate design from
*  creativity. I view design as the process of generating or synthesizing new ideas, whereas
*  design is much more of a goal-directed process that's really trying to produce some kind of
*  an output to communicate some goal or to accomplish some kind of mission that you're setting out for.
*  I think what we've seen is actually that creativity is something that is like the highest enjoyment
*  for people and that people generally want to spend the most amount of their time doing.
*  When it comes to design, we've actually done a lot of user research on this and actually what
*  we've seen is actually a perfect split of a third of people want to spend more time designing,
*  a third of people want to spend less time designing, and a third of people want to spend
*  about just the same amount of time doing it. I think what this really makes it clear for us
*  as Canva is that our job is to really just help break down the barriers for true global creativity
*  and also give people the tools they need to really augment and enrich their workflows no matter where
*  they fall on that spectrum. I think generally how much automation or how much augmentation
*  people want, which is something I'm excited to dig into and talk more about that difference,
*  really depends on the type of job that they're trying to do and how much of that creative
*  expression they want to put onto the process versus how much they view it as a production-oriented task.
*  Yeah, okay. That's interesting. A third, a third, a third. Are you trying to serve
*  all those people? We have like obviously Adobe is out there for the people that really want to
*  specialize in the craft of a certain kind of design. Are you trying to support all of these
*  different profiles or how do you think about what are the really in-focus user perspectives for Canva?
*  Definitely. I think within Canva is 200 million plus users who would definitely have a mix of all
*  those types of folks. I think the thing that I think is so exciting to me about Canva and our
*  mission to empower the world to design is that we're really trying to actually give people
*  creative confidence where they might not have otherwise had it. There's this really unique
*  kind of gap in the market that enabled Canva to get to the scale that it's at, which actually does
*  help people no matter where they are on that spectrum actually express themselves in a way
*  that makes them feel proud and ultimately it makes them feel good about themselves. I think that even
*  within that spectrum of those 200 million plus that Canva creates, there's a really wide range
*  of what people are looking for there. I think what we're really trying to do is help support all of
*  them. I think that is obviously a difficult task from a product experience standpoint,
*  but I think it's also something that I think we've done a pretty good job at for the last decade.
*  Maybe you could organize this by personas. How do you think about the kinds of AI-assisted
*  experiences that these different folks will be best served by? In our case at Waymark, we
*  really started to hear, and this is really what set me off on the AI journey that has now become
*  personal consuming obsession, but we really started to hear from people in the 2020-2021
*  timeframe as we had finished our in-browser rendering and finished all the easy to use
*  editing features and whatnot. We were, okay, what can we do next to make this product better and
*  easier to use for you? People started to tell us, nothing really comes to mind. They would be like,
*  it is pretty easy to use. That's not really a problem. I just don't have that many ideas.
*  I don't really know what to say. I find writing to be kind of a challenge. We were like, man,
*  that's going to be really hard for us to UI our way around. I think for our user type, which
*  canonically is like small business owner who is the typical story there is they open the bakery
*  because they love to bake and now they've got all these other responsibilities. I think that's
*  definitely a private Canva target user too. We found for our people that they mostly just wanted
*  this done for them and that has led us to a very, tell us what you want. We'll try to make it for
*  you. One thing I was struck by as I was looking at Canva over the last few days is there's a lot
*  more local utility tools, some of which are extremely well done and definitely lead the
*  market. The background removal is top notch and hard to match otherwise from what I've seen,
*  but there's less of a super big picture. Give us your high level idea in 10 words and we'll spit
*  all out at you. Really interested in how you've thought about those forking paths and which ones
*  you've chosen to go down. I think at the highest level, again, there's automation and augmentation.
*  I think generally we've seen what people want from automation is to remove the ick from something
*  that's just super annoying to do. This is where things like background remover is a great example
*  or something like magic switch where you're converting a doc into deck format or things like
*  even magic sort within our new whiteboards product where you can take all the sticky notes from a
*  brainstorm and put them into a new order. There's things where there's like as a user, you know what
*  you want the outcome to be, but you just kind of want it done for you. I think that's automation.
*  The other dimension here is augmentation, which is, hey, I am fundamentally in the driver's seat.
*  I am working towards something that I can't quite see what it is in my head yet. I want a set of
*  tools or a suite of capabilities that help me take that fuzzy feeling and make it into something
*  that's more concrete. Really turn that idea into reality. I think that's really been where I think
*  the, again, it's a much fuzzier bounce there because it's less obvious how can measure the
*  outcome as a user where you know it when you see it in a way. I think we think a lot about our
*  product portfolio in these two different dimensions of augmentation and automation.
*  I think generally speaking, when it comes to things that are more augmentation focused,
*  what we've seen is that having really natural AI integration points, the existing product is really
*  the best way to drive this forward. So it's very fundamentally like an embedded AI strategy where
*  we're trying to, again, put AI at the point of need for users so that it can actually help them
*  assist in whether they're again looking for that automation task or that augmentation task.
*  I think that when you're asking about having maybe a more separate or AI native experience,
*  actually this is something we've been thinking about and actually DreamLab, our first point of
*  view or opinion on what kind of a separate, maybe more AI centric experience can look like. So
*  DreamLab is a new text image generation product that Canada just launched with our Leonardo team,
*  which is incredibly incredible in addition to the Canada family. And ultimately what DreamLab does
*  is it actually expands the use cases that people have for Canva because our magic media product,
*  which lives in the editor for text to image generation, helps the user when they're actually
*  in the process of doing an existing design. But the mindset is, hey, I'm designing a social media
*  post for my daughter's first birthday. I want to find that perfect image or create that perfect
*  image for it. Whereas, and that's one kind of call it serviceable market. But when you look at
*  what you can do with image generation in general, there's a much wider set of things that maybe
*  isn't tied to a specific design. So I think when we talked about that creativity and design
*  delineation up to the top, something like DreamLab is actually much closer to the creativity of the
*  spectrum that I think is again very much about augmenting a human's capabilities. So I think
*  this is something we're getting a lot of positive feedback about, we're excited about,
*  and would be excited to think about other potential opportunities for these more AI
*  native experiences in the future as well. I did use the new Leonardo DreamLab to create
*  almost exactly what you said. I went in and asked for a birthday party invitation for my
*  soon to be six year old with astronaut dinosaurs. And it's always worth for me reminding myself of
*  just how new all this stuff is, just how recently it's gotten so good. Because even the original
*  stable diffusion, which was obviously a tipping point moment for the field, couldn't do anything
*  like that. And it even placed the text, but it did a really nice job of laying the font in that said
*  Ernie's sixth birthday. And then it had a lot of made up stuff that wasn't actually coherent text
*  below that where it was like, maybe if I had given it our address and the time and the date,
*  it would have also set that perfectly accurately. But I didn't. And so it just like did like an
*  abstract form of that, which then I went back and erased and at some point maybe can fill in.
*  I guess a big question that I have there around the image generation is how you guys are thinking
*  about the right level of abstraction for the AI to be working. Interestingly, at Waymart, we still
*  haven't integrated a straight up text to image generator, because we feel like that hasn't been
*  quite controllable enough for our small business users, they want to represent their real business.
*  And then they might be able to get like astronaut dinosaurs, but when they really want to show their
*  business and set realistic expectations and show themselves off in the way they want to show up,
*  it just doesn't quite hit the mark well enough. And so we tend to be a little bit higher level
*  where we present to the AI like, here is the structure that we want you to follow. And it's
*  like your job to fill in these different dimensions. So on the one hand, you have every pixel is
*  generated by AI, and it's all kind of one layer. And then on the other end, you maybe have like
*  choice of template kind of totally decisions. What do you find to be the right balance? Or how do you
*  organize your thinking about that when you have so many different options?
*  I think that so one thing that I've heard Mel, Canvas CEO and virus leader say many times,
*  one of those things that just kind of lives rent free in my head is that one of the
*  real original innovation of Canva was moving design from a world of pixels to a world of objects,
*  right? So being able to have all this integrated inventory of all these elements, this whole
*  template library so that every stock photo, every graphic, every video, every font you could ever
*  want was just all in one place. And you could just drag and drop it in this really easy to use an
*  intuitive editor. That was really the market opportunity that led Canva to really grow and
*  take off in the first place and make again, creativity accessible in a way that it wasn't
*  before. When you look at what AI is doing is it's I think we believe it's moving to a world from
*  object level manipulation into a world of concept level manipulation. So instead of having to
*  only work at the level of objects, which will always be a place for you're able to now do these
*  higher order extractions or higher order manipulations. And again, when you think
*  about this in a world of text generation, or when we think about something like Claude's artifacts
*  product, there I think it was a deliberate product decision for them to not let you select or
*  manipulate specific pieces of text, but instead asked to do these more conceptual edits across
*  the entire generated markdown file. I think that similarly within kind of the image generation
*  space and with these new multimodal diffusion transformer models that have really kind of
*  been a huge innovation and, you know, text and image alignment, but also ecosystem of innovations
*  around comfy UI pipelines or control nets and things. I think we're seeing a new level of that
*  conceptual control also being available. So things like being able to do depth maps, so you can
*  actually do things like really like I rendered architectural models or things like pose destination
*  models where you can get the exact pose of a person or content models where you can actually
*  maintain the overall conceptual or semantic meaning of an image or like style control.
*  So I think that what's happening now is that similar to how we went from pixels to objects to
*  concepts, that right concept level control is like what I think is really starting to win out at the
*  level of image generation. You see a lot of interesting movements in this space as well with
*  things like Cree as real time generation or Leonardo's real time generation, where you can
*  also just design and high level abstract rectangles and circles, put that with a text prompt and see
*  what comes out. And I think that this is a shows a really promising direction for future.
*  Hey, we'll continue our interview in a moment after word from our sponsors.
*  Regardless of how you felt about the outcome of the election, I think we were all united in
*  looking forward to an end to the constant fundraising emails and text messages. Unfortunately for me,
*  they haven't stopped even now more than a week after the election. And that's to say nothing of
*  the normal commercial spam coming at me from all directions at all times. It turns out that most of
*  this noise is caused by data brokers. These companies aren't just collecting your contact
*  details. They're gathering everything from your social security number and financial records to
*  your online shopping habits. And they're now working with insurance companies, which could
*  potentially impact your rates. That's why I'm excited to now be using incognito. Incognito
*  contacts five types of data brokers, marketing, recruiting, financial information, risk mitigation,
*  and people search sites and demands that they remove your information. Then they continue
*  monitoring on your behalf to prevent data recollection. Take your personal data back
*  with incognito or protect up to four family members with their family and friends plan.
*  They offer a 30 day money back guarantee if you're not satisfied. So take your personal data back
*  with incognito. Use code revolution at the link below and get 60% off an annual plan.
*  That's incognito.com revolution.
*  The cognitive revolution is brought to you by Shopify. I've known Shopify as the world's leading
*  e-commerce platform for years, but it was only recently when I started a project with my friends
*  at quickly that I realized just how dominant Shopify really is. Quickly is an urgency marketing
*  platform that's been running innovative time limited marketing activations for major brands
*  for years. Now we're working together to build an AI layer, which will use generative AI to scale
*  their service to long tail e-commerce businesses. And since Shopify has the largest market share,
*  the most robust APIs and the most thriving application ecosystem, we are building exclusively
*  for the Shopify platform. So if you're building an e-commerce business upgrade to Shopify and
*  you'll enjoy not only their market leading checkout system, but also an increasingly robust
*  library of cutting edge AI apps like quickly, many of which will be exclusive to Shopify on
*  launch cognitive revolution listeners can sign up for a $1 per month trial period at shopify.com
*  slash cognitive where cognitive is all lowercase. Nobody does selling better than Shopify. So visit
*  shopify.com slash cognitive to upgrade your selling today. That's shopify.com slash cognitive.
*  I like the notion of exposing concept level interfaces to the user from an implementation
*  standpoint. Probably the answer is both. I feel like I can guess where this goes, but I wonder if
*  you have any more nuanced comments than both when it comes to, okay, to the user will expose concept
*  level controls. But what do we ask the AI to do? Do we ask the AI to do object level work or do we
*  ask it to go down to like pixel level work? And maybe it just depends on the use case, but
*  I'm interested in how you have those decisions. Silly does. Of course, the answer is it depends,
*  but I'll try to give a little bit more depth than that. When you think about even the
*  domain of design that Candle works in, of graphic design, which again, it limits it,
*  but it doesn't limit it that much. Right. Graphic design is a massive domain. Today there's over
*  500 different design categories that are supported on Canva. And if you look at each of those and
*  you can map them generally into a spectrum of how much it's about the form versus the function
*  of the thing. Right. So the form, it's much more purely about the aesthetics or the visual nature
*  of it on a functional level. It's much more about the text or the content that's being explained.
*  So on one extreme of form, you have something like maybe a logo or social media posts on the
*  other extreme of function. Maybe you have something like a doc or a whiteboard. And I think when you
*  look across that spectrum, the level of expectation of both what the user wants to be able to do,
*  but also what we need to ask the AI to do is very different. And I think what we're starting to see
*  is that the world of large language models and diffusion models is really starting to converge.
*  And this is true both at a model architecture level, like again, generally a lot of what's
*  happening in the multimodal space and be able to have these new types of cross-attention mechanisms
*  at the encoder level, but also then at a user experience level, being able to actually let
*  users work at a concept level to start with, and then pop into things at the object level
*  where it makes sense. So for things that are generally more functionally oriented,
*  you can probably get really far to start with at a concept level. Again, think of
*  cloud artifacts or markdown files to start with, but then you still need to be able to let a user
*  at the end of the day tweak the wording. So that's, you can imagine they're starting from concept,
*  jumping into object. And similarly, when it gets you on the other side of the extreme form,
*  you actually want to start at a concept level, planning a thing or be able to explain what is
*  the vibe you're going for with your logo, but you still need to actually have some lower level
*  control to change the current, for example. I think there's just a wide range of use cases
*  within the domain of design that the combination of large language models and diffusion models
*  offers an interesting perspective at both of what the model capabilities can be in the future.
*  The hard part for Canva and the industry is figuring out the right native interfaces on
*  top of all of this to make it not overly confusing to users. Yeah. So what do you think the future of
*  that is? Cause I feel like everything is trending toward, not everything's an extreme statement,
*  but a lot of things are trending toward a open, just tell us what you want starting point.
*  And so I would imagine like a future of Canva, me being like confronted with probably some
*  suggestions or whatever, not that this would be the only way to interact, but like a natural
*  first way to interact would be just tell us what you want to create. Next step would be,
*  here's a version of it for you and then drop down into those object level or pixel level
*  refinements as needed. Is that kind of the vision that you have for the product or do you
*  want to zag where everybody else is going in that direction? Yeah. I think that one of the things
*  that we've seen in general is that people want more or less the same amount of design.
*  We really appreciate it, especially when you take a very global view here, people have different
*  modes or different means of being able to communicate the most effectively. And especially
*  it's true in design. Even if you ask three professional designers to describe a design,
*  they're actually might all do it in very different ways. Or if you ask five different designers to
*  explain what modernism is and what it means for modern logo design, you probably get a
*  different answers. So I think that there's a huge opportunity for just building a more natural
*  interface for users to be able to interact with all AI systems, certainly design oriented ones as
*  well. But I don't think that should be just limited to tech. I think that especially for
*  things that are inherently multimodal, like you need to be able to convey ideas through
*  imagery, through touch, through gesture, through voice, through text. I think design is by
*  definition one of the most absolutely multimodal disciplines that you can imagine. So I think that
*  while these open-ended text-based interfaces have done a great job at getting humans familiar with
*  this new underlying technology, I think the reason we've started there is because it's
*  maybe not necessarily the best UI for AI in general, but it's just maybe the best one for
*  large language models or this token in token out based input. Definitely more natural conversational
*  is going to be a way that the industry continues to move. But at the same time,
*  it's not going to be limited to just text. And I think that what you're going to see is things
*  where there's just the right amount of interface that's put at the right moments in a user's
*  journey to help capture more context, help ask for questions. But as an example, if you're saying,
*  hey, here's four options, which of them do you like? It doesn't make sense to have a user type
*  or say, oh, I like the third one. Maybe you should just go to click it. So I think that we need to
*  really challenge the assumption that text is the best ubiquitous interface for AI. And I think
*  that's something that I'm very excited about to see happening in the industry, but also to figure
*  out what that means for the industry. Yeah. I also really like the idea of multi-generation.
*  I feel like the future of a lot of this software is it works in the background for us every single
*  day, even if we don't visit. And what I want to do is start to send people like, hey, here's your
*  new video that we made today, or maybe even a couple, and have them be seasonally appropriate
*  and all that kind of good stuff so that maybe people don't even publish 10% of them. But the
*  option is always there and it becomes more... Somebody once told me, clients don't want software.
*  Clients want service. And I always remember that because we couldn't really do that at the time,
*  but it is starting... Everything is starting to look more service-like. So it sounds like you also
*  have been down in Canva being more of a designer that's always on in the background more proactively
*  as we go forward in time, bringing you ideas. Well, it's interesting. Actually, independent of
*  Canva, I'll touch on it for sure. My last startup was called Aesthetic, which was actually more
*  as design as a service company. So we're a tech-enabled design agency. And a lot of the
*  core idea was that the world is going to need more design over time, but there's still not
*  enough design co-founders. So what if you could actually give every company in the world
*  a designer co-founder? What would that look like? And I think, again, this was back in 2018.
*  We were very inspired by the recent advances in GAN models and things that Ian Goodfellow and
*  Labs were doing. We thought that there was a promise to actually not just automate a lot of
*  the back office work of managing a design agency, but also to start eating into the actual core
*  design work itself. And ultimately, from a business model standpoint, many design agencies, they
*  are doing a project basis. They're selling the actual work. They're not selling the time.
*  Sometimes they do, but generally they're selling the work. So I think that I very much believe in
*  this AI eating into the services industry. And I think that there's going to be a huge opportunity
*  for that across the industry. When it comes to Canva, I think, again, we fundamentally believe
*  that creativity is going to remain deeply central to our product and what we continue to offer to
*  the world. I think there's a lot of opportunities for these agentic workflows to help support more
*  production-oriented tasks. And again, in my mind, production design is the stuff that you can almost
*  imagine it in your head the moment you think of it and you just need it to get done. And I think,
*  again, we see this as a way to really help remove friction from the process versus removing humans
*  from it while still really maintaining the right human intervention points. And I think that's the
*  big difference is that I think fundamentally in this current or pre-AI era of tooling, a human had
*  to learn every new tool that they wanted to use and ultimately would have to use many of them in
*  order to get a job done. And again, this new era, the AI actually adapts to the human and the job
*  that they're trying to do and it supports them across that entire workstream. So I think, again,
*  for design in particular, there'll be a lot of work that just does happen for you in the background
*  or that just understands your content calendar and understands the holidays and can proactively
*  make suggestions for you. I think that's going to be a really, really promising or exciting future,
*  but I don't think any of that's going to come at the cost or the expense of having humans not be
*  core and central to the work worth as well. We certainly see very few videos ultimately downloaded
*  out of our product that don't have some element of human edit and edit to be for any number of
*  reasons. There is a certain irreducible taste factor. I don't know if it's funny to say this
*  because I feel like I'm young, but I'm dating myself with a Simpsons reference. But I don't
*  know if you ever remember the one where there's like a gallery unveiling. I always cite this,
*  but Mr. Burns is confronted with a piece of art and he says, I'm no art critic, but I know what I
*  hate. And I feel like that is exactly the mindset that we are kind of tapping into with our users,
*  where a lot of times they're like, that ain't it. Give me another one. And then they're like,
*  that's close to it, but there is part of it that I hate. And that's the part I'm going to drill in
*  and fix. And then they may even end up doing more than that, but it often starts with a feeling of,
*  oh, that's close, but there's something there that's bugging me. And that takes them down
*  into these like object or lower level. Exactly. And that's again, just back to that,
*  the object level. That's I think why maintaining and preserving that ability to actually get users
*  have highest durability and control over the output is super, super critical to this work output.
*  Also, we got Simpsons Co., which I do remember that episode and I'm a big Simpsons fan myself.
*  Remember some work that we did at Pinterest where there's a corpus of four billion pins.
*  And one of the biggest challenges was when there would be new content coming into the system,
*  understanding by any measure, whether it was something that was good enough to even start
*  showing to users, because historically the only way to know whether something is good is whether
*  people like it, right? Or people engage with it. So I think in what we found after spending a lot
*  of time doing research into this problem, it's actually quite easy to have machine learning
*  systems that can predict whether something is bad or low quality. It is extremely difficult to have
*  it predict whether something is very, very high quality. And it's been interesting to actually
*  try similar approaches or points of view now and call it a post-foundation model,
*  multimodal foundation model era and see how things are similar or different. But I think
*  what remains true is that you can only have an AI system predict quality to a certain level,
*  that you're always going to need human intervention, which is why I think that this world of having a,
*  call it, fully automated brand presence for a company posting across every channel,
*  I think it's a cool art concept, but I think it's very far from reality just because I think,
*  again, humans are always going to want to have control and always going to want to
*  imbue their own opinion and make sure their own taste is applied to the core outputs,
*  especially when it's something that their name is going to be attached to.
*  Yeah. And especially as we imagine a potentially more abundant future in many respects,
*  this is one of the areas where it is work in some cases, but it's also just expression. And
*  at some point, what else are we going to have to do except find new ways to express ourselves?
*  Yeah, I definitely agree with the importance of just retaining that control. It is interesting
*  to imagine how that evolves too. I mean, the cloud computer use, which is obviously the
*  latest and greatest new hotness does sort of suggest like a new era of like my AI talking to
*  your AI. Are you starting to wrap your heads around that at all? First thing I did was went
*  and just had the cloud computer use, use Waymark and just see like, could it do it? It's actually
*  pretty good at prompting other AIs I found quickly, some issues still in the fine points of the UI,
*  but do you think that if you were advising like smaller companies that maybe can't serve every
*  profile, would you be steering them towards saying, keep designing the UI and building the UI for the
*  human to drill down into the UI and exert their control? Or would you think, geez, the AIs
*  themselves are like getting much better at understanding the instructions and much better
*  at implementing the point by point changes. So maybe it could still be a sort of verbal or
*  whatever sort of interaction that still allows you to have the same level of control and feeling
*  of ownership in the end. Yeah, definitely. My intuition here is that like similar to actually
*  you mentioned before, AI is actually very good at like learning how to write prompts for other AI
*  or interacting with other AI. One of my favorite things to do is to ask an LLM to generate a prompt
*  to use in a diffusion model or asking Claude to help me write a prompt for perplexity. I love that
*  stuff and it works far better than I could have done myself. I think that trend is going to
*  continue and ultimately, practically what it means is that not every company is going to have to have
*  like API integrations with each other in order to enable connectivity between software. So I think
*  that's like the mental model that I have for this is it's really just a, it's almost like instead of
*  it being something that goes over the top of the software that's like quite literally using it,
*  which obviously is like user experience of it, it's much more similar to like the operating system
*  level experience that is just able to like manipulate and connect things together in a way
*  that it wasn't able to before. It's like the pipe command in Linux, we can take the output of one
*  thing and put it into the input of another. And I think as you're building software, I think you
*  have to basically build for that feature. And I think really practically what that means if you're
*  building an AI native experience where there's like a large language model under the hood that's
*  powering a lot of the experience, you do want to make sure that you have some means of exposing
*  that functionality to users. And I think being able to actually let a user always directly
*  interact with the AI is like kind of the escape hatch independent of whatever UI you might be
*  building otherwise, while also then building the most ergonomic experience for the masses.
*  Right. So I think that even when you're building this more opinionated user experience on top of
*  this large language model capability, you still always want to have an escape hatch, if you will.
*  I think that's true for the human user and that's especially true for the AI user. I think generally
*  speaking, the things that are most interpretable or easy to use for AI is also going to be the
*  stuff that's the easiest to interpret for humans. This stuff gets pretty hall of mirrors pretty
*  quick in some cases. Yeah, big time. Hey, we'll continue our interview in a moment after our
*  word from our sponsors. Even if you think it's a bit overhyped, AI is suddenly everywhere from
*  self-driving cars to molecular medicine to business efficiency. If it's not in your industry yet,
*  it's coming and fast. But AI needs a lot of speed and computing power. So how do you compete without
*  costs spiraling out of control? Time to upgrade to the next generation of the cloud, Oracle Cloud
*  Infrastructure, or OCI. OCI is a blazing fast and secure platform for your infrastructure, database,
*  application development, plus all your AI and machine learning workloads. OCI costs 50% less
*  for compute and 80% less for networking. So you're saving a pile of money. Thousands of businesses
*  have already upgraded to OCI, including MGM resorts, specialized bikes, and Fireworks AI.
*  Right now, Oracle is offering to cut your current cloud bill in half if you move to OCI for new U.S.
*  customers with minimum financial commitment. Offer ends $12.3124. So see if your company
*  qualifies for this special offer at oracle.com slash cognitive. That's oracle.com slash cognitive.
*  This episode of the Cognitive Revolution is sponsored by the Brave Search API.
*  You may know of Brave as an alternative to Chrome. But did you know that Brave has its
*  own independent search engine powered by its own 20 billion page index of the web?
*  The Brave Search API gives developers reliable and affordable access to programmable web search,
*  auto suggest, spell check, and more. With flexible plans for all types of use cases,
*  from rag search to automated business intelligence. On top of that, it's up to three times cheaper
*  than Bing, all without compromising on quality, speed, or reliability. Over 700 businesses,
*  including Cohere, Chegg, and Kagi, rely on the Brave Search API. And a recent survey showed that
*  94% of customers would recommend it to their peers. To start building apps with the power of the web,
*  sign up at brave.com slash API and get up to 5000 free monthly calls.
*  Going back to some of the like moment of need AI experiences that you have today,
*  we mentioned the background removal and the magic eraser are two that like,
*  I sometimes come to Canva for that just because it's really good at that. And even if I don't
*  need like any other surrounding stuff, I just, I need to do this operation. Really good models
*  for that. Do I recall correctly that there was a company that maybe was acquired also to do that
*  background removal at one point in time? This Collido, which is an incredible team based out
*  of Vienna, Austria, and is like a big part of our Gen. AI research division today. And yeah,
*  continuing to build incredible products through the Canva experience, as well as separate properties
*  as remove.bg. So what other narrow, very purpose specific AI experiences would you want to highlight?
*  Yeah. And maybe you could take that in multiple directions. It could be like,
*  there's a great utility here that people should know about. I'd also be interested in any
*  interesting anecdotes or favorite open source models that you think people are sleeping on
*  that definitely round out this whole tool set. Yeah. So I think first of all, one thing I'm
*  really excited about is that the canvas, like AI features have been used over 10 billion times.
*  Across our platform. So I think that's like just one of the things that I think gets me really
*  excited about the breadth of applications that we've defined through this embedded approach.
*  I think some of the ones that I think are really exciting again are magic switch. So being able to
*  transform doc types from one to another, which is also similar to our magic resize feature.
*  Actually Expedia has gotten a ton of use out of this and have been able to take some of their
*  workflows that would have taken eight hours before and turned into something that took 20 minutes.
*  Another example is magic edit, which I think you referred to like the actual image editing side of
*  things and being able to use a brush, kind of find, highlight part of an image, describe what
*  you'd want to have different, something that a real estate investment trust like FNRE,
*  I think like crazy time leverage from. I think that personally I mentioned magic sort,
*  which I use a lot. Our magic write personalized tone of voice is like a lifesaver for me. So
*  being able to actually give magic writes one of my own writing samples and then being able to
*  basically just do something stream of consciousness and have it then transformed into like my style
*  or into our brand style has been huge. When I'm actually then also putting presentations and slide
*  decks together, our magic layouts feature has been epic. So being able to actually just throw stuff
*  onto a page, not worrying about like how it's set up and then being able to visualize dozens of
*  different layouts that you can get that go from a purely functional item to something that has a
*  bit more of a form thought out as well. I think those are some of the ones that I've gotten a
*  lot of personal value out of and like some of my daily drivers, as well as ones I think we've seen
*  a lot of benefit from, especially some of our larger enterprise customers. To drill in a little
*  bit on the writing use case, this has been one of my own like personal white whale projects for
*  some time. I guess I have found on a specific task, like for example, I always write an intro
*  essay for the podcast. My workflow now is I have a standard PDF doc that has 30 intro essays from
*  past episodes. I'll put that into Claude and transcript of the current episode and say a
*  pretty standard prompt using the style, tone, voice and perspective of the essays, write a new
*  one. And then I can also give it a little bit of incremental runtime instructions if there's
*  something I want to emphasize in a particular case, which often enough there is. And then it
*  does a pretty remarkable job coming out. One thing that is notable about that though is I'm
*  usually giving it like 50,000 tokens of context. And it really does seem to need, at least to
*  satisfy me, it does seem to need a lot of those prior essay examples. If I just say in adjectives,
*  here's how I want to sound, or if I just give it one, it doesn't seem to nail it as much.
*  So do you guys do something similar with that feature? Like are you guiding users
*  toward assembling tens of thousands of tokens of context to customize the writing somehow?
*  So it's interesting to figure out where that efficient frontier is of like the number
*  of token priors to help get the right tone of voice. We've done some evaluation across that
*  curve. I think what's really interesting is it's very brand, very person specific. I think if
*  harder, we haven't quite been able to give very prescriptive guidance on how much to get Nathan's
*  voice right, or maybe how much to get John's voice as an example. But I think more is generally
*  better. So I think that what we have seen is we can let users put quite a bit of text. I'm not
*  sure whether we would support the 50,000 tokens at this point, but like definitely thousands of
*  tokens is like what I personally would do when I'm using this within Canva. Similar to you, I've
*  also compared it to the Clawed Project approach of having prior posts and giving a stream of
*  consciousness. And my own qualitative evaluation is that it does actually work extremely well.
*  I think that's just part of a testament to I think a lot of the fine tuning and the tweaking
*  at the prompts level to really get this right, as well as a lot of user experience that we're
*  building on top to help guide users in the right direction. And I think that's the key thing here
*  too is again, this is a perfect example of a concept level editing where we're basically
*  helping a user edit at a concept of their tone, while then giving them full control of the object,
*  which is actually the words or the tokens themselves. I think this is an active area
*  where we're working to continue to invest more and continue to push more. But I think that what
*  we've seen through our own use and through feedback from customers is the current approach is actually
*  getting pretty exciting results. I don't know if you can share what models underlie those
*  writing features today. For me, Claude has been the best. Obviously, that's something that you
*  would have to use as a customer as opposed to be able to run your own version on your own
*  infrastructure, which at canvas scale, I imagine has some appeal. I normally advise developers
*  not to rush into that unless they're really at serious scale, which you are. So how do you think
*  about using the latest and greatest frontier model versus fine tuning a llama model or whatever
*  you can actually bring in and make truly your own? Yeah. So we've kind of maintained a three-prong
*  approach here between building a lot of our own models, which we're going to be doing since 2017
*  across a wide variety of domain problems. So I think we actually have over 100 models that
*  are being used in production today, but partnering with the best of breed of what's out there and
*  partnering with all of the research labs and getting access to everything that they're working
*  on and figuring out the different ways of integrating that to leverage within our product,
*  as well as working through an ecosystem of app development partners to bring their capabilities
*  and apps natively into Canva for our end users to experience. So again, we kind of work across
*  those three of building partnering and our ecosystem. I think it's what we've seen,
*  especially in the large language model realm, there's so much innovation and so much advancement
*  here that being able to just try lots of different approaches and try lots of different things
*  is yielded a lot of really positive results. And I think something that we're going to continue to
*  try various versions of what's out there and to like, and weight them against each other.
*  Have you, this might be something you can't disclose even if you have, but I am waiting for
*  the GPT-4O image editing capability with a lot of anticipation. I feel like that has sort of almost
*  been memory hold at this point, but they did show us a bit a number of months ago about how
*  it seemed like it was like instruct picks to picks, but like, you know, two generations forward,
*  it seemed. So I guess if there's anything you can tell us about any exposure you've had to that,
*  I'd be fascinated to know about it. And then more generally, again, it's like, how do you think
*  about in a particular situation like that where I see that there's something out there that's got to
*  be coming before too long, but I'm not sure when I would really be able to deploy it. How do I invest
*  in that knowing that probably no matter what I invested, I'm going to have a hard time match
*  that capability. Yeah, totally. I think that's part of what makes it so fun to be building in
*  this space. I think that speaking like more generally here, again, like the big advancement
*  called the like GPT, you know, moment for a lot of these diffusion models, in my opinion, was the
*  release of these multimodal diffusion transformers, which again really helps basically maintain like a
*  single transformer model that can use a text encoder, which could be a GPT level equivalent
*  or could literally be, you know, one of the opening eye class models or llama or whatever it needs to
*  be, as well as these encoder models with this like cross attention field actually like understand the
*  adherence and the alignment between the text and the specific semantics of the image in a way that
*  was just not really possible before. And I think that's what's really enabling all this new generation
*  of image infills, image expansions, image generation, and all the like. I think this has been an area
*  where there's been like tremendous amount of progress. I'd say as much progress as we've seen
*  in the text generation era, we're seeing that very much in the image generation era as well.
*  This is an area where I continue to tinker, continue to explore, but also really excited to have
*  the incredible Leonardo team who's like really just going absolutely super, super deep into this
*  space as well and being able to actually like train and launch their own state-of-the-art models in
*  this space as well. So I think we're kind of, we benefit as Canva of both seeing and understanding
*  what's happening across the industry, but also being, you know, very deeply invested in being
*  our own model developers in this space as well. Yeah. All of the above definitely makes sense,
*  I suppose, at the Canva scale. How do you think about evaluation and deciding what is good enough
*  to launch? We talked a little bit about the challenge of taste. I won't bore you with my
*  full history of trying to use aesthetic evaluation models, but suffice it to say,
*  it's like way harder, it seems, to get to any sort of ground truth or any sort of agreement on
*  matters of taste than it is on, you know, classification tasks or whatever. So big time.
*  Are you guys, I assume you have to be running on more than vibes with 200 million users. So
*  what sits between vibes and objective ground truth when there is no objective ground truth?
*  Yeah, no, this is the heart of the question. I'd say for any people building in the AI space,
*  starting with the evaluation is so critical. I know in traditional software engineering,
*  we've talked about test-driven development. I think that in the world of AI, a lot of folks
*  start with like vibe-driven development, but you've really got to get to this kind of like eval-based
*  approach as fast as you possibly can. This is something that basically for the last two years,
*  we've gone extremely deep into. I think especially because there are a lot of these LMSys type
*  arenas for chatbots that exist for like the larger English model space. It doesn't exist
*  for the domain of designs. So I think we've had to go to the end of the earth here to become really
*  the best in the world at this. So I think in particular, what this comes down to is being
*  able to have very rigorous customer evaluation guidelines that ultimately describe the human
*  taste aspect of what is good. Combined with a trained set of professional designers and evaluators,
*  we're able to actually imbue that judgment onto a larger scale, large enough to actually have
*  statistical significance. You can also imagine we're not working across like a single
*  document or design type, but working across many different types. So you have to have a lot of
*  category-specific examples or references, what makes a good slide deck versus social media posts,
*  website versus whiteboard. And ultimately then you have to be able to have a way to actually have
*  multiple different generators or multiple versions of generators, ultimately compete with each other
*  and be able to actually be evaluated against each other in a highly comparative way. Then come up
*  with scores across all the different dimensions that you might care about. So certainly things
*  like visual quality or prompt appearance, you can imagine there's five or 10 different dimensions
*  that you might care about that some are similar, but some are different across the wide range
*  designs as well. So I think that being able to actually have this kind of golden set of prompts
*  that we can then evaluate for each different category of design we care about, for every
*  different potential generator that we want to evaluate, be able to then actually have this
*  comparative scoring across these different dimensions. There's a lot of investment and
*  math that has to go into getting that to be really good. All that is in service of actually
*  helping avoid homogeneity in the design process and helping give end users what feels like a very
*  high amount of control or steerability over the models that they're actually using. So again,
*  eval is something very near and dear to my heart and something that we think a lot about within
*  Canvas for sure. If I was going to imagine a sort of graduated approach to ultimately launching a
*  feature and having the benefit of Canvas scale, I might think, okay, let's take background removal.
*  For example, we've got the current background removal model and we've got a new background
*  removal model and developers say it's better. I could imagine using other models to do
*  evaluation and maybe that could be as simple as send 100 of them to GPT-4.0 and Claude and have it
*  compare. I personally don't trust that stuff that much yet for most things, but it could be like an
*  initial smoke test or at least has to not look a lot worse according to those standards to then move
*  on. Then I guess it sounds like there's sort of a group of trusted people who you're like, bounce it
*  off of them and get a score and see if it is better. And then I would admit even imagine doing
*  some, hey, user live in the product, here's two background removals that you pick the one that
*  you want and really kind of doing post-launch monitoring that way. Is that kind of the
*  structure and what I have read wrong about that and where do you get the reach value?
*  Yeah, it's a great mental model for it. I think what I described was a lot of the call it like
*  offline evaluation side of the house in particular for design generation tasks. I think there's
*  definitely a lot of online eval, which is ultimately more of looking at user engagement,
*  X versus like thing A or thing B and understanding it there. I think that generally when launching
*  any type of new machine learning product, whether it's an incremental version of a new model or a
*  new model in general, a lot of what you need to do is again, first by defining what success looks
*  like. So in the case of background generation, the nuance has to do with how tightly is the
*  foreground image cropped. So you can imagine if we were coming up with an evaluation rubric,
*  we're talking about, is the right item picked out? Yes or no. And for that right item,
*  was the cropping good? Yes or no. And if it was good, was it overcropped, undercropped?
*  Just as an example, you can imagine those three criteria and then being able to actually then
*  pre-generate the examples. So you have to show those to enough evaluators who are trained on
*  that rubric to get a ground truth to come up with a point of view. Is this good or is this bad?
*  That's generally the way that these things kind of roll out or would work. I think that what I
*  think is exciting though, is as you do these types of evaluations at enough of a scale,
*  you can actually start to build some kind of custom machine learning models that are actually
*  kind of focused on actually being aligned to the human judgment. The hard part here is that if you
*  show the same example to three different human evaluators for this background generation task,
*  you might get three different answers or they might not fully agree with each other from an
*  iterator alignment standpoint. So I think generally that causes a lot of challenge for training these
*  models. But generally speaking, it's possible to get something that has 70, 80, maybe even 85 or 90%
*  prediction quality when you're comparing what a model can do compared to what a human evaluator
*  can do. But again, that's only really possible when you have a more narrowly scoped domain task.
*  It's much more difficult for something very open-ended or that's very style dependent.
*  I'd say for us at Canva, we focus a lot on getting really great offline evaluation in place. And we
*  also then do a lot of offline evaluation where we'll have a new version of a design generation
*  model. We'll push it into production where we'll interleave the results and compare those to other
*  versions of the model. Ultimately, you see what the uplift is from one model versus another.
*  Very similar to what you would do for recommendation engines or for search engines,
*  figuring out how to actually do that for generation models has been a pretty exciting task as well.
*  Have you experimented with fine-tuning the GPT-4O models that now support image in the fine-tuning?
*  I wonder to what degree you may have a stable of highly bespoke evaluation models that might
*  soon give way to GPT-4O fine-tune evaluation models. Yeah, definitely. So we have definitely
*  tried a lot of fine-tuning of this multimodal class of models and there's a huge amount of
*  potential benefit. In fact, a lot of those training tasks that I talked about, some of them still
*  would have to maybe train your own model for, but a lot of them you actually are just doing a fine-tune
*  on an existing foundation model. And that's one of those things that still blows my mind
*  compared to how much more leverage we have now as an industry compared to back when I was at
*  Pinterest and we had to do all this stuff from scratch. But I think that definitely fine-tuning
*  models is a more promising place to start than having to go train your own model from scratch,
*  especially for things that are in the domain of texture image generation or more generally where
*  the semantic understanding is really important or where understanding a broader context for what's
*  being evaluated is important. So again, a thousand, five thousand examples of background generation or
*  social media posts to get some kind of output or evaluation out. The fact that these models have
*  seen millions, tens of millions, billions of examples of these things as a lot of priors that
*  really dramatically improve the results compared to what you would get otherwise.
*  Soterios Johnson Do you have rules of thumb for fine-tuning foundation models in terms of
*  how much data? Because I find this always surprises people in terms of, especially if they've been
*  schooled in thinking about big data. Now it's like, I typically advise people to start with
*  ten examples just because that's achievable and doesn't feel too intimidating. How do you think
*  about how many examples is worth starting with and how you kind of escalate through orders of
*  magnitude of examples? James Johnson
*  Yeah, I think that definitely it depends a lot on the type of model you're working with. So in
*  diffusion models, if you're trying to do like a Laura on a diffusion model to consistently
*  create a specific style, you can often do that with tens of examples. I think that if you're
*  doing something for writing or for kind of understanding brand tone, it does take, I think,
*  more examples than that. I don't know the exact frontier, but I think the general intuition
*  or the risk that I've seen in fine-tuning of large language models is that it's very
*  easy to overfit them if you don't give enough examples. So I'd say that for like diffusion
*  models, I think it's very clearly you can do it for a lot less examples. I think that shows a lot
*  of promise for what you can do in the general media generation space. For the text generation
*  world, I do think it takes quite a bit longer, but also I would generally challenge a lot of
*  the reasoning behind why fine-tuning these larger models is required, especially when you have such
*  long context windows. Most of the time, what I would advise is that before even trying to do
*  anything on fine-tuning a language model, just try getting a ton of context. If you have like a
*  million-token window or you can add 30 or 50,000 tokens of your prior writing examples in your
*  workflow, that's nine out of 10 times going to yield a better result than having to
*  try and do a broader fine-tuning task. Yeah, I think that's an apt point that overfitting can
*  work for or against you. If you have a very specific task that you want to dial in performance
*  on, then it's like really, yeah, exactly. If you want to maintain the generality that you're used
*  to with a chatbot, but give it a different vibe somehow, then I think that's like stuffing
*  definitely is the way to go. It works really well for things. If you are trying to do a classification
*  task, that's a great use of fine-tuning. But if you're trying to capture the vibe of something,
*  again, like style, I think that's generally not a very good use case for it. Interesting.
*  How do you guys think about cost and latency in your designs? Obviously, especially if you're
*  working with an API and paying my token, especially with 300 billion users, you could run up a real
*  bill. At the same time, I often think people are, especially when they're getting started,
*  I think they think about the cost way too soon. Do you have a framework or guidelines for your team?
*  Yeah. I think generally our development flow is just like make it work, make it good,
*  make it fast, and then make it cheap. Generally, we'll talk about launch milestones around
*  after we make it good, maybe sometimes after we start making it fast, depending on what the use
*  case is. For us, we're definitely quite cost aware, but it's certainly not the primary driver.
*  I think if you just zoom out and look at what's happening with just
*  like Moore's law in terms of like compute availability, but also just like the cost
*  curves of both inference time compute for all these models. I think in the last year, we've seen
*  a 95% cost reduction or something in that order of magnitude, but I don't think we need to over
*  rotate on costs when you're getting started, especially. That's what I would advise for folks
*  as well. Just focus on really nailing the user experience. Yeah, I'm with that for sure. That
*  might be a t-shirt. Can I design a t-shirt on Canva? Say, yeah, let's get you out. We'll do
*  that in Canva and we can get it printed and delivered. Make it work, make it good, make it
*  fast, make it cheap. Could be a mantra. Let me see. What else did I have here? It sounds like
*  fine tuning is not like per account fine tuning. That was a question I wanted to ask. It sounds
*  like that's not going to be a huge focus maybe on the image generation side for styling, but
*  not in the big picture thing of these high order functions of creating stuff so much.
*  Yeah, I think that's the mental model that we have today. I think that again, these things are also
*  changing so quickly. I think we're staying close to this, but I think the use cases that probably
*  make the most sense are capturing aesthetic style. That's ones that I've tested and are looking into,
*  but generally speaking, per account fine tuning isn't a big part of our strategy today.
*  Okay, cool. How about in hiring AI engineers? That's probably our most common listener profile
*  type, although data is muddy. I think Ellicit has had a really good explication of their philosophy,
*  but they're doing a very different thing obviously. I don't know if you know Ellicit's product,
*  but it's essentially AI assisted literature review for biomedical context and things like that.
*  It's a very different corner of the economy. I wonder how your most important traits,
*  best practices for AI engineering might compare to theirs.
*  Yeah, absolutely. I think for the Canva, our number one, number two, and number three priority
*  when it comes to gen AI in general is being the best in the world at design AI. We are extremely
*  motivated and dedicated to being the world leaders in design AI technology. I think first
*  and foremost, people who are deeply passionate about that mission is the number one thing that
*  we look at for folks who are coming in the door. It doesn't necessarily mean that you have to be a
*  designer by background, but you have to actually be excited about the interplay between humans and AI
*  in the domain of creative work. I think generally speaking, people who are extremely curious and a
*  very strong growth mindset and are just willing to be in touch with this world that is changing
*  and evolving every single day, but also are excited to actually live in and use the Canva
*  product every day, which is a huge part of our culture and something that was one of my favorite
*  things we get to do is literally use the thing that we're building every single day. I think that
*  generally folks who are also very practical with their problem solving abilities and are actually
*  excited to wear multiple hats and actually thinking about and solving problems at a huge
*  scale. I think that generally this is a non-purist approach where it's people who are excited to
*  actually ship a new model to test and try within the product and actually understand what the jagged
*  edges of it are before they think that it might not be perfect by some offline evaluation metric.
*  I think it's generally this multi-disciplinary approach that I've seen work extremely well,
*  and I think that it's really differentiated the AI engineering culture that we've been able to
*  build at Canva. Are there any best practices in terms of engineering approaches or pattern of
*  problem solving or just habits of mind that you would impart on people? I think there's a certain
*  grit and determination that I've seen, which I think really how that plays out is an unwillingness
*  to be blocked or an unwillingness to not persevere through the problem. I've seen this play
*  out in a few different ways. It's being able to proactively ask for support or help when you need
*  it. Maybe you need some support from a different team or from somebody on the business development
*  side. Being able to proactively raise your hand when you need support and not just waiting or
*  expecting somebody else to come to you. I think that's extremely important as well as just, again,
*  that grit to be willing to just grind through these really complicated problems. In many cases,
*  there literally is no industry precedent for what we're trying to build. So being able to actually
*  be deeply first principled in how you go about that and actually come out of problem from a deeply
*  user and domain-centric point of view. I think those are things that are extremely important for
*  all people who are entering this field and certainly those who would be excited to work at Canva.
*  Cool. I like that. Let me try a couple of mine out on your end. You can either
*  riff on them or reject them or whatever you think. One that I use is do the hard part first or
*  sometimes I rephrase that as work from the AI out. Meaning, I think to contrast this
*  kind of product development with traditional software development,
*  we don't really always know what's going to work. So it's like, we can't design everything end to
*  end and say, okay, we've got all this planned out. This is the plan. Now we execute the plan.
*  There's got to be a more dynamic interplay between the planning and the actual making the key part
*  of it, which is typically an AI model confirming that works. So I always try to say, start with a
*  prototype or sometimes I've done collab notebooks. A lot of times it's in a repl, but get that.
*  Core thing to work first. We'll figure out the plumbing later.
*  Can we get down to inputs and outputs actually working? So your thoughts.
*  I vehemently agree. I think that you can either think about this as either the walking skeleton
*  of the system. So it's just like, what's the bare bones version of the thing going from end to end?
*  And oftentimes that critical thing is taking that jagged edge of the software and smoothing it out.
*  So being able to actually figure out what is that core most unknown piece of the puzzle and just
*  being relentless about focusing on that first. I think that's a really, really good call out.
*  Another one for your thoughts. Sometimes I call this situational awareness, although that's
*  such an overloaded term in AI discourse. But the sort of mistake that I sometimes see people making
*  is rabbit holeing on a particular solution and being like, just not changing the frame or zooming
*  out and being like, this doesn't seem to be working. Could I just try a totally different
*  approach and trying to incrementally grind? This is the flip side to the tenacity thing,
*  because I think tenacity is important. But then I also think sometimes you need to have that
*  awareness to say, okay, I've been able to grind from 79 to 82% here or whatever. And that may not
*  even be a real measurement. But I feel like I'm topping out below where I want to be.
*  Can I reconceive this problem or try a totally different strategy?
*  Intangible for me, but I don't know if you can make that any more tangible guidelines in place
*  or whatever. I think it's to me, I think about that really as the problem orientation versus the
*  solution orientation. Because I think oftentimes, like this guy, Dave Herndon, who was the former
*  CTO and now distinguished engineer at Canva, he had this saying that I love, which is we've had
*  the idea for hoverboards for 50 years, right? But no one's ridden a hoverboard yet. So I think
*  oftentimes the outcome is so clear that we can see it. You can often prototype it or you can
*  golden path the solution. But being able to actually deliver on that is extremely,
*  extremely difficult. And I think this is oriented to the problem orientation, which
*  the goal was to build a hoverboard. There might be one promising solution in order to get there
*  that gets you from 72 to 81% or whatever it may be. But if you're topping out at 81, and we know
*  you need to get to 98, it probably means that you need to maintain the problem focus but switch the
*  solution. So I think that orienting around the problem is really key and also is difficult,
*  right? Because it might mean that you have to just fundamentally change your approach or pivot on a
*  dime. And that's hard to do. It's hard to be both deeply passionate about what you're doing,
*  but also be willing to take a sidestep sometimes. Yeah. I like your framing better than mine,
*  actually. I think it's quite a bit clearer. So watch out for that to come in a few of some.
*  Sounds like your true presence, Austin. A lot of t-shirts here.
*  Yeah. Let's maintain problem orientation, be willing to let go of solution orientation. I
*  like that a lot. What other products do you look at in the space for inspiration?
*  Who is on the edge of in your minds that you just want to see what they're doing on a regular basis?
*  Yeah, totally. So that's one of the coolest things about building in this space is just
*  seeing how much incredible innovation and how many extremely smart and motivated teams there are
*  working across all angles. I think within the creativity space, some of the ones I love using
*  very inspired by. So I think like Korea AI is doing a really awesome job and I think building
*  some really interesting things in terms of the blending, the concept and object level manipulation.
*  I've also like, I studied architecture in college. So actually I'm very keen to a lot of what's
*  happening in the 3D world. So a lot of things are meshy and swine. I think what they're doing
*  is just super fascinating and kind of the call it text to 3D model world. I think on that architecture
*  path. So space maker and art design are two really, really interesting ones that when I
*  play with them or dust off my old skills from using Rhino and AutoCAD way too much, and I see
*  what this new generation of tools is capable of doing, it just completely blows my mind and
*  really inspires me to think about continuing to distill down and refine these extremely deep and
*  complicated workflows using AI to actually both again, automate and augment. And also just my
*  personal daily drivers, I would say is, I use perplexity cloud, chat GPT, Otter, like every
*  single day. So I'm always very inspired by a lot of the work that's being pushed there and
*  really thinking about the general large language model approaches and how you build these kind of
*  paved roads and most generic possible functionality on top of these models, as well as in how you
*  integrate those into either the world's knowledge or interior and personal knowledge repositories.
*  The 3D call that is really interesting. How good are those things getting these days? I haven't
*  used any like architecture generator. It's getting there. I think that what's really
*  fascinating. So like the thing I actually first fell in love with generative design back in 2008.
*  So like when I was in architecture school, like Tom Reese, like the, you know, creator of V3JS,
*  Processing JS, excuse me, like kind of gave a lecture that was showing how you could write
*  an algorithm to generate some like output image. And this is the key thing. It was the main
*  dealt thing was they were introducing randomness into the process. So I think that one of the,
*  and that kind of led to this whole world of like parametric design. So there's going to actually
*  a lot of parametric design tools, which is not using AI, but it's just more or less like putting
*  doves and knobs and dials around how many rooms are in the house, how many square feet is each
*  other room and then like change the dog and you can look at different variations. That stuff's
*  been around for quite a while, but seeing now how that is integrating with AI is wild because
*  ultimately there's new levels of abstraction on the interface. Again, now concept level interactions,
*  you can say create a room with three houses that's 2000 square feet and on this site plan
*  and actually come up with like some pretty interesting renderings of it, or even like the
*  actual 3D model or the BIM, the building information model on top of it. That's like very,
*  very exciting to see. I think there's also new capabilities of being able to actually
*  simulate the lived experience in these different houses. So being able to, or buildings in general,
*  being able to take an office building and simulate the weather or the temperature inside based on
*  where the sun is relative to the GPS coordinates and then using that to then optimize the location
*  of windows or being able to take the number of the seating plan on the office floor and based on
*  the predicted paths to the bathrooms or the cafeterias understand where you might need to
*  put other programming around it. I think that ultimately what I see the most here is this true
*  augmentation realm where you're really helping the architect have a 10x, 100x leverage on their work
*  product as well as then some of the automation around the rote tasks that would be required to
*  go from a concept or an idea of a building into having that thing that you can actually
*  physically step into in the real world. So again, super exciting stuff. Again, I think this world is
*  very early on, which is part of why I'm very keen to keep my eyes on it. I think again,
*  there's no map of every building in the world on the internet, which means it's not inside of these
*  frontier models today. So kind of seeing how the companies are going about developing that is really,
*  really inspiring. That is fascinating. Architecture is a really interesting one too, because
*  it does strike me as one of the verticals where, or like say one of the professions where
*  the sort of, well, we'll always just want more and more and more might not actually be true.
*  Whereas with graphic design, it's quite ephemeral. We could always produce more. The streams are
*  flowing fast and they can continue to flow faster and probably will. When we think about designing
*  homes or designing buildings, it's like the bottleneck is still going to be building them
*  in the real world and the bulk of the cost is going to be there. And it's probably not the case
*  that if architects get 10x more efficient or 100x more efficient, that we're going to build 10 or
*  100x more buildings. So one does start to wonder then like, what does the future of architecture
*  look like? And especially if some of these software platforms get easy enough to use that
*  prospective homeowner can do a decent chunk of that at the concept level.
*  Should architects be worried about the future of their profession?
*  I don't think so, especially because in order to actually have something be built in the real world,
*  it has to be signed off by an accredited architect. So somebody who's legally liable for
*  the quality of what was put into the world. But actually one of the things I think is the most
*  interesting about architecture profession, so much of the time, especially for these massive projects,
*  so much of the time that is being spent is actually on the work to win the bid in the first place.
*  You're actually spending, you're pretty much doing a lot of the work before the client actually
*  chooses to work with you. And that's true for these large commercial projects. It's often even
*  true for a lot of these like residential projects. So I think that the opportunity is to actually help
*  first order to help actually visualize the permutation space or actually take the
*  client's idea of what they want and help visualize permutations with like the architects and ones on
*  it before to actually help them win the deal. So I think that's actually where this will first kind
*  of eat into the creative work itself, which again is fundamentally an augmentation task.
*  I think independent of that, there's going to be a lot of automation that takes place in turning the
*  fully produced pad and building information model and then using that to create all of the permit
*  paperwork, all of the specialized construction plans for the electrical or the plumbing,
*  all that kind of stuff. So all the like discrete programming based on the building information
*  model, I think there's a lot of automation opportunity there. But no, I think the role of
*  the creative director, the architect, to some degree just gets heightened or gets even more
*  elevated with all these kind of new tools at their disposal. Yeah, several fascinating
*  things to ponder there. The role of the of like insurance and liability as potentially
*  determinative is interesting. I do still wonder if like somebody couldn't, like a software company
*  couldn't take that on at some point, like get confident enough in the models and say, hey,
*  we'll insure this or self insured even perhaps. One of the places where this is happening first
*  is for call it like semi prefab housing, where you either have, you basically have like a design
*  system for a house, you have call it like the frames or the flooring or all the kind of like
*  individual after the roofing, like these kind of core pieces of the design system prebuilt.
*  And then ultimately, the design process is figuring out the right combination of those things
*  to put together. So this is kind of where you're vertically integrating across the architecture
*  and the construction, which keep in mind today are generally two completely separate industries.
*  But when you actually can vertically integrate across the architecture and the construction,
*  that's where I think there was going to be like the opportunity for these more
*  AI enabled products. Actually, this was this idea was actually the place where my last company
*  aesthetic originally the concept started as like an architecture, like vertically integrated
*  architecture firm, but then moved into the graphic design space. And we kind of saw where a lot of
*  the technology was. So I'm very passionate about this space. And there's actually been some
*  interesting case studies that there was a company called Katara, which kind of tried to do this and
*  ultimately didn't end up working. But there's a lot to learn from that. The lesson to learn,
*  I don't think is that it's a bad idea. I think it's more about execution and AI enablement.
*  But I do hope to see some of these kind of more vertically integrated players here as well. I
*  think just in general, the application layer of JMI, I think is like really, really, really exciting.
*  I think it's going to be where the lion's share of economic returns come from in the next five,
*  10 years. Anything we can do to bring down the cost of housing, it would certainly be
*  most welcome. Last section, and I really appreciate how generous you've been with your time and
*  insights. You recently wrote a blog post called the Gen. AI Application Layer, which is about
*  kind of why you're bullish on the application layer and a little bit about what you're looking
*  for as an investor in the application layer. I won't spoil it. I want to give us just kind of
*  your case for and your priorities when you're thinking about application layer investments.
*  Yeah, absolutely. So I think what we've seen is this like platform shift, this pattern
*  for any of the major platform shifts that have happened here from on-prem to cloud,
*  desktop to mobile, now called pre to post AI. Where things always tend to start and aggregating
*  value at the infrastructure level, moving into then the platform level, then moving into the
*  application level. So I think that has played out and there's pretty clear data on this,
*  especially looking at the on-prem to cloud level, where again, the first big companies happened at
*  like the infrastructure level. So a lot of the chips and the data centers and things like this
*  moved into a lot of the platforms. So again, this hyperscalers and then enabled all the application
*  layer. So literally pretty much any internet enabled company. I believe that we're currently
*  in the infrastructure era for AI. If you really think about it, I think how this plays out,
*  today like the global GDP is something around 110 ish trillion dollars. I think they expected
*  to grow to like 130 trillion dollars by like 2030, give or take. And then today the tech sector is
*  call it about five trillion of that. And if you can imagine being able to even just grow that
*  percentage of how much tech can eat into the rest of that, which generally is like services
*  industries and things like this, which even if that grows by like 3%, right? Like that's a
*  multi-trillion dollar opportunity that I think happens at the application layer eating into
*  a lot of these things that used to be more traditionally thought of as services. So I think
*  this blog post from Sequoia about the $600 billion gap or problem for AI. When I think about the
*  shift in labor and how it's going to be augmented and automated in some cases with AI, I think it
*  just makes it very clear that the application level is extremely underserved compared to this
*  opportunity. So you have three apps called out by name in the blog post. There's GitHub Copilot,
*  Jasper and Harvey. I think listeners will probably know each of those by name.
*  It strikes me that like those are not necessarily, I wouldn't be equally confident in their eventual
*  or like long-term success. Jasper in some ways has become the poster child for like being the thin
*  rapper that was like very good on identifying a customer need, very good at being quick to market.
*  But I don't know exactly what the latest news out of Jasper has now been confronting the fact that
*  they didn't necessarily have like their own platform that they were building on. Whereas
*  obviously with a Canva, you've got 10 years of like design software that OpenAI is not going to
*  recreate in their Canvas thing in the immediate future. In contrast to that, Harvey is like
*  solving a really hard problem. But then you could still wonder, well, I don't know, what's GPT-5
*  going to do? Anyway, with that sort of background in mind, what leading indicators are you looking
*  for in terms of how people pick problems to solve or possibly like how they think about
*  structuring their business? I'm very intrigued, for example, by aligning your revenue to a more
*  like service-based thing. If we can solve a ticket, that's a dollar or things like that.
*  But yeah, what are your kind of heuristics for what inspires you for applications?
*  I think the first and I think most important thing is like deep customer centricity. Because
*  I think that being able to really attach onto like a specific persona and a specific like
*  a specific person, you can see the light of their eyes and you can literally feel the pain that they
*  have. That's like the most important first thing. Because I think, especially when we're talking
*  about this, like fast evolving platform layer that is increasingly building its own thin,
*  highly generalized application layer on top, it's more important than ever to be highly
*  epiminated and vertically focused about what you're building. So I think that's the first
*  piece is deep customer orientation. I think the second piece personally, I think that
*  the further a field from call it the existing tech has eaten the world. So things that are maybe
*  going into industries that have not historically had as much tech penetrations like the mining
*  industry or the real estate and the construction industries like we've spoken about, you know,
*  I think those are places where I think there's a lot of immediate leverage to be had with that
*  customer orientation and focus. I think that then the third piece is being able to really build
*  really intuitive user experiences and products that are actually like deeply aware of the jagged edge
*  of what the software is able to do today. Because I think that if you're going a little bit further
*  afield from the straight and narrow use cases, you'll probably get a meaningful amount of value
*  from using AI for that problem, but it's not going to be 100% solved for that for it. So being able
*  to actually tailor a user experience around and those kind of shortfalls of the model and
*  could actually account for those is extremely, extremely important. So when I'm talking to
*  promising startups or advising founders, I really want to see those three things in order to feel
*  like they're really set up for success in the next decade as things continue to evolve.
*  Cool. That's great. That could be a good note to end on. I think that's all my questions.
*  Anything else on your mind that you want to share? Any last drops of wisdom for the audience?
*  No, this has been awesome, Nick. And I really appreciate your time and the thoughtful questions
*  have been really fun. Cool. Likewise. I've had a great time. John Militovich, head of Gen. AI
*  product at Canva. Thank you for being part of the cognitive revolution.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the
*  show. So please don't hesitate to reach out via email at tcr at turpentine.co or you can
*  DM me on the social media platform of your choice.
