image IntroAni0 = qAnimation("IntroAni/IntroAni{}.png", 0.01, 10, False)
image IntroAni1 = qAnimation("IntroAni/IntroAni{}.png", 0.01, 19, False, startNr=11)
image IntroAni2 = qAnimation("IntroAni/IntroAni{}.png", 0.01, 30, False, startNr=20)
image IntroAni3 = qAnimation("IntroAni/BIntroAni{}.png", 0.01, 19, False, True, 11)
image IntroAni4 = qAnimation("IntroAni/IntroAni{}.png", 0.01, 10, False, True)
image IntroAni5 = qAnimation("IntroAni/IntroAni{}.png", 0.01, 19, False, True, startNr=11)
image IntroAni6 = qAnimation("IntroAni/IntroAni{}.png", 0.01, 30, False, True, startNr=20)

image RayxAdam0 = qAnimation("AdamxRayBJ/AdamxRayAni_{}.png", 0.025, 19, startNr=0)
image RayxAdam1 = qAnimation("AdamxRayBJ/AdamxRayAni_{}.png", 0.025, 39, reverse=True, startNr=20)
image RayxAdam2 = qAnimation("AdamxRayBJ/AdamxRayAni_{}.png", 0.025, 39, repeat=True, startNr=20, bck=True)
image RayxAdamAni:
    "RayxAdam0"
    pause 0.5
    "RayxAdam1"
    pause 0.5
    "RayxAdam2"

image DonnaxNateAni = Movie(play="images/DonnaxNate.webm",  start_image="images/DonnaxNate.png")
image MCxLillyHJAni = qAnimation("MCxLillyHJ/MCxLilly_{}.png", 0.025, 40, repeat=True, startNr=0, bck=True)
image MCxLillyRAni = qAnimation("MCxLillyR/MCxLilly_{}.png", 0.025, 39, repeat=True, startNr=0, bck=True)
image MCxLillyDoggyAni = Movie(play="images/MCxLillyDoggy.webm",  start_image="images/MCxLillyDoggy.png")
image Scene1039 = Movie(play="images/Scene1039.webm",  start_image="images/Scene1039Start.png")
image Scene1042 = Movie(play="images/Scene1042.webm",  start_image="images/Scene1042Start.png")

image Scene1333 = Movie(play="images/Scene1333.webm", start_image="images/Scene1333Start.webp")
image Scene1356 = Movie(play="images/Scene1356.webm", start_image="images/Scene1356Start.webp")

image Scene1551 = Movie(play="images/Scene1551.webm", start_image="images/Scene1551Start.webp")
image Scene1714 = Movie(play="images/Scene1714.webm", start_image="images/Scene1714Start.webp")

image Scene2167B = Movie(play="images/Scene2167B.webm", start_image="images/Scene2167BStart.webp")
image Scene2249 = Movie(play="images/Scene2249.webm", start_image="images/Scene2249Start.webp")
image Scene2250B = Movie(play="images/Scene2250B.webm", start_image="images/Scene2250BStart.webp")

image Scene2422 = Movie(play="images/Scene2422.webm", start_image="images/Scene2422Start.webp")

image Scene2513 = Movie(play="images/Scene2513.webm", start_image="images/Scene2513Start.webp")

image Scene2653Ani:
    "images/Scene2653A.webp" with vpunch
    pause 1
    "images/Scene2653B.webp" with vpunch
    pause 1
    "images/Scene2653C.webp" with vpunch
    pause 1
    "images/Scene2653B.webp" with vpunch
    pause 1
    repeat

image Scene2782 = Movie(play="images/Scene2782.webm", start_image="images/Scene2782Start.webp")
image Scene2916 = Movie(play="images/Scene2916.webm", start_image="images/Scene2916Start.webp")

