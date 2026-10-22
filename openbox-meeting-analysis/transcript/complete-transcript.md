# OpenBox AI developer meeting — complete timestamped transcript

**Recording:** 21 October 2026  
**Duration:** 01:30:34.042  
**Coverage:** Complete local-ASR pass over the full recording; 1,361 retained speech segments  
**Speakers:** Five participant names are visible in the meeting UI, but full acoustic diarization was unavailable. To avoid false attribution, transcript turns are labelled `Speaker (unattributed)`.  
**Method:** Local Faster-Whisper base, CPU/int8, Silero VAD. No media was uploaded.  
**Uncertainty:** `[ASR uncertain]` marks low-confidence segments. Minimal spelling normalization was applied only for high-confidence product/technology names; the raw ASR is retained in `transcript.json`. Segment timestamps are approximate.

Visible participant names: Tahir Mahmood, Aswin Kumar, Asim Ahmad, Bharat J, and Bi Vu. Visibility does not by itself justify assigning every utterance to a named speaker.

---

[00:00:02–00:00:38] **Speaker (unattributed):** Where's the note from a marketing perspective? A lot of other people when they think of these names, they are not so, you could say English about it as in the word isn't like describing like what's in the 10. It's not so descriptive. They tend to be like make it seem like something magical or big. I've been able to come up with the sub-brands. I have no intention of coming up with them. [ASR uncertain]

[00:00:38–00:00:46] **Speaker (unattributed):** group, they leave the name to me. Yeah. Okay. So to give an example, the goal on Friday at 8am

[00:00:46–00:00:53] **Speaker (unattributed):** Eastern time is to actually go out and announce that, you know, OpenBox is on AWS marketplace,

[00:00:53–00:00:58] **Speaker (unattributed):** because that's again, a social proof. And to be there, people know it's not just a question of

[00:00:58–00:01:03] **Speaker (unattributed):** building an app and sending it. It is quite good. And the website be ready for us to do it, or you

[00:01:03–00:01:07] **Speaker (unattributed):** I don't mind it not to be ready.

[00:01:07–00:01:09] **Speaker (unattributed):** As we just cannot wait.

[00:01:09–00:01:10] **Speaker (unattributed):** We have to...

[00:01:10–00:01:12] **Speaker (unattributed):** Well, all of this is being done.

[00:01:12–00:01:14] **Speaker (unattributed):** We need to build the momentum.

[00:01:14–00:01:18] **Speaker (unattributed):** And I've got a plan I've been discussing with Bion,

[00:01:18–00:01:21] **Speaker (unattributed):** especially with Ashwin and Omi.

[00:01:21–00:01:23] **Speaker (unattributed):** So we're going to start hitting it.

[00:01:23–00:01:25] **Speaker (unattributed):** And then the website will catch up.

[00:01:25–00:01:26] **Speaker (unattributed):** But we just can't wait.

[00:01:26–00:01:30] **Speaker (unattributed):** So the example here is, well, we put together is again,

[00:01:30–00:01:32] **Speaker (unattributed):** a page, which will be...

[00:01:32–00:01:39] **Speaker (unattributed):** So basically, you know, OpenBox AI, maybe OpenBox AWS, I don't know what it's going to be up here.

[00:01:39–00:01:45] **Speaker (unattributed):** But Ender is now available on AWS marketplace, Gov.AI agents inside your AWS account.

[00:01:45–00:01:52] **Speaker (unattributed):** Now, interesting enough, we know it doesn't have to be AWS, but you're selling a product within AWS.

[00:01:52–00:01:56] **Speaker (unattributed):** And he did a lot of competitive analysis and other stuff as well.

[00:01:56–00:02:00] **Speaker (unattributed):** And you know, if you OpenBox and AWS marketplace, you click it, book a demo,

[00:02:00–00:02:05] **Speaker (unattributed):** you know blah blah blah all this stuff buy OpenBox for your AWS account what are the benefits you

[00:02:05–00:02:12] **Speaker (unattributed):** would get if you did that build for AWS procurement to runtime native deployment south host date runtime blah blah

[00:02:13–00:02:19] **Speaker (unattributed):** build to run any inside your account not hours how we would how would you achieve it blah blah blah

[00:02:19–00:02:25] **Speaker (unattributed):** works with your agent stack you already know use again repeating it glang bang bang all the things that

[00:02:25–00:02:27] **Speaker (unattributed):** that you work five phases authorization,

[00:02:27–00:02:29] **Speaker (unattributed):** start governing your agents on AWS.

[00:02:29–00:02:30] **Speaker (unattributed):** blah blah blah.

[00:02:30–00:02:33] **Speaker (unattributed):** So you see this, and again, you know,

[00:02:33–00:02:36] **Speaker (unattributed):** a pair of platform docs pricing,

[00:02:36–00:02:39] **Speaker (unattributed):** it's all like a product, right?

[00:02:39–00:02:42] **Speaker (unattributed):** So what we're doing is, is we're going to start

[00:02:42–00:02:45] **Speaker (unattributed):** turning the whole website, rather than doing a,

[00:02:45–00:02:48] **Speaker (unattributed):** you know, one day it changes overnight.

[00:02:48–00:02:51] **Speaker (unattributed):** We're just gonna start adding these pages

[00:02:51–00:02:54] **Speaker (unattributed):** and get, you know, get the momentum going.

[00:02:54–00:03:00] **Speaker (unattributed):** So at least when people come, they'll see it that there is a product, a different product.

[00:03:00–00:03:07] **Speaker (unattributed):** So if somebody comes in there, somehow come to the site and go, oh, AWS marketplace.

[00:03:07–00:03:08] **Speaker (unattributed):** Oh, right.

[00:03:08–00:03:11] **Speaker (unattributed):** And what is it that you're buying in the AWS marketplace?

[00:03:11–00:03:13] **Speaker (unattributed):** At least it starts the journey.

[00:03:13–00:03:15] **Speaker (unattributed):** So I'll come back to that.

[00:03:15–00:03:19] **Speaker (unattributed):** This is sort of as an example of the way we're going to start moving forward.

[00:03:19–00:03:24] **Speaker (unattributed):** And it seems like, as you said, you've always seen this as the way forward.

[00:03:24–00:03:28] **Speaker (unattributed):** and we just haven't latched on to it and done it.

[00:03:28–00:03:32] **Speaker (unattributed):** Okay, but the one I want to discuss is, okay.

[00:03:32–00:03:36] **Speaker (unattributed):** So obviously, we need to start making money.

[00:03:36–00:03:40] **Speaker (unattributed):** And it's obvious that it doesn't matter how many doors we knock on

[00:03:40–00:03:42] **Speaker (unattributed):** when it comes to enterprise,

[00:03:42–00:03:46] **Speaker (unattributed):** none of that's going to result with the money in the bank tomorrow.

[00:03:46–00:03:50] **Speaker (unattributed):** The only place we can make money in the bank tomorrow

[00:03:50–00:03:53] **Speaker (unattributed):** is this side which is what we've been calling it, the left shift.

[00:03:53–00:03:56] **Speaker (unattributed):** I call it OpenBoxKate right now.

[00:03:56–00:03:59] **Speaker (unattributed):** This is the place where I believe we can make money.

[00:03:59–00:04:00] **Speaker (unattributed):** Now, when I say make money,

[00:04:00–00:04:02] **Speaker (unattributed):** one of the things that I've done is,

[00:04:02–00:04:04] **Speaker (unattributed):** I've sent a document to

[00:04:06–00:04:09] **Speaker (unattributed):** what's his name, Sam.

[00:04:09–00:04:13] **Speaker (unattributed):** Let me just get that document up one second.

[00:04:13–00:04:18] **Speaker (unattributed):** Where is it?

[00:04:18–00:04:22] **Speaker (unattributed):** Okay, yeah, here we go.

[00:04:22–00:04:28] **Speaker (unattributed):** Just get this up a little bit.

[00:04:28–00:04:36] **Speaker (unattributed):** Yeah, got it here.

[00:04:36–00:04:38] **Speaker (unattributed):** Okay, let me just show my screen.

[00:04:44–00:04:46] **Speaker (unattributed):** Okay, let me know when you can see

[00:04:46–00:04:56] **Speaker (unattributed):** this one. Yeah. Okay. So the idea behind here is OpenBox AI is a runtime governance in

[00:04:56–00:05:01] **Speaker (unattributed):** a test station platform for agents. It intercepts agent actions inside framework blah blah blah blah blah all

[00:05:01–00:05:09] **Speaker (unattributed):** the bullshit. The proposal under review is to open source the enforcement core. The PEP and the

[00:05:09–00:05:15] **Speaker (unattributed):** verdict a test station format under OSI approve license while keeping the decision plane control

[00:05:15–00:05:21] **Speaker (unattributed):** and as Testation Verification Service proprietary, a classic open-core split.

[00:05:21–00:05:27] **Speaker (unattributed):** So, the idea is that there's parts of our platform which we want to open source

[00:05:27–00:05:33] **Speaker (unattributed):** and this is just defining Peppies policy enforcement point, PDP is policy decision point.

[00:05:33–00:05:41] **Speaker (unattributed):** And all of these come from all of us, borrowed from all of these standards, to these standard words.

[00:05:41–00:05:50] **Speaker (unattributed):** So the idea behind it is that we open source parts of our software that get says into where

[00:05:50–00:05:52] **Speaker (unattributed):** people can see what we're doing.

[00:05:52–00:05:58] **Speaker (unattributed):** And certainly when it comes to a testing, the test station part should be done by the other

[00:05:58–00:06:03] **Speaker (unattributed):** parties so they can see it and it's visible and so forth.

[00:06:03–00:06:08] **Speaker (unattributed):** So all this does is market evidence licensing lessons learned, how people screwed up when

[00:06:08–00:06:14] **Speaker (unattributed):** they did it the wrong way. They did it very open and then try to make it narrow when really you

[00:06:14–00:06:21] **Speaker (unattributed):** should start narrow and open it up. And basically what this document talks about is how we will start

[00:06:21–00:06:29] **Speaker (unattributed):** narrow and open it up as we go along. And I've asked Sam to review this document and look at the

[00:06:29–00:06:35] **Speaker (unattributed):** strategy proposed in here on what sort of licensing and blah blah blah we should be putting together

[00:06:35–00:06:39] **Speaker (unattributed):** and he said, you know, since it's not that big, he'll take a look at it and come back to me

[00:06:39–00:06:47] **Speaker (unattributed):** hopefully tomorrow. So all this does is, is basically say that what we do is a couple of things

[00:06:47–00:06:55] **Speaker (unattributed):** moving forward. Things like taking parts of our code base and open sourcing it with the right

[00:06:55–00:07:02] **Speaker (unattributed):** license is the right way to go, and especially the parts which are to do with building trust.

[00:07:02–00:07:09] **Speaker (unattributed):** Right? How is somebody going to trust today if you're using our SaaS-based platform and

[00:07:09–00:07:16] **Speaker (unattributed):** we are doing the certification? Well, who are we to certify that the logs, the

[00:07:16–00:07:24] **Speaker (unattributed):** Merkel routes and the attestation is not, is valid? We're not. Is there a third party that is more

[00:07:24–00:07:29] **Speaker (unattributed):** trusted? Blah blah blah. These are the sort of questions, you know, I've been working through.

[00:07:29–00:07:36] **Speaker (unattributed):** And my goal was I realized that one of the things we have to fix is the part which is we really

[00:07:36–00:07:42] **Speaker (unattributed):** should be a company that is heading towards open source. And I think we put it quite nicely

[00:07:42–00:07:49] **Speaker (unattributed):** where he referred to the use case of temporal and the use case of Microsoft governance and

[00:07:49–00:07:50] **Speaker (unattributed):** everybody else.

[00:07:50–00:07:56] **Speaker (unattributed):** Elwam Microsoft over the last couple of years always had an open source first strategy, which

[00:07:56–00:07:58] **Speaker (unattributed):** which is they said, you know,

[00:07:58–00:08:00] **Speaker (unattributed):** apart from our office suite of applications,

[00:08:00–00:08:03] **Speaker (unattributed):** we will always provide open source of everything

[00:08:03–00:08:08] **Speaker (unattributed):** and then any services or things that we add to that open source,

[00:08:08–00:08:12] **Speaker (unattributed):** which we believe is our IP that we don't want to open source.

[00:08:12–00:08:15] **Speaker (unattributed):** It's available in the open source platform,

[00:08:15–00:08:18] **Speaker (unattributed):** but it's payable, you get to pay for it.

[00:08:18–00:08:23] **Speaker (unattributed):** Or if you want us to host and run this open source platform

[00:08:23–00:08:28] **Speaker (unattributed):** because we built it and you don't have the people or the power or you don't want to maintain

[00:08:28–00:08:34] **Speaker (unattributed):** it from a worry of security floors or bugs which you can't fix and you don't have those teams,

[00:08:34–00:08:40] **Speaker (unattributed):** then obviously come back to us. And that really is the way we should go because the whole

[00:08:40–00:08:46] **Speaker (unattributed):** of the industry is going down that which is why I said everybody signs up to the Linux foundation.

[00:08:48–00:08:52] **Speaker (unattributed):** Yeah, but we're still in the stuff. But one thing to note, we've kind of hijacked the

[00:08:52–00:08:54] **Speaker (unattributed):** the call a bit, but it's because it's to do it.

[00:08:54–00:08:56] **Speaker (unattributed):** We are talking full on strategy.

[00:08:56–00:08:57] **Speaker (unattributed):** And I wanted you in it.

[00:08:57–00:08:59] **Speaker (unattributed):** So I told them to pose.

[00:08:59–00:09:02] **Speaker (unattributed):** And if there's anything, and I know for sure,

[00:09:02–00:09:04] **Speaker (unattributed):** there are things that even I want to cover,

[00:09:04–00:09:06] **Speaker (unattributed):** which is this me, you and Tahir.

[00:09:06–00:09:08] **Speaker (unattributed):** We can always cover that straight after this

[00:09:08–00:09:10] **Speaker (unattributed):** or another time if you're busy after this,

[00:09:10–00:09:14] **Speaker (unattributed):** but we should be able to stay on longer.

[00:09:14–00:09:16] **Speaker (unattributed):** But I'll give the floor back to Tahir.

[00:09:16–00:09:18] **Speaker (unattributed):** Maybe Tahir, you want to recap a little bit,

[00:09:18–00:09:20] **Speaker (unattributed):** even though we're deliberately recording

[00:09:20–00:09:24] **Speaker (unattributed):** in transcribing this session so you can have the nods.

[00:09:24–00:09:25] **Speaker (unattributed):** Yeah, no, no problem.

[00:09:25–00:09:30] **Speaker (unattributed):** Anyway, what I've been doing over the last sort of

[00:09:30–00:09:33] **Speaker (unattributed):** since I came back from San Francisco is, you know,

[00:09:33–00:09:36] **Speaker (unattributed):** I put on my CMO hat completely and sort of said,

[00:09:36–00:09:38] **Speaker (unattributed):** you know, what is it that we need

[00:09:38–00:09:41] **Speaker (unattributed):** that will allow us to generate revenue

[00:09:41–00:09:43] **Speaker (unattributed):** and what will be the right strategy

[00:09:43–00:09:45] **Speaker (unattributed):** for Earth going forward with our code?

[00:09:45–00:09:48] **Speaker (unattributed):** That obviously what I did was I started pretty much

[00:09:48–00:09:54] **Speaker (unattributed):** this session a little bit earlier, but I started it with, let me just stop and show you again, stop.

[00:09:54–00:10:03] **Speaker (unattributed):** So if I show my screen. So I went back to the map, the, you know, the map,

[00:10:03–00:10:08] **Speaker (unattributed):** my map that you've got to see. And from here, what I tried to explain is that, you know, we have

[00:10:09–00:10:15] **Speaker (unattributed):** an enormous amount of capability and features, and it's almost impossible to traverse and find

[00:10:15–00:10:20] **Speaker (unattributed):** what it is that the product is about and what benefits it brings blah blah blah.

[00:10:20–00:10:27] **Speaker (unattributed):** So what we've been, so outside of everything else, what came very clear and very visible is that

[00:10:27–00:10:32] **Speaker (unattributed):** what we need to do is productize the whole platform. And what I mean by productizing it is

[00:10:32–00:10:39] **Speaker (unattributed):** what we end up doing is we take parts of the platform and go, you know what,

[00:10:39–00:10:43] **Speaker (unattributed):** But what we've been calling shift left,

[00:10:43–00:10:48] **Speaker (unattributed):** and hopefully that's popped up on your screen.

[00:10:48–00:10:49] **Speaker (unattributed):** Yeah.

[00:10:49–00:10:50] **Speaker (unattributed):** OK.

[00:10:50–00:10:54] **Speaker (unattributed):** Here is a mockup of a product called OpenBoxGate,

[00:10:54–00:10:59] **Speaker (unattributed):** a sub brand, to do with what we've been calling shift

[00:10:59–00:11:01] **Speaker (unattributed):** left, which is basically all the things

[00:11:01–00:11:04] **Speaker (unattributed):** that you offer a coding editor.

[00:11:04–00:11:07] **Speaker (unattributed):** And it's not no words like shift left, blah, blah, blah.

[00:11:07–00:11:09] **Speaker (unattributed):** It's literally, as an example,

[00:11:09–00:11:11] **Speaker (unattributed):** it's a policy gait for coding agents.

[00:11:11–00:11:14] **Speaker (unattributed):** let the agents run, keep the boundaries yours.

[00:11:14–00:11:15] **Speaker (unattributed):** Right?

[00:11:15–00:11:18] **Speaker (unattributed):** You know, I've been trying to come up with messaging and wording,

[00:11:18–00:11:21] **Speaker (unattributed):** and then basically it says how it works,

[00:11:21–00:11:26] **Speaker (unattributed):** integrations, policies, how the work and community documentation.

[00:11:27–00:11:31] **Speaker (unattributed):** So basically if somebody comes to our website,

