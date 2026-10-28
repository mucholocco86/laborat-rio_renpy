init python:
    def cg_init_card_game():
        global cg_questions_list
        global cg_cards_list
        global cg_cpu1_score_list
        global cg_cpu2_score_list
        global cg_cpu3_score_list
        global cg_cpu1_card_score_list
        global cg_cpu2_card_score_list
        global cg_cpu3_card_score_list
        global cg_questions_asked
        global cg_reader
        global cg_current_question
        global cg_question_idx
        global cg_cards_on_hand
        global cg_winning_string
        global cg_mc_card_draw_idx
        global cg_cpu_selected_cards
        global cg_mc_selected_card
        global cg_current_winner
        global cg_mc_cards_order
        global cg_card_list
        global cg_cpu_answers_list
        global cg_scores
        global cg_winner
        
        cg_winner = ""
        cg_scores = [0,0,0,0]
        cg_winning_string = ""
        cg_current_winner = -1
        cg_current_question = -1
        cg_reader = -1
        cg_question_idx = 0
        cg_mc_selected_card = -1
        cg_cpu1_score_list = []
        cg_cpu2_score_list = []
        cg_cpu3_score_list = []
        cg_cpu1_card_score_list = []
        cg_cpu2_card_score_list = []
        cg_cpu3_card_score_list = []
        cg_cpu_selected_cards = []
        cg_questions_list = []
        cg_cards_list = []
        cg_cards_on_hand = []
        cg_cpu_answers_list = []
        cg_mc_card_draw_idx = 0
        
        cg_questions_asked = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        renpy.random.shuffle(cg_questions_asked)
        cg_mc_cards_order = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
        renpy.random.shuffle(cg_mc_cards_order)
        
        cg_populate_cpu_responses()
        
        cg_card_list.append("Violent diarrhea.")
        cg_card_list.append("Too many orgasms.")
        cg_card_list.append("A crusty cum sock.")
        cg_card_list.append("Gay porn.")
        cg_card_list.append("A finger in the anus.")
        cg_card_list.append("Nothing.")
        cg_card_list.append("A short adventure.")
        cg_card_list.append("Ok, grandpa. Let's get you to bed.")
        cg_card_list.append("Birthday cake.")
        cg_card_list.append("Your girlfriend.")
        cg_card_list.append("STDs.")
        cg_card_list.append("Building sandcastles.")
        cg_card_list.append("A microwave.")
        cg_card_list.append("Mayonaisse.")
        cg_card_list.append("Brown stuff.")
        cg_card_list.append("Your Mom.")
        cg_card_list.append("Yatzy!")
        cg_card_list.append("Laughter.")
        cg_card_list.append("Sperm.")
        cg_card_list.append("Snorting cocaine.")
        
        for i in range(0,5):
            cg_mc_get_new_card()
        
        
        cg_questions_list.append("What's the best cure for depression?")
        cg_cpu_answers_list.append([["An apple.","Drinking all night long.","A big black cock."],["Dancing the night away.","Vaseline.","Money."],["Spaghetti.","A fistful of parsely.","Tiny hats."]])
        
        cg_cpu1_score_list.append([[0,0,0],[4,8,5],[6,3,7]])
        cg_cpu2_score_list.append([[4,6,4],[0,0,0],[3,7,8]])
        cg_cpu3_score_list.append([[4,5,6],[3,8,7],[0,0,0]])
        
        cg_cpu1_card_score_list.append([4,10,9,9,10,4,5,4,7,5,5,3,1,4,6,7,6,1,3,6])
        cg_cpu2_card_score_list.append([1,4,3,2,1,6,7,4,8,6,2,8,4,6,5,5,10,10,8,5])
        cg_cpu3_card_score_list.append([4,7,6,5,6,8,4,3,2,5,6,8,5,7,8,7,8,7,7,10])
        
        
        cg_questions_list.append("What's my favorite hobby? I won't tell you exactly what it is, but it involves...")
        cg_cpu_answers_list.append([["Two condoms.","Grandma.","Lube."],["Doing things.","A bowl of fruit.","A human pyramid."],["Getting drunk.","Talking to strangers.","A wet tongue."]])
        
        cg_cpu1_score_list.append([[0,0,0],[7,2,3],[5,4,6]])
        cg_cpu2_score_list.append([[6,7,2],[0,0,0],[5,4,3]])
        cg_cpu3_score_list.append([[7,9,8],[6,10,5],[0,0,0]])
        
        cg_cpu1_card_score_list.append([9,6,8,7,10,4,3,0,5,9,10,6,3,10,6,10,10,2,9,10])
        cg_cpu2_card_score_list.append([3,4,5,4,6,2,7,0,8,6,6,10,8,9,2,6,8,7,6,7])
        cg_cpu3_card_score_list.append([10,9,8,8,7,5,3,0,9,8,7,6,9,9,9,6,7,4,8,8])
        
        
        cg_questions_list.append("What I want to do tonight? It's simple. You, me and...")
        cg_cpu_answers_list.append([["Eight other dudes.","Tequila.","Butt stuff."],["My belly button.","Shredding top-secret documents.","Screaming in libraries."],["An encyclopedia.","A bouncy castle.","69."]])
        
        cg_cpu1_score_list.append([[0,0,0],[8,4,5],[3,6,7]])
        cg_cpu2_score_list.append([[8,5,4],[0,0,0],[6,9,7]])
        cg_cpu3_score_list.append([[7,4,6],[8,9,5],[0,0,0]])
        
        cg_cpu1_card_score_list.append([7,6,4,6,9,2,3,1,5,7,7,5,2,10,7,4,8,1,5,6])
        cg_cpu2_card_score_list.append([5,6,2,3,4,4,6,1,7,7,6,8,5,8,4,6,9,5,6,7])
        cg_cpu3_card_score_list.append([7,7,6,6,7,7,6,2,7,5,8,8,6,8,7,5,9,4,6,8])
        
        
        cg_questions_list.append("What's the title of my sex tape?")
        cg_cpu_answers_list.append([["My Mom's friend Susan.","A filthy pig.","Riding a horse."],["Disappointment.","Tears of joy.","My first time."],["Getting wet.","Ketchup on a wiener.","Butt sex."]])
        
        cg_cpu1_score_list.append([[0,0,0],[7,5,8],[6,9,9]])
        cg_cpu2_score_list.append([[7,3,4],[0,0,0],[8,6,5]])
        cg_cpu3_score_list.append([[7,7,6],[8,5,4],[0,0,0]])
        
        cg_cpu1_card_score_list.append([8,7,9,9,10,4,6,10,3,7,8,3,1,7,8,8,6,5,7,4])
        cg_cpu2_card_score_list.append([5,6,4,3,5,3,8,8,6,7,5,6,2,4,2,5,6,7,6,3])
        cg_cpu3_card_score_list.append([6,7,8,7,8,4,8,9,5,6,7,2,3,8,6,5,7,8,6,2])
        
        
        cg_questions_list.append("Do you know what would liven this party up?")
        cg_cpu_answers_list.append([["An inappropriate cluck on Rooster.","Poop.","Naughty girls."],["Free WiFi.","Absolute silence.","A monkey."],["A juicy orange.","Estrogen.","Low inhibitions."]])
        
        cg_cpu1_score_list.append([[0,0,0],[3,7,9],[4,5,8]])
        cg_cpu2_score_list.append([[8,4,5],[0,0,0],[7,6,9]])
        cg_cpu3_score_list.append([[4,7,5],[3,8,6],[0,0,0]])
        
        cg_cpu1_card_score_list.append([10,6,3,6,7,6,4,3,6,7,7,4,2,5,4,6,9,8,7,10])
        cg_cpu2_card_score_list.append([5,6,4,6,5,8,8,4,6,4,3,6,3,2,0,5,8,8,7,7])
        cg_cpu3_card_score_list.append([7,7,5,5,6,6,6,3,6,5,6,7,2,8,6,4,8,7,7,9])
        
        
        cg_questions_list.append("Today's youth are spoiled. When I was young all I had to play with was...")
        cg_cpu_answers_list.append([["My left hand.","Boogers.","Boner."],["My brother.","A million dollars.","Marbles."],["A bucket.","A banana.","Mustard."]])
        
        cg_cpu1_score_list.append([[0,0,0],[7,8,5],[6,9,4]])
        cg_cpu2_score_list.append([[7,0,4],[0,0,0],[6,8,5]])
        cg_cpu3_score_list.append([[8,6,8],[7,9,4],[0,0,0]])
        
        cg_cpu1_card_score_list.append([6,2,7,6,9,8,3,9,4,7,7,3,5,6,4,8,8,5,9,8])
        cg_cpu2_card_score_list.append([2,2,4,4,5,6,6,8,7,6,5,4,5,6,2,8,7,5,6,7])
        cg_cpu3_card_score_list.append([7,5,8,8,9,8,5,9,6,6,7,4,7,8,5,7,7,3,7,7])
        
        
        cg_questions_list.append("What do you dream of doing when you get older?")
        cg_cpu_answers_list.append([["My boss's wife.","Naked parachuting.","Shaving my balls."],["Driving too slow to piss people off.","Smiling when you feel dead inside.","A night in jail."],["Posting awesome memes.","A wicked backflip.","Being horny all the time."]])
        
        cg_cpu1_score_list.append([[0,0,0],[8,6,6],[7,7,9]])
        cg_cpu2_score_list.append([[7,6,4],[0,0,0],[8,8,5]])
        cg_cpu3_score_list.append([[7,7,6],[8,8,8],[0,0,0]])
        
        cg_cpu1_card_score_list.append([8,7,5,6,4,9,5,3,7,9,6,4,2,4,3,5,8,1,4,9])
        cg_cpu2_card_score_list.append([3,4,3,4,4,9,8,7,5,6,4,6,4,5,4,6,8,5,4,7])
        cg_cpu3_card_score_list.append([6,5,4,4,5,7,7,8,6,9,6,6,4,4,4,6,7,3,5,8])
        
        
        cg_questions_list.append("What do you give to a man who has it all?")
        cg_cpu_answers_list.append([["Syphilis.","A spleen.","AIDS."],["A high five.","Peace and love.","Three tomatoes and an onion."],["A warm smile.","Ginger ale.","Unpaid parking tickets."]])
        
        cg_cpu1_score_list.append([[0,0,0],[7,4,6],[5,5,5]])
        cg_cpu2_score_list.append([[6,6,4],[0,0,0],[7,7,7]])
        cg_cpu3_score_list.append([[8,6,8],[7,5,7],[0,0,0]])
        
        cg_cpu1_card_score_list.append([5,5,6,7,8,9,3,0,6,9,7,3,5,6,4,5,8,4,9,6])
        cg_cpu2_card_score_list.append([2,3,3,4,4,8,6,3,9,7,5,4,6,7,5,6,8,5,4,6])
        cg_cpu3_card_score_list.append([6,5,5,7,7,9,6,3,8,7,7,5,6,7,5,5,8,4,6,5])
        
        
        cg_questions_list.append("Stop it! You and your sister are both great, but at different things. She's good at socializing. You're good at...")
        cg_cpu_answers_list.append([["A blowjob.","Masturbating.","Farting."],["Juggling.","Drinking water.","Failing tests."],["Doing cartwheels.","Fucking things up.","Eating lasagna."]])
        
        cg_cpu1_score_list.append([[0,0,0],[5,5,7],[4,8,8]])
        cg_cpu2_score_list.append([[0,6,6],[0,0,0],[5,7,8]])
        cg_cpu3_score_list.append([[7,7,7],[6,6,8],[0,0,0]])
        
        cg_cpu1_card_score_list.append([7,4,1,6,7,9,3,0,3,2,2,5,3,4,5,4,9,6,5,10])
        cg_cpu2_card_score_list.append([3,3,2,3,4,9,5,2,4,3,4,8,5,5,4,3,8,6,5,9])
        cg_cpu3_card_score_list.append([5,3,4,5,6,9,5,0,4,2,5,7,5,6,4,5,9,3,2,8])
        
        
        cg_questions_list.append("What's the secret to a happy relationship?")
        cg_cpu_answers_list.append([["That Swyper account you said you deleted.","Coughing to cover up your fart.","Alcohol."],["Silently nodding while zoning out.","Optimism.","Being sassy."],["Tofu.","Shutting the fuck up.","Having an affair."]])
        
        cg_cpu1_score_list.append([[0,0,0],[5,4,7],[6,8,8]])
        cg_cpu2_score_list.append([[6,6,4],[0,0,0],[5,7,5]])
        cg_cpu3_score_list.append([[7,6,6],[8,5,8],[0,0,0]])
        
        cg_cpu1_card_score_list.append([4,8,6,5,8,6,5,2,5,7,6,5,4,6,5,5,8,7,7,8])
        cg_cpu2_card_score_list.append([0,6,2,5,6,7,8,3,7,6,5,6,4,6,3,4,8,7,6,8])
        cg_cpu3_card_score_list.append([4,6,3,2,6,7,7,2,5,5,4,5,3,6,4,5,8,7,7,8])
        
        
        cg_questions_list.append("If that mockingbird won't sing, Mama's going to buy you...")
        cg_cpu_answers_list.append([["A trip to Thailand.","A fucking goat.","A double-headed dildo."],["A cat.","Therapy.","A hamster."],["A jar of jam.","A hammer.","A bucket of coleslaw."]])
        
        cg_cpu1_score_list.append([[0,0,0],[5,6,7],[4,8,4]])
        cg_cpu2_score_list.append([[6,7,6],[0,0,0],[5,5,8]])
        cg_cpu3_score_list.append([[7,7,7],[6,6,8],[0,0,0]])
        
        cg_cpu1_card_score_list.append([5,3,6,8,5,7,6,2,7,7,6,3,8,9,3,3,6,3,8,3])
        cg_cpu2_card_score_list.append([3,3,4,5,5,8,5,3,4,5,3,5,8,9,6,5,7,5,8,3])
        cg_cpu3_card_score_list.append([5,5,3,7,7,8,5,3,7,6,5,3,8,9,6,5,8,6,8,2])
        
        
        cg_questions_list.append("How do you know when a date is not for you? When they start talking about...")
        cg_cpu_answers_list.append([["Children.","Sobriety.","Waterboarding."],["Shaving your cat.","Setting things on fire for fun.","Quantum physics."],["An ex-boyfriend.","A poem about your reproductive organ.","Pineapple on a pizza."]])
        
        cg_cpu1_score_list.append([[0,0,0],[7,6,6],[5,8,5]])
        cg_cpu2_score_list.append([[3,2,2],[0,0,0],[5,6,7]])
        cg_cpu3_score_list.append([[4,7,6],[8,5,3],[0,0,0]])
        
        cg_cpu1_card_score_list.append([10,3,5,10,7,6,2,0,4,8,9,7,6,8,7,4,5,3,7,8])
        cg_cpu2_card_score_list.append([3,3,3,4,4,7,5,2,5,7,9,7,5,7,4,5,6,4,5,6])
        cg_cpu3_card_score_list.append([6,2,3,6,6,6,4,2,5,7,8,8,5,7,5,4,4,4,7,7])
        
        
        cg_questions_list.append("I failed the class. My Professor didn't enjoy my essay on...")
        cg_cpu_answers_list.append([["Boobs.","Dingleberries.","Doing it doggystyle."],["The alphabet.","Braille.","The best reality shows on TV."],["Wet dreams.","Gloryholes.","People I don't like."]])
        
        cg_cpu1_score_list.append([[0,0,0],[4,4,5],[6,7,6]])
        cg_cpu2_score_list.append([[4,2,2],[0,0,0],[5,3,6]])
        cg_cpu3_score_list.append([[6,3,6],[4,4,4],[0,0,0]])
        
        cg_cpu1_card_score_list.append([7,7,5,6,8,9,2,2,4,3,7,5,4,6,3,2,6,4,7,7])
        cg_cpu2_card_score_list.append([3,4,3,3,4,7,4,2,6,3,6,7,5,7,3,2,6,4,6,5])
        cg_cpu3_card_score_list.append([6,5,5,6,6,7,4,2,2,2,5,3,4,6,2,3,6,2,7,7])
        
        
        cg_questions_list.append("At my college we don't play Rock paper scissors. We play Rock paper...")
        cg_cpu_answers_list.append([["Dildo.","A fanny kiss.","Fart."],["A garden hose.","MEOW!","Pencils."],["A smelly fish.","Fuck you.","Camel toe."]])
        
        cg_cpu1_score_list.append([[0,0,0],[3,7,5],[4,8,9]])
        cg_cpu2_score_list.append([[4,5,8],[0,0,0],[6,6,7]])
        cg_cpu3_score_list.append([[6,4,6],[3,7,5],[0,0,0]])
        
        cg_cpu1_card_score_list.append([8,4,3,6,9,5,2,7,4,4,6,3,5,7,2,4,8,4,8,7])
        cg_cpu2_card_score_list.append([2,3,2,3,5,6,4,5,7,3,5,4,3,7,5,2,7,4,5,5])
        cg_cpu3_card_score_list.append([3,4,3,4,6,5,3,2,6,4,6,4,5,7,5,3,6,2,6,7])
        
        
        cg_questions_list.append("All I got for Christmas was...")
        cg_cpu_answers_list.append([["Herpes.","An awkward conversation about birds and bees.","A fingernail."],["A hug.","A song.","A balloon animal."],["Sympathy.","Anxiety.","An empty box."]])
        
        cg_cpu1_score_list.append([[0,0,0],[5,3,5],[6,6,4]])
        cg_cpu2_score_list.append([[4,5,0],[0,0,0],[6,6,6]])
        cg_cpu3_score_list.append([[5,5,8],[6,4,6],[0,0,0]])
        
        cg_cpu1_card_score_list.append([8,8,8,8,8,6,1,4,6,5,7,2,4,5,2,1,5,2,5,3])
        cg_cpu2_card_score_list.append([2,4,3,4,4,6,5,5,6,4,5,3,5,7,3,4,7,2,3,4])
        cg_cpu3_card_score_list.append([6,6,6,5,6,6,4,5,3,2,5,3,5,6,3,4,4,4,4,4])
        
        
        cg_questions_list.append("Thank you for the award, but I couldn't have done this by myself. I got a little help from...")
        cg_cpu_answers_list.append([["Vodka.","Cocaine.","An imaginary friend."],["My dog.","The entire internet.","People."],["A Chinese woman.","Sexual education.","My pet rock."]])
        
        cg_cpu1_score_list.append([[0,0,0],[6,7,6],[8,5,5]])
        cg_cpu2_score_list.append([[6,4,7],[0,0,0],[5,5,8]])
        cg_cpu3_score_list.append([[5,6,6],[4,7,8],[0,0,0]])
        
        cg_cpu1_card_score_list.append([5,3,3,5,3,2,2,0,3,5,4,3,3,5,3,8,4,3,5,8])
        cg_cpu2_card_score_list.append([3,4,3,3,3,5,3,7,5,5,6,4,5,6,4,7,7,5,4,6])
        cg_cpu3_card_score_list.append([5,5,4,3,4,3,3,5,4,6,5,4,4,6,5,7,7,4,4,7])
        
        
        cg_questions_list.append("Instead of donating money to third-world countries, we will donate...")
        cg_cpu_answers_list.append([["A funny joke.","The homeless.","Sand."],["Two dollars.","Rooster likes.","Breakfast."],["A prayer.","Breast milk.","Leftovers."]])
        
        cg_cpu1_score_list.append([[0,0,0],[7,5,5],[6,9,6]])
        cg_cpu2_score_list.append([[5,3,5],[0,0,0],[4,4,6]])
        cg_cpu3_score_list.append([[4,6,7],[8,5,5],[0,0,0]])
        
        cg_cpu1_card_score_list.append([7,7,7,7,7,9,2,0,5,3,10,4,6,8,5,5,5,4,7,3])
        cg_cpu2_card_score_list.append([2,4,3,4,4,7,5,3,6,2,4,2,5,6,2,4,5,4,7,5])
        cg_cpu3_card_score_list.append([4,6,5,5,4,6,5,1,5,4,6,4,5,6,3,4,7,5,6,3])
        
        
        cg_questions_list.append("The winner of the competition receives $1000. The prize for the runner-up is...")
        cg_cpu_answers_list.append([["A mischievous little slut.","A weekend with me.","A fist bump."],["$2000.","Spanish lessons.","A hip hip hooray!"],["A hickey.","22 hot shots.","A wooden stick."]])
        
        cg_cpu1_score_list.append([[0,0,0],[8,5,7],[6,4,4]])
        cg_cpu2_score_list.append([[1,6,6],[0,0,0],[7,4,4]])
        cg_cpu3_score_list.append([[5,5,6],[8,7,8],[0,0,0]])
        
        cg_cpu1_card_score_list.append([6,7,5,7,8,9,6,2,6,6,8,5,8,8,7,6,7,8,9,9])
        cg_cpu2_card_score_list.append([5,7,5,6,6,8,7,3,6,5,7,5,7,7,6,4,6,7,5,5])
        cg_cpu3_card_score_list.append([6,6,5,5,6,7,6,3,5,4,5,4,7,7,5,4,6,7,5,7])
        
        
        cg_questions_list.append("How the date went? It started off with a candlelit dinner and ended with...")
        cg_cpu_answers_list.append([["A wet willy.","A house fire.","Peekaboo!"],["Dinner.","Dessert.","A handshake."],["Mexico.","Sex.","Thumb wars."]])
        
        cg_cpu1_score_list.append([[0,0,0],[7,7,8],[6,6,9]])
        cg_cpu2_score_list.append([[5,8,8],[0,0,0],[6,6,7]])
        cg_cpu3_score_list.append([[7,7,8],[6,9,6],[0,0,0]])
        
        cg_cpu1_card_score_list.append([8,6,5,6,9,7,5,3,6,7,9,6,4,7,7,8,10,7,8,8])
        cg_cpu2_card_score_list.append([3,6,3,4,6,6,6,3,5,5,7,7,4,4,6,6,8,8,6,7])
        cg_cpu3_card_score_list.append([5,7,5,6,7,6,6,4,6,5,6,7,5,7,6,7,7,7,6,7])
        
        
        cg_questions_list.append("What's not appropriate for Show and Tell?")
        cg_cpu_answers_list.append([["A buttplug.","A beer bong.","Making babies."],["Confetti.","Moonshine.","A bunch of fireworks."],["A hobo.","A diaper.","Russian roulette."]])
        
        cg_cpu1_score_list.append([[0,0,0],[5,7,7],[8,6,8]])
        cg_cpu2_score_list.append([[5,5,7],[0,0,0],[6,4,4]])
        cg_cpu3_score_list.append([[6,4,6],[5,5,8],[0,0,0]])
        
        cg_cpu1_card_score_list.append([8,8,8,9,9,4,3,3,5,8,8,6,5,6,5,7,7,4,8,10])
        cg_cpu2_card_score_list.append([3,5,4,4,7,6,6,3,6,7,7,7,6,7,8,8,8,5,6,7])
        cg_cpu3_card_score_list.append([7,7,6,7,7,6,5,2,2,4,5,7,5,7,7,8,8,5,4,7])
        return

    def cg_populate_cpu_responses():
        global cg_cpu_selected_cards
        cg_cpu_selected_cards = []
        for i in range(0,20):
            cg_cpu_selected_cards.append([renpy.random.randint(0,2),renpy.random.randint(0,2),renpy.random.randint(0,2)])
        renpy.random.shuffle(cg_cpu_selected_cards)
        return

    def cg_get_next_question():
        global cg_current_question
        global cg_reader
        global cg_question_idx
        cg_current_question += 1
        cg_reader += 1
        if cg_reader == 4:
            cg_reader = 0
        cg_question_idx = cg_questions_asked[cg_current_question]
        return

    def cg_get_current_question_string():
        global cg_question_idx
        global cg_questions_list
        return cg_questions_list[cg_question_idx]

    def cg_mc_select_card(card):
        global cg_mc_selected_card
        cg_mc_selected_card = card
        return

    def cg_discard_card(card):
        global cg_mc_card_draw_idx
        global cg_cards_list
        global cg_mc_cards_order
        cg_cards_on_hand[card] = cg_mc_cards_order[cg_mc_card_draw_idx]
        cg_mc_card_draw_idx += 1
        return

    def cg_get_mc_card_string(idx):
        global cg_card_list
        global cg_cards_on_hand
        return cg_card_list[cg_cards_on_hand[idx]]

    def cg_mc_get_new_card():
        global cg_mc_card_draw_idx
        global cg_cards_list
        global cg_mc_cards_order
        
        cg_cards_on_hand.append(cg_mc_cards_order[cg_mc_card_draw_idx])
        cg_mc_card_draw_idx += 1
        return

    def cg_simulate_winner():
        global cg_cpu1_card_score_list
        global cg_cpu2_card_score_list
        global cg_cpu3_card_score_list
        global cg_cpu1_score_list
        global cg_cpu2_score_list
        global cg_cpu3_score_list
        global cg_reader
        global cg_current_winner
        global cg_winning_string
        global cg_cpu_answers_list
        global cg_question_idx
        if cg_reader == 0:
            if cg_cpu1_card_score_list[cg_question_idx][cg_cards_on_hand[cg_mc_selected_card]] > cg_cpu1_score_list[cg_question_idx][1][cg_cpu_selected_cards[cg_question_idx][1]] and cg_cpu1_card_score_list[cg_question_idx][cg_cards_on_hand[cg_mc_selected_card]] > cg_cpu1_score_list[cg_question_idx][2][cg_cpu_selected_cards[cg_question_idx][2]]:
                cg_current_winner = 3
                cg_winning_string = cg_get_mc_card_string(cg_mc_selected_card)
            elif cg_cpu1_score_list[cg_question_idx][1][cg_cpu_selected_cards[cg_question_idx][1]] > cg_cpu1_score_list[cg_question_idx][2][cg_cpu_selected_cards[cg_question_idx][2]]:
                cg_current_winner = 1
            else:
                cg_current_winner = 2
        elif cg_reader == 1:
            if cg_cpu2_card_score_list[cg_question_idx][cg_cards_on_hand[cg_mc_selected_card]] > cg_cpu2_score_list[cg_question_idx][0][cg_cpu_selected_cards[cg_question_idx][0]] and cg_cpu2_card_score_list[cg_question_idx][cg_cards_on_hand[cg_mc_selected_card]] > cg_cpu2_score_list[cg_question_idx][2][cg_cpu_selected_cards[cg_question_idx][2]]:
                cg_current_winner = 3
                cg_winning_string = cg_get_mc_card_string(cg_mc_selected_card)
            elif cg_cpu2_score_list[cg_question_idx][0][cg_cpu_selected_cards[cg_question_idx][0]] > cg_cpu2_score_list[cg_question_idx][2][cg_cpu_selected_cards[cg_question_idx][2]]:
                cg_current_winner = 0
            else:
                cg_current_winner = 2
        elif cg_reader == 2:
            if cg_cpu3_card_score_list[cg_question_idx][cg_cards_on_hand[cg_mc_selected_card]] > cg_cpu3_score_list[cg_question_idx][0][cg_cpu_selected_cards[cg_question_idx][0]] and cg_cpu3_card_score_list[cg_question_idx][cg_cards_on_hand[cg_mc_selected_card]] > cg_cpu3_score_list[cg_question_idx][1][cg_cpu_selected_cards[cg_question_idx][1]]:
                cg_current_winner = 3
                cg_winning_string = cg_get_mc_card_string(cg_mc_selected_card)
            elif cg_cpu3_score_list[cg_question_idx][0][cg_cpu_selected_cards[cg_question_idx][0]] > cg_cpu3_score_list[cg_question_idx][1][cg_cpu_selected_cards[cg_question_idx][1]]:
                cg_current_winner = 0
            else:
                cg_current_winner = 1
        
        if cg_current_winner < 3:
            cg_get_winning_cpu_string()
        return

    def cg_update_scores():
        global cg_current_winner
        global cg_winner
        global cg_leader
        cg_scores[cg_current_winner] += 1
        
        cg_leader = []
        if cg_scores[0] == max(cg_scores) and max(cg_scores) > 0:
            cg_leader.append("Derek")
        if cg_scores[1] == max(cg_scores) and max(cg_scores) > 0:
            cg_leader.append("Maya")
        if cg_scores[2] == max(cg_scores) and max(cg_scores) > 0:
            cg_leader.append("Sage")
        if cg_scores[3] == max(cg_scores) and max(cg_scores) > 0:
            cg_leader.append("You")
        
        if cg_scores[cg_current_winner] == 5:
            if cg_current_winner == 0:
                cg_winner = "Derek"
            elif cg_current_winner == 1:
                cg_winner = "Maya"
            elif cg_current_winner == 2:
                cg_winner = "Sage"
            else:
                cg_winner = "MC"
            renpy.jump("cg_game_over_label")
        return

    def cg_get_winning_cpu_string():
        global cg_winning_string
        global cg_cpu_answers_list
        global cg_question_idx
        global cg_current_winner
        global cg_cpu_selected_cards
        cg_winning_string = cg_cpu_answers_list[cg_question_idx][cg_current_winner][cg_cpu_selected_cards[cg_question_idx][cg_current_winner]]
        return

    def cg_get_cpu_string(idx):
        global cg_cpu_answers_list
        global cg_cpu_selected_cards
        global cg_question_idx
        return cg_cpu_answers_list[cg_question_idx][idx][cg_cpu_selected_cards[cg_question_idx][idx]]

    def cg_get_response_style(score):
        if score < 2:
            return "very bad"
        elif score < 4:
            return "bad"
        elif score < 8:
            return "fun"
        else:
            return "very fun"

    def cg_shuffle_responses():
        global cg_answers_and_reactions
        global cg_read_idx
        global cg_reader
        global cg_question_idx
        global cg_mc_selected_card
        global cg_cpu1_card_score_list
        global cg_cpu2_card_score_list
        global cg_cpu3_card_score_list
        global cg_cpu1_score_list
        global cg_cpu2_score_list
        global cg_cpu3_score_list
        global cg_cpu_selected_cards
        global cg_cards_on_hand
        
        cg_read_idx = 0
        cg_answers_and_reactions = []
        
        if cg_reader == 0:
            cg_answers_and_reactions.append([cg_get_mc_card_string(cg_mc_selected_card), cg_get_response_style(cg_cpu1_card_score_list[cg_question_idx][cg_cards_on_hand[cg_mc_selected_card]])])
            cg_answers_and_reactions.append([cg_get_cpu_string(1), cg_get_response_style(cg_cpu1_score_list[cg_question_idx][1][cg_cpu_selected_cards[cg_question_idx][1]])])
            cg_answers_and_reactions.append([cg_get_cpu_string(2), cg_get_response_style(cg_cpu1_score_list[cg_question_idx][2][cg_cpu_selected_cards[cg_question_idx][2]])])
        elif cg_reader == 1:
            cg_answers_and_reactions.append([cg_get_mc_card_string(cg_mc_selected_card), cg_get_response_style(cg_cpu2_card_score_list[cg_question_idx][cg_cards_on_hand[cg_mc_selected_card]])])
            cg_answers_and_reactions.append([cg_get_cpu_string(0), cg_get_response_style(cg_cpu2_score_list[cg_question_idx][0][cg_cpu_selected_cards[cg_question_idx][0]])])
            cg_answers_and_reactions.append([cg_get_cpu_string(2), cg_get_response_style(cg_cpu2_score_list[cg_question_idx][2][cg_cpu_selected_cards[cg_question_idx][2]])])
        elif cg_reader == 2:
            cg_answers_and_reactions.append([cg_get_mc_card_string(cg_mc_selected_card), cg_get_response_style(cg_cpu3_card_score_list[cg_question_idx][cg_cards_on_hand[cg_mc_selected_card]])])
            cg_answers_and_reactions.append([cg_get_cpu_string(0), cg_get_response_style(cg_cpu3_score_list[cg_question_idx][0][cg_cpu_selected_cards[cg_question_idx][0]])])
            cg_answers_and_reactions.append([cg_get_cpu_string(1), cg_get_response_style(cg_cpu3_score_list[cg_question_idx][1][cg_cpu_selected_cards[cg_question_idx][1]])])
        else:
            cg_answers_and_reactions.append([cg_get_cpu_string(0), 0])
            cg_answers_and_reactions.append([cg_get_cpu_string(1), 1])
            cg_answers_and_reactions.append([cg_get_cpu_string(2), 2])
        renpy.random.shuffle(cg_answers_and_reactions)
        return

    def cg_get_reaction_string(str, reaction):
        global cg_reader
        if cg_reader == 0:
            return cg_get_reaction_derek(str, reaction)
        elif cg_reader == 1:
            return cg_get_reaction_maya(str, reaction)
        elif cg_reader == 2:
            return cg_get_reaction_sage(str, reaction)
        else:
            return cg_get_reaction_mc(str, reaction)

    def cg_get_reaction_derek(str, reaction):
        global cg_derek_vb_responses
        global cg_derek_b_responses
        global cg_derek_f_responses
        global cg_derek_vf_responses
        global cg_question_idx
        
        if "Vaseline." == str:
            return "HAHA! Vaseline and what...?"
        elif "Spaghetti." == str:
            return "Haha! Why spaghetti?"
        elif "Tiny hats." == str:
            return "Haha! We should have bought those for this party."
        elif "Money." == str:
            return "Haha. Yeah, if I had a shitload of cash I sure wouldn't be depressed."
        elif "Doing things." == str:
            return "Haha! Yeah, no shit."
        elif "A bowl of fruit." == str:
            return "A bowl of fruit? What? Why?"
        elif "An encyclopedia." == str:
            return "Nerd alert."
        elif "My belly button." == str:
            return "Haha! Stay away from my belly button."
        elif "69." == str:
            return "Haha! Funny, but also gross depending on who played the card."
        elif "Ketchup on a wiener." == str:
            return "BAHAHA! Gross!"
        elif "Butt sex." == str:
            return "HAHA! An obvious but perfect answer."
        elif "My first time." == str:
            return "HAHA! You don't say."
        elif "A monkey." == str:
            return "Hahaha! It sure would."
        elif "Low inhibitions." == str:
            return "Haha! Yes. That would do it."
        elif "A million dollars." == str:
            return "Hahaha! Only a million?"
        elif "A banana." == str:
            return "I bet I know what you did with that banana. Haha!"
        elif "Driving too slow to piss people off." == str:
            return "I hate it when they do that. Haha!"
        elif "Being horny all the time." == str:
            return "Hahaha! That's so gonna be me."
        elif "Drinking water." == str:
            return "Haha! That's a good skill to have."
        elif "Peace and love." == str:
            return "I suppose you could."
        elif "Eating lasagna." == str:
            return "Hahaha! What a fatty."
        elif "Shutting the fuck up." == str:
            return "Hahaha! I'm no expert, but I don't think that's it."
        elif "A poem about your reproductive organ." == str:
            return "Haha! No way! That's a keeper!"
        elif "Shaving your cat." == str:
            return "Haha! Shaving your pussy on the other hand... Now that's funny."
        elif "Gloryholes." == str:
            return "Haha! I swear, there's one of those at school. It's crazy!"
        elif "MEOW!" == str:
            return "Rock paper MEOW! Haha! I'd play that."
        elif "Camel toe." == str:
            return "HAHAHA! Best answer ever."
        elif "A Chinese woman." == str:
            return "HAHA! Why is that so funny? It's so random."
        elif "Breast milk." == str:
            return "HAHA! That would make me move to Canada. Canada is third-world, right?"
        elif "Silently nodding while zoning out." == str:
            return "HAHA! I do that all the time."
        elif "A handshake." == str:
            return "Haha! That's one bad date."
        
        if "A finger in the anus." == str and cg_question_idx == 0:
            return "BAHAHA! That wouldn't cure me!"
        elif "Violent diarrhea." == str and cg_question_idx == 0:
            return "What a shitty cure. Literally."
        elif "Too many orgasms." == str and cg_question_idx == 0:
            return "Haha! Yes. Man... I envy girls. If I were a girl, I'd cum so many times."
        elif "A crusty cum sock." == str and cg_question_idx == 0:
            return "Haha! Man's best friend, am I right?"
        elif "Gay porn." == str and cg_question_idx == 0:
            return "Haha! Sign me up for some lesbian porn."
        elif "A finger in the anus." == str and cg_question_idx == 0:
            return "HAHA! It depends on whose finger."
        elif "A finger in the anus." == str and cg_question_idx == 1:
            return "BAHAHA! Like a human finger puppet."
        elif "A finger in the anus." == str and cg_question_idx == 3:
            return "HAHA! Sounds like a best seller!"
        elif "Ok, grandpa. Let's get you to bed." == str and cg_question_idx == 3:
            return "HAHAHA! Not grandpa!"
        elif "Sperm." == str and cg_question_idx == 5:
            return "Haha! Hey! Me too!"
        elif "Nothing." == str and cg_question_idx == 6:
            return "Haha! Yes! Very relatable."
        elif "Sperm." == str and cg_question_idx == 7:
            return "Absolutely disgusting. I love it!"
        elif "Nothing." == str and cg_question_idx == 8:
            return "Haha! I feel this one was aimed at me. It's sad, but true."
        elif "Your girlfriend." == str and cg_question_idx == 8:
            return "That's cute and sexist at the same time."
        elif "Gay porn." == str and cg_question_idx == 10:
            return "Hahaha! That's the mother of the year."
        elif "Violent diarrhea." == str and cg_question_idx == 11:
            return "Hahaha! Beggars can't be choosers."
        elif "A finger in the anus." == str and cg_question_idx == 13:
            return "HAHA! What a hardcore version of it."
        elif "Nothing." == str and cg_question_idx == 16:
            return "HAHA! Spot on."
        elif "Sperm." == str and cg_question_idx == 16:
            return "HAHA! Go ahead and build that pipeline. I'll contribute!"
        elif "Yatzy!" == str and cg_question_idx == 18:
            return "HAHAHA! What a fucking loser!"
        elif "Snorting cocaine." == str and cg_question_idx == 19:
            return "HAHAHA! It sure isn't."
        elif "A finger in the anus." == str and cg_question_idx == 19:
            return "HAHAHA! More like Show and Smell, am I right?"
        
        if reaction == "very bad":
            return cg_derek_vb_responses[renpy.random.randint(0,len(cg_derek_vb_responses)-1)]
        elif reaction == "bad":
            return cg_derek_b_responses[renpy.random.randint(0,len(cg_derek_b_responses)-1)]
        elif reaction == "fun":
            return cg_derek_f_responses[renpy.random.randint(0,len(cg_derek_f_responses)-1)]
        else:
            return cg_derek_vf_responses[renpy.random.randint(0,len(cg_derek_vf_responses)-1)]

    def cg_get_reaction_maya(str, reaction):
        global cg_maya_vb_responses
        global cg_maya_b_responses
        global cg_maya_f_responses
        global cg_maya_vf_responses
        global cg_question_idx
        
        if "Drinking all night long." == str:
            return "Cheers! That could work."
        elif "A fistful of parsely." == str:
            return "Hahaha! Why is that funny?"
        elif "Tiny hats." == str:
            return "Hahaha! That's so stupid, but it would make me feel happier."
        elif "Lube." == str:
            return "Why do I feel like Derek played this one?"
        elif "Eight other dudes." == str:
            return "Haha! Doing what?"
        elif "Two condoms." == str:
            return "Haha! Two?"
        elif "Grandma." == str:
            return "Haha! I don't want to know what you'd do with grandma."
        elif "A bouncy castle." == str:
            return "Hahaha! Yes! That sounds like a perfect night!"
        elif "My Mom's friend Susan." == str:
            return "Hahaha! Oh, no. Not Susan! I won't be able to look her in the eyes now."
        elif "Getting wet." == str:
            return "Hahaha! Yes, that would be it."
        elif "An inappropriate cluck on Rooster." == str:
            return "Haha! Although topical, let's not have another one of those."
        elif "Poop." == str:
            return "Poop? Really? That's so juvenile."
        elif "Boogers." == str:
            return "EWW! That's just nasty."
        elif "Boner." == str:
            return "Haha. The only thing amusing about that one is that it's grammatically incorrect."
        elif "Shaving my balls." == str:
            return "Haha! I can tell you for a fact that I don't dream of doing that."
        elif "Posting awesome memes." == str:
            return "Hahaha! By then, memes will probably be way retro. That's scary to think about."
        elif "AIDS." == str:
            return "No. Not funny. Just horrible."
        elif "Unpaid parking tickets." == str:
            return "Haha! Yeah, he could afford paying those."
        elif "A blowjob." == str:
            return "NO! That's so inappropriate! EWW!"
        elif "Farting." == str:
            return "Really? A fart joke? I hate that it made me laugh. Haha!"
        elif "Having an affair." == str:
            return "That's not something I'd recommend doing. Haha!"
        elif "A fucking goat." == str:
            return "Hahaha! That curse word made it more fun."
        elif "A bucket of coleslaw." == str:
            return "Hahaha! You guys are so weird!"
        elif "Children." == str:
            return "Clearly we have different red flags."
        elif "Pineapple on a pizza." == str:
            return "Yes! Haha! Not on my pizza!"
        elif "People I don't like." == str:
            return "Haha! Probably because that essay was too long."
        elif "Fart." == str:
            return "Hahaha! NO! Fart jokes aren't supposed to be funny! HAHAHA!"
        elif "A fingernail." == str:
            return "Derek... I know this one was you. It's not funny..."
        elif "Sand." == str:
            return "Haha. Insensitive, but amusing."
        elif "Leftovers." == str:
            return "Haha! That's mean!"
        elif "A hickey." == str:
            return "Haha! If that won't make you fight for first place, nothing will."
        elif "Peekaboo!" == str:
            return "Hahaha! What a numbskull."
        elif "Making babies." == str:
            return "Haha! You guys are funny."
        
        if "Yatzy!" == str and cg_question_idx == 0:
            return "Hahaha! That's so stupid!"
        elif "Laughter." == str and cg_question_idx == 0:
            return "Hahaha! Corny but hilarious! It's the best medicine, after all."
        elif "Building sandcastles." == str and cg_question_idx == 1:
            return "Hahaha! You can't tell me what it is? But building sandcastles is very specific."
        elif "Yatzy!" == str and cg_question_idx == 2:
            return "Hahaha! Yay!"
        elif "Mayonaisse." == str and cg_question_idx == 2:
            return "Haha! What the hell are we going to do with mayo?"
        elif "A short adventure." == str and cg_question_idx == 3:
            return "Hahaha! How short are we talking about?"
        elif "Ok, grandpa. Let's get you to bed." == str and cg_question_idx == 5:
            return "Haha! That fits in perfectly!"
        elif "Birthday cake." == str and cg_question_idx == 7:
            return "Hahaha! That's clever and funny!"
        elif "Snorting cocaine." == str and cg_question_idx == 8:
            return "Hahaha! Who the hell played this one!? Oh my God!"
        elif "Snorting cocaine." == str and cg_question_idx == 13:
            return "Haha! Who would have thought the Professor wouldn't enjoy that?"
        elif "Violent diarrhea." == str and cg_question_idx == 9:
            return "Eww! Gross! That's not funny."
        elif "Gay porn." == str and cg_question_idx == 10:
            return "Hahaha! This is so not politically correct. It's so funny."
        elif "STDs." == str and cg_question_idx == 11:
            return "Hahaha! As people on dates often do."
        elif "Nothing." == str and cg_question_idx == 16:
            return "Haha! What a cruel answer!"
        elif "Your Mom." == str and cg_question_idx == 19:
            return "Haha! Yeah, that would be weird."
        elif "Your Mom." == str and cg_question_idx == 15:
            return "Haha! That's so stupid."
        elif "69" == str and cg_question_idx == 2:
            return "Haha! That sounds like a fun night."
        
        if reaction == "very bad":
            return cg_maya_vb_responses[renpy.random.randint(0,len(cg_maya_vb_responses)-1)]
        elif reaction == "bad":
            return cg_maya_b_responses[renpy.random.randint(0,len(cg_maya_b_responses)-1)]
        elif reaction == "fun":
            return cg_maya_f_responses[renpy.random.randint(0,len(cg_maya_f_responses)-1)]
        else:
            return cg_maya_vf_responses[renpy.random.randint(0,len(cg_maya_vf_responses)-1)]

    def cg_get_reaction_sage(str, reaction):
        global cg_sage_vb_responses
        global cg_sage_b_responses
        global cg_sage_f_responses
        global cg_sage_vf_responses
        global cg_question_idx
        
        if "Vaseline." == str:
            return "Haha! I guess it depends on what you do with it."
        elif "Money." == str:
            return "Haha! It's probably true."
        elif "A bowl of fruit." == str:
            return "Hahaha! What fucking hobby would that be?"
        elif "Grandma." == str:
            return "Hahaha! I've got more questions after hearing that answer."
        elif "My boss's wife.." == str:
            return "Hah! That's naughty."
        elif "Shredding top-secret documents." == str:
            return "Haha! Yes, I'll be your partner in crime. Sign me up!"
        elif "A filthy pig." == str:
            return "Hahaha! The only one I'm sure didn't play this card is Maya."
        elif "Disappointment." == str:
            return "Haha! I'd say that's a common name for it."
        elif "Poop." == str:
            return "Haha! I'm highly skeptical that it would."
        elif "My left hand." == str:
            return "Haha! That's so sad."
        elif "A million dollars." == str:
            return "Hahaha! Yeah! Fucking spoiled brats."
        elif "Smiling when you feel dead inside." == str:
            return "Haha! I sure hope this isn't my future."
        elif "Three tomatoes and an onion." == str:
            return "Haha! That's so random, but funny."
        elif "AIDS." == str:
            return "Haha! Am I really going to pick an AIDS joke as the best? I think I might..."
        elif "Failing tests." == str:
            return "Hahaha! That's so evil!"
        elif "Being sassy." == str:
            return "Hahaha! Mhm!"
        elif "A double-headed dildo." == str:
            return "Haha! Mama better not buy me that."
        elif "A hamster." == str:
            return "Hahaha! Why a hamster!?"
        elif "Shaving your cat." == str:
            return "Hahaha! Yes, you better run!"
        elif "MEOW!" == str:
            return "Hahaha! How do you play that? What does meowing do!?"
        elif "A fingernail." == str:
            return "Hahaha! Too soon! Right, Derek?"
        elif "Two dollars." == str:
            return "Hahaha! The generosity is unparalleled."
        elif "A hip hip hooray!" == str:
            return "Hahaha! I guess they ran out of prize money."
        elif "Dessert." == str:
            return "Hahaha! It's so mundane it is funny."
        elif "A bunch of fireworks." == str:
            return "Hahaha! That sounds like something Derek would bring."
        elif "A handshake." == str:
            return "Haha! Not a keeper of a date."
        
        if "Violent diarrhea." == str and cg_question_idx == 0:
            return "Hahaha! I don't think it is! But I bet it makes you forget about the depression for a while."
        elif "Snorting cocaine." == str and cg_question_idx == 0:
            return "Hahaha! Now, there's bad advice and there's {b}bad{/b} advice."
        elif "Violent diarrhea." == str and cg_question_idx == 1:
            return "Hahaha! So gross! What could that hobby even be?"
        elif "Too many orgasms." == str and cg_question_idx == 1:
            return "Hahaha! Sign me up for that hobby!"
        elif "Mayonaisse." == str and cg_question_idx == 1:
            return "Haha! Whatever that is, it's good that it's just a hobby and not a profession."
        elif "Yatzy!" == str and cg_question_idx == 2:
            return "Haha! What a wild night that would be."
        elif "A crusty cum sock." == str and cg_question_idx == 3:
            return "Top-notch comedy. Haha!"
        elif "A finger in the anus." == str and cg_question_idx == 3:
            return "Kinky! HAHA!"
        elif "Yatzy!" == str and cg_question_idx == 4:
            return "Haha! I think this game is enough for this party."
        elif "Your girlfriend." == str and cg_question_idx == 6:
            return "Haha! Dream big!"
        elif "A finger in the anus." == str and cg_question_idx == 7:
            return "Haha! The immature answers are fucking funny."
        elif "Mayonaisse." == str and cg_question_idx == 13:
            return "Hahaha! An instant classic."
        elif "Your Mom." == str and cg_question_idx == 15:
            return "Haha! Yeah, she's very helpful. I'm sure you did."
        elif "Laughter." == str and cg_question_idx == 17:
            return "Haha. What a shitty prize."
        elif "STDs." == str and cg_question_idx == 18:
            return "Haha. Worst date ever!"
        
        if reaction == "very bad":
            return cg_sage_vb_responses[renpy.random.randint(0,len(cg_sage_vb_responses)-1)]
        elif reaction == "bad":
            return cg_sage_b_responses[renpy.random.randint(0,len(cg_sage_b_responses)-1)]
        elif reaction == "fun":
            return cg_sage_f_responses[renpy.random.randint(0,len(cg_sage_f_responses)-1)]
        else:
            return cg_sage_vf_responses[renpy.random.randint(0,len(cg_sage_vf_responses)-1)]

    def cg_get_reaction_mc(str, reaction):
        global cg_mc_f_responses
        global cg_mc_b_responses
        
        if reaction == "fun":
            return cg_mc_f_responses[renpy.random.randint(0,len(cg_mc_f_responses)-1)]
        else:
            return cg_mc_b_responses[renpy.random.randint(0,len(cg_mc_b_responses)-1)]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