image Scene3203Ani = Movie(play="images/Scene3203.webm", start_image="images/Scene3203Start.webp")
image Scene3205Ani = Movie(play="images/Scene3205.webm", start_image="images/Scene3205Start.webp")
image Scene3207 = Movie(play="images/Scene3207.webm", start_image="images/Scene3207Start.webp")

image Scene3490Ani = Movie(play="images/Scene3490.webm", start_image="images/Scene3490Start.webp")
image Scene3520 = Movie(play="images/Scene3520.webm", start_image="images/Scene3520Start.webp")
image Scene3521 = Movie(play="images/Scene3521.webm", start_image="images/Scene3521Start.webp")

image Scene3855 = Movie(play="images/Scene3855.webm", start_image="images/Scene3855Start.webp")
image Scene3856 = Movie(play="images/Scene3856.webm", start_image="images/Scene3856Start.webp")
image SceneRxMCAni = Movie(play="images/RxMC.webm", start_image="images/SceneRxMCStart.webp")

image Scene4268Ani = Movie(play="images/Scene4268Ani.webm", start_image="images/Scene4268Start.webp")
image Scene4367Ani = Movie(play="images/Scene4367Ani.webm", start_image="images/Scene4367Start.webp", loop=-1)

image Scene4494Ani = Movie(play="images/Scene4494Ani.webm", start_image="images/Scene4494Start.webp", loop=-1)
image Scene4495Ani = Movie(play="images/Scene4495Ani.webm", start_image="images/Scene4495Start.webp", loop=-1)
image Scene4559Ani = Movie(play="images/Scene4559Ani.webm", start_image="images/Scene4559Start.webp", loop=-1)
image Scene4564Ani = Movie(play="images/Scene4564Ani.webm", start_image="images/Scene4564Start.webp", loop=-1)

image Scene4675Ani = Movie(play="images/Scene4675Ani.webm", start_image="images/Scene4675Start.webp", loop=-1)

image Scene4860Ani = Movie(play="images/Scene4860Ani.webm", start_image="images/Scene4860Start.webp", loop=-1)

image Scene4954Ani = Movie(play="images/Scene4954Ani.webm", start_image="images/Scene4954Start.webp", loop=-1)
image Scene4955Ani = Movie(play="images/Scene4955Ani.webm", start_image="images/Scene4955Start.webp", loop=-1)
image Scene4978Ani = Movie(play="images/Scene4978Ani.webm", start_image="images/Scene4978Start.webp", loop=-1)
image Scene5161Ani = Movie(play="images/Scene5161Ani.webm", start_image="images/Scene5161Start.webp", loop=-1)

image Scene5401Ani = Movie(play="images/Scene5401Ani.webm", start_image="images/Scene5401Start.webp", loop=-1)

image Scene5666Ani = Movie(play="images/Scene5666Ani.webm", start_image="images/Scene5666Start.webp", loop=-1)
image Scene5674Ani = Movie(play="images/Scene5674Ani.webm", start_image="images/Scene5674Start.webp", loop=-1)
image Scene5640ani = Movie(play="images/Scene5640Ani.webm", start_image="images/Scene5640Start.webp", loop=-1)

image Scene5823Ani = Movie(play="images/Scene5823Ani.webm", start_image="images/Scene5823Start.webp", loop=-1)

image Scene6002Ani = Movie(play="images/Scene6002Ani.webm", start_image="images/Scene6002Start.webp", loop=-1)
image Scene6005Ani = Movie(play="images/Scene6005Ani.webm", start_image="images/Scene6005Start.webp", loop=-1)
image Scene6117Ani = Movie(play="images/Scene6117Ani.webm", start_image="images/Scene6117Start.webp", loop=-1)
image Scene6168Ani = Movie(play="images/Scene6168Ani.webm", start_image="images/Scene6168Start.webp", loop=-1)