[00:11:31–00:11:36] **Speaker (unattributed):** the homepage will literally be to navigate you

[00:11:36–00:11:38] **Speaker (unattributed):** to the product you're looking for.

[00:11:38–00:11:41] **Speaker (unattributed):** Okay, so to give you another example,

[00:11:41–00:11:42] **Speaker (unattributed):** following on from that.

[00:11:42–00:11:47] **Speaker (unattributed):** So we are gonna announce on Friday,

[00:11:47–00:11:49] **Speaker (unattributed):** Eastern time, 8 AM,

[00:11:50–00:11:54] **Speaker (unattributed):** which is what we're gonna do.

[00:11:54–00:11:58] **Speaker (unattributed):** So basically what we wanna do is,

[00:11:58–00:12:00] **Speaker (unattributed):** oh, what we can do, where is it?

[00:12:00–00:12:05] **Speaker (unattributed):** Let me just share.

[00:12:05–00:12:08] **Speaker (unattributed):** So what OME did is, he put together,

[00:12:10–00:12:11] **Speaker (unattributed):** let me know if you can see it.

[00:12:11–00:12:13] **Speaker (unattributed):** No.

[00:12:13–00:12:15] **Speaker (unattributed):** Okay, so OME put together something

[00:12:15–00:12:19] **Speaker (unattributed):** which regarding AWS when we announced

[00:12:19–00:12:22] **Speaker (unattributed):** that we are on AWS marketplace,

[00:12:22–00:12:25] **Speaker (unattributed):** we're actually selling it as a product, right?

[00:12:25–00:12:30] **Speaker (unattributed):** You know, government AI agents inside your AWS account, right?

[00:12:30–00:12:32] **Speaker (unattributed):** So that, so you know, somebody you can come

[00:12:32–00:12:35] **Speaker (unattributed):** and go, you know, what is this product in AWS?

[00:12:35–00:12:39] **Speaker (unattributed):** We're selling you governance inside your AWS account

[00:12:39–00:12:41] **Speaker (unattributed):** and then obviously we can explain all of us

[00:12:41–00:12:42] **Speaker (unattributed):** as in aspects.

[00:12:42–00:12:45] **Speaker (unattributed):** But I guess in the shortest way,

[00:12:45–00:12:47] **Speaker (unattributed):** what I'm trying to describe is,

[00:12:47–00:12:51] **Speaker (unattributed):** and you know, Asim quite rightly said that back in November,

[00:12:51–00:12:52] **Speaker (unattributed):** not November,

[00:12:54–00:12:57] **Speaker (unattributed):** before we launched the company and the product in March

[00:12:57–00:13:00] **Speaker (unattributed):** of this year, Asim was of the view

[00:13:00–00:13:04] **Speaker (unattributed):** that we should have productized that what we're building.

[00:13:04–00:13:07] **Speaker (unattributed):** Now at that time, it was really just an SDK

[00:13:07–00:13:09] **Speaker (unattributed):** and a call back end.

[00:13:09–00:13:11] **Speaker (unattributed):** So there wasn't a lot,

[00:13:11–00:13:13] **Speaker (unattributed):** but you know, we could have done a better job,

[00:13:13–00:13:16] **Speaker (unattributed):** but obviously we're trying to fix that right now.

[00:13:16–00:13:20] **Speaker (unattributed):** So the strategy is that the whole of the platform

[00:13:20–00:13:24] **Speaker (unattributed):** and everything that is done is broken down into sub brands

[00:13:24–00:13:27] **Speaker (unattributed):** and I'll get us him to start working on the sub brands

[00:13:27–00:13:29] **Speaker (unattributed):** but over the next day or two,

[00:13:29–00:13:31] **Speaker (unattributed):** I will break the whole of everything we have

[00:13:31–00:13:35] **Speaker (unattributed):** that's in that mind map down into what are the products

[00:13:35–00:13:37] **Speaker (unattributed):** and what are the benefits and features

[00:13:37–00:13:39] **Speaker (unattributed):** each one of those products offer.

[00:13:39–00:13:41] **Speaker (unattributed):** So when a user,

[00:13:41–00:13:43] **Speaker (unattributed):** or when we're selling the company

[00:13:43–00:13:45] **Speaker (unattributed):** and we're selling the,

[00:13:45–00:13:47] **Speaker (unattributed):** what is not one big,

[00:13:47–00:13:48] **Speaker (unattributed):** very much of a product,

[00:13:48–00:13:51] **Speaker (unattributed):** we're selling these sub brands.

[00:13:51–00:13:53] **Speaker (unattributed):** So if you meet a developer,

[00:13:53–00:13:55] **Speaker (unattributed):** you're selling OpenBox gates

[00:13:55–00:13:57] **Speaker (unattributed):** if that's what it's gonna be called.

[00:13:57–00:13:58] **Speaker (unattributed):** If you're, if you,

[00:13:58–00:14:00] **Speaker (unattributed):** you know, somebody says,

[00:14:00–00:14:01] **Speaker (unattributed):** you know, AWS,

[00:14:01–00:14:03] **Speaker (unattributed):** you can sell them, we're on marketplace.

[00:14:03–00:14:05] **Speaker (unattributed):** And from there you can buy our product

[00:14:05–00:14:06] **Speaker (unattributed):** and you can blah, blah, blah,

[00:14:06–00:14:08] **Speaker (unattributed):** look at all the lovely things you get

[00:14:08–00:14:11] **Speaker (unattributed):** from the advantage of being on marketplace.

[00:14:11–00:14:13] **Speaker (unattributed):** aside from just the governance and all the other things

[00:14:13–00:14:14] **Speaker (unattributed):** that you get from it.

[00:14:14–00:14:17] **Speaker (unattributed):** Similarly, as we walk into it, now,

[00:14:17–00:14:20] **Speaker (unattributed):** the earlier demonstrated two new features

[00:14:20–00:14:21] **Speaker (unattributed):** that are gonna be added,

[00:14:21–00:14:24] **Speaker (unattributed):** which is basically building policies with natural language

[00:14:24–00:14:28] **Speaker (unattributed):** and also having it that at the end of a session

[00:14:28–00:14:30] **Speaker (unattributed):** when an agent's finished its session

[00:14:30–00:14:35] **Speaker (unattributed):** and is generated a Merkel route or a receipt of a testation,

[00:14:35–00:14:43] **Speaker (unattributed):** There's a security context or security review that is done which sort of says, you know, this session,

[00:14:43–00:14:52] **Speaker (unattributed):** when you map it to the all-wast framework, you know, your agent from a security point of view might not have done very well,

[00:14:52–00:14:54] **Speaker (unattributed):** or it is done well.

[00:14:54–00:14:56] **Speaker (unattributed):** And again, I'll leave at a different time.

[00:14:56–00:14:59] **Speaker (unattributed):** I don't want him to go through it all over again. He's already done it twice.

[00:14:59–00:15:03] **Speaker (unattributed):** But about that leave beach, sort of, catch up and bring you up to speed.

[00:15:03–00:15:08] **Speaker (unattributed):** So this idea of natural language, creating evals,

[00:15:08–00:15:13] **Speaker (unattributed):** evals providing non-deterministic response to whatever,

[00:15:13–00:15:17] **Speaker (unattributed):** even to the point of us telling you in the security reviews,

[00:15:17–00:15:22] **Speaker (unattributed):** your security was really bad for that step function of what the agent did.

[00:15:22–00:15:25] **Speaker (unattributed):** And you should add more policies, more guardrails,

[00:15:25–00:15:26] **Speaker (unattributed):** you should add whatever.

[00:15:26–00:15:30] **Speaker (unattributed):** It really does help you and guide you as to what you need to do,

[00:15:30–00:15:31] **Speaker (unattributed):** really clever stuff. Okay.

[00:15:31–00:15:36] **Speaker (unattributed):** So I'm going to come back to this as a high level.

[00:15:36–00:15:39] **Speaker (unattributed):** That is what you're going to see me doing to the website.

[00:15:39–00:15:42] **Speaker (unattributed):** But by next week, I'm going to be productizing it with us

[00:15:42–00:15:46] **Speaker (unattributed):** himself. And again, I'm happy to have you help out,

[00:15:46–00:15:50] **Speaker (unattributed):** which is it will be the homepage will be your land on it.

[00:15:50–00:15:54] **Speaker (unattributed):** And it won't be anything but we have a bunch of products.

[00:15:54–00:15:57] **Speaker (unattributed):** It would simple notes of this product.

[00:15:57–00:15:59] **Speaker (unattributed):** There's this, this, this, this, which one are you after?

[00:15:59–00:16:01] **Speaker (unattributed):** which what are you?

[00:16:01–00:16:03] **Speaker (unattributed):** Are you a C-SO? Are you a developer?

[00:16:03–00:16:04] **Speaker (unattributed):** Are you a whatever?

[00:16:04–00:16:07] **Speaker (unattributed):** It should help you start that journey in a very simple

[00:16:07–00:16:11] **Speaker (unattributed):** and my goal is that I'm not interested in making the homepage

[00:16:11–00:16:13] **Speaker (unattributed):** anything more than one page.

[00:16:13–00:16:15] **Speaker (unattributed):** You shouldn't even need to scroll.

[00:16:15–00:16:17] **Speaker (unattributed):** And if you need to scroll,

[00:16:17–00:16:20] **Speaker (unattributed):** you're scrolling down to the footer and that's it.

[00:16:20–00:16:24] **Speaker (unattributed):** So all the other shit that's on our website, it will be gone.

[00:16:24–00:16:28] **Speaker (unattributed):** Yeah. I love that perspective of

[00:16:28–00:16:33] **Speaker (unattributed):** of product centric because the mind map you have is very compelling.

[00:16:33–00:16:35] **Speaker (unattributed):** That's how bees educated me on the product.

[00:16:35–00:16:40] **Speaker (unattributed):** Most companies websites stay here and there's so many features

[00:16:40–00:16:46] **Speaker (unattributed):** and so much capability and so many use cases and industries that we can solve for.

[00:16:46–00:16:49] **Speaker (unattributed):** So for example, here I love the policy gate for coding it.

[00:16:49–00:16:54] **Speaker (unattributed):** It's like a very clear mission for this product line or this particular use case

[00:16:54–00:16:56] **Speaker (unattributed):** or this particular message, if you will,

[00:16:56–00:16:59] **Speaker (unattributed):** as a marketing package, if you will,

[00:16:59–00:17:01] **Speaker (unattributed):** you attack that market.

[00:17:01–00:17:04] **Speaker (unattributed):** Most companies' websites have a product page,

[00:17:04–00:17:07] **Speaker (unattributed):** then they have a solutions page, and over time,

[00:17:07–00:17:09] **Speaker (unattributed):** and solutions could be use cases,

[00:17:09–00:17:11] **Speaker (unattributed):** and over time they get into industries.

[00:17:11–00:17:15] **Speaker (unattributed):** And in our case, because of the governance bent,

[00:17:16–00:17:18] **Speaker (unattributed):** and personas, of course, matter,

[00:17:18–00:17:21] **Speaker (unattributed):** but personas sometimes get sorted through in a meeting

[00:17:21–00:17:24] **Speaker (unattributed):** because different personas care for different things,

[00:17:24–00:17:26] **Speaker (unattributed):** and maybe you have a way of thinking about that

[00:17:26–00:17:29] **Speaker (unattributed):** in terms of how that gets represented on the website.

[00:17:30–00:17:33] **Speaker (unattributed):** But are you thinking off like a,

[00:17:33–00:17:34] **Speaker (unattributed):** because what do you have in the mine map

[00:17:34–00:17:37] **Speaker (unattributed):** is all the different areas within governance

[00:17:37–00:17:39] **Speaker (unattributed):** and all the amazing features?

[00:17:39–00:17:40] **Speaker (unattributed):** There's of course the benefits,

[00:17:40–00:17:42] **Speaker (unattributed):** and as B and I went through it,

[00:17:42–00:17:45] **Speaker (unattributed):** some of the features are not what's showing in a meeting

[00:17:45–00:17:48] **Speaker (unattributed):** because that's the secret sauce behind the scenes example,

[00:17:48–00:17:51] **Speaker (unattributed):** that we may not want to share.

[00:17:51–00:17:56] **Speaker (unattributed):** Or, so are you thinking along the lines of solutions

[00:17:56–00:18:04] **Speaker (unattributed):** and packages and value prop is that what you're saying the same thing as what most companies

[00:18:04–00:18:11] **Speaker (unattributed):** websites have, which is products and products could be those big six or seven buckets you have.

[00:18:11–00:18:16] **Speaker (unattributed):** And then each product page could have some elements of the features with some screenshots

[00:18:16–00:18:22] **Speaker (unattributed):** as teasers and the intent would be for somebody to click and then fill a web form out so we

[00:18:22–00:18:25] **Speaker (unattributed):** can then start to work that as a lead.

[00:18:25–00:18:30] **Speaker (unattributed):** solutions would be more of the use cases and B has been extremely helpful in educating

[00:18:30–00:18:35] **Speaker (unattributed):** me on all the product capabilities and in those conversations we're beginning to get

[00:18:35–00:18:41] **Speaker (unattributed):** into packaging almost or use cases like this compliance use case and I'm new so all

[00:18:41–00:18:45] **Speaker (unattributed):** these might be second nature to you folks you probably talk about this almost every

[00:18:45–00:18:49] **Speaker (unattributed):** week this is compliance use case can we work with compliance services companies who

[00:18:49–00:18:56] **Speaker (unattributed):** put compliance packages or do end-to-end services in certain regulated industries to ensure

[00:18:56–00:18:58] **Speaker (unattributed):** They're compliant and they need tools.

[00:18:58–00:18:59] **Speaker (unattributed):** So we sell to those companies.

[00:18:59–00:19:03] **Speaker (unattributed):** As we were looking at those compliance use case was emerging

[00:19:03–00:19:06] **Speaker (unattributed):** as was an agent development lifecycle use case.

[00:19:06–00:19:10] **Speaker (unattributed):** You already have that here with your strategy for PLG.

[00:19:10–00:19:12] **Speaker (unattributed):** But the agent development lifecycle use case

[00:19:12–00:19:16] **Speaker (unattributed):** might be one to really tune in on and focus on even for

[00:19:16–00:19:18] **Speaker (unattributed):** an outbound GTM.

[00:19:18–00:19:20] **Speaker (unattributed):** I'm just sharing my thoughts out loud

[00:19:20–00:19:22] **Speaker (unattributed):** because engineering teams have a lot of budget.

[00:19:22–00:19:25] **Speaker (unattributed):** And this whole space is exploring

[00:19:25–00:19:28] **Speaker (unattributed):** And it got validated for me with a seam in your presentation

[00:19:28–00:19:31] **Speaker (unattributed):** at the San Francisco event with Octawe,

[00:19:31–00:19:33] **Speaker (unattributed):** both Manoj and Andrew used the word

[00:19:33–00:19:34] **Speaker (unattributed):** that we have budget for this.

[00:19:34–00:19:36] **Speaker (unattributed):** So let me just pause there.

[00:19:36–00:19:38] **Speaker (unattributed):** I know I set a lot, but first of all,

[00:19:38–00:19:44] **Speaker (unattributed):** I love this, the branding here and what you shared.

[00:19:44–00:19:46] **Speaker (unattributed):** I'm just trying to confirm how it will be organized around

[00:19:46–00:19:49] **Speaker (unattributed):** products and solutions and potentially industries

[00:19:49–00:19:51] **Speaker (unattributed):** in the future, we may be too early for that for now.

[00:19:51–00:19:54] **Speaker (unattributed):** And then some ideas and potentially

[00:19:54–00:19:56] **Speaker (unattributed):** where we could start to focus on

[00:19:56–00:19:59] **Speaker (unattributed):** if we need to right now, although I'm not sure.

[00:19:59–00:20:04] **Speaker (unattributed):** So, take it as you're 90% spot on what you've said.

[00:20:04–00:20:07] **Speaker (unattributed):** Because remember, what I'm doing is not rocket science

[00:20:07–00:20:11] **Speaker (unattributed):** and what I'm doing, I'm not about to patent as my idea.

[00:20:11–00:20:14] **Speaker (unattributed):** It's pretty much the way the industry it works.

[00:20:14–00:20:16] **Speaker (unattributed):** And I'll give you an example,

[00:20:16–00:20:18] **Speaker (unattributed):** when I was at Microsoft in the very early days

[00:20:18–00:20:22] **Speaker (unattributed):** and we created what Microsoft Excel is the first application.

[00:20:22–00:20:26] **Speaker (unattributed):** After we created Excel, we decided to create a word

[00:20:26–00:20:28] **Speaker (unattributed):** and word was there, and then PowerPoint.

[00:20:28–00:20:31] **Speaker (unattributed):** And then we created the idea of feature parity,

[00:20:31–00:20:32] **Speaker (unattributed):** the word feature parity, man.

[00:20:32–00:20:36] **Speaker (unattributed):** That all the applications should look and feel the same.

[00:20:36–00:20:38] **Speaker (unattributed):** The only thing that you need to do inside

[00:20:38–00:20:40] **Speaker (unattributed):** is the only thing that's different.

[00:20:40–00:20:43] **Speaker (unattributed):** So the learning curve for somebody to use office

[00:20:43–00:20:46] **Speaker (unattributed):** should be the minimum, right?

[00:20:46–00:20:47] **Speaker (unattributed):** To get up and running.

[00:20:47–00:20:50] **Speaker (unattributed):** So the whole premise behind this is that

[00:20:50–00:20:53] **Speaker (unattributed):** rather than try to be some creative studio

[00:20:53–00:20:55] **Speaker (unattributed):** and I'm trying to be the next best artist

[00:20:55–00:20:58] **Speaker (unattributed):** in terms of graphic design.

[00:20:58–00:21:01] **Speaker (unattributed):** We're just gonna go with what everybody in this tree knows

[00:21:01–00:21:04] **Speaker (unattributed):** and understands, which is they wanna get there

