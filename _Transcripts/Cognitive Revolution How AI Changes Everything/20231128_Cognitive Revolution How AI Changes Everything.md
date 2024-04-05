---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 4539s
Video Keywords: []
Video Views: 2797
Video Rating: None
---

# Vercel CEO Guillermo Rauch on v0, AI-Powered Coding, and Software 2.0
**Cognitive Revolution "How AI Changes Everything":** [November 28, 2023](https://www.youtube.com/watch?v=KBGR5NhJikc)
*  My own personal website, I painstakingly crafted every pixel for.
*  And I've been doing front-end engineering for 20 freaking years.
*  Not only was I able to reproduce my entire front-end, my entire app,
*  with just natural language prompts, but where I was really shocked was when I pressed view code.
*  And what I found was better code than what I wrote.
*  And for example, one of the areas where it was objectively better was it was more accessible.
*  The AI produced not just the icon, but it produced the label Twitter.
*  And the label Twitter was only being displayed for screen readers,
*  meaning for people that need assistive devices to navigate the Internet.
*  And that had slipped my mind.
*  It's little details like that that AIs will just, you know, they have infinite memory.
*  Like Mark Andreessen says, infinite patience.
*  They have access to infinite data and they keep getting more and more and more.
*  So it's going to be hard to compete with that.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas,
*  and together we'll build a picture of how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Thornburg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today, I'm glad to get past the recent drama and return to our regularly scheduled programming.
*  And my guest is Gijermo Routch, CEO of Versel,
*  the front end cloud that enables developers to build and publish wonderful things.
*  Gijermo is by any standard a world class software developer,
*  who now, like so many other founders, has recognized the transformative power of AI
*  and begun to pivot his company around it.
*  For Versel, so far, this means releasing both open source template projects
*  that embody the best practices for developing LLM-powered token streaming applications
*  and also developing their own unique pro tool, v0.dev,
*  which allows developers to prompt for and iterate on interactive UIs directly in the browser.
*  But of course, these are just the beginning.
*  In this conversation, we discuss coding assistance as LLM's breakthrough use case,
*  the critical importance of developing the skill of using AI tools effectively,
*  the future of software development by human AI hybrid teams,
*  why and how AI will be incorporated into essentially all software products,
*  which types of AI experiences make sense as GPTs and which are better with standalone UIs,
*  the business strategy that informs AI product strategy,
*  the importance of staying up to date on AI developments and constantly questioning one's assumptions,
*  and why Gijermo believes that open source approaches will ultimately win out in the end.
*  As always, if you're finding value in the show, we'd appreciate a review on Apple podcasts or Spotify,
*  and we always love to see people sharing the show with their friends.
*  Now, I hope you enjoyed this conversation about the future of AI and software development
*  with Gijermo Roush of Versel.
*  Gijermo Roush of Versel, welcome to the Cognitive Revolution.
*  Great to be here, Nathan. Good to see you.
*  Yeah, great to see you too. It's funny, we have known each other mostly from a distance for a long time.
*  I've been following your career as a software developer since you were, I think, 19 years old
*  and kind of a technology prodigy working in Buenos Aires.
*  I don't know if it was your first project, but the first one that I came across was the Moo Tools library,
*  which I used to build a couple web applications back in the day.
*  And since then, you've gone on to found this company, Versel, where you're the CEO,
*  and you really have built a remarkable reputation for just super high quality work throughout the software industry.
*  So I kind of want to just spend a little bit of time setting the stage.
*  I think people, obviously, listen to the show, are very interested in AI.
*  They may or may not have a lot of context on the business that you've built.
*  So maybe just for starters, kind of run me through a few of the themes of your career,
*  JavaScript, TypeScript, performance, deployments, all these kind of great themes,
*  and tell us about the business, and then we'll get into the AI that's coming online now.
*  Yeah, for sure. It's interesting how the dots are connecting.
*  My entire career has been devoted to creating amazing experiences on the web.
*  Versel is building what we call the front-end cloud,
*  which is a way of deploying websites and applications at a global scale
*  that makes these websites really fast and really dynamic.
*  And a lot of that is predicated on the success of a bunch of open source projects
*  that I've been involved with in the past.
*  You mentioned Moo Tools.
*  I was like super early on one of the, I would call it one of the predecessors
*  to some of the greatest technologies that exist in the JavaScript ecosystem today.
*  I was still in Argentina. I became a core contributor to that open source project.
*  That led me to some interesting international opportunities.
*  My first job and my first time leaving the country was with this startup in Switzerland
*  that had just adopted the Moo Tools framework.
*  And then that led to me visiting San Francisco one day.
*  And I actually remember you were one of the first people I met here
*  at Phil's Coffee here in San Francisco.
*  It was an awesome connection to be made.
*  And honestly, open source has been this thing that has created incredible business opportunities,
*  incredible connections, incredible networks of people.
*  And nowadays I work on this project called Next.js.
*  So Next.js, you can think of it as the Kubernetes of front-end.
*  It's this orchestration layer for user interfaces.
*  The way that I explain to non-technical folks is there's this engine underneath Next.js called React.
*  And React created a way of sharing user interface components, almost like Lego bricks.
*  Everything on modern user interfaces from e-commerce to marketing to all of the AI products,
*  I would say, are using these components under the hood.
*  And this has resulted in incredible productivity gains for developers
*  because they no longer have to reinvent the wheel every time they start a new project.
*  But it's also led to this new and emergent class of applications that are highly dynamic, highly personalized.
*  And it's in that context that Vercell has helped power a lot of the big successes in artificial intelligence.
*  We power the user interface and front-ends of a lot of products in AI, like Next.js powers Chagi PT.
*  I found out last night, meeting Mustafa, that it powers Pi.
*  It powers for Plexity. It powers U.com.
*  So it's sort of become this lingua franca of the part of the application that the user basically deals with,
*  the things that you see on your screen.
*  And Vercell is also very invested in the success of the web, and open source is sort of the end-all, be-all platform.
*  There's a missionary side of things for us, which is the web needs to win.
*  Open source needs to win, which is another topic that's super interesting in the context of AI,
*  as we start going into this world of the collision course between proprietary models and open source models.
*  Yeah, no doubt. I'll definitely make a note to return to that in a few minutes.
*  Maybe just for a little bit more context for those that are not web developers,
*  which I think is probably most of the audience.
*  Obviously, to have those leading AI companies using the technology speaks to the quality of the technology.
*  Could you give us a little bit more about the differences?
*  You mentioned productivity gains for developers.
*  Maybe you could frame this in terms of workflows, with or without, before or after.
*  But just a little bit more about why this is so much better than what came before.
*  Yeah, it's super interesting.
*  The way that software on the web emerged is you would go to these providers,
*  and they would give you basically bucket loads of software, monolithic software.
*  You would go to companies like Oracle or SAP, and they would give you basically the fast pass to get online,
*  especially if you were a larger company.
*  But they were incredibly opinionated about this stack of software.
*  So for the business, it was really limiting to just adopt one platform,
*  and that's the end-all, be-all of your technology stack.
*  What's happening now in the cloud that is fascinating is all of the different parts of your application stack have become modular and composable.
*  So there's always a part of the application that the user interfaces with.
*  That's the front end side of the application.
*  That's what Versel is specializing in.
*  And the way to think about us is that we give you the front end infrastructure as a service.
*  We've done all of the heavy lifting of creating the tools, the framework, and the infrastructure,
*  so that if you need to create the next great dot com, you can come to us, and we give you basically all of the building blocks.
*  And then, of course, on top of that, you bring in the knowledge of your business, your brand, your identity.
*  And the interesting part, too, is that you're connecting to this plethora of cloud services and data services that now you can inject into this front end.
*  So it makes the Internet very modular and reusable.
*  So you were asking about productivity gains.
*  One of the key productivity gains of this way of building software is that you no longer have to go all in on a specific solution.
*  You can incorporate services that are off the shelf as you evolve your technology stack.
*  You might have heard of companies like Stripe, like Twilio, and now, of course, OpenAI.
*  These companies are giving you these APIs, which are basically how developers connect systems over the network.
*  And now you no longer have to reinvent the wheel of now this other part of the stack that we call the backend.
*  So Versel tells you this awesome value proposition of focus on the front end.
*  That's where the customer actually experiences your product.
*  You can make it faster. You can make it more engaging. You can focus on that part of the stack.
*  And then the backend, I'm not going to say commoditized because I think that's too heavy of a word, but now it becomes more reusable.
*  It actually becomes more competitive. If you don't like provider A, that's a module.
*  You replace it with provider B.
*  To give you more of an example, we power one of the largest retailers in the United States.
*  We power their dot com, and they have three brands that people know when they go shopping.
*  And I was talking to the chief digital officer that just incorporated Versel into their stack, and he told me,
*  look, this is the last digital transformation process that I need to do because now I've decoupled my front end from my back ends.
*  And yes, I know that maybe the order tracking system that powers my checkout,
*  maybe it's not going to be the one that powers my checkout 10 years from now.
*  Maybe I'm doing Google Pay and Apple Pay today, and maybe in three months I'm going to incorporate Prime Pay by Amazon.
*  It's not to say that things are going to stay fixed, but you no longer have to do this major migrations of software.
*  It almost seems like every time you talk to a company, they're going from platform A to platform B to platform C.
*  So it makes businesses just run better. That's ultimately what Versel is enabling.
*  Businesses run better on the web.
*  And the other side of it is, which connects back to my past and the way that you got to know me, is developer experience.
*  I'm a developer. I taught myself how to code when I was 9, 10 years old.
*  I started very early and I've always had this inclination for using products.
*  And this almost sounds selfish, but developers just love the tools that feel the best.
*  It's kind of like you optimize for buying the best mattress or buying the most comfortable chair at your office.
*  Developers choose the products that feel the best.
*  Software engineering is a very tedious, almost frustrating job.
*  You're always confronted with an error and a failure and the build failed.
*  In building software, the compilation step of software takes a long time.
*  So Versel said, OK, what if we really optimize all those processes?
*  What if we make the developer the biggest advocate, even within the largest organizations in the world?
*  We're talking, for example, the other day I heard a top three world's largest bank migrating to Next.js.
*  I didn't go and convince the CTO of that bank.
*  And in fact, that was my first time meeting them.
*  Their developers were the ones that said, this is a tool that feels great.
*  It makes me productive. It makes me happy. And it's open source.
*  So Next.js is just free software, MIT licensed, and anybody in the world can adopt it.
*  And that's why you find now that increasingly powers a lot of the Internet and especially a lot of the newer products that are coming to market.
*  I remember one day in one of our San Francisco meetings, I remember stopping in the office and just before we went out to the coffee or lunch or whatever,
*  you just did a super quick command at the command line.
*  And it was like, deploy, go, enter.
*  And at the time, I didn't even really appreciate just what a flex that was.
*  But it definitely, that's a very small moment, has burrowed in my memory all these years later,
*  as I've experienced some of the pain that you're talking about in building a software company where the build is up to an hour.
*  And what are we going to do to get it down? And it's like, nobody really wants to do that work or prioritize it.
*  It's kind of not, the customers don't care how long it takes to build, right?
*  Except that the developers are not able to ship stuff as fast.
*  So it seems like every company has kind of wrestled with this.
*  And the solutions that you're building are definitely memorable for me to have seen that very early.
*  That was a pretty long pre-versal, but still a moment that I remember is just like,
*  he's doing something a little different than what I'm doing over here.
*  I'm going to go ahead and start with the first question.
*  So I'm going to start with the first question.
*  So I'm going to start with the first question.
*  So I'm going to start with the first question.
*  So I'm going to start with the first question.
*  Shopify helps turn browsers into buyers with the Internet's best converting checkout,
*  up to 36% better compared to other leading commerce platforms.
*  And Shopify helps you sell more with less effort thanks to Shopify Magic, your AI-powered all-star.
*  With Shopify Magic, whip up captivating content that converts from blog posts to product descriptions.
*  Generate instant FAQ answers. Pick the perfect email send time.
*  Plus, Shopify Magic is free for every Shopify seller.
*  Businesses that grow, grow with Shopify.
*  Sign up for a $1 per month trial period at Shopify.com slash Cognitive.
*  Go to Shopify.com slash Cognitive now to grow your business no matter what stage you're in.
*  Shopify.com slash Cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  At the heart of Vercell, and I dare say at the heart of progress in the modern software world,
*  is the idea of deployment.
*  You have to deploy, you have to iterate fast.
*  And something that I've always been obsessed with, and I'm glad you remember that moment
*  because at my previous startup, when you came to visit our office,
*  I was obsessed with optimizing the deployment pipeline of our engineers.
*  So I created like a mini Vercell at that time.
*  I didn't know, of course, that one day I could turn that into an infrastructure business
*  and it could be a product in its own right.
*  But I had this inclination to if our engineers can make changes faster,
*  they can discover what the customer really needs and really wants faster.
*  Today, the word that we use at Vercell for this is iteration velocity.
*  It's not iteration speed because if you just like do something fast
*  and it's not what the customer wants, you're not going to make progress.
*  If you implement iteration velocity, if you optimize for iteration velocity,
*  it's a speed with a direction.
*  One of the key tenets of the Vercell platform is we get you data about the website that's being rendered.
*  We give you, for example, what we call the speed insights.
*  We tell you how fast we're delivering your website and your code.
*  And there's plenty of studies and data that supports, for example,
*  that if you make your website 100 milliseconds faster, you improve conversion on mobile by 8 percent.
*  For each 100 milliseconds of improvement, this is a study that Google commissioned to Deloitte.
*  So if I give you the data that says, hey, look, your checkout is slow.
*  Look at how you could prioritize this, optimize this.
*  Here's the tools. Here's the insights.
*  Now, that's what I mean when I talk about iteration velocity.
*  So it's not, OK, I deploy fast.
*  It's also about the continuous feedback that makes software improve.
*  If you look at, you know, the all of the companies that people like to talk about,
*  these are companies that are iterating really fast.
*  Chaggpt launched. Chaggpt plugins launched.
*  Maybe Chaggpt plugins wasn't quite the thing.
*  OK, let's get feedback. OK, let's launch GPTs now.
*  It's all about empowering teams to fearlessly iterate.
*  The fear part is also really important because when you're operating at scale,
*  things get trickier, right? You have to be more experimental.
*  You have to have a platform that allows you to roll a change, just a small percentage of traffic.
*  You have to use what we call feature flags.
*  You have to say, OK, let's test it in a small cohort of users first.
*  Let's flag them in.
*  I always give people the metaphor of the best movie studios.
*  Give this like pre-screenings to small groups of people, critics,
*  to get a sense of how they react into the content.
*  So the best software engineering companies in the world, that's how they do everything.
*  They're always launching small experiments or looking at their business metrics.
*  They revert experiments automatically.
*  Now, imagine that your company is trying to break through,
*  whether you're a startup company or whether you're a big company that's going through a digital transformation.
*  Are you going to re-implement all this infrastructure from scratch?
*  Are you going to hire?
*  You know, your competition sometimes is Google and Amazon, especially if you're in e-commerce.
*  Are you going to go through the 20 years of iterations that led to these best practices?
*  Or you can just sign up for a resell and you don't even need to talk to a salesperson.
*  And you can now deploy a product and get a sense of how different software development can be.
*  Let's get to the AI part of this story.
*  Obviously, over the last couple of years, it's become increasingly undeniable
*  that there's sort of a new paradigm emerging.
*  And curious to hear how you as a, obviously, busy technology company CEO first kind of caught the bug.
*  And maybe also a little bit about kind of how you're seeing your companies across,
*  your customer companies across the spectrum starting to react to it.
*  I think one thing that has been really interesting about this technology wave is that
*  incumbents are not sleeping on it nearly as much as they might have slept on some of the earlier waves.
*  Absolutely. So I'll tell you how I'm glad you asked how I caught the bug because
*  when I first tried AI based code completion with Copilot.
*  Now, as I mentioned earlier, I'm at Front Engineer.
*  I've been writing code for 20 years.
*  I love writing code, but now I run an organization with over 450 colleagues.
*  We are at a very significant scale.
*  We have a senior executive team. I don't have as much time to code anymore.
*  But when I used generative AI to basically write code, something got dislodged in my brain.
*  And this was before Chad GPT.
*  And the reason is, first of all, I was short on time.
*  But also I have a ton of experience to be able to like pattern match and see if what it's suggesting is very valuable or not.
*  And if it's a distraction or not.
*  And if it's just a random result looked up from a database or truly insightful or not.
*  And then I realized that it was a one way street.
*  And now that that category of product has only improved since then.
*  But what I realized was in the way that basically AI has come to programming is you type and then what we call ghost text shows up by right next to what you typed.
*  Right. And the ghost text is a suggestion.
*  And you can accept it or not.
*  My framework at the time was we are going to need a ghost text for every product in the world.
*  This is just step one. It's in the fact that step one that was programming makes this insight even more profound because programming is a really difficult task.
*  So at the time I was thinking any any time I'm writing anything, I'm going to need that completion.
*  That suggestion from an AI.
*  And of course, I didn't know exactly what's going to take the shape of this conversational chatboss like Chachi BD.
*  But it indeed happened nowadays.
*  Even when I'm writing a tweet, I ask the AI to proofread it or to maybe help me rephrase something.
*  When I use notion, now I use notion AI.
*  In fact, when Copilot came out and I'm a small investor in notion, I remember reaching out to their CEO and saying like we need to figure out how to add ghost text to notion.
*  That was my of course, it didn't quite it took the shape of ghost text in the in the document editor.
*  It's more like a slash command and it's a context menu option.
*  But it turned out to be a very positive development even for them as well.
*  So our thesis at Vercelli is the speed at which you deliver this user interface is a skin.
*  So there is a huge opportunity to do the same thing for user interfaces.
*  So how can we give you a UI based on your intent and we're completing your thoughts basically.
*  And so we built this product called VZero.
*  As the name implies, it generates the first version of your user interface.
*  And it's also inspired not just in how Copilot sort of led the way, but also mid journey where there's something deeply creative about creating a web website with interface.
*  And we should be responsible for giving you options when you are in that creative process.
*  So VZero, I can come in and I say, please give me a sign up form for my e-commerce website.
*  And then we give you three or four options.
*  And then we get you into this loop of iterating together with AI on all the refinements and adjustments that you want to make to the UI.
*  And the really cool thing about it is we produce production grade code.
*  We're constantly optimizing the AI to generate something that you can actually ship and incorporate into your code basis.
*  So when I talked earlier about the kind of customers that we serve, we serve customers that are operating a very large scale.
*  In fact, I always tell customers, if you're just building your uncle's restaurant website, Vercell is probably overkill.
*  It's like going to AWS if you just need to sort of file where you instead should go to Dropbox.
*  So we had this requirement of the UIs that we generated with this AI.
*  They need to be at a level of maturity and quality that our customers will ship them into their products.
*  And it's been amazing so far to see what folks are doing with this. It's shipping UIs into production.
*  We've done hundreds of thousands of generations on behalf of a very small group of customers that have so far been accepted into the waitlist.
*  And yeah, we're very excited to transform how people think about creating for the web with AI.
*  Yeah, it's cool. I've had a chance to try it out a little bit and a couple of different aspects of it that I'm interested to explore a bit more.
*  I guess, again, just for people that maybe don't have a huge background in software development or in web application development,
*  I recently had this experience where, and I didn't have access yet, so I had to do it a bit differently, but I'm building this app at this company,
*  Athena. Listeners have heard this. Executive Assistant business. We're trying to create an internal chat that's kind of like chat GPT,
*  but has like an access to a long lived client profile that you can kind of query and update directly from the chat.
*  Well, a lot of our users are not that savvy yet with AI. And so we got the idea of what if we added a prompt coach where when you put something in,
*  then it can also kind of look at that and say, are there any prompting best practices that you may have neglected to use here that could help you get a lot better performance from the AI?
*  So this is kind of a classic new component for the overall web application. I've already got kind of the mainframe where I'm doing the chat and I've got the one side bar where I've got my history,
*  very chat GPT like, and I want to put this other component in the other lower corner to kind of pop up and say, hey, I've got some feedback on what you just did and how you could make better use of AI.
*  And what is very interesting about this React framework, which I'm not an expert in, but you know, dabbled in a bit, is how it does make it pretty easy to just kind of come up with a new component and kind of drop it into its place,
*  tie it into the rest of the application. And, you know, even I wasn't the original developer on this application and I don't have a ton of React experience with the help of GPT-4,
*  I was able to like create out of nowhere and integrate this new module in just like a few hours. That's pretty awesome. Now, the experience itself, I want to break down just a little bit of like some of the decisions that you've made because
*  notably to me, it does kind of read as a pro tool. And I think one of the big, I'm not sure there's like a either or on this, but there's a lot of talk obviously about helping people do stuff that they couldn't do before.
*  And then there's also a lot of talk about like, you know, improving the productivity of professionals, you know, in whatever it is that they're already doing. This to me feels as I was using it felt like a tool that was like a tool for the developers, you know, as you said, like you're obsessed with developer tools, so that makes sense.
*  I wonder how you think about kind of the future of software development, you know, through the lens of this product. Is there something also that you think of as like expanding who can do this stuff? Or are you like intending to be still focused on that core professional developer profile?
*  Hey, we'll continue our interview in a moment after a word from our sponsors. AI might be the most important new computer technology ever. It's storming every industry and literally billions of dollars are being invested. So buckle up.
*  The problem is that AI needs a lot of speed and processing power. So how do you compete without costs spiraling out of control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI. OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds offers one consistent price instead of variable regional pricing. And of course, nobody does data better than Oracle. So now you can train your AI models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, eight by eight and Databricks Mosaic, take a free test drive of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive, oracle.com slash cognitive.
*  If you're a startup founder or executive running a growing business, you know that as you scale your systems break down and the cracks start to show. If this resonates with you, there are three numbers you need to know 36,025 and one 36,000.
*  That's the number of businesses which have upgraded to NetSuite by Oracle. NetSuite is the number one cloud financial system, streamline accounting, financial management, inventory, HR, and more. 25. NetSuite turns 25 this year. That's 25 years of helping businesses do more with less, close their books in days, not weeks, and drive down costs.
*  One, because your business is one of a kind, so you get a customized solution for all your KPIs in one efficient system with one source of truth. Manage risk, get reliable forecasts, and improve margins. Everything you need all in one place. Right now, download NetSuite's popular KPI checklist designed to give you consistently excellent performance, absolutely free, and NetSuite.com slash cognitive. That's NetSuite.com slash cognitive to get your own KPI checklist. NetSuite.com slash cognitive.
*  Yeah, I love this question because I have a huge amount of respect for the task of software engineering, especially when you get to products. Like the products are taken over the world, right? Like when you look at the amount of effort that went into the front end code base of a product like Gmail, it's non-trivial to get there.
*  And what I would say is that V0 is helping people up level in many ways. So if I'm very seasoned, I might be very seasoned in backend development. I might be very seasoned in another language. But the lingua franca of the internet, of the web, of the front end is JavaScript and TypeScript.
*  And I just don't know what all the best practices are. So I know how the systems work on a high level. I know about how programming languages work. I know about how code sort of fits into the context of a deployment pipeline. I might even know just the basics.
*  But what AI is helping with is bringing the enormous corpus of knowledge of everybody in the world. And it's also being remixed with what Vercell knows are the best practices for creating web interfaces. So it's almost like this confluence of the large language models have become experts, because they've read every single piece of knowledge about React and how it works.
*  They know about styling websites. They know how to produce the right syntax most of the time. That's where the other part of software engineering comes in, correcting for the errors of the AI. And then we have this augmentation, fine tuning, retrieval, etc. All these techniques where Vercell can say, okay, V0 should know how to create an accessible web interface.
*  Here is the things where we can orient the AI. And the interface should work well in a mobile device and an adaptive desktop screen. So we can continue to sort of fine tune and improve the output in that direction.
*  So it's an accelerant of learning for a lot of people. Even for professionals, I'll share an anecdote that is kind of mind blowing. But the moment that for me V0 very clearly became in my head, the future of UI development, or at least a big part of the future of UI development was my own personal website,
*  I painstakingly crafted every pixel for. And I've been doing front-end engineering for 20 freaking years. So I said, okay, I wonder if under my creative direction, V0 could arrive to the same result. It was a way of me giving feedback to the team about V0. I was like, okay, I'm going to try it out to reproduce my website.
*  Not only was I able to reproduce my entire front-end, my entire app with just natural language prompts, which for the audience, the way to think about it is like I said, okay, use a gray background, center it in the middle of the screen, give me a list of blog posts, on the top right, add a link that says about, and add a little icon for Twitter so that folks can follow me.
*  So I just spoke in these terms, and I arrived to a very satisfying result, visually speaking. But where I was really shocked was when I pressed view code, so you can go and see the code that V0 has generated. And what I found was better code than what I wrote. So I was like, okay, one perspective on this is like, okay, this guy is a little rusty, but he's got a lot of code.
*  Most of the code that I wrote for Vercell is being rewritten by really seasoned engineers that are specialists in each domain. But I can tell when things are objectively better. And for example, one of the areas where it was objectively better was it was more accessible. So if I remember correctly, it was the Twitter link, and I was able to see the code that V0 has generated.
*  And that had slipped my mind. And it's literally like, okay, so I'm going to go and see what's going on. And I'm like, okay, so I'm going to go and see what's going on. And I'm like, okay, so I'm going to go and see what's going on. And I'm like, okay, so I'm going to go and see what's going on. And I'm like, okay, so I'm going to go and see what's going on. And I'm like, okay, so I'm going to go and see what's going on. And I'm like, okay, so I'm going to go and see what's going on. And I'm like, okay, so I'm going to go and see what's going on. And I'm like, okay, so I'm going to go and see what's going on. And I'm like, okay, so I'm going to go and see what's going on. And I'm like, okay, so I'm going to go
*  and see what's going on."
*  And it all sits in this folder because now they have access to the computer.
*  And even having access to touch принters. Because they have access to so much data,
*  and they cancode to the NPCs, and everything is so easy. And there's always some little details like that that
*  a eyes will just you know, they have infinite memory,
*  exercise a skill of working with these AIs because it's not all natural and there's a
*  skill to it as well. There's a skill to prompting, there's a skill to understanding what it's
*  capable of, understanding what gives the AI more trouble.
*  The other day I had this awesome experience where I think you might have seen this on
*  X, someone posted about replicating Angry Birds with AI. Did you catch that? And I was
*  very, very surprised that they got in there, especially when I used the game. And so I
*  actually immediately DM the gentleman that wrote that demo and said, okay, I really need
*  to dig into the details here, like how much of this game was actually written by AI. It
*  turned out to be all of it.
*  One of the things that I took away from that conversation that was really interesting was
*  he told me about very specific things during the development of the game that the AI could
*  not understand, which is not reason about. For example, the passage of time. When you write a
*  video game, you have to have some state about the evolution of time. For example, you're
*  evolving the position of the character and you're doing simple math or doing collision
*  detection and things like this. Chagy Bidish is not able to reason about that. He can do
*  incredible things, but that particular aspect of game development, which is not.
*  So now think about this from the skill building perspective. It's not that humans are not going
*  to need any skills. It's going to be very useful to develop the skill of where the AI falls short
*  and when to best use it. Our conclusion with V0 is that it's really awesome to fix this problem
*  that engineers have, which I call the empty canvas. To your point, I need to create a new page on my
*  website. I need to create a new app. You almost face a writer's block. You start with today,
*  you start with a blank text file. That's how most engineers work today. I think we're going to look
*  back on this and we're going to be like, those were the dark ages of development. It's amazing
*  that engineers almost started from scratch every time they had to create a user interface.
*  So that's where V0 sort of comes in and gives you that head start.
*  You mentioned the skill. I wonder if you have any other kind of specific practical tips. One thing
*  that I have found to be very useful in that I want to kind of unpack the future of workflows
*  and just how much productivity is maybe going to grow. But one thing that's really useful for me,
*  I'm tentatively calling coding by analogy, where I basically will take, and I usually go to chat
*  GPT for this. I may be working in VS code or perhaps I'm in a notebook somewhere or whatever,
*  but most of the time chat GPT is the best. So because it's not integrated everywhere and it's
*  first best form, I go to it and I'll bring usually a snippet of working code. Maybe it's a class that
*  I already have that I want to add a method to, or a class that implements something, a caching
*  strategy or whatever that works for me that I want to use again in another new thing that I'm doing.
*  Maybe it's even just documentation or examples from documentation. And I kind of say,
*  here's what I have and here's what I want. And I find that giving it something that I have is really
*  useful for then getting something that I want that kind of follows whatever established things
*  that are working. So I guess for starters, do you have any kind of points of skills that you've
*  picked up that I should know about or that others should emulate? I use a lot of AIs. So one of the
*  things that I'm developing more and more conviction about is you set skills, I think is an awesome
*  way to put it. I think we're going to go to different AIs for different skills.
*  And the reason for this is that each domain has to account for the nuances of how to best
*  solve for different problems, how to do error correction, how to limit hallucination,
*  how to keep information fresh. So for example, if I have to learn something that I am confident
*  is very real time and is seeing very frequent updates, I might go to something like perplexity
*  I find myself when I need to summarize a very recent trend that people are talking about,
*  I go to that tool. The other day discovered this platform called metaphor. And what they specialize
*  in is crawling the web and exploring it with chat GPT like prompts. So it's really useful as a
*  replacement for Google searches where you literally don't know the keyword. You know that is the
*  famous joke about like, what's that song that's like duty duty daddy daddy and like you're like,
*  what? But an AI can figure it out with very little signal and AI can figure out so that
*  tool is really good at like converting sparse data and signal into a list of results that are
*  also very fresh for programming. To your point, there's things that chat GPT is very good at and
*  there's little techniques there. For example, something I learned recently is you shouldn't
*  hesitate to include the entire error message that you're getting from your compiler or tool,
*  give us as much context as possible to the AI about your problem. And this is, it sounds obvious,
*  but it's super counterintuitive because we're used to searching with Google with keywords.
*  And you just enter two or three words. But the more context you give to the AI,
*  the better. It's almost like you're influencing how it navigates its neural network.
*  You're giving it those significant tokens so that it can create better neural connections.
*  It can be something small like responding with a question and including the question mark
*  is sending the AI in a different direction than I know if you've noticed this failure mode where
*  you ask the AI, what is two plus two? And it says four. And he's like, no, no, it's five.
*  It's just, yes, sorry, it's five. Clearly you have to, what I've learned is that you have to
*  sort of understand the make, if you can, of course, the underlying mechanism, that next token prediction
*  mechanism, and that the AI is just trying to like work off of what you're giving it.
*  And so if you phrase it as a question, then it's that quote unquote overconfidence is not
*  going to happen as, or you're going to reduce the likelihood of that overconfidence of that
*  hallucination happening. And the same happens if you again, upload more context. And this is why I
*  think OpenAI is going with this GPTs and system prompt concept. Because if it's always fresh,
*  and it's always starting from scratch, it's very difficult for it to be helpful to you.
*  And it's also very expensive, by the way, because this AI is said to be extremely powerful.
*  They have to have a very high reasoning power. I attended recently last night, in fact, an event
*  where Satya Nadella was speaking and he was saying, when you evaluate large models versus small models,
*  would you, you know, in terms of always using a large model, like would you cross the street
*  with a Ferrari? So the way to think about it is when we use GPT-4, we're using the Ferrari.
*  It just so happens that because it's so powerful, it can be useful with very little context. But
*  again, the more you give it, the more quality you get back. When it comes to programming,
*  I'm also finding there's very interesting resources that are focusing very deeply on
*  programming subjects. There's this company called Find.com, P-H-I-N-D, that is focused
*  very specifically on indexing developer resources. I find that to be very, very interesting.
*  I go there sometimes when I have to search all of the documentation of the internet,
*  especially when I'm working on integrations or my teams are working on integrations.
*  And I need to have a high degree of confidence that the AI has looked at very recent developer
*  documentation, is spanning many, many, many different resources. It's been super useful.
*  Imagine that you're saying, like, give me pros and cons of technology A. If you ask that to
*  chat GPT with a cutoff date of 2021, maybe you're going to be misled or maybe it's going to be out
*  of date. And yes, it's getting better, but it's never going to be as fresh as Google. Now, if you
*  turn on web browsing, it's going to use Bing. So the challenge there is also very interesting,
*  because Bing has all the SEO games and there's only so many results that it can consider.
*  So I'm finding the products that are indexing developer documentation to be really helpful.
*  And last but not least, I'm also really bullish on this idea of companies incorporating their
*  own chat bots in their own experiences. So we're seeing that with Shopify. Shopify.com.
*  They're basically going to include a, they call it like the copilot for merchants,
*  which is going to be an experience is always in the website. So this is, of course, I'm now talking
*  my book because one of the strategic bets that Vercell is making is that everybody's going to
*  incorporate AI into their products. So it's not just about V zero and helping you create user
*  interfaces. We're also betting that every product in the planet is going to become an AI product in
*  some capacity. So we've built a lot of templates and a lot of technology to very quickly help you
*  develop these AI integrations. So if you go to SDK dot Vercell at AI, you're going to see our
*  documentation for basically what is the easiest way to add AI to an existing product or a new product.
*  And in my bet will be that a lot of folks are going to be adding this assistance to their
*  experiences. You're going to be able to ensure that the information is up to date. You're going
*  to be able to better engage your customers. So here's where I also encourage folks to be smart
*  about their businesses. You can't just sit on the sidelines and wait for a chat GPT to do everything
*  and just train people to go to one website instead of yours because you want to prioritize the direct
*  connection to your customer. And again, you can build better AIs. We have all the tools necessary.
*  We have the rags. We have the LLMs. We have the fine tuning. You too can incorporate AI into your
*  products. And that's the better we're making. I love your maybe just a little bit more about this
*  kind of when to go the GPT route. Obviously, this is all very fresh. We're just talking
*  just a couple of days after the OpenAI dev day. And I think one question a lot of people are
*  faced with coming out of that is like, should I make a GPT and try to put my offering or my
*  know-how or whatever into chat GPT for people to use there? Or should I try to bring the AI
*  through essentially the sort of isomorphic assistance API to my own product and have people
*  kind of use it there? It sounds like you have, first of all, kind of a general sense that like,
*  for strategic reasons, most people should at least try to bring people to their own
*  products. I also see in the vZero experience, at least one other kind of
*  rationale, which is just that in the context of that particular product, obviously, there's a lot
*  of different versions of this, what you are creating is not just text. What you are doing is not
*  easily represented in kind of the chat GPT token streaming. Chat GPT could stream you a component,
*  react component, but to actually render it, to be able to put your mouse over and see the dynamic
*  changes of it, that's not something that, at least in the immediate term, and who knows,
*  but at least for now, that's not something that they even seem to be approaching.
*  So the different experience when you're on the vZero product is that you prompt and you wait a
*  second and then it's there and it's kind of tactile immediately for you. So I see that as being
*  another big reason that you would bring a assistant to your product, as opposed to like
*  stuffing your product into the assistant. But any other kind of high level or principle or guiding
*  thoughts on that? There's two levels to this. I mean, I approached the product and technical one
*  and I'm going to give you the business one. I'll give the business one really quickly out of the
*  way, because it's kind of fun. I mentioned that Vercell serves a lot of the largest e-commerce
*  websites on the planet. Companies like Under Armour and Chico's and many other notable brands.
*  Those companies, when they faced the challenges slash opportunity of going online,
*  they could have just given all their inventory to amazon.com.
*  So that's where the metaphor starts with like, Chaggpt and the GPTs. Do you want to retain the
*  direct connection to your customer? Or do you want to be a product in somebody else's shelf?
*  So that's the kind of like a strategic question that you have to ask yourself.
*  Now, what's interesting about that example is that in a lot of cases, the answer is both.
*  So I'll give an example that's probably wrong, but let's say that I'm Casper mattresses.
*  I don't know if they sell on the Amazon marketplace, but maybe they sell on amazon.com
*  and you can search for Casper. And maybe they have casper.com. So sometimes the answer is both.
*  So that's kind of like the business framework to think about. But I love the sort of technical
*  nuance that you introduced because I think it's completely spot on, which is what happened also
*  with Amazon is that the visual medium is extremely limited. I don't know exactly how the marketplace
*  thing works, but I imagine it's like, hey, upload four photos. We have one carousel here.
*  All the product description pages look the same. And you can upload your description,
*  which is plain text. And that's how we ship your products on Amazon.com.
*  And the way that GPT works is very similar. It's okay. These are the things that we can do for you.
*  We can render a little, we can render a snippet of code. We can render some bold italics. We have
*  these constraints. It all has to fit in within our UI. So it feels to me like history repeating
*  itself. It's going to be very limited. I have no doubt that you are going to find lots of use cases
*  for it. But to your point, a product like V0 needs a lot of visual and UI flexibility. It's only going
*  to get more and more sophisticated over time. So you need that creative freedom. You need that
*  front-end freedom. And that's exactly a bet that Versa is making. I think we're going to see a lot
*  of verticalized AI assistance. Some of them are going to be integrated into existing products.
*  Some are going to be new products that hit the market.
*  An example I'd love to give is the new Bloomberg terminal. What would that look like now that we
*  have AI? Another one is anything about... I used to go to Google a lot to say,
*  my wife is pregnant. What is preeclampsia? What is this? What is that? Maybe there will be new
*  experiences for healthcare that are AI first. That again, you need a completely different medium
*  for how to present information, even for regulatory reasons. So my bet is that, yes,
*  there's going to be GPTs, of course. And there's going to be a lot of products that are standalone.
*  And to your point on the technical side, need more of that visual freedom and flexibility
*  out and break out of the constraints that the Chagypti product imposes.
*  Everything everywhere all at once is my mantra for some of these. Let's talk a little bit about
*  the future of software development. I mean, this is really your wheelhouse. You've helped define
*  over the last decade significant parts of what current software development looks like.
*  I would say I personally get a multiple X speed up in terms of how quickly I can execute a project
*  to working. I'm not that great of a coder. GPT-4 is definitely a better coder than me.
*  The fact that it is even occasionally able to do something that you didn't do is super impressive.
*  And I kind of wonder, how far does this go? And there's, I think, a lot of different visions
*  we've had a couple of folks from Replet on the show, and they have a very distinctive vision.
*  But I want to hear, what's your vision? Are we still writing code, kind of character by character?
*  Does that all go away? Does it become kind of prompting and management? Are we talking about
*  sitting on tops of towers of agents who are doing all the work? My crystal ball is real foggy,
*  but maybe yours is a little clearer. Yeah, I think to some extent, everybody's foggy.
*  So I want to preface this by saying, you know, the future is in flux right now. Every week,
*  you have to re-evaluate your assumptions. That's the best operating model right now. Why? Because
*  the models are becoming more capable, the context windows are changing, the fine tune opportunities
*  are changing, the architectures might improve. So every week, my advice is re-evaluate your priors,
*  try to get a better and less foggy understanding of the future.
*  I'll give you a couple of frameworks that I have in my head about the future software development.
*  One that is kind of a provocative idea, maybe wacky on some levels, is a lot of folks have
*  read the very predictive and prophetic essay by Andrew, Andre Carpathi called Software 2.0.
*  So Andre was the lead of Tesla AI, a pioneer in deep learning. Now he works at OpenAI.
*  So what he defines as Software 2.0 is basically the new wave of software that is... So that's
*  how I give the people the metaphor. It's more like cooking than engineering. Instead of writing code
*  and classical algorithms and data structures, you use data. You mix it up. You train neural
*  networks. You train almost like fixed pieces of code because the architectures are pretty fixed.
*  We evolve them over time, but the human code has already been written. It lives in frameworks
*  like PyTorch and TensorFlow and JAX, et cetera. And then you throw data and compute at it.
*  We're mixing this huge pot of soup of what ends up being code, but we don't interpret and read
*  that code. Folks are always pointing out that it's incredibly difficult to understand.
*  There's an emergent field of mechanistic interpretability of neural networks,
*  but it's really difficult to understand why they work and what the neurons are responsible for and
*  things like that. So those are the broad characteristics of Software 2.0. Software
*  1.0 was the opposite. Software 1.0 is all about explainability. It's about becoming experts in
*  algorithms and data structures and programming languages and whatnot. And the most exciting
*  thing that happened before this wave of AI was cloud computing. So I draw this connection between
*  Software 1.0 and Cloud 1.0 and Software 2.0 and Cloud 2.0. It's really interesting because
*  when AWS and Google Cloud and Azure all came out, let's call that Cloud 1.0, they also had
*  these artifacts that you were using like the virtual machine EC2, the object storage with S3.
*  And now on Cloud 2.0, we have different services. We have the vector database. We have the LLM.
*  We have the indexing pipelines that connect these two. We have the retrieval method. So we have
*  all these new services that are native to, let's call it the Software 2.0 wave. That's broadly how
*  I think we're entering this 2.0 world where it's not that 1.0 ceases to exist. All that stuff is
*  still very important. But think about it as that was our launch pad into the future.
*  So one of the things that technical leaders and CIOs and CTOs should be asking themselves is that
*  how much are we investing in the 2.0 paradigm and the 1.0 paradigm? And of course,
*  Vercell has a horse in this race. Our argument is infrastructure is not your business. Offloaded
*  to these platforms like Vercell, we already hire all the infrastructure engineers. We did all the
*  heavy lifting. Focus on your product. Focus on bringing the 2.0, Software 2.0 features to market.
*  That's kind of my thinking of like, when I think about myself, when I think about our investments,
*  why we're creating VZero is I want to aggressively move into this Software 2.0 world.
*  I think it's all very reasonable. Now I'll go into more like the
*  wacky stuff that could be a prediction. I think the fact that all of our attention,
*  no pun intended, with Transformer architectures and all of our money and all of the consumer
*  excitement and all of the venture capital is going to 2.0 technologies might ossify
*  1.0 technologies. What do I mean by this? So, ChatGPT is particularly good at writing some
*  programming languages. It's really good at JavaScript. It's really good at Python. Is it
*  good at wacky-de-wacky-lang that has maybe 100 documentation pages on the internet? No.
*  It might create this flywheel of as we continue to focus on the next layer of computing,
*  it's not that there's going to be less innovation on 1.0, but because it becomes more AI automated,
*  it almost reinforces the choices that we've already made in that layer.
*  There might be an argument for there's going to be stabilization, let's call it,
*  of that layer of the internet. For good reason, I think. I think you asked earlier, why are we
*  excited about VZero is because it's going to broaden access to more people to create software
*  and to have an impact. They're not going to have to learn that deep stack of software that came
*  before. There are metaphors that validate this hypothesis. JavaScript is really popular because
*  it doesn't deal with memory layouts and offsets and pointers and pointer arithmetic. It automated
*  all the memory management away. I think there's going to be a wave of AI technologies that automate
*  the creation of software away, where to your question concretely, writing code is less
*  important, period. Again, it doesn't go away, but our attention moves and our attention goes elsewhere.
*  The reinvention of the wheel of software 1.0 starts to give diminishing results and diminishing
*  returns and it requires more investment and the AI helps you less with those techniques.
*  So that's my broad view. I think it's very... So who wins? I think people coming into the
*  industry right now. It took me a long time to learn and become an expert in all this stuff.
*  Now, someone that has ChaiGBT can get up to speed a lot faster. It's a reality. So very good time
*  to start creating products today. You're going to have tools like ChaiGBT and VZero and just
*  endless amazing tools. I think both the startups and incumbents win. Startups are going to be able
*  to create these 2.0 products that are so different from what the incumbents are offering,
*  from a visual point of view, from what they do, from the customers they engage,
*  that it's going to be hard for the big company to pivot into that space.
*  Now for the incremental AI additions, like we talked about, it's smart for you to add an assistant
*  to your dashboard, to your console, to your website. That's going to happen for the incumbents and they're
*  going to move really fast and they're going to throw a lot of dollars at it and they're going to see results.
*  But obviously I'm a startup guy and I'm really excited to see what is the Uber and Airbnb of this cloud 2.0 face?
*  Because without the cloud, companies like Dropbox and Airbnb, without the cloud and mobile,
*  those companies would not have existed. What I'm excited about is what are the companies that would
*  not exist without these foundational 2.0 techniques like large language models,
*  diffusion models, etc. It seems like we're just starting to get a glimpse of a little bit of that.
*  Things like character, AI and replica and these kind of virtual interactions come to mind first.
*  AI-first social networks are definitely going to happen. I'm excited to see who cracks that nut.
*  But it's a perfect place because social networks always have this chicken-egg problem when launching.
*  How do you feed content? How do you create engagement? There's got to be other people
*  at the bar for you to be interested in it. Of course, also content producing is hard.
*  Arguably TikTok is that first AI-first social network, right? But it's because they're CEO
*  or CTO. I can remember one of their co-founders, literally a deep learning pioneer. Now that it's
*  democratized, I think we're going to see the Mark Zuckerberg of social networks in AI where Mark,
*  like me, was a PHP developer and was orchestrating those software 1.0 technologies. There was a
*  database here. He brought in MySQL. He brought in PHP. He deployed the website and he made something
*  happen. I think we're going to see again another wave of innovation that is more like grassroots
*  like that because you can use all these awesome off-the-shelf services that I talked about in
*  the beginning of the call where there's just so much has already been built and you can leverage
*  the APIs. You don't have to reinvent. You don't have to take a PhD in machine learning to have
*  an impact in this new world. Open source obviously has been a tremendous enabler for all sorts of
*  companies, projects, individuals in software 1.0. It's hotly contested in 2.0. I'd love to hear the
*  base way that you think about it and then specifically how you engage with the worries
*  that people have that like, hey, we don't even really know what these things can do yet. So it's
*  maybe a little premature to put the most powerful ones out into the open for anybody to use.
*  The sound bite here is never underestimate open source. It's the worst mistake. It's been done.
*  Microsoft once upon a time underestimated all the memos are public. Now they've learned their lesson
*  with Azure. They're doing a great job with open source and GitHub. Of course,
*  it's costly and it's short-sighted to bet against open source. So if you look at Versel,
*  I started the company with this open source project, Next.js.
*  What's amazing about open source is that open source builds on other open source.
*  Underneath Next.js is React, which is this engine that Facebook created and open sourced.
*  It's a marvel of engineering. Next.js in the beginning wasn't the most sophisticated
*  technology in the world. Of course. We were literally two or three persons startup when
*  we started that project. Maybe a four person startup when we started the project. I remember
*  I had a meeting here in SF with a CTO of a very popular real estate website. He came to our office
*  and he was like, oh man, I just wish Next.js was more mature in this regard, this regard.
*  You know what? I can't use it. I have to build my own. Maybe at the time that was the right call
*  for him to build his own. He went sort of the proprietary route. Fast forward a couple of years,
*  we've captured every single major player in online real estate is now built on Next.js.
*  You can never underestimate how quickly open source gets better. It starts out looking,
*  it's like that famous meme of the little doge and the super muscle doge. It starts looking weak and
*  fragile and less powered. I want to offer that framework and metaphor for Lama versus GPT perhaps.
*  It's easy to point out how code Lama is not as good as copilot or how Lama might not be as
*  powerful as GPT-4, but it's also dangerous to assume that it's not going to get better.
*  Here's one key way in which it gets better. In the early days of Next.js, CTOs would come to me
*  and tell me that the best feature of Next.js was that they could go to the internet and Google,
*  and they would find problems and solutions for Next.js issues they were having.
*  When you go proprietary, you're not leveraging this massive ecosystem of resources and knowledge
*  and intelligence, and it's really difficult to partner. It's really difficult for someone in the
*  hardware space to build the best chip to execute an infer GPT-4 because they don't have access to
*  it. What's going to happen is that the garage startups that are thinking about the chips of
*  the future, they're going to download Lama first, and they're going to battle test their technology
*  against what's available. I call this the unreasonable effectiveness of open source-based
*  business development. Business development is not done with phone calls and meetings and contracts.
*  It's done by doing a Git clone of a repository. What I think can happen is that, yes, today,
*  open source is not as good, but over time, it becomes this force that is just unstoppable.
*  Now, the one adversary or potential slowdown to this is, of course, regulatory capture.
*  There are people right now that are rightfully concerned that folks want to stop open source
*  training and development. Another thesis against this is that, and actually, I think this one is
*  really interesting for folks to ponder, is that the model is like the engine of the AI platform.
*  There are other technologies that are sitting on top that expose that model to the internet.
*  So think of it as if you're technical as a distinction between an API
*  and the internal implementation details of that API. What's happened over the past decade is that
*  over long periods of time, APIs win because they provide this ease of use and flexibility to
*  developers. That's why companies like Stripe and Twilio become so useful. It's because I don't go
*  to MasterCard as my implementation detail. I go to Stripe and say, hey, please make this payment
*  happen. So I think what folks in the open source world need to reckon with is we have to provide
*  utility on top of the open source model. But again, this is where startups will have tremendous
*  opportunities. And this is also an area where Vercelli is investing heavily, where I mentioned
*  earlier the connective tissue between the product and the AI model. There's a lot of
*  white space there. And we have this product called the AISDK that helps you automate a lot of that
*  wiring that you need to do to the model. So I think over long periods of time, open source
*  always wins. And I hope that it's also true for the AI revolution. I just have to ask one follow-up
*  question. I broadly agree with you, certainly in the history of the software industry. I think that
*  narrative is hard to... Basically, incontrovertible at this point. And I wouldn't bet against long-term
*  open source also coming to do a lot of amazing things in large models as well. Maybe a little
*  bit different just because if you're talking about something where you got to put billions of dollars
*  down, then it may change the analysis of like, do we really want to open source this? A few folks,
*  a few metas out there that can put down that kind of investment and then just turn it loose.
*  But I guess bigger picture, zooming out as far as you can, it seems to me like we have no idea how
*  far this goes. And are we going to have a totally transformed society? Are we going to have AI-run
*  corporations? Are we going to have... The top worry among the AI safety people right now is
*  some of these models are starting to get to the point where they can help you design a new pandemic
*  agent. Obviously, if we had a language model that could tell anybody how to create a pandemic agent,
*  and then we put that in everyone's hands, somebody would probably use it for bad.
*  So do you have a theory of how we get all these upsides of the open source,
*  which again, I think are undeniable without also running unacceptable risk? And I would not ask
*  that about any other technology except for this one. I think AI is an accelerating agent. I think
*  it's going to amplify all the good and all the risks as well that exist within society. So
*  as an example, there's clear product market fit in this AI friends. You mentioned character AI,
*  replica, there's a bunch. That's not something that AI created. It was product market fit,
*  unfortunately predicated on a loneliness epidemic that exists. And the fact that folks are,
*  they just don't have as many deeply human connections anymore. And so,
*  that kind of already existed. That was the case. There's been lots of studies about the
*  effects that social media and Instagram has had on teenagers and the psyche of people and so on.
*  So now you bring AI and what do you get is acceleration of those effects. And that's where
*  you have to be very cognizant of what are the risks, what are the negative effects. And hopefully,
*  this time around, we're better prepared to face those and address those compared to the previous
*  wave of let's call it cloud 1.0 and social web and so on, where maybe there was just pure,
*  unabated optimism and euphoria and nothing can go wrong. I think we're wiser this time around.
*  As far as AI's running businesses, I think so. I think so. I think so. I think so. I think so.
*  As far as AI's running businesses, I think so. I think so. Because I think it goes back to that
*  human in the loop. Today, coding is no longer just people. It's AI's are doing a lot of the coding.
*  I think it would be a mistake to say, oh, no, no, no, the job of X and Y is only human. It's
*  always going to be a hybrid. That's also going to introduce risk as well. Just like
*  any sort of technology has brought risk to the transformations that we saw from how we used to
*  do business to now. Impersonation is a good example. One of the risks that we face from cyber attacks
*  is folks are constantly trying to impersonate me and other leaders of the company. And they say this
*  incredibly sophisticated email campaigns targeting our employees
*  try to impersonate me. So as I mentioned earlier, AI is going to be an accelerant of that.
*  There's going to be better impersonation. And also because folks are going to expect that a lot of
*  other people are using AI, if they notice something is slightly strange, they might even give it a
*  pass because, well, he might be using AI right now. It's not that he's in the car. He's using,
*  you know, speech to text. So we don't even know yet what those risks are. No one knew that the
*  internet was going to create the Nigerian prince scam factor. You know what I mean?
*  And so I think people would be lying if they told you, oh, yeah, I know exactly what's going to
*  happen. These are the three risks. This is how we mitigate them. We have to be very watchful.
*  I don't know if I'm a contrarian at that point. I don't know what the popular narrative is.
*  The whole AI is a nuclear-grade weapon thing. That meme needs to die because it's not. And
*  we're very far away from AGI that is truly self-agent and poses a lethal threat to humanity.
*  Well, I might take the under on that timeline bet, but I know that our time today is short. So
*  I guess we'll all just have to stay super vigilant. I'll come back when we get the
*  next generation of large-language models. I'll come back to revisit our prior. As I said earlier,
*  every week we have to re-examine. Yeah, weekly basis. I think that's a great
*  bit of guidance for everybody trying to figure out this space. Everybody definitely needs to
*  to stay on their toes because the AI future is coming at us about as fast as a
*  for cell-hosted website. So for now, I will say Guillermo Rauch,
*  thank you for being part of the cognitive revolution. That was incredible. Thank you,
*  Nathan. It is both energizing and enlightening to hear why people listen and learn what they
*  value about the show. So please don't hesitate to reach out via email at tcr at turpentine.co,
*  or you can DM me on the social media platform of your choice.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