image Scene6418Ani = Movie(play="images/Scene6418Ani.webm", start_image="images/Scene6418Start.webp", loop=-1)
image Scene6419Ani = Movie(play="images/Scene6419Ani.webm", start_image="images/Scene6419Start.webp", loop=-1)
image Scene6420Ani = Movie(play="images/Scene6420Ani.webm", start_image="images/Scene6420Start.webp", loop=-1)
image Scene6421Ani = Movie(play="images/Scene6421Ani.webm", start_image="images/Scene6421Start.webp", loop=-1)

image Scene6638Ani = Movie(play="images/Scene6638Ani.webm", start_image="images/Scene6638Start.webp", loop=-1)

image Scene7031Ani = Movie(play="images/Scene7031Ani.webm", start_image="images/Scene7031Start.webp", loop=-1)
image Scene7088Ani = Movie(play="images/Scene7088Ani.webm", start_image="images/Scene7088Start.webp", loop=-1)
image Scene7174Ani = Movie(play="images/Scene7174Ani.webm", start_image="images/Scene7174Start.webp", loop=-1)

image Scene7357Ani = Movie(play="images/Scene7357Ani.webm", start_image="images/Scene7357Start.webp", loop=-1)

image Scene7446Ani = Movie(play="images/Scene7446Ani.webm", start_image="images/Scene7446Start.webp", loop=-1)

image Scene7776Ani = Movie(play="images/Scene7776Ani.webm", start_image="images/Scene7776Start.webp", loop=-1)

image Scene7956Ani = Movie(play="images/Scene7956Ani.webm", start_image="images/Scene7956Start.webp", loop=-1)
image Scene7957Ani = Movie(play="images/Scene7957Ani.webm", start_image="images/Scene7957Start.webp", loop=-1)
image Scene7957BAni = Movie(play="images/Scene7957BAni.webm", start_image="images/Scene7957BStart.webp", loop=-1)

image Scene8054Ani = Movie(play="images/Scene8054Ani.webm", start_image="images/Scene8054Start.webp", loop=-1)

image Scene8279Ani = Movie(play="images/Scene8279Ani.webm", start_image="images/Scene8279Start.webp", loop=-1)

image Scene8475Ani = Movie(play="images/Scene8475Ani.webm", start_image="images/Scene8475Start.webp", loop=-1)

image Scene8592Ani = Movie(play="images/Scene8592Ani.webm", start_image="images/Scene8592Start.webp", loop=-1)
image Scene8662Ani = Movie(play="images/Scene8662Ani.webm", start_image="images/Scene8662Start.webp", loop=-1)

image Scene8764Ani = Movie(play="images/Scene8764Ani.webm", start_image="images/Scene8764Start.webp", loop=-1)

image Scene9032Ani = Movie(play="images/Scene9032Ani.webm", start_image="images/Scene9032Start.webp", loop=-1)

image Scene9127Ani = Movie(play="images/Scene9127Ani.webm", start_image="images/Scene9127Start.webp", loop=-1)
image Scene9225Ani = Movie(play="images/Scene9225Ani.webm", start_image="images/Scene9225Start.webp", loop=-1)

image Scene9261Ani = Movie(play="images/Scene9261Ani.webm", start_image="images/Scene9261Start.webp", loop=-1)
image Scene9267Ani = Movie(play="images/Scene9267Ani.webm", start_image="images/Scene9267Start.webp", loop=-1)
image Scene9269Ani = Movie(play="images/Scene9269Ani.webm", start_image="images/Scene9269Start.webp", loop=-1)

image Scene9442Ani = Movie(play="images/Scene9442Ani.webm", start_image="images/Scene9442Start.webp", loop=-1)
image Scene9443Ani = Movie(play="images/Scene9443Ani.webm", start_image="images/Scene9443Start.webp", loop=-1)

image Scene9851Ani = Movie(play="images/Scene9851Ani.webm", start_image="images/Scene9851Start.webp", loop=-1)
image Scene9852Ani = Movie(play="images/Scene9852Ani.webm", start_image="images/Scene9852Start.webp", loop=-1)