[00:21:04–00:21:06] **Speaker (unattributed):** and they wanna go, this is me,

[00:21:06–00:21:09] **Speaker (unattributed):** that's the product I want.

[00:21:09–00:21:13] **Speaker (unattributed):** And obviously, what can I do with it?

[00:21:13–00:21:14] **Speaker (unattributed):** What does it solve?

[00:21:14–00:21:15] **Speaker (unattributed):** What are my benefits?

[00:21:15–00:21:17] **Speaker (unattributed):** Blah blah blah, what's the value I get?

[00:21:17–00:21:22] **Speaker (unattributed):** bomb, get there very quickly. And the goal behind that is you're going to take them from the

[00:21:22–00:21:31] **Speaker (unattributed):** top of that funnel to the ability, in our case, to two paths. The only place and I'll come back to

[00:21:31–00:21:37] **Speaker (unattributed):** where I was continuing. So I talked about how we're going to open source massive parts of our

[00:21:37–00:21:44] **Speaker (unattributed):** of our platform and other parts we won't. And that's part of the way the industry is going. Everybody

[00:21:44–00:21:49] **Speaker (unattributed):** trust you if they can see what you build, right? And there are parts of our code which

[00:21:50–00:21:55] **Speaker (unattributed):** they're not even worth IP. They're not something like, oh my god, I need to be patenting it.

[00:21:55–00:22:01] **Speaker (unattributed):** But what they do is they build the trust from the community that they have access to be able

[00:22:01–00:22:06] **Speaker (unattributed):** to see your code and what you build. And they completely understand there's parts of it which

[00:22:06–00:22:11] **Speaker (unattributed):** you want to keep secret, the secret source. And that's fine and no problem. And you know,

[00:22:11–00:22:15] **Speaker (unattributed):** So B talked about how you have Microsoft governance framework,

[00:22:15–00:22:18] **Speaker (unattributed):** you have temporal where they've given a lot of their stuff

[00:22:18–00:22:21] **Speaker (unattributed):** in community open source, part of the Linux foundation.

[00:22:21–00:22:26] **Speaker (unattributed):** But then, you know, no credible enterprise is going to say,

[00:22:26–00:22:29] **Speaker (unattributed):** oh, you know what, I'll give the open source project

[00:22:29–00:22:33] **Speaker (unattributed):** to my development team who's working on my core competence

[00:22:33–00:22:35] **Speaker (unattributed):** for my business and say, now become experts

[00:22:35–00:22:37] **Speaker (unattributed):** in the Microsoft governance toolkit.

[00:22:38–00:23:08] **Speaker (unattributed):** They're not. They're going to go, let's use it to test our, what we're trying to achieve. But once we've done that, we're going to pay Microsoft and say, you're using the governance toolkit. We like it. We, it was open source. We trusted, but you're running it, but we can't keep supporting it for fixing bugs or managing it, whatever can we just pay you, right, which is where we want to end up. Okay. So with that said, I'm coming back to this. Okay. We now are at that position.

[00:23:08–00:23:16] **Speaker (unattributed):** where we need to start making revenue. Now, all goodwill, all hats off to you, Barat coming

[00:23:16–00:23:23] **Speaker (unattributed):** on board, whatever we do with Octo, whatever we do with Salesforce, whatever we do with anybody,

[00:23:23–00:23:28] **Speaker (unattributed):** we've done it with Camporral, with Mastero, with Copilot kit, with whatever. And again, nothing

[00:23:28–00:23:34] **Speaker (unattributed):** of that is transformed into anything because you know what, we haven't got a page which says

[00:23:34–00:23:42] **Speaker (unattributed):** OpenBox temporal, OpenBox master, OpenBox CopilotKit, right? All we have is a page when you go to

[00:23:42–00:23:52] **Speaker (unattributed):** our website is integrations and some things which mean absolutely a fall. Yeah. So it means nothing

[00:23:52–00:23:58] **Speaker (unattributed):** to anyone unless you know about temporal unless you know about CopilotKit and they're not pushing us.

[00:23:58–00:24:04] **Speaker (unattributed):** I don't see temporal cylinders. Yeah, we're on the website but how much traffic do we get? I don't

[00:24:04–00:24:09] **Speaker (unattributed):** I don't know Ashwin, do we have any analytics about how much traffic we get from time

[00:24:09–00:24:12] **Speaker (unattributed):** portal?

[00:24:12–00:24:18] **Speaker (unattributed):** No, we don't have specific analytics until they use a GTM link.

[00:24:18–00:24:19] **Speaker (unattributed):** Right.

[00:24:19–00:24:21] **Speaker (unattributed):** So again, we're doing very little.

[00:24:21–00:24:25] **Speaker (unattributed):** I mean, so we're so poor at doing this, but we've got to be better.

[00:24:25–00:24:31] **Speaker (unattributed):** Okay, so going through this, where we can make money is in this area.

[00:24:31–00:24:33] **Speaker (unattributed):** This is the only place we can make money.

[00:24:33–00:24:37] **Speaker (unattributed):** Now when I say we can only make money, what I've done is I've done my own work.

[00:24:37–00:24:41] **Speaker (unattributed):** regarding how do we give developers an experience,

[00:24:41–00:24:46] **Speaker (unattributed):** a really easy experience where they get on board for free.

[00:24:46–00:24:47] **Speaker (unattributed):** Now when they're on board for free,

[00:24:47–00:24:49] **Speaker (unattributed):** is it that they give,

[00:24:49–00:24:52] **Speaker (unattributed):** they get everything that we can do with this policy,

[00:24:52–00:24:55] **Speaker (unattributed):** which we call OpenBox gate for now for a month,

[00:24:55–00:25:00] **Speaker (unattributed):** and then they have to start paying $10, $15, $20,

[00:25:00–00:25:02] **Speaker (unattributed):** or something based on actions and usage

[00:25:02–00:25:10] **Speaker (unattributed):** because obviously until Tony finishes the billing side of things, we've never had the mechanism

[00:25:10–00:25:16] **Speaker (unattributed):** to build to take money. So it's not like we could have done it last month or the month before,

[00:25:16–00:25:21] **Speaker (unattributed):** we could have prioritized billing two months, three months ago, but we're now at a stage where

[00:25:21–00:25:28] **Speaker (unattributed):** billing has to work in the way that's needed. So some of the ideas behind this has been we have

[00:25:28–00:25:33] **Speaker (unattributed):** the free tier, we have the team tier and then we have the enterprise tier.

[00:25:33–00:25:41] **Speaker (unattributed):** And obviously, what we want to do is get developers from the free tier to a single license,

[00:25:41–00:25:46] **Speaker (unattributed):** to a team license, to an enterprise license. And I've been doing my work and I'll present that

[00:25:46–00:25:51] **Speaker (unattributed):** at a different time. We're all sending the documents out because I don't need to present all of that today.

[00:25:51–00:25:58] **Speaker (unattributed):** But the goal is to do that now. With that said, let's say we have all the pricing sorted out.

[00:25:58–00:26:03] **Speaker (unattributed):** Let's say we've all of this has been built out and all of this is built out and it's missing

[00:26:03–00:26:09] **Speaker (unattributed):** all the cool stuff that we offer people when we offer OpenBox gate which is provenance which is

[00:26:09–00:26:17] **Speaker (unattributed):** maybe to do with the fact that you know you can easily set up policies through natural language

[00:26:17–00:26:23] **Speaker (unattributed):** you can in fact you've got a security because we do a security review as part of this.

[00:26:23–00:26:29] **Speaker (unattributed):** All of those fantastic things will have to be documented, put together here, whether it's a video,

[00:26:29–00:26:36] **Speaker (unattributed):** whether it's like this broken down into some simple explainers, whatever it may be. But one thing

[00:26:36–00:26:45] **Speaker (unattributed):** that will need to happen in our company is we're going to need product owners, right? That means

[00:26:45–00:26:52] **Speaker (unattributed):** that person's job is to look after OpenBox gates on this page, everything that happens,

[00:26:52–00:26:58] **Speaker (unattributed):** everything to do with marketing it, to pushing it out, everything to getting feedback from a

[00:26:58–00:27:05] **Speaker (unattributed):** customer and getting it into the backlog of development or bugs that happen. Blah blah blah.

[00:27:05–00:27:11] **Speaker (unattributed):** And that's one of the things that we need to do because our platform is so massive. As

[00:27:11–00:27:17] **Speaker (unattributed):** soon cannot be the only product owner going out there and selling it. When we can easily

[00:27:17–00:27:25] **Speaker (unattributed):** take on Kita and say, on Kita, you are now the product owner of OpenBoxGate. Forgive

[00:27:25–00:27:31] **Speaker (unattributed):** my language, if the rest of the platform of what everything else you can do, go sell

[00:27:31–00:27:40] **Speaker (unattributed):** this. Right? And that way, we can focus the people in the company because if we're going

[00:27:40–00:27:47] **Speaker (unattributed):** to grow, you know, the GTM lead, if we're going to grow, you know yourself, you can't

[00:27:47–00:27:52] **Speaker (unattributed):** sell all of this in one big goal. Like they say, you can't eat an elephant in one bite.

[00:27:55–00:27:59] **Speaker (unattributed):** Okay. So particular piece is very focused on like this a lot.

[00:28:01–00:28:06] **Speaker (unattributed):** Well, we have to be, I mean, we just cannot. And that's, you know, as I said, I put on my CMO

[00:28:06–00:28:11] **Speaker (unattributed):** hat and I've done a couple of days of a very long night and mornings, I'll tell you,

[00:28:11–00:28:16] **Speaker (unattributed):** it's still speaking to me like four AM, my time and I'm deep into this and I'm not even

[00:28:16–00:28:19] **Speaker (unattributed):** and showing you a third of the stuff that I've done

[00:28:19–00:28:22] **Speaker (unattributed):** because I wanna present it properly,

[00:28:22–00:28:25] **Speaker (unattributed):** but today was the day where I wanted to get over

[00:28:25–00:28:29] **Speaker (unattributed):** and let everybody know that the way we're gonna go forward,

[00:28:29–00:28:33] **Speaker (unattributed):** and I use the way, it says, I mean, I'm looking for feedback

[00:28:33–00:28:36] **Speaker (unattributed):** and I'm looking for people to be devils advocate

[00:28:36–00:28:39] **Speaker (unattributed):** and I want people to tell me that I've got my head screwed

[00:28:39–00:28:41] **Speaker (unattributed):** on the wrong way and this is not the way to go.

[00:28:41–00:28:44] **Speaker (unattributed):** And I'm the first to be the one to say to you, okay,

[00:28:44–00:28:47] **Speaker (unattributed):** you tell me how we start generating revenue, right?

[00:28:47–00:28:49] **Speaker (unattributed):** If anyone has got a better idea

[00:28:49–00:28:52] **Speaker (unattributed):** than what I'm talking about right now, have added.

[00:28:52–00:28:58] **Speaker (unattributed):** I'll be to pass the button on and say you go do it, okay?

[00:28:58–00:29:00] **Speaker (unattributed):** But I'm presenting at least with my,

[00:29:00–00:29:02] **Speaker (unattributed):** you know, I've got three decades of experience

[00:29:02–00:29:03] **Speaker (unattributed):** even in marketing.

[00:29:03–00:29:06] **Speaker (unattributed):** So I've done my audit that I assume you I was doing that

[00:29:06–00:29:08] **Speaker (unattributed):** over the last couple of days,

[00:29:08–00:29:10] **Speaker (unattributed):** and I'm now starting to present

[00:29:10–00:29:12] **Speaker (unattributed):** what's coming out of the audit that I've done,

[00:29:12–00:29:14] **Speaker (unattributed):** the marketing audit, okay.

[00:29:14–00:29:18] **Speaker (unattributed):** So we need a product owner for each area, right?

[00:29:18–00:29:20] **Speaker (unattributed):** And in the case of, like I said,

[00:29:20–00:29:24] **Speaker (unattributed):** where I see Ankita in San Francisco performing well

[00:29:24–00:29:27] **Speaker (unattributed):** is we're not asking her to go and sell OpenBox.

[00:29:27–00:29:29] **Speaker (unattributed):** That is too big.

[00:29:29–00:29:31] **Speaker (unattributed):** She won't even know where to start.

[00:29:31–00:29:35] **Speaker (unattributed):** She just needs to be told by you Ankita,

[00:29:35–00:29:37] **Speaker (unattributed):** we're gonna have OpenBox gate.

[00:29:37–00:29:38] **Speaker (unattributed):** If that's what we end up calling her,

[00:29:38–00:29:41] **Speaker (unattributed):** OpenBox boundary was another name I had,

[00:29:41–00:29:43] **Speaker (unattributed):** but I didn't think that was so good.

[00:29:43–00:29:45] **Speaker (unattributed):** But we will get that done.

[00:29:45–00:29:51] **Speaker (unattributed):** My goal is to get this thing, which is the one that can generate as revenue plugged in and

[00:29:51–00:29:56] **Speaker (unattributed):** live by the end of next week with the billing platform. So this is the one where we can

[00:29:56–00:30:02] **Speaker (unattributed):** sell it because it's the one where we can quickly get people on board. Now, how do we get to those

[00:30:02–00:30:07] **Speaker (unattributed):** developers? How do we get them to try the free version? How do we get them to migrate from fee to

[00:30:07–00:30:15] **Speaker (unattributed):** paying to team to enterprise, that's part of what I'm busy putting together, which includes

[00:30:15–00:30:21] **Speaker (unattributed):** this strategy around an open source. So I've decided the rest of the product doesn't

[00:30:21–00:30:27] **Speaker (unattributed):** mean anything to me right now because I cannot sell to a single enterprise and get as

[00:30:27–00:30:36] **Speaker (unattributed):** money in November. That's my view, not a single one. But I know I can sell to developers

[00:30:36–00:30:41] **Speaker (unattributed):** and I can get some to start paying.

[00:30:41–00:30:41] **Speaker (unattributed):** Okay?

[00:30:41–00:30:46] **Speaker (unattributed):** Now any comments on that?

[00:30:46–00:30:47] **Speaker (unattributed):** No.

[00:30:47–00:30:49] **Speaker (unattributed):** I'm with you.

[00:30:49–00:30:49] **Speaker (unattributed):** Okay.

[00:30:49–00:30:52] **Speaker (unattributed):** I'm okay with the, obviously, the idea.

[00:30:52–00:30:55] **Speaker (unattributed):** And obviously, you know, I'm all up for productization.

[00:30:55–00:30:58] **Speaker (unattributed):** I think allocating separate product managers

[00:30:58–00:31:01] **Speaker (unattributed):** and making them, you could say almost like responsible

[00:31:01–00:31:03] **Speaker (unattributed):** for sales and sales strategy.

[00:31:03–00:31:04] **Speaker (unattributed):** I wouldn't go that far.

[00:31:04–00:31:08] **Speaker (unattributed):** And you have to just think about if we have enough people

[00:31:08–00:31:13] **Speaker (unattributed):** to do and even if even in the case of Ankitra to fit that kind of role.

[00:31:13–00:31:17] **Speaker (unattributed):** No, no, we don't have to discuss that separately.

[00:31:17–00:31:18] **Speaker (unattributed):** No, no, no, no.

[00:31:18–00:31:20] **Speaker (unattributed):** She doesn't have experience, but exactly.

[00:31:20–00:31:25] **Speaker (unattributed):** I'm just giving a high level view that if we were a bigger organization and a lot more

[00:31:25–00:31:28] **Speaker (unattributed):** money behind this, which in Shalab, we will do, right?

[00:31:28–00:31:33] **Speaker (unattributed):** We're going to have product owners that are internal slash outward facing to have drive

[00:31:33–00:31:34] **Speaker (unattributed):** the product roadmap.

[00:31:34–00:31:42] **Speaker (unattributed):** But obviously we're going to have people in GTM sales account executives, whatever you want to you and Barrett will be focusing on that.

[00:31:42–00:31:51] **Speaker (unattributed):** But what I'm saying to you guys is you and Barrett need to focus on making sure that those people where Barrett doesn't go alright we've got some money less.

[00:31:51–00:31:57] **Speaker (unattributed):** We managed to do another seed round or a series or whatever or an extension or a down-round gottuners whatever we got some more money.

[00:31:57–00:32:00] **Speaker (unattributed):** and then suddenly with that more money,

[00:32:00–00:32:02] **Speaker (unattributed):** you're able to hire two, three more people.

[00:32:02–00:32:04] **Speaker (unattributed):** It's useless trying to say to two, three more people.

[00:32:04–00:32:08] **Speaker (unattributed):** Let's hire someone who can sell everything.

[00:32:08–00:32:09] **Speaker (unattributed):** Yeah, no, no, I agree.

[00:32:09–00:32:14] **Speaker (unattributed):** I just thought we were talking like literally like a plan.

[00:32:14–00:32:16] **Speaker (unattributed):** So that's fine.

[00:32:16–00:32:18] **Speaker (unattributed):** It's certainly concerned when you mentioned,

[00:32:18–00:32:21] **Speaker (unattributed):** if it was this hypothetical and the way growth works,

[00:32:21–00:32:22] **Speaker (unattributed):** I get that.

[00:32:22–00:32:26] **Speaker (unattributed):** Yeah, in that growth phase, that's eestructuring.

[00:32:26–00:32:27] **Speaker (unattributed):** Right.

[00:32:27–00:32:34] **Speaker (unattributed):** That's one of these objectives I have asked him for you and Barrett to do is from this

[00:32:34–00:32:37] **Speaker (unattributed):** as a takeaway is to go and think about that area.

[00:32:37–00:32:44] **Speaker (unattributed):** Yes, so this is one thing I've been thinking about where, and I'm new to this space, so

[00:32:44–00:32:48] **Speaker (unattributed):** if some of this is too basic, let me know, this is one thing I wanted to run by you folks,

[00:32:48–00:32:50] **Speaker (unattributed):** and I may have texted you yesterday.

