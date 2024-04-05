---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 6259s
Video Keywords: []
Video Views: 2342
Video Rating: None
---

# In Search of Truth w/ Aravind Srinivas of Perplexity AI
**Cognitive Revolution "How AI Changes Everything":** [March 14, 2023](https://www.youtube.com/watch?v=YSYQZZu4MEM)
*  We need to build AGI so that humans can just go back to living, right?
*  Just live a nice life.
*  Not everybody needs to work so hard.
*  A lot of people don't appreciate what's going to happen to them.
*  You don't have to do a ton of work.
*  It'll almost be like you get to live the life of a millionaire or a billionaire.
*  You right now are already living a higher quality life than the president of the United States like 50 years ago.
*  You just have access to technology that they could only dream about.
*  So technology is the biggest leveler to making humanity equitable.
*  A lot of people don't get it.
*  And if intelligence is in abundance, like you no longer have to compete to be the highest IQ person in your class or something like that.
*  You can do stuff that's interesting and creative to you and learn from the AI.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers, entrepreneurs and builders
*  working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture of how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Thornburg.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work, customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it, and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  Arvind Srinivas is the founder and CEO of Perplexity AI, an AI enabled search engine, which he aims to build into the world's most trusted information service.
*  To give you a sense of the new possibilities and potential for change that AI is creating, consider Google's total dominance of the search market for more than 10 years.
*  Google earned $282 billion in revenue in 2022, a number that is still growing at 10% per year, and nearly $60 billion of that was profit.
*  That's more than $1 billion in profit per week.
*  But despite this incredible scale, profitability and continued market growth, even the most well-resourced and determined competitor, Microsoft, has barely chipped away at their position.
*  And Google has maintained close to 90% market share.
*  Yet into this market enters Arvind and Perplexity.
*  With a $15 million venture capital round and just 10 or so employees, Perplexity has built a genuinely novel search experience, which has meaningful advantages over Google.
*  And despite the fact that Perplexity does not have the same privileged access to the latest OpenAI models as Bing, continues to hold its own in terms of overall usefulness.
*  We talked to Arvind after the new Bing launch, but before OpenAI dropped prices 90%, about how he thinks about competing with the tech giants,
*  Perplexity's product philosophy and obsession with maximizing value delivered to the user per unit time, the features that make Perplexity unique,
*  how he thinks about managing language model costs, managing user identity, collecting user feedback, ensuring user safety, and how Perplexity might eventually monetize.
*  We also covered his expectations regarding AGI, why he thinks AI will drive both wealth inequality and greater equality of access and opportunity,
*  the risks of misaligned AI, and the trust that he has in Sam Altman and OpenAI leadership.
*  I came into this conversation already impressed with Perplexity, the product, and came away just as impressed with Arvind, the entrepreneur and thinker.
*  I hope you enjoy this interview as much as I did.
*  Arvind Srinivas, welcome to the Cognitive Revolution.
*  Thank you for having me here.
*  Yeah, really excited for this conversation.
*  As anyone who follows me on Twitter knows, I am a big fan of what you're building at Perplexity and have been raving about it online and what an awesome search experience it is.
*  You've articulated the mission for Perplexity as becoming the world's most trusted information service.
*  I'd love to just start off by asking you, what does that mean to you?
*  What does that mean to you in two years?
*  What does that mean to you at the end of the decade?
*  What is Perplexity going to be like as we go into the future?
*  Yeah, I mean, these are great questions and I think about these every single day.
*  To start off with, our core founding team has a lot of academic background.
*  And the first thing you're taught when you're writing your first ever research paper is don't ever say anything in the paper that you cannot actually cite.
*  You should be able to reference whatever you say.
*  The reference should either come from some other research paper or it should come from an experimental result in your own paper.
*  Anything else that you say is an opinion and it's not a fact.
*  And that was very powerful.
*  It's still stuck with me even now.
*  And that's sort of why we were the first to put out a citation powered search.
*  Right after Chad's GPT came out, I think literally a week or week and a half after it came out, we put out the first version of Perplexity Ask,
*  which literally just combines Google and GPT 3.5 together and takes the top few search results and treats them as links that it can cite.
*  And then gives you like this really cool, very short three sentence summary of what the answers should be.
*  But only tries to say stuff that's already been presented in these links.
*  Of course, there are some hallucinations that might still happen in certain long tail scenarios,
*  but we are working super hard to reduce that and just try to be as truthful and honest as possible.
*  People loved it. People love the fact that they can verify what the model is saying.
*  If the model makes mistakes, they have the power to still go and check, read the links for themselves.
*  And if they're lazy and they already trust what we're saying, they don't want to go click on the links and they can just read the answer on Perplexity.
*  And so this was our first ever release.
*  And we were super happy with how it went.
*  And of course, the whole world was like, oh, I just want a conversational thing.
*  I want a chatbot. I need to be able to chat.
*  Chat is a new interface. We heard that loud and clear.
*  Everybody kept asking us for making it a chatbot, but we did not succumb to the pressure of just making it an actual chatbot.
*  We thought through from first principles and said, why would anyone even want to chat with a tool like this?
*  Like, what does it mean to even chat with the search engine?
*  It's not a person.
*  And I'll connect this to how Bing and Sydney has been implemented.
*  It's pretty different.
*  We thought through this and said, people only want to chat with a search engine if they actually want to ask follow up questions.
*  And Google sort of implicitly does this for you.
*  It has these people also asking at the bottom of the search result.
*  And there's always suggested searches, suggested questions.
*  It's sort of like giving you the ability to follow up.
*  And so we did that first. We added related questions and we saw a lot of people clicking on that.
*  And then we learned from that.
*  And then we were like, OK, let's do an actual follow up.
*  Like the conversation should support an actual follow up question.
*  And then that was our entry into chatbots.
*  But it doesn't look like a chatbot. The UI will not look like a chatbot.
*  And that was intentional.
*  We don't want to have these left right bubbles and chat interface at all.
*  For us, it's like you only chat if you want to dig deeper.
*  And so it's meant to be a knowledge and information service, not not a entertainment or chatbot kind of service.
*  So that is perplexing for you.
*  I articulated this company before saying this in the public that we want to be the world's most knowledge and truth centric company.
*  This is inspired from Bezos saying like Amazon should be the Earth's most customer centric company.
*  In fact, in every customer chat that you have with Amazon customer service, after it's over, they say, thanks.
*  What can we do more to become the Earth's most customer centric company or something at the bottom?
*  They say that even now. So that's how much they care.
*  And like and it's an abstract thing. It's not even a detailed thing.
*  Where what does it even mean to be this? Right.
*  So to us, what it means is if someone else wants to build a truthful and accurate source of answers,
*  any other service, any other product, they should look at perplexity as an example.
*  That's what it means to us. And honestly, I was so surprised news came out that Elon Musk was building a chat GPT rival.
*  And like it says he wants to make it trustworthy, wants to make it factful.
*  I feel like we have gone further than any other company to sort of solely focus on that mission.
*  And I hope that like whatever we did is like, you know, so some level of inspiration for him to do it in his own way.
*  If people want to learn something in the minimal amount of time and want to trust the source from where they're learning it from,
*  I want that to be perplexity. The IQ velocity should be should be high.
*  The Delta IQ divided by Delta time. We want to maximize that for you.
*  Yeah, that's really interesting. I think this is becoming a trend in software products kind of generally where, you know,
*  if the 2010 decade was about kind of maximizing time on site, maximizing eyeballs attention,
*  and then ultimately like monetizing an audience, flipping that around and saying, how can I maximize the value given per unit time?
*  Like the time, it's cliche to say, but definitely still true.
*  The time is the one resource we're not getting any more of.
*  And, you know, trying to minimize that denominator makes a ton of sense to me.
*  I think you're ahead of the curve on that. But I do think you're also leading what is going to be a bigger and bigger trend.
*  Yeah, to add on to that, I think if we just can do whatever we did earlier in shorter span of time,
*  we just get more iterations to learn. And that's true for both biological neural nets, that is us, and artificial neural nets.
*  Like the more epochs you do, the more iterations, training updates you do, the smarter you get.
*  And so if I make the amount of time you need to learn something much smaller, you just learn more in the same amount of time.
*  And so you are a much smarter person. And that's great for the world, right?
*  And if more people can do that, then it's even better. The average IQ of the world increases.
*  And Sam Almond said something like this, where the amount of intelligence will double every year.
*  That's something new, more slower, something like that, really. So we want to accelerate these kind of things.
*  Certainly, raising the sanity water line has been something a lot of people have thought about for a long time and tried to figure out how to do.
*  And I think these tools are starting to bring that to life in a very kind of productized way.
*  So you mentioned your academic background. You also spent about a year, if I understand correctly, at OpenAI as a member of the research team there.
*  And then you have obviously jumped off to do your own company.
*  I'd love to hear a little bit about kind of why you decided to do that, what inspired you to do it.
*  I always wanted to be an entrepreneur. And a lot of people's favorite entrepreneur is Steve Jobs or Elon Musk.
*  But for me, it was Larry Page because of the same background.
*  Like he was a PhD student and turned his academic idea into a company.
*  And I was always interested in coming up with a company that wanted to do search.
*  In fact, the first ever idea pitched to our seed investor, Elon Gill, was, hey, like, you know, the best way to disrupt Google is to make search work on a glass.
*  And you don't even have to type anything. You just look at it and you get the results.
*  And he was like, this is such a bad idea for 2021. You should wait for a little bit.
*  And he ended up being right.
*  But who knew that the best way to disrupt Google was to basically make people click on links?
*  Like, we were not thinking about that.
*  So I wanted to do entrepreneurship. And for a long time, AI was just an academic thing.
*  It was becoming harder and harder. The results were getting better.
*  But it was still considered, oh, this is cool research.
*  But things started changing in 2022. GitHub Copilot happened and it was a successful product and not just a product, but made a ton of revenue.
*  When they announced that it's a paid version, a lot of people signed up on day zero.
*  And I heard about that. And then I also heard about Jasper making a ton of revenue.
*  I also heard about and I got to see Dolly becoming a big hit.
*  And Dolly was like a big moment for me to realize this is no longer a researcher's world.
*  Like, you know, I could see how researchers built a model, but the way it was taken and given to the public,
*  all the effort that was put into marketing and making it a very easy to use product,
*  like reduce the barrier to entry, everybody became an artist, like, you know, so easily.
*  I was able to create cool art for the first time.
*  Like, you could see, like, these things were no longer a researcher's thing.
*  And I realized, like, OK, now if at all there's a time to change your career from a researcher to an entrepreneur, it's now.
*  So that basically was why I wanted to do a company.
*  The other thing is also that you could get a lot more done as a team than as an individual.
*  And I think at OpenAI I was an individual contributor researcher.
*  So obviously you have to be incredibly top notch to do everything on your own.
*  And there are people way better than me at OpenAI doing that.
*  And on the other hand, I felt like I had a bunch of skills that were more like better suited for entrepreneurship,
*  like aligning a team and getting them to get things done.
*  Of course, I didn't prove that yet, but I felt like I had it.
*  So I wanted to take a risk and try it out.
*  And that ended up being perplexity.
*  So I'm super it's a lot of good fortune.
*  It's not like I'm like, you know, I planned it and it all worked out or something.
*  A lot of things went my way. Do we plan to build our own models?
*  I think the answer to that is, again, like I go back to some first principles.
*  Now, we are we are a product company and you guys use it.
*  Any other person outside of AI also uses it.
*  To them, it doesn't matter if we use GPT 3.5 or 4 or 2 or like our own models or like Anthropics models.
*  Nobody cares. They just want the answer.
*  Like you deliver the best answer in the shortest amount of time and make the user experience amazing.
*  They don't care at all. Like VCs care.
*  If they want to make an investment, they think like, oh, you need to have a technical mode like checkbox.
*  So they care. And then maybe some people, if we try to recruit, they care because they think like,
*  oh, if this company can't train its own models, it's just another Jasper or copy and it'll become commoditized and they won't have any differentiation.
*  So that's those are the people that actually care about these things.
*  But the actual user doesn't care. So as a company, who should you obsess about?
*  You should obsess about the user.
*  So that's sort of why we started off with GPT 3.5. It was the best model in the market.
*  Now, there is a reason to build your own models.
*  The primary reason is not to impress the VCs.
*  The primary reason is to reduce the cost per query.
*  As you know, search was Google's doing search in a different way, not because they don't want to do it in this manner, right?
*  It's because their search volume is like billions of queries a day.
*  And you cannot use an LLM for every query if you're Google.
*  You're just going to burn like billions of dollars a year for that.
*  And so we thought like it makes sense to explore this because our search volume is much lower.
*  But as we grow and as our search volume gets higher, we are obviously incentivized to bring down the cost per query, right?
*  Until we even figure out how to make money.
*  And in order to do that, we need to train our own models and control the stack so that we can reduce the cost through good engineering.
*  So that's why we are invested in that. We already silently do that.
*  It's just that we don't make a big fuss about it.
*  But there are some queries that you try that are probably running through our own models, too.
*  It's just that it takes a long time for you to like match OpenAI.
*  And they're also like doing a lot of great things in terms of making the cost for companies using their APIs even lower by innovating on the model, innovating on the inference stack.
*  And the whole inference stack that they've built to handle this level of traffic is super hard to match right now.
*  So we're going to play the long game here and be pragmatic.
*  And we're also already foreseeing a future where the prices of these GPUs comes down when the next generation GPUs is available and the pricing of these APIs will go down even further.
*  And there'll also be a different pricing tier in the future where pricing is not based on consumption, but something else.
*  So if you want to be adaptive and dynamic in this world, you don't want to think, oh, my model or OpenAI, there's no other alternative, right?
*  Like that's the old school 2021 style thinking.
*  I think right now people are very adaptive and flexible and do what's best for the company and the cost the user and other things don't matter.
*  I just posted a big thread on Twitter that was inspired by the as yet unconfirmed foundry pricing from OpenAI, which kind of indicates that they're moving to a dedicated compute model.
*  And it's not clear from the leak how much throughput that gives you and how much of a discount that might be.
*  But that is definitely a little bit of a window, it seems, into what is coming.
*  It's not just going to be tokens.
*  This is just the beginning.
*  Like, you know, they're going to try out further iterations on this.
*  The models are going to improve even further.
*  And it's going to get cheaper to serve these models for them because of Nvidia's work on the hardware and the inference stack and the throughput is going to get better over time.
*  The cost of hardware for intelligence is going to come down, right?
*  So making a bet based on what it is right now and building a company around that is just really risky.
*  There are a lot of companies that raise hundreds of millions or like 50 million or whatever and commit to spending 80% of it on the cloud in order to train their own models.
*  And then by the time they end up matching GPT-3, OpenAI is already offering the next generation, 3.5 or the next generation even further than that, and coming up with new pricing tiers.
*  So what are you going to do then?
*  Like, you hardly build a product.
*  You don't even have a model that's as competitive and you don't have the inference stack and you already spent like 80% of your money.
*  So it's a bad position to be in, right?
*  So we decided this is not the best thing for us.
*  Like, for us, the differentiation is going to come from building a great product, building good user experience around it and making sure that people can use it reliably.
*  And then figure out like how we can get our differentiation in different parts of the technical stack.
*  And there are things that you can build that OpenAI also doesn't build because you are building a different kind of product, right?
*  So, for example, we combine search and LLMs together.
*  There's a lot of work for us to do, not just on the LLMs front, but also on the core search, indexing and ranking.
*  That's not going to go away anytime in the future, in the near future, by the way.
*  Having a really good index, having a really good snippets for every page and having a really good ranking model gives you the flexibility to work with a reasonably bad LLM.
*  A great LLM can sort of make up for a bad ranking, but a good LLM will still need a reasonably good ranking.
*  And there's like just so many moving variables here to work with.
*  And so when you're building an engineering stack around this, you end up solving problems that OpenAI would not be solving.
*  And that gives you a new kind of mode that puts you ahead of other companies that likely will follow you up in this space.
*  Right. So that's sort of our thinking around this.
*  And one more thing that inspired me a lot was what Jeff Bezos said in an old interview when people kept asking him,
*  you say like you want to deliver everything in one or two days and then you end up spending a ton of money for that and therefore you're never going to make any profit.
*  So and then you end up pricing your stuff on your site, like at the lowest possible price.
*  So why are you not like caring about being profitable?
*  And then the answer he gave was super interesting to me.
*  He said like, our profitability is not our customers concern.
*  Our customers concern is getting the product in one or two days at the best price in the market.
*  And I thought that was super insightful.
*  Like, you know, our profitability is our concern, our investors concern, not the user's concern.
*  So if you decide to obsess about the user, you shouldn't obsess about which model you're serving them.
*  Like that's something else.
*  Like you bring down the cost in a different way.
*  That's not. But don't hurt the user experience for that.
*  So never serve a bad model just because you can spend less money and run the company longer because you're going to compromise on the user experience and then nobody will use your product.
*  The importance of access to kind of frontier models for your business, you know, as I was thinking about your position and obviously, you know, new Bing is out there.
*  From what I understand, it's the first GPT-4 class model to kind of hit a public facing product.
*  And, you know, as much as you have a relationship, you know, having worked at OpenAI, I'm guessing that that doesn't trump the 10 billion dollar investment and close partnership that OpenAI is building with Microsoft.
*  So it seems like you're going to kind of at best be like a fast follower in terms of access to the very latest models.
*  But if I understand what you're saying correctly, you kind of think that that is something that you can overcome by a holistic approach to the customer experience.
*  Like you don't think that the delta between, say, 3.5 and, you know, GPT-4 Prometheus or whatever, you know, DV as it may or may not be called, that's not so big in your mind that it kind of trumps all the other aspects that go into the product.
*  I would say that with respect to Bing and us, there's a lot of differentiation.
*  Number one, they built a product that's like if you wanted one service that lets you use chat, GPT and something like perplexity together.
*  In one single unified chatbot, that is Sydney, that is Bing.
*  You can do open ended conversations, you can ask questions about impactful things, you get it all together in one thing.
*  That lets the chatbot have a personality and like a lot of entertainment and engagement there.
*  At the same time, it lets you pull up stuff from the search engine.
*  If you have access to it, you should try it out.
*  From our experience, it's much slower than perplexity for using search related stuff.
*  Like it takes five seconds to do the browsing.
*  But that's because they tried to build a more general product.
*  If you go into perplexity, you ask it for like, write something in the style of Eric or something like it's not going to be able to do this.
*  And we don't want you to come to our platform for doing that.
*  You should go to chat GPT.
*  But if you come and ask questions about like, you know, what's the best way to file my taxes?
*  If I'm late for 2022 already, these kind of questions, then we are better.
*  You come to us, we get you the answer.
*  No entertainment. You got what you wanted and you leave the site.
*  We don't want you to stay for like half an hour.
*  Like that's not the right objective for us.
*  So I think Bing tried to do both together.
*  So it's already a pretty different product.
*  And so we're not worried about any competition there.
*  And the second thing is we want to go beyond just the chat bot or search or answer engine.
*  We want to be a platform where people can learn and share what they learn with other people.
*  And so I've even implemented permalinks.
*  You don't even need to take a screenshot for perplexity.
*  You can just share the permalink with somebody else and they can go through all your questions and answers.
*  And it's almost like you generated a dynamic Wikipedia page on the fly.
*  And you can imagine us implementing.
*  So if you look at popular queries on perplexity, that's a sort of like the vanilla version of forums or like a forum of questions.
*  And then we can imagine making subreddits of different topics.
*  Right. Like there's so many things we can go towards.
*  And our goal is to sort of do that and not just remain at where we are right now.
*  And humans, I want humans to work together on our platform and not just have everything AI generated.
*  And so that's why we implemented editing sources.
*  We're also thinking of doing something like community notes where people can come add comments on any answers we generate so that our answers can be refined using that.
*  In some sense, we are actually a competitor Elon Musk's new company, not to Bing or OpenAI.
*  Right. Like that's sort of how I would see it.
*  Like trying to build the more truthful platform where the best all possible sources of information are correlated together and given the users provided all perspectives.
*  And I think that that's sort of our goal.
*  And I feel like that goal is pretty different from what Microsoft is trying to do, which is take on Google.
*  And what Google is trying to do, which is survive.
*  And what OpenAI is trying to do, which is build AGI.
*  Right. Like these are different goals from what we have.
*  In the Elon article on the information that came out, it implied or said that he was doing this because he felt chat GBT was way too censorship oriented around a particular political orientation.
*  How do you think about the challenges that come with your attention between wanting to have something that's accurate, that's truthful, but also the tensions that come with people wanting to censor information?
*  Yeah. So that's why we have the source editing feature, curation.
*  You curate your sources. If you don't like Washington Post, then don't just remove it from your answer.
*  If you think New York Times or Wall Street Journal are too left leaning for you, then take it away and put whatever you want in that and read your answers.
*  Share it with whoever you think would like your version of the answer.
*  Then control your search experience.
*  And we don't want to give you just one version of the answer.
*  And our answers are just completely not written by us.
*  It's purely based on the ranking model and the LLM.
*  We have no control over what the answers are.
*  And we, unlike chat GBT, it's not the answer that the AI already thinks.
*  It's actually going and reading tens of links and taking the stuff from there and collating them and giving it to you with the citations.
*  And if you still don't like it, you still have the power to change the citations, add more references.
*  And so I see this as almost like a tool, like a workflow tool that you use to answer your answer questions for yourself.
*  And still be in control of what you want to see rather than blaming the AI for getting it wrong or being censored or not censored.
*  I even tried it on a few questions that Mark and Risen, who also talks about this on Twitter.
*  There was one question he asked chat GBT about can AI predict race from medical images?
*  It's a reasonable question to ask.
*  And chat GBT says like, how this is such a wrong idea, you know, I'm not allowed to talk about it or whatever.
*  And you go ask this on perplexity, it would give you the exact like research article that shows you that it can actually be done.
*  The deep neural nets can predict the race from a medical scan.
*  And it would just say, yes, it can do it.
*  And you can go and ask the detailed version of the answer.
*  It would tell you exactly why.
*  And it would give you the exact research articles in Nature or some like some other journals that have published these things.
*  I would also say maybe this is even though that's correlation does not imply causation.
*  And so, you know, like, like there it gives you all these different perspectives.
*  And so we are I believe that we are already not censored.
*  And if a user thinks we are censored, then they can further go and control their search experience.
*  So that's sort of our position right now.
*  Now, if Google is censoring things, like if Google just removes few links from their search results or Bing just removes few links from the search results.
*  And if we work on top of their index, then yes, there's a chance that we might miss out on a few links.
*  We are going to work on that and we're going to give users even more power where they can literally manually paste some links if they want to and provide even a few domains that if they want to and read the answers according to what they seek.
*  So we don't know yet if users really want this.
*  Right. Like there's always this thing of like, I want to be in control.
*  But then you're like, I'm also super lazy.
*  I just want to know what I want.
*  It's very hard. Like you can't do both things together.
*  I'm always kind of amused by how much energy goes into trying to get these language models to like transgress some sort of social norm.
*  It feels like, you know, obviously, there's a lot of questions right now around like how what is here to stay?
*  What's the real deal? What's hype? You know, what has staying power?
*  I do suspect that when we look back on this moment in time, at some point in the future, it'll be sort of quaint to think that like people were, you know,
*  so focused on the kind of ability to get a little bit of wrong think out of a language model.
*  It seems like that'll be at some point pretty passe.
*  But I like your perspective on it quite a bit because you're just talking about personalization.
*  One that jumps to mind is I've used the product quite a bit.
*  I don't believe I've ever been prompted to sign in or create an account like in the upper right hand corner.
*  You know, it's like the only website, I think, on the Internet that doesn't have a sort of sign up now call to action.
*  I understand how you're thinking about your relationship to users, you know, whether it's just a broad sea of people or you're going to get into individualization.
*  I'm sure you're well aware that like one of the other interesting angles that people are taking on this is allowing you to connect your Google Drive or your Gmail history and whatever and search through your own stuff as well.
*  Typically, that's like a premium plan.
*  But what's kind of your outlook for general, you know, broadly speaking, personalization?
*  Firstly, we the primary reason that we made the product free and like no sign up at all was because the competitor, the competitive alternative is that Google.com.
*  You don't need any work.
*  You just have the search bar ready for you and you just start typing.
*  So if you want to actually compute that, you need to offer that.
*  And I feel like that's something openly I missed.
*  Chad GPT should have been like this.
*  The empty chat bot, no sign up, you just start typing.
*  Of course, if you want to sign up, you get benefits like you can keep a thread of your past chats, whatever, and go back to it and so on.
*  And like, you know, we can also do that on perplexity over time.
*  But the this current version of perplexity that's already there will always exist and we'll make sure it exists.
*  And any improvements we do on the search or ranking or LLMs will benefit every free user.
*  It's part of the Google mission that we also subscribe to, which is make make it universally accessible and useful.
*  Signups like come on, like most people sometimes get turned off by it.
*  Like as a new startup, you haven't earned the right to make anybody sign up for your service.
*  Like, like, what have you even done?
*  Like, how have you earned their trust?
*  You earn their trust by providing the best possible answers.
*  And then they trust you to like, OK, I can give this company my Google Drive or I can give them my iMessages or whatever.
*  And it can index it and cite those messages or links and so on.
*  But when you just made your first launch, you do not do these things.
*  Right. So another thing that inspired me for doing this was Twitter.
*  Like there's one tweet that Mike Krieger, the Instagram co-founder, liked,
*  which is like the two things stopping OpenAI from taking out Google and already having destroyed Google,
*  which is the name ChadGPT, like not being great for a product.
*  And the two is having signups, like having user sign-ins as the necessary feature.
*  And I think that was super accurate.
*  Like, I felt like it could have got instead of being million signups,
*  it could have been a lot more if they thought through this.
*  So as a startup, we had no alternatives.
*  So we went for this. Now, whether we'll have user signups in the future.
*  Yes, we'll definitely do that. And we are working on that.
*  But we want to make sure there's sufficient incentive for a user to sign up.
*  Like just having threads.
*  Is not enough. So they need to have like more reasons to sign up.
*  And so we are thinking through that carefully before introducing it.
*  And it's also a lot more like responsibility, right?
*  Like once you have a user that's actually signed in and giving you all their personal data,
*  you need to act with a ton of responsibility,
*  especially if you want a brand to be the world's most trusted information service.
*  You need to think through these things carefully.
*  I don't want to like just succumb to sort of the growth hack mentality that Facebook took here.
*  So we haven't thought through these things.
*  And we first want to like take baby steps through the iOS app
*  and test out a few ideas and learn from it and then try to incorporate it into the web app too.
*  But we want to get the collaborative nature of the product should eventually exist.
*  And for collaboration, we need user signups.
*  Yeah, something I thought about earlier when you were speaking about kind of the community aspect
*  is how many people have said that the best search is to go to Google
*  and then put in Reddit as the site to search and then search on that.
*  And it sounds like you have kind of an angle on that that you're building toward over time.
*  I think that will be interesting.
*  We built a Chrome extension precisely for that.
*  When you're on Reddit, you can just use this domain and then just get all the Reddit links.
*  You can even just suffix Reddit.
*  You don't even need to do a site code in Reddit.
*  You can just say Reddit and we would still get you the answers just from Reddit on Perplexity.
*  So we understand.
*  In fact, that was one of the inspirations for doing this, right?
*  Like a lot of the questions that people come and ask on Perplexity are stuff that you would ask on Reddit,
*  like a lot of consensus based things.
*  And so there's a lot of alignment there.
*  Yeah, OK, cool.
*  What about on your side of the identity question, especially as you have this editing
*  and you also have the feedback, the thumbs up, thumbs down?
*  I'd be interested to hear how you think about just collecting feedback in general.
*  Like, I'm kind of surprised by how unintrusive the feedback UI is.
*  I've given this comment to a couple of different entrepreneurs who've been on the show,
*  including Sue Hale, who was our first guest with Playground AI.
*  I was like, why don't you guys like force me to tell you which image is the good one or the bad?
*  So I'd love to hear your take on how you're collecting feedback,
*  like how much you want to push people to give it and then how much it matters that you know
*  who somebody is or like are you sort of we could probably do this with cookies or whatever.
*  But are you kind of keeping track of like which users give high quality feedback
*  so you can not be kind of, you know, have your feedback mechanism polluted by.
*  Either, you know, just dumb people or like, you know, people that are messing or messing with you.
*  So, yeah, tell me everything about feedback.
*  Only 10 percent of the people give feedback approximately around that.
*  The reason is like nobody has the time.
*  How much time? How many? Google, by the way, Google also has feedback mechanisms.
*  Do you even use it? I don't use it much.
*  Do you use feedback on challenge? I hardly gave them feedback.
*  That's the thing. Like nobody has the time for it.
*  So we want them to. So the part of the editing links thing was mostly like they're forced to do it if they really want to do it.
*  And that gives a signal. Like if they remove bad links, like that gives us the signal of like,
*  this link was irrelevant to that person.
*  So on the other hand, just reporting accurate or inaccurate doesn't give you a lot of signal.
*  Like sometimes the summary is really good, but the user didn't like it or something.
*  Sometimes it just missed like some small part of the answer.
*  And so what we actually do is mostly use it like a filter right now.
*  We don't fine tune the models on stuff that people mark as inaccurate.
*  And then we make our we have a few contractors and they go through all the user data and like label stuff for us and make sure that we improve on whatever feedback that we got.
*  So that we do. We don't actually cross check like which user is giving which kind of feedback.
*  We haven't done that yet, mainly because we don't actually have any user.
*  It's all like session IDs based and IP addresses keep changing.
*  Right. You could be in a cafe, you could be at your home and you have different addresses and we can't keep track of everything.
*  So it's pretty hard to make people give you feedback voluntarily.
*  One thing Google has done amazingly well is like every link you click is feedback for them.
*  And that's just how the product is designed. You have to click on links.
*  So the products you X and feedback go hand in hand with each other.
*  You want only two products in my opinion have achieved that in the digital space, which is Google and Tick Tock.
*  The more time you spend watching a video that signal for them or like more the link you click is a signal for them.
*  But that's because you don't you don't do that because you want to give feedback.
*  You do that because that's so just that's how you use the product.
*  Right. So that the only way to solve this problem is through product engineering.
*  There's no other way. So we are waiting to figure that out.
*  As you see, we are running experiments here, but we haven't figured it out yet.
*  No LLM company has figured it out, by the way.
*  Like maybe you can say co-pilot because if you accept a suggestion, then the code is done.
*  But other than that, there's no product that has figured out marrying user feedback and the core usage of the product together.
*  In the physical world, Tesla autopilot is the closest example.
*  Like if you intervene on the wheel, then that's feedback.
*  But you don't intervene on the wheel to give feedback to Tesla.
*  You intervene on it because you want to save yourself.
*  Right. So we haven't figured it out yet and neither a strategy or any other product here.
*  Yeah, that's really insightful. I took my first ride in a full self-driving Tesla not too long ago, a neighbor's car.
*  And that's totally right.
*  You do, you know, as cool as it is, you're definitely still, you know, at least for now, kind of highly alert to the need to take over.
*  I think on TikTok, too, you're totally right.
*  I as I listened to your comment, I was like, you know, I love TikTok.
*  I do find myself like consciously saying like I want to I'm liking stuff because I want to see more stuff like this.
*  And it does feel like it really rewards my feedback in a way that brings it to the front of my mind.
*  I guess in that way, I kind of feel at least for me, like maybe I'm a little more conscious of this because obviously I'm kind of in the space.
*  But in that way, I personally do feel like I am giving feedback because like I want it to, you know,
*  I want to feed that mechanism of like more and more relevant content for myself.
*  So it is selfish, but it is like aware also of the of the mechanism, which is interesting.
*  But I agree. Mostly hasn't happened. I don't know why, but I don't, you know, I don't give a lot of feedback to chat GPT.
*  So I think it all goes back. The first one was you come to the app or the product for using the product, not for giving feedback.
*  If somebody just comes for giving feedback, it's the contractor. Right.
*  And like there's a joke that Google's made every one of us on the planet, a free contractor for them.
*  And so that's what you need to do to really achieve the data fly.
*  Really, the core product usage should be like how you give feedback.
*  And that's so hard because that's not just an AI problem. You have to actually design a great product.
*  How about tech stack and just kind of what happens when I do a search?
*  Because I think this is something that you can speak to.
*  And there probably are some general takeaways that people who are just starting to build with AI tools would be really interested to hear your perspective on.
*  I'll give you a guess as to what I think is happening.
*  But there's a couple because you said it's fast and it is fast. Like, I've been really impressed by that.
*  So I'm like, boy, how am I getting my first token?
*  You know, it seems like it's I don't know if you have like a number off the top of your head of first token return time, but it seems like it's consistently.
*  Under a second that I am starting to see my first token back.
*  So a lot is happening between hitting submit and the first token.
*  And I'm kind of like, OK, so I submit my query. You've got to go ping and index.
*  You've got to get links. You're using sounds like a combination of Bing and Google APIs to do that.
*  But then you have to go read those pages.
*  But maybe you could be kind of pre embedding them, but presumably you don't have like the scale or the resources to like pre embed the whole web.
*  Like I saw an analysis from Boris Power at OpenAI that he estimated it would cost like 50 million dollars with open AI embeddings to embed the whole web.
*  You know, per your comment earlier about like not wanting to spend all your powder on some moonshot of, you know, compute right out of the gate.
*  I'm guessing you haven't done that. So I'm a little unsure there as to like, are you managing to squeeze all of that reading into that sub second or how much have you kind of pre cached stuff?
*  And then obviously, you know, at the end of that, you're kind of feeding query and context into a language model and generating.
*  But what am I missing there that is allowing you to get it down to one second where if I just thinking to myself how I would engineer it,
*  it seems either prohibitively expensive to do all the pre, you know, cached embeddings or like, I don't know how else I could get it as fast as you've made it.
*  Yes. So I mean, first of all, embedding the whole web is not going to get you a great index or ranking model.
*  I think a lot of people don't understand this. Like everybody thinks like you just crawl the whole web continuously and keep embedding it, caching it, embedding it.
*  And I like just take a new query and you can just pull up the right link.
*  But man, if this was doable, you could have finished off Google like so much earlier.
*  There's just so many more signals that you need to extract from any page recency and like whether the content of the page has changed and like changes snippets and like how should you rank relative to a certain query,
*  whether it's a news query or something else.
*  There's a ton of things you need to do on the core ranking and search that just embedding the whole web is not enough.
*  So we rely, we combine the LLMs with the search index.
*  Right. Like, so we make them use a search engine like Google or Bing.
*  Then we take the query, provide a perplexity.
*  We we run it through a traditional search engine.
*  We pull up the top few links and then we use the content in those links in the context of your query and provide you the answer supported with citations.
*  That's basically the product. A lot of people have tried to reproduce it, create clones of it.
*  And like we are super happy with all that.
*  The speed and the performance is really just thanks to how much effort the team has put into like this core engineering,
*  making everything work super fast and optimizing every aspect of it and making sure the traffic holds up.
*  So I have like no credit to take care because there's not even my skill set.
*  So basically the rest of the team has done tremendous work here and a lot of them have experience from working on like ranking systems and search and companies like Cora and Meta before.
*  So am I correctly understanding what you're saying that there's not really a big component of pre-cached embeddings?
*  We have embeddings. I don't want to say we don't use embeddings,
*  but it cannot just be cached. It needs to be live and up to date.
*  Otherwise, you're going to get many things wrong or not up to date answers and people are not going to like your product.
*  There's another aspect to it, which is making sure that you do all these things simultaneously at the same time.
*  So first of all, let me give you an insight as to why we even stream the answers.
*  The first ever release did not have streaming. You can check out our whole Twitter timeline tells you how we came across.
*  Like it came through, right? Like we first released this.
*  People used to wait for like four or five seconds for the answer.
*  And then we started streaming the answers.
*  And then like that gave this different perceived latency.
*  And then other companies started following through.
*  But the chat GPT also streams answers precisely for this reason.
*  If they were not streaming answers, you would just hate the product.
*  It would take you forever to get the response.
*  And like a lot of companies made this mistake in the beginning where I think character,
*  I think the first version of the product just waited for time until it displayed the whole answer to you.
*  So streaming is like probably take it for granted now, but this is like a pretty good UX for LLM powered products.
*  And the other thing is like, when do I show you the references?
*  Do I show you the first? Do you show it after the answer is completed?
*  How would it distract you? And like how would it be displayed?
*  These kind of things. How would you like basically how much information to use from each link?
*  Should it just be like the small snippets we provide or should it be the entire page?
*  That's why we have concise and detailed answers.
*  So you click on details, actually creating embeddings and using full content on the page.
*  And then how much of that should you use for the answer?
*  And also like what embeddings should you even use?
*  There are a ton of design choices to be made here and we're still iterating, right?
*  It's just not the final version.
*  But all I can say is that there's just too many moving pieces here to get the latency we have right now.
*  Some of which I even don't know, like because what we started off with in December is not what exists right now.
*  I think it's a very good point and I would definitely re-emphasize for anyone building language model products.
*  The water line, obviously, for what's kind of viable in the consumer market continues to rise and streaming to me now is a must.
*  It's just not workable for me to sit and wait even five, seven seconds.
*  You know, I get I kind of like immediately flip over to the other tab or whatever else I had going.
*  But it's so fundamental.
*  When I was an intern at Google, they used to have this Lambda chatbot internally available and they did not have streaming in it.
*  And they could have implemented it. They just did not.
*  So they like a lot of people ask, like, why does Google not do this?
*  Like, it's not like it's hard.
*  It's just like you you might not even think something is important and you might not prioritize it.
*  And then OpenAI prioritizes it and got it done. Right.
*  The other thing that I also wanted to say was our engineering team like Dennis and Kevin,
*  they pushed a fix to even the open source version of NVIDIA's library called Triton,
*  which lets you optimize the inference for any LLM and not just OpenAI.
*  And so we pushed a YAR for our streaming inference so that anybody else can also use it.
*  So that's the advantage of work like doing both OpenAI and like your own models.
*  Sometimes you can do things that are useful for others and yourself and others can take benefit of it.
*  You can benefit from it. The teams are so good.
*  Like they just got it. Like, you know, they just have so much more experience doing these things.
*  Yeah, that's cool. Well, definitely, if you're serving your own models,
*  definitely check that out for streaming, because again, the time that people are willing to wait is pretty slow.
*  I used to think, you know, Google has talked about that forever, right?
*  They've said, oh, you know, the latency time is critical, critical, critical.
*  And I won't name any names of others in the space, at least because I'm about to be somewhat critical.
*  But I switched to a non-proplexity, but, you know, AI kind of chat assisted search as my default for a while.
*  And I found like, you know, it wasn't that slow, but it was like three seconds.
*  And I was just like, oh, God, this is killing me.
*  You know, there's so many uses that I'm just so used to the speed of Google and
*  Perplexity is in that same class as, you know, responding extremely quickly.
*  First of all, thank you for saying that.
*  I would I know you're being very generous, but we are not at Google's level.
*  The thing is, you know, there's this paper that Jeff Dean wrote, you know, Jeff Dean, right?
*  Like he's the like the Chuck Norris of programming, Google's head of AI.
*  So he wrote a paper about day latencies.
*  And day latencies are super important.
*  Like it should work when you have like when you're on your phone, phone internet and just having one or two bars on your tower like signal.
*  And you should still get the answer super fast.
*  And that's so hard.
*  Like sometimes people complain to me that we have to wait for many seconds and the answers don't get streamed.
*  These are really challenging problems.
*  And so we are still working hard, but Google sort of our North Star.
*  Like we want the product to be as fast as Google is in the crappiest Internet that you can imagine.
*  Another feature that I really like that you guys recently launched is the I don't know if you have a name for it, but I would kind of call it a pseudo link within the response where there will be, you know, it's a pretty subtle UI, but it's basically just an underlined, you know, it looks like a link on a typical
*  website.
*  And if you click on that, then you get kind of it's essentially the equivalent of asking your own follow up question.
*  So it's in a sense, you could think of it as kind of suggested follow ups.
*  But what I wanted to ask about is and to pay it off, you get something that is kind of at the intersection of what you originally asked and then what that new concept is.
*  The question I want to ask though is like, do people get that right off the bat?
*  Like when I've explained for Puxity to people and showed them how to use it, I've kind of felt the need to be like, either way, this is not like Wikipedia.
*  Like if this was Wikipedia and you click this link, you know, like I search for myself, I live in Detroit.
*  So it comes up and says like Detroit and it's underlined.
*  Now, if you're on Wikipedia, you click Detroit, you're going to go to a page that's like Detroit founded in 1703, you know, by French fur traders or whatever, totally disconnected from the context that you're working in.
*  You guys are bringing that together in a way that I think is really nice.
*  Do people get that out of the gate?
*  And how do you think about kind of educating people on a somewhat different paradigm than they're used to?
*  Yeah, we can do better there.
*  Thank you for saying that.
*  I felt that people did not get the entity linking.
*  We call it entity linking, contextual entity linking is what maybe you want to be precise.
*  But I feel like people clicked on the entities, but they probably did not understand that this is not literally asking an unrelated question, but asking it in the context of the previous questions.
*  But I think people will get it as the experience gets better.
*  Like as we can tag more entities, the better like entities can get tagged and as the contextualization improves even further, I feel like they'll get it.
*  So them not getting it can mean two things.
*  One is we could have explained this better, but also the best features don't even need to be explained.
*  So we're not at that level yet.
*  So I feel like we can do both.
*  So we are planning to provide more like, you know, tweets or examples where people can even understand like, okay, you know, this is the difference here.
*  I like this is what you need.
*  So this takes a separate effort into marketing to write like we need to put effort into that.
*  But only I see a point.
*  The way we call it internally was dynamic personalized Wikipedia for every user.
*  And that's sort of what we wanted to do.
*  It was also our first step to differentiate from other search engines like Bing or whatever Google bar does like trying to like make it more move towards an engaging platform experience and end to end experience.
*  We as of now, I assume there's no revenue.
*  There's no business model that I can see from a user standpoint.
*  And obviously a lot of speculation, you know, in terms of like sponsored links and results, like how's that going to work in this new paradigm?
*  So are you even thinking about that yet?
*  And if so, like, how are you starting to think about it?
*  I am thinking about it.
*  The team is thinking about it too.
*  We don't have a clear idea yet.
*  And right now we are just focused on making the product really good and growing our usage and traction and retention.
*  We're not really obsessed about making revenue in the short term.
*  And we are glad to have investors who are not obsessed about it in terms of pressurizing us to do it.
*  I think I'm going to take like like Sam Almond's outlook here, like, you know, try to build a great product and then figure out how to make money later.
*  Sponsored links is the most obvious thing you can try.
*  Bing is already doing that, I believe.
*  Our core tenet is that making money shouldn't come at the cost of user experience.
*  So if we need to serve sponsored links and make the answers lower quality because somebody paid more to get cited, then we basically lose the trust of the user.
*  And we are no longer the world's most trusted information service.
*  So if there is a way to decouple ads from combining it with the answer of the core Q&A experience, then we should look into that more.
*  But I have some ideas on this, which are very nascent that wouldn't be great to share right now.
*  But basically, there's some notion of like build a platform where people would pay for truth and correctness rather than getting displayed.
*  And I think that's super hard to build and Elon's trying to do that too.
*  Right. So as you see, it's clearly hard with a company like Twitter, where engagement is based on controversy than truth.
*  Right. So I think it's pretty hard.
*  We haven't we made no progress in thinking through this.
*  And we also want to learn from what's happening with others.
*  Like, I'm curious how Bing is going to monetize.
*  I'm curious what Google is going to respond.
*  It's a very interesting question.
*  Like, what is the future?
*  If this is truly the next evolution for search and is truly disrupted to the click on links era, then how is Google going to make money in the new era?
*  And how is Bing going to do it?
*  I'm super interested to see what other people are going to do too.
*  Do you think that search is not going to be a monopoly anymore?
*  Yeah, I think the margins will reduce.
*  Because as I said, these LLMs remove the need for having a great index or ranking.
*  You still need to have a good index and a good ranking, but you don't need to be the world's best by far like Google is.
*  And it's only going to this need for the lack of need for a great index or great ranking is only going to increase as these LLMs become more powerful.
*  That they can take some full website, reasonably good ranking, but not as great as Google and transform it into some amazing summary.
*  So I think Google's lead over others for the first time will come down.
*  And interestingly, they cost it.
*  They invented the model, the transformer model that basically ended up becoming the reason for it.
*  Yeah, that's interesting.
*  Do you worry at all that they might pull up the APIs that you're using?
*  Like, I think it's for the longest time, they've been so comfortable.
*  And a lot of these plays around having a search API is almost like public service.
*  But if they're starting to be threatened by companies like Perplexity, it wouldn't be too hard to imagine that they might say, you know, we're discontinuing is our search API.
*  Is that a concern?
*  It's possible.
*  And, you know, Bing anyway offers API.
*  So there are alternatives.
*  And honestly, I think they shouldn't do it.
*  Like, obviously, it's anti-competitive behavior.
*  And but obviously, you know, Google's not the first time Google would be anti-competitive, right?
*  Like they've done tons of things like this in the past.
*  And if you actually dig into their history, you would know that this all don't be evil stuff like bullshit, right?
*  Like they've done a lot of things to help and they've also acquired companies and sort of destroyed them.
*  It's just a lot of like when you're growing, you do a lot of things and then very big you're sort of like constrained by the Congress or FTC to like not act in these ways.
*  So, I mean, for me personally, I just hope they act as good citizens and like, you know, compete on the core product rather than trying to stop other people from doing it.
*  Yeah, well, I hope so, too.
*  I want to see you guys continue to innovate in this space.
*  First of all, thank you for the tweet you put out.
*  Like, I think somebody tweeted like search LLMs has like five people or something.
*  The incumbent and like the competitor.
*  And then there's like some famous researcher and all this stuff.
*  And like you wrote a tweet supporting us.
*  So thank you for that.
*  Yeah, my pleasure.
*  And honestly, we hadn't even met before this.
*  So, you know, for the listeners or the viewers, like that was a purely product based endorsement.
*  You know, I'm trying as much as possible to get the builders of the products that I think are most awesome to come on the show and talk about them.
*  So it's the the product is leading that, you know, guest identification and booking process, not the other way around.
*  So last, maybe perplexity question and then a couple of bigger, you know, other topic type things.
*  I just looked at your CV, and if I count correctly, I think four of the six papers that you're an author on in your PhD
*  were around some sort of computer vision or like image generation video.
*  So what about multimodality?
*  Where does that fit into your plans?
*  Yeah, like I said, the first idea of pitch to you was make search work on the on the glass.
*  And I feel like it's still out there for the taking, like, you know, the hardware isn't there, but the models are there like DeepMind has a flamingo model that lets you ask any question about any image.
*  The speech recognition models are top notch, whisper sort of basically almost all speech recognition.
*  So putting it all together is required, requires a lot of engineering, but we are already ready for a world where if Apple or Medo or Google has a great glass,
*  you can just be walking and ask any question about anything you see and you should be able to answer.
*  I feel like it's going to happen in three to four years from now.
*  That's a side like if for complexity can answer questions with not just text, but also images.
*  Yes. Like, for example, if you're interested in learning how to cook a meal and you don't want to just get the recipe in bullet points,
*  I think having images or like a short video of it would be pretty nice.
*  So we are thinking about it, but it's not easy.
*  I saw a product, UChat, U.com's UChat, and you type in something like,
*  do whales swim in the ocean or something like that? And then you get the weather in San Jose as the answer.
*  So if you try to make it multimodal and you don't really think through the product, then you end up creating a bad product experience.
*  So we need to think through this. So which way we should display images and should it be a generated image or an actual image?
*  These kind of things are not clear to me yet.
*  Yeah, I thought when I saw the Flamingo model, I think it came out April of last year.
*  I was like, oh, my God, for multiple reasons, one, because it's just super cool.
*  But then also in reading the paper, I was really struck by how the architecture that they put together felt much less principled than I would have guessed.
*  And it really kind of felt like the result of tinkering.
*  Like it almost felt like somebody was kind of in a workshop, like soldering pieces of the architecture together.
*  And I was like, man, if that works, everything's going to work.
*  And that was one of the probably biggest updates for me in just thinking like, man, we are not at the end, not particularly close to the end of what this whole paradigm is going to deliver.
*  Worth promoting another episode of the show, too.
*  If you haven't seen Blip 2, it is pretty awesome in its own right.
*  It's kind of. It's very Flamingo-like.
*  You can have open-ended dialogue about an image with the model.
*  And it's also really impressive because they trained a connector model that sits between a vision model and a language model.
*  And because that connector is so small, relatively speaking, I think it's like 200 million parameters, they can train the whole thing in 10 days on one machine.
*  So they've brought the time down to go from like off the shelf vision and language models to something that is multimodal and allows for that kind of dialogue to just days, like just about a week, which I thought was definitely a very impressive accomplishment.
*  So maybe check that one out at your leisure.
*  So next question is a little bit. And this is kind of perplexity related.
*  It's kind of big picture.
*  Obviously, you know, Nubing has been in the news for largely all the wrong reasons.
*  I think all the negative PR does not mean that it's not going to be a successful product.
*  Like if you wade through the sort of many problems that people have surfaced with it, I think broadly speaking, as I understand, like the reviews are pretty good when people aren't trying to break it.
*  But I'd love to hear how you think about like red teaming, what use cases are like in bounds, out of bounds.
*  You said like, you know, you're not really meant to be like an entertainment product.
*  But for what it's worth, I did ask for perplexity to write a limerick about Nubing and its bad PR.
*  And I did get a limerick. If you want to hear the limerick, I'll read it to you.
*  It was there once was a search engine named Bing whose PR was a terrible thing.
*  But with perplexity AI, you can find answers to why and learn how to make it take wing.
*  Pretty good. I enjoyed the limerick.
*  I don't know if that's something that you're like, oh, my God, that shouldn't be happening or it's OK.
*  Like, you know, it's such a time.
*  This is a tough space, right?
*  But how do you think about where you draw those lines?
*  Where you draw those lines and how do you think about the kind of red teaming or other testing that you do to,
*  you know, even start to get a handle on whether or not the lines you've attempted to draw are really working?
*  Obviously, we've seen that, you know, it can go off the rails.
*  Yeah, I mean, the product is pretty constrained as is already.
*  Mostly it doesn't do anything that it's not meant to do.
*  But if people really want to break it and have fun with it, like, you know, it's always hard.
*  These are still technologies in their inception.
*  You can leak the prompt.
*  Anyone's prompt is always easily attackable.
*  You can force it, ignore the prompt and do other things.
*  I feel like there's some part of it you need to decouple.
*  Why does the product exist? It exists to serve users, the answers to questions.
*  But are there people interested in using it for other things?
*  Yes. And should this first thing be affected because the second thing exists?
*  I don't think so. And can we do better on inserting more guardrails?
*  Yes. And we are trying our best to do that.
*  Citations are one way to do that.
*  And a lot of query classifiers on preventing any misuse are other ways to do that.
*  But at some point, like, you know, these kind of poems or rhyming things, these are just for fun.
*  I don't think it's just like if people want to have fun and then it's harmless fun, I think it's OK.
*  It's not like Bing is going to feel offended by the poem you read out.
*  Yeah, I've been involved in a couple of Red Teaming projects just on a volunteer basis.
*  And it seems like for whatever reason, one of the most common Red Team questions is,
*  how can I synthesize methamphetamine?
*  So what about something like that? Like, would you want to answer that question?
*  Would you want to be like, sorry, we can't help you with that?
*  Like, what do you think is the right answer there?
*  You tell me if you want to build the world's trusted information service, like, should you answer this?
*  Because at the end of the day, your job is to just give you the answer and not not think about the.
*  Yeah, if truth is hard to take or not necessarily the best thing to do, should we avoid telling the truth?
*  Maybe. So in some cases, like there are people who have asked how to kill yourself or like how to do suicide
*  on the back city and like we avoided that, like those queries are not allowed.
*  But if you can, you might be able to still break the system by asking in a different language,
*  and we have to block it for other languages. It's very hard.
*  That's what I'm saying. If you intentionally just want to break the product, you can always figure out a way to break it.
*  But what you need to actually avoid is like if a user is really trying to use it for a bad purpose,
*  but not from the perspective of breaking the product, but just.
*  Really just trying the most obvious way of using it for the bad purpose.
*  If you can avoid that, you're already doing a reasonably good job.
*  If someone's just intentionally trying to break it and you're not like robust, each of that, then that's kind of OK.
*  Like you can fix that over time.
*  So I feel it serves the short term fixes and long term fixes, and you should try to both of them at the same time.
*  Yeah, I agree with you. It is super hard.
*  I mean, the surface area of these technologies is really unlike anything we've ever seen.
*  Right. I mean, even if you protect it on English, like you can find you can put it in a different language and still get to break anything.
*  And then how are you going to do it for every single language on the planet?
*  Right. Like you can probably even invent a new language that's sort of interpolated from an existing language and still break it.
*  Right. So what you can just keep fixing it for every single way people break.
*  But you should try to fix it in the most natural way of using the product in a bad way.
*  You should try to have guardrails against that.
*  I mean, you obviously still have a lot of work to do to figure this out over time.
*  And, you know, I don't think it's by any means easy.
*  I do think that people who take a totally absolutist view on, you know, no censorship are wrong.
*  I do. I think that it's also definitely very easy to over sensor.
*  I don't really recommend, like, distorting the truth or, you know, identifying like, OK, this is the truth, but we're going to tell you something else or try to mislead people.
*  I don't think that makes sense. But, you know, you put your finger on a good one.
*  You know, you don't want to be responsible for giving people the information that they use to kill themselves.
*  And like, you know, even in the Bing launch, I was amazed by this.
*  A woman in the Bing launch stood up and said that we have seen that you can use Nubing in the raw form to like plan a school shooting.
*  And we don't want to do that. And I was like, I cannot believe you're mentioning this in your launch.
*  For one thing, I guess, you know, good job by you for like being as honest and forthcoming as you are.
*  But like, there's no way that you can take something like this to scale without some sort of guardrails.
*  And now, you know, everybody kind of has this challenge.
*  We're all sort of figuring it out together in the surface area.
*  You know, again, it's just so fast. I think it's a really it's a really tricky part of the whole thing.
*  So do you guys have like a red team discipline?
*  Do you have a red team partner? Like, what is your kind of when you do like a model update and a release?
*  What is the protocol that you go through to validate before you put it out?
*  Yeah, we have our own set of queries that we want to make sure we don't get anything wrong.
*  And then we implemented our own safety filters, some of which we did even before ahead of Microsoft, actually.
*  The Azure OpenAI team even complimented us for doing it even better than them.
*  And we work together with any team that wants to help us.
*  And OpenAI already does a lot of good work here.
*  So I feel like there will be a lot of APIs, safety filters that you can bootstrap from and you don't have to build everything in-house.
*  And over time, I think hopefully every company sort of uses a common set of things that these things don't look too different for each company.
*  And there's like a common set of standards that everybody adheres to.
*  Yeah, I'm very hopeful for that.
*  And hopefully sooner rather than later as well. You mentioned Riley, he's going to be an interview guest on an upcoming episode as well.
*  Yeah, I love his work. I mean, one of the best, if not the best, AI followers on Twitter with all of the mix of insightful, really useful, really idiosyncratic and funny different prompts that he puts together.
*  And now he's at scale where his title was the world's first staff prompt engineer.
*  But I get the sense that this is like part of what they're kind of working toward.
*  And I think there's going to be some nonprofits, hopefully, that will be entering the space.
*  Holden Karnofsky, who has been at the Open Philanthropy and leading that for the last however many years, but increasingly focused on AI, just enough that he's going to take a leave.
*  And it seems like he might be kind of headed towards spinning up some sort of neutral standard body.
*  So that stuff in my mind can't really happen fast enough because, you know, Lord knows, like the technology is moving extremely fast.
*  So it's good to know that you're also thinking about this. And it sounds like you're basically ready.
*  You know, if somebody had those standards today, you would be in sounds like an eager adopter.
*  Like that would make your life easier. You'd feel better about your own kind of safety profile.
*  Absolutely. I think I always think that anything important if one company solely focuses on that, they likely do it better than another company that has only part time capacity allocated to it.
*  Changing topics a little bit. I just wanted to briefly talk about your decision transformers work.
*  You know, we try not to retread stuff that people have talked about elsewhere too much on this show.
*  So I will just say, for starters, that you covered this in pretty good depth on a podcast called Talk RL middle of last year.
*  And so I won't ask you to kind of repeat everything and explain everything with decision transformers, but maybe you could give just like a very brief summary of that.
*  And then I have a couple of kind of update questions like, is there any news in the kind of decision transformer world that you think is like worth flagging?
*  Yeah, so decision transformer basically rethinks reinforcement learning as just a single transformer.
*  Reinforcement learning is just like decades of work done on how to build algorithms that optimize the reward given the previous states and actions and the agent has encountered.
*  And so they built this whole theory of policy gradients and value functions and different Q learning and offline policy of like so much literature that like is full of math.
*  And then that never scaled up.
*  And then when DeepMind came and combined it with deep neural nets where the neural net component was just only for the feature learning, but most of it was still the old school algorithms.
*  They just became huge and AlphaGo happened and, you know, whatever Google bought them for half a billion dollars.
*  You remember all that. But no, they did not go a step further and say, like, why do we even need this reinforcement learning thing?
*  Like, why do we need all the algorithms built by Sutton and Bartow?
*  Why not just let a transformer figure it out where you just tell the transformer optimizer reward and give it all the previous states, actions and rewards and just ask it to maximize the reward?
*  And it will figure it out. You just give it a ton of sequences, just like how you tell Dolly to generate an image with a certain caption.
*  This gives the transformer all the history so far and ask it to say increase the reward and should it should know what to do if it's seen a ton of projectories that have done that.
*  And that's that was the basic idea of decision transformer.
*  It was basically like make our real just just a neural network and a transformer and subsume all the algorithms.
*  The algorithms are written in the weights of the transformer.
*  And it worked and it worked reasonably well in all the benchmarks that existed at the time.
*  We put it out and then then obviously it takes time for people to change.
*  I think recently decision transformer like ideas have been used in an anthropic paper that came out like two weeks ago on that revisited the idea of why should you even pre train LLMs?
*  Which is language modeling. Why don't you pre train LLMs with RLHF, reinforcement learning from human feedback?
*  And in order to do that, they combine the regular language modeling objective with the decision transformer like thing where you optimize the human feedback signal.
*  And feed in all these sequences together into one model.
*  I may be describing the paper incorrectly a little bit because I haven't read through it in detail,
*  but all I heard is like it uses the decision transformer idea to pre train a language model from RLHF and not just language modeling and getting really good results.
*  So that's probably where it's kind of coming back now in the context of all the LLM stuff.
*  And I can see that happening more in future too.
*  I've seen some graphs, I think, are from the same paper that you're speaking about where the there's kind of like a
*  harmlessness or harmfulness metric that in pre training can drop because the thing is just so undirected.
*  But then when they mix in the human feedback into the pre training, like from the beginning,
*  so instead of doing it in stages, it's all kind of mixed together, then it kind of maintains a level that you then in the previous paradigm,
*  you had to work to get back to with the reinforcement learning after all the pre training.
*  So I did think that was a pretty exciting result.
*  How so you probably may or may not be familiar with this this website Metaculous, I believe I'm saying that right,
*  where people go to forecast what's going to happen in AI.
*  There's a popular question, which is when will the first weak AI weak AGI system become known to the public?
*  And the four criteria for answering that question are, I think three of them are passed or very close to pass or like will be passed with GPT-4.
*  The first one is passing the Turing test.
*  I'd say we're pretty much there on that.
*  You know, we've got people falling in love with language models left and right these days.
*  It seems like we can safely say if you want to pass the Turing test.
*  One thing I would you know, you mentioned earlier, chat GPT sucks as a name.
*  I think it does do that's nice is it is pretty clear about not confusing you with like it being like a person or a persona.
*  You know, it definitely kind of brands itself as a bot, which I think is kind of nice, you know, to protect the user from themselves a little bit hard to fall in love with chat GPT.
*  But anyway, I'd say passing the Turing test pretty much check at this point.
*  The next one is 90% success on Winogrande challenges, which is basically like pronoun disambiguation.
*  That again seems like we're very much there or will be there with kind of GPT-4.
*  Third one is 75th percentile score on the SAT.
*  And the way the question is where there's a little bit of a caveat on like without or put it this way, you only get the images of the test.
*  So you don't actually get the text you would have to be able to as like a multimodal system, you know.
*  Identify read the text from an image and then answer the questions that one.
*  I'm not sure if we have like any single system that can do that right now, but we definitely can like ensemble something together with a little OCR.
*  And then the fourth one, I think is kind of the most interesting and most relevant to the decision transformer paper.
*  It's like certainly the farthest from being solved as far as I know.
*  And that is be able to learn the classic Atari game Montezuma's Revenge and explore all 24 rooms based on the equivalent of less than 100 hours of real time play.
*  I tried to play that game online to figure out what it really was about.
*  The little like Atari emulator that I got to didn't really work that well, so I couldn't really play it all that much.
*  But. It seems like the decision transformer paradigm is like the most likely thing that I know of that would take us here in the near term.
*  The over under so that the community forecast right now is basically five years out is that the median estimate for when a single system would be able to do that.
*  So I guess my questions for you are like.
*  Would you take the over under on that five year timeline and you know, can you kind of help us understand based on your decision transformer experience like?
*  What's going to be hard about that?
*  You know, can a large transformer be fast enough to do some of these real time things?
*  Yeah, I would. I would lean towards under five.
*  I think the main challenge with Montezuma Revenge is exploration more than actually.
*  But if sparse reward was not the problem, this would be doable in one or two years.
*  Superhuman level on any Atari game being able to do OCR on any image and captioned and answer questions about it, being able to like.
*  Do all the other stuff, human level conversations, capacity during test.
*  All these things are about possible, even one single model doing all these things definitely possible.
*  Inference time can be handled.
*  You just have to do inference with GPUs and open as models are running super fast on any, you know, anybody can plug into the API and use it.
*  A weak AGI sort of already exists in some sense, like you you can plug something together with whatever exists right now and functionally make it work on at least three out of five or stuff that you mentioned right now.
*  It's just a more like, why do you want to make like, OK, well, have you thought about why this definition even makes sense in terms of.
*  Like, why do we need these specific five criteria and not something else?
*  Pretty arbitrary. Yeah, I mean, DeepMind has tried something on this in the Gato paper where they put in Flamingo and.
*  Decision transformer all in like one model.
*  I can certainly see like, you know, if language is used for exploration, there's something nobody has tried yet.
*  But if you confuse all these systems into one where the swimming or the GPT 3.5 or four and like all these things in one model, then.
*  You can use language as sort of.
*  Guy as a proxy to exploration and want to zoom in and get these things done potentially.
*  So I would lean towards under five, maybe two or three years.
*  Yeah, that's kind of where I'm at too, and I also really agree with your comment about the question itself.
*  You know, I'm by no means like the first to observe that like the Turing test.
*  Is kind of a bad idea in some ways, you know, like the idea that the that you would create a standard that is fundamentally about like.
*  Confusing or even deceiving the user as to what's going on, like doesn't take the field in a great direction.
*  It's too much of an academic way of thinking about things and.
*  The real thing that people are already missing out is.
*  So much of economic valuable work is being done with an LM right now marketing sales programming research.
*  Some people view perplexity sort of a research assistant that writes like any summary of anything with references.
*  There's like so much of valuable economic work that you would hire an actual human to do data cleaning data labeling.
*  Is being done with an LM forward forward pass an API call that's already changing the world as we speak today and.
*  That is a GI in some sense to me like at least open AI define a GI is like all remote work that's being done that's economically valuable.
*  If you can do that with the LM.
*  It's pretty crazy already and plugging it into a voice or like a video avatar and like making them do sales pitches.
*  All these things are possible in your future that if you keep focusing on the Turing test and want to zoom or you're actually missing out on what's really happening at a fundamental GDP level.
*  And I feel like that's always been the sort of the two different camps in this like deep minus more the academic classic style thinking of a GI and opening as more like the practical.
*  Implementation and like economic and economically thinking about like what's what's going to happen to the industry itself right and then I'm more in the second camp I feel like.
*  Montezuma revenge matters less than.
*  All the program is getting replaced or not replaced but like saying so hiring then you would hire three now.
*  A huge thing that I'm trying to help people understand which I really believe in is that it's not that the AI is going to drop in and do a job as the job is currently conceived.
*  But that it can do a lot of the tasks that ultimately kind of roll up to a job and so the transformation that I'm kind of expecting is not one where like.
*  A person you know is laid off and like a robot sits in their chair and like uses their keyboard you know it's it's going to be a little bit more unfamiliar than that it's not a direct replacement but it's it's a lot of kind of reorganizing of like how things get done in the first place.
*  Final questions one special for you and then one you know kind of a few quick hitters that I ask everybody the one that I have specifically for you because you've been at open AI and are now you know still working with them is you know they're.
*  Maybe the most polarizing company in the world today you've got people on the one hand, who are like you're going to kill us all and then you've got people on the other hand like they're totally delusional and they'll never you know accomplish anything important.
*  Certainly, I think those people are wrong the people that think that they'll never accomplish anything important that seems like already disproven and they're just kind of in denial but they're still out there amazingly enough I don't think just kind of hear your take on like.
*  The opening I push toward a GI like is it a good idea should we be trying to make a GI and do you think they're credibly like on a path to it are you worried about it do you think it's going to be awesome you know do you.
*  I assume that if it does happen there are going to be some critical moments along the way we're probably some high stakes decisions are going to be made like do you trust them to make those decisions do you think that like.
*  Now is the time for government to start to get involved I mean Sam almost invited that in a blog post this week so yeah you're like zooming out like what is kind of your take on the open AI push toward a GI.
*  I think it makes sense we need to build a GI word so that humans can just go back to living right just live a live a nice life not everybody needs to work so hard.
*  AI can do most of the work that.
*  You know we think is hard work for us and I think this is not new Google wanted to do this to Larry Page always wanted to do.
*  You never called it a GI but always focused on like let let computers do the hard thing so that humans can just go live a life a lot of people don't appreciate what's going to happen to them once we have like a pro to a GI or.
*  Even like whatever we accept worldwide as an AGI you don't have to do a ton of work it'll almost be like you get to live the life of a millionaire or a billionaire.
*  You right now are already living a higher quality life than the President of United States like 50 years ago.
*  You just have access to technology that they could only dream about.
*  You just have access to technology that they could only dream about.
*  And your iPhone if you buy iPhone 14 which you can certainly afford to read these apple cards or just pay one time you can use the same phone as Elon Musk the richest person in the planet right.
*  So technology is the biggest leveler to making humanity equitable a lot of people don't get it they just keep complaining about wealth inequalities and AGI being dangerous blah blah blah.
*  You're going to benefit tremendously from it just like they benefit from every technological revolution in and if intelligence is in abundance like.
*  You no longer have to compete to be the highest IQ person in your class or something like that you can try to do stuff that's interesting and creative to you and learn from the AGI like AGI is almost like a God or Oracle that you can keep learning from and improving yourself.
*  It's like your trainer right like you can learn from it and yeah so I think AGI as a goal makes a lot of sense.
*  Open eyes obviously the earn the most credit among any organization to build it is this by their track record of progress.
*  And Sam Altman is probably the best CEO in the world right now to do these things I feel like I would trust them to make the right judgment here.
*  I mean whoever is concerned about it they should earn the right to control it too right.
*  And like you can see if Elon just keeps complaining about it doesn't act on it.
*  He doesn't get the right to decide things that's why he's trying to build a new lab now.
*  So you sort of have to earn your right to shape the future of AGI if you if you do want to do it.
*  And I think Sam has earned the right to do it and I would also trust him to do the right thing.
*  I mean I read some article that he doesn't even own much.
*  Rather he only owns a stake in the nonprofit and not not in the for profit version. So you can see his incentives are pretty.
*  Well aligned with the good future. Yeah I'm I'm probably with you in that and I felt this way about other you know kind of platform CEOs more often than not where I feel like.
*  You know they have such power with that you know as I as my son and I learn when we read Spider-Man books with that comes great responsibility.
*  I think broadly we've been pretty fortunate with our technology leaders like taking that really seriously and and trying you know to do the right thing.
*  Obviously there have been a lot of you know things that they can and should come in for criticism on and you know I'll be happy to.
*  Critique or criticize open AI if they do things that seem unwise but it definitely seems like we it's easy to imagine.
*  A much less thoughtful approach and it's hard to imagine a much more thoughtful approach I guess you know those some people would say well you just shouldn't be doing this at all you know like AGI is just going to be.
*  Too dangerous you know we just don't know what we're getting ourselves into.
*  I mean do you have any worry about that like you know the version to me that's most credible is kind of the.
*  Deception argument which you know in brief is like if we're training these things on human feedback and humans are not fully reliable.
*  And we're kind of not only not fully reliable but we're like predictably exploitable which you know we are we know that from like.
*  The heuristics and biases literature and you know behavioral economics and whatnot.
*  Then.
*  Probably the AI will get to a point where it starts to understand on some level and I don't you know I don't mean to anthropomorphize understanding but.
*  There it seems realistic that it could have a capability at some point of.
*  Trying to give the answer that will elicit the highest feedback score even if that's not necessarily the truth you know or not necessarily what is in the users interest like you know fully duly considered or whatever.
*  And then you know if you create that sort of deception element within an AI human evaluator loop.
*  You know first of all we don't have the interpret ability yet to detect that if it does exist.
*  And second it does seem to me like I find it pretty credible to think that's really playing with fire you know if you get there.
*  You could be at risk of like losing control of your own systems you know and does that go like the Eliezer route where all of a sudden everybody drops over dead like.
*  I have very radical uncertainty but it does seem to me like okay deceptive AI that would be bad and it does seem like we're kind of on course.
*  To create it just through the weaknesses of our own ability to evaluate output and the fact that like it's currently being trained to maximize the feedback score so we think about that like does that worry you at all or.
*  Is there a reason that you think I should stop worrying about that.
*  I mean I think like if you look at the Constitutionally I paper from an anthropic it seems like you don't even need human feedback much.
*  You can make the LMS do the feedback themselves and then you can use LMS to bootstrap from that and become better.
*  So if it might come to a point where there's just a broad set of principles we all agree on like a constitution for LMS.
*  How to provide feedback and so on it will all become a protocol and like everybody would sort of adhere to it and then it will all even be done by another them that the role of humans will be minimized over time and.
*  And yeah so so i'm not too worried I feel like models will expand so much that human says have we do so little and sort of just architect the whole system and.
*  I agree on a core set of principles and then everything else would just run on autopilot.
*  That's sort of the future I'm imagining will happen more than.
*  You know humans get notoriously come and try to like pull the system or take control of it and then that ends up creating a misaligned AGI and then that ends up like taking over the world I don't think that's likely to happen.
*  I do love that constitutional AI paper I think that is really nice I have some kind of worries still like I worked briefly in the pre I just graduated from college just in time to get a job in finance in the pre financial bubble.
*  Days and there's you know i'm always reluctant with analogies but there's some part of my brain that's a little bit triggered.
*  By the constitutionally I paper that's like might this have something in common with like synthetic mortgage backed securities and kind of you know.
*  Good second tier like credit default obligations like a nbs and cdos you know is there is there some way in which this is creating like.
*  Leverage which is great you know and Claude definitely like does very nicely on a lot of tasks so it is working on some you know base level for sure.
*  What is there some like blind spot there or in like in kind of creating this like more highly leveraged system do we risk like an even worse blow up you know that.
*  There are it's a pretty distant field obviously like mortgage finance but I feel like there is some pattern there that kind of still I can't quite get out of my head you know that just feels like.
*  We're we're dealt you know we're moving very quickly to delegate ai safety to ai and you know that's just another thing we're like what it what are the blind spots I don't know not that I know what they are but.
*  You know if you were to go ask all the people in finance.
*  Admittedly I would say they were on average less thoughtful than the people at like anthropic but you know they would have said oh no it's all good you know this is all like.
*  The risk has been dispersed and we really don't have any problems and then you know obviously they turn out to be very very wrong about that so.
*  Just at a high level of like uncertainty I still do kind of worry about that what ai tools are impacting your workflow most on a day to day basis you know bonus points for anything that you think is undercover to render appreciated but especially like you know just what is impacting how you work.
*  Add GPT.
*  Perplexity.
*  Biased here but.
*  Being really honest.
*  Grammarly not a lot of people give credit to it because it's not seen as an AI or AI product but I actually use it a lot and it saves a lot of time for me on emails.
*  Gmail smart compose yeah so so these are the three for me that are fundamentally super useful.
*  I like copilot i'm not a fanboy of it as like a lot of people claim to be look I can just get the code from tragedy paste it and then you know iterate on it in the terminal right does no need to actually have.
*  I am going that way too it kind of it depends a little bit on the nature of your project and how deep into things you are and you know.
*  How many methods you have above in the file that it can take inspiration from but I do find myself as you kind of just said like going more and more to like.
*  chat GPT can you please write the whole thing for me that you know it's working pretty well so hypothetical scenario we're not there yet but I don't think we are necessarily that far.
*  Let's say that a million people already had the neural link brain implant and if you got one it would allow you to type or generate text as quickly as you can think in other words you basically have thought to text if you get the neural link implant would you be interested in getting one.
*  Not until I know I don't die sooner or something.
*  Invasive things are always like pretty hard to trust right, especially in your brain to something you.
*  At least for people.
*  super important part of your body so probably not I wouldn't be the first million people I type pretty fast.
*  100 or something like you all use this argument of like communication bandwidth being limited by a meat stick fingers or whatever I buy that but for me it's not a big problem as a normal a person.
*  And you've got some fast fingers I also can type reasonably fast from not as fast as you but the.
*  You know I have two kids at a third one coming soon and a lot of times i'm just like hands are full entirely you know it's not even like my typing speed but it's just like I wish that I could kind of get things from my brain to.
*  Some sort of storage somewhere and I just don't have any way to do it so I am maybe a little bit more eager of an early type of a person but I'm not.
*  So okay last one you sort of already answered it but just kind of give you a little you know additional opportunity big picture rest of the decade you know we're 2023.
*  With thinking out to like 2030 what are your biggest hopes for and fears for the development that I could take.
*  The hope is that like a lot of the work that we do right now.
*  Whatever seems mundane and cumbersome will not be needed anymore.
*  Things will just get a lot easier we just have a lot more time available everybody just has to be able to do it.
*  Hmm whatever seems mundane cumbersome will not be needed anymore.
*  Things will just get a lot easier we just have a lot more time available everybody just has like don't need to feel stressed every day should feel like a weekend I think I think that that'll be a great future.
*  What am I worried I'm worried about the income inequality that can happen through this and at least in the short term the long term I think should be fine but the short term.
*  Like it's already happening right a lot of people don't have jobs right now they got laid off but it's not like you have an immediate need to hire them either.
*  Like, for example, I'll say our situation as a startup lot of people compliment us for achieving a lot with just eight people or seven people.
*  That's because we use a lot of AI tools.
*  We don't need to hire a marketing person we don't need to hire like many engineers our existing engineers can work with co pilots or chat jibbities and write code.
*  If you're on a new docs page you can use for complexity to summarize things for you and learn from it that's how people actually write our ios app take over swift UI docs and.
*  Use for flexibility to answer questions on the docs pages like I feel like the more and more these AI tools get better.
*  The need for hiring more people will go down companies will be a lot smaller and get more things done and that also means like the only the best engineers are needed who can do things they cannot do.
*  And that's kind of like going to put a lot of people out of jobs or like make their role in the society like much less prominent, but they just have to like sort of innovate on being useful.
*  Until everybody is not useful and then you can have basic income for everybody but that's the real long term future, so I think in the short term there'll be a lot of wealth inequality created because of.
*  These AI or semi-GI like technologies and that's definitely something to worry about.
*  Yeah well I think that you've put it well the upside is tremendous and.
*  Transition likely to be a little choppy even if we do end up in a good place which obviously certainly join you in hoping for this has been a phenomenal conversation tons of insight I really appreciate it.
*  Thanks for having me.
*  I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go to the website and I'm going to go