image Scene10195Ani = Movie(play="images/Scene10195Ani.webm", start_image="images/Scene10195Start.webp", loop=-1)

image Scene10269Ani = Movie(play="images/Scene10269Ani.webm", start_image="images/Scene10269Start.webp", loop=-1)
image Scene10378Ani = Movie(play="images/Scene10378Ani.webm", start_image="images/Scene10378Start.webp", loop=-1)

image Scene10439Ani = Movie(play="images/Scene10439Ani.webm", start_image="images/Scene10439Start.webp", loop=-1)
image Scene10520Ani = Movie(play="images/Scene10520Ani.webm", start_image="images/Scene10520Start.webp", loop=-1)

image Scene10742Ani = Movie(play="images/Scene10742Ani.webm", start_image="images/Scene10742Start.webp", loop=-1)
image Scene10789Ani = Movie(play="images/Scene10789Ani.webm", start_image="images/Scene10789Start.webp", loop=-1)
image Scene10790Ani = Movie(play="images/Scene10790Ani.webm", start_image="images/Scene10790Start.webp", loop=-1)

image Scene10927Ani = Movie(play="images/Scene10927Ani.webm", start_image="images/Scene10927Start.webp", loop=-1)

image Scene11116Ani = Movie(play="images/Scene11116Ani.webm", start_image="images/Scene11116Start.webp", loop=-1)

image Scene11420Ani = Movie(play="images/Scene11420Ani.webm", start_image="images/Scene11420Start.webp", loop=-1)
image Scene11475Ani = Movie(play="images/Scene11475Ani.webm", start_image="images/Scene11475Start.webp", loop=-1)
image Scene11515Ani = Movie(play="images/Scene11515Ani.webm", start_image="images/Scene11515Start.webp", loop=-1)

image Scene11716Ani = Movie(play="images/Scene11716Ani.webm", start_image="images/Scene11716Start.webp", loop=-1)
image Scene11721Ani = Movie(play="images/Scene11721Ani.webm", start_image="images/Scene11721Start.webp", loop=-1)

image Scene11747Ani = Movie(play="images/Scene11747Ani.webm", start_image="images/Scene11747Start.webp", loop=-1)
image Scene11856Ani = Movie(play="images/Scene11856Ani.webm", start_image="images/Scene11856Start.webp", loop=-1)

image Scene11988Ani = Movie(play="images/Scene11988Ani.webm", start_image="images/Scene11988Start.webp", loop=-1)

image Scene12077Ani = Movie(play="images/Scene12077Ani.webm", start_image="images/Scene12077Start.webp", loop=-1)

image IntroAniA:
    "IntroAni0"
    pause 0.1
    "IntroAni1"
    pause 0.08
    "IntroAni2"
    pause 0.1

image IntroAniB:
    "IntroAni6"
    pause 0.1
    "IntroAni5"
    pause 0.08
    "IntroAni4"
    pause 0.1

image IntroAniC:
    "IntroAni6"
    pause 0.1
    "IntroAni3"
    pause 0.08
    "IntroAni4"
    pause 0.1

image IntroAni:
    "IntroAniA"
    pause 0.28
    "IntroAniB"
    pause 0.28
    "IntroAniA"
    pause 0.28
    "IntroAniB"
    pause 0.28
    "IntroAniA"
    pause 0.28
    "IntroAniB"
    pause 0.28
    "IntroAniA"
    pause 0.28
    "IntroAniB"
    pause 0.28
    "IntroAniA"
    pause 0.28
    "IntroAniB"
    pause 0.28
    "IntroAniA"
    pause 0.28
    "IntroAniB"
    pause 0.28
    "IntroAniA"
    pause 0.28
    "IntroAniB"
    pause 0.28
    "IntroAniA"
    pause 0.28
    "IntroAniC"
    pause 0.28
    repeat

image black = Solid("#000")
image alph = Solid("#fff2")

define faded = Fade(0.5, 1, 0.5)