[00:32:50–00:32:54] **Speaker (unattributed):** I've been reading about agent development lifecycle and maybe I should have read about that

[00:32:54–00:32:55] **Speaker (unattributed):** nine months back.

[00:32:55–00:33:00] **Speaker (unattributed):** this whole agent development life cycle is very particular.

[00:33:00–00:33:02] **Speaker (unattributed):** And that's what this also ties into.

[00:33:02–00:33:05] **Speaker (unattributed):** You're taking a PLG approach, bottoms up approach.

[00:33:05–00:33:09] **Speaker (unattributed):** I'm sort of based on my very limited experience here

[00:33:09–00:33:12] **Speaker (unattributed):** and knowledge base in this area.

[00:33:12–00:33:14] **Speaker (unattributed):** I'm kind of getting to the point where

[00:33:14–00:33:18] **Speaker (unattributed):** this same idea in terms of the outbound

[00:33:18–00:33:21] **Speaker (unattributed):** to go to the VP of engineering or

[00:33:21–00:33:23] **Speaker (unattributed):** whoever to say, look, I mean,

[00:33:23–00:33:25] **Speaker (unattributed):** you're going to be pinged by your security

[00:33:25–00:33:26] **Speaker (unattributed):** and governance team at some point of time.

[00:33:26–00:33:28] **Speaker (unattributed):** with everybody struggling with this in my book.

[00:33:28–00:33:31] **Speaker (unattributed):** Like, you folks were on the stage and both Manojo

[00:33:31–00:33:32] **Speaker (unattributed):** and we should talk about that separately,

[00:33:32–00:33:34] **Speaker (unattributed):** a seam around Manojo and Andrew.

[00:33:34–00:33:36] **Speaker (unattributed):** They both said, yeah, there's budget for this.

[00:33:36–00:33:37] **Speaker (unattributed):** Can you show it to us?

[00:33:37–00:33:39] **Speaker (unattributed):** To me, that seems to be,

[00:33:39–00:33:42] **Speaker (unattributed):** and it's so then it gives us focus to here.

[00:33:42–00:33:45] **Speaker (unattributed):** So you write like short term enterprise revenue

[00:33:45–00:33:47] **Speaker (unattributed):** versus as we start to build towards this.

[00:33:47–00:33:50] **Speaker (unattributed):** And we have a lot of experience with massive accounts

[00:33:50–00:33:52] **Speaker (unattributed):** that are seen as continuing to penetrate.

[00:33:52–00:33:54] **Speaker (unattributed):** And we can discuss that separately.

[00:33:54–00:33:58] **Speaker (unattributed):** but in terms of a focused use case,

[00:33:58–00:34:01] **Speaker (unattributed):** this could potentially be that use case

[00:34:01–00:34:03] **Speaker (unattributed):** around agent development lifecycle.

[00:34:03–00:34:05] **Speaker (unattributed):** And if I'm speaking our line, let me know

[00:34:05–00:34:07] **Speaker (unattributed):** because I could be totally wrong.

[00:34:07–00:34:08] **Speaker (unattributed):** I'm very new here.

[00:34:08–00:34:11] **Speaker (unattributed):** But this agent development lifecycle use case end to end,

[00:34:11–00:34:13] **Speaker (unattributed):** which is emerging with the entire industry.

[00:34:13–00:34:16] **Speaker (unattributed):** Like look at Anthropic, it's everything's blown up around that

[00:34:16–00:34:19] **Speaker (unattributed):** and you're tying this, that exact same thing.

[00:34:19–00:34:23] **Speaker (unattributed):** I would love to think through that agent development use case,

[00:34:23–00:34:30] **Speaker (unattributed):** life cycle use case very deeply with this team with everyone here structure the enterprise go to

[00:34:30–00:34:35] **Speaker (unattributed):** market around that in a focused fashion and I see this is something you and I need to bring

[00:34:35–00:34:40] **Speaker (unattributed):** storm separately but that this could also then support that because then we're taking the both

[00:34:40–00:34:45] **Speaker (unattributed):** the LG approach and enterprise approach around a specific use case and target person on an audience.

[00:34:45–00:34:50] **Speaker (unattributed):** We're not going to say no to the governance teams and CSOs right. All these things will line up

[00:34:50–00:34:54] **Speaker (unattributed):** Anyways, but we could start to use some of your thinking and

[00:34:54–00:34:57] **Speaker (unattributed):** part leadership here to hear around the work here and reuse

[00:34:57–00:35:02] **Speaker (unattributed):** those assets around you and enterprise GTM and penetration.

[00:35:02–00:35:03] **Speaker (unattributed):** We start to build with this use case as well.

[00:35:05–00:35:10] **Speaker (unattributed):** Well, the lovely part is I'm not here to do all the work for

[00:35:10–00:35:15] **Speaker (unattributed):** everybody. I'm here to sort of provide that high level thinking

[00:35:15–00:35:18] **Speaker (unattributed):** and strategy and sort of say, you know, we need to turn this into

[00:35:18–00:35:22] **Speaker (unattributed):** something that starts generating revenue this quarter.

[00:35:22–00:35:23] **Speaker (unattributed):** Right?

[00:35:23–00:35:25] **Speaker (unattributed):** When I say this quarter, okay, I mean,

[00:35:25–00:35:27] **Speaker (unattributed):** I've only got a chance to get on top of this

[00:35:27–00:35:30] **Speaker (unattributed):** since this last week when we came back from San Francisco.

[00:35:30–00:35:34] **Speaker (unattributed):** So my quarter is going into January or end of January,

[00:35:34–00:35:36] **Speaker (unattributed):** but my goal is I promised I'll send,

[00:35:36–00:35:41] **Speaker (unattributed):** I'll get in something that shows a million ARR in this quarter.

[00:35:41–00:35:42] **Speaker (unattributed):** Okay?

[00:35:42–00:35:44] **Speaker (unattributed):** So I'm working on where can I get that?

[00:35:44–00:35:47] **Speaker (unattributed):** And obviously clear messaging,

[00:35:47–00:35:51] **Speaker (unattributed):** like communications, productizing, people focus,

[00:35:51–00:35:54] **Speaker (unattributed):** making sure we have got things that will resonate

[00:35:54–00:35:58] **Speaker (unattributed):** with all the different ICPs, target audience

[00:35:58–00:35:59] **Speaker (unattributed):** for each product.

[00:35:59–00:36:03] **Speaker (unattributed):** It's for me, it's a lot easier to go, you know what?

[00:36:03–00:36:06] **Speaker (unattributed):** Ashwin and B, you are developers.

[00:36:06–00:36:09] **Speaker (unattributed):** So one question I'm going to ask now of Ashwin and B,

[00:36:09–00:36:11] **Speaker (unattributed):** and this is where I need your help.

[00:36:11–00:36:15] **Speaker (unattributed):** Okay, we know we built codex and codex

[00:36:15–00:36:19] **Speaker (unattributed):** and Claude and Muse Code integration.

[00:36:19–00:36:22] **Speaker (unattributed):** And you guys know better than anybody,

[00:36:22–00:36:24] **Speaker (unattributed):** what is on the backend, right?

[00:36:24–00:36:27] **Speaker (unattributed):** The integration part of how you integrate,

[00:36:27–00:36:29] **Speaker (unattributed):** and I've got some notes on stuff

[00:36:29–00:36:31] **Speaker (unattributed):** that I want you guys to consider.

[00:36:31–00:36:33] **Speaker (unattributed):** But based on everything that you know be

[00:36:33–00:36:36] **Speaker (unattributed):** that we built on the backend, right?

[00:36:37–00:36:43] **Speaker (unattributed):** What should we be selling here?

[00:36:43–00:36:46] **Speaker (unattributed):** You mean for the script length?

[00:36:46–00:36:49] **Speaker (unattributed):** Yeah.

[00:36:49–00:37:04] **Speaker (unattributed):** I thought it's a big like a hard pick for me here.

[00:37:04–00:37:17] **Speaker (unattributed):** But like for example I met with a general manager of a pretty big outsourcing company,

[00:37:17–00:37:20] **Speaker (unattributed):** like a dev house company in Vietnam.

[00:37:20–00:37:25] **Speaker (unattributed):** and he was saying that eventually he needed something

[00:37:26–00:37:31] **Speaker (unattributed):** to managing his developers

[00:37:31–00:37:37] **Speaker (unattributed):** and also able to control,

[00:37:38–00:37:44] **Speaker (unattributed):** like helping them to give them the tools

[00:37:44–00:37:49] **Speaker (unattributed):** so that the products that they make

[00:37:49–00:37:54] **Speaker (unattributed):** Mike for their customer is more secure, is better,

[00:37:56–00:38:01] **Speaker (unattributed):** like in terms of securing security and policy

[00:38:02–00:38:05] **Speaker (unattributed):** and compliance, et cetera.

[00:38:05–00:38:08] **Speaker (unattributed):** Because like, for example, if you know,

[00:38:08–00:38:10] **Speaker (unattributed):** like developer in those deaf house,

[00:38:10–00:38:14] **Speaker (unattributed):** usually working on like a particular project at the same time.

[00:38:14–00:38:16] **Speaker (unattributed):** And one of the,

[00:38:20–00:38:29] **Speaker (unattributed):** the crazy thing is like like he he afraid that like for example like using like like like

[00:38:29–00:38:37] **Speaker (unattributed):** leaking data or ncp or tools that from from one customer to another one and then so so things

[00:38:37–00:38:44] **Speaker (unattributed):** like that is it's one of the concerning things that that he is looking for a solution.

[00:38:45–00:38:50] **Speaker (unattributed):** Right so do we have a solution that he can use tomorrow?

[00:38:52–00:39:09] **Speaker (unattributed):** We have the technology, but like, we have the technology and capability, but in order to give a direct solution, we need a bit more work on.

[00:39:09–00:39:10] **Speaker (unattributed):** Yeah.

[00:39:10–00:39:12] **Speaker (unattributed):** We need to figure that out.

[00:39:12–00:39:20] **Speaker (unattributed):** The solution can be figured out in the room with this to me confirms, and sorry to interject, I'm going to shut up, but this to me confirms what I just said.

[00:39:20–00:39:22] **Speaker (unattributed):** and it's beautiful what he said.

[00:39:22–00:39:24] **Speaker (unattributed):** We have the technology.

[00:39:24–00:39:25] **Speaker (unattributed):** Based on what you've shown to me,

[00:39:25–00:39:27] **Speaker (unattributed):** we absolutely have it.

[00:39:27–00:39:29] **Speaker (unattributed):** It's a matter of plugging it in

[00:39:29–00:39:32] **Speaker (unattributed):** their environment giving that person for free,

[00:39:32–00:39:35] **Speaker (unattributed):** saying all the developers could use this for free for 30 days

[00:39:35–00:39:37] **Speaker (unattributed):** or whatever we define the package to be.

[00:39:37–00:39:40] **Speaker (unattributed):** Let's get them on and then the Ashwin and team or whoever,

[00:39:40–00:39:45] **Speaker (unattributed):** or we get in there and deploy that for all the developers,

[00:39:45–00:39:47] **Speaker (unattributed):** with a committed contract or

[00:39:47–00:39:51] **Speaker (unattributed):** some level of commitment saying based on your budget and appetite,

[00:39:51–00:39:53] **Speaker (unattributed):** If you can give this piece of mind to you,

[00:39:53–00:39:56] **Speaker (unattributed):** here are all the reasons why he is the value prop.

[00:39:56–00:39:59] **Speaker (unattributed):** And in 30 or 45 days, you will commit to this contract

[00:39:59–00:40:05] **Speaker (unattributed):** and the pricing would be specific to the region.

[00:40:05–00:40:07] **Speaker (unattributed):** Yeah, no, no, absolutely.

[00:40:07–00:40:09] **Speaker (unattributed):** That's the remedy.

[00:40:09–00:40:12] **Speaker (unattributed):** Yeah, well, as I said, the reason I'm asking the question

[00:40:12–00:40:16] **Speaker (unattributed):** is that he's talking to somebody who genuinely is going,

[00:40:16–00:40:18] **Speaker (unattributed):** look, I have a problem.

[00:40:18–00:40:19] **Speaker (unattributed):** How do I solve it?

[00:40:19–00:40:23] **Speaker (unattributed):** So give an example, let me now do a slide

[00:40:23–00:40:24] **Speaker (unattributed):** of their introduction.

[00:40:24–00:40:32] **Speaker (unattributed):** Okay, so to give you an example right here is packaging pricing for the OpenBox gates.

[00:40:32–00:40:34] **Speaker (unattributed):** I'm not going to call it shift left anymore.

[00:40:34–00:40:42] **Speaker (unattributed):** So the pricing is free individual zero team $15 a seat per month, placeholder market band

[00:40:42–00:40:47] **Speaker (unattributed):** can be based on others that are seen and to price custom maps to observe government

[00:40:47–00:40:54] **Speaker (unattributed):** move additions and the on-prem price list enforcement full fail closed local.

[00:40:54–00:40:56] **Speaker (unattributed):** And that's something we have to make sure we can do.

[00:40:56–00:40:59] **Speaker (unattributed):** Full, full managed settings pending,

[00:40:59–00:41:01] **Speaker (unattributed):** default policy pack, yes,

[00:41:01–00:41:05] **Speaker (unattributed):** and yes plus all policy overlay, yes plus custom packs,

[00:41:05–00:41:08] **Speaker (unattributed):** policy as code, yes, yes with all-global precedents,

[00:41:08–00:41:11] **Speaker (unattributed):** yes with sign policy lineage,

[00:41:11–00:41:14] **Speaker (unattributed):** proof certificate limited per month to 50,

[00:41:14–00:41:15] **Speaker (unattributed):** unlimited, unlimited,

[00:41:15–00:41:18] **Speaker (unattributed):** local ankle, proof retention,

[00:41:18–00:41:21] **Speaker (unattributed):** 30 days one year configurable on-prem,

[00:41:21–00:41:23] **Speaker (unattributed):** approval route in local prompt only,

[00:41:23–00:41:26] **Speaker (unattributed):** Slack, GitHub, Review, blah, blah, blah.

[00:41:26–00:41:28] **Speaker (unattributed):** Some of these may or may not make sense,

[00:41:28–00:41:32] **Speaker (unattributed):** but I'll go through that with B and Ashwin

[00:41:32–00:41:34] **Speaker (unattributed):** are more of a technical.

[00:41:34–00:41:38] **Speaker (unattributed):** But the idea being is that here,

[00:41:38–00:41:40] **Speaker (unattributed):** the Open Gate will go to Market Plan.

[00:41:40–00:41:42] **Speaker (unattributed):** Developers do not buy governance.

[00:41:42–00:41:45] **Speaker (unattributed):** They buy things that let them run their coding agents

[00:41:45–00:41:49] **Speaker (unattributed):** with less supervision and less fear.

[00:41:49–00:41:50] **Speaker (unattributed):** The product that they're developing stalls

[00:41:50–00:41:52] **Speaker (unattributed):** is a gate plus a receipt,

[00:41:52–00:41:59] **Speaker (unattributed):** Fail-close policy gate is the agent's tool loop and a signed proof certificate of what

[00:41:59–00:42:04] **Speaker (unattributed):** the agent was authorized to do what it actually did. Governance is what the team buys.

[00:42:04–00:42:10] **Speaker (unattributed):** Once several developers already have the gate installed, policy, shared policy, as code,

[00:42:10–00:42:15] **Speaker (unattributed):** central proof storage, retention, approval routing, SSO and fleetwide policy pinning.

[00:42:16–00:42:21] **Speaker (unattributed):** That maps directly onto the existing OpenBox editions, observe, govern, prove,

[00:42:21–00:42:27] **Speaker (unattributed):** and developer seats metric already in the master service agreement one point which are you know

[00:42:27–00:42:32] **Speaker (unattributed):** we put out there to review so the self-service seat is the top of the funnel for the enterprise

[00:42:32–00:42:38] **Speaker (unattributed):** business rather than a separate business so what this basically says is literally that which is

[00:42:39–00:42:45] **Speaker (unattributed):** how do we get people to play with OpenBox you know getting them to

[00:42:45–00:42:54] **Speaker (unattributed):** to use OpenBox core or use OpenBox for a behemoth engine is impossible, right?

[00:42:54–00:42:58] **Speaker (unattributed):** Because nobody, and you know, I said, well, I will attest to this.

[00:42:58–00:43:02] **Speaker (unattributed):** There isn't a single company since the six months we've started,

[00:43:02–00:43:07] **Speaker (unattributed):** who apart from having demos, loving what we see,

[00:43:07–00:43:11] **Speaker (unattributed):** talking about how we all the features look amazing, amazing, amazing.

[00:43:11–00:43:17] **Speaker (unattributed):** I think the only company I came across that even how to go was

[00:43:17–00:43:22] **Speaker (unattributed):** Squigy and then the people from next discovery those are the only two

[00:43:22–00:43:27] **Speaker (unattributed):** people who if I'm right Ashwin correct me who've had a go at getting our

[00:43:27–00:43:33] **Speaker (unattributed):** system up and running. Yes they are the only two. Right and can you describe to me

[00:43:33–00:43:44] **Speaker (unattributed):** what their experience is be? I mean for them it's like so for Squigy it was

[00:43:44–00:43:53] **Speaker (unattributed):** It was a bit easy for them because they switched to their custom framework and we built

[00:43:53–00:44:00] **Speaker (unattributed):** I mean nothing in a week of time we just built the entire SDK for them for the new framework.

[00:44:00–00:44:07] **Speaker (unattributed):** Currently what they are doing is just working on their systems to make sure everything is

[00:44:07–00:44:14] **Speaker (unattributed):** all right and OpenBox is in their product with the launch for them it's fine. For next

[00:44:14–00:44:21] **Speaker (unattributed):** discovery I think apparently what they're doing is they are also working on the SDK they also have

[00:44:21–00:44:28] **Speaker (unattributed):** a question for you know but they are still working on the SDK from their side it's not on

