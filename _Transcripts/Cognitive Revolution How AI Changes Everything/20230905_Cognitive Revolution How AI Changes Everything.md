---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 4806s
Video Keywords: []
Video Views: 643
Video Rating: None
---

# Cryptography Will Revolutionize AI Data Privacy with Daniel Kang
**Cognitive Revolution "How AI Changes Everything":** [September 05, 2023](https://www.youtube.com/watch?v=O9sWKxwp-0I)
*  So if I want to somehow prove that I'm human today,
*  the way that I need to do that is essentially
*  reveal a lot of information about myself
*  because AI generation methods are becoming so powerful.
*  Maybe we don't want this.
*  So for example, you have services which take pictures of
*  your face to verify that you're a real human being.
*  But the way this works is that they literally
*  upload your biometrics to a server.
*  There's a lot of potentially problematic things that come with this,
*  including the potential for surveillance.
*  But cryptography gives us a hammer that lets us bypass
*  this fundamental trade-off between privacy and authenticity.
*  That's what I'm really excited about.
*  Hello, and welcome to the Cognitive Revolution,
*  where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas,
*  and together we'll build a picture of how AI technology will transform work,
*  life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Torenberg.
*  Hello, and welcome back to the Cognitive Revolution.
*  Today, I'm very excited to be speaking with Professor Daniel Kang,
*  Assistant Professor of Computer Science at the University of Illinois,
*  who has done pioneering work bringing
*  zero-knowledge cryptographic proofs to the domain of AI inference,
*  making it possible for people to prove that a model has been
*  faithfully executed as promised based on
*  certain pre-commitments and cryptographic calculations.
*  Now, as someone who knows very little about
*  cryptography and the modern crypto space writ large,
*  I have been wondering for some time what it might mean for
*  AI to put the smart in cryptos, so-called smart contracts.
*  As someone who has developed some very Byzantine heuristic systems in my day,
*  it always seemed to me that the core limitation of
*  smart contracts has been the fact that everything
*  needs to be fully spelled out with explicit code.
*  Could the use of language models in the context of
*  contract execution and dispute resolution change the potential for
*  smart contracts and perhaps a lot more besides?
*  It's been surprisingly difficult to find someone who could inform
*  my thinking on this question,
*  but Daniel Kang is indeed the perfect person.
*  Motivated by the growing trade-off we face between
*  authenticity and privacy,
*  Daniel set out to develop methods that would allow people to answer
*  key questions without having to reveal
*  the specific inputs used to calculate the answer.
*  Now, that's a mouthful, so here's a couple of examples.
*  One, a human might prove their humanity by running
*  an AI model on biometric data collected and analyzed locally on
*  their phone without having to reveal the biometric information itself,
*  or an AI model provider like OpenAI might prove that it ran the model it
*  promised to run and not a smaller, faster, cheaper one instead.
*  And yes, as in my original thought experiment,
*  an AI might be used to resolve disputes where multiple parties can
*  submit private data and all can verify that the model ran properly.
*  Daniel even envisions broad use of so-called attested devices,
*  which cryptographically sign the data they capture immediately on device
*  so that we can trace information such as photographs or audio recordings
*  back to their physical source.
*  The cost and complexity do remain limiting factors for these techniques for now.
*  But Daniel does see a path to making such techniques a seamless part of our future
*  AI infrastructure, much like HTTPS is for web traffic today.
*  And the fact that he undertook this work in the first place shows an
*  unusually forward-thinking approach.
*  So I was really excited to ask him not only all about how this technology works,
*  but also about how he expects it to be used as society adapts to and
*  hopefully takes full advantage of AI.
*  To be honest, I'm not sure I ever achieved the level of intuition for
*  the cryptographic math that I might have hoped.
*  But I definitely came away with a much better sense of what sorts of things can
*  be proved, why we might need such proofs in the near term future, and how this
*  technology can be useful in all sorts of as yet undiscovered and likely quite
*  unpredictable ways.
*  As always, if you're finding value in our attempts to understand the near term
*  future, we always appreciate your reviews and comments.
*  One that recently came in on Apple podcasts made my day.
*  The reviewer says, I'm a full stack web developer with an interest in AI.
*  I've followed generative AI loosely for a while, but with Chess GPT and all these
*  amazing products coming out, I felt like I had severely fallen behind.
*  So when I found this podcast from the very first episode, I was hooked.
*  Each episode was not only informative, but also thought provoking.
*  I went back and listened to all of the podcast episodes from the start.
*  And after each episode, I'd spend time learning about any concepts I didn't quite
*  understand.
*  I've used the podcast as a guide and as of this week, a catalyst for my career
*  growth.
*  I have just accepted a position as a full time AI engineer at a Fortune 100
*  organization where I'll be helping other developers learn and use AI to build AI
*  powered products.
*  I can't wait to give back to the community.
*  Thanks, Nathan, for being such a great scout through this cognitive revolution.
*  All I can say to that is wow and thank you.
*  And I hope to continue to live up to that review, starting with this
*  conversation about the application of zero knowledge cryptographic proofs to AI
*  inference with Professor Daniel Kang.
*  Daniel Kang, welcome to the cognitive revolution.
*  Thank you. It's great to be here.
*  Yeah, very excited to talk to you.
*  This is a topic that which you are expert in that I know very little about, but have
*  been kind of speculating about, wondering about and frankly, trying to find the right
*  person to talk to for a while.
*  So I'm glad that this day is finally here.
*  And the topic broadly is the intersection between AI and quote unquote crypto, you
*  know, maybe more specifically cryptography, because this is not like we won't be
*  launching any coins on today's episode.
*  And more specifically, you have done some really interesting work around the use of
*  zero knowledge proofs within the context of machine learning.
*  And that has some, I think, very interesting properties.
*  And I think people will hopefully get a little bit better sense of just what you know,
*  just how strange the future might be in some regards by understanding some of these
*  possibilities and the problems that you're trying to get ahead of to solve.
*  So I think it's going to be super interesting.
*  I definitely ask you to bear with us a little bit as we go, because I know very, again,
*  very little about the crypto space.
*  And I expect that our listeners who are obviously very interested in AI probably also
*  have some gaps in their knowledge around how some basic stuff works.
*  So I did prepare by listening to a couple of previous appearances that you've made
*  where the audience and the hosts were more crypto savvy here.
*  I think we've got a little more of the AI savvy, but the crypto is probably highly varied.
*  I'd love to just start off with an articulation of what motivates this work, kind of what's
*  the problem that you're anticipating and wanting to solve.
*  And then we can get into some of the mechanics of the zero knowledge proofs and how that
*  all works.
*  And then kind of circling back toward the end, I want to open it up a little bit and
*  envision a world where this stuff is really working and kind of how it might ultimately
*  be deployed.
*  How's that sound?
*  Yeah, happy to talk about that.
*  What's the motivation for bringing zero knowledge proofs to the AI space?
*  Of course, the long term vision I've been thinking about is that as AI increases in its
*  power, it seems like to me there's going to be this really fundamental trade off between
*  privacy and authenticity.
*  So if I want to somehow prove that I'm human today, the way that I need to do that is to
*  essentially reveal a lot of information about myself because AI generation methods are becoming
*  so powerful.
*  But I think that maybe we don't want this.
*  So for example, today, I've actually heard dating apps are one of the biggest users of
*  this.
*  You have services which take pictures of your face to verify that you're a real human being.
*  But the way this works is that they literally upload your biometrics to a server.
*  And I think that there's a lot of potential problematic things that come with this, including
*  the potential for surveillance and other negative consequences.
*  At some fundamental level, without cryptography, there's no way to get around this, as far
*  as I know.
*  But cryptography gives us a hammer that lets us bypass this fundamental trade off between
*  privacy and authenticity.
*  And that's what I'm really excited about.
*  Yeah, that's interesting.
*  And that's kind of another I think we can unpack a variety of use cases over time.
*  This one has kind of become somewhat more well known in the last few months with the
*  WorldCoin release.
*  I think, again, most folks have probably heard of that and maybe have a sense that and this
*  is about where my knowledge also stops that like the part of that scheme is that it allows
*  you to prove that you are a human and tries to give kind of each human one unique ID to
*  be able to prove that motivated there by the, as you said, the fact that basically since
*  the this person does not exist dot com website went online, a simple square headshot isn't
*  going to suffice anymore to prove that you're human.
*  And so we need kind of ever escalating ways.
*  And obviously, those become more and more sensitive.
*  Another really interesting one, just to kind of preview the breadth of application potentially
*  for techniques like this is basically what I'm starting to call model fraud, the notion
*  that if you are paying for an AI model to be run in any number of contexts, how do you
*  know that the thing was actually run in the way that you wanted it to be run, which could
*  be as simple as just kind of a provider cutting costs and cutting corners,
*  potentially at your expense, or could be all sorts of more nefarious attacks, more
*  intentional malicious attacks than just laziness.
*  So tell me a little bit about that, too, because I know that's also part of the motivation.
*  Yeah, that's another application I'm really excited about.
*  So maybe to set the context a bit, if you look at what opening does with their services,
*  they will change the model that you're being served, that you might even be paying for
*  without any warning and without any guarantees of quality.
*  And so if you in fact look at some analyses over time, there's a great article on paper
*  associated with that, where some folks at Stanford and Berkeley measure chat GBT's
*  performance over time, and they showed it's substantially degraded.
*  So it went from something like on a particular task, say 93% accuracy down to like 7% accuracy.
*  And as a customer, you have absolutely no recourse today, because you have no idea what
*  OpenAI is running.
*  You might have some suspicions, but there's currently no way to check that OpenAI is
*  running a certain type of computation.
*  In this case, a machine learning model.
*  The same cryptography that allows you to prove authenticity can allow you to prove that
*  OpenAI ran a specific model, say the same model that was running a month ago, which
*  could potentially allay some concerns about performance drops in services like chat GBT
*  and other kinds of ML services as well.
*  So one short footnote on that for practitioners using the API.
*  If you trust them, they do now have at least a bit better answer to that question than
*  they've had in the past.
*  They recently did introduce basically a model dating scheme where, again, assuming you
*  trust that they're doing what they say they're doing, they at least now say that they are
*  freezing model weights according to these timestamps and then giving developers a chance
*  to kind of revalidate and upgrade at their convenience when new models come out.
*  So contingent on trust with OpenAI, in particular, that's a little bit better than it used to
*  be in general, though the problem remains that A, if I don't trust them, then all bets
*  are off and B, there's a lot of other providers out there increasingly proliferating, which
*  don't have such a scheme and also probably have a lot less reputation and a lot less
*  reason to trust that they're consistent in their product delivery as opposed to an OpenAI
*  in the first place.
*  I can also give another example, which is a bit more out there.
*  So there's a lot of medical ML services that are proliferating.
*  And so you could imagine one way to a malicious attacker, perhaps even a state actor can
*  incapacitate someone is that if you send them in, someone goes in for a routine checkup,
*  say to check for cancer or something else.
*  They can simply just replace whatever ML model might be predicting to either flip the diagnosis
*  in one way or another.
*  So for example, someone does have cancer, you can report that they don't and they won't
*  get any treatment and then might suffer from the delayed treatment.
*  But on the flip side, if they don't have cancer, you can simply flip the prediction and say
*  they do have cancer and then they might get, say, treatment which could harm them despite
*  not having any ailments.
*  And so today we have absolutely no way of telling whether or not a prediction from a
*  medical ML model actually came from the model that was, say, certified by the FDA or not.
*  So that's a pretty good starter set of use cases.
*  And let's get into the guts of the technology a little bit more and then kind of map this
*  back onto a little bit more of a futuristic vision toward the end.
*  So here's kind of the headline result.
*  And then I'm going to rely on you much more to unpack it.
*  But with these zero knowledge proofs in general, the idea is that you can prove that a certain
*  process was executed faithfully.
*  But you can do that in a way that does not reveal the inputs to the process.
*  And if you frame the machine learning inference problem as one of those processes, then the
*  inputs become the weights of the model itself, which again, obviously something that providers
*  very much in many cases don't want to share and will choose to keep private over probably any
*  number of other goods that they might value, including the ability to verify in the absence
*  of a technique like this.
*  And then the other input is your input, whatever you put in at runtime.
*  And so the technology allows you to kind of selectively expose and different parties to know
*  some of the inputs, but ultimately can prove this execution without revealing any information about
*  the inputs or the intermediate states, just that the final result was a faithful execution.
*  Is that right?
*  That's right.
*  If this resonates with you, there are three numbers you need to know.
*  Thirty six thousand, twenty five and one.
*  Thirty six thousand.
*  That's the number of businesses which have upgraded to NetSuite by Oracle.
*  NetSuite is the number one cloud financial system, streamline accounting, financial management,
*  inventory, HR, and more.
*  Twenty five.
*  NetSuite turns twenty five this year.
*  That's twenty five years of helping businesses do more with less, close their books in days,
*  not weeks, and drive down costs.
*  One, because your business is one of a kind, so you get a customized solution for all your
*  KPIs in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts, and improve margins.
*  Everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist designed to give you consistently
*  excellent performance, absolutely free, at netsuite.com slash cognitive.
*  That's netsuite.com slash cognitive to get your own KPI checklist.
*  netsuite.com slash cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it, and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  The most salient thing here is that it forces the person or the party that's producing the
*  proof, for example, OpenAI or a medical level provider, to stick to that computational process.
*  So not only do you prove that the computational process ran, but the prover cannot cheat.
*  They cannot actually run some other process.
*  Let's say that you want to prove that you ran on model A.
*  They can't turn around and set what on model B and then use that result instead.
*  They're forced to use model A.
*  So let's break this down a little bit at maybe two different levels.
*  One is kind of the protocol, which is basically crypto language for
*  the algorithm of execution, right?
*  The steps that the different parties have to take in order for the guarantees to hold.
*  And then going a little deeper than that, I'd love to try to understand the math and at least
*  get some intuition for why we can believe this at the most fundamental level.
*  But take me kind of through the steps that I and OpenAI would go through if I wanted to,
*  and they were willing to make these sorts of guarantees.
*  Who has to do what in what order?
*  Yeah, I think it's worth drawing an analogy to how you would take a machine learning model
*  and deploy it on a GPU.
*  And in some sense, you can think of the zero knowledge proof as a GPU that
*  proves that I ran a specific model.
*  So if you want to deploy a model on a regular GPU, what you first have to do is specify the model
*  architecture.
*  Common tools like TensorFlow and PyTorch for this.
*  So the framework that I've built accepts currently variants of TensorFlow and a format that PyTorch
*  exports to.
*  And then you specify the model weights in addition to the architecture, you specify the input,
*  and then you say run this on the GPU.
*  Similarly today, that's what the stuff that happens.
*  You first start off by specifying an architecture, the weights and the input, and then you pass it
*  to the system, which then proves that the model executed correctly.
*  And so from the perspective of both the model provider and also the person who's receiving the
*  proof, it's all fairly black box.
*  You can simply run a program.
*  So the model provider can produce a proof that says I ran this specific model on this
*  specific input.
*  And the person who's receiving the proof and the prediction can verify that that happened
*  honestly.
*  There are some additional time sensitive sequences though in that, right?
*  Like for me as a customer to ultimately have confidence in the final assertion,
*  if I understand correctly, the provider needs to say, okay, first of all, here is essentially a hash
*  of the architecture and the weights.
*  Like there's a bundle of sort of what defines the model that gets kind of hashed out to a
*  alphanumeric string or whatever, right?
*  That I can sort of say, okay, this was, and that's basically a pre-commitment.
*  They have said, you know, and this thing is inalterable, right?
*  So that I have to have that in advance.
*  Then I can call the model they can execute.
*  Then they can also produce the proof.
*  Now I have both the pre-commitment artifact and the final proof.
*  And then I get to do something on my end to verify, right?
*  With those based on those two things, I can sort of verify that the whole thing was legit
*  end to end.
*  Is that right?
*  Yeah, that's right.
*  Okay, cool.
*  So help us understand how this is working under the hood.
*  I think your GPU analogy is really interesting.
*  I, in general, listeners of the show will know I'm always really reluctant to base my
*  understanding on analogies.
*  I think that, you know, obviously very useful in many ways for developing intuition, but
*  I try to hold myself to the standard of I want to understand this.
*  I'm happy to simplify some details, but I kind of want to find a way to kind of understand
*  it that is very literal, even if simplified, and still not wrong.
*  That's kind of the base camp for future understanding in my view.
*  So help us kind of get to that.
*  Like what is going on at each of these steps when first of all, a pre-commitment is made
*  and then a proof is made and then a verification is made.
*  All three of those things have to happen.
*  And if I understand correctly, the model itself, that bundle, that's a one-off process.
*  So they can basically publish almost, you know, plays a similar role to like a public
*  key, I guess.
*  That's like, this is a starting point.
*  Then for each instance that we want to prove, right?
*  I don't know if it would come down to each token or each, you know, if it could be something
*  that's like for a full, you know, long text generation.
*  But we have to kind of do this proving and verifying each time, right?
*  Yeah.
*  So for every input, you have to produce a new proof.
*  That's correct.
*  So in terms of how it works, cryptography is one of these things where there's many
*  levels of abstractions.
*  And so I'll try to aim at one level of abstraction.
*  You can tell me if I'm going too deep or too shallow.
*  The commitment is the easiest thing to explain, I think, because people have actually,
*  most people have used this in some form or another.
*  The commitment is simply a hash.
*  So a cryptographic hash is literally a function, a program that you've run and you assume that
*  it's really difficult to produce an input that produces the same hash as the one that
*  you produced.
*  So in general, if I produce a hash, I know that a program actually run that hash,
*  then I can essentially prove that I know some inputs that have resulted in this hash.
*  So this is actually what secures the Bitcoin network and billions of dollars in value.
*  So hopefully, fingers crossed, that hashes stand the test of time.
*  And just for a little bit more color there, these have been around before crypto.
*  I have used hash functions in programming, even for just hacky things like uniqueness checks,
*  because of the property you said.
*  There are a lot of different hash functions out there.
*  They generally have this sort of, I don't know if it's proven or if it's just, you said,
*  kind of assumptions, but that's an interesting wrinkle.
*  But in general, it's like there are more possible hash outputs than atoms in the
*  universe or whatever.
*  And there's some mapping from large inputs to these relatively small, presumably unique
*  outputs such that it's pretty commonplace in just general programming to use them to dedupe
*  larger objects to have a database of hashes where it's like, okay, we want to check.
*  Is somebody uploading some copyrighted material straight away to just hash it and to check?
*  So that's fairly familiar.
*  But I am interested in that wrinkle of what are we assuming there?
*  And just the sanity check, would this be like a quantum computing future that might break
*  that assumption perhaps?
*  So there are many different kinds of hash functions, and different hash functions have
*  different assumptions.
*  So hash functions are one of these things where they fall under the broad umbrella of
*  cryptography.
*  And typically, what you do is you assume some property, so a common property to assume,
*  cryptography in general, is that inverting a logarithm in a finite field is hard.
*  And so if you assume that, then you can assume that some certain kinds of computations are
*  difficult.
*  We also have some hash functions which are assumed to be quantum resistant.
*  But it's one of these things where there's no strict mathematical proof that these things
*  are impossible.
*  But they're widely used in practice.
*  And as far as we know, after decades and decades of research, there's been no actual
*  basically ways to break these hash functions.
*  So, OK, we've got no formal guarantees, but we do have decades of practice.
*  Are there examples of hash collisions with modern hashes where people report things going
*  weird on them?
*  Or is this just like totally smooth sailing in practice?
*  Yeah, that's a complicated question to answer because there's two levels to this.
*  One level is that if you think about passwords, there's actually whole engineering teams at
*  dark corners of the internet dedicated to reverse engineering passwords.
*  But that's because passwords have essentially limited entropy.
*  So the most common password is password.
*  And so if I just look at a random password and I just guess, OK, that input's probably
*  password, then I get it with 10% probability or something.
*  But if I'm trying to be secure about this, I can add, let's say I choose a truly random
*  password, I do what's called, I salt the password, then it's assumed to be extremely difficult.
*  It requires a lot of computing power to break that.
*  I've used this technique a little bit, but basically the salting is you take the original
*  raw input, you add some kind of secret additional input and then hash that.
*  Yeah.
*  So secret additional input also adds entropy.
*  So it becomes hard to guess because it's random.
*  Or if you're doing it correctly, it's random.
*  So I describe this in the context of passwords because passwords are the most common way people
*  interact with hash functions.
*  But in the case of trying to protect your secrets from an ML model, what you can basically
*  do is you can salt the ML model.
*  You take the ML model weights, which might have low entropy, and you add however many
*  bits of entropy at the end.
*  And then by doing this, because the last set of bits are random, the hash becomes
*  essentially random.
*  We have a trained model in this scenario where we want to prove the model ran without
*  really revealing anything about the weights.
*  We first can take the trained model, represent it in some form.
*  Well, there is still a trick here, right?
*  Because I am not going to ever have access presumably to the model to rerun the hash.
*  But yet that hash is now going to feed into this scheme to allow me to prove something
*  downstream of it.
*  So that's interesting.
*  So, OK, let's keep going.
*  We've got the thing hashed.
*  Now we come to the point where we want to prove that the computation ran.
*  So describe that proving process.
*  OK.
*  So at the highest level, the technology we're using is called zero-knowledge proof.
*  And we're using a specific form of a zero-knowledge proof called a zkSNARK.
*  The zkSNARK, or sorry, zero-knowledge proofs in general, allow you to prove that any arbitrary
*  computation ran correctly.
*  The key here is to choose what computation or what function to prove.
*  Now the function that we're going to prove has two parts.
*  So the inputs are the model weights and the hidden input.
*  For example, the user prompt.
*  So when we have the zero-knowledge proof, we can reveal any part of the computation.
*  So we might reveal the input as a concrete example.
*  Now inside this function, the first thing we compute is the hash of the model along
*  with the salt.
*  And then we reveal that hash.
*  So because I computed the hash inside the zero-knowledge proof, I as a model provider
*  cannot use a different set of weights because the hash you can think of as binding and the
*  zero-knowledge proof is also binding.
*  Then the other thing you prove is that you actually ran the ML model, the architecture
*  correctly with the given weights and input.
*  And then you can reveal the output.
*  And so by doing this, you essentially forced a fixed architecture within the function
*  specification.
*  You forced a fixed set of weights by revealing the salted hash.
*  And then you've also forced the input by revealing it.
*  Okay.
*  So let's dig in a layer deeper then.
*  How it's very unfamiliar territory for me, obviously, but what I found kind of interesting
*  about this is models themselves, right, are all linear algebra, all matmols.
*  That's not quite true because there are also these nonlinear layers that sit between.
*  And it does seem to be a, I don't know if this is quite proven either, but it does seem to be a
*  important and pretty robust empirical result that the best results kind of come from this.
*  Mix of lots of linear algebra followed by this kind of nonlinearity that acts seemingly as a
*  sort of filtering function to kind of allow certain meaningful signals through and, you know,
*  sort of stop other signals that are just noise, something like that seems to be going on.
*  Then in the context of this proof, there's kind of a process of
*  arithmetization, which is taking this computation, right, which is, as you mentioned,
*  you know, kind of ultimately defined by an architecture executed with, you know,
*  a specific set of weights on a GPU, a lot of arithmetic there, but not entirely arithmetic
*  given the nonlinearity. And essentially the first big part of this is creating an arithmetic
*  approximation of that original kind of proper computation. First of all, do I have that right?
*  And second, like, I'm still not quite sure, like, why are we making an arithmetic approximation in
*  the first place? Okay. So once we get to the point where we have a zero-knowledge proof,
*  so ignoring ML models entirely, just if you have an arbitrary function that you want to prove,
*  arithmetization refers to the process of taking that function, which might be specified as,
*  say, a Python program and turning that into the format that the proving system,
*  the thing that produces the zero-knowledge proof, can actually
*  ingest because it doesn't take in Python programs. I believe the reason it's called
*  arithmetization is that historically zero-knowledge proofs were constructed using this thing, this
*  mathematical object called an arithmetic circuit. So you have to represent your function as an
*  arithmetic circuit. So you arithmetize the function to the arithmetic circuit.
*  For the zero-knowledge proofs that we're talking about for ML models, the arithmetization is simply
*  taking the ML model architecture and weights and then turning that into a format that the
*  zero-knowledge proof can ingest. At this point, there's actually no approximation. It's an exact
*  one-to-one mapping. Okay. We were doing a ton of arithmetic plus these non-linearities, and now
*  we're essentially restating a ton of arithmetic as arithmetic. And then you have kind of an additional
*  element where you're using lookup tables for the non-linearities to basically say,
*  if I understand correctly, because the proving system doesn't accept that kind of function
*  as an input that it can do proofs over, we need a, I don't know if I would call it simpler,
*  but we need a more explicit numerical representation of the non-linearities. So
*  I guess there's basically like equivalent of the sort of renaissance log tables where
*  all of these values are just kind of pre-computed and then can be looked up.
*  So is that the main transformation that's happening in the first place? It's all exact in the
*  arithmetic and you have high precision on these lookup tables. And so do I have an artifact there
*  that gets input into the proving system that basically could be run in place of the model?
*  Like it's truly a like for like, like it would generate the same outputs?
*  Yeah, it would generate the same outputs. So you do have to quantize the model, which is actually
*  a very common thing to do with machine learning models in production. OpenAI does this and a bunch
*  of other, pretty much all other serving systems do this in some form or another. So once you do
*  the quantization, it is an exact representation of what happens. Everything is correct from an
*  intuition standpoint. I guess one thing I might make a little bit more precise is that the lookup
*  tables are also exact results. So for example, if you have a quantized input and then you apply
*  say a value or a 10H non-linearity, you can just get the exact output after applying the lookup.
*  And so literally there's a value for every, I think that was the phrase in the paper,
*  exhaustively pre-computed, which basically means like down to the level of precision that is
*  possible every last, if it's eight digits, you've got eight digits worth of lookup values waiting
*  to be referred to. Fascinating. Okay. Can we take just a little bit more of a detour into the
*  floating point versus the fixed point operations? I think this is something that honestly most
*  people probably totally gloss over. I think what we know, what I feel like I know is, okay,
*  naturally if I've got, you know, whatever a 64, you know, digit number versus 32 versus 16,
*  versus eight versus four, intuitively makes a lot of sense that like I would need less memory,
*  you know, it would be faster to do these whatever compute process over just smooth data.
*  That would be true if I was doing it by hand, it seems intuitive that it'd be true doing it on a
*  computer, but it seems there's a little bit more kind of stuff going on there than just that.
*  There's something more fundamental where this change has to be made. And it's like probably
*  in practice fine because it's often made for these efficiency reasons, but it seems like this is not
*  an efficiency question in this context. It's more of a like validity question. So there are
*  not, it's going to allow you to prove arbitrary functions. So you can prove the full floating
*  point arithmetic if you want, it just becomes much slower to produce the proofs. Gotcha. Okay. So
*  it's the same basic concept. Is it just computationally saving to go with the quantized version?
*  Yeah. Yeah. And quantization is used very widely. I believe recently Elon Musk revealed that they
*  use quantized models within the Tesla vehicles. So you have millions of cars running around on
*  the roads with these quantized models and they're used by Google, OpenAI, many other services as
*  well. So we're up to the point now where we have, having pre-committed, we now have a fully
*  arithmetic representation of the computation that the model is actually going to perform,
*  including this main change being the substitution from a traditional non-linear calculation to
*  the exhaustive lookup function that has 10 to the eight things in it, right? Or eight to the 10,
*  I should say maybe. So because of your quantization, you actually don't need to represent that many
*  digits. Like it's more like something like two to the 15 or something. So like on the order of like
*  hundreds of thousands or maybe slow millions of possible inputs. Okay. So now this all gets
*  ingested into the proving system. And I guess this is where it probably starts to get
*  a little bit crazy. So what happens next? Yeah. So there are many different kinds of
*  proving systems for zero knowledge proofs and there are many different kinds of ZK-SNARKS.
*  Talking about all of them in this full generality is the outside of the scope of this podcast,
*  but I can talk about the general intuition. Well, actually this is somewhat precise. So
*  almost every proving system I'm aware of relies on the fact that polynomials
*  can represent arbitrary computations. So if you allow the number of variables in a polynomial to
*  grow, you can literally represent any computation. So maybe some photographers will get mad at me,
*  but I think you can basically think of this as if you grow the number of variables in a polynomial,
*  you can write down anything you want within that polynomial.
*  This is basically like Taylor expansion like work, right? I can recall doing these sort of,
*  okay, what's the first approximation? What's the second approximation? Is it enable a square
*  parameter and a cube parameter? And lo and behold, you can reconstruct the sine wave
*  if you allow infinite terms in that sequence. Obviously, you don't have to achieve infinite
*  terms, but that's basically the same type of math. Is that right?
*  So the intuition is the same, but because we're working over finite fields, I think maybe a
*  more precise analogy might be, sorry, if you have two logic gates, a NAND and a NOR,
*  you can literally represent any computation. And then one reduction you can do is that you can
*  actually, if you have a polynomial of multiple variables, you can literally just like take the
*  variables and then multiply them and add them in certain ways, like literally represent NAND and
*  NOR. And so then the polynomial gets reduced to these NAND and NOR gates, and then the NAND and
*  NOR gates are then universal, it can represent any computation. So a reduction, the polynomial
*  can represent any computation. Yeah. Can you
*  impact the finite fields a bit more? This is kind of where we make the leap into cryptography,
*  right? Because the finite fields basically has to do with using prime numbers in some way to
*  basically make the math hard to reverse, right? Or hard to kind of tell me, just sharpen me up.
*  So finite fields, you can basically think of as integers from zero to some large number,
*  and once you get that large number, you wrap around back to zero. That's the basic intuition
*  behind the finite field. And then you have certain operations. The operations we care about are plus
*  and minus multiplication. And then there are constants, which are from zero to the large
*  prime number that we care about. So one other thing is that we actually also operate over
*  elliptic curves at some point, but that's like maybe not super relevant for the purpose of this
*  discussion. The reason that we use finite fields is that polynomials or finite fields have this
*  amazing property, which is that if you have two polynomials, let's call them f and g,
*  and you take a random number in the finite field and you compute f of the r, let's say the random
*  number, and g of r, the random number, f and g, unless they're equal to each other, are not going
*  to be the same at this random point. The probability that they match at this random point is vanishingly
*  small. So this lets you do something amazing, which is that maybe an easy way to think about
*  this is let's say I have f and you have g. And let's say that we're both honest for the time being.
*  I can compute, and we want to check that f and g are equal. Instead of sending a representation
*  of f, which are, for example, coefficients, what I can simply do is take a random point, we both
*  agree on a random point, and we just send f of r and g of r to each other, and we can check that
*  the evaluations match. So the coefficients even differ at one point, at one of the coefficients,
*  even off by one, the values will be completely different. Okay, so taking a step back, as long
*  as there's some way to force a prover to what's called commit to a polynomial, which basically
*  says I'm going to use this specific polynomial, then we know that they actually use that specific
*  polynomial because of this amazing property of polynomials in the finite fields.
*  Just zooming out, I always kind of, you know, try to zoom out for a second and then zoom back
*  into the part where it's confusing. So we've got our, you know, three-step protocol. We're going to
*  commit with a hash to this is the model that we're going to use. Now we're in part two, which is
*  we're going about the proving, and then part three is going to be the verifying.
*  In part two, we first do an arithmetization of all the computation. This is an exact representation,
*  but in a different form, making use of, for example, lookup tables such that with that
*  transformation, we could still do the exact original, you know, we could run that as our
*  forward pass, but then that whole process gets kind of mapped onto this sort of wonky arithmetic
*  that is operating over finite fields, which is like somehow all this is now represented in like
*  modular math with a given kind of prime key and the same sort of hash-like property is preserved
*  such that can only get to that result if I used the same input that I promised.
*  Yeah, that's more or less correct. So the process of arithmetization is taking the computation,
*  and you can think of it as turning it into a polynomial over a finite field.
*  So polynomial is a representation of the computation.
*  And the whole secret here is that there's some private key prime number, large prime number,
*  that is being used that nobody knows, right? And that's why like the whole thing becomes
*  irreversible. And that's also the whole reason that we're using this prime based scheme in the
*  first place. So for all the proving systems that rely on these polynomials in a specific way,
*  I'll talk about relies on what's called toxic waste, which is the term of art for this random
*  prime. So this random value that is used to ensure the secrecy because you can't reverse that.
*  So at some point, there's a couple of things that kind of got a little confusing here. So,
*  you know, in kind of zooming out and looking at the results, one thing that's interesting is
*  the setup or that original kind of commitment, right? It has a certain amount of compute attached
*  to it. Then the proving also has a certain amount of compute attached to it. And then the
*  verifying is like much faster. So it definitely makes sense to me, given what we're talking. I mean,
*  inference is, you know, compute intensive in the first place. So it's no surprise that
*  doing this transformation and actually executing it takes a significant amount of time.
*  But one thing that kind of was confusing to me is there at some point, there is an approximation
*  is introduced, right? Or a sort of lack of like full fidelity to the original. Like at some point,
*  I can no longer use this as a substitute for my original forward pass, right? So when and how does
*  that complication arise? So that complication arises if you do quantization in a way that's not
*  efficient and in a way that results in basically bad approximations. Well, we've actually fixed that
*  in some upcoming work. And so basically, you can think of it as a fully faithful representation
*  of the forward pass. Interesting. Okay. That's it. That's a meaningful update. It sounds like
*  it's a matter of making a better quantization in the first place that gets you out of this
*  indeterminacy. So there's no indeterminacy anywhere. Yeah, that's loose, loose speak.
*  But I guess just let's back up for one second before we talk about the solution, because in
*  the original paper, which I was trying to make as much sense of as I could coming into this,
*  there is a probabilistic sense of you can be so confident that the thing has run. And to kind of
*  build more confidence, you have to like do more compute, right? So there seemed to be kind of a
*  Pareto frontier there somehow, where depending on how confident I wanted to be, I can invest more in
*  a more rigorous kind of convincing proof. I see. Yeah. So there's actually two levels here. So
*  one is the individual proof. The individual proof, you can basically think of as unforgeable
*  as an exact representation. Once you have this primitive of a proof, then you can layer things
*  on top of that. So for example, let's say I want to approximate GPT-4's accuracy on some task.
*  Well, maybe I have a test set of a hundred thousand examples, but producing a hundred
*  thousand proofs is very, very costly. So instead, what I can do is I can ask, open the eye,
*  well, produce proofs on a hundred of my test set. And I'm going to use that as a rough
*  approximation of a measure of accuracy. And then a hundred might be too small. I might
*  instead ask for a thousand or 10,000. But that is something that you layer on top of these proofs.
*  The proofs themselves are, you can think of as unforgeable, no way to cheat that. And then this
*  test set accuracy computation is something you layer on top of these proofs.
*  Okay. So I think I misunderstood in a pretty important way what some of these percentages
*  meant. Big update in my understanding here. So the individual proofs are fully robust. If I
*  run this process, I will get a proof that a computation was run and it will be sort of
*  have all the nice properties of it. It'll be unforgeable. I can fully kind of be confident
*  in that. And then the subsequent kind of layer is, okay, but this is still expensive. I mean,
*  it's essentially another forward pass, but even more computationally intensive, right? Because
*  we've got to do all this kind of weird math that does it in the finite field. So it's even more
*  relative to running your forward pass. This kind of provable running of the forward pass is just
*  a lot more expensive. Is there a ratio? Should we have a rule of thumb in mind for how much more
*  expensive? With the work that we did in the paper, you can think of it as something like 10,000 times
*  more expensive, which is quite out there. Fingers crossed in the next few months, we'll have some
*  work that bring down this cost. So orders of magnitude more expensive, hopefully the number
*  of orders of magnitude coming down. But obviously that is a lot. So basically then if we're going to
*  do 10,000 inferences and I just wanted to prove one, I would be doubling my total compute bill.
*  Yeah, that's roughly right. And obviously again, you're working to make that more efficient.
*  So then naturally it follows from that, that I wouldn't want to verify every single one would
*  be infeasible. So I have kind of more statistical, classical statistical sampling techniques that
*  you're just kind of mapping out for people saying, okay, you can do this many on a set of this many
*  and you can kind of get this confidence. Okay. That all I have much more intuition for. Now,
*  I think we're basically getting to the end of part two, right? Where we've created a fully faithful
*  and unforgeable, albeit 10,000 times, or hopefully soon less more expensive version
*  of the same computation that has all these nice properties for verification.
*  And then what is the proof of itself at the end of this? It kind of just spits out some like
*  bit string basically, right? That is kind of the final proof. And that's independent,
*  like that's sort of in addition to the actual output. Yes. So you have to specify the proof
*  and you also have to specify the output. You have to send both. So then I get as a user,
*  as a customer of whatever the model provider that I want to double check, they give me both things.
*  I look at the output and then what do I do to do the verification? I'm also running like relevant
*  additional software on my end, right? You can think of this as verifying a hash on your end.
*  You basically kind of how like you send checksums or hashes with large files to ensure that it's
*  got sent over the wire properly. You can sort of, and you've run the hash in your end as a user,
*  you can sort of think of this proof as like a hash, put unquote, of the computation.
*  And you just verify that it matches. And to do this, you do some more basically finite
*  filter or something. But it's way easier this time because I mean, this is just one of many things
*  that it's like much easier to verify than to do. Is there any more intuition I should have for that?
*  It goes back to this thing where you have to basically check polynomial equalities. As the
*  prover, I basically need to say, okay, I'm actually going to use all of these coefficients
*  and this fixed polynomial, which requires a lot of effort. But then as a verifier, you can just say,
*  okay, well, if I know what the polynomial form is, I can just check it at a random point.
*  And so I have to do much less work than the prover does.
*  So I'm getting the polynomial form or that is the proof represents the polynomial form. Because
*  the polynomial form is irreversible, I can actually receive the polynomial form without
*  being able to run the model on my own downstream. Well, I'm using this term colloquially, but it's
*  called the verification key, which specifies the layout of the computation, which in this case is
*  basically what polynomial you're using. And then you can basically check that polynomial was run
*  correctly. If we do set this up and I am the client, the verifier, and I get this polynomial
*  form, does that mean that I basically have a 10,000 times slower instantiation of the model?
*  Could I somehow run that with other inputs if I were willing to do it at 10,000 times slower,
*  or do I still not have enough information to perform inference? You could do it with your own
*  weights, but the weights will not be revealed to you. So basically the polynomial encodes the model
*  architecture, but not the weights. So the polynomial represents the computation of compute hash and
*  compute model architecture with a hidden set of weights. But because the weights are hidden,
*  if I send you this polynomial, you can run the polynomial on your own, but you won't have my
*  weights. So is that it's dependent on my specific inputs? Like I'm just a little confused as to how
*  we somehow make this jump from there's a fully faithful reformulation of the computation
*  that I can verify, but still can't run it on inputs in general. I can run it on my input and
*  confirm that it works, but I can't run it on arbitrary inputs. How does that narrowing happen?
*  So here's an analogy. So Twitter recently open sourced their recommendation algorithm.
*  But even though the code is all there, you can literally just look at the PyTorch architecture.
*  You cannot run that code like as Twitter does because Twitter has information that you do not
*  have. So you can think of the verification key, this polynomial form as the PyTorch architecture.
*  But even though you have that PyTorch architecture, you still cannot run Twitter's
*  recommendation algorithm. So if I send you a Python file, which says, okay, so here's the Twitter
*  architecture. We have some multilayer perceptron with some skip connections and all this kind of
*  other stuff. And then you ask them, okay, so given this PyTorch architecture, can you actually
*  verify that the timeline is generated from this architecture? The answer is no, there's no way,
*  because Twitter has the input data and the model weights, which are unknown to you.
*  But in our main case, I'm trying to isolate this one kind of leap that I'm not quite following on.
*  I mean, it depends on the initial commitment. I understand that. There's some
*  commitment to particular weights. And that is needed. I guess there's some sort of factorization
*  or whatever happening at the end that is basically saying, because I know this hash of the weights,
*  I can do some sort of thing. But the final verification depends on my input. So I couldn't
*  verify for any other input. I'm not quite getting why that is. Because in the case of the Twitter
*  thing, I'm basically just saying, well, yeah, but they also haven't given me the ability to verify.
*  So I can't run it, but I also can't verify it. Here, I'm getting this ability to verify it,
*  but I'm trying to figure out where exactly in the steps the verification comes through
*  and the ability to redo that on a different input stops or doesn't come with the ability to verify.
*  OK, so this polynomial form that we've been talking about, let's call it the verification key.
*  You can think of the verification key as the model architecture plus the hash.
*  That's the right way to think about it. So if I have this verification key, I can put in my own
*  weights and then run the Twitter algorithm. But the hash is not going to match because I don't know
*  the weights as a verifier. So even though I have this verification key, I cannot produce a proof
*  that matches with this hash because I don't know the weights. Only the model provider who knows the
*  weights, for example, Twitter, can produce this like a passing proof because when you plug in the
*  weights, it will match the commitment. That's what forces Twitter to use a specific model,
*  a specific set of model weights. Yeah, I get the scheme. I still don't fully get the math,
*  but I do get the scheme and I'm probably not going to get the math today in its full complexity. So
*  might be time to give up on that dream. But just to restate the scheme, the step one is the
*  commitment to the hash that defines the architecture. So there's some transparency
*  around the architecture, but the weights themselves are just in this compressed hash
*  with the process of the arithmetization and the 10,000x hopefully soon lower increase in
*  compute cost. I can do this math over this strange kind of large prime modular space instead of in
*  its original arithmetic form. That's a lot more work, but it also allows me to kick out at the end
*  another basically hash looking thing that constitutes the proof. And then the prover at
*  the end as the verifier, what am I running at the end to do the check?
*  You're basically evaluating a polynomial at a random point.
*  So I'm confirming that the thing that I got back is producible based on the previous commitment
*  that I got and the inputs that I personally already had that were known to me. Yeah. So
*  you're basically checking that the hash, the commitment of the model weights match,
*  the architecture matches and the input matches. That's what you're doing into it.
*  I think this is definitely super fascinating. I mean, to zoom out, we're entering a world where
*  AI agents are getting worked on feverishly and people are looking at a future of all sorts of
*  autonomous things. People are going to need to prove that they are human. Agents or models are
*  going to have to prove that they ran the right thing. And so all this stuff can be used anywhere
*  where the value and reliable, even with kind of a single, and this is probably the biggest
*  update in this conversation for me is that it's not just a probabilistic thing, but it is a fully
*  guaranteed thing. So I could do this just you and me one-on-one. You have a model. I want you to
*  run it for me. I don't need any other parties. I don't need any other like reputation mechanism
*  or platform. If we're willing to pay the compute tax to do the verification, then we can verify
*  that you're running what you said you were going to run. Yeah. You don't need third parties. You
*  can literally just do this on your own and there's no way to cheat it. Let's talk about what this
*  enables. I mean, one thing that I've been looking out for for a long time, I mean, long time,
*  whatever, a long time in AI years, which is like one year, but obviously so much crypto infrastructure
*  has been built up and there's been this promise of smart contracts. And when I look at smart
*  contracts, I'm always like, well, they're typically limited by the limitations on the smart.
*  What we've had historically is like auto executing contracts, which has been labeled smart contracts,
*  but they're still kind of traditionally really constrained by just the fact that they're running
*  explicit code and explicit code is hard to make smart, especially around like real world complexity
*  use cases. Certainly when it comes to disputes, right? I mean, people are, there's a lot of dispute
*  resolution mechanisms kind of proposed for crypto, but in the end, it's like, as long as you're
*  relying on explicit code, it's a fairly brittle thing. And I might prefer to have recourse to
*  a human. Now it does seem like there's this opportunity to start to use language models
*  to help do some of this kind of on chain, trustless arbitration, dispute resolution of all sorts.
*  And this goes back to my, I was a member of the GPT-4 red team. One of the things that I tried in
*  that early testing was, this wasn't even really a red team thing, was just like, I was very interested
*  in this. Could we get GPT-4 to do basic mediation and dispute resolution? And sure enough, it's
*  quite good at that, especially as you look forward into a world of like multimodality
*  and other kinds of evidence being able to be brought to bear, besides just like the
*  testimony of different parties, then it really starts to look promising that you could have
*  first line dispute resolution powered by AI models, but then it really starts to matter,
*  what model are we running? And can we trust that? And who's doing this execution? So one way to do
*  it would obviously be to trust a third party. Even then though, if the stakes are high enough,
*  I might want to audit a somewhat trusted third party. I'd certainly want to have some ability
*  to do that in cases where it felt necessary. It seems like that is kind of coming online.
*  Why isn't that already here? Is it because this kind of work that you're doing has been the
*  bottleneck to date? I would love to hear more of your vision for the future of the additional
*  roles that language models and multimodal language models can play now that we have this additional
*  layer of guarantees. Yeah, I think that'd be really cool. There's a few challenges though.
*  So one challenge is the computation. So right now, if you think how much GPT-4 costs, you build a
*  cost up by 10,000, then- We're back to the cost of a human arbitrator.
*  You're back to the cost of a human arbitrator. Yeah, maybe a little bit under, but still it's
*  very, very expensive. I think the second thing though is that both parties have to agree to
*  a specific model and agree to the outcome. I think this gets quite challenging because the
*  specific way you phrase a prompt can result in different kinds of outputs. And there's a lot of
*  human complexities when it comes to things like contracts. I personally think that liars are going
*  to be the last people to be automated away because people don't like feeling like there's just a
*  random machine making decisions for your life. That's just my personal thing. I think
*  technologically speaking, the main blocker is just the cost.
*  So yeah, I think that's a very interesting question to debate and speculate about.
*  How much do you think the cost comes down? Because if GPT-4 is, let's say, whatever,
*  it's three cents per thousand input tokens, six cents per thousand output tokens, presumably that
*  they've got a long track record of reducing their prices. And that's obviously downstream of
*  ever increasing computational efficiency on their end from all sorts of different optimizations.
*  But okay, let's say four cents on average for per thousand tokens. If we do a 10,000x on that,
*  you're now looking at like 400 bucks, which again, is order of magnitude, human-powered
*  arbitration. Although yeah, probably still a little cheaper, although maybe we need more
*  than a thousand tokens too, depending on the situation. How much do you think you can bring
*  that down? Because it seems like the difference between 10,000x and even 100x is like the
*  difference between human arbitration level and a couple percent of human arbitration level, which
*  might be the whole game in terms of getting into a cost regime where maybe it's not that the
*  lawyers are automated away, but just that a whole new set of protections and interactions
*  are made possible that just previously there wasn't enough recourse to create the conditions
*  for people to transact in all sorts of different ways. That's a great question. And a lot of this
*  is active research, so it's very difficult to predict where the final numbers will be.
*  We do have some results, which we'll be releasing in a few months, which bring down the cost of
*  certain kinds of models pretty dramatically. So something like 10 to 100 times lower cost.
*  But transformers, so GPT-3, 4-style models are quite challenging due to the way the competition
*  is laid out. So the cost savings are unfortunately not quite as high. This is also something we're
*  actively looking into. And there's basically new developments both on the cryptography side
*  and also on how do you actually do this polynomial competition more efficiently side as well.
*  Things are changing literally every couple of weeks in this space. So sometimes it's hard to
*  guess where the final numbers will be. But hopefully in maybe a couple of years, the numbers
*  will be maybe 100 times more expensive. Yeah. And that does seem like it would be
*  really useful just in my own day-to-day commercial life. I've got an old house and it has
*  these idiosyncratic projects that it needs. And it's tough to engage an individual contractor
*  who might be good, might not. It's hard for them to develop a reputation. It's hard for us to agree
*  on should I pay this whole thing upfront? You may ghost me. There's all these kinds of friction
*  points. If I had some ability to enable order of magnitude $10 recourse, I do think that would be
*  pretty interesting and a huge enabler of all sorts of more decentralized peer-to-peer
*  commercial interactions. So I do find that super interesting, super promising.
*  A couple of the things that you've talked about in some of your other works that I think are
*  really interesting here too is the secure provenance of assets. So if I was going to hire
*  somebody to fix my plaster wall in an idiosyncratic way, I would probably want images. And I would
*  want those images to be reliably known when they were taken and maybe on what device they were
*  taken. It sounds like this is actually quite a bit farther along than probably most people
*  realize. So could you give us a little bit of... And this isn't exactly necessarily your work,
*  but I'd love to just ground this future possibility and also the fact that
*  we have, it sounds like pretty decent solutions for that kind of problem already too.
*  Yeah, this is one of these things which I am personally very passionate about, but somehow
*  trying to spread the word as much as possible. So given the rise of AI-generated images,
*  with existing technology, you just cannot tell if something is real or fake.
*  And the way to sidestep this is also cryptographic techniques, specifically what are called
*  attested sensors and for images, an attested camera. I also think that this is the way to
*  get around these things where you have to go to an orb somewhere and then trust some company that
*  they're not going to sell your iris information, which is apparently happening today.
*  So the way that an attested camera works is that you have a camera sensor, which basically takes
*  in light and then emits an electric signal, which is basically bits. And what you do is you put
*  a hardware device physically right next to the camera where the bits get rid of.
*  And then before those bits go anywhere else on your computer or anywhere else on the device,
*  it essentially hashes the inputs and computes a signature of the hash.
*  And so it's very difficult to forge these kinds of things. And so you can basically show that,
*  oh, I took an actual image of say my wall and this plaster. Now, there are also some mechanisms,
*  which I think are very interesting, which can be combined in a way that you can also,
*  approve is not the right word here. People will be mad if I use the word approve, but you can
*  be convinced that someone took an image at a particular time as well. And by combining these
*  along with say machine learning models, you can then do things as you mentioned, like dispute
*  mechanisms. Like, no, you promised the plaster would look like this, but the plaster actually
*  looks like that. So I want my money back. And that's one way that you can do this kind of
*  dispute resolution. And then the ML model can determine whether or not the plaster looks closer
*  to what they promised or whether or not it looks closer to something else. But besides that,
*  you can also, so going back way back to this conversation, I mentioned that I am interested
*  in a world where you can have privacy and not trust a bunch of people with these weird devices,
*  where you don't even know what's going on, but also prove authenticity. And the way to do this is that,
*  assuming Apple and Google and other phone manufacturers play ball, we can have a test
*  of cameras on every smartphone that's being produced in the future. And then you can basically take an
*  image of your face and say that, okay, I say, for example, batch image on a driver's license.
*  And you can do this using these ML models completely privately. Like as say, someone who is
*  trying to log onto a service, I can literally reveal that I can only reveal that I am a citizen
*  of the United States over the age of 21 and nothing else. And so this resolves privacy
*  concerns for consumers and also even perhaps resolves some concerns about data gravity and
*  privacy for service providers as well. So I'm hoping that this is not, I guess, more widely
*  adopted, especially these attested cameras. So the way that that would work, and this is kind
*  of an inversion, right? Because now we're saying we want, you know, use case we've primarily talked
*  about is a commercial model provider. You know, we want to be able to confirm in an individual case
*  or kind of audit generally that they're doing what they said they were going to do. Similarly,
*  you know, in a context of like a dispute resolution, if it really matters to me, I want to be sure that
*  like the, you know, the evaluating model that I agreed to use is the one that is in fact being
*  used. In those cases, like I, as the consumer, don't have access to the weights. But now in this other
*  scenario where I'm trying to prove my humaneness, all that stuff is now happening on device, right?
*  So instead, basically, my iPhone is running a process that is using like some ML model trained
*  by, you know, whoever can be the government or Apple or whatever that that allows it to export
*  a proof of something being human or something, you know, being attached to certain information,
*  doing that in a way that doesn't reveal the inputs. So in this case, the model weights would maybe be
*  known to all parties, but the inputs that I used are not, but I can still get to the point where
*  it's like, okay, yes, so this computation was run and therefore, you know, we can trust this individual
*  user, you know, took a live photo of their face or whatever. Yeah, exactly. That, that, you, the model
*  weights here would be known to both, but the inputs will only be known as a person taking the picture.
*  I mean, a couple of little detailed questions and maybe just zooming out again to close. How does
*  this change if we relax certain restrictions or kind of constraints on the problem? Like, if we were
*  to say, instead of, you know, hypothesizing an open AI as the model provider, what if, you know,
*  you know, me and my home contractor agreed to some kind of open situation where the model that
*  we're agreeing to use is kind of known to us. Like we, you know, there's a canonical version where
*  we have the weights. In that case, you know, I was just kind of thinking thought experiment, like,
*  I guess worst case, we could both run the model and kind of, you know, compare and contrast that way.
*  In an open source model context, is there a need for this? I guess there would still be, you know,
*  to preserve my own inputs to a certain degree, but help me kind of understand that. Because
*  obviously the open source, I wouldn't say it's quite catching up, but it's certainly achieving
*  all sorts of new milestones where, you know, llama three might be perfectly good for,
*  for various forms of dispute resolution. And, you know, we'll probably have those weights.
*  So with this new resolution in particular, like you can each individually just run the model.
*  But the problem is that if you have a smart contract arbitrating the dispute mechanism,
*  like a smart contract needs to be able to run the model, so to speak. And as you pointed out,
*  smart contracts running standard code is very expensive. So the zero knowledge proof here would
*  just be used to basically confirm the smart contract that the model ran in a particular way.
*  Also, because these zero knowledge proofs can ensure privacy, you also might imagine if you
*  are publishing something to a smart contract that's publicly on the blockchain, you might
*  want to not say post pictures of the inside of your house publicly, so that you can instead
*  do that privately. And so there are other reasons why you might want to use these mechanisms
*  regardless of whether or not you're using an open source model or not.
*  I mean, my crystal ball gets very foggy after the next six months. The fact that you are
*  doing this work suggests, you know, a vision into the future that's it. You know, and I don't want
*  to suggest that you are overconfident in your predictions, but you definitely have a point of
*  view as to kind of where the world is going and what is needed. Could you kind of, you know,
*  sketch out a little bit more how you think this impacts daily life? Like, are we interacting with
*  these things all the time a few years from now? Does this pose a challenge to, you know, conventional
*  legal systems if, you know, because that's been the promise of blockchain, but obviously hasn't
*  really materialized. But, you know, again, you put the smart in smart contract, things might
*  actually get pretty interesting. I'd love to hear your just kind of, you know, license to speculate.
*  Granted, you know, tell me what you think we have in store for us.
*  That's a great question. I wish I had crystal ball, you know, by Bitcoin and tights followed it not.
*  But let me take a step back. If you think about how cryptographic techniques are deployed today,
*  they're basically deployed in ways that you and I don't really think about on a day-to-day basis.
*  So we're recording this on a platform called Riverside. And there's this like
*  lock that you see in your browser, which says that I have a secure connection to Riverside.
*  And the underlying technology is called TLS, HTTPS. This is all run without you and I ever
*  really thinking about this. I'm hoping that if the cost come down enough, it's basically the same
*  thing. So for high stakes situations, like you just don't even want to think about it. It'll just like,
*  integrated everywhere. So if you take up an image of an X-ray or like a CAT scan or something,
*  they'll just be like a sign, a sign device there. It'll sign what comes off. You send it to the
*  MIME model. The MIME model will produce a proof. So this is all auditable. You can always go back
*  and just check what happened, which will make medical disputes not as much easier. But on a
*  day-to-day basis, assuming everything is done properly, I don't even have to think about it.
*  Similarly, for these smart contracts, the goal would be to make it so that disputes can be
*  done automatically and ideally in a much cheaper way. I mean, if you look at the cost of wires,
*  high powered ones, they're quite expensive. So if there are any ways you can reduce the cost and
*  allow everyday people to use these technologies in this automatic way, I think that's what's
*  moving towards. But in order for that vision to happen, the costs need to come down quite
*  dramatically. We need to convince the hardware manufacturers to include these siding units,
*  which can be quite expensive onto your phones, say. But I think that as generative AI becomes
*  stronger in terms of those capabilities, hopefully we will move towards this vision.
*  What is the cost profile for these on-device mechanisms?
*  And then I'm also wondering, obviously there's a lot of societal concern around
*  deep fakes and information, disinformation, scanning. We got spearfishing attacks on the rise.
*  Does this seem like a policy intervention that might have legs? I mean, again, the cost will
*  be pretty critical there, but people are looking, I think, very actively right now for
*  what are things that we could mandate that would give us some assurances about the future?
*  And people are looking at choke points. In the AI safety discourse, it's like, well, hey,
*  maybe we can sort of engineer certain things into the GPUs so that if they're ever part of a super
*  big cluster, they'll phone home and tell people about it. And we'll see if that ever materializes.
*  But here there's something kind of similar where there is a serious choke point in a major couple
*  choke points. There's only a few really big device manufacturers for, say, cell phones on which the
*  majority of the images are now captured. If the cost was reasonable and it wasn't too onerous,
*  it does seem like there could be an intervention there where you could imagine a new regulation
*  that would say, hey, Apple, Google, Android, whatever, you guys, you want to sell these things,
*  you got to have this capability on there. I don't know if it would be the kind of thing that would
*  be annoying on a daily basis. The cost could be hardware costs. It could be runtime cost for each
*  image. It could be that I can't take 10 pictures a second anymore and I can only take how many
*  pictures. I'd love to understand those costs a little bit better and whether you think this is
*  headed for a possibility of a mandate of some of these technologies just to try to keep control
*  on the information environment. That's a great question. There's several costs here. There's
*  a hardware cost and there's also costs of, say, when you're taking photos live. Maybe to address
*  the second one first, it's very easy to put bypass mechanism. You don't always have to go through the
*  signing channel. You can basically engineer these things such that if I want to take pictures
*  normally without this special thing going on, I can just do it. From a user perspective, no cost at
*  all. From a hardware perspective, I can tell you actually that the Apple does come with what's
*  called a secure enclave already. It's just not hooked up to the camera in a way that developers
*  can access. Basically, we need to change that. They just need to hook up the secure enclave to the
*  camera and allow some programmatic access. The reason that they haven't done this is because,
*  as you point out, there's no mandate to. It does cost a bit extra in terms of engineering
*  time and a little bit extra in terms of manufacturing costs. This does sound like
*  a perfect place for regulation to, or at the very least, nudge them in the right direction.
*  If any of your listeners or yourself happen to know people who want to think about this,
*  I would love to chat with them because I personally think that we should be moving to
*  a world where we should have the option to authenticate any kind of media, whether it be
*  audio, video, images, or otherwise, to fight against things like generative AI. This is something that
*  these hardware manufacturers know how to do already. They just haven't because of the costs,
*  which sounds like a great place for regulation. In dollar values, do you have a sense,
*  go pay $1,000 retail for an iPhone? They're obviously making some healthy profits on that.
*  It seems like if this was a $1 hard cost to Apple, it would be pretty easily absorbed in the system.
*  Obviously, they're selling a lot of units, but still, it's not a big deal. If it was 100,
*  you'd probably get real pushback. Do you have any idea what that incremental would be?
*  This is one of these things where people have very wildly different opinions.
*  Apple is the one who knows their internal is the best, but if I had to speculate, I would say
*  very marginal. They literally already have a secure enclave on every iPhone that's produced
*  today. It just needs to be wired in the correct way. It's not that expensive to do that. Maybe in
*  the $1 to $10 additional cost is my guess. Fascinating, really. Any other kind of visions
*  for the future you want to tease or anything else that we didn't get to that you want to make sure
*  the audience understands? Maybe just the previous and upcoming stuff. I mentioned already we're
*  going to be publishing work in the next few months that will reduce the cost for certain
*  kinds of models quite dramatically. We'll also reduce really some work also hopefully in the
*  upcoming months on how to audit ML models in a very specific way. That's all I had in mind.
*  Professor Daniel Kang, thank you for being part of the cognitive revolution.
*  Thank you for having me. This was a lot of fun. It is both energizing and enlightening to hear
*  why people listen and learn what they value about the show. So please don't hesitate to reach out
*  via email at tcr at turpentine.co or you can DM me on the social media platform of your choice.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike
*  so much that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
