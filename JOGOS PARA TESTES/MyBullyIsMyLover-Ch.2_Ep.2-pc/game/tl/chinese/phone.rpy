init python:
    def force_translate_timestamps(s):
        # 确保只在中文语言下生效，避免影响英文原版
        if _preferences.language != "chinese":
            return s
            
        import re
        
        # 使用正则表达式匹配并替换动态时间文本
        # \1 代表捕获的数字
        
        # 匹配 "X year ago" 或 "X years ago" -> "X年前"
        s = re.sub(r'^(\d+) year(?:s?) ago$', r'\1年前', s)
        
        # 匹配 "X month ago" 或 "X months ago" -> "X个月前"
        s = re.sub(r'^(\d+) month(?:s?) ago$', r'\1个月前', s)
        
        # 匹配 "X day ago" 或 "X days ago" -> "X天前"
        s = re.sub(r'^(\d+) day(?:s?) ago$', r'\1天前', s)
        
        # 匹配 "X hour ago" 或 "X hours ago" -> "X小时前"
        s = re.sub(r'^(\d+) hour(?:s?) ago$', r'\1小时前', s)
        
        # 匹配 "X min ago" -> "X分钟前"
        s = re.sub(r'^(\d+) min ago$', r'\1分钟前', s)
        
        return s

    # 将此函数注册到 Ren'Py 的文本替换钩子中
    config.replace_text = force_translate_timestamps

init python:
    # 当语言是中文时，增加预览文本的长度限制
    # 这样可以防止英文原句在翻译前被截断，从而让翻译生效
    # 中文通常比英文短，所以即使显示完整句子通常也不会爆框
    if _preferences.language == "chinese":
        phone_config["preview_max_length"] = 200