[00:44:28–00:44:36] **Speaker (unattributed):** outside so I have limited information on that. Okay but what I'm saying is at least

[00:44:36–00:44:43] **Speaker (unattributed):** set and those guys saw value in using OpenBox. Yeah. Yeah. Yeah. They saw that. Yeah. And

[00:44:43–00:44:52] **Speaker (unattributed):** next discovery, where are we with them? For that, I think last week they had some query and

[00:44:52–00:44:58] **Speaker (unattributed):** we texted them like we could just jump on a call and sort it out. We are just waiting for the

[00:44:58–00:45:05] **Speaker (unattributed):** reply. The Omar is it? The guy? Yeah. We're just waiting for Omar because Jeremy reached out to

[00:45:05–00:45:09] **Speaker (unattributed):** to me about, again, just catching up because the whole idea

[00:45:09–00:45:12] **Speaker (unattributed):** was that last week they were going to try to get it over the line

[00:45:12–00:45:16] **Speaker (unattributed):** with some of that what's called Cloud Fire stuff

[00:45:16–00:45:17] **Speaker (unattributed):** that they needed.

[00:45:17–00:45:27] **Speaker (unattributed):** So I thought I would open the relevant ports or whatever. Obviously I thought I was done by last Friday, but the real goal is to try to get them over the line this week. [ASR uncertain]

[00:45:48–00:45:50] **Speaker (unattributed):** we have big logos.

[00:45:50–00:45:51] **Speaker (unattributed):** Those are the only two customers.

[00:45:51–00:45:54] **Speaker (unattributed):** And you know what, the difference it will make to the website

[00:45:54–00:45:57] **Speaker (unattributed):** from just putting logos to do with temporal or master

[00:45:57–00:45:59] **Speaker (unattributed):** or whatever is one thing.

[00:45:59–00:46:01] **Speaker (unattributed):** Another one is actually be able to say

[00:46:01–00:46:04] **Speaker (unattributed):** we have live use cases.

[00:46:04–00:46:06] **Speaker (unattributed):** And those two companies would be over the moon

[00:46:06–00:46:08] **Speaker (unattributed):** to have their logos on our website

[00:46:08–00:46:12] **Speaker (unattributed):** and pointers to their website, saying these guys offer

[00:46:12–00:46:19] **Speaker (unattributed):** whatever it is they offer and they use OpenBox.

[00:46:19–00:46:24] **Speaker (unattributed):** So the thing I was going to ask was between UNB Ashwin is,

[00:46:24–00:46:26] **Speaker (unattributed):** I really, really, I need you guys to get

[00:46:26–00:46:31] **Speaker (unattributed):** these two companies over the line.

[00:46:31–00:46:33] **Speaker (unattributed):** Yeah, it makes sense.

[00:46:33–00:46:35] **Speaker (unattributed):** Also, if you're happy that that would gel me.

[00:46:35–00:46:39] **Speaker (unattributed):** And if Omar is ready to handle the SDK to us,

[00:46:39–00:46:41] **Speaker (unattributed):** we can pretty build that for Omar,

[00:46:41–00:46:43] **Speaker (unattributed):** that then him building in house,

[00:46:43–00:46:45] **Speaker (unattributed):** because we know the box better.

[00:46:45–00:46:49] **Speaker (unattributed):** OK, well, I would ask you, Ashwin, then please try to do that.

[00:46:49–00:46:51] **Speaker (unattributed):** I know we talked about all the other things

[00:46:51–00:46:53] **Speaker (unattributed):** you are going to take on to do between now

[00:46:53–00:46:55] **Speaker (unattributed):** and maybe Eros coming on board or not.

[00:46:55–00:46:57] **Speaker (unattributed):** But it really is important.

[00:46:57–00:46:59] **Speaker (unattributed):** And the reason I'm saying that is,

[00:46:59–00:47:00] **Speaker (unattributed):** and Barat will tell you as well,

[00:47:00–00:47:03] **Speaker (unattributed):** we can have our website talking about our money

[00:47:03–00:47:06] **Speaker (unattributed):** we raised about all these integrations we've done.

[00:47:06–00:47:10] **Speaker (unattributed):** But if we can't name a single credible use case,

[00:47:10–00:47:12] **Speaker (unattributed):** and for me, the way I've been working it

[00:47:12–00:47:15] **Speaker (unattributed):** is the proof of concept we did for every

[00:47:15–00:47:18] **Speaker (unattributed):** will be one use case I'll be documenting.

[00:47:18–00:47:26] **Speaker (unattributed):** the what should be considered as live projects with squidgy and next discovery will be the

[00:47:26–00:47:31] **Speaker (unattributed):** other two use cases. So I've got three and I'm trying to think of any others that we are

[00:47:31–00:47:38] **Speaker (unattributed):** working on that would be at least worth mentioning as use cases of, you know, that we have

[00:47:38–00:47:43] **Speaker (unattributed):** been involved in. We don't have to say whether they're proof of concept or they're live.

[00:47:43–00:47:47] **Speaker (unattributed):** We just have to go, these are the kind of projects we're working on. That's about as close

[00:47:47–00:47:52] **Speaker (unattributed):** to social proof as I'm going to be able to get the website. So somebody comes and says

[00:47:52–00:47:54] **Speaker (unattributed):** somebody actually is using their product.

[00:47:57–00:48:01] **Speaker (unattributed):** Eros is so specialized as well. Is that what mentioning to hear?

[00:48:01–00:48:09] **Speaker (unattributed):** My goal behind Eros is that once that's a goal, meaning it's not far down the road in the

[00:48:09–00:48:16] **Speaker (unattributed):** sense that once they go ahead and we can get it over the line, I believe when we say it's so

[00:48:16–00:48:22] **Speaker (unattributed):** specialized. The way I've been putting it together is talking about how we can do water marking

[00:48:22–00:48:30] **Speaker (unattributed):** and fingerprinting sits very much as I've seen it once, it's still governance, it's IP governance,

[00:48:30–00:48:37] **Speaker (unattributed):** right? And the fact that it's something we can describe in what we do, but sort of it's the way

[00:48:37–00:48:44] **Speaker (unattributed):** we word it which is, is it so much of an outlier that it was done like a customized project,

[00:48:44–00:48:48] **Speaker (unattributed):** or is it something we can offer as a standard feature?

[00:48:48–00:48:51] **Speaker (unattributed):** And my goal is to actually make it OpenBox,

[00:48:51–00:48:56] **Speaker (unattributed):** I don't know, water marks, slash fingerprinting as a product.

[00:48:56–00:48:57] **Speaker (unattributed):** Yes, that's right.

[00:48:57–00:48:59] **Speaker (unattributed):** We're on this exact same page, perfect.

[00:48:59–00:49:00] **Speaker (unattributed):** Yeah, that's right, man.

[00:49:00–00:49:03] **Speaker (unattributed):** Yeah, so and there we have a chance to demonstrate,

[00:49:03–00:49:06] **Speaker (unattributed):** and the idea is, and this is where Asim will come in,

[00:49:06–00:49:09] **Speaker (unattributed):** that once it's a go and we deliberate,

[00:49:09–00:49:12] **Speaker (unattributed):** I'm hoping by December when it's ready to go live

[00:49:12–00:49:17] **Speaker (unattributed):** and they're using it will be able to do a big press release with them and talk about how

[00:49:17–00:49:23] **Speaker (unattributed):** OpenBox is, I worked with the biggest digital agency with the 1.2 billion whatever their

[00:49:23–00:49:29] **Speaker (unattributed):** assets blah blah blah blah blah. You can't get any more proof than that, right? The fact

[00:49:29–00:49:35] **Speaker (unattributed):** that it will be a paid project, right, is amazing because there'll be a solid number behind

[00:49:35–00:49:43] **Speaker (unattributed):** it, okay? So yeah, so that's the way we're going, okay, so I know bees have to drop off but

[00:49:43–00:49:46] **Speaker (unattributed):** That's okay, I'm gonna sort of pretty much wrap up.

[00:49:46–00:49:48] **Speaker (unattributed):** So in essence, as I said,

[00:49:48–00:49:50] **Speaker (unattributed):** I'm working on the next couple of days

[00:49:50–00:49:54] **Speaker (unattributed):** to learn in next week to try to bring it all together

[00:49:54–00:49:57] **Speaker (unattributed):** in a way that I'll be able to start demonstrating

[00:49:57–00:49:59] **Speaker (unattributed):** what the homepage looks like.

[00:49:59–00:50:02] **Speaker (unattributed):** All these sub pages, and this is about you

[00:50:02–00:50:04] **Speaker (unattributed):** and I'll start getting you guys.

[00:50:04–00:50:06] **Speaker (unattributed):** And I guess I'm from your perspective

[00:50:06–00:50:08] **Speaker (unattributed):** to start getting you to think,

[00:50:08–00:50:09] **Speaker (unattributed):** and I'll group it for you,

[00:50:09–00:50:11] **Speaker (unattributed):** what these sub brands are about,

[00:50:11–00:50:13] **Speaker (unattributed):** without a new come up with the names

[00:50:13–00:50:16] **Speaker (unattributed):** if you wanna be the one who'll work with Barra,

[00:50:16–00:50:17] **Speaker (unattributed):** you know, whichever I mean,

[00:50:17–00:50:20] **Speaker (unattributed):** I'm happy to take on board whatever you come up with

[00:50:20–00:50:22] **Speaker (unattributed):** to me, they're just a way to refer to

[00:50:22–00:50:24] **Speaker (unattributed):** and that functionality and capability

[00:50:24–00:50:27] **Speaker (unattributed):** and the benefits that brings to the people.

[00:50:27–00:50:30] **Speaker (unattributed):** Now, the last thing I wanted to talk about is

[00:50:30–00:50:32] **Speaker (unattributed):** this is all great and imagine a week and a half

[00:50:32–00:50:35] **Speaker (unattributed):** from now all of us done, the new website is done,

[00:50:35–00:50:38] **Speaker (unattributed):** the new strategy, the tactical plans,

[00:50:38–00:50:40] **Speaker (unattributed):** you know, the point will be is,

[00:50:40–00:50:44] **Speaker (unattributed):** Okay, great, Dr. presentation announcement,

[00:50:44–00:50:46] **Speaker (unattributed):** Salesforce President announcement,

[00:50:46–00:50:48] **Speaker (unattributed):** we already have 10 polls and all that,

[00:50:48–00:50:51] **Speaker (unattributed):** but we're not making any traction and inroads enough

[00:50:51–00:50:54] **Speaker (unattributed):** to at least be making money.

[00:50:54–00:50:55] **Speaker (unattributed):** And as I've said, I come back to this,

[00:50:55–00:50:58] **Speaker (unattributed):** this idea of an OpenBox gate,

[00:50:58–00:51:00] **Speaker (unattributed):** as I said, I don't call it shift left anymore,

[00:51:00–00:51:03] **Speaker (unattributed):** is where I'm gonna focus my effort

[00:51:03–00:51:05] **Speaker (unattributed):** throughout the whole of November and December

[00:51:05–00:51:09] **Speaker (unattributed):** to get those developers to go through that journey

[00:51:09–00:51:13] **Speaker (unattributed):** of free tier to team to enterprise

[00:51:13–00:51:17] **Speaker (unattributed):** and look at using that as the entry wedge into enterprises.

[00:51:17–00:51:21] **Speaker (unattributed):** So by the time those developers have installed

[00:51:21–00:51:23] **Speaker (unattributed):** and started to use our product

[00:51:23–00:51:25] **Speaker (unattributed):** and gain confidence in using it

[00:51:25–00:51:29] **Speaker (unattributed):** that it would propagate itself up to the enterprise.

[00:51:29–00:51:32] **Speaker (unattributed):** So we start to develop.

[00:51:32–00:51:34] **Speaker (unattributed):** Okay, now my goal is, and this is where

[00:51:34–00:51:38] **Speaker (unattributed):** a giving example of how I'm thinking of approaching it.

[00:51:38–00:51:49] **Speaker (unattributed):** Right. So my goal is I'm looking to target one developer per company that I believe is either

[00:51:49–00:51:55] **Speaker (unattributed):** very targeted or right. So let's just take it this way. Someone who's a single developer

[00:51:55–00:52:00] **Speaker (unattributed):** alone wolf is not really going to buy into this, not to be right now. Okay. And maybe

[00:52:00–00:52:04] **Speaker (unattributed):** wrong. But for now, I don't think they're going to buy into it. But then they're not going

[00:52:04–00:52:09] **Speaker (unattributed):** to give us the money we need either. Even if I even if I got a one of these people to say

[00:52:09–00:52:11] **Speaker (unattributed):** get on and try with the free.

[00:52:11–00:52:13] **Speaker (unattributed):** They'll be like, maybe I'm just okay with the free.

[00:52:13–00:52:15] **Speaker (unattributed):** I don't need to move to team.

[00:52:15–00:52:19] **Speaker (unattributed):** Where we're going to make money are the developers we target.

[00:52:19–00:52:21] **Speaker (unattributed):** He'll move to team, right?

[00:52:21–00:52:24] **Speaker (unattributed):** Me wanting to pay, even if it's team for themselves,

[00:52:24–00:52:27] **Speaker (unattributed):** with some of the extra features that'll be made visible

[00:52:27–00:52:30] **Speaker (unattributed):** to them, where maybe they might get them free of charge

[00:52:30–00:52:32] **Speaker (unattributed):** for 30 days, and then after 30 days,

[00:52:32–00:52:35] **Speaker (unattributed):** those features disappear, but we've hoped them,

[00:52:35–00:52:37] **Speaker (unattributed):** and they're ready to pay for those features.

[00:52:37–00:52:41] **Speaker (unattributed):** Eventually, they're doing so great where they say to their mates,

[00:52:41–00:52:43] **Speaker (unattributed):** hey, you know what, you should use this as well.

[00:52:43–00:52:44] **Speaker (unattributed):** You should use this as well.

[00:52:44–00:52:46] **Speaker (unattributed):** And then we get a team license.

[00:52:46–00:52:49] **Speaker (unattributed):** And then the enterprise goes, you know what,

[00:52:49–00:52:50] **Speaker (unattributed):** this has been so cool for us.

[00:52:50–00:52:52] **Speaker (unattributed):** We should buy an enterprise license,

[00:52:52–00:52:56] **Speaker (unattributed):** why we're paying 15 quid and pop when we just buy an enterprise license,

[00:52:56–00:52:58] **Speaker (unattributed):** which is the same as everybody else does.

[00:52:58–00:53:02] **Speaker (unattributed):** And we're in that there is no better way than that because we're in

[00:53:02–00:53:06] **Speaker (unattributed):** because the only difference between that

[00:53:06–00:53:11] **Speaker (unattributed):** and our enterprise product is going from coding agent

[00:53:11–00:53:17] **Speaker (unattributed):** governance or security to runtime governance and security.

[00:53:17–00:53:19] **Speaker (unattributed):** And I'll add to this.

[00:53:19–00:53:22] **Speaker (unattributed):** I'm now starting to use the word security more.

[00:53:22–00:53:26] **Speaker (unattributed):** And Asim knows he and I spoke about when I was at the G-SAC

[00:53:26–00:53:31] **Speaker (unattributed):** in Dubai about how everybody's talking about agent security,

[00:53:31–00:53:35] **Speaker (unattributed):** which is worth more and scares people enough

[00:53:35–00:53:46] **Speaker (unattributed):** want to do something about it, then agent governance. Agreed, I'll say?

[00:53:46–00:53:52] **Speaker (unattributed):** Yeah, yeah, no, definitely. And I think there's definitely a bloodline between the two.

[00:53:54–00:53:59] **Speaker (unattributed):** So it's definitely worth mentioning. A lot of our competitors are sitting on the borderline.

[00:53:59–00:54:05] **Speaker (unattributed):** Like, if you think about Jetstream as a company, their website Jetstream.Security,

[00:54:05–00:54:12] **Speaker (unattributed):** but you go to the top of their website and they are calling themselves AI governance platform.

[00:54:12–00:54:15] **Speaker (unattributed):** But the company's name is Jetstream Security.

[00:54:15–00:54:23] **Speaker (unattributed):** So it's almost interchangeable in terms of what we're doing the way people are using it.

[00:54:23–00:54:28] **Speaker (unattributed):** But the thing is, from a messaging us, that is how we get them on board.

[00:54:28–00:54:33] **Speaker (unattributed):** Getting to them have governance as far as my research has been,

[00:54:33–00:54:37] **Speaker (unattributed):** it's like saying, well, you don't really need it.

[00:54:37–00:54:41] **Speaker (unattributed):** You never get an individual engineer getting governance.

[00:54:41–00:54:46] **Speaker (unattributed):** because you ask, it's like so on, say they're thinking, oh, I need to govern myself.

[00:54:46–00:54:53] **Speaker (unattributed):** Like it just doesn't even make sense. And you know, yeah, they'll buy security.

[00:54:53–00:54:59] **Speaker (unattributed):** And you know, I'm manager will buy security and governance because they want to govern their team.

[00:55:00–00:55:05] **Speaker (unattributed):** And then the security budget is all as bigger than anything, which is like a new line out of

[00:55:05–00:55:11] **Speaker (unattributed):** which is governance. Yeah, exactly. So we want to target the part that already has money.

[00:55:13–00:55:17] **Speaker (unattributed):** Yes, so it depends on the organization and the internal structure.

[00:55:17–00:55:21] **Speaker (unattributed):** Does the product leader lead research and product?

[00:55:21–00:55:24] **Speaker (unattributed):** Is it the CTO, titles where the, where is the budget?

[00:55:24–00:55:28] **Speaker (unattributed):** And is the engineering owner and of all times I'm seeing,

[00:55:28–00:55:32] **Speaker (unattributed):** and also depends on which market that customer or that enterprise is selling

[00:55:32–00:55:32] **Speaker (unattributed):** the products into.

[00:55:32–00:55:33] **Speaker (unattributed):** Is it consumer?

[00:55:33–00:55:35] **Speaker (unattributed):** Do they have a B2B product?

[00:55:35–00:55:38] **Speaker (unattributed):** The PLG motion with individual developers,

[00:55:38–00:55:42] **Speaker (unattributed):** we need to think through the messaging and you folks are experts at that with

[00:55:42–00:55:46] **Speaker (unattributed):** Ashwin as well in terms of developer relations and what is an individual developer looking at?

[00:55:46–00:55:50] **Speaker (unattributed):** They want to show they're better at this than others. They want their resume to be published. They want

[00:55:50–00:55:56] **Speaker (unattributed):** to build secure code and have this gate built into their coding practices. They're more mature

[00:55:56–00:56:01] **Speaker (unattributed):** developer. Whatever the messaging there is, these two things will converge but the part of money

[00:56:01–00:56:09] **Speaker (unattributed):** and enterprise, that's where folks like Manoj and Andrew, all these teams have to build software

[00:56:09–00:56:11] **Speaker (unattributed):** that has to be then reviewed by security teams, right?

[00:56:11–00:56:15] **Speaker (unattributed):** And the budget, it depends on again,

[00:56:15–00:56:17] **Speaker (unattributed):** the organization, does the security team,

[00:56:17–00:56:19] **Speaker (unattributed):** does that compliance team,

[00:56:19–00:56:22] **Speaker (unattributed):** is it sitting within legal?

[00:56:22–00:56:25] **Speaker (unattributed):** Or because I've seen those teams inject themselves

[00:56:25–00:56:27] **Speaker (unattributed):** towards the end and they're trying to get to the beginning

[00:56:27–00:56:28] **Speaker (unattributed):** of the product development lifecycle

[00:56:28–00:56:31] **Speaker (unattributed):** by building relationships with product and engineering

[00:56:31–00:56:32] **Speaker (unattributed):** to say, hey, give us a seat at the table.

[00:56:32–00:56:36] **Speaker (unattributed):** Let us show you the important aspects of coding

[00:56:36–00:56:38] **Speaker (unattributed):** that you need to consider from a security standpoint

[00:56:38–00:56:43] **Speaker (unattributed):** front, but they're just influencing the conversation or trying to inject themselves

[00:56:43–00:56:48] **Speaker (unattributed):** into the product development life cycle, if you will, or agent development life cycle.

[00:56:48–00:56:53] **Speaker (unattributed):** But the budget from what I've seen sits with the engineering leaders who will say, yeah,

[00:56:53–00:56:58] **Speaker (unattributed):** we absolutely have to have this because this will then develop code in a safe fashion,

[00:56:58–00:57:02] **Speaker (unattributed):** right? So if you can build a package around this, which is throughout your agent development

[00:57:02–00:57:06] **Speaker (unattributed):** life cycle, your building traces and e-walls and whatever other frameworks you've built

[00:57:06–00:57:12] **Speaker (unattributed):** language. That's why all these teams have an AI chief for somebody VP of AI being hired

[00:57:12–00:57:17] **Speaker (unattributed):** or they already have one, if they don't have one they're behind. That person's job is

[00:57:17–00:57:23] **Speaker (unattributed):** to bring that type of expertise. So we try to educate some of those folks and then go directly

[00:57:23–00:57:27] **Speaker (unattributed):** to directors of engineering, managers of engineering to say here's a framework for your development

[00:57:27–00:57:35] **Speaker (unattributed):** teams to be productive with agents, but all these teams are trying to create structures and standards

[00:57:35–00:57:41] **Speaker (unattributed):** within their organizations around, they calling them, what are the terms they use, not Godreel,

[00:57:41–00:57:47] **Speaker (unattributed):** they use a different term, like to keep, so their standards and specs and core development are

[00:57:47–00:57:52] **Speaker (unattributed):** adhered to, so they're building their own standards internally for agents to use.

[00:57:53–00:57:58] **Speaker (unattributed):** So if you can become part of that standard within a company that the AI team is launching

[00:57:58–00:58:01] **Speaker (unattributed):** to bring other engineers on board. So this is the shift that is happening.

[00:58:01–00:58:05] **Speaker (unattributed):** And that's why, and that's where the market is,

[00:58:05–00:58:07] **Speaker (unattributed):** which is what all of us are saying.

[00:58:07–00:58:10] **Speaker (unattributed):** So, I think some of the way that part of money sits

[00:58:10–00:58:12] **Speaker (unattributed):** to here will depend on the organization

[00:58:12–00:58:14] **Speaker (unattributed):** in terms of whether R&D reports

[00:58:14–00:58:16] **Speaker (unattributed):** into the product team or not.

[00:58:16–00:58:18] **Speaker (unattributed):** Most of the times it won't,

[00:58:18–00:58:19] **Speaker (unattributed):** it may be the other way around

[00:58:19–00:58:21] **Speaker (unattributed):** with the product roads into engineering,

[00:58:21–00:58:25] **Speaker (unattributed):** which is perfectly normal as well.

[00:58:25–00:58:28] **Speaker (unattributed):** But if we start with engineering leaders

[00:58:28–00:58:30] **Speaker (unattributed):** and test around this,

[00:58:30–00:58:34] **Speaker (unattributed):** while you folks also work on individual developers

[00:58:34–00:58:35] **Speaker (unattributed):** and the message in around that,

[00:58:35–00:58:37] **Speaker (unattributed):** that might be one way to think about this.

[00:58:37–00:58:40] **Speaker (unattributed):** Okay, so let me go on to the next phase.

[00:58:40–00:58:41] **Speaker (unattributed):** That's fine, great.

[00:58:41–00:58:46] **Speaker (unattributed):** Okay, so my go to market for OpenBox gates

[00:58:47–00:58:48] **Speaker (unattributed):** and I'll just call it gates

[00:58:48–00:58:50] **Speaker (unattributed):** unless Asim comes up with some other name

[00:58:50–00:58:52] **Speaker (unattributed):** or you guys come up with some other name is,

[00:58:52–00:58:56] **Speaker (unattributed):** what I'm gonna do is I'm gonna use the playbook

[00:58:56–00:58:58] **Speaker (unattributed):** of how do we go viral, right?

[00:58:58–00:59:00] **Speaker (unattributed):** Asim and I talked about this

[00:59:00–00:59:03] **Speaker (unattributed):** and Asim was asking, how would you think we're going to go viral?

[00:59:03–00:59:04] **Speaker (unattributed):** Do we just happen, chance?

[00:59:04–00:59:06] **Speaker (unattributed):** Hopefully, we go viral.

[00:59:06–00:59:10] **Speaker (unattributed):** Well, the way you go viral is the way digital media works

[00:59:10–00:59:11] **Speaker (unattributed):** everywhere in the world.

[00:59:11–00:59:13] **Speaker (unattributed):** You pay influences.

[00:59:13–00:59:13] **Speaker (unattributed):** It's it.

[00:59:13–00:59:16] **Speaker (unattributed):** That's the only way you do it.

[00:59:16–00:59:18] **Speaker (unattributed):** The happen chance of doing something

[00:59:18–00:59:21] **Speaker (unattributed):** where you go and release open-claw equivalent of a project

[00:59:21–00:59:24] **Speaker (unattributed):** and the whole world wants to start using it,

[00:59:24–00:59:26] **Speaker (unattributed):** it doesn't happen very often.

[00:59:26–00:59:29] **Speaker (unattributed):** But what you can do, and this is where I was going

[00:59:29–00:59:37] **Speaker (unattributed):** Ashwin to get involved is get Ashwin to select 10 decent developers who are put decent projects out there

[00:59:37–00:59:45] **Speaker (unattributed):** where it doesn't have to have the highest number of GitHub stars but at least they have good following good voice

[00:59:45–00:59:49] **Speaker (unattributed):** Right go and reach out to them and sort of say you know what?

[00:59:49–00:59:57] **Speaker (unattributed):** Your famous you've got your project out there blah blah blah. We're willing to pay you to you for you to review our

[00:59:57–01:00:02] **Speaker (unattributed):** our OpenBox gate which obviously will mean they'll search the rest of the product

[01:00:03–01:00:11] **Speaker (unattributed):** and if you're willing to review it and give us a testimonial, we would be willing to pay you for

[01:00:11–01:00:21] **Speaker (unattributed):** it. Part of that testimonial is that you will need to, obviously, say something in the wild world,

[01:00:21–01:00:29] **Speaker (unattributed):** West of digital media that's why you're an influencer. So my goal is to say the way we do it is

[01:00:29–01:00:37] **Speaker (unattributed):** is I cannot find a single way. It's funny, given example, I probably spent most of what's

[01:00:37–01:00:46] **Speaker (unattributed):** today, Wednesday, Thursday, Thursday, on Monday or Tuesday, wide coding a number of projects

[01:00:46–01:00:54] **Speaker (unattributed):** that I thought I could use whether it was to do with OpenBox what I call call that I could open

[01:00:54–01:01:01] **Speaker (unattributed):** source and maybe somebody it would be picked up and it would go viral right to give an example Ashwin

[01:01:01–01:01:06] **Speaker (unattributed):** you know that what was that thing you made open source that you put together about book reading

[01:01:06–01:01:14] **Speaker (unattributed):** or something? Yeah it looks regarding that you know those e-increasants so I just build up on

[01:01:14–01:01:21] **Speaker (unattributed):** for that where agents can now read your book, summarize it for you, ask questions around it

[01:01:22–01:01:30] **Speaker (unattributed):** in a small, e-n-divise. Right. And you made that open source. Yeah. And how's the traction gone?

[01:01:32–01:01:40] **Speaker (unattributed):** Not much. I didn't promote it, but I got like two stars. Right. So, so it shows you that if you

[01:01:40–01:01:48] **Speaker (unattributed):** just put it out there, nothing happens. Yeah. Yeah. Yeah, nobody finds you. And it's the way it goes.

[01:01:48–01:01:55] **Speaker (unattributed):** So the whole idea behind it is we are told us in next week to make me videos of the whole of our

[01:01:55–01:02:02] **Speaker (unattributed):** platform, not at a technical deep level but at least at the level where I can start and again

[01:02:02–01:02:09] **Speaker (unattributed):** that we will have our YouTube channel. Ashwin, you know the YouTube channel that junior started,

[01:02:09–01:02:15] **Speaker (unattributed):** do we have control of that again with the proper sort of generic email address or is it still

[01:02:15–01:02:20] **Speaker (unattributed):** fucked up? I'm sorry to use that word. No, no, we have control over the OpenBox,

[01:02:21–01:02:26] **Speaker (unattributed):** we do the countdown. Okay, so the idea is we're going to start that from fresh,

[01:02:27–01:02:33] **Speaker (unattributed):** delete whatever's there or if we do keep it, let's categorize it properly. And Asim is going to start

[01:02:34–01:02:39] **Speaker (unattributed):** putting videos together for the whole of our platform, but now doing it by product.

[01:02:40–01:02:42] **Speaker (unattributed):** not just by generically less login

[01:02:42–01:02:44] **Speaker (unattributed):** and let you walk you through the product.

[01:02:44–01:02:45] **Speaker (unattributed):** He should start his journey with,

[01:02:45–01:02:48] **Speaker (unattributed):** I am gonna demonstrate OpenBox gate.

[01:02:48–01:02:51] **Speaker (unattributed):** I'm gonna blah, blah, blah, this and then do the high level.

[01:02:51–01:02:53] **Speaker (unattributed):** And then I'm gonna, as worth found this,

[01:02:53–01:02:57] **Speaker (unattributed):** I'm gonna do videos about the more technical detail

[01:02:57–01:03:00] **Speaker (unattributed):** underneath of it, or get Ashway, no B, whatever it may be.

[01:03:00–01:03:04] **Speaker (unattributed):** But certainly, there'll be deeper and deeper videos.

[01:03:04–01:03:08] **Speaker (unattributed):** We're almost to the point of how do you do this, right?

[01:03:08–01:03:10] **Speaker (unattributed):** we will get to that stage, that's part of my plan.

[01:03:10–01:03:13] **Speaker (unattributed):** But the main plan I have is start of November

[01:03:13–01:03:15] **Speaker (unattributed):** is that Ashwin is gonna target

[01:03:17–01:03:19] **Speaker (unattributed):** give me a list of 50 influencers,

[01:03:19–01:03:23] **Speaker (unattributed):** good developers who's got decent following,

[01:03:23–01:03:26] **Speaker (unattributed):** decent projects, if they've got something to say,

[01:03:26–01:03:27] **Speaker (unattributed):** but at least people will go,

[01:03:27–01:03:30] **Speaker (unattributed):** okay what was this?

[01:03:30–01:03:31] **Speaker (unattributed):** What is he talking about?

[01:03:31–01:03:31] **Speaker (unattributed):** Why?

[01:03:31–01:03:34] **Speaker (unattributed):** Now, if it means we gotta spend some money

[01:03:34–01:03:38] **Speaker (unattributed):** that could be, whether it's $100 to get him to try,

[01:03:38–01:03:45] **Speaker (unattributed):** $500 or $1,000 depending on or $10,000 depending on who they are.

[01:03:45–01:03:52] **Speaker (unattributed):** If you've got someone that is phenomenal, but they're willing to accept $10,000 from us,

[01:03:52–01:03:58] **Speaker (unattributed):** but they're willing to literally try our product, use it, put something credible out there,

[01:03:58–01:04:04] **Speaker (unattributed):** let us have a testimonial, whatever it may be, that money is the only way we're going

[01:04:04–01:04:05] **Speaker (unattributed):** to go viral.

[01:04:05–01:04:08] **Speaker (unattributed):** is no other way, although I am going to try like the

[01:04:08–01:04:11] **Speaker (unattributed):** clappers to try to build something, which I'm starting to

[01:04:11–01:04:14] **Speaker (unattributed):** build loads of different proof of concepts, which will be

[01:04:14–01:04:17] **Speaker (unattributed):** like, what can I build? And what I was going to throw

[01:04:17–01:04:24] **Speaker (unattributed):** Ashwin to you, Tony, B, Tino, that, Brian, whatever, was

[01:04:24–01:04:28] **Speaker (unattributed):** that in the month of November, I want all of you to try to

[01:04:28–01:04:33] **Speaker (unattributed):** think of, what could you build that would utilize? Remember,

[01:04:33–01:04:40] **Speaker (unattributed):** There's nothing you can build for which is OpenBox gate or the chef that's just a capability.

[01:04:40–01:04:45] **Speaker (unattributed):** But what can you build that uses OpenBox runtime,

[01:04:45–01:04:49] **Speaker (unattributed):** if we call it core the runtime that could be useful to somebody,

[01:04:49–01:04:53] **Speaker (unattributed):** but it's only useful because it has governance,

[01:04:53–01:04:56] **Speaker (unattributed):** so it has governance-class security.

[01:04:56–01:05:02] **Speaker (unattributed):** That will be one of the takeaways or one of the asks that I have Ashwin of you,

[01:05:02–01:05:05] **Speaker (unattributed):** all the developers in the company. I'll be asking you guys,

[01:05:05–01:05:10] **Speaker (unattributed):** please think of what could you buy code and knock it pretty quickly

[01:05:10–01:05:15] **Speaker (unattributed):** and we could throw into a repo. And so to say, hey, you know what,

[01:05:15–01:05:21] **Speaker (unattributed):** if you're like, give an example, Shoria earlier, just did a demo of a

[01:05:21–01:05:27] **Speaker (unattributed):** support agent's end to end. The agent does one, there's this one, there's this one, there's

[01:05:27–01:05:33] **Speaker (unattributed):** That to me is something I can offer, but we didn't talk a lot about governance of that.

[01:05:33–01:05:39] **Speaker (unattributed):** But if I can add governance to that workflow and put that out there,

[01:05:39–01:05:45] **Speaker (unattributed):** because in that way, you know that support agent is doing the right thing.

[01:05:45–01:05:48] **Speaker (unattributed):** And we make some noise about it by sort of saying,

[01:05:48–01:05:54] **Speaker (unattributed):** if you as a company are looking to use and build a gentry systems where you will need support,

[01:05:54–01:05:59] **Speaker (unattributed):** and you want these four agents that talk to each other to resolve the support ticket

[01:05:59–01:06:03] **Speaker (unattributed):** and it's already done out of the box, clone it, spin it up,

[01:06:03–01:06:10] **Speaker (unattributed):** it points to OpenBox, you get your governance, your security, that's the kind of thing I'm looking for.

[01:06:12–01:06:13] **Speaker (unattributed):** That's big length.

[01:06:14–01:06:19] **Speaker (unattributed):** Sorry, you just reminded me of it depends, some people have commented in a different way,

[01:06:19–01:06:27] **Speaker (unattributed):** like if you think about that company, Liza, LYZR, they basically came at enterprises as like an

[01:06:27–01:06:32] **Speaker (unattributed):** agent builder and then afterwards realized how important governance is now they've launched this

[01:06:32–01:06:38] **Speaker (unattributed):** control plane. So we're almost going the other way where you know governance can't be solved like

[01:06:38–01:06:46] **Speaker (unattributed):** that. So you're basically selling the, you're basically open sourcing like an agent builder type

[01:06:46–01:06:51] **Speaker (unattributed):** capability, but the governance just has to come in as a standard. So you're just trying to

[01:06:52–01:06:58] **Speaker (unattributed):** find a way to be valuable, right, to enterprises. Well, the thing is what we're trying to do is I

[01:06:58–01:07:05] **Speaker (unattributed):** want to make it happen where every, every small medium-sized business out there that doesn't know

[01:07:05–01:07:12] **Speaker (unattributed):** how to do XYZ will be to know that if you go to OpenBox, here are all of the projects

[01:07:12–01:07:19] **Speaker (unattributed):** that we have got which allow you to achieve some benefits in your company, some value risk, fix a

[01:07:19–01:07:24] **Speaker (unattributed):** fix a pain point help you with it. You can clone it, we're giving it to you for free. And by the way