translate chinese strings:
    #UI

    old "Messages"
    new "消息"

    old "View full history..."
    new "查看历史记录"

    old "Aine — Full History"
    new "艾妮 - 历史记录"

    old "Freya — Full History"
    new "芙蕾雅 - 历史记录"

    old "Emma — Full History"
    new "艾玛 - 历史记录"

    old "Moon — Full History"
    new "月 - 历史记录"

    old "Gwen — Full History"
    new "格温 - 历史记录"

    old "Shu — Full History"
    new "修 - 历史记录"

    old "June — Full History"
    new "琼 - 历史记录"

    old "Sky — Full History"
    new "斯凯 - 历史记录"

    old "Naomi — Full History"
    new "娜奥米 - 历史记录"

    old "Lily — Full History"
    new "莉莉 - 历史记录"

    old "Klara — Full History"
    new "克拉拉 - 历史记录"

    old "Claire — Full History"
    new "克莱尔 - 历史记录"

    old "Jess — Full History"
    new "婕斯 - 历史记录"

    old "just now"
    new "刚刚"

    old "Empty chat..."
    new "暂无消息……"

    old "[typing_who] is typing"
    new "[typing_who!t]正在输入"
    
    
    
    #AINE

    old "[mc]..."
    new "[mc!t]……"

    old "I know you're trying to distract yourself, but going back to work this soon isn't the way."
    new "我知道你想分散注意力，但这么快就回去工作可不是办法。"

    old "Your body just went through hell. You have to let it catch up before you start pretending you're okay again."
    new "你的身体刚经受过地狱般的折磨。你必须先恢复恢复，再开始假装自己没事。"

    old "Please... give yourself a little room to breathe."
    new "求你……给自己一点休息的时间。"

    old "I'm fine, Aine. Really."
    new "我没事的，艾妮。真的。"

    old "Lying around all day is driving me insane. I need to move before my brain starts eating itself alive."
    new "整天躺着，我都快疯了。我得动起来，免得我的大脑开始自我吞噬。"

    old "Needing something to keep you occupied isn't the same as being okay."
    new "需要有事情做不代表你已经没事了。"

    old "I just... don't want you passing out somewhere I can't reach you."
    new "我只是……不想让你在我触及不到的地方晕倒。"

    old "You scared me once. That's already more than I can handle."
    new "你已经吓过我一次。只那一次就已经不是我能承受的了。"

    old "Alright. Two more days of rest. No arguments."
    new "好吧。再休息两天。不许反驳。"

    old "Still not enough... but I'll take the win while I can."
    new "还是不够……但我就暂且接受这个结果吧。"

    old "Freya just sent me a photo..."
    new "芙蕾雅刚刚给我发了一张照片……"

    old "What? What's going on?"
    new "什么？怎么了？"

    old "Fuck..."
    new "我操……"

    old "She said I wouldn't have the guts to send you something like that."
    new "她说我没胆子给你发那样的照片。"

    old "As if I'm still the prude sister you two love teasing."
    new "说得好像我还是你俩以前总爱调戏的那个爱害羞的姐姐一样。"

    old "Guess I proved her wrong."
    new "看来我已经证明她错了。"

    old "Aine... holy! This is... GOD."
    new "艾妮……我去！这……太棒了。"

    old "Pfft. 😝"
    new "嘻嘻。😝"

    old "Exactly the reaction I pictured."
    new "跟我预料的反应一模一样。"

    old "I came."
    new "我射了。"

    old "Huh?!"
    new "啊？！"

    old "You—"
    new "你——"

    old "[mc]... it hasn't even been a full minute."
    new "[mc!t]……一分钟都没到呢。"

    old "You sent me a photo like {b}that{/b}. What did you expect?"
    new "你可是给我发了{b}那种{/b}照片。你以为我会怎么样？"

    old "Maybe a gasp. A flustered keyboard smash. Not—"
    new "可能就惊讶一下。狠狠拍一下键盘。而不是——"

    old "... that."
    new "……那样。"

    old "Blame yourself for being so fucking hot. Honestly? A public safety hazard."
    new "都怪你太他妈漂亮了。说实话，简直是个公共安全隐患。"

    old "If I'm a hazard, you're hopeless. And I'm not even a little sorry."
    new "如果我是隐患，那你就没救了。而且我一点也不抱歉。"

    old "I love you, though! 😊😘"
    new "不过我爱你！😊😘"

    old "Oh my god—I'm so sorry. I didn't think before I said that. 😭"
    new "我的天啊，真的真的对不起。我说话之前没多想。😭"

    old "Someone was bound to mention him sooner or later."
    new "早晚会有人提到他的。"

    old "Even I'm surprised she kept it in for as long as she did."
    new "就连我也没想到她能坚持那么久。"

    old "Can we talk...? I suddenly feel dizzy. It brought back things I wasn't ready to feel."
    new "我们能聊聊吗……？我突然感觉头晕。我回想起了一些我还没准备好面对的事情。"

    old "Stay where you are. I'm coming."
    new "你就待在原地。我马上来。"

    old "Hey, I was thinking..."
    new "那个，我突然想到……"

    old "Should we... I don't know... have pet names or something?"
    new "我们要不要……就是……互相起个爱称什么的？"

    old "[mc], no."
    new "不要，[mc!t]。"

    old "Pet names never felt real to me."
    new "我从来都不喜欢爱称。"

    old "Anyone can say \"baby\" or \"honey.\" It doesn't make the feeling behind it true."
    new "谁都可以随便说“宝贝”或者“亲爱的”。但不代表爱称背后有真实的感情。"

    old "And to be honest, after everything I put you through back then, I don't feel like I've earned anything beyond your actual name."
    new "而且说实话，就凭我以前对你做过的那些事，我也觉得我只配喊你的真名。"

    old "Labels don't prove love. What I do for you now does."
    new "名字不能证明什么。我现在为你做的事才能代表我对你的爱。"

    old "I wasn't trying to force anything. Just thought maybe you'd want one."
    new "我没想强迫你什么。只是觉得也许你想试试。"

    old "I know. And it's sweet that you asked."
    new "我知道。你能提这事我很高兴。"

    old "But I like your name. It feels honest. Honest hits deeper than cute."
    new "但是我喜欢你的名字。让我觉得踏实。踏实比可爱更有分量。"

    old "And you can keep calling me Aine. That's enough for me."
    new "你也可以继续叫我艾妮。这样对我来说就足够了。"

    old "You really gotta let go of the past, though."
    new "你真的要放下过去了。"

    old "I have. You can, too."
    new "我已经放下了。你也可以的。"

    old "I'm trying. It's just... not that simple."
    new "我在努力。这事儿……没那么简单。"

    old "You do remember I used to pick on you, right?"
    new "你也记得我以前是怎么欺负你的吧？"

    old "Most people wouldn't forgive their childhood tormentor so easily."
    new "大多数人都是不会轻易原谅以前霸凌过自己的人的。"

    old "Yeah, well... I'm not most people."
    new "是啊……但我不是大多数人。"

    old "And you're not that girl anymore."
    new "你也不是以前那个女孩了。"

    old "Maybe."
    new "可能吧。"

    old "But sometimes I look at you and think, \"Do I really deserve this?\""
    new "但有时候我看着你，就会想，“我真的配得上你吗？”"

    old "Oh, trust me. I remember every shove, every glare, every sarcastic hit-and-run."
    new "噢，我跟你说。我记得你每一次推我，每一次瞪我，每一次说完嘲讽我的话就走。"

    old "And now look at you—apologizing every other day. Life's hilarious."
    new "再看看现在的你——动不动就道歉。人生真是搞笑。"

    old "I'm trying to be better, okay?"
    new "我在努力改善了，知道不？"

    old "And for the record, you were impossible to leave alone. You were adorable when you got annoyed."
    new "再说了，当时也不可能放过你。你生气的时候真是太可爱了。"

    old "So bullying me was your love language?"
    new "所以欺负我就是你表达爱意的方式吗？"

    old "... Don't say it like that."
    new "……别这么说。"

    old "It sounds way worse when you make it sound that cute."
    new "你说得这么可爱，反而听起来更糟糕了。"

    old "Too late. I'm keeping it."
    new "太迟了。我会一直这么说下去的。"

    old "Besides, if I didn't forgive you, I wouldn't have the upgraded version of you now."
    new "再说了，如果我没有原谅你，就不会跟现在升级版的你在一起了。"

    old "Upgraded? Really?"
    new "升级？你说什么啊？"

    old "What am I, a software patch?"
    new "我是能更新的软件吗？"

    old "A very sexy one."
    new "非常性感的软件。"

    old "... You're ridiculous."
    new "……你真是没救了。"

    old "But fine. I'll try to stop letting the past hover over us."
    new "不过好吧。我会尽量不让过去的事情影响我们。"

    old "Just don't expect me to stop apologizing overnight."
    new "但也别指望我能立马就不道歉了。"

    old "I know you're probably acting like you forgot, but I didn't."
    new "我知道你可能只是装作自己忘了，但我没忘。"

    old "Happy birthday."
    new "生日快乐。"

    old "I hope today feels a little lighter than the rest. You deserve at least that much."
    new "我希望今天你能感觉轻松一点。这是你应得的。"

    old "You remembered."
    new "你记得啊。"

    old "Yeah. Of course I remembered."
    new "是啊。我当然记得。"

    old "I've always known the date. Don't ask how. My brain just hoards information when it comes to you."
    new "我一直都知道日子。别问我是怎么做到的。有关你的一切我都能记住。"

    old "Anyway... I hope you're doing something for yourself today."
    new "总之……我希望你今天能为自己做点什么。"

    old "Wasn't planning anything special. Haven't really felt like celebrating my birthday lately. Not sure why."
    new "没计划什么特别的事。最近也不太想庆祝生日。不知道为什么。"

    old "That doesn't sound like you."
    new "这不像你会说的话。"

    old "So what are you up to, hm? Trying to squeeze a reaction out of me?"
    new "你在打什么主意呢，嗯？想从我这里得到什么反应吗？"

    old "Do you want someone to spoil you? Tell you you've been a very good boy today?"
    new "你想要有人宠着你吗？告诉你今天你是个乖孩子？"

    old "You really do know me."
    new "你真的很了解我。"

    old "Where are you?"
    new "你在哪里？"

    old "In the supermarket."
    new "在超市。"

    old "On my way."
    new "我马上到。"

    old "Thanks, Aine."
    new "谢谢，艾妮。"

    old "Look who I stole from the supermarket."
    new "看看我在超市碰到了谁。"

    old "You did NOT just send that!"
    new "你还敢发给我！"

    old "My legs are still shaking and you're out here sending photographic evidence?"
    new "我的腿还在发抖，你居然还发这种照片给我？"

    old "Delete it before I spontaneously combust."
    new "赶紧给我删了，不然我随时都可能自燃。"

    old "I look—"
    new "我看着——"

    old "God, I can't even finish that sentence."
    new "天啊，我都没法把这句话说完。"

    old "You look perfect."
    new "你看着完美极了。"

    old "Stop."
    new "别说了。"

    old "I'm already red and you're making it worse."
    new "我已经脸红了，你还在火上浇油。"

    old "You drag me into a hotel and then decide to immortalize the moment... unbelievable."
    new "你把我拉进酒店，然后居然还要拍照……难以置信。"

    old "... But don't you dare send that to anyone else."
    new "……你敢发给别人试试。"

    old "That's for your eyes only."
    new "只能你自己看。"

    old "Also, while we're on the subject."
    new "对了，说到这个。"

    old "A hotel, [mc]? For a {b}few hours{/b}?"
    new "为了那么{b}几个小时{/b}，就要订酒店吗，[mc!t]？"

    old "Do you have any idea how absurd that is?"
    new "你知道这有多荒谬吗？"

    old "It was worth it."
    new "很值啊。"

    old "That's not the point."
    new "这不是重点。"

    old "You dropped that much money just because you felt like dragging me upstairs?"
    new "你只为了把我拉上楼，就花了那么多钱？"

    old "You could've at least *pretended* to compare prices first."
    new "你哪怕先{b}假装{/b}比比价格呢。"

    old "I wasn't really thinking about prices, you know?"
    new "我当时也没考虑价格的事。"

    old "Yeah, I know."
    new "我知道。"

    old "You were thinking with something else entirely."
    new "你完全在想别的事情。"

    old "Still, don't make a habit of this. Please."
    new "总之，拜托不要养成这种习惯。"

    old "You sound like you're lecturing me in the afterglow."
    new "感觉你是在贤者时间里训斥我。"

    old "Because I {b}am{/b}."
    new "因为{b}确实如此{/b}。"

    old "I'm not letting you go broke because you can't control yourself around me."
    new "你在我身边就管不住自己，我不会让你因为这个破产的。"

    old "Really, I don't regret it."
    new "说真的，我不后悔。"

    old "You should at least regret the receipt."
    new "你至少应该对价钱感到后悔。"

    old "I swear... of all the things to splurge on..."
    new "那么多能花钱的地方……偏偏……"

    old "Next time, warn me. I would've booked something cheaper."
    new "下次，先跟我说一声。我会订更便宜的地方。"

    old "You'd really do that?"
    new "真的吗？"

    old "Yes. Because one of us has to think with their actual brain."
    new "是啊。因为至少我们俩的其中一个得用上面的头思考。"

    old "And clearly... it's not going to be you. Aren't you supposed to be saving money for something?"
    new "而显然……那个人不会是你。你不是正在为什么东西存钱吗？"

    old "I keep forgetting how practical you are. Okay—no more reckless spending. Promise."
    new "我总是会忘掉你有多实际。好吧——不再乱花钱了。保证。"

    old "Good."
    new "很好。"

    old "But... we're talking about the moment itself? Yeah. It was worth it. Thank you, [mc]."
    new "但是……单说那一刻的话，没错。很值得。谢谢你，[mc!t]。"

    old "You made me feel really special. And you know how much that means to me."
    new "你让我感觉非常特别。你也知道这对我来说有多重要。"

    old "See? Told you it was worth it."
    new "看吧？我早说了很值。"

    old "Still! I was supposed to give {b}you{/b} something for your birthday."
    new "话是这么说！但本来应该是我给{b}你{/b}准备生日礼物的。"

    old "Not end up being... {b}that{/b}."
    new "结果却变成……{b}那样{/b}。"

    old "You gave me a ride. Or three."
    new "你让我干了个爽。三次。"

    old "Really {b}grinded{/b} out that last one."
    new "最后一次真是绝了。"

    old "Maybe next time we book a flight to Vegas. Really make things extra special."
    new "要不下次我们直接飞到维加斯去。那样会更特别。"

    old "For God's sake! NO!"
    new "我的天啊！不行！"

    old "I'm still recovering from the hotel receipt. Don't you dare escalate."
    new "我还在心疼这次花的钱。你少得寸进尺。"

    old "Are you free later? I need an extra pair of hands."
    new "你待会有空吗？我需要人帮忙。"

    old "Sky ordered equipment again. Heavy ones. She apparently thinks I have the physique of a forklift. HELP. 😫"
    new "斯凯又买设备了。很重。她显然觉得我的力气跟叉车一样大。救命。😫"

    old "So you thought of me."
    new "所以你来找我？"

    old "You're the strongest option available!"
    new "你是力气最大的了！"

    old "And the least likely to complain while doing it..."
    new "也是干活的时候最不爱抱怨的……"

    old "Am I really that convenient?"
    new "我就这么好用吗？"

    old "If the shoe fits."
    new "说得好听点就是这样。"

    old "But... yes. I could really use your help. PRETTY PLEASE? 😭"
    new "不过……嗯。我真的需要你的帮忙。求你了？😭"

    old "Time?"
    new "什么时候？"

    old "Anytime after lunch. Sky will \"supervise,\" which means she'll point at things and sound like a strict principal."
    new "午饭之后就行。斯凯会“监督”我们，意思就是她会跟严厉的校长一样在旁边指指点点。"

    old "So I'm the actual labor and she's management. Got it."
    new "所以我干体力活，她是管理层。明白了。"

    old "Welcome to my daily suffering."
    new "欢迎体验我每天都要遭受的苦难。"

    old "At least you help without making me feel like I owe you my firstborn."
    new "至少你帮忙的时候不会让我觉得我欠你一个孩子。"

    old "What do I get, then?"
    new "那我能得到什么好处？"

    old "My gratitude. Extremely rare, very precious."
    new "我的感激。极其罕见，非常珍贵。"

    old "I'll take it."
    new "好，我答应你。"

    old "Phew! Thank you."
    new "好！谢谢你。"

    old "You sure you just need help lifting things?"
    new "你确定你只是需要帮忙搬东西吗？"

    old "Don't read into it."
    new "别多想。"

    old "... for now."
    new "……之后的事之后再说。"

    old "But I'll see you later!"
    new "我们待会见！"

    old "How was today's shift?"
    new "今天的工作怎么样？"

    old "Damn, Aine. It's 11 PM."
    new "我去，艾妮。都晚上11点了。"

    old "I know. I just... can't sleep for some reason."
    new "我知道。我就是……不知怎么的睡不着。"

    old "So... how was it?"
    new "所以……怎么样呢？"

    old "How was it, huh..."
    new "要说怎么样……"

    old "Long."
    new "很久。"

    old "Loud."
    new "很吵。"

    old "And my feet hate me."
    new "而且我的脚疼死了。"

    old "You say that every week..."
    new "你每星期都这么说……"

    old "Try resting instead of pretending you're made of steel."
    new "休息休息吧，别再假装自己是铁打的。"

    old "Here you go with the nagging again."
    new "你又开始唠叨了。"

    old "Just checking on you."
    new "只是关心你一下。"

    old "I can stop caring if you want me to."
    new "你不愿意的话，我可以不管你。"

    old "Didn't say that."
    new "我没那个意思。"

    old "Customers were extra fun today."
    new "今天的客人特别有意思。"

    old "Had a guy argue with me about the size of his drink for ten minutes."
    new "有个男的非说他的饮料上错了，跟我吵了十分钟。"

    old "Let me guess... Freya stepped in and actually fought with him?"
    new "我猜猜……最后芙蕾雅也掺和进来，真的跟他骂起来了？"

    old "How did you know that?"
    new "你怎么知道？"

    old "I don't know. Maybe because we crawled out of the same hole? 😑"
    new "我也不好说。可能因为我们俩是从同一个洞里爬出来的？😑"

    old "LMAO! 🤣"
    new "哈哈哈哈！🤣"

    old "We both have the fighting spirit. She just swings it faster."
    new "我们都有战斗精神。只是她显露得更快。"

    old "Yeah, I've noticed."
    new "嗯，我发现了。"

    old "How's the online teaching thing going? You haven't talked about it lately."
    new "你的线上教学又怎么样了？你最近都没提过。"

    old "The kids were out for blood today."
    new "今天的孩子们个个都想翻天。"

    old "Rough class?"
    new "很难办？"

    old "One of them learned how to screen-share memes."
    new "其中有一个学会了分享屏幕。"

    old "In the middle of reading time."
    new "于是就在阅读时间开始放烂梗。"

    old "Fifteen tiny faces laughing at a dancing potato."
    new "十五张小脸蛋对着一个跳舞的土豆开始笑。"

    old "And what did you do?"
    new "那你怎么办了？"

    old "Pretended I wasn't dying inside."
    new "尽量没有气晕过去。"

    old "Then bribed them with stickers so they'd behave."
    new "然后用贴纸贿赂他们，让他们乖一点。"

    old "Sounds like you. Cold exterior, marshmallow core."
    new "确实像你。外表高冷，内心像棉花糖。"

    old "Don't start."
    new "得了吧。"

    old "I'm only a marshmallow for one person, and he knows who he is."
    new "我只会对一个人像棉花糖，是谁他自己心里清楚。"

    old "If he's smart, he won't take that for granted."
    new "他要是够聪明，就不会把这当成理所当然。"

    old "Good thing he's smarter than he looks. 😘"
    new "还好他其实也没那么笨。😘"

    old "Wanna hang out by the pool? I've got beer in the fridge. Might help you sleep."
    new "要去泳池玩吗？冰箱里有啤酒。说不定喝了就想睡了。"

    old "Yeah, sure!"
    new "好啊，当然！"

    old "I'll be waiting there."
    new "我在那等你。"

    old "Give me a minute. Need to put on PJs."
    new "等我一下。先换上睡衣。"

    old "I'm only in panties right now, and I'm not walking out like that."
    new "我现在只穿了内裤，没法出门。"

    old "No, don't!"
    new "别换衣服！"

    old "... Of course that's your first reaction."
    new "……就知道你会是这种反应。"

    old "You can't just drop \"only in panties\" and expect me to behave."
    new "你都说“只穿内裤”了，还指望我能淡定？"

    old "Too bad. I'm choosing warmth and dignity."
    new "可惜。我选择温暖和尊严。"

    old "Killjoy..."
    new "没劲……"

    old "Good night, [mc]. Thanks for the company."
    new "晚安，[mc!t]。谢谢你陪我。"

    old "And... I love you. Just in case I didn't say it enough."
    new "还有……我爱你。我怎么说都说不够。"

    old "I love you too, Aine. Sleep well."
    new "我也爱你，艾妮。睡个好觉。"

    old "You said you had something important to tell me?"
    new "你说你有重要的事要跟我说？"

    old "Yeah. I finally made a decision about the group."
    new "嗯。组织的事，我终于下定决心了。"

    old "Really? You're sure you're not rushing this? Because that sounds... big."
    new "真的吗？你不是一时冲动吧？这……可是大事。"

    old "Yeah. I've made up my mind. We're not running it like a mafia anymore."
    new "嗯。我打定主意了。不能再像黑手党那样运营了。"

    old "We're turning everything into a charity foundation. Just like Hera wanted."
    new "我们要把组织转变成慈善基金会。走赫拉想走的路线。"

    old "You're serious?"
    new "你认真的？"

    old "I wouldn't have said it if I wasn't."
    new "如果不认真就不会跟你说了。"

    old "As strange as it is to say... she'd be proud of you."
    new "虽然这么说很奇怪……但她会为你感到骄傲的。"

    old "More than you think."
    new "远比你想象的还要骄傲。"

    old "You think so?"
    new "是吗？"

    old "I know so."
    new "我很确定。"

    old "Mother wanted to build something good. Something that gave back."
    new "妈妈想建立一个好的组织。一个能回馈社会的组织。"

    old "And you're choosing to finish what she started."
    new "而你选择去完成她未竟的事业。"

    old "Feels strange."
    new "感觉挺奇怪。"

    old "Like I'm rewriting something that was meant to stay dark."
    new "好像我在重写一些本该永远留在黑暗里的东西。"

    old "Dark doesn't have to stay dark."
    new "黑暗没必要永远是黑暗。"

    old "The moment someone refuses to let it swallow them, it changes."
    new "当有人拒绝被黑暗吞噬的时候，黑暗就会改变。"

    old "That's what you're doing."
    new "这就是你正在做的事。"

    old "I'm trying. I just... don't feel like I should be leading this organization at all."
    new "我尽力了。我只是……不认为该由我领导这个组织。"

    old "Trying is enough."
    new "尽力就够了。"

    old "And you're not doing it alone. You have me."
    new "而且不是只有你一个人在做这件事。我会陪着你。"

    old "Also..."
    new "还有……"

    old "I'm genuinely glad it's you stepping up."
    new "由你来承担这个责任，我真的很高兴。"

    old "Because we both know I have no idea what to do with that kind of power."
    new "因为你我都知道，我根本不知道该怎么处理那种权力。"

    old "So if you're feeling lost... remember I'm right there with you."
    new "所以如果你感到迷茫……记住我会一直陪着你。"

    old "Good. Hearing that makes it feel a little less heavy."
    new "好的。听你这么说，我感觉轻松了一点。"

    old "We should talk about this in person. Not through a screen."
    new "我们应该面对面聊这事。而不是隔着一个屏幕。"

    old "If you're not too tired later... meet me by the pool?"
    new "如果你之后不太累的话……去泳池见我？"

    old "I'll bring the beer."
    new "我带上啤酒。"

    old "Sounds good."
    new "听起来不错。"

    old "Then I'll see you later."
    new "那我们待会见。"

    old "[mc], where are you?"
    new "[mc!t]，你在哪里？"

    old "Shit! Sorry, my shift schedule got moved again."
    new "操！抱歉，我又换班了。"

    old "I see. It's okay."
    new "我知道了。没关系。"

    old "So I went through the documents Hera left behind."
    new "我看了看赫拉留下的文件。"

    old "There's a lot more to this whole \"charity reform\" than we thought."
    new "这个“慈善改革”比我们想象的要复杂得多。"

    old "Yeah? What's the damage?"
    new "是吗？怎么说？"

    old "First: we have to dissolve the shell companies. All of them."
    new "首先：我们必须解散所有的空壳公司。一个不留。"

    old "Then re-register the entire organization as a legal foundation."
    new "然后把整个组织重新注册为合法的基金会。"

    old "And don't even get me started on the tax documentation."
    new "跟税务相关的文件就更别提了。"

    old "Sounds fun."
    new "感觉很有意思。"

    old "Don't joke. This is serious."
    new "别开玩笑了。这是正事。"

    old "We can't build a charity with questionable money floating around."
    new "我们不能用来路不明的钱来建立慈善机构。"

    old "Relax. I'm calling Sicae Agency to help us handle the paperwork."
    new "放心。我会找西卡的人帮我们处理文件的。"

    old "... Already?"
    new "……这就找上他们了？"

    old "You didn't even ask me first."
    new "你都不先问问我吗？"

    old "I thought you'd want things done fast."
    new "我想着你会想快点办妥这事。"

    old "Yes, but I also want to know who's sticking their hands into our documents."
    new "没错，但我也想知道谁会动我们的文件。"

    old "What if they mess something up?"
    new "万一他们搞砸了呢？"

    old "They won't. Sicae handles corporate conversions all the time."
    new "不会的。西卡经常处理公司转型的事。"

    old "They can manage everything, and I trust them."
    new "他们能处理好一切，我相信他们。"

    old "Tch. That makes one of us."
    new "切。我可不会。"

    old "You're not a fan of them?"
    new "你不喜欢他们？"

    old "It's not that I dislike them. I just need them {b}not{/b} to screw us over."
    new "不是我不喜欢他们。我只是不允许他们把我们的事搞砸。"

    old "You're so dramatic."
    new "你太夸张了。"

    old "I'm being realistic here!"
    new "我只是在说实话！"

    old "You're the one who thinks every problem can be fixed with charm and one deep breath."
    new "是你觉得每个问题都能用魅力和深呼吸解决的。"

    old "It works most of the time."
    new "大部分时候都可以啊。"

    old "Not with the government, it doesn't."
    new "对政府可不管用。"

    old "Okay, okay. How about this..."
    new "好吧，好吧。那要不这样……"

    old "You handle reviewing the legitimacy reports, and I'll let Sicae deal with the dirty history."
    new "你负责审核合法的报告，我让西卡处理黑历史。"

    old "... So I get the boring parts?"
    new "……所以我负责无聊的部分？"

    old "You get the parts you're better at."
    new "你负责你更擅长的部分。"

    old "Hmph."
    new "哼。"

    old "Fine."
    new "好吧。"

    old "But if your agency screws up even one line, I'm blaming you personally."
    new "但假如你找的人弄错了哪怕一行字，我会亲自找你算账。"

    old "Noted. I'll take the hit like a man."
    new "记住了。我会像个男人一样承担责任的。"

    old "Good to know."
    new "那就好。"

    old "Because despite all this arguing... I'm excited."
    new "因为尽管我们吵了这么多……我还是很兴奋。"

    old "We're actually doing it, [mc]."
    new "我们真的要开始了，[mc!t]。"

    old "Yeah. We are."
    new "是啊。我们要开始了。"

    old "Let's talk more later, alright?"
    new "我们之后再聊，好吗？"

    old "Then as long as you trust them."
    new "只要你相信他们就行。"

    old "[mc]. You up?"
    new "[mc!t]。起床了吗？"

    old "Yeah. What's going on?"
    new "起了。怎么了？"

    old "We actually did it."
    new "我们真的办成了。"

    old "The papers went through. The foundation is officially recognized."
    new "文件都搞定了。基金会正式成立了。"

    old "I'm... still processing."
    new "我……还在消化这个消息。"

    old "No more mafia. Just a charity now."
    new "不再是黑手党了。现在只是一个慈善机构。"

    old "Feels surreal."
    new "感觉太不真实了。"

    old "Surreal is one word."
    new "不真实算是一种说法。"

    old "Terrifying works too."
    new "说是可怕也行。"

    old "But mostly... good. Really good."
    new "但更多的是……好。真的很好。"

    old "You wanna celebrate?"
    new "你想庆祝吗？"

    old "By the pool?"
    new "去游泳池？"

    old "With beer?"
    new "带上啤酒？"

    old "Obviously."
    new "当然。"

    old "Alright. Give me five minutes."
    new "好。等我五分钟。"

    old "Okay. I'm here."
    new "好了。我到了。"

    old "The water looks cleaner than usual. Weird."
    new "水看起来比平时干净。奇怪。"

    old "I cleaned it. Already anticipated this."
    new "我清理过了。早就想到了这一点。"

    old "I was basically standing next to a huge steaming bowl of foreshadowing."
    new "实际上真不知道有谁会想不到。"

    old "LOL! 😂"
    new "哈哈！😂"

    old "I... didn't think we'd get this far."
    new "我……没想到我们会走到这一步。"

    old "Part of me kept waiting for something to fall apart."
    new "我心里多少有一部分一直在等着事情崩溃的那一天。"

    old "But it didn't, right?"
    new "但并没有那样，对吧？"

    old "That's because you did good, Aine."
    new "那是因为你做得很好，艾妮。"

    old "Stop..."
    new "别这样……"

    old "You're going to make me weirdly emotional."
    new "会让我莫名其妙想哭的。"

    old "Come on, it's a big night. You're allowed."
    new "没事，今晚很重要。允许你了。"

    old "It still feels strange hearing praise from you. The headpats and everything."
    new "听你夸我还是感觉很奇怪。还有你摸我头之类的。"

    old "I'm used to being the one scolding you about money, and pretty much... everything."
    new "我已经习惯因为钱的事……还有其他各种各样的事训斥你了。"

    old "We can switch roles tonight if you want."
    new "你愿意的话，我们今晚交换一下角色。"

    old "Ha. Sure."
    new "哈。好啊。"

    old "You couldn't scold me if your life depended on it."
    new "哪怕世界末日，你也不会训我的。"

    old "Maybe I just like it when you're soft."
    new "也许我就是喜欢你柔软的一面。"

    old "And I like those {b}soft{/b} parts of yours. Especially the one that gets wet when you hear my voice."
    new "而且我还喜欢你那些{b}柔软{/b}的地方。尤其是听到我声音时会变湿的那个地方。"

    old "Don't... I'm already holding a beer."
    new "别这样……我手里还拿着啤酒呢。"

    old "That doesn't sound like you're telling me to stop."
    new "这怎么听也不像是想让我停下来的意思。"

    old "You're impossible..."
    new "你真是无可救药……"

    old "Well? I'm waiting."
    new "来吧？我等着呢。"

    old "And so goddamn ready..."
    new "更是早就准备好了……"

    old "I can hear that sultry voice from up here."
    new "我在这都能听见你那性感的声音。"

    old "{b}\"1 Night in Aine\"{/b}"
    new "{b}“艾妮一夜”{/b}"

    old "Oh my god... I look so..."
    new "我的天……我看着也太……"

    old "You look so...?"
    new "你看着也太……？"

    old "Horny and... needy..."
    new "色情……又……饥渴……"

    old "Like I wasn't thinking straight. As if I didn't care if anyone else sees us."
    new "就好像我脑子已经不正常了。好像我根本不在乎被其他人看到。"

    old "Not sure if it's the alcohol, but I didn't know I could look that open."
    new "不知道是不是因为喝了酒，但是我真没想到我也能有那么放荡的样子。"

    old "Look at you. My daring little show-off."
    new "瞧瞧你。大胆露出狂。"

    old "[mc]! I'm actually liking this, and I'm sober! What have you done to me?!"
    new "[mc!t]！我很清醒，却开始喜欢这样了！你都对我做了什么？！"

    old "I don't know. You were the one so eager to do it outside. I was just enjoying the adventure."
    new "我不知道。是你急着想在外面做的。我只是享受一下冒险的感觉。"

    old "But glad to know you can finally articulate what you feel. I'm so proud of you."
    new "不过很高兴你终于能说出自己的感受了。我为你感到骄傲。"

    old "Uhm... Can I save these?"
    new "呃……我能存下这些照片吗？"

    old "Yes, I know, I know! Not for research purposes!"
    new "我知道，我知道！不是为了研究用途！"

    old "All yours, my lady."
    new "都随你，小姐。"

    old "Emma seemed tired today. You too."
    new "今天艾玛看着很疲惫。你也是。"

    old "Long week."
    new "这周事情很多。"

    old "What have you two been up to?"
    new "你们俩干什么去了？"

    old "Well... kind of a long story."
    new "呃……说来话长。"

    old "She asked for some help."
    new "她找我帮忙。"

    old "Help with what?"
    new "帮什么忙？"

    old "She's got a new case. Complicated one."
    new "她有了个新案子。挺复杂。"

    old "I offered Sicae's hand to lighten the load."
    new "我请了西卡的人帮忙。"

    old "They know what they're doing."
    new "他们是行家。"

    old "If Sicae's involved, I'm not worried."
    new "既然有西卡出手，我就不担心了。"

    old "Glad to know you trust them now."
    new "你现在信任他们了，挺好。"

    old "Guess who just got scolded."
    new "猜猜谁又挨骂了。"

    old "What did you do this time?"
    new "你这次干嘛了？"

    old "Apparently I \"overshared\" her case with you."
    new "说是我跟你“透露”了她的案子。"

    old "Which is funny, because I didn't even tell you anything."
    new "还挺搞笑的，我根本什么都没跟你说啊。"

    old "... Oh no."
    new "……天呐。"

    old "Emma scolded you?"
    new "艾玛说你了？"

    old "Yes."
    new "是啊。"

    old "Yes she did."
    new "我被她骂了。"

    old "Pffft!"
    new "哈哈哈哈！"

    old "Sorry. I shouldn't laugh."
    new "抱歉。我不该笑的。"

    old "But I'm absolutely laughing. LOL! 🤣"
    new "但我真是笑疯了。哈哈！🤣"

    old "Wow. Thanks for the emotional support."
    new "哇。真是谢谢你的安慰。"

    old "Hey, I get it. Emma's terrifying when she goes serious."
    new "我明白。艾玛一旦严肃起来就很可怕。"

    old "But watching her scold you for something you didn't even do? That's comedy gold."
    new "不过看她因为你根本没做的事说你……真是顶级喜剧。"

    old "Do we entertain you? 😒"
    new "我们让艾妮大人好好笑了一把？😒"

    old "Maybe...?"
    new "可能吧……？"

    old "But if it makes you feel better..."
    new "不知道我这么说你能不能好受点……"

    old "I already forgot half of what you told me anyway."
    new "反正你跟我说的话，我已经忘了一半了。"

    old "That somehow makes it worse."
    new "我反而更难受了。"

    old "Hey, [mc]? You there?"
    new "[mc!t]？你在吗？"

    old "Yeah?"
    new "怎么了？"

    old "You know... I've been thinking."
    new "那个……我一直在想。"

    old "Uh-huh?"
    new "想什么？"

    old "Or more like... looking."
    new "或者说……在看。"

    old "Aine... if you're this flustered, I know it's something sex-adjacent."
    new "艾妮……你要是害羞成这样，那我就知道是跟那方面有关的了。"

    old "Just say it."
    new "你说吧。"

    old "I'm looking at the photos you sent me and..."
    new "我在看你给我发的照片，然后……"

    old "And...?"
    new "然后……？"

    old "[mc], I want more..."
    new "[mc!t]，我还想要更多……"

    old "Not \"kinda\" more? Not \"maybe\" more?"
    new "不是“有点”想要更多？不是“可能”想要更多？"

    old "You mean you {b}definitely{/b} want more? More sex?"
    new "你是说你{b}绝对{/b}想要更多？更多做爱？"

    old "No, not just the sex itself..."
    new "不，不止是做爱本身……"

    old "I want you to look at me more."
    new "我想让你多看看我。"

    old "HOLY SHIET!"
    new "我了个操！"

    old "You like that...? 🫣"
    new "你喜欢吗……？🫣"

    old "Do you even have to ask?"
    new "还用问吗？"

    old "Remember the first photo I sent you months ago?"
    new "还记得我前几个月发给你的第一张照片吗？"

    old "And you said you..."
    new "你当时还说你……"

    old "Let's just say I didn't exactly look at it once and move on."
    new "可以说那张照片我并没有只看了一次就算了。"

    old "Haha!"
    new "哈哈！"

    old "Yeah... that felt good to hear. REALLY good."
    new "是啊……听你这么说感觉真好。真的很好。"

    old "If you want to do this more often from now on, I am {b}absolutely{/b} not complaining."
    new "如果你以后想多发的话，我{b}绝对{/b}不会抱怨的。"

    old "Not even a little. NO, MA'AM."
    new "一丁点都不会有。绝对不会，小姐。"

    old "So... is that a yes?"
    new "所以……你同意了？"

    old "YES. Hell yes."
    new "同意。肯定同意。"

    old "Phew... oh my god. That took a lot out of me."
    new "太好了……天啊。我鼓起了好大的勇气。"

    old "You did great, you know."
    new "你做得很棒。"

    old "Actually saying what you want? I love that."
    new "把自己想要的东西大胆说出来，我喜欢你这样。"

    old "Please don't make me shy now..."
    new "你别让我害羞了……"

    old "But... thank you for liking my newfound... glory. 😋"
    new "不过……谢谢你喜欢我新发现的……爱好。😋"

    old "LMAO. Always liked that band."
    new "哈哈。我希望你再多发现点。"

    old "On my way home."
    new "在回家的路上。"

    old "Also... I took something for you."
    new "而且……给你拍了点东西。"

    old "HOOOOOOOOO! God bless boobs!"
    new "嚯噢噢噢噢！上帝保佑奶子！"

    old "I should've known the moment you said \"something for you.\""
    new "你说“拍了点东西”的时候我就该想到的。"

    old "You surprised?"
    new "算是个惊喜？"

    old "Not really. I always knew you had it in you."
    new "算不上吧。我一直都知道你能做到的。"

    old "Just trying to figure out when exactly my fiancée turned into a public menace."
    new "只是想搞明白我的未婚妻什么时候变成了露出狂的。"

    old "You like it, though?"
    new "你喜欢吗？"

    old "Yeah, and that's the problem."
    new "喜欢，而这就是问题所在。"

    old "You drop stuff like this and expect my brain to function normally. 😵‍💫"
    new "你给我发这种东西，还期望我的大脑能正常运行。"

    old "It's motivating me, at least. 😊"
    new "至少给了我动力。😊"

    old "Just be careful. I love the adventure, but I swear, if someone else even touches... 😤"
    new "不过要小心。我喜欢冒险，但我发誓，如果有别人哪怕碰你一下……😤"

    old "Relax. I'm being careful."
    new "放心。我很小心的。"

    old "No one even saw anything. I checked. Promise."
    new "根本都没人看见。我特地确认过了。我保证。"

    old "I'm just for you."
    new "我只是你一个人的。"

    old "You know exactly how to make my day. Or night..."
    new "你很懂怎么让我开心起来。白天也好，晚上也好……"

    old "I'm getting off in a few stops."
    new "我再过几站就下车了。"

    old "Try not to melt before I get there."
    new "可别在我回来之前就融化掉。"

    old "I... might've taken another one today. Or two."
    new "我……今天又拍了一张。其实是两张。"

    old "You should probably be somewhere private before opening it."
    new "最好到没人的地方再打开。"

    old "Aine, what am I supposed to do with myself after seeing this?"
    new "艾妮，你说我看到这种照片之后该干什么呢？"

    old "Uhh... appreciate it quietly? Tell me it turns you on?"
    new "呃……静静欣赏？告诉我你很兴奋？"

    old "Quietly is not happening. I want to lick every drop off you. 😜"
    new "静静是不可能的。我想把你那里的每一滴水都舔干净。😜"

    old "You look unreal. And very aware of what you're doing to me."
    new "你太美了。而且很清楚我会有什么反应。"

    old "Good. Then the lighting wasn't a waste."
    new "很好。算是我没有白准备打光。"

    old "Lighting? You planned this?"
    new "打光？你还做了准备？"

    old "Hey, I'm not half-assing our tradition."
    new "我可不会敷衍我们的传统。"

    old "If I'm sending you something, it should be worth the heart attack."
    new "如果我要给你发东西，那一定要让你心跳加速。"

    old "Mission accomplished. I'm still processing."
    new "那你的任务完成了。我还在消化中。"

    old "... You okay?"
    new "……你没事吧？"

    old "Don't worry about me. Just wiped my phone. Got wet."
    new "不用担心我。刚刚擦了擦手机。给弄湿了。"

    old "Got wet with WHAT?!"
    new "被什么弄湿了？！"

    old "[mc]."
    new "[mc!t]。"

    old "We need to talk."
    new "我们得谈谈。"

    old "Yeah. I felt the storm coming."
    new "嗯。我料到你会生气了。"

    old "You went ahead with the expansion plan without me."
    new "你没有跟我商量就推进了扩张计划。"

    old "AGAIN!"
    new "第二次了！"

    old "It wasn't a power move. We needed to act, Aine."
    new "我没想搞权力博弈之类的。只是我们需要做出行动，艾妮。"

    old "Bullshit!"
    new "放屁！"

    old "Fast is fine. But I'm NOT an afterthought, [mc]!"
    new "速度快是好事。但你不能做完之后才想到我，[mc!t]！"

    old "We're supposed to be leading this together!"
    new "我们应该一起领导这个组织才对！"

    old "We've been stuck for weeks because we can't agree on anything!"
    new "我们没法达成一致意见，已经卡住好几个星期了！"

    old "I made a call to keep things moving. That's it."
    new "我只是决定让事情动起来。仅此而已。"

    old "No. You made {b}your{/b} call and decided to skip the part where I exist!"
    new "不对。你做了{b}你{/b}的决定，而完全忽略了我的存在！"

    old "You can't run a charity like that! And you sure as hell can't run {b}me{/b} like that!"
    new "慈善怎么能这么运营呢？而且你也绝对不能这么指挥{b}我{/b}！"

    old "What the hell, Aine? I'm not \"running\" you!"
    new "你胡说什么啊，艾妮？我哪有“指挥”你！"

    old "How the hell am I supposed to keep this thing alive if you shoot down everything I suggest?"
    new "我的每个提议你都否决，那我还怎么让组织活下去呢？"

    old "I shoot them down because half of them are reckless! Why can't you see that?!"
    new "我否决是因为有一半的提议都极其鲁莽！你为什么就看不出来呢？！"

    old "But sure, blame me for being the one thinking past tomorrow."
    new "但行吧，怪我总是想着长远的事。"

    old "Oh, right. Because you're the only one with a brain, is that it?"
    new "可太对了。因为只有你有脑子，对不对？"

    old "I didn't say that!"
    new "我没那个意思！"

    old "But if that's how you want to twist it—fine. I'm done trying."
    new "但要是你想这么曲解我的话——行吧。我不管了。"

    old "Wow. Just... wow."
    new "哇。真是……哇。"

    old "For someone who keeps saying we're partners, you talk like you don't trust me at all."
    new "你嘴上总说我们是搭档，可你刚刚说的话里对我没有一点信任。"

    old "Because you're making it really hard to!"
    new "因为你真的让我很难信任你！"

    old "You keep making decisions behind my back and then... what? I'm supposed to nod and applaud?"
    new "你总是背着我做决定，然后……我还得点头称赞你？"

    old "So what do you want from me, Aine?"
    new "那你到底想让我怎么样，艾妮？"

    old "Tell me what I'm supposed to do so you'll finally stop acting like I'm shutting you out!"
    new "跟我说我该怎么做，然后赶紧别再装得像是我故意排挤你一样了！"

    old "Aine! Where are you?! Pick up your damn phone!"
    new "艾妮！你在哪？！接电话啊！"

    old "AINE!"
    new "艾妮！"

    old "LEAVE ME ALONE!"
    new "少烦我！"

    old "Where are you?!"
    new "你在哪？！"

    old "I said..."
    new "我说了……"

    old "LEAVE."
    new "少。"

    old "ME."
    new "烦。"

    old "ALONE!"
    new "我！"

    old "No. I'm not backing off until you tell me where you are."
    new "不行。你不告诉我你在哪，我是不会罢休的。"

    old "... You know where I am."
    new "……你知道我在哪。"

    old "You just don't see me anymore."
    new "你只是眼里已经没有我了。"

    old "Somewhere along the way, you forgot everything we had..."
    new "在某个时候，你忘记了我们曾经拥有的一切……"

    old "You stopped looking at me... and it hurts."
    new "你不再看我了……真的好难受。"

    old "There you are."
    new "找到你了。"

    old "I CAN'T with you!"
    new "我受不了你了！"

    old "I still hate you! 😡"
    new "我还是恨你！😡"

    old "You didn't sound like that the other night."
    new "你那天晚上可不是这么说的。"

    old "Stop bringing that up... I'm still sore all over."
    new "别提了……我还是浑身酸痛。"

    old "Surely you're not complaining about not being able to walk straight or sit like a normal person? Should I have been gentler? 🤨"
    new "你不会是在抱怨自己路也走不了，坐也坐不成吧？我是不是该温柔点？🤨"

    old "Ugh, have I told you I hate you?"
    new "唉，我有没有跟你说过我很烦你？"

    old "But... no, don't you dare. 😈"
    new "但是……不行，不准温柔。😈"

    old "Roses? All I see is an axilla that smells sweeter than any flower."
    new "玫瑰花？我只看到了比任何花都香的腋下。"

    old "I could bury my nose there and lick you all day..."
    new "我想把鼻子埋在那里，舔你一整天……"

    old "[mc]... what is wrong with you? I'm so offended."
    new "[mc!t]……你犯什么病？我感到极大的冒犯。"

    old "All day? Why not all week? 😘"
    new "一整天？为什么不是一整个星期呢？😘"

    old "Noted for next time..."
    new "记下了，下次我会说的……"

    old "...You really are impossible, you know that? 😌"
    new "……你真是无可救药，你知不知道？😌"

    old "God, they smell sooooo good, [mc]."
    new "天啊，太~~~香啦，[mc!t]。"

    old "Thank you. 🥰"
    new "谢谢你。🥰"

    old "This means we're good, right?"
    new "这就代表我们和好了，对不对？"

    old "It means I'm willing to talk without screaming."
    new "这代表我愿意不大喊大叫地跟你说话。"

    old "I love you. 😘"
    new "我爱你。😘"

    old "I love you too, Aine."
    new "我也爱你，艾妮。"

    old "Now go get some sleep."
    new "快去睡觉吧。"

    old "YOU get some sleep. 😁"
    new "你也去睡觉。😁"

    old "[mc]?"
    new "[mc!t]？"

    old "Just left the office. The volunteers wouldn't let me go unless I promised I'd eat something."
    new "我刚离开办公室。我要是不吃点东西，志愿者们都不让我走。"

    old "Did you?"
    new "你吃了吗？"

    old "Half a sandwich. I don't really feel like eating."
    new "吃了半个三明治。我其实不太想吃东西。"

    old "Aine..."
    new "艾妮……"

    old "Anyway... are you set for later?"
    new "总之……你准备好了吗？"

    old "The food drive, I mean."
    new "食物募捐的事。"

    old "Almost. Still waiting on the delivery from the shelter."
    new "差不多了。还在等庇护所那边送来的货。"

    old "God... I just want today to go right. Please let it go right."
    new "天啊……我只希望今天一切顺利。拜托让一切顺利吧。"

    old "Feels like we need a win after last month's disasters."
    new "上个月太糟糕了，我们现在真的需要把事办成一次。"

    old "Oh, trust me, we will. If there's anything I know about you, it's that your hard work always pays off."
    new "相信我，我们一定行的。我对你最了解的就是，你的努力总会有回报的。"

    old "We're still learning, but this time? I'm sure it's a success."
    new "我们还在学习，不过这次，一定会成功的。"

    old "Pep-talking me?"
    new "这是给我加油打气吗？"

    old "1% pep talk, 99% truth."
    new "1%的加油打气，99%的事实。"

    old "Want me to pick you up? The delivery just arrived."
    new "需要我去接你吗？货刚到了。"

    old "Oh, good idea!"
    new "噢，好主意！"

    old "Well, well, well... someone went commando today?"
    new "瞧瞧瞧瞧……某人今天没穿内裤啊？"

    old "Cumming!"
    new "在撸上了！"

    old "*Coming."
    new "*路"

    old "Pfft! Food drive first! 🤪"
    new "得了！先搞好食物募捐！🤪"

    old "Yes, ma'am!"
    new "收到，小姐！"

    old "Can I ask you something personal?"
    new "能跟你说件私事吗？"

    old "It's not like you to ask permission from me... What's this about?"
    new "你可很少会向我请求许可……怎么了？"

    old "It's about Hera."
    new "是赫拉的事。"

    old "Alright. What about her?"
    new "好吧。她怎么了？"

    old "Do you ever plan on looking for her?"
    new "你有打算去找她吗？"

    old "We've turned the whole organization around. She'd want to know that, right?"
    new "我们改造了整个组织。她会想知道这些的，对吧？"

    old "I've thought about it."
    new "我考虑过。"

    old "Then why haven't you?"
    new "那为什么没有去呢？"

    old "Because I don't know if she wants to be found."
    new "因为我不知道她想不想被找到。"

    old "She left before everything with you happened."
    new "她在你那些事发生之前就走了。"

    old "And she didn't leave a trace. Not a single one."
    new "而且她没有留下任何痕迹。一点都没有。"

    old "It's been months."
    new "都好几个月了。"

    old "Exactly."
    new "没错。"

    old "If she wanted to come back, she would've by now."
    new "如果她真想回来，早就已经回来了。"

    old "You don't sound angry. Kinda surprised."
    new "你听起来并不生气。我有点惊讶。"

    old "I'm not."
    new "我没有生气。"

    old "I'm just tired of expecting things from her."
    new "我只是厌倦了对她抱有期待。"

    old "Aine."
    new "艾妮。"

    old "Anyway."
    new "总之。"

    old "We've done a lot without her."
    new "我们没有她也做了很多事。"

    old "We cleared the assets. Cut off the old connections. Rebuilt the structure from the ground up."
    new "我们清理了资产。切断了旧的关系。从头开始重建了组织结构。"

    old "We've opened three community programs already—kids, food distribution, and legal assistance."
    new "我们已经开设了三个社区项目——儿童救济、食物分发和法律援助。"

    old "And every time something works, I think, \"She would've liked this.\""
    new "每次有成效的时候，我都会想，“她会喜欢这个的。”"

    old "Deep inside, I want her to be proud of me."
    new "在内心深处，我希望她为我感到骄傲。"

    old "But I'm stuck between wanting that and actually chasing her down."
    new "但我就卡在渴望认可和真正去找她之间。"

    old "What if I find her and she doesn't want any of this?"
    new "万一我找到她之后，发现她根本不想要这些怎么办？"

    old "What if she feels free... and I ruin it?"
    new "如果她觉得自由了……而我却毁了一切呢？"

    old "Let me tell you something..."
    new "那我也跟你说一个可能性吧……"

    old "What if she misses you just as much?"
    new "万一她也一样想你呢？"

    old "... She never misses me. And probably never will."
    new "……她从来没想过我。可能也永远不会想我。"

    old "That's a hard truth she hammered into me growing up."
    new "这是在我长大的过程中，她用最残忍的方式让我明白的。"

    old "But... thank you for asking."
    new "不过……谢谢你问我这些。"

    old "For what it's worth... I think she'd be proud of you too."
    new "至少……我觉得她也会为你感到骄傲的。"

    old "I'll pretend I didn't read that."
    new "我就假装我没看见这句话吧。"

    old "Good night, [mc]."
    new "晚安，[mc!t]。"

    old "In my room. Why?"
    new "在我房间里。怎么了？"

    old "I'm coming over."
    new "我现在过去。"

    old "For what?"
    new "来干嘛？"

    old "To make sure you're not crying alone."
    new "看你有没有一个人偷偷哭。"

    old "[mc], I updated the soft copies. Check the last page before you head out."
    new "[mc!t]，我更新了电子版。你出发前看看最后一页。"

    old "On it."
    new "明白。"

    old "Also... did you eat anything yet? You sounded awful this morning."
    new "还有……你吃东西了吗？你今天早上听起来很糟糕。"

    old "Your fever won't drop if you keep skipping meals."
    new "你要是一直不吃饭，发烧是不会好的。"

    old "Stop, stop, stop."
    new "停停停。"

    old "I'm not dying, okay?"
    new "我又不是要死了，好吗？"

    old "I'll eat. I'll rest. Just don't give me another dissertation on nutrition."
    new "我会吃饭的。我会休息的。不要再给我发营养学的论文了。"

    old "I did {b}not{/b} write a dissertation... 😒"
    new "我{b}没有{/b}写什么论文……😒"

    old "You were halfway through Chapter 2, I just can't prove it... 🙄"
    new "你已经写到第二章一半了，我只是没法证明而已……🙄"

    old "Anyway... you take care. 😘"
    new "总之……你保重。😘"

    old "YOU take care. 😡"
    new "你更该保重。😡"

    old "Are you guys still at home? Any update on her?"
    new "你们还在家吗？她怎么样了？"

    old "About that..."
    new "等一下……"

    old "Sorry, we're not home right now. Sky and I are tied up in a work meeting."
    new "抱歉，我们现在不在家。我和斯凯正在开工作会议。"

    old "But like... what else is she supposed to be doing? Honestly, I doubt anything's changed."
    new "但……她还能干嘛呢？说实话，我不觉得会有什么情况。"

    old "It's been—what, how long now? A year? And she's still locked up in her room..."
    new "都已经——多久了啊？一年吗？她还是把自己锁在房间里……"

    old "And hey, again, I'm really sorry. I shouldn't have brought it up back then."
    new "还有，再说一次，真的很抱歉。我当时不应该提的。"

    old "Yeah"
    new "是啊"

    old "Yeah."
    new "是啊。"

    old "Let's stop pointing fingers"
    new "别再怪罪自己了"

    old "Aine... how long are you gonna keep beating yourself up over this?"
    new "艾妮……你还要为这事自责多久？"

    old "To be fair, none of us saw it coming. Not even me."
    new "说实话，我们谁都没想到会变成这样。连我自己都没想到。"

    old "You were trying to help. That's more than most would've done. So let's not dwell on it, alright?"
    new "你当时是想帮忙。这就已经超过绝大多数人了。所以别再纠结了，好吗？"

    old "Alright."
    new "好吧。"

    old "You saw she was down, and you tried to be there for her. That's not a mistake."
    new "你当时看到她心情不好，想陪在她身边。你没有犯错。"

    old "None of us could've predicted how she'd react. I certainly didn't."
    new "我们谁都没法预料她会有什么反应。我当然也没预料到。"

    old "You meant well, and did more than most people would've even tried. So let's stop pointing fingers, yeah?"
    new "你是出于好意，而且做了大多数人根本试都不愿意试的事情。所以别再怪罪自己了，好吗？"

    old "Okay."
    new "好吧。"

    old "I miss you."
    new "我很想你。"

    old "Give me something"
    new "发点东西给我"

    old "Come on... give me something."
    new "好啦……发点东西给我吧。"

    old "Pfft! It's only been a few hours, [mc]. Cool that {i}thing{/i} down."
    new "噗！才几个小时而已，[mc!t]。让{i}那玩意儿{/i}歇歇吧。"

    old "You're lucky I'm in the bathroom. Sky thinks I'm neck-deep in spreadsheets."
    new "你运气好，正好赶上我去洗手间。斯凯还以为我在埋头做报表呢。"

    old "Hot damn! That just made my whole day!"
    new "色爆了！我一整天都会开心的！"

    old "Haha! You sap. Like we haven't been pulling this stunt for almost six months now."
    new "哈哈！你这个傻瓜。我们都已经这样演了快六个月了。"

    old "Hey, even tradition's gotta keep up with the times."
    new "传统也得与时俱进嘛。"

    old "Alright, alright, you big ol' cheese ball."
    new "行吧，行吧，说不过你这个大色狼。"

    old "Now all I can think about is burying my face between those gorgeous curves... teasing every inch with my tongue while my fingers trace over your pebbled peaks..."
    new "我现在满脑子都是把脸埋在那绝妙的曲线里……一边揉捏鸽乳上的娇嫩蓓蕾，一边用我的舌头四处出击……"

    old "... trailing kisses down to your ribs, your stomach, your hips... lower, and lower, until..."
    new "……一路往下，吻你的肋骨，吻你的肚子、腰肢……越来越低，直到……"

    old "You're redder than a rose again, aren't you?"
    new "脸又红得要滴血了吧？"

    old "I hate you..."
    new "烦死你了……"

    old "I love you. Come home safe."
    new "我爱你。一路顺风。"

    old "Oh, I'll definitely be {i}coming{/i} when I get there..."
    new "不仅一路顺风，回去之后还会一“撸”顺风呢……"

    old "... Remind me why I agreed to marry you again?"
    new "……我为什么会愿意嫁给你啊？"

    old "Pfft! It's only been a few hours, [mc]. You seriously can't survive a single day without me?"
    new "噗！才几个小时而已，[mc!t]。你离了我一天都活不下去吗？"

    old "And yet, somehow, your radiant smile never ceases to make my whole damn day."
    new "可是呢，你灿烂的笑容还是能让我有一天的好心情。"

    old "Alright, alright... you big softie."
    new "好吧，好吧……嘴倒是挺甜。"

    old "[mc], just a heads-up: I'm crashing at the office tonight. Gonna try and power through a few days' worth of work."
    new "[mc!t]，跟你说一下，我今晚睡在办公室了。我准备一口气把几天的工作都干完。"

    old "Make sure you get some rest, okay?"
    new "你一定好好休息，知道了吗？"

    old "Alright. Thanks for the FYI. Just don't push yourself too hard."
    new "好。谢谢你告诉我。你也别把自己逼太紧。"

    #FREYA

    old "hey did youeat or were you runningon vibes agian"
    new "哥们你吃饭了吗还是有在强撑"

    old "Coffee is a food group."
    new "咖啡也算是食物吧。"

    old "yuo worry meanyway im stealing your hoodie tomorroww this is not a requets"
    new "尼反正天天让我操心我明天天就把你卫衣偷走我不管同不同意"

    old "WTF?"
    new "什么鬼？"

    old "I don't know if you stole Gwen's potion called alcohol, because you sound like a drunk sissy."
    new "你怕不是偷喝了格温的酒，都醉成什么样子了。"

    old "I don't even have a hoodie."
    new "我根本没有卫衣。"

    old "IM NOT drnuk ok??im typignPERFECTLY"
    new "我没最好吧、、》我打地美个字都好着呢"

    old "Freya."
    new "芙蕾雅。"

    old "Hit the space bar."
    new "点逗号键。"

    old "It's free. You can use it."
    new "不要钱。随便用。"

    old "DONTtellMEhowTOlivMYIFE"
    new "不用你叫我怎么做我自己有己活法我是最不一样的烟火"

    old "THE SPACE BAR, GODDAMNIT!"
    new "妈的，用逗号！"

    old "im honry"
    new "我想被查"

    old "Hi, honry."
    new "查还是插？"

    old "Should I call the spelling police?"
    new "用不用我真的喊错别字警察来给你调查一下？"

    old "wtf did i text u last night"
    new "我他妈昨晚都给你发什么了"

    old "How would {b}I{/b} know?"
    new "{b}我{/b}怎么可能知道？"

    old "You typed like your thumbs were fighting for custody."
    new "你昨晚打字的时候就跟大拇指之间在打架似的。"

    old "Wait. Did you..."
    new "等等。难道你……"

    old "I DID NOT!!"
    new "我没有！！"

    old "Hm..."
    new "嗯……"

    old "Interesting reaction. I didn't even finish the sentence."
    new "这反应挺有意思。我都没把话说完啊。"

    old "Feels like someone's guilty. Don't worry, Frey. You're secret's safe with me."
    new "看来某人犯错了。别担心，芙蕾。我会帮你保守秘密。"

    old "SHUT UP SHUT UP SHUT UP!!! DON'T TALK TO ME AGAIN!"
    new "闭嘴闭嘴闭嘴！！！别再跟我说话了！"

    old "You sure put more effort into your punctuations when you're pissed. Nice!"
    new "你生气的时候对标点符号和停顿就更上心了。不错！"

    old "AAAAAAAAAAAAAAAAA!!!"
    new "啊啊啊啊啊啊啊啊啊啊啊啊啊！！！"

    old "Want me to come over tonight?"
    new "今晚我去找你？"

    old "please? 😍😍😍"
    new "可以吗？😍😍😍"

    old "Damn, my queen of blowjobs..."
    new "真是口交女王……"

    old "You looked so good with me in your mouth, Frey."
    new "你把我含在嘴里的时候真好看，芙蕾。"

    old "But that face paint looks so much better on you. 😉"
    new "不过你脸上化的妆更是漂亮。😉"

    old "dont remind me or im dragging u here rn"
    new "别再说了不然我现在就把你拉到我这来"

    old "Promise?"
    new "说到做到？"

    old "How long does it take to withdraw a salary, Frey?"
    new "取个工资要花多久啊，芙蕾？"

    old "Did the ATM ask you for a full character backstory or what?"
    new "ATM机是要你输入你的人生历程吗？"

    old "shut UP its calculating my financial trauma"
    new "闭嘴它正在算我怎么花了这么多钱"

    old "Tell it to hurry. I'm growing roots here."
    new "让它快点。我在这都要长草了。"

    old "daddy chill im on my way"
    new "别急老爸我马上到"

    old "ok serious question how many near death experiences does one guy need??"
    new "我真要问问你一个人要在鬼门关走多少回才算够啊？？"

    old "I'm collecting them. Like stamps."
    new "我在做全收集呢。就跟集邮一样。"

    old "maybe trade them in for therapy instead???"
    new "要不拿你的收藏去兑换个心理治疗？？？"

    old "Sounds expensive."
    new "感觉很贵。"

    old "so is DYING, [mc]"
    new "{b}死掉{/b}也很贵，[mc!t]"

    old "HEY! that was the road-rager's fault. Not mine."
    new "拜托！都怪那个路怒症的人啊。不是我的错。"

    old "u were quiet"
    new "你不说话了"

    old "something wrong"
    new "出事了"

    old "Is that supposed to be a question or a statement?"
    new "你这是问句还是陈述句？"

    old "I'm fine. Just thinking."
    new "我没事。只是在思考。"

    old "You stremaing?"
    new "你要直播吗？"

    old "*streaming"
    new "*去掉吗"

    old "pfft 😄"
    new "哈哈😄"

    old "yeah in a bit"
    new "嗯马上就播"

    old "Tuning in."
    new "我会去看的。"

    old "well shit happy birthday ur officially ancient now"
    new "我操生日快乐你现在正儿八经是个老头了"

    old "Thank you. I think?"
    new "谢谢你。你是真心的吧？"

    old "dont get sappy im only doing this once a year"
    new "别太感动我一年就说这么一次"

    old "one (1) greeting limited edition cherish it"
    new "限量版祝福好好珍惜吧"

    old "You remembered. I'm surprised."
    new "你还记得啊。我很惊讶。"

    old "EXCUSE ME i have a functioning brain"
    new "少放屁我脑子好使着呢"

    old "mostly"
    new "大多数时候算好使"

    old "This actually means a lot. Thanks, Frey."
    new "这真的很重要。谢谢你，芙蕾。"

    old "STOP"
    new "停"

    old "dont make it emotional im allergic"
    new "别让我感动我对这个过敏"

    old "happy birthday [mc]"
    new "生日快乐[mc!t]"

    old "i just saw someone who walks exactly like you"
    new "我刚刚看到一个走路姿势跟你一模一样的人"

    old "same \"i hate being perceived\" energy"
    new "一样的“我最烦被人看见”的感觉"

    old "Maybe it was me?"
    new "可能那就是我？"

    old "no this one looked like they slept"
    new "不是那个人一看就有好好睡觉"

    old "so definitely not you"
    new "所以肯定不是你"

    old "And where exactly are you going with this conversation, Freya?"
    new "那你跟我说这些是什么意思呢，芙蕾雅？"

    old "to my heart obviously"
    new "当然是关心你"

    old "You've... never actually said you loved me, you know."
    new "你其实……从来没对我说过我爱你。"

    old "EW WHY WOULD YOU SAY IT LIKE THAT"
    new "呕你干嘛说这个啊"

    old "my spine just folded in half"
    new "我都快被尬成两半了"

    old "gross emotional man"
    new "少恶心人哥们"

    old "You brought it up."
    new "是你先提的。"

    old "im gonna throw up brb"
    new "我去吐一下马上回来"

    old "fine"
    new "行吧"

    old "i love you ok 😘"
    new "我爱你好吧😘"

    old "if u tell ANYONE i said that i will bite you"
    new "你要是敢说出去我就咬死你"

    old "they moved you to night shift again?"
    new "他们又给你换成夜班了？"

    old "AAAAAAAAAAA!!! 🤬"
    new "啊啊啊啊啊啊啊啊！！！🤬"

    old "Relax. It won't last."
    new "别急。不会太久的。"

    old "Night shifts burn more electricity and bring in fewer customers. Not exactly cost-efficient."
    new "夜班用电更多，客人反而更少。根本不划算。"

    old "sooo basically corporate math is gonna save u?"
    new "所以资本主义会救你吗？"

    old "Pretty much."
    new "差不多。"

    old "god bless capitalism i guess"
    new "那就感谢资本主义吧"

    old "i swear u have old man energy sometimes"
    new "我真觉得你有时候跟老头没什么区别"

    old "Why?"
    new "为啥？"

    old "u make that tiny sigh before sitting down"
    new "你坐之前会轻轻叹气"

    old "thats when the soul leaves the body"
    new "那就是你灵魂出窍的时候"

    old "I only sigh around you."
    new "我只在你面前叹气。"

    old "SEE???? elderly"
    new "看吧？？？？死老头"

    old "jeez i hate it when they move your schedules like this"
    new "烦死了我最烦他们乱给你调班"

    old "when are u coming back to work"
    new "你什么时候回来上班"

    old "My shift ended an hour ago."
    new "我一个小时之前就下班了。"

    old "yea but like"
    new "是啊但是"

    old "come back"
    new "你回来"

    old "the store is too quiet without u"
    new "你不在店里太安静了"

    old "You miss me?"
    new "你想我了？"

    old "dont get cocky or ill change my answer"
    new "别自恋不然我就改口了"

    old "remember when u said i should \"behave\" on stream"
    new "你记不记得你让我在直播的时候“规矩”点"

    old "Because you absolutely should."
    new "因为你绝对应该规矩点。"

    old "well too late"
    new "已经晚了"

    old "chat asked why i kept smiling at my phone"
    new "弹幕问我为什么一直对着手机笑"

    old "ur fault btw"
    new "全都怪你"

    old "thats what i was smiling at"
    new "我就是在对着这个笑"

    old "Wait, when did you..."
    new "等等，你什么时候……"

    old "queen of blowjobs?"
    new "口交女王？"

    old "Oh..."
    new "噢……"

    old "You're going to get me doxxed. LOL."
    new "你迟早会害我被开盒的。哈哈。"

    old "worth it you were sooooo hot btw 😍"
    new "那也值了你真的太帅了😍"

    old "did u know u have the emotional range of a teaspoon"
    new "你知不知道你的感情波动就跟茶匙一样"

    old "I tell you... things."
    new "我会跟你……说话啊。"

    old "u tell me FACTS"
    new "你只说事实"

    old "thats not emotions thats customer service voice"
    new "那不叫感情那是客服的语气"

    old "I have emotions."
    new "我有感情。"

    old "name ONE"
    new "哪怕说一个出来呢"

    old "I love you."
    new "我爱你。"

    old "my entire body made a windows error noise"
    new "我全身都报错了"

    old "You just wanted to get that out of me, didn't you?"
    new "你就是想让我说这个，对不对？"

    old "hey random question"
    new "我随便问你一下"

    old "is miss klara doing okay"
    new "克拉拉阿姨还好吧"

    old "i havent seen her in forever"
    new "我好久没见过她了"

    old "She's... not doing great."
    new "她……不太好。"

    old "She's been staying in her room most days. Heck, I haven't seen her open the door once."
    new "她一直在房间里不出来。我都没见她开过门。"

    old "shit"
    new "我操"

    old "i knew she wasnt like sunshine or anything but thats different"
    new "我知道她不是那种阳光型的但也不至于这样吧"

    old "tell her i said hi i guess"
    new "那你替我跟她问声好吧"

    old "and that she can punch me if she ever needs to yell at someone"
    new "还有如果她需要找人撒气可以来打我"

    old "I'll tell her."
    new "我会告诉她的。"

    old "not the punch me part tho"
    new "可以打我那句就不用了"

    old "stream overrrrrr"
    new "下播啦啦啦啦啦啦啦啦啦啦啦"

    old "ty for hanging out chat was actually tolerable today"
    new "谢谢你来看今天的弹幕还算能忍"

    old "ALSO"
    new "还有"

    old "WHAT WAS THAT DONO"
    new "你给我打那么多钱干嘛"

    old "i almost choked on my drink live"
    new "我差点直播的时候被水呛到"

    old "do u WANT me to die on camera is that it"
    new "你是不是想让我死在镜头前"

    old "Consider it hazard pay for letting the internet look at you."
    new "算是让全网都能看你的风险津贴吧。"

    old "thats not pocket change that was like"
    new "那可不是小钱那简直是"

    old "\"i feel guilty watching the vods for free\" money"
    new "“我免费看你直播心里真是过意不去”级别的钱"

    old "You work hard. Let me spoil you a bit."
    new "你很努力了。让我宠你一次吧。"

    old "stop saying nice things im feral i dont know how to process that"
    new "别说好听的我受不了我不知道怎么反应"

    old "ok fiiiine"
    new "行吧行吧行吧"

    old "special thank u for my favorite whale only: [ftname]"
    new "给我最爱的老头[ftname!t]一个特别感谢"

    old "Worth every cent."
    new "钱没白花。"

    old "DONT SAY IT LIKE THAT IM GONNA SHORT CIRCUIT"
    new "别这么说话我会短路的"

    old "Cum tribute done."
    new "打给你了。"

    old "YOU DID WHAT???"
    new "打什么了？？？"

    old "im at Corner Potatoes"
    new "我在角落薯条店"

    old "these fries are so good im actually mad youre not here"
    new "这家的薯条太好吃了你没来我真有点生气"

    old "Hello? You could've invited me?"
    new "你怎么不喊我呢？"

    old "i did"
    new "我喊了"

    old "in my head"
    new "脑子里喊的"

    old "you didnt answer"
    new "你没回我"

    old "movie night on our day off?"
    new "休息日一块看电影？"

    old "ill even let u pick so u stop crying about my taste"
    new "我甚至愿意让你选看什么免得你再抱怨我的品味"

    old "Your taste is violence and trauma."
    new "你的品味就是暴力和创伤。"

    old "and subtitles"
    new "还有字幕"

    old "im cultured"
    new "我是懂行的"

    old "You made me watch a 3-hour film where everyone died in silence."
    new "你让我看了一部三个小时长，最后所有人都默默死去的电影。"

    old "absolute cinema is about suffering [mc]"
    new "完美的电影就是讲苦难的[mc!t]"

    old "also bc u whined like a sissy when i picked the romance one"
    new "选那个还因为我选了爱情片之后你像个小姑娘一样抱怨"

    old "It was about two people staring at each other for fifteen DAMN minutes straight."
    new "那部电影就是两个主角对视了他妈的整整十五分钟。"

    old "Heck, Twilight had better love story than whatever that abomination was."
    new "连暮光之城里的爱情故事都比那破玩意儿好。"

    old "THATS CALLED TENSION"
    new "那叫张力"

    old "u wouldnt get it"
    new "你不懂"

    old "I get tension. I lived through your commentary."
    new "我懂什么叫张力。因为我经历过你的解说。"

    old "my commentary was ICONIC shut up"
    new "我的解说才是经典你闭嘴吧"

    old "anyway pick something good this time"
    new "总之这次挑一部好看的"

    old "Lower your expectations."
    new "把期待值放低点。"

    old "never"
    new "不可能"

    old "screw the movie this was a better happy ending"
    new "电影无所谓了这才是更棒的好结局"

    old "... Frey."
    new "……芙蕾。"

    old "You're gonna kill me one of these days."
    new "你迟早要把我害死。"

    old "soooooo"
    new "所以"

    old "u werent gonna tell me"
    new "你都不打算告诉我"

    old "that youre LEAVING this store to go be mr. fancy REGIONAL MANAGER??"
    new "你要离开这家店去当你那狗屁区域经理？？"

    old "I was going to tell you today."
    new "我本来今天打算跟你说的。"

    old "uh huh sure thats what ppl say when they get caught"
    new "嗯哼当然啦每个人被抓包的时候都是这么说的"

    old "cant believe youre abandoning me with THIS gremlin"
    new "你居然抛弃我要留我一个人跟这个妖精一起上班"

    old "I'm not abandoning you."
    new "我没有抛弃你。"

    old "you kinda ARE"
    new "就是有"

    old "whos gonna stop me from fighting customers now???"
    new "之后谁来阻止我跟客人吵架啊？？？"

    old "You're not supposed to fight customers {b}now{/b}."
    new "你{b}现在{/b}就不该跟客人吵架。"

    old "YEAH AND WHO ENFORCES THAT RULE???"
    new "是啊这是谁定的规矩呢？？？"

    old "I'll still be around. It's just a different position."
    new "我还是会去的。只是职位不一样了。"

    old "different position my ass"
    new "什么职位不一样我一屁股坐死你"

    old "Is that a promise next time I visit for a back room \"inspection\"? 😜"
    new "下次我去店里“视察”的时候你坐一下试试？😜"

    old "stop making me horny im trying to vent!!!"
    new "别让我兴奋我只是想发泄！！！"

    old "youre leaving ME here while you go play boss man somewhere else"
    new "你把我丢在这跑去其他地方当领导"

    old "i hate it"
    new "我讨厌这样"

    old "... I didn't think you'd take it this hard."
    new "……我没想到你会这么难过。"

    old "like im not crying or anything jeez"
    new "我也没有哭没有什么的天啊"

    old "im just MAD bc we were a duo"
    new "我就是很生气因为我们是搭档"

    old "and now its just me and an idiot who dont know how to read instructions"
    new "现在就剩我和一个连说明书都看不懂的傻逼了"

    old "You'll survive. You're Freya."
    new "你能行的。你是芙蕾雅。"

    old "stop hyping me up im trying to be mad at you"
    new "别给我打鸡血我正准备生你的气呢"

    old "You can be mad. I get it."
    new "你可以生气。我理解。"

    old "But it's a good opportunity. I couldn't turn it down."
    new "但这是个好机会。我不能拒绝。"

    old "yeah yeah growth character development blah blah whatever"
    new "行行行人物成长角色发展之类的废话随便你了"

    old "still hate it"
    new "还是讨厌"

    old "but im proud of you too or whatever"
    new "不过随便吧我也为你感到骄傲"

    old "Thank you. Really."
    new "谢谢你。真的。"

    old "dont make this wholesome im trying to sulk"
    new "别弄得这么温馨我正要生闷气呢"

    old "Frey."
    new "芙蕾。"

    old "dont talk to me im sad"
    new "别跟我说话我很伤心"

    old "*mad"
    new "*生气"

    old "Still?"
    new "还是生气？"

    old "still so shoo"
    new "还是烦你"

    old "You on shift tomorrow?"
    new "你明天上班吗？"

    old "yeah why what did i do"
    new "上啊怎么了我干嘛了"

    old "Nothing... yet."
    new "目前……还没干嘛。"

    old "Heads up: I've got a performance inspection at your branch tomorrow."
    new "提醒你一下：我明天要去你们店里做绩效检查。"

    old "I'm not really supposed to warn you in advance, so you didn't hear this from me."
    new "我不该提前告诉你的，所以别跟别人说是我说的。"

    old "oh so youre cheating for me now"
    new "哦你给我开后门是吧"

    old "love that for us"
    new "我喜欢这样"

    old "I just don't want you or the girl you're training getting blindsided."
    new "我只是不想让你或者你带的那个女生被打个措手不及。"

    old "oh GREAT her"
    new "太好了你还惦记着她啊"

    old "she cant even stack buns in the right order"
    new "她连面饼都不会放"

    old "if she drags my score down im committing a crime"
    new "如果她拉低我的评分我一定会发疯"

    old "and why the F does she keeps calling me \"maam\""
    new "而且她他妈的为什么老叫我“女士”"

    old "which is RUDE bc im baby"
    new "太没礼貌了我明明是个小宝宝"

    old "You're many things. \"Baby\" is not the word I'd use."
    new "你可以是很多东西。但不会是“宝宝”。"

    old "SHUSH! im delicate"
    new "闭嘴！我很脆弱的"

    old "but ok noted inspector sir"
    new "不过行吧我知道了检查官先生"

    old "ill make sure no one sets anything on fire"
    new "我会保证没人会把店里给烧了"

    old "Walk her through the basics before I get there."
    new "我去之前把基础的东西跟她讲讲。"

    old "ugh fiiine \"teamwork\" or whatever"
    new "唉行吧行吧还是得整点“团队合作”"

    old "That would be appreciated."
    new "谢谢你。"

    old "if i survive this u owe me fries"
    new "要是我撑过去了你要请我吃薯条"

    old "Deal. Just don't bite a customer in front of me."
    new "没问题。别当着我的面咬客人就行。"

    old "no promises"
    new "没法保证"

    old "hey"
    new "嘿"

    old "can u pick me up after my shift?"
    new "能来接我下班吗"

    old "feet will be dead, dignity will be gone, i will require evac"
    new "到时候脚都废了尊严也没了我需要人来救援"

    old "I'll be there. End of shift, right?"
    new "可以。下班之后到，对吧？"

    old "yeah"
    new "对"

    old "dont be late i wanna complain about management to management"
    new "别迟到我想向管理层投诉一下管理层"

    old "Nerd..."
    new "死宅……"

    old "hey 😡"
    new "喂😡"

    old "i love"
    new "我也"

    old "I love...?"
    new "我也……？"

    old "i love you too goddamnit"
    new "我也爱你他妈的"

    old "hey, [mc]"
    new "[mc!t]"

    old "can u pick me up later? 😩"
    new "待会能来接我吗？😩"

    old "Yeah, sure. I'll be there."
    new "可以啊。我会去的。"

    old "Do I need to bring anything? Water? Snacks?"
    new "需要我带什么东西吗？水？零食？"

    old "... a stretcher? Ambulance?"
    new "……担架？救护车？"

    old "WOW"
    new "靠"

    old "im tired not DYING wtf"
    new "我是累了不是要死了我操"

    old "but like if u DID show up w an ambulance i wouldnt complain"
    new "但你要是真开救护车来我也没意见"




    #EMMA

    old "[mc]. [mc]. Emergency."
    new "[mc!t]。[mc!t]。紧急情况。"

    old "Emergency? What happened?"
    new "紧急情况？怎么了？"

    old "I need to take a photo of myself for online authentication."
    new "我在网上认证，需要拍一张自己的照片。"

    old "How do I switch to the front camera?"
    new "怎么切换到前置摄像头？"

    old "... You're serious?"
    new "……你认真的？"

    old "I'm not very tech-savvy, okay?"
    new "我不太懂科技的东西，不行吗？"

    old "I'll learn once you teach me."
    new "你教我一下我就能学会了。"

    old "I'm quite impressed you've survived this long."
    new "你居然能活到现在，我还挺佩服的。"

    old "Next to the capture button, see the two arrows forming a circle?"
    new "在快门按钮旁边，有一个两个箭头组成的圆圈，看见了没？"

    old "Tap that."
    new "点一下。"

    old "Okay, it worked."
    new "好，我会了。"

    old "But how do I delete this?"
    new "但怎么把这张照片删掉？"

    old "You can't. Once it's sent, it's mine forever."
    new "没法删。你一发过来，就永远都在我这了。"

    old "Then just don't save it."
    new "那你不保存就行了。"

    old "Problem solved."
    new "很容易解决。"

    old "Sure."
    new "好的。"

    old "You saved it."
    new "你肯定存了。"

    old "Of course I did."
    new "我当然要存。"

    old "You telling me not to save it is basically reverse psychology."
    new "你让我别存不就是反向心理学吗？"

    old "I'm keeping this as evidence of your crimes, Detective. 😈"
    new "我会保存你这张犯罪的证据，警探。😈"

    old "See you in bed."
    new "我们床上见。"

    old "I mean, in court!"
    new "不对，法庭见！"

    old "WHY?? 😡"
    new "为什么？？😡"

    old "Really like how you've been styling your hair lately. You should keep it."
    new "很喜欢你最近的发型。别换了。"

    old "You mean that?"
    new "真的吗？"

    old "Yeah. It kinda reminds me of how you wore it back when we were kids."
    new "是啊。有点像我们小时候你留的发型。"

    old "Okay, I will. 😊"
    new "好，那我不换了。😊"

    old "I love you!"
    new "我爱你！"

    old "I love you too, Em."
    new "我也爱你，小艾。"

    old "[mc]. [mc]. Quick question."
    new "[mc!t]。[mc!t]。问你个事。"

    old "Possibly urgent. Possibly stupid."
    new "可能很紧急。也可能很蠢。"

    old "You have my attention."
    new "你说吧。"

    old "My laptop says it needs an update."
    new "我的笔记本上面显示需要更新。"

    old "If I click it, will it explode?"
    new "如果我点了的话，会爆炸吗？"

    old "Thank you for contacting [mc]Tech™ Support."
    new "感谢您联系[mc!t]科技™的客服支持。"

    old "My name is [mc]. I'll be assisting you today."
    new "我的名字是[mc!t]。今天由我来为您服务。"

    old "Huh? What are you talking about?"
    new "啊？你在说什么？"

    old "Before we proceed, I must ask:"
    new "在我们继续之前，请您回答："

    old "Have you tried turning it off and on again?"
    new "您有尝试过重启吗？"

    old "Hold on."
    new "等一下。"

    old "Okay, I did that. It's still asking to update."
    new "我重启完了。还是说要更新。"

    old "Excellent. Progress has been made."
    new "非常棒。我们有很大进展。"

    old "Now, please click the update button."
    new "现在，请您点击更新按钮。"

    old "Your device will not explode. Probably."
    new "您的设备大概率不会爆炸。"

    old "\"Probably\" is not reassuring."
    new "“大概率”这词有点不靠谱。"

    old "Okay. I clicked it."
    new "好。我点了。"

    old "Great choice."
    new "非常明智的选择。"

    old "While we wait, please refrain from touching anything."
    new "在等待更新的时候，请您哪里都不要碰。"

    old "Too late."
    new "已经晚了。"

    old "Emmaaaaaaaaaa!"
    new "艾玛啊啊啊啊啊啊！"

    old "Relax! I just adjusted the brightness."
    new "别急！我只是调了调亮度。"

    old "It's done now. It says \"Update Complete.\""
    new "好了。显示“更新完成”。"

    old "Congratulations."
    new "恭喜您。"

    old "Your system is up to date and your life remains intact."
    new "您的设备已是最新版本，并且您的人身安全也没有受到损害。"

    old "Wow."
    new "哇。"

    old "Thank you, Mr. Tech Support."
    new "谢谢你，客服先生。"

    old "Anytime."
    new "不用客气。"

    old "[mc]Tech™ Support is available 24/7."
    new "[mc!t]科技™的客服全天候为您服务。"

    old "Payment accepted in snacks, compliments, or coffee."
    new "我们接受零食、赞美或咖啡作为付款。"

    old "I love you. Keep the change. 😘"
    new "我爱你。不用找了。😘"

    old "Payment received: one (1) heartfelt \"I love you.\""
    new "确认收到了您一份真挚的“我爱你”。"

    old "No receipt needed. Transaction complete."
    new "无需打印收据。交易已完成。"

    old "Thank you for choosing [mc]Tech™ Support."
    new "感谢您选择[mc!t]科技™的客服支持。"

    old "Please come again if the internet scares you."
    new "若您再被互联网吓到，请随时再联系我们。"

    old "[mc]. [mc]. Happy birthday! 🥰"
    new "[mc!t]。[mc!t]。生日快乐！🥰"

    old "I checked the date twice to be sure."
    new "我确认了两次日期，就怕弄错。"

    old "Thanks, Em."
    new "谢谢，小艾。"

    old "But I don't really feel like celebrating my birthdays anymore."
    new "但是我现在不太想庆祝生日了。"

    old "What?"
    new "什么？"

    old "No. I won't accept that."
    new "不行。我不允许。"

    old "I'm clocking out early. I'm coming to get you."
    new "我今天提前下班。我去找你。"

    old "We're buying a cake. This is not optional."
    new "我们一定要买个蛋糕。没得商量。"

    old "Stay there, okay?"
    new "哪儿也别去，听见没有？"

    old "Okay..."
    new "好吧……"

    old "Stop slapping my butt!"
    new "不要再打我屁股了！"

    old "I don't know. Kinda felt like an invitation."
    new "不好说哦。它就在那等我去打呢。"

    old "I hate you for planning this."
    new "你居然给我下套，我真是讨厌死你了。"

    old "I didn't see through it at all. Not even a little."
    new "我根本就没想到。一点都没发现。"

    old "Guess that makes me your weakness."
    new "看来我是你的弱点。"

    old "That, and technology."
    new "还有科技也是。"

    old "Unfortunately... yes."
    new "不幸的是……的确如此。"

    old "Love you, Em."
    new "爱你，小艾。"

    old "I love you too, [mc]. I did enjoy tonight."
    new "我也爱你，[mc!t]。我今晚很开心。"

    old "Just not the slapping."
    new "除了你打我屁股的时候。"

    old "You're making it very hard to behave. 🤣"
    new "你越说我越忍不住想打你屁股。🤣"

    old "[mc]. [mc]."
    new "[mc!t]。[mc!t]。"

    old "I need [mc]Tech™ Support again."
    new "我又需要找[mc!t]科技™的客服了。"

    old "[mc]Tech™ Support online."
    new "[mc!t]科技™的客服已上线。"

    old "Please describe the issue without panicking."
    new "请不要惊慌，描述一下您的问题。"

    old "I am already panicking."
    new "我已经很慌了。"

    old "I got an email that says my account has been compromised."
    new "我收到一封邮件，说我的账号被盗了。"

    old "Understood."
    new "明白了。"

    old "First question."
    new "第一个问题。"

    old "Did the email address look even remotely human?"
    new "发件人的邮箱地址看着像是正常人会用的吗？"

    old "It was something like support-security-alert-official-team@totallylegit.ru"
    new "好像是an-quan-tuan-dui-guan-fang-jing-bao@bushipianzi.ru。"

    old "Excellent."
    new "很好。"

    old "That already tells me everything I need to know."
    new "我已经知道是怎么回事了。"

    old "So, I {b}am{/b} hacked?"
    new "所以我真的被盗号了？"

    old "No."
    new "没有。"

    old "You are being courted by a phishing attempt."
    new "你这是被钓鱼邮件盯上了。"

    old "Phishing, like fish?"
    new "钓鱼？在网上怎么钓鱼？"

    old "Except instead of bait, they use panic."
    new "网络上的钓鱼用的不是鱼饵，而是恐慌。"

    old "And instead of a hook, they want your password."
    new "而且他们要的不是鱼，而是你的密码。"

    old "It {b}did{/b} say I had to act immediately or lose access forever."
    new "这里面确实说了我必须立马行动，不然就永远登不上这个号了。"

    old "That's classic lure."
    new "这是很经典的话术。"

    old "Did you click anything?"
    new "你什么都没点吧？"

    old "EMMAAAAAAAAAAAA!"
    new "没点吧？艾玛！！！！！"

    old "I didn't {b}enter{/b} anything!"
    new "我什么都没{b}输入{/b}！"

    old "I just hovered over the link."
    new "只是把鼠标放到链接上了。"

    old "Hovering is safe."
    new "放上去没事。"

    old "Clicking is how they get you."
    new "要点下去才会中招。"

    old "So what do I do now?"
    new "那我现在该怎么办？"

    old "Step one: Do not reply."
    new "第一步：不要回复。"

    old "Step two: Do not click anything."
    new "第二步：什么都不要点。"

    old "Step three: Report it as phishing."
    new "第三步：举报这封钓鱼邮件。"

    old "That's it?"
    new "就这些？"

    old "That's it."
    new "就这些。"

    old "Also delete it. With prejudice."
    new "然后把它删掉。彻底删掉。"

    old "Okay, done."
    new "好，我照做了。"

    old "I really thought I was about to lose everything."
    new "我真的以为账号里的东西全都要没了。"

    old "You did the right thing."
    new "你做得很对。"

    old "You asked before acting."
    new "你在行动之前先问了我。"

    old "Guess I'm learning."
    new "看来我有所长进。"

    old "Proud of you."
    new "你真棒。"

    old "I love you, Mr. Tech Support. 😁"
    new "我爱你，客服先生。😁"

    old "I love you too!"
    new "我也爱你！"

    old "[mc]. [mc]. Confirming a phishing attempt."
    new "[mc!t]。[mc!t]。我好像又收到钓鱼邮件了。"

    old "Good evening, ma'am. [mc]Tech™ Support online."
    new "晚上好，小姐。[mc!t]科技™的客服为您服务。"

    old "What tipped you off?"
    new "出什么事了？"

    old "Email claims my mobile account is \"overdue.\""
    new "有封邮件说我的手机号“欠费”了。"

    old "Uses urgency. Mentions service interruption."
    new "说是很紧急。还说会给我停机。"

    old "That's pressure tactic. 😤"
    new "这是压力战术。😤"

    old "Sounds suspicious so far."
    new "目前为止是有点可疑。"

    old "Sender domain matches the carrier."
    new "发件人的域名跟我的运营商是一样的。"

    old "Which is exactly what they'd want you to think."
    new "他们就是要让你这么想。"

    old "Naturally."
    new "我就知道。"

    old "No spelling errors."
    new "没有错别字。"

    old "Polite but firm tone."
    new "语气很礼貌又坚定。"

    old "Includes the last four digits of my account."
    new "里面还有我手机号的后四位。"

    old "Em?"
    new "小艾？"

    old "Yes?"
    new "怎么了？"

    old "Did you forget to top up your prepaid plan again?"
    new "你是不是又忘交话费了？"

    old "Irrelevant."
    new "无关紧要。"

    old "The email includes a PDF attachment."
    new "邮件里有个PDF附件。"

    old "A bill?"
    new "账单？"

    old "A {b}weaponized{/b} bill."
    new "是伪装成账单的{b}武器{/b}。"

    old "Em, what exactly does the subject line say?"
    new "小艾，邮件的主题那一栏里写了什么？"

    old "\"Monthly Statement — Payment Due.\" Why?"
    new "“月度账单——欠费。”怎么了？"

    old "And the sender?"
    new "发件人呢？"

    old "Herizon <billing@herizon.com>"
    new "Herizon <billing@herizon.com>"

    old "And the amount?"
    new "金额？"

    old "$24.80."
    new "24.8金城元。"

    old "EMMAAAAAAAAAAAAA!"
    new "艾玛！！！！！！"

    old "That is your phone bill!"
    new "你没交话费！"

    old "Really!"
    new "真的！"

    old "You told me last week you \"definitely pay it later.\""
    new "你上星期跟我说你“之后肯定交”。"

    old "I was under duress."
    new "我当时很慌张。"

    old "By procrastination."
    new "因为你在拖延。"

    old "So, it's not phishing."
    new "所以不是钓鱼。"

    old "No.{#1}"
    new "不是。"

    old "Then why does it feel like a threat?"
    new "可为什么总感觉邮件里的话像是在威胁我呢？"

    old "Because capitalism is scarier than scammers."
    new "因为资本主义比骗子更可怕。"

    old "I already reported it."
    new "我已经举报了。"

    old "To who?"
    new "举报给谁？"

    old "The carrier."
    new "运营商。"

    old "You reported the carrier... to itself?"
    new "你向运营商……举报运营商？"

    old "In my defense, the form was very convincing."
    new "没办法，那个举报表格让我看了就想填。"

    old "Please pay your bill."
    new "你赶紧把话费交了吧。"

    old "Good. Thank you for choosing [mc]Tech™ Support."
    new "很好。感谢您选择[mc!t]科技™的客服支持。"

    old "And I love you, Emma Meyer."
    new "还有我爱你，艾玛·梅耶。"

    old "I love you too, [mc]."
    new "我也爱你，[mc!t]。"

    old "I'll see you later at dinner."
    new "晚饭时候再见吧。"

    old "It's your favorite for tonight."
    new "今晚有你最爱吃的。"

    old "[mc]. [mc]. I have a situation."
    new "[mc!t]。[mc!t]。我遇到麻烦了。"

    old "Why's this a monthly thing now...?"
    new "怎么每个月都会这样……？"

    old "Anyway, [mc]Tech Support™, this is [mc] speaking."
    new "总之，我是[mc!t]科技™的客服，[mc!t]。"

    old "Are you calling about billing, hardware, or a life-ruining pop-up?"
    new "你是想咨询账单、硬件，还是毁掉人生的弹窗？"

    old "I have been charged."
    new "我被扣钱了。"

    old "For something I did not consciously agree to."
    new "但我根本没有同意过。"

    old "Ah. Accidental subscription."
    new "啊。意外订阅。"

    old "Let me guess, free trial, seven days, now billed annually?"
    new "我猜猜，免费试用七天，然后就扣了你一年的钱？"

    old "How did you know?"
    new "你怎么知道？"

    old "Experience."
    new "经验之谈。"

    old "[mc], I want it canceled."
    new "[mc!t]，我想取消掉。"

    old "I can guide you through it."
    new "我可以一步步教你怎么做。"

    old "Can't you cancel it yourself?"
    new "你不能亲自帮我取消吗？"

    old "I cannot access your account."
    new "我没法登录你的账号。"

    old "That would be illegal, unethical, and deeply unattractive."
    new "那样既违法，又不道德，还特别没法装逼。"

    old "Okay, fine."
    new "好吧，听你的。"

    old "Guide me, please."
    new "教我吧。"

    old "Step one: open the app."
    new "第一步：打开app。"

    old "It's open."
    new "打开了。"

    old "Step two: tap your profile icon."
    new "第二步：点击你的个人资料图标。"

    old "Top right?"
    new "右上角？"

    old "Why is it smiling at me? 🫤"
    new "为什么它会对我笑？🫤"

    old "Ignore the mascot. It feeds on hesitation."
    new "别管那个吉祥物了。它就是为了让你犹豫的。"

    old "I see \"Account.\""
    new "我看到“账号”了。"

    old "Tap it."
    new "点一下。"

    old "Now it says \"Manage Subscription.\""
    new "这里面有个“管理订阅”。"

    old "This is exactly where they try to scare you."
    new "他们专门会在这个地方吓你。"

    old "It says I'll lose access to premium features."
    new "说是我会失去所有高级功能的使用权。"

    old "You never used those."
    new "你也没用过那些功能。"

    old "I {b}might have{/b}."
    new "我可能用过。"

    old "Em? For what?"
    new "啊？用什么了？"

    old "I downloaded an e-book called \"Talking Normally: A Guide for Professionals Who Don't\"."
    new "我下载了一本电子书，《正常说话指南：给不会说话的专业人士的指导》。"

    old "It was actually good and informative until five pages later, it said \"Warning: Your current tone may intimidate civilians. Unlock better inflections through Premium Plan now.\""
    new "开头的五页还挺有用的，结果后面就变成“警告：你现在的语气可能会吓到普通人。现在就开通高级计划，解锁更好的语调吧。”"

    old "I wanted to finish it, so I pressed the button."
    new "我想把它看完，就点了那个按钮。"

    old "As your tech support, I don't even know what to say..."
    new "作为你的科技客服，我都不知道该说什么好了……"

    old "It's asking me why I'm leaving."
    new "它问我为什么要取消订阅。"

    old "Select \"Too expensive.\""
    new "选“价格太贵”。"

    old "There's also \"Not what I expected.\""
    new "还有一个“与预期不符”。"

    old "That one is emotionally honest but less effective."
    new "那个原因虽然很诚实，但没那么有效。"

    old "Selected."
    new "选好了。"

    old "Now it says, \"Are you sure?\""
    new "现在问我“你确定吗？”"

    old "They always ask twice."
    new "他们总是问两遍。"

    old "This is your moment. Be strong."
    new "加油。坚强点。"

    old "I interrogate murder suspects for a living."
    new "我的工作可是审问杀人犯。"

    old "Confirmed."
    new "确认了。"

    old "It says \"Subscription canceled.\""
    new "显示“订阅已取消。”"

    old "That's it. That's what you want."
    new "好了。搞定。"

    old "They almost made me stay with a discount."
    new "他们还说给我打折，我差点就答应了。"

    old "Yeah, they always try one last bribe. Like an ex who learned budgeting."
    new "是啊，他们总会最后试探一下，就像学会理财的前任。"

    old "I'll just buy physical copies next time. Thanks, Mr. Tech Support."
    new "我下次买实体书就好了。谢谢你，客服先生。"

    old "Payment received:"
    new "款项已收到："

    old "One successful cancellation."
    new "一次成功的取消。"

    old "Zero data breaches."
    new "没有数据泄露。"

    old "One \"I love you\"."
    new "一句“我爱你”。"

    old "Receipt emailed. No refunds."
    new "收据已发送。无需退款。"

    old "[mc]. [mc]. I require technical assistance."
    new "[mc!t]。[mc!t]。我需要技术支持。"

    old "Again. Sorry. 😖"
    new "又要麻烦你了。抱歉。😖"

    old "My phone is altering my messages."
    new "我的手机会擅自改掉我发的消息。"

    old "Altering how?"
    new "怎么改的？"

    old "Like typos, or..."
    new "是错别字，还是……"

    old "Sabotage."
    new "曲解语意。"

    old "I typed: \"The suspect is cooperative.\""
    new "我打的是：“嫌疑人很配合。”"

    old "It sent: \"The suspect is adorable.\""
    new "发出去的是：“嫌疑人很可爱。”"

    old "Oh. My. Goodness!"
    new "我。的。天！"

    old "Please tell me that wasn't to the suspect."
    new "请你一定告诉我那不是发给嫌疑人的。"

    old "It was to my supervisor."
    new "是发给我的上司的。"

    old "This compromises my credibility."
    new "这影响了我的信誉。"

    old "Okay. Deep breath."
    new "好吧。先深呼吸一下。"

    old "That's autocorrect."
    new "这是因为自动纠错功能。"

    old "But I did not authorize correction."
    new "可是我没有授权它纠正啊。"

    old "Yeah, it does that anyway."
    new "是啊，但它不会听你的。"

    old "It guesses what you're trying to say."
    new "它会猜测你想说什么。"

    old "It guessed wrong."
    new "它猜错了。"

    old "And confidently!"
    new "还错得理直气壮！"

    old "You can turn it off."
    new "你可以把它关掉。"

    old "Can you guide me through it?"
    new "你能教我怎么关吗？"

    old "Settings."
    new "设置。"

    old "Keyboard."
    new "键盘。"

    old "Then toggle off autocorrect."
    new "然后关掉自动纠错。"

    old "Done."
    new "好了。"

    old "If I make a mistake now, it will be my mistake."
    new "接下来要是我打错了，那就是怪我了。"

    old "I can accept that, at least. 😑"
    new "至少那样我能接受。😑"

    old "Glad I could help."
    new "很高兴能帮到你。"

    old "Anything else while you've got me?"
    new "趁这机会，还有别的事要问我吗？"

    old "Yeah.{#1}"
    new "有。"

    old "Why did it replace \"suspect\" with \"sweetheart\" earlier."
    new "之前还把“嫌疑人”改成“心上人”了。"

    old "... That one might be on you."
    new "……那可能是你的问题。"

    old "Unacceptable."
    new "不可接受。"

    old "Thank you for your assistance."
    new "谢谢你帮我。"

    old "Anytime!"
    new "不客气！"

    old "If this happens again, I will switch to handwritten notes."
    new "如果再出现这种情况，我就改用手写了。"

    old "Technology has been warned! 😠"
    new "这是我对所有科技产品的警告！😠"

    old "[mc]. [mc]. The problem has evolved! 😨"
    new "[mc!t]。[mc!t]。问题又变大了！😨"

    old "Oh no."
    new "完蛋。"

    old "What did autocorrect do this time?"
    new "这次又自动纠正什么了？"

    old "It's learning my vocabulary."
    new "它正在学我的用词。"

    old "It's now attempting to speak like me."
    new "现在说起话来很像我。"

    old "... That's literally what it does."
    new "……就是这样设计的。"

    old "But I'm scared to ask."
    new "但我不敢问。"

    old "I typed: \"Good morning.\"."
    new "我打的是：“早上好。”"

    old "It suggested: \"State your purpose.\"."
    new "它却建议改成：“说明你的来意。”"

    old "PLEASE tell me you didn't send that."
    new "拜托你千万不要把那句话发出去。"

    old "I didn't send it accidentally."
    new "我没有不小心发出去。"

    old "I was conducting a controlled test."
    new "我是为了测试。"

    old "Of what? Do I dare to ask...?"
    new "测试什么？这是能问的吗……？"

    old "Autocorrect behavior."
    new "就是自动纠错的机制。"

    old "I selected a low-risk civilian."
    new "我选了一个低风险的普通人。"

    old "The barista."
    new "咖啡师。"

    old "She stared at me for three seconds."
    new "她瞪了我三秒。"

    old "Then she gave me the coffee without speaking."
    new "然后一句话没说就把咖啡递给我了。"

    old "Em? I'm getting concered now..."
    new "小艾啊……我现在有点担心了……"

    old "You don't test software on people."
    new "你不能拿人当软件的测试对象。"

    old "I disagree."
    new "我不同意。"

    old "People are unpredictable."
    new "人是不可预测的。"

    old "Software should not be."
    new "但软件应该可以。"

    old "You scared her into compliance."
    new "你是吓得她不得不配合你。"

    old "It also attempted to replace \"thank you\" with \"cooperation noted.\"."
    new "它还把“谢谢你”改成“感谢你的配合”了。"

    old "Okay, yeah, it's turning into Detective Autocorrect."
    new "行吧，这是变成警用版自动更正了。"

    old "We need to turn off the learning feature."
    new "得把学习功能关掉。"

    old "Walk me throught it. I promise this will be the last time. 😭"
    new "教教我吧。我保证这是最后一次了。😭"

    old "Open Settings."
    new "打开设置。"

    old "Then go to Keyboard."
    new "然后点键盘。"

    old "Look for something like \"Predictive\" or \"Learn from typing.\""
    new "看看有没有“预测输入”或者“根据输入学习”之类的选项。"

    old "I see \"Predictive Text.\""
    new "我看见一个“预测文本”。"

    old "Turn it off."
    new "把它关掉。"

    old "It's resisting."
    new "它在反抗。"

    old "Emma."
    new "艾玛。"

    old "It's a switch."
    new "那只是个开关。"

    old "I turned it off."
    new "我关掉了。"

    old "It turned itself back on!"
    new "然后它自己又打开了！"

    old "... Okay, now I'm scared."
    new "……好吧，现在我有点害怕了。"

    old "Try again. And don't leave the screen until it stays off."
    new "再试试。然后别划走，确认真的关掉了。"

    old "Off."
    new "关了。"

    old "It's staying off."
    new "没有再打开了。"

    old "Now, clear the learned suggestions."
    new "现在把已经学习的内容都删掉。"

    old "There should be an option like \"Reset Keyboard Dictionary\" or \"Clear personalized data.\""
    new "应该会有“重置键盘词典”或者“清除个性化数据”之类的选项。"

    old "Found it."
    new "找到了。"

    old "It says it will remove words I've taught it."
    new "显示说会删掉我教给它的所有词汇。"

    old "Yep. Wipe its brain."
    new "对。把它的大脑清空。"

    old "You're recommending memory deletion?"
    new "你建议我进行记忆删除？"

    old "I'm recommending you stop your keyboard from issuing warrants!"
    new "我是建议你别让键盘再乱发逮捕令了！"

    old "Okay, okay. Done!"
    new "好吧，好吧。删掉了！"

    old "Test it."
    new "测试一下。"

    old "Type: \"Good morning.\""
    new "输入：“早上好。”"

    old "Good morning."
    new "早上好。"

    old "It didn't accuse anyone."
    new "这次没有指控任何人。"

    old "Huge progress."
    new "巨大的进步。"

    old "Thank you."
    new "谢谢你。"

    old "Cooperation noted."
    new "感谢你的配合。"

    old "EMMAAAAAAAAAAAAAA!"
    new "艾玛！！！！！！"

    old "Habit."
    new "习惯了。"

    old "[mc]. [mc]. I may need your help."
    new "[mc!t]。[mc!t]。我可能需要你的帮助。"

    old "Tech?"
    new "科技？"

    old "Not this time, no."
    new "这次不是了。"

    old "New case."
    new "新案子。"

    old "Multiple shell accounts. Clean paperwork with no obvious leaks."
    new "很多个空壳账户。文件很干净，没有明显的漏洞。"

    old "Hm, nobody's that clean unless they're hiding something."
    new "除非想隐瞒什么，不然没人的文件会这么干净。"

    old "I don't like it."
    new "我有不好的预感。"

    old "Alright. Walk me through what you've tried."
    new "好吧。跟我说说你都试过什么方法了。"

    old "Cross-referenced vendors."
    new "询问了供应商。"

    old "Pulled financial trails."
    new "追踪了财务线索。"

    old "Interrogated two people."
    new "又审讯了两个人。"

    old "They both cried. 😒"
    new "那两个人都哭了。😒"

    old "Did it help?"
    new "有收获吗？"

    old "But I now know one of them is lactose intolerant."
    new "但我现在知道其中一个人乳糖不耐受了。"

    old "Any progress?"
    new "现在案子整体有多少进展了？"

    old "Marginal at best."
    new "可以说几乎没有。"

    old "Okay. If it's that airtight, you might be dealing with professional laundering."
    new "好吧。如果这么滴水不漏的话，你可能碰上了专业的洗钱集团。"

    old "That was my conclusion."
    new "我也是这么想的。"

    old "Look... this might be bigger than what you can legally poke at alone."
    new "我觉得……这案子是你一个人没法用合法手段调查清楚的。"

    old "You could bring in outside analysts."
    new "可以请第三方的分析师帮忙。"

    old "Are you suggesting your agency?"
    new "你是说让你们机构帮忙？"

    old "As a last resort, of course."
    new "当然，只是最后的手段。"

    old "Sicae can audit quietly. No flags. No noise. No whatsoever."
    new "西卡可以悄无声息地做审计。不会有任何动静。"

    old "I don't like relying on them professionally."
    new "我不喜欢让他们插手我的工作。"

    old "I know how they operate. Sicae can complicate things more than they should."
    new "我知道他们是怎么干活的。西卡会把事情搞到没必要得复杂。"

    old "But you called me anyway."
    new "但你还是来找我了。"

    old "Because I trust you."
    new "因为我相信你。"

    old "So... Sicae?"
    new "那……就去找西卡？"

    old "I'll think about it."
    new "我考虑考虑。"

    old "Can we talk in person after your shift?"
    new "你下班之后我们当面聊吧？"

    old "I don't like having work conversations through a screen."
    new "我不喜欢隔着屏幕聊工作。"

    old "Yeah. That works."
    new "好。没问题。"

    old "The park?"
    new "在公园见？"

    old "You still remember it."
    new "你肯定还记得。"

    old "You don't have to tug at my heartstrings."
    new "你没必要撩动我的心弦。"

    old "But, fine."
    new "不过，好吧。"

    old "Let's meet there."
    new "我们在那里见。"

    old "I need to address something."
    new "我要强调一件事。"

    old "That sounds ominous."
    new "听起来不妙。"

    old "Did I commit a crime?"
    new "我犯罪了？"

    old "Not a felony."
    new "不是重罪。"

    old "But don't get comfortable."
    new "但我也不会轻饶你。"

    old "You told Aine I'm working a complicated case."
    new "你跟艾妮说我在处理一件很复杂的案子。"

    old "I didn't tell her anything."
    new "我什么都没跟她说啊。"

    old "That's like... the opposite of details."
    new "根本……没透露一丁点细节。"

    old "It is still information."
    new "那也依然算是走漏风声。"

    old "Also it made her ask questions."
    new "还让她来问我问题了。"

    old "Which made me tired."
    new "搞得我很累。"

    old "She asked {b}you{/b} questions?"
    new "她去问{b}你{/b}问题了？"

    old "Yes!"
    new "是啊！"

    old "She was very polite!"
    new "还问得很礼貌！"

    old "Which somehow makes it harder to escape!"
    new "反而没法糊弄过去！"

    old "I'm sorry, detective."
    new "对不起，警探。"

    old "I was just explaining why I've been MIA."
    new "我只想跟她解释一下我为什么那么忙。"

    old "I know."
    new "我知道。"

    old "And I appreciate it."
    new "我也理解你。"

    old "I just prefer when your explanations don't include me."
    new "我只希望你解释的时候不要提到我。"

    old "... Are you jealous of Aine?"
    new "……你吃艾妮的醋了？"

    old "I'm just protective of my case."
    new "我只是很重视我的案子。"

    old "And protective of you."
    new "也很重视你。"

    old "And slightly annoyed that you are adorable when you play dumb."
    new "还对你装傻时那份可爱有点恼火。"

    old "Aww. So you {b}are{/b} jealous."
    new "啊哈。所以你的确吃醋了。"

    old "Wrong!"
    new "没有！"

    old "Don't try to win this with flirting. 😑"
    new "别以为用调情就能赢过我。😑"

    old "It's my personality."
    new "我性格如此。"

    old "Your personality is a security risk, [mc]!"
    new "你的性格是个安全隐患，[mc!t]！"

    old "So what do you want me to say next time?"
    new "那你想让我以后怎么说呢？"

    old "Say: \"work.\""
    new "说：“因为工作。”"

    old "Say: \"Emma is busy.\"."
    new "说：“艾玛很忙。”"

    old "Do not say: \"complicated case.\""
    new "不要说：“案子很复杂。”"

    old "Got it. Just \"work.\""
    new "知道了。就说“工作”。"

    old "You're really cute when you're bossy, you know that?"
    new "你发号施令的时候真的很可爱，你知道吗？"

    old "I am not cute."
    new "我不可爱。"

    old "I am exhausted."
    new "我是累坏了。"

    old "And I miss you! 😡"
    new "还很想你！😡"

    old "But don't let that distract you."
    new "不过别以为我这么说就代表没关系了。"

    old "This is still a reprimand."
    new "这依旧是对你的批评教育。"

    old "Yes, ma'am! I receive the reprimand."
    new "好的，小姐！我一定改正。"

    old "Good. Now bring coffee."
    new "很好。给我送咖啡来。"

    old "But you don't want anyone coming into your office."
    new "可是你不愿意让人进你的办公室啊。"

    old "I make exceptions, of course."
    new "当然也有例外。"

    old "For you."
    new "比如你。"

    old "The month's almost over. No tech emergencies this time?"
    new "这个月马上结束了。不需要找客服吗？"

    old "Did the world finally stop breaking?"
    new "这个世界终于不再出问题了？"

    old "I adapted."
    new "我习惯了。"

    old "And I've been busy."
    new "而且我很忙。"

    old "You're always busy. 😔"
    new "你总是很忙。😔"

    old "So are you."
    new "你也一样。"

    old "I've been focusing on Francis."
    new "我一直在专心调查弗朗西斯的案子。"

    old "I'm not taking any other cases right now."
    new "我现在已经不管其他的案子了。"

    old "Your boss can't be thrilled about that."
    new "你的上司肯定不会高兴吧。"

    old "He isn't."
    new "的确。"

    old "But I made him a deal."
    new "但我跟他谈好了条件。"

    old "If I close more cases than I did last year, I get the rest of this year to work however I want."
    new "只要我破的案子比去年多，今年剩下的时间我就可以随意安排自己的工作。"

    old "So that's why you leaned on Sicae."
    new "所以你才会找西卡求助。"

    old "One last push. Leave an impression."
    new "最后一搏，留下个好印象。"

    old "If I have to bend my principles to see this through, then I will."
    new "如果我必须违背原则才能搞定这件事，那我也不介意抛弃原则。"

    old "You want him found too, don't you?"
    new "你也想找到他吧？"

    old "Because I do."
    new "反正我很想。"

    old "I want justice for what he did to you."
    new "他对你做的事……必须得到应有的惩罚。"

    old "I want him found."
    new "我想找到他。"

    old "But I don't want you hollowing yourself out to do it."
    new "但我不想你为了这件事把自己掏空。"

    old "Use Sicae if it gives you leverage."
    new "如果西卡能帮上忙，就找他们吧。"

    old "Just don't confuse pressure with progress."
    new "不要把压力当成进展。"

    old "I'm not asking you to be reckless for me."
    new "我不愿意你为了我而鲁莽行事。"

    old "I simply want you to come back intact."
    new "我只想让你平平安安地回来。"

    old "We'll see once I get there."
    new "那种事到时候再说吧。"

    old "Come on, Em..."
    new "拜托，小艾……"

    old "Em, we're starting dinner."
    new "小艾，我们要吃晚饭了。"

    old "Left a plate in the fridge. Top shelf."
    new "冰箱里给你留了一盘。在最顶层。"

    old "You didn't have to."
    new "不用操心我的。"

    old "But thanks."
    new "不过谢谢。"

    old "I wanted to."
    new "我想替你操心。"

    old "I'll eat it when I get home. 🙏"
    new "我回去之后会吃的。🙏"

    old "[mc]. [mc]. I might be late again."
    new "[mc!t]。[mc!t]。我可能又要晚点回去了。"

    old "That's okay."
    new "没事的。"

    old "Do you want me to stay up?"
    new "需要我等你吗？"

    old "No.{#2}"
    new "不用。"

    old "But leave the porch light on for me. 🙏"
    new "不过给我留着门廊的灯吧。🙏"

    old "Always."
    new "当然。"

    old "Love you! 😘"
    new "爱你！😘"

    old "Love you too, Em. 💦"
    new "我也爱你，小艾。💦"

    old "Why that emoji??"
    new "为什么发那个表情？？"

    old "I miss you. It's been a while, you know?"
    new "我很想你。上次都已经很久了吧？"

    old "Mm, [mc]. 🫦"
    new "亲亲，[mc!t]。🫦"

    old "Nevermind, I'm coming home early."
    new "算了，我要早点回家。"

    old "Yes! 😍"
    new "太好了！😍"

    old "No taking photos!"
    new "不准拍照！"

    old "You skipped lunch again, didn't you?"
    new "你又没吃午饭吧？"

    old "I had coffee."
    new "我喝了咖啡。"

    old "Yeah... I'm not exactly innocent either."
    new "好吧……我也干过一样的事。"

    old "So I won't lecture you. Just... try not to make it a habit?"
    new "所以我就不说你了。只是……别养成习惯，好吗？"

    old "Oh. By the way."
    new "噢。对了。"

    old "I found a store in the mall that still sells the stuffed toys I used to have."
    new "我在商场里看到一家店，还在卖我以前的那些毛绒玩具。"

    old "Seriously? They still make those?"
    new "真的吗？居然还有？"

    old "Apparently."
    new "是啊。"

    old "Do you want one?"
    new "你想要吗？"

    old "Say the word. I'll grab it for you."
    new "跟我说就行。我去给你买。"

    old "I'm too old for toys, [mc]."
    new "我已经不是玩玩具的年龄了，[mc!t]。"

    old "And some memories are better left where they belong."
    new "而且有些记忆还是留在原处比较好。"

    old "Still... it was nice seeing them again. 😊"
    new "不过呢……能再见到它们还是挺好的。😊"

    old "But if you change your mind, you know I'm already halfway there."
    new "不过如果你改变主意，我还是会第一时间去给你买。"

    old "I've been thinking about getting a car lately."
    new "我最近一直想买辆车。"

    old "That's... a pretty big thought to just drop like that."
    new "这么大的事……你就这么随便说出来了。"

    old "It's not too sudden, is it?"
    new "也没有很突然吧？"

    old "I'm just tired of either borrowing your truck, or using the company car."
    new "我只是不想再要么借你的车，要么开公司的车了。"

    old "No need to justify. I'm actually proud of you."
    new "不用解释。我真的为你感到骄傲。"

    old "I just want something reliable."
    new "我想要一辆可靠的。"

    old "Quiet."
    new "安静的。"

    old "And difficult to break."
    new "怎么都不会坏的。"

    old "So... basically you."
    new "也就是你呗。"

    old "Inaccurate comparison!"
    new "非常不准确的比喻！"

    old "But acceptable."
    new "不过可以接受。"

    old "Want me to come with you when you look?"
    new "我跟你一起去挑？"

    old "Please."
    new "拜托你了。"

    old "I got you. Just say when."
    new "没问题。到时候跟我说就行。"

    old "[mc]. [mc]. I don't think I'll make it to dinner tonight. Go ahead without me, alright?"
    new "[mc!t]。[mc!t]。我今晚可能赶不及吃晚饭了。你先吃吧，不用等我了。"

    old "I'll save you a plate."
    new "我给你留一盘。"

    old "Thanks. I love you."
    new "谢谢。我爱你。"

    old "Love you too, Em."
    new "我也爱你，小艾。"

    old "Thanks."
    new "谢谢。"

    old "Yes? Call me if it's an emergency."
    new "怎么了？有急事的话直接给我打电话。"

    old "No, nothing like that."
    new "不，不是急事。"

    old "Are you at the hospital?"
    new "你在医院吗？"

    old "That was the plan."
    new "本来打算去的。"

    old "But Elaine just called. They picked up Leah's mother."
    new "但是伊莱恩刚刚打来电话，说找到了莉娅的妈妈。"

    old "They talking to her?"
    new "现在正在向她问话吗？"

    old "Yeah. Elaine's running the interview."
    new "是的。伊莱恩正在问话。"

    old "Got it. I'm handling some paperwork at the office."
    new "明白了。我准备去办公室处理文件。"

    old "I'll swing by the hospital later if you're still around."
    new "如果到时候你还在附近的话，之后我也去医院一趟。"



    #MOON

    old "Hey. I've been looking around. Where are you?"
    new "嘿。找你很久了。你在哪？"

    old "Location update:"
    new "地点汇报："

    old "— Near the old rail platform"
    new "——靠近旧铁轨站台"

    old "— West side"
    new "——西侧"

    old "— Covered"
    new "——有掩护"

    old "... Covered?"
    new "……掩护？"

    old "Affirmative."
    new "确定。"

    old "Windbreak. Partial shade."
    new "防风。部分遮阳。"

    old "Right. Uh... You waiting for someone?"
    new "好吧。呃……你在等人吗？"

    old "Negative."
    new "否定。"

    old "Status:"
    new "状态汇报："

    old "— Sitting"
    new "——坐着"

    old "— Observing foot traffic"
    new "——观察人流"

    old "— Lollipop and hot chocolate acquired"
    new "——已拿到棒棒糖和热可可"

    old "Huh..."
    new "嚯……"

    old "Didn't know you text this way. It's like you're filing a report."
    new "都不知道你会这样发短信。跟在写报告一样。"

    old "LOL. 😅"
    new "哈哈。😅"

    old "Correction."
    new "订正。"

    old "This is concise."
    new "这样很简洁。"

    old "Most people don't list bullet points like this, you know?"
    new "大多数人不会像这样列出要点的。"

    old "People waste time."
    new "他们在浪费时间。"

    old "Fair enough. Can you just... say where exactly you are?"
    new "行吧。你能……直接说清楚你在哪吗？"

    old "Stand by."
    new "稍等。"

    old "Refining."
    new "精确定位中。"

    old "Bench. Third from the left."
    new "长椅。左数第三个。"

    old "Blue paint. Chipped."
    new "蓝色。掉漆。"

    old "You'll see me before I see you."
    new "你会在我看到你之前先看到我。"

    old "That's... not ominous at all."
    new "这……可真是一点都不吓人。"

    old "Noted."
    new "明白。"

    old "Intent was efficiency."
    new "本意是为了高效。"

    old "I think I'm close."
    new "我应该快到了。"

    old "Copy."
    new "收到。"

    old "I have eyes on you."
    new "我盯上你了。"

    old "... You didn't have to say it like that."
    new "……没必要用这种说法吧。"

    old "Okay. Found you."
    new "好。看见你了。"

    old "I made it home, Capt."
    new "我到家了，队长。"

    old "Status check:"
    new "状态汇报："

    old "— You: upright"
    new "——你：站着"

    old "— Mood: stable"
    new "——心情：稳定"

    old "— Injuries: none observed"
    new "——受伤：未发现"

    old "You didn't observe me getting home."
    new "你根本没有看到我回家。"

    old "Inference."
    new "推测。"

    old "Your gait was steady when we separated."
    new "我们分开时你的步伐很稳。"

    old "You really don't turn this off, do you? 😕"
    new "你的这个模式真的关不掉吗？😕"

    old "But I can... deprioritize."
    new "但我可以……降低优先级。"

    old "That sounds reassuring. I think."
    new "那我多少能放心点了。大概。"

    old "After-Action Summary:"
    new "事后总结："

    old "— Time spent: productive"
    new "——花费的时间：高效"

    old "— Environment: acceptable"
    new "——环境：可接受"

    old "— Company:"
    new "——陪伴："

    old "   • yours"
    new "   • 是你"

    old "   • unexpectedly... good"
    new "   • 出乎意料地……好"

    old "\"Unexpectedly?\""
    new "“出乎意料”？"

    old "Clarification."
    new "澄清。"

    old "Expectation was high."
    new "预期很高。"

    old "Outcome exceeded baseline."
    new "结果超越了基准线。"

    old "I'll take that as a compliment."
    new "我就当你是在夸我吧。"

    old "You should."
    new "没错。"

    old "I don't inflate reports."
    new "我不会在报告里夸大事实。"

    old "Noted. Anything else in your report?"
    new "明白了。还有什么要报告的？"

    old "One addendum."
    new "补充一点。"

    old "— You laughed more than usual."
    new "——你笑得比平时多。"

    old "Is that bad?"
    new "那是坏事吗？"

    old "Assessment: positive deviation."
    new "评估：积极的偏差。"

    old "Low risk. Acceptable."
    new "低风险。可接受。"

    old "Guess it'll take some time to get used to this."
    new "看来要花上一段时间才能习惯你这样。"

    old "Anyway, stay safe."
    new "总之，你保重。"

    old "Say hi to Jess for me."
    new "替我向婕斯问好。"

    old "I will."
    new "我会的。"

    old "So, uh... Capt. I heard you know I'm not celebrating my birthday this year."
    new "那个……队长。我听说你已经知道我今天不庆祝生日了。"

    old "Intel source was reliable."
    new "情报来源可靠。"

    old "What? Reliable?"
    new "什么？可靠？"

    old "High confidence."
    new "可信度高。"

    old "Motivation assessment: predictable."
    new "动机评估：可预测。"

    old "Predictable?"
    new "可预测？"

    old "You planned the \"I don't want anything\" approach to get me alone."
    new "你想用“我什么都不要”的方法把我单独约出来。"

    old "Birthday bypass strategy."
    new "生日迂回策略。"

    old "Objective: intimacy."
    new "目标：亲密。"

    old "How the hell do you always figure this out so fast?"
    new "你为啥能这么快就看出来？"

    old "Pattern recognition."
    new "模式识别。"

    old "You made the same face every year in the past."
    new "你过去每年都是同样的表情。"

    old "I have a face?"
    new "我有表情吗？"

    old "\"Seduction face.\""
    new "“勾引的表情。”"

    old "Okay, first of all, rude."
    new "好吧，首先，很无礼。"

    old "Second of all... you're not wrong."
    new "其次……你说得没错。"

    old "Already complied."
    new "已经配合了。"

    old "Mission: successful."
    new "任务：成功。"

    old "So you're not mad about it?"
    new "所以你不生气吗？"

    old "I liked watching you try."
    new "我喜欢看你努力的样子。"

    old "And I liked what followed."
    new "我也喜欢接下来的事。"

    old "I feel extremely seen right now."
    new "我现在感觉完全被看穿了。"

    old "Not gonna lie..."
    new "说实话……"

    old "Best birthday I've ever had."
    new "这是我这辈子最棒的生日礼物。"

    old "I keep looking at that photo, and I recall our past."
    new "我一直在看那张照片，然后想起我们的过去。"

    old "It's strange."
    new "挺奇怪。"

    old "But I don't remember feeling so alive like how it is with us now."
    new "可是我不记得当时的感觉有现在这么强烈。"

    old "Like you could see all the way through me."
    new "就好像你可以看穿我一样。"

    old "I did."
    new "我是可以。"

    old "I always do."
    new "我总是可以。"

    old "Please keep looking at me like that."
    new "请一定要继续那样看我。"

    old "Disregard previous transmission."
    new "忽略之前的通讯。"

    old "Emotional clarity temporarily compromised."
    new "情感清晰度暂时受损。"

    old "Post-operation condition: elevated."
    new "行动后状况：兴奋。"

    old "This is normal."
    new "这很正常。"

    old "Contained."
    new "克制。"

    old "Under control."
    new "在控制之中。"

    old "You okay there, Captain?"
    new "你没事吧，队长？"

    old "Affirmative, Commander."
    new "确定，指挥官。"

    old "Status restored."
    new "状态已恢复。"

    old "However..."
    new "不过……"

    old "Recommending same strategy next year."
    new "推荐明年采取同样策略。"

    old "I'll be ready."
    new "我会准备好的。"

    old "Then I'd like you to at least pretend to have no idea. 😑"
    new "那我希望你至少可以假装不知道。😑"

    old "... Wow."
    new "……哇。"

    old "Now that ain't fair. Taking that photo without me."
    new "这不公平。拍照片不带上我。"

    old "You look incredible, Moon."
    new "你真漂亮，月。"

    old "If this is how my secretary clocks in, I might need a minute to recover."
    new "我的秘书要是这样来上班，我得每天都花点先缓缓。"

    old "Observation:"
    new "观察结果："

    old "You're flustered."
    new "你慌神了。"

    old "A little."
    new "有一点。"

    old "Really damn happy you're working with me now."
    new "你现在跟着我干了，我真的是很开心。"

    old "New objective logged:"
    new "新目标已记录："

    old "— stay by your side"
    new "——陪在你身边"

    old "— permanent assignment"
    new "——永久任务"

    old "No transfer requests."
    new "不得转岗。"

    old "Permanent, huh?"
    new "永久，是吧？"

    old "Forever is the plan."
    new "永远都不走。"

    old "I love you, Moon. Past and present."
    new "我爱你，月。过去和现在都爱。"

    old "You froze again? I thought you got past that already?"
    new "你又死机了？我还以为你已经克服那个问题了？"

    old "I did not freeze."
    new "我没有死机。"

    old "I was..."
    new "我是在……"

    old "Reassessing."
    new "重新评估。"

    old "But you froze..."
    new "但你就是死机了……"

    old "i dnt freeze."
    new "我bbbbuhui死机"

    old "I jus"
    new "我只"

    old "u knw what i mean."
    new "ni懂我yis"

    old "Okay, okay. I'll stop pushing. Looks like I broke you already."
    new "好吧，好吧，我不逗你了。看来我已经把你弄坏了。"

    old "Status update:"
    new "状态汇报："

    old "— You didn't realize you were smiling during the meeting, Cap"
    new "——你没有发现你开会的时候在笑，队长"

    old "— It stuck with me longer than it should have"
    new "——我心里一直在想这件事"

    old "— I don't think I ever stopped choosing you"
    new "——我不管怎么样总是会来找你"

    old "That's not how the format works, Commander."
    new "不是这种格式，指挥官。"

    old "I think it works perfectly, though."
    new "但我觉得这样完全没问题啊。"

    old "Assessment:"
    new "评估："

    old "— reckless"
    new "——鲁莽"

    old "— imprecise"
    new "——不精确"

    old "— effective"
    new "——有效"

    old "Effective?"
    new "有效？"

    old "Heart rate elevated."
    new "心率上升了。"

    old "So yes."
    new "所以有效。"

    old "One correction."
    new "纠正一点。"

    old "You forgot the conclusion line."
    new "你忘了总结。"

    old "Conclusion:"
    new "总结："

    old "— You're mine, Moon."
    new "——你是我的，月。"

    old "Conclusion acknowledged."
    new "总结已确认。"

    old "And reciprocated."
    new "并且已回应。"

    old "Capt. I need you."
    new "队长。我需要你。"

    old "Aine and I blew up."
    new "我和艾妮吵架了。"

    old "Expansion's moving, but she thinks I cut her out. Again."
    new "扩张计划开始了，但她觉得我又一次把她排除在外。"

    old "Give me your decision. In one line."
    new "用一句话告诉我你的决定。"

    old "We proceed with Phase One expansion this week."
    new "我们这周开始推进第一阶段的扩张。"

    old "I'm not freezing the charity because we can't agree."
    new "我不会因为没法达成一致就搁置慈善事业。"

    old "That's defensible."
    new "可以理解。"

    old "Gridlock kills momentum. Momentum is food, medicine, beds."
    new "僵局会扼杀势头。势头就代表食物、药品和床位。"

    old "I need you to do something."
    new "我需要你做件事。"

    old "Lock the expansion tasks in and push them forward."
    new "确定好扩张任务，大力推进。"

    old "But do it clean. Paper trail, approvals, donors. No mess."
    new "但是要干净利落。文件记录、审批、捐赠人都要有。别搞得一团糟。"

    old "Action items:"
    new "行动事项："

    old "— Confirm Phase One scope + budget ceiling"
    new "——确认第一阶段的范围和预算上限"

    old "— Freeze Phase Two until joint sign-off"
    new "——冻结第二阶段，直到两方都签字批准"

    old "— Draft comms for staff + donors: \"time-sensitive rollout\""
    new "——为员工和捐赠人起草备忘录：“尽快落实”"

    old "— Schedule partner briefing with Aine within 24 hours"
    new "——在24小时内安排与艾妮的合作伙伴简报会"

    old "You're really taking my side?"
    new "你真要站在我这边？"

    old "I'm taking the charity's side."
    new "我站在慈善这边。"

    old "Your call keeps the mission alive."
    new "你的决定让任务能进行下去。"

    old "But your method is bleeding trust."
    new "可是你的方法会损害信任。"

    old "... Yeah. I feel bad about it, but I'm thinking about our people."
    new "……是啊。我对此感到很抱歉，但我是在为我们的人考虑。"

    old "What do I say to her?"
    new "我该怎么跟她说？"

    old "Say this:"
    new "这么说："

    old "— \"I acted because people are waiting.\""
    new "——“我做出行动是因为大家都在等。”"

    old "— \"I should've looped you in before it landed.\""
    new "——“我本应该在事情发生前让你知道。”"

    old "— \"Phase Two doesn't move without you.\""
    new "——“第二阶段没有你的批准不会进行。”"

    old "No sarcasm. No winning the argument."
    new "不要讽刺。不要争论谁对谁错。"

    old "She said I don't see her anymore."
    new "她说我眼里没有她了。"

    old "Stuck in me more than it should."
    new "这话让我很在意。"

    old "That's not about the expansion, but about being outpaced by your life."
    new "那不是因为扩张，而是因为你的节奏太快了，她跟不上。"

    old "Give her a lane. Give her visibility. Give her a \"first call\" rule."
    new "给她一条路。给她知情权。给她定一个“优先告知”的规矩。"

    old "First call rule?"
    new "优先告知？"

    old "If it's urgent, you act."
    new "如果很紧急，你就先行动。"

    old "If it's not urgent, she hears it from you before the world does."
    new "如果不紧急，就保证在告诉别人之前，第一个先告诉她。"

    old "Partnership, so to say."
    new "就是所谓的合作关系。"

    old "Do the paperwork. I'll handle Aine."
    new "去弄文件吧。我来处理艾妮。"

    old "Wilco."
    new "明白。"

    old "And Commander?"
    new "还有，指挥官。"

    old "Next time you feel the storm coming, don't wait for lightning."
    new "下次你再感到风暴要来的时候，不要等闪电出现。"

    old "Brief your partner first."
    new "先通知你的搭档。"

    old "Hey, Capt. About the sword."
    new "队长。关于那把刀。"

    old "What about it?"
    new "怎么了？"

    old "Sometimes when I hold it, it feels somewhat wrong."
    new "有时候我把它拿在手里，会觉得有点不对劲。"

    old "It's not heavy. But it's as if it's alive."
    new "并不重。但感觉它像是活的一样。"

    old "Alive?"
    new "活的？"

    old "I hear things."
    new "我会听到一些声音。"

    old "It's not clear. Like voices under water."
    new "听不清楚。就像水下的声音。"

    old "It only happens when I'm alone."
    new "只有我一个人的时候才会这样。"

    old "Is it cursed or something?"
    new "难道那上面有诅咒？"

    old "Because if it is, I'd really like a heads up before I even think of unsheathing it."
    new "如果真有的话，我希望在我拔刀之前能先把情况搞清楚。"

    old "Not cursed."
    new "没有诅咒。"

    old "That pause didn't help."
    new "你隔了一段时间才回让我根本没法放心。"

    old "It remembers you."
    new "它还记得你。"

    old "Remembers how?"
    new "怎么可能？"

    old "You used it before."
    new "你曾经用过它。"

    old "Not in this life."
    new "虽然不是在这一世。"

    old "But it was always yours."
    new "但它一直都属于你。"

    old "That's not helping either. I know it's mine. But this thing doesn't speak to me centuries ago."
    new "这也不解决问题。我知道它是我的。但这东西几个世纪前并不会跟我说话。"

    old "I eventually passed it on before I took my life, but it simply went back to me."
    new "我自杀前把它送给了别人，但它还是回到了我手里。"

    old "But even then, it never listened to me the way it listens to you, now that I have Sora's memories."
    new "现在我有了空的记忆，我很清楚，即便是在那时候，它聆听我的方式也和聆听你的方式完全不一样。"

    old "Listens?"
    new "聆听？"

    old "Responds."
    new "回应。"

    old "It's waiting."
    new "它在等待。"

    old "Waiting for what?"
    new "等待什么？"

    old "For you to reach back to it."
    new "等你回应它。"

    old "Moon..."
    new "月……"

    old "You're not in danger."
    new "你没有遇上危险。"

    old "If the voices get louder, tell me."
    new "如果声音变大，就告诉我。"

    old "You've dealt with this before?"
    new "你曾经遇见过这种事？"

    old "I have."
    new "是的。"

    old "And you trusted me then."
    new "那时候你就相信过我。"

    old "You can trust me now."
    new "你现在也可以相信我。"

    old "I'll keep it close."
    new "我会好好保管它。"



    #GWEN

    old "Heard you're back at work already."
    new "听说你已经回去工作了。"

    old "You do realize you were kidnapped, right?"
    new "你难道不知道自己刚被绑架吗？"

    old "You and Aine..."
    new "你和艾妮……"

    old "I'm fine, Gwen. Can't stay on bedrest forever."
    new "我没事，格温。总不能一直在床上躺着。"

    old "Yeah? Looks more like you're trying to speedrun a relapse."
    new "是吗？我倒觉得你更想早点再回床上躺着去。"

    old "You don't have to prove you're unbreakable. Nobody's giving out medals for it."
    new "你没必要证明自己是铁打的。又没人会给你发奖牌。"

    old "I'm not proving anything. Just doing my job."
    new "我没想证明什么。只是在做自己的工作。"

    old "Uh-huh. Sure. Anyway..."
    new "行吧。随你。对了……"

    old "Have you had lunch?"
    new "你吃午饭了吗？"

    old "Define lunch."
    new "先定义一下什么叫午饭。"

    old "No.{#3}"
    new "不要。"

    old "I'm not playing that game with you."
    new "我才不跟你玩这一套。"

    old "Stay where you are. I'm coming to get you."
    new "你哪儿都别去。我去找你。"

    old "Gwen..."
    new "格温……"

    old "[mc]. You nearly died."
    new "[mc!t]。你差点就死了。"

    old "You're eating a real meal today not whatever \"technically counts\" as lunch in that disaster of a food pyramid you call a cup of coffee."
    new "你今天必须好好吃顿饭，绝对不能随便喝杯咖啡之后就说你“也算是吃了”。"

    old "Be outside in fifteen."
    new "十五分钟之后在外面等我。"

    old "... Yes, ma'am."
    new "……好的，小姐。"

    old "Freya's with you, right? Bring her. We'll feed both of you."
    new "芙蕾雅跟你在一块吧？把她也带上。我们一起吃。"

    old "Then you better take us to a Korean resto. She's been craving kimchi stew like a pregnant woman."
    new "那你带我们去一家韩国餐厅吧。她一直想吃泡菜汤，跟怀孕了一样。"

    old "You sure you haven't accidentally started a family with her yet? 😏"
    new "你确定你没有真的把她给搞怀孕吗？😏"

    old "WHAT? NO?!"
    new "什么？没有啊？！"

    old "Emergency question."
    new "紧急问题。"

    old "Black skirt or jeans?"
    new "黑裙子还是牛仔裤？"

    old "Skirt. No contest."
    new "裙子。毫无疑问。"

    old "It fits. But if anyone stares, that's on YOU. 😉"
    new "很合适。不过如果有人盯着看，那可就怪你了。😉"

    old "What if {b}I{/b} wanna look?"
    new "要是{b}我{/b}想看呢？"

    old "Then you better start running, my love. Because I won't be gentle when I catch you."
    new "那你最好动作快点了，我的爱人。因为我抓到你的时候可不会手下留情。"

    old "Alright, alright..."
    new "好吧，好吧……"

    old "Not exactly my style, but..."
    new "不太符合我的风格，不过……"

    old "There. You happy now?"
    new "给。满意了？"

    old "Holy peaches, Gwen. This is... wow. Smoking hot."
    new "我的老天，格温。这也太……哇。太色了。"

    old "Thinking about it... you never actually send me stuff like this. Why now?"
    new "仔细想想……你从来没给我发给这种东西。怎么突然来了兴致？"

    old "For the record, I prefer barging into your room and shoving my ass in your face directly."
    new "事先声明，我更喜欢冲进你的房间，然后直接一屁股坐到你脸上。"

    old "But just this once, I will indulge you. 😁"
    new "但就这一次，我还是满足一下你吧。😁"

    old "Gwen... you don't go out of character for no reason."
    new "格温……你可不会无缘无故做不想做的事。"

    old "Is there something I should know?"
    new "你有事瞒着我吗？"

    old "Yeah. But like I said, if we're talking, it's face-to-face. Not over text. Not over calls."
    new "有。但我说过了，要聊的话，就当面聊。不能发短信，也不能打电话。"

    old "Lunch?"
    new "去吃午饭？"

    old "Oh hell yeah. I'm not turning that down."
    new "当然了。我可不会拒绝。"

    old "You look so... sad! ROFL! 🤣"
    new "你看着也太……伤心了！我要笑死了！🤣"

    old "I {b}am{/b} sad! Stop laughing at me!"
    new "我就是很伤心啊！别笑我了！"

    old "There, there... It's not like I'm disappearing forever."
    new "好啦，好啦……又不是以后永远见不到我了。"

    old "\"I don't know when I can come back.\" What do you think I'm supposed to feel?"
    new "“我不知道我什么时候能回来。”你觉得我听完这句话该怎么想？"

    old "It's still three months away. We've got time, you know?"
    new "还有三个月呢。还有时间呀。"

    old "And hey, I'll still be here for your birthday."
    new "而且呢，我也能陪你过生日啊。"

    old "Fair... 😔"
    new "好吧……😔"

    old "I'm at the mall right now."
    new "我现在在商场。"

    old "Birthday boy, tell me if there's anything you want."
    new "大寿星，跟我说说你想要什么。"

    old "I don't know, Gwen."
    new "我不知道，格温。"

    old "I don't really feel like celebrating my birthdays anymore."
    new "我已经不想庆祝生日了。"

    old "The fuck? 🤨"
    new "说什么胡话呢？🤨"

    old "Alright then. Go wait in my room."
    new "行吧。去我房间里等着。"

    old "If you're not celebrating, I'll do it for you."
    new "你不想庆祝的话，我就帮你庆祝。"

    old "Don't argue. Just be there."
    new "不准还嘴。你去就是了。"

    old "Gwen - 1, [mc] - 0."
    new "格温1分，[mc!t]0分。"

    old "Looks like your master plan didn't work. Next time, maybe don't tell me you \"don't feel like celebrating.\""
    new "看来你的宏伟计划没有成功。下次试试别跟我说你“不想庆祝”。"

    old "Damn it, Gwen."
    new "妈的，格温。"

    old "Six rounds was insane. You didn't even let me breathe between them. 😫"
    new "做六次真的是疯了。你甚至都不让我歇歇。😫"

    old "Birthday cardio. You're welcome."
    new "生日特别有氧运动。不用客气。"

    old "Now stop whining. You needed it more than you think. 😜"
    new "别哼唧了。你明明就很需要。😜"

    old "Lunch! Come out! 😠"
    new "吃午饭了！出来！😠"

    old "Wait, what? Where are you?"
    new "什么？你在哪？"

    old "Where do you think?"
    new "你觉得呢？"

    old "Oh shit! Hold on! Clocking out!"
    new "我操！等一下！马上下班！"

    old "Is this really it? 😭"
    new "真的就这么结束了吗？😭"

    old "Hey... don't talk like I'm not coming back."
    new "喂……别说得好像我不会回来了似的。"

    old "I promised I'll be there for your next birthday."
    new "我答应过我会陪你过下一个生日的。"

    old "I hate that this is the last thing I see of you."
    new "你在我眼里的最后一幕居然是这样的。好烦。"

    old "Hey, stop. Wipe your tears, okay?"
    new "行了。把眼泪擦干净。"

    old "I'm not crying."
    new "我没哭。"

    old "You are. I can literally see you from the window."
    new "就是哭了。我透过窗户都能看到。"

    old "Where?"
    new "在哪儿？"

    old "Wipe them off."
    new "快擦掉。"

    old "Good boy."
    new "真乖。"

    old "I told you: do something meaningful while I'm gone. And you promised."
    new "我跟你说了，我不在的时候，你要做些有意义的事情。你也跟我保证过了。"

    old "So when I get back, something better damn well be waiting for me."
    new "所以我回来的时候，你最好给我准备点好东西。"

    old "Yeah. I know what I need to do. I'll get it done before you come back. Promise."
    new "嗯。我知道我该做什么。我会在你回来之前做完的。我保证。"

    old "Make me proud."
    new "让我以你为傲吧。"

    old "Alright, the crew's already yelling at me. I need to turn my phone off."
    new "好了，乘务员们已经要对我发脾气了。我得把手机关了。"

    old "I'll see you later, [mc]. I love you. 😘"
    new "再见，[mc!t]。我爱你。😘"

    old "I love you too. See you later... 😔"
    new "我也爱你。再见……😔"

    old "[mc]. Just got settled in, so I figured I'd do a quick check-in."
    new "[mc!t]。我刚安顿好。想着简单聊两句。"

    old "Did you get any sleep?"
    new "你有好好睡觉吗？"

    old "Don't lie to me. I'll know."
    new "别骗我。我看得出来。"

    old "Trying."
    new "在努力了。"

    old "Not exactly winning at it."
    new "但是没什么效果。"

    old "Try again."
    new "继续努力。"

    old "Or never mind."
    new "算了。"

    old "I'll just call you."
    new "我给你打电话。"

    old "Also, drink some water."
    new "还有，多喝点水。"

    old "I won't be able to text every day."
    new "我没法每天都给你发消息。"

    old "But I'm still here."
    new "但我会一直在。"

    old "Okay?"
    new "好吗？"

    old "Okay... 🥲"
    new "好……🥲"

    old "Holy!"
    new "天啊！"

    old "Saw your charity post!"
    new "看到你那个慈善机构的帖子了！"

    old "Keep going."
    new "继续加油。"

    old "Still remember your promise, yeah?"
    new "还记得你的承诺吧？"

    old "Yes, boss!"
    new "记得，老大！"

    old "Don't wait on me."
    new "别那样叫我。"

    old "Aye!"
    new "是！"

    old "Hey, Gwen. Just checking in."
    new "格温，想问问你的情况。"

    old "Kinda miss hearing from you."
    new "好久没收到你的消息了。"

    old "Hope you're eating, sleeping, and... you know. Surviving."
    new "希望你吃得好，睡得好，反正就……过得好呗。"

    old "Shit! Sorry! I completely missed this."
    new "操！对不起！我没看见。"

    old "It's been nonstop. Barely had a second to check my phone."
    new "事情太多了。根本没时间看手机。"

    old "And don't you dare throw that concern back at me."
    new "而且你别想把我变成受关心的人。"

    old "YOU eat. YOU sleep."
    new "{b}你{/b}要吃好。{b}你{/b}要睡好。"

    old "You hear me?"
    new "听见了没？"

    old "I am."
    new "我有在照做。"

    old "... Mostly."
    new "……大部分时候在吧。"

    old "Call me. I have some time left before the next meeting."
    new "给我打电话。离下个会议还有一会儿。"

    old "Saw something today that reminded me of you."
    new "今天看到一个东西，让我想到了你。"

    old "Some girl at a café was humming off-key and still looked confident as hell."
    new "咖啡馆里有个女生唱歌跑调，但依然很自信。"

    old "Made me laugh. You would've rolled your eyes so hard at her. 😂"
    new "我一下就笑了出来。你肯定会对她狠狠翻白眼的。😂"

    old "I absolutely would have."
    new "我肯定会的。"

    old "But I respect the confidence."
    new "但我佩服她的自信。"

    old "Glad I still live rent-free in your head."
    new "看来你脑子里依旧全是我。好事。"

    old "You do."
    new "是啊。"

    old "You do... 😔"
    new "全是你……😔"

    old "You holding up okay?"
    new "最近你过得怎么样？"

    old "Not trying to bug you. I've just... been thinking about you a lot lately."
    new "不是想烦你。我就是……最近很想你。"

    old "I don't know what you did to me, but I feel stupidly lonely without you."
    new "不知道你对我做了什么，不过没了你，我感觉特别孤独。"

    old "…even with the other girls around."
    new "……哪怕其他姑娘们都在我身边。"

    old "[mc]? Why aren't you answering my calls?"
    new "[mc!t]？你为什么不接我的电话？"

    old "Fuck me..."
    new "我真是操了……"

    old "Hey."
    new "嘿。"

    old "I miss you too. Don't spiral on me."
    new "我也很想你。你冷静点，别失控了。"

    old "And yes, when I get back, I'll absolutely fuck you senseless."
    new "而且呢，我回去之后，绝对会让你狠狠操的。"

    old "Calling."
    new "马上给你打电话。"

    old "Why isn't Aine replying to my text messages?"
    new "为什么艾妮不回复我的消息？"

    old "We kind of blew up..."
    new "我们算是……吵架了……"

    old "That \"kind of\" is doing some heavy lifting there. LMAO! 🤣"
    new "“算是”这个词用得很妙。哈哈哈！🤣"

    old "My love still breathing?"
    new "我的爱人还活着吗？"

    old "Last I checked, yeah. Unfortunately alive. 😒"
    new "很不幸，还活着。😒"

    old "But you barely text, so ask me again in a week."
    new "但你基本都不给我发消息，所以再过一星期可能就不一定了。"

    old "Don't you fucking dare."
    new "不要开这种玩笑。"

    old "I miss you, Gwen. Come home soon."
    new "我很想你，格温。早点回家吧。"

    old "Sorry for the late reply, [mc]."
    new "抱歉回复晚了，[mc!t]。"

    old "But I'm planning to be back for your birthday."
    new "我打算回去给你过生日。"

    old "That's a promise. At least to you."
    new "我保证。至少能对你保证。"

    old "... Yeah."
    new "……好。"

    old "That's enough to get me through."
    new "这就足够我撑下去了。"




    #SHU

    old "ah fck! THAT was from my private stash."
    new "操了！那是我的私人珍藏"

    old "how do u unsend"
    new "怎么撤回啊"

    old "UNSEND!!!"
    new "撤回！！！"

    old "Why the hell do you have pics of your naked femboy ass on your phone?"
    new "你他妈为什么会在自己手机里存一张把你那男娘小屁股全露出来的照片？"

    old "bcuz i'm sexy af and the ladies deserve a sneak peek at the Shuper goods."
    new "因为我色疯了，而姑娘们需要瞻仰修神的美貌。"

    old "... You did not just say that."
    new "……很难想象人类可以说出这种话。"

    old "no, dumbass."
    new "我当然没有说，傻逼。"

    old "i {b}texted{/b} it. duh."
    new "我是{b}打字{/b}。"




    #JUNE

    old "Come outside."
    new "出来。"

    old "what? i'm not even home"
    new "什么？我根本不在家啊"

    old "You are."
    new "你在家。"

    old "I can see that busted-ass toupee from the window."
    new "我在窗户外面都能看见你那张更年期提前的脸。"

    old "bro"
    new "哥们"

    old "you could've just called me"
    new "你给我打个电话不行吗"

    old "or knocked"
    new "或者敲门"

    old "there's literally a door"
    new "门就在门口"

    old "you blind fuck"
    new "你个瞎逼"

    old "If you don't wanna see me just say so. I'll dip."
    new "你不想见我的话直说就行。我立马走人。"

    old "oh get the hell outta here"
    new "你他妈滚吧"

    old "you really pulled the guilt card on me?"
    new "不见你又成我的错了是不？"

    old "See?"
    new "看吧？"

    old "Wasn't that hard."
    new "没那么难。"

    old "yeah yeah yeah"
    new "行行行"

    old "you looked like shit warmed up"
    new "你看着就像加热过的狗屎"

    old "but good to see you too"
    new "不过我也很高兴见到你"

    old "Hello, valued customer. We've been trying to reach you about your car's extended warranty. This is your {b}final{/b} notice."
    new "亲爱的客户，您好。我们一直试图联系您，讨论给您的汽车延长保修的事宜。这是您的{b}最终{/b}通知。"

    old "if shu's there, go fuck yourselves"
    new "要是修也在，你们俩给我一起滚蛋"

    old "what the hell was that?"
    new "你他妈搞什么飞机？"

    old "i work with DFCS"
    new "我是在DFCS上班"

    old "not an engineer, you walking protein shake."
    new "又不是工程师，你个傻大个"

    old "You can work DFCS {b}and{/b} be an engineer, bite-size."
    new "你可以既在DFCS工作{b}又{/b}当工程师，小矮子。"

    old "ugh"
    new "唉"

    old "whatever"
    new "随便吧"

    old "i really don't wanna have another dumb, circular fight with you two"
    new "我真的不想再跟你们两个傻逼争些没用的东西"

    old "You say that like you don't sprint straight into it every time."
    new "你照样每次都上赶着参加啊。"

    old "hey got a situation"
    new "有情况"

    old "What's up?"
    new "怎么了？"

    old "leah won't talk"
    new "莉娅不肯说话"

    old "not to me not to dr. park"
    new "不跟我说，也不跟帕克医生说"

    old "not to staff"
    new "也不对医院员工说"

    old "she just sits in her room"
    new "她就坐在房间里"

    old "Since when?"
    new "什么时候开始的？"

    old "since this morning"
    new "今天早上"

    old "hasn't said a word to anyone"
    new "一个字都没说过"

    old "she keeps asking for emma"
    new "一直要找艾玛"

    old "Keeps asking? Thought she wasn't talking."
    new "一直找艾玛？她不是不肯说话吗？"

    old "she wrote it down"
    new "她是写下来的"

    old "i need emma here, [mc]"
    new "快让艾玛过来，[mc!t]"




    #SKY

    old "Sky."
    new "斯凯。"

    old "About our practice."
    new "说一下我们的练习的事。"

    old "told u already. call."
    new "跟你说了。打电话。"

    old "hate txt. 😑"
    new "很烦发短信。😑"

    old "I know. I'm in the middle of a meeting right now."
    new "我知道。我现在正在开会。"

    old "Just wanted to give you a heads-up about later."
    new "只是想提前跟你说一下。"

    old "call after."
    new "那就待会再打电话。"

    old "... Alright."
    new "……好吧。"

    old "[mc]!"
    new "[mc!t]！"

    old "???"
    new "？？？"

    old "The hell?"
    new "太阳打西边出来了？"

    old "Since when do you text?"
    new "你居然会发短信？"

    old "ik ik"
    new "我懂"

    old "but had 2 say smth"
    new "只是有事要说"

    old "About?"
    new "说什么？"    
    
    old "dinner!!"
    new "晚饭的事！！"

    old "when mom asked how it went"
    new "妈妈问情况如何"

    old "thought she meant US"
    new "还以为是在问我们的事"

    old "Wait, what?"
    new "什么？"

    old "was SWEATING"
    new "流汗了都"

    old "full panic mode"
    new "吓死我"

    old "u didnt notice???"
    new "你没发现？？？"

    old "I thought you were just tired."
    new "我还以为你只是累了。"

    old "was"
    new "是累"

    old "but also dying inside"
    new "但心里也怕得很"

    old "she kept looking @ me"
    new "她一直看我"

    old "then @ u"
    new "然后看你"

    old "then back @ me"
    new "然后又看我"

    old "You're overthinking it, Sky."
    new "你想多了，斯凯。"

    old "AM I THO"
    new "真想多了吗"

    old "felt like she KNEW"
    new "感觉她知道了"

    old "She was probably just wondering why you looked half dead."
    new "她可能只是在想为什么你一幅快死的样子。"

    old "maybe..."
    new "可能吧……"

    old "but i'm telling u"
    new "但我跟你说"

    old "that look she gave me?"
    new "她瞪我那一眼"

    old "soul left my body 💀"
    new "魂都快给我吓没了💀"

    old "Dramatic much?"
    new "有这么夸张吗？"

    old "U WERENT THE ONE GETTING STARED DOWN"
    new "又不是你被她瞪"

    old "anyway"
    new "总之"

    old "just... b careful around her ok?"
    new "你……在她身边小心点"

    old "idk what she knows but"
    new "我不清楚她知不知道但是"

    old "she DEF suspects smth"
    new "她肯定起疑心了"

    old "Now get some sleep."
    new "你快睡觉吧。"

    old "cant"
    new "睡不着"

    old "still too wired from dinner"
    new "还在后怕"

    old "Sky..."
    new "斯凯……"

    old "FINE"
    new "行行行"

    old "going 2 bed"
    new "这就睡"

    old "night"
    new "晚安"

    old "I love you"
    new "我爱你"

    old "Good night"
    new "晚安"

    old "Good night."
    new "晚安。"

    old "Good night, Sky."
    new "晚安，斯凯。"

    old "i luv u 2 😚"
    new "我也爱你😚"

    old "When we're ready."
    new "我们迟早会告诉她的。"

    old "when ready"
    new "嗯嗯"

    old "oh w8"
    new "哦等一下"

    old "sorry messy hair"
    new "对不起头发有点乱"

    old "Not something new to my eyes, but I like that on you."
    new "也不是第一次见了，不过我喜欢你这模样。"

    old "geez"
    new "哎呀得了吧"

    old "sleep well [mc]"
    new "睡个好觉[mc!t]"

    old "Sleep well, Sky."
    new "睡个好觉，斯凯。"

    #NAOMI

    old "So, how you holding up?"
    new "你情况怎么样了？"

    old "Better by the day. Finally walking without feeling like every step's a chastisement."
    new "好不少了。终于没有再觉得每走一步都是在受罪。"

    old "Thanks again for visiting, even though I was technically a corpse with a pulse."
    new "我当时都是具有心跳的尸体了，你还来看我。真的谢谢你。"

    old "All good. You'd do the same for me."
    new "没什么。你也会为我做同样的事的。"

    old "So, when're you coming over so I can make good on my promise?"
    new "所以你什么时候过来，让我兑现我的承诺？"

    old "The what now? What could you possibly owe me?"
    new "什么东西？你什么时候欠我一个承诺了？"

    old "Cracking open a cold one to celebrate you no longer being a log stuck in a hospital bed. Or regular bed, for that matter."
    new "开一瓶冰啤酒，庆祝你不再是躺在医院病床上的木头人了。或者说不用再躺在任何床上了。"

    old "Right, that. How's tomorrow night?"
    new "还真是，想起来了。明天晚上怎么样？"

    old "Sweet. Got a beer preference?"
    new "可以。爱喝什么啤酒？"

    old "Something proudly \"Advance Cesa Fair\". Maybe Foster's."
    new "正宗澳洲风味的。比如福斯特啤酒。"

    old "Yeah nah."
    new "一边去。"

    old "Bye."
    new "再见。"

    old "What? What did I say?"
    new "啊？我说错话了吗？"

    old "Mate, if you reckon Foster's is Cesa beer, you might as well drink straight from the dunny."
    new "伙计，你要觉得福斯特是正宗澳洲啤酒的话，那你还不如直接从厕所里喝算了。"

    old "Clearly your brain's still booting up, but no stress, Naomi's got you covered."
    new "显然你的脑子还没完全清醒过来，不过别担心，娜奥米会帮你的。"

    old "You want something crisp, bright, proper flavour? Stuff that actually tastes like beer, not regret?"
    new "你想要清爽，明亮，口感正宗的啤酒吗？不是喝一口就后悔那种？"

    old "I thought your dad was Mr. Scott, not Mr. Mays."
    new "你爸不是斯考特先生吗，怎么变成酒鬼梅斯先生了？"

    old "Fair call. You'll see when you get here."
    new "好吧。等你来就知道了。"

    old "Can't wait. See you tomorrow, Naomi."
    new "我很期待。明天见，娜奥米。"

    old "Catch you then."
    new "明天见。"

    old "Here's Johnny..."
    new "强尼来咯……"

    old "Huh? What are you on about?"
    new "啊？你在说什么？"

    old "Movie reference. Anyway, I'm in your driveway."
    new "电影台词。总之，我在你家车道上了。"

    old "Out back. Working on another beauty."
    new "后院。正在鼓捣另一辆美女。"

    old "Moved your makeup to your shed? 😉"
    new "你在工作室里化妆啊？😉"

    old "Ease up, Casanova. Keep it up and I might actually let you take her for a spin."
    new "收着点吧，大情圣。再这样下去，我可能真就让你跟她去兜风了。"

    old "Which one?"
    new "哪个她？"

    old "Where's the fun in telling you? 😜"
    new "告诉你了还有什么意思呢？😜"

    old "Quit stuffing around and get in here. Beer's not staying cold for you."
    new "别闹了，快进来。一会儿啤酒都不凉了。"

    old "Heading over now."
    new "马上过去。"

    old "Actually, where's your shed again?"
    new "对了，你的工作室在哪来着？"

    old "LMAO."
    new "笑死。"

    old "You're something else. Now seriously, get in here or I'm nicking your beer"
    new "你真是个奇葩。说真的，快进来，不然我可要把你的啤酒偷走了。"

    old "Ha... right..."
    new "哈……好吧……"

    old "... You're actually serious."
    new "……你是真心在问啊。"

    old "Afraid so. 😬"
    new "恐怕是的。😬"

    old "Bloody hell. Backyard, left side. Follow the dirt track and you can't miss it."
    new "操了。后院，左边。沿着土路走，肯定能看见的。"

    old "Wait, what driveway are you even parked on?"
    new "等一下，你停在哪个车道上了？"

    old "The back one."
    new "后面那个。"

    old "You muppet. Should've used the front like you used to."
    new "你个傻瓜。应该跟以前一样用前面的。"

    old "Noted for next time. Be there soon."
    new "下次我会记住的。马上就到。"

    old "G'day, you beauty."
    new "你好，美女。"

    old "Good timing, was just about to message you."
    new "来得正好，我也打算给你发消息。"

    old "Oh yeah?"
    new "是吗？"

    old "Was thinking of getting back into my restoration project next week. Been putting it off long enough."
    new "想着下周恢复我的修复项目。已经拖了够久了。"

    old "Your SRT Demon?"
    new "你那辆SRT恶魔？"

    old "Yep. Poor girl's been sitting there collecting dust like some forgotten museum piece."
    new "对。已经跟博物馆里的古董一样吃灰很久了。"

    old "Truth is... I wanted to finish it with you. Then you went completely off the grid and, well, kinda killed the rhythm."
    new "其实……我本来想跟你一起弄好。然后你就完全失联了，就……有点打乱了节奏。"

    old "Figured I'd wait till you were back on your feet before I laid a finger on her again."
    new "于是我决定在你恢复过来之前都不碰她。"

    old "You just want to see me more often, don't you?"
    new "你只是想多见见我吧？"

    old "Was gonna say that next, smartass. 😉"
    new "我接下来就打算说那句话呢，大聪明。😉"

    old "But hey, I know you've got your day job, so just swing by whenever you're free. No pressure."
    new "不过我知道你还要上班，所以你有时间的时候过来就行了。不用着急。"

    old "Next week, right? How about Monday after my shift?"
    new "下周开始吗？那要不我周一下班后过来？"

    old "Works for me!"
    new "没问题！"

    old "Just rock up. No need to call or text. Gate's always open for you."
    new "直接来就行。不用打电话或发短信。一直给你留着门呢。"

    old "Gotcha."
    new "明白。"

    old "Today was fun, [mc]. Unplanned, but fun. 😂"
    new "今天很有趣，[mc!t]。虽然在计划外，但很有趣。😂"

    old "I promise I'll wash the dishes."
    new "我保证我会洗盘子。"

    old "Vacuum the house."
    new "扫地。"

    old "Clean the bathroom."
    new "打扫浴室。"

    old "Pick up the garbage."
    new "倒垃圾。"

    old "Make the sandwich."
    new "做三明治。"

    old "Do the laundry."
    new "洗衣服。"

    old "Cook the dinner."
    new "做晚饭。"

    old "Walk the dogs."
    new "遛狗。"

    old "Cut the grass."
    new "修剪草坪。"

    old "Pay the bills"
    new "交水电费。"

    old "Wash the car"
    new "洗车。"

    old "LOL! 🤣"
    new "哈哈哈！🤣"

    old "That wasn't meant to be a threat!"
    new "我不是威胁你！"

    old "I'm pregnant! 🥵"
    new "我怀孕了！🥵"

    old "Alright, nope. Stop it. 😅"
    new "行了行了，停吧。😅"

    old "Tomorrow. Same time?"
    new "明天同样的时间？"

    old "Wouldn't miss it."
    new "我一定来。"

    old "Naomi. What on earth happened last night?"
    new "娜奥米。昨晚到底发生什么了？"

    old "Message Undeliverable"
    new "发送失败"




    #LILY

    old "hey, [mc]! 🌼"
    new "[mc!t]！🌼"

    old "i know it's been a while. i hope that's okay."
    new "好久没联系了。希望你不介意。"

    old "i just wanted to say hi while i still have the luxury."
    new "我就是想趁还有时间的时候来打个招呼。"

    old "i remembered today's your birthday."
    new "我记得今天是你的生日。"

    old "happy birthday, [mc]!"
    new "生日快乐，[mc!t]！"

    old "i hope you're doing okay."
    new "希望你一切都好。"

    old "and that you and freya are taking care of each other. 🤍"
    new "还有你跟芙蕾雅要好好照顾彼此。🤍"

    old "Forget my birthday! Holy hell, Lily!"
    new "别管我的生日了！我的天啊，莉莉！"

    old "Jesus. How long has it been?"
    new "都多久了？"

    old "How are you?"
    new "你过得怎么样？"

    old "actually, pretty great!"
    new "其实挺好的！"

    old "i mean, kinda?"
    new "算好吧？"

    old "today's my first day at a new job."
    new "今天是我新工作的第一天。"

    old "i'm pretty nervous."
    new "我很紧张。"

    old "but i think i'll manage."
    new "不过我觉得我能应付得来。"

    old "look!"
    new "你看！"

    old "Wait... seriously?"
    new "等等……真的吗？"

    old "seriously."
    new "真的。"

    old "i'm training high school students."
    new "我在给高中生当教练。"

    old "Damn... that's nostalgic."
    new "我去……真怀念啊。"

    old "yeah. i didn't expect this, honestly."
    new "是啊。说实话我也没想到会这样。"

    old "it's way bigger than what i thought i'd ever get."
    new "我从来没想过我会遇上这么好的机会。"

    old "i figured i'd end up as a water girl or something."
    new "我还以为我最后会当服务员之类的。"

    old "guess all that experience paid off. 😁"
    new "看来以前的经验还是有用的。😁"

    old "But do you love it?"
    new "但你喜欢这样吗？"

    old "i do!"
    new "喜欢啊！"

    old "it's close enough to my dream that i'm happy."
    new "这已经很接近我的梦想了，我很开心。"

    old "Then that's what counts."
    new "那才是最重要的。"

    old "what about you?"
    new "你呢？"

    old "still at the burger shack?"
    new "还在汉堡店？"

    old "Ouch."
    new "扎心了。"

    old "oh! no, i didn't mean it like that."
    new "哦！我不是那个意思。"

    old "Relax. I know."
    new "没事。我知道。"

    old "Yeah, I'm still there."
    new "嗯，我还在那。"

    old "But I'm working on something new, too."
    new "不过我也同时在做一些新的工作。"

    old "Not a dream job... but it's something."
    new "算不上我梦想中的工作……但总归是点什么吧。"

    old "then what's your dream job?"
    new "那你的梦想工作是什么？"

    old "Honestly?"
    new "说实话。"

    old "I don't really know anymore."
    new "我已经不太清楚了。"

    old "huh? why?"
    new "啊？为什么？"

    old "Things have been off since you left."
    new "你走之后，出了很多事。"

    old "I wish I could explain everything."
    new "真希望我能把一切都解释清楚。"

    old "But I can't."
    new "但我做不到。"

    old "that's okay."
    new "没事的。"

    old "maybe one day. 😁"
    new "说不定以后会有机会。😁"

    old "Yeah. One day."
    new "嗯。以后再说吧。"

    old "the students are here."
    new "学生们来了。"

    old "i'll text you some other time, [mc]."
    new "我会再给你发短信的，[mc!t]。"

    old "tell freya to take care of herself for me, please?"
    new "告诉芙蕾雅要好好照顾自己，行吗？"

    old "she was kinda mad i can't facetime much anymore."
    new "我没法经常跟她打视频了，她还有点生气。"

    old "I will. And good luck out there."
    new "我会的。祝你在那边一切都好。"

    old "you too, [mc]."
    new "你也是，[mc!t]。"




    #KLARA

    old "when you pass by the store later,"
    new "你待会路过商店的时候，"

    old "buy a box of hair dye."
    new "买一箱染发剂。"

    old "the dark one."
    new "黑的。"

    old "you know which."
    new "你知道哪种。"

    old "i want things back to how they should be."
    new "我想回到从前的样子。"

    old "Sure.{#1}"
    new "好。"

    old "i knew it."
    new "我就知道。"

    old "delete that. now."
    new "现在就删掉。"

    old "i swear on the ashes of my sanity, [mc], if that photo surfaces, so will your obituary."
    new "我用我仅剩的理智发誓，[mc!t]，如果那张照片被传出去，你的讣告也会立马上报纸。"

    old "No. No, I don't think I will."
    new "不。我不删。"

    #CLAIRE




    #JESS