[01:07:24–01:07:29] **Speaker (unattributed):** isn't that what Squitchie's doing, like they're doing the agent builders.

[01:07:29–01:07:34] **Speaker (unattributed):** No, no, but what they're doing is they're saying here's a platform where you can build these agent

[01:07:34–01:07:41] **Speaker (unattributed):** builders, right? Right? Okay. So it's giving them the agents directly ourselves. Yeah, yeah,

[01:07:41–01:07:48] **Speaker (unattributed):** we could literally take their agent build their platform and build 10 solutions

[01:07:49–01:07:53] **Speaker (unattributed):** because they're going to want to. Yeah, yeah, and we could just say to

[01:07:53–01:07:55] **Speaker (unattributed):** to set, aset, you know. [ASR uncertain]

[01:07:55–01:08:02] **Speaker (unattributed):** What are the things you've gone to the effort of putting in OpenBox? And obviously, what are [ASR uncertain]

[01:08:02–01:08:07] **Speaker (unattributed):** they buying when they buy OpenBox? Are they buying an enterprise license? Are they buying [ASR uncertain]

[01:08:07–01:08:17] **Speaker (unattributed):** a team license? You and I are not even at that conversation with them up. No, I kind of left [ASR uncertain]

[01:08:17–01:08:22] **Speaker (unattributed):** at you. You know what the on-prem cost is? And I think you guys will be putting together [ASR uncertain]

[01:08:22–01:08:29] **Speaker (unattributed):** the casting for the SaaS, right? So I think it'll be something along those lines and then

[01:08:29–01:08:33] **Speaker (unattributed):** then basically a conversation if he wants it if it's not suited for him.

[01:08:33–01:08:39] **Speaker (unattributed):** Yeah, so from our perspective, whether we knock up some example applications using their

[01:08:39–01:08:44] **Speaker (unattributed):** platform and give it to them and say, here's we've done this on yours, please make this

[01:08:44–01:08:51] **Speaker (unattributed):** available to the whole of your community, right? And because at the end of the day, the

[01:08:51–01:08:55] **Speaker (unattributed):** The way Seth makes money isn't because he's got these built solutions.

[01:08:55–01:09:00] **Speaker (unattributed):** He's saying we have got a tool to help you build these solutions payers because they're

[01:09:00–01:09:05] **Speaker (unattributed):** pretty much selling themselves as a tool service company.

[01:09:05–01:09:08] **Speaker (unattributed):** If I go to him and say, oh, I've got an FDET.

[01:09:08–01:09:09] **Speaker (unattributed):** That will work.

[01:09:09–01:09:11] **Speaker (unattributed):** I knock out 20 a week.

[01:09:11–01:09:17] **Speaker (unattributed):** That's not going to work because you're cannibalizing his income.

[01:09:17–01:09:20] **Speaker (unattributed):** But again, somebody has to market that solution.

[01:09:20–01:09:25] **Speaker (unattributed):** Yeah. And that's a support example. It's a very big market and there are so many big players

[01:09:25–01:09:30] **Speaker (unattributed):** that can walk you through that separately to here in the meeting. No, no, agree. But what I'm saying

[01:09:30–01:09:37] **Speaker (unattributed):** is there's a group, if you take SMBs and again, as part of my research and audit is there are certain

[01:09:37–01:09:44] **Speaker (unattributed):** pain points pretty much every SMB has, right? And the part is what you're trying to do is put something

[01:09:44–01:09:52] **Speaker (unattributed):** out there as a freebie by sort of saying, you know what, it's done. You just need the

[01:09:52–01:09:58] **Speaker (unattributed):** most minimum knowledge, right? And you can spin this up. Now what I've noticed is the

[01:09:58–01:10:03] **Speaker (unattributed):** majority of people who are doing really well, I call it at the application there, is

[01:10:03–01:10:09] **Speaker (unattributed):** that people don't know how to build agents. But if you can, if you've got some kind of

[01:10:09–01:10:14] **Speaker (unattributed):** platform, some kind of ability where somebody just says, I need two agents, one that does

[01:10:14–01:10:19] **Speaker (unattributed):** there's one that checks the output of this one over that blah blah blah, they just do it through

[01:10:19–01:10:25] **Speaker (unattributed):** natural language or whatever or talking voice to text or whatever and it builds it and they can run it

[01:10:26–01:10:34] **Speaker (unattributed):** you're making money yeah these are you know every single company I know and it's interesting how

[01:10:34–01:10:41] **Speaker (unattributed):** last year I was in a keynote speaker in Bogdard Columbia talking about AI governance and I met a

[01:10:41–01:10:47] **Speaker (unattributed):** company outside in the area where this lady was running it and all she did was build

[01:10:47–01:10:53] **Speaker (unattributed):** N10 workflows and she was charging her N10 workflow $10,000.

[01:10:55–01:10:58] **Speaker (unattributed):** And she was already in the millions.

[01:10:59–01:11:04] **Speaker (unattributed):** Exactly. So the entire software development life cycle is moving to agent development.

[01:11:04–01:11:09] **Speaker (unattributed):** That's where the market is. Nobody understands this different level of understanding.

[01:11:09–01:11:13] **Speaker (unattributed):** and all the integrations we have land graft and coral,

[01:11:13–01:11:17] **Speaker (unattributed):** all of these clairs have their own education on this topic out there

[01:11:17–01:11:20] **Speaker (unattributed):** to build a developer community, get them all on their platforms.

[01:11:20–01:11:24] **Speaker (unattributed):** That's where the market is at, now how do we attach to that market?

[01:11:24–01:11:25] **Speaker (unattributed):** Well, again, yes.

[01:11:25–01:11:33] **Speaker (unattributed):** And as I said, I won't complete it off today, but I'm aiming towards

[01:11:33–01:11:34] **Speaker (unattributed):** founding this off.

[01:11:34–01:11:39] **Speaker (unattributed):** And my goal is by early next week I will be able to do my final

[01:11:39–01:11:43] **Speaker (unattributed):** sort of presentation with all my mockups and everything else with the intent that we can use

[01:11:43–01:11:50] **Speaker (unattributed):** the rest of the week to turn it into a proper final, you know, go to market for a final website,

[01:11:50–01:11:56] **Speaker (unattributed):** final tactical plans, product owners, blah, blah, blah, and sort of say, right, the moment that

[01:11:56–01:12:02] **Speaker (unattributed):** website is now open ready at the start of November, everybody knows what we're doing and what's the

[01:12:02–01:12:08] **Speaker (unattributed):** game that's going to be played. Now Ashwin, from your own experience, you know, again, I'm not saying

[01:12:08–01:12:21] **Speaker (unattributed):** is rocket science. You know that awesome website, open repo, sorry, sorry Ashwin,

[01:12:21–01:12:29] **Speaker (unattributed):** yeah, yeah. Can you just walk through the conversation you had with that guy and

[01:12:29–01:12:38] **Speaker (unattributed):** what he wanted to charge to do XYZ? Yes, so awesome, it's a awesome agent with

[01:12:38–01:12:51] **Speaker (unattributed):** So basically these are repos which basically is like a collective repo where you just list everything around age and like tools and everything.

[01:12:51–01:12:55] **Speaker (unattributed):** So this is a common path practice in GitHub.

[01:12:55–01:13:04] **Speaker (unattributed):** And this repo particularly has like 44k, I remember correctly like 44k stars and that's

[01:13:04–01:13:08] **Speaker (unattributed):** huge when you consider in GitHub terms.

[01:13:08–01:13:15] **Speaker (unattributed):** So what that guy is saying is like he would place OpenBox in that repo so that anyone

[01:13:15–01:13:23] **Speaker (unattributed):** who visits that repo sees OpenBox and he is charging 150 dollars per month and we will

[01:13:23–01:13:25] **Speaker (unattributed):** be turning a pilot.

[01:13:25–01:13:28] **Speaker (unattributed):** You're planning to run a pilot with him for three months

[01:13:28–01:13:36] **Speaker (unattributed):** to see what's at his end.

[01:13:36–01:13:40] **Speaker (unattributed):** So what I'm saying is obviously,

[01:13:40–01:13:42] **Speaker (unattributed):** where do we see any success from that or not?

[01:13:42–01:13:44] **Speaker (unattributed):** I just booked out some about it.

[01:13:44–01:13:46] **Speaker (unattributed):** And as him was like, yeah, I mean,

[01:13:46–01:13:48] **Speaker (unattributed):** if it's like $450, or $1,

[01:13:48–01:13:53] **Speaker (unattributed):** and we can justify that maybe we'll get some traction from it

[01:13:53–01:13:54] **Speaker (unattributed):** then why not?

[01:13:54–01:13:58] **Speaker (unattributed):** It's not like we can't put some money where it might actually

[01:13:58–01:13:59] **Speaker (unattributed):** work.

[01:13:59–01:14:11] **Speaker (unattributed):** So what I'm trying to do now is over the next few days is finish off the rest of the work that I'm putting together and present it to you guys and sort of present it with even some idea of budgets.

[01:14:11–01:14:17] **Speaker (unattributed):** I'll send for you to sort of get a feel for the kind of money that we may need to try to get this something viral to happen.

[01:14:18–01:14:26] **Speaker (unattributed):** And remember, I see it as I can't get something viral to happen when I've got a lot of wooden straw without a light.

[01:14:26–01:14:32] **Speaker (unattributed):** And I'm going to build the straw and the wood to be able to build a fire, but we're going

[01:14:32–01:14:39] **Speaker (unattributed):** to have to make a not wait for lightning to strike, which is hoping by magic.

[01:14:39–01:14:42] **Speaker (unattributed):** It goes viral just because we are there.

[01:14:42–01:14:49] **Speaker (unattributed):** We're going to have to put some petrol and put a light to it.

[01:14:49–01:14:52] **Speaker (unattributed):** Is there any, I love this discussion.

[01:14:52–01:14:59] **Speaker (unattributed):** Sorry, I'll just agree with you.

[01:14:59–01:15:04] **Speaker (unattributed):** In all these examples, pilots and POCs we have with

[01:15:04–01:15:07] **Speaker (unattributed):** every or squishy next discovery,

[01:15:07–01:15:10] **Speaker (unattributed):** are any of these around the development world?

[01:15:10–01:15:15] **Speaker (unattributed):** You just plug an MCP or whatever it is and it automatically

[01:15:15–01:15:19] **Speaker (unattributed):** governs or securitizes your development?

[01:15:19–01:15:22] **Speaker (unattributed):** Or maybe there were so many startups at that week

[01:15:22–01:15:26] **Speaker (unattributed):** that are all trying to do something, right?

[01:15:26–01:15:29] **Speaker (unattributed):** What if we just get a few of them to start building using our

[01:15:29–01:15:31] **Speaker (unattributed):** as DKN, give it to them for free.

[01:15:31–01:15:35] **Speaker (unattributed):** I mean, get them to attest to their agent development

[01:15:35–01:15:37] **Speaker (unattributed):** being much stronger with OpenBox.

[01:15:37–01:15:40] **Speaker (unattributed):** Like what if we just get four or five logos

[01:15:40–01:15:44] **Speaker (unattributed):** and testimonials around this development stuff

[01:15:44–01:15:46] **Speaker (unattributed):** we're talking to for enterprises?

[01:15:46–01:15:49] **Speaker (unattributed):** As part of this, get them onboarded,

[01:15:49–01:15:51] **Speaker (unattributed):** get them to see some nice things

[01:15:51–01:15:52] **Speaker (unattributed):** and put their picture and some nice things

[01:15:52–01:15:55] **Speaker (unattributed):** on the website as examples.

[01:15:55–01:15:58] **Speaker (unattributed):** Not absolutely bar, I mean, the whole point is

[01:15:58–01:16:00] **Speaker (unattributed):** but I'm saying is, thinking of it this way,

[01:16:00–01:16:03] **Speaker (unattributed):** you could spend right up to Christmas,

[01:16:03–01:16:06] **Speaker (unattributed):** trying to land one enterprise client,

[01:16:06–01:16:08] **Speaker (unattributed):** which is not gonna be easy.

[01:16:08–01:16:09] **Speaker (unattributed):** It's not that it can't be done.

[01:16:09–01:16:12] **Speaker (unattributed):** It's the fact that we know the cycle is not easy.

[01:16:12–01:16:13] **Speaker (unattributed):** Yeah.

[01:16:13–01:16:16] **Speaker (unattributed):** But this thing around software development life cycle

[01:16:16–01:16:20] **Speaker (unattributed):** and sort of an OpenBox gate, left shift, whatever,

[01:16:20–01:16:23] **Speaker (unattributed):** is an easy, much much much easier.

[01:16:23–01:16:24] **Speaker (unattributed):** And it genuinely...

[01:16:24–01:16:25] **Speaker (unattributed):** Yeah, exactly.

[01:16:25–01:16:28] **Speaker (unattributed):** So, here I'm saying that is also the easy path

[01:16:28–01:16:30] **Speaker (unattributed):** to an enterprise, global market.

[01:16:30–01:16:31] **Speaker (unattributed):** I know you were saying the same thing.

[01:16:31–01:16:32] **Speaker (unattributed):** Yeah.

[01:16:32–01:16:34] **Speaker (unattributed):** So the question being is that you should

[01:16:34–01:16:39] **Speaker (unattributed):** be starting to think between now and when I finish my work,

[01:16:39–01:16:45] **Speaker (unattributed):** how do you activate this capability in San Francisco?

[01:16:45–01:16:47] **Speaker (unattributed):** Like you say, give it to them for free.

[01:16:47–01:16:49] **Speaker (unattributed):** Well, it's not easy to give them for free

[01:16:49–01:16:52] **Speaker (unattributed):** because I've talked to many of these people and said,

[01:16:52–01:16:53] **Speaker (unattributed):** oh, I've got a product.

[01:16:53–01:16:54] **Speaker (unattributed):** Why don't you try it?

[01:16:54–01:16:56] **Speaker (unattributed):** It's for free that I haven't got the time.

[01:16:56–01:16:58] **Speaker (unattributed):** Why should I make the time?

[01:16:58–01:17:01] **Speaker (unattributed):** what reason have I got for doing that, right?

[01:17:01–01:17:02] **Speaker (unattributed):** Yeah, that's exactly.

[01:17:02–01:17:05] **Speaker (unattributed):** So that's where any startups you talk to,

[01:17:05–01:17:06] **Speaker (unattributed):** any startup founders,

[01:17:06–01:17:08] **Speaker (unattributed):** and I'll think of you here that I met.

[01:17:08–01:17:11] **Speaker (unattributed):** I just want them to use the SDK or deploy it

[01:17:11–01:17:12] **Speaker (unattributed):** and give us testimonials,

[01:17:12–01:17:14] **Speaker (unattributed):** we can put them on a webpage.

[01:17:14–01:17:16] **Speaker (unattributed):** We're gonna start targeting

[01:17:16–01:17:17] **Speaker (unattributed):** and I'll come back to you with a plan,

[01:17:17–01:17:19] **Speaker (unattributed):** I'll work with a C moment.

[01:17:19–01:17:20] **Speaker (unattributed):** Because of engineering,

[01:17:20–01:17:22] **Speaker (unattributed):** directors of engineering.

[01:17:22–01:17:24] **Speaker (unattributed):** Okay, well, give an example, right?

[01:17:24–01:17:27] **Speaker (unattributed):** So again, as part of my go-to-market,

[01:17:27–01:17:30] **Speaker (unattributed):** I have this view which was like, hey, Asim,

[01:17:30–01:17:33] **Speaker (unattributed):** you know your company's invested in 40 projects.

[01:17:33–01:17:38] **Speaker (unattributed):** Can you get 10 of them to have a go at Openbox Gate

[01:17:38–01:17:41] **Speaker (unattributed):** and give us some feedback and just get right

[01:17:41–01:17:46] **Speaker (unattributed):** as a testimonial, right?

[01:17:46–01:17:50] **Speaker (unattributed):** Asim's got the power to go to his portfolio

[01:17:50–01:17:55] **Speaker (unattributed):** and go, hey guys, I need a favor.

[01:17:55–01:17:56] **Speaker (unattributed):** That's hard to do.

[01:17:58–01:18:02] **Speaker (unattributed):** Yeah, I want them to do that with the VC.

[01:18:02–01:18:06] **Speaker (unattributed):** Most of those companies who are in private

[01:18:06–01:18:13] **Speaker (unattributed):** integers, they all fighting right.

[01:18:13–01:18:17] **Speaker (unattributed):** I remember one of them wanted us to put something into

[01:18:17–01:18:20] **Speaker (unattributed):** our company and we didn't do it.

[01:18:20–01:18:24] **Speaker (unattributed):** OK, well, as I said, in my view is,

[01:18:24–01:18:28] **Speaker (unattributed):** everybody needs to open their black books, including mine

[01:18:28–01:18:32] **Speaker (unattributed):** and Ashwein and B. Yeah, mine will be done in other ways.

[01:18:32–01:18:34] **Speaker (unattributed):** There'll be other types of connections.

[01:18:34–01:18:38] **Speaker (unattributed):** Yeah, just like Eros and others, those were the black books.

[01:18:38–01:18:42] **Speaker (unattributed):** So we need to do that now with this new product.

[01:18:42–01:18:47] **Speaker (unattributed):** Like I think, let's get, if I try to close Eros,

[01:18:47–01:18:51] **Speaker (unattributed):** then I might be able to get this deployed within Eros as well.

[01:18:51–01:18:52] **Speaker (unattributed):** Right, they'll be using code editors.

[01:18:52–01:18:54] **Speaker (unattributed):** So then I get this into Eros.

[01:18:54–01:18:57] **Speaker (unattributed):** We can try a few others like that as well.

[01:18:57–01:19:01] **Speaker (unattributed):** Okay, but that again, part of my go-to-market

[01:19:01–01:19:07] **Speaker (unattributed):** tactical plan is to go to every single person in the company that we have and say you've

[01:19:07–01:19:14] **Speaker (unattributed):** got to land one company. It's not like they have to pay. You've got to ask them that they've

[01:19:14–01:19:22] **Speaker (unattributed):** got to almost everyone, we know, must have a developer, we can win over to try our open

[01:19:22–01:19:30] **Speaker (unattributed):** boss gate, we'll make it dead easy for them, try it, play around with it, it's free and

[01:19:30–01:19:35] **Speaker (unattributed):** give us some feedback and ideally maybe give us a testimonial. Now, what's interesting

[01:19:35–01:19:47] **Speaker (unattributed):** is you can then go on the website that here are 10 developers, a group who are used or

[01:19:47–01:19:55] **Speaker (unattributed):** are using it. I have to work out the wording, our product from company XYZ, whatever. And

[01:19:55–01:19:57] **Speaker (unattributed):** And I'm not infringing anything.

[01:19:57–01:20:00] **Speaker (unattributed):** They do work at that company.

[01:20:00–01:20:03] **Speaker (unattributed):** I'm not saying that company is using the product.

[01:20:03–01:20:06] **Speaker (unattributed):** I can just say, blah, blah, blah.

[01:20:06–01:20:09] **Speaker (unattributed):** I'm trying to work out without sort of getting,

[01:20:09–01:20:11] **Speaker (unattributed):** being called for defamation or something.

[01:20:11–01:20:14] **Speaker (unattributed):** But one of my technical plans in November

[01:20:14–01:20:17] **Speaker (unattributed):** is that every single person in the company

[01:20:17–01:20:21] **Speaker (unattributed):** should land at least one, one.

[01:20:21–01:20:23] **Speaker (unattributed):** And I'm not talking about paying.

[01:20:23–01:20:25] **Speaker (unattributed):** I'm just talking about one developer.

[01:20:25–01:20:28] **Speaker (unattributed):** they know at an organization, right?

[01:20:28–01:20:32] **Speaker (unattributed):** Not a solar wealth, not a one-man band.

[01:20:32–01:20:33] **Speaker (unattributed):** It means nothing.

[01:20:33–01:20:37] **Speaker (unattributed):** Somebody who is at a reputable company to go,

[01:20:37–01:20:41] **Speaker (unattributed):** I will take a use and play with it.

[01:20:41–01:20:45] **Speaker (unattributed):** If we're lucky and I think we can be,

[01:20:45–01:20:46] **Speaker (unattributed):** we'll win that person over enough,

[01:20:46–01:20:48] **Speaker (unattributed):** where they're like, you know what, yeah,

[01:20:48–01:20:49] **Speaker (unattributed):** I'll use it permanently.

[01:20:49–01:20:54] **Speaker (unattributed):** I've no reason to switch it off, okay?

[01:20:54–01:20:57] **Speaker (unattributed):** That will be one of the asks that I have asked him.

[01:20:57–01:21:02] **Speaker (unattributed):** at the start of November.

[01:21:02–01:21:04] **Speaker (unattributed):** Yeah, that's fine.

[01:21:04–01:21:05] **Speaker (unattributed):** Okay.

[01:21:05–01:21:06] **Speaker (unattributed):** And this also ties this,

[01:21:06–01:21:08] **Speaker (unattributed):** this also ties into where the market is.

[01:21:08–01:21:10] **Speaker (unattributed):** Everybody's trying to learn this stuff, right?

[01:21:10–01:21:12] **Speaker (unattributed):** So what if we make this a learning opportunity

[01:21:12–01:21:14] **Speaker (unattributed):** around the events we were planning

[01:21:14–01:21:16] **Speaker (unattributed):** and with Octane others,

[01:21:16–01:21:18] **Speaker (unattributed):** we can think through that.

[01:21:18–01:21:20] **Speaker (unattributed):** So this should be fairly straightforward.

[01:21:20–01:21:23] **Speaker (unattributed):** To get people on regardless of the logos they have,

[01:21:23–01:21:25] **Speaker (unattributed):** there'll be plenty of people who want to upscale

[01:21:25–01:21:27] **Speaker (unattributed):** on this Asian development life cycle.

[01:21:27–01:21:30] **Speaker (unattributed):** And we can just have our own spin to this

[01:21:30–01:21:32] **Speaker (unattributed):** agent development life cycle, just like LangGraph has,

[01:21:32–01:21:36] **Speaker (unattributed):** just like temporal has, just like all of them do cursor has.

[01:21:36–01:21:37] **Speaker (unattributed):** They have their education videos.

[01:21:37–01:21:42] **Speaker (unattributed):** We can have our own spin to do this message with security,

[01:21:42–01:21:43] **Speaker (unattributed):** because there's so much fear

[01:21:43–01:21:46] **Speaker (unattributed):** with all these folks talking about agents

[01:21:46–01:21:48] **Speaker (unattributed):** will take over the world and kill humans.

[01:21:48–01:21:51] **Speaker (unattributed):** It's perfect time to tap into that fear,

[01:21:51–01:21:53] **Speaker (unattributed):** to come at it from a security perspective

[01:21:53–01:21:55] **Speaker (unattributed):** and make them all heroes,

[01:21:55–01:21:57] **Speaker (unattributed):** saying you can be the thought leader inside your companies.

[01:21:57–01:21:59] **Speaker (unattributed):** We also have to them think through,

[01:21:59–01:22:04] **Speaker (unattributed):** Are we doing a weekly webinar with B. Or Ashwin or somebody else or Ankitab, if we can

[01:22:04–01:22:08] **Speaker (unattributed):** get the communication there to talk to these things, I'm happy to do them.

[01:22:08–01:22:12] **Speaker (unattributed):** Like, we're presenting to these folks, we're training them, we're getting this deployed

[01:22:12–01:22:13] **Speaker (unattributed):** in there.

[01:22:13–01:22:15] **Speaker (unattributed):** But that comes after to hear you right.

[01:22:15–01:22:17] **Speaker (unattributed):** But I think this should be fairly straightforward.

[01:22:17–01:22:24] **Speaker (unattributed):** I guess the way this is going to be about is the method I have in November is that once

[01:22:24–01:22:28] **Speaker (unattributed):** the website is done and tested, ready for the start of November.

[01:22:28–01:22:33] **Speaker (unattributed):** For me, the one of the reasons I'm going up to Hanoi to spend time with B

[01:22:33–01:22:36] **Speaker (unattributed):** is that to try to finish everything that I want,

[01:22:36–01:22:39] **Speaker (unattributed):** I'd rather be having next to be sitting there

[01:22:39–01:22:44] **Speaker (unattributed):** and getting it right perfectly, using Ashwin and AI at the moment to get it

[01:22:44–01:22:46] **Speaker (unattributed):** the new website done and tested.

[01:22:46–01:22:50] **Speaker (unattributed):** It's not going to need a heavy, like a massive,

[01:22:50–01:22:55] **Speaker (unattributed):** in terms of a ready-to-re-experience graphic designer,

[01:22:55–01:22:57] **Speaker (unattributed):** we can pretty much get most of what we want.

[01:22:57–01:23:00] **Speaker (unattributed):** And we're recruiting a graphic designer in Hanoi.

[01:23:00–01:23:03] **Speaker (unattributed):** We had one called Aslan, but we decided

[01:23:03–01:23:06] **Speaker (unattributed):** the guy is not good enough, so we've not taken him on,

[01:23:06–01:23:07] **Speaker (unattributed):** but we are looking for more.

[01:23:07–01:23:10] **Speaker (unattributed):** But my goal is to get it to the stage

[01:23:10–01:23:12] **Speaker (unattributed):** that by the end of next week,

[01:23:12–01:23:14] **Speaker (unattributed):** I have the whole of what I've

[01:23:14–01:23:16] **Speaker (unattributed):** talking about, the website ready to go.

[01:23:16–01:23:19] **Speaker (unattributed):** Now, from there onwards, like I said,

[01:23:19–01:23:27] **Speaker (unattributed):** The first week of November will be every single person in the company must find one developer

[01:23:27–01:23:36] **Speaker (unattributed):** who works at least a credible company would be better to commit to trying OpenBox gate

[01:23:36–01:23:40] **Speaker (unattributed):** shift left whatever we end up as we decide it to be. And I'm happy, Asim, if you want to

[01:23:40–01:23:48] **Speaker (unattributed):** work on that and I do need you to finalize it by middle of next week to go forward and say,

[01:23:48–01:23:52] **Speaker (unattributed):** Now, the way I work it is, you know, if we look at how many people we have in the company,

[01:23:52–01:23:57] **Speaker (unattributed):** outside of me working as our office manager, even including what's the name,

[01:23:57–01:24:03] **Speaker (unattributed):** eyes as well, she has to do this. I expect every single person in the company to come back with one

[01:24:03–01:24:11] **Speaker (unattributed):** developer that will, you know, you win them over to get to try our shift flag product,

[01:24:13–01:24:17] **Speaker (unattributed):** tell us what's good, what's bad about it, if they really love it, will they be willing to ride

[01:24:17–01:24:23] **Speaker (unattributed):** the testimonial. That is all I want in the first week of November. And from that, if I can do

[01:24:23–01:24:31] **Speaker (unattributed):** that, I should have anywhere from half a dozen to 12 to 15 developers and testimonials.

[01:24:32–01:24:40] **Speaker (unattributed):** Yeah, and let's try it with all of us, right? We can all try this as well. But use me as a guinea pig,

[01:24:40–01:24:45] **Speaker (unattributed):** right? Put me through this. I'll deploy it. Somebody will have to train me. Somebody has to tell me

[01:24:45–01:24:50] **Speaker (unattributed):** me very quick. What are those assets like? What is that process? We have to think through that now

[01:24:50–01:24:55] **Speaker (unattributed):** because let's say, first week of November, and suddenly people start to line up, then what?

[01:24:55–01:25:01] **Speaker (unattributed):** We have to think through exactly what that education onboarding and experience would look like for

[01:25:01–01:25:06] **Speaker (unattributed):** them to be successful. Sort of in a concierge way where it happens quickly, everything's documented.

[01:25:06–01:25:11] **Speaker (unattributed):** Here's a document with screen charge, walk through this, do this, click here. This is where you get

[01:25:11–01:25:14] **Speaker (unattributed):** and we need to think through a very specific use case.

[01:25:14–01:25:16] **Speaker (unattributed):** Simple one up front that they try and they go,

[01:25:16–01:25:18] **Speaker (unattributed):** aha, this works, this is simple.

[01:25:18–01:25:20] **Speaker (unattributed):** So we need to think through all of that

[01:25:20–01:25:21] **Speaker (unattributed):** and document that now,

[01:25:21–01:25:24] **Speaker (unattributed):** at the here outside of the website even,

[01:25:24–01:25:27] **Speaker (unattributed):** almost as an experience.

[01:25:27–01:25:28] **Speaker (unattributed):** It's gonna be on the website.

[01:25:28–01:25:33] **Speaker (unattributed):** The actual URUX experience of how you onboard somebody

[01:25:33–01:25:36] **Speaker (unattributed):** to the OpenBox gates and get it open running.

[01:25:36–01:25:39] **Speaker (unattributed):** Not only will we make it that is brainless

[01:25:39–01:25:49] **Speaker (unattributed):** any idea you can take and get it running would be that you would at least need to be a developer and know how to use Cloud Code or cursor or codex or news.

[01:25:49–01:25:58] **Speaker (unattributed):** At least you know you're not we're not trying to teach you the basics of them, but you're someone we have to at least start with the minimum bar that you know how to use that tool.

[01:25:58–01:26:01] **Speaker (unattributed):** Then the instructions will be if you use that tool,

[01:26:01–01:26:05] **Speaker (unattributed):** either follow these instructions or

[01:26:05–01:26:08] **Speaker (unattributed):** here is a file which is very little.

[01:26:08–01:26:10] **Speaker (unattributed):** It's got all the scripts and everything you need.

[01:26:10–01:26:13] **Speaker (unattributed):** You just click it, drop it into one of the folders,

[01:26:13–01:26:16] **Speaker (unattributed):** which is generally the case and bobs you're on till it will be open running.

[01:26:16–01:26:23] **Speaker (unattributed):** If it's something that simple with proof that they have,

[01:26:23–01:26:25] **Speaker (unattributed):** that they can start showing then it's great.

[01:26:25–01:26:28] **Speaker (unattributed):** It needs to be something super simple that they do in BOMIT works

[01:26:28–01:26:31] **Speaker (unattributed):** and their eyes light up.

[01:26:31–01:26:35] **Speaker (unattributed):** and they have a simple login to the OpenBox UI where they click on this one button to look at the

[01:26:35–01:26:41] **Speaker (unattributed):** audit of what happened, our audit screen or whatever shows the run-back playback of what happened

[01:26:41–01:26:46] **Speaker (unattributed):** and they go, oh my god, like, you know, this works. So now I'm excited. The initial

[01:26:47–01:26:51] **Speaker (unattributed):** experience being something very simple where they get positive proof based on their little

[01:26:51–01:26:58] **Speaker (unattributed):** effort they put in, tends to work for people's brains. Yeah, well as I said, that will be

[01:26:58–01:27:03] **Speaker (unattributed):** the intent and it really is, I mean to give you an example, you know, the way I put it together is

[01:27:04–01:27:10] **Speaker (unattributed):** it literally is one of where you go to a club, you type in the line on a Claude code,

[01:27:10–01:27:16] **Speaker (unattributed):** Claude plug in install, OpenBox gate and it's done. That is, that is literally what it should take

[01:27:16–01:27:24] **Speaker (unattributed):** with what I've been working on and you're done. Right? So we're going to work towards all of that.

[01:27:24–01:27:27] **Speaker (unattributed):** Don't worry, none of this is going to be heavy lifting. We're going to make it so it's

[01:27:27–01:27:34] **Speaker (unattributed):** brain debt is easy, you're up and running. But like I said, so if I set the target that

[01:27:34–01:27:40] **Speaker (unattributed):** every single person in the company has to find one developer per week or not even asking

[01:27:40–01:27:45] **Speaker (unattributed):** one developer a day or per hour, I'm just asking a developer a week. And we've let's say this

[01:27:45–01:27:53] **Speaker (unattributed):** 10 of us who do it, that's 40 people that we can say are using our product, even if all they

[01:27:53–01:27:58] **Speaker (unattributed):** should do is they log on and we're not going to go statistically and say, oh, by the way,

[01:27:58–01:28:04] **Speaker (unattributed):** we've got data at the moment that shows that they are using OpenBox 20 times a day,

[01:28:04–01:28:09] **Speaker (unattributed):** right? Or we're seeing a million actions a day. We just need to show that we have people using

[01:28:09–01:28:18] **Speaker (unattributed):** our product in November. Yeah, that's where I need to get to. So I already have step-up plan,

[01:28:18–01:28:22] **Speaker (unattributed):** I'm putting a project plan together of activities. We do week by week in November,

[01:28:22–01:28:30] **Speaker (unattributed):** and we just follow that and that will start moving the traction part of it because I want us

[01:28:30–01:28:37] **Speaker (unattributed):** if I can get us to equivalent to a million ARR, I want us to be able to talk to, we raise

[01:28:37–01:28:46] **Speaker (unattributed):** money, whatever we take, whether we do a full series, another seed, a top of a downround

[01:28:46–01:28:54] **Speaker (unattributed):** whatever it takes but what we need is money in the bank next year in the first quarter so we can

[01:28:54–01:28:59] **Speaker (unattributed):** really push this and I've got something in mind that I can start doing from November for two

[01:28:59–01:29:06] **Speaker (unattributed):** to three months that will move the needle. At the moment we've got inertia and we can't get off

[01:29:06–01:29:12] **Speaker (unattributed):** inertia. We need momentum. We need to get that needle the car. You know that first time you push a

[01:29:12–01:29:16] **Speaker (unattributed):** kind is so hard you can't get it to move but the moment you start getting to

[01:29:16–01:29:20] **Speaker (unattributed):** move it just feels like it's downhill it just keeps going.

[01:29:20–01:29:29] **Speaker (unattributed):** Yeah, okay, that's that's it for me guys. It's already coming to do something [ASR uncertain]

[01:29:29–01:29:36] **Speaker (unattributed):** I'm pretty much ready to sleep. I've got a flight at I've got to be at the airport at 5.30 a.m. [ASR uncertain]

[01:29:36–01:29:42] **Speaker (unattributed):** To Hanoi, so I'm not even gonna sleep tonight. Is there anything else anyone wants to discuss before we call it today? [ASR uncertain]

[01:29:42–01:29:55] **Speaker (unattributed):** Nothing for me. I know we had the stuff to cover, but maybe we just try to do that tomorrow or something then [ASR uncertain]

[01:29:55–01:30:00] **Speaker (unattributed):** Sounds good. Yeah. Okay guys. Yeah, so I'm gonna say good night. Thank you [ASR uncertain]

[01:30:00–01:30:03] **Speaker (unattributed):** think about this deeply and I'll

[01:30:03–01:30:06] **Speaker (unattributed):** send a lane by tomorrow end of

[01:30:06–01:30:08] **Speaker (unattributed):** play to get you their high level

[01:30:08–01:30:11] **Speaker (unattributed):** products, categories or some brands

[01:30:11–01:30:12] **Speaker (unattributed):** and what at least don't

[01:30:12–01:30:14] **Speaker (unattributed):** capabilities and features will be in

[01:30:14–01:30:17] **Speaker (unattributed):** each one so you can start putting

[01:30:17–01:30:18] **Speaker (unattributed):** your creative head on.

[01:30:18–01:30:22] **Speaker (unattributed):** Cheers. That sounds good.

[01:30:22–01:30:23] **Speaker (unattributed):** Okay guys, good night.

[01:30:23–01:30:24] **Speaker (unattributed):** Thanks guys.

[01:30:24–01:30:25] **Speaker (unattributed):** Bye.

[01:30:25–01:30:25] **Speaker (unattributed):** Can I?

[01:30:25–01:30:26] **Speaker (unattributed):** Bye.
