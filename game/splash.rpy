## splash screen is first thing that gets shown to player
init -100 python:
    # archive check for mods
    for archive in ['audio','images','fonts']:
        if archive not in config.archives:
            renpy.error("看样子你还没有把 DDLC 游戏的文件复制过去呐。")
    # if persistent.playthrough >= 1 and not persistent.disable_awful_music:
    #     config.main_menu_music = audio.t4g
    # t4g is too dark for a main menu music
# disclaimers
init python:
    menu_trans_time = 1

    splash_message_default = "这是非官方的粉丝向 Mod，与 Team Salvato 无关。\n本 Mod 不适合儿童或心理承受能力较弱的人。"

    splash_messages = [
        "请多多支持 Dan 鸽www",
        "Just Monika.",
        "在这里，成就 = 被吓死（",
        "您有 1/6 的几率在部室的海报上看到你的 DNA。\n如果你看到了这行警告，请加油触发（",
        "Dan 鸽也被自己的游戏吓到过 XD",
        "我不希望你连“儿童或心理承受能力较弱的人”的心理能被影响几成都搞不懂。",
        "我不希望你是个{i}瞎子{/i}，\n看不懂“本游戏不适合儿童或心理承受能力较弱的人”是什么意思。",
        "管管孩子，救救游戏",
        "为什么 Sayori 总是被迫害？"
    ]

image splash_warning = ParameterizedText(style="splash_text", xalign=0.5, yalign=0.5)


image menu_logo:
    "/mod_assets/2ndActEmu.png"
    subpixel True
    xcenter 240
    ycenter 120
    zoom 0.60
    menu_logo_move

image menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_move

image game_menu_bg:
    topleft
    "gui/menu_bg.png"
    menu_bg_loop

image menu_fade:
    "white"
    menu_fadeout

image menu_art_y:
    subpixel True
    "gui/menu_art_y.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n:
    subpixel True
    "gui/menu_art_n.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s:
    subpixel True
    "gui/menu_art_s.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m:
    subpixel True
    "gui/menu_art_m.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_y_ghost:
    subpixel True
    "gui/menu_art_y_ghost.png"
    xcenter 600
    ycenter 335
    zoom 0.60
    menu_art_move(0.54, 600, 0.60)

image menu_art_n_ghost:
    subpixel True
    "gui/menu_art_n_ghost.png"
    xcenter 750
    ycenter 385
    zoom 0.58
    menu_art_move(0.58, 750, 0.58)

image menu_art_s_ghost:
    subpixel True
    "gui/menu_art_s_ghost.png"
    xcenter 510
    ycenter 500
    zoom 0.68
    menu_art_move(0.68, 510, 0.68)

image menu_art_m_ghost:
    subpixel True
    "gui/menu_art_m_ghost.png"
    xcenter 1000
    ycenter 640
    zoom 1.00
    menu_art_move(1.00, 1000, 1.00)

image menu_art_s_glitch:
    subpixel True
    "gui/menu_art_s_break.png"
    xcenter 470
    ycenter 600
    zoom 0.68
    menu_art_move(.8, 470, .8)

image menu_nav:
    "gui/overlay/main_menu.png"
    menu_nav_move

image menu_particles:
    2.481
    xpos 224
    ypos 104
    ParticleBurst("gui/menu_particle.png", explodeTime=0, numParticles=20, particleTime=2.0, particleXSpeed=6, particleYSpeed=4).sm
    particle_fadeout

transform particle_fadeout:
    easeout 1.5 alpha 0

transform menu_bg_move:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat
    parallel:
        ypos 0
        time 0.65
        ease_cubic 2.5 ypos -500

transform menu_bg_loop:
    subpixel True
    topleft
    parallel:
        xoffset 0 yoffset 0
        linear 3.0 xoffset -100 yoffset -100
        repeat

transform menu_logo_move:
    subpixel True
    yoffset -300
    time 1.925
    easein_bounce 1.5 yoffset 0

transform menu_nav_move:
    subpixel True
    xoffset -500
    time 1.5
    easein_quint 1 xoffset 0

transform menu_fadeout:
    easeout 0.75 alpha 0
    time 2.481
    alpha 0.4
    linear 0.5 alpha 0

transform menu_art_move(z, x, z2):
    subpixel True
    yoffset 0 + (1200 * z)
    xoffset (740 - x) * z * 0.5
    zoom z2 * 0.75
    time 1.0
    parallel:
        ease 1.75 yoffset 0
    parallel:
        pause 0.75
        ease 1.5 zoom z2 xoffset 0

image intro:
    truecenter
    "white"
    0.5
    "bg/splash.png" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image warning:
    truecenter
    "white"
    "splash_warning" with Dissolve(0.5, alpha=True)
    2.5
    "white" with Dissolve(0.5, alpha=True)
    0.5

image tos = "bg/warning.png"
image tos2 = "bg/warning2.png"


init python:
    if not persistent.do_not_delete:

        import os
        try:
            if not os.access(config.basedir + "/characters/", os.F_OK):
                os.mkdir(config.basedir + "/characters")

        #     try: renpy.file("../characters/monika.chr")
        #     except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
        #     try: renpy.file("../characters/natsuki.chr")
        #     except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
        #     try: renpy.file("../characters/yuri.chr")
        #     except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
        #     try: renpy.file("../characters/sayori.chr")
        #     except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

            if persistent.playthrough <= 2:
                try: renpy.file("../characters/monika.chr")
                except: open(config.basedir + "/characters/monika.chr", "wb").write(renpy.file("monika.chr").read())
            if persistent.playthrough <= 1 or persistent.playthrough == 4:
                try: renpy.file("../characters/natsuki.chr")
                except: open(config.basedir + "/characters/natsuki.chr", "wb").write(renpy.file("natsuki.chr").read())
                try: renpy.file("../characters/yuri.chr")
                except: open(config.basedir + "/characters/yuri.chr", "wb").write(renpy.file("yuri.chr").read())
            if persistent.playthrough == 0 or persistent.playthrough == 4:
                try: renpy.file("../characters/sayori.chr")
                except: open(config.basedir + "/characters/sayori.chr", "wb").write(renpy.file("sayori.chr").read())

        except:
            pass

label splashscreen_warning:
    default persistent.first_run = False
    default invoking_warning_from_main_menu = False
    if not persistent.first_run or invoking_warning_from_main_menu:
        $ quick_menu = False
        scene white
        pause 0.5
        if persistent.recording:
            show game_menu_bg zorder 1
            with Dissolve(1.0)
        else:
            scene tos # may be no longer relevant
            with Dissolve(1.0)
        pause 1.0

        "[config.name] 是 Doki Doki Literature Club 的粉丝向 Mod，与 Team Salvato 无关。"
        "本 Mod 还在开发中，因此可能会遇到汉化不完全和其他 bug。"
        #if persistent.first_run:
            #$ gtext = glitchtext(7)
            #"{fast}我喜欢写 bug[gtext]{nw}"
            #$ history_list.pop()
        "因为本 Mod 包含大量剧透，所以本 Mod 理应在通关原游戏后再进行游玩。"
        "中文剧本内容基于 {a=https://steamcommunity.com/sharedfiles/filedetails/?id=1176221672}Steam 社区知名汉化版 DDLC{/a} 进行翻译并加以修改，在此致谢。"
        pause 1.0
        "请注意！由于本 Mod 包含原作的恐怖元素，焦虑症、抑郁症患者，以及儿童，均不适合游玩此 Mod。"
        "同时受“清朗”行动的影响，请谨慎游玩。"
        "请点击{a=https://ddlc.moe/warning.html}这里{/a}以查看原作恐怖内容的清单。（英文，含剧透）"
        pause 1.0
        "如果继续游玩 [config.name] 将视为你已经通关原游戏。"
        "与此同时，我们将视你为 16 岁以上，心理健康，且同意接受恐怖内容的玩家。"

        if not persistent.first_run:
            menu:
                "你想要继续吗？"
                "继续。":
                    if not persistent.recording:
                        scene tos2
                        with Dissolve(1.5)
                    "再次说明，本 Mod 为 DDLC 中文 Mod 模板的新 Demo。"
                    "接下来，您将体验到模板的许多特殊功能。"
                    jump splashwarning_final
                "退出。":
                    $ renpy.quit()
        else:
            if not persistent.recording:
                scene tos2
                with Dissolve(1.5)
            "既然你已经同意过了，我们也就不再需要你的意见了。"

        label splashwarning_final:
            "但是，如果感到不适，请立即退出游戏。"
            "祝您玩得愉快！"
            window hide
            pause 1.0
            pass
            scene white

            $ invoking_warning_from_main_menu = False
            $ persistent.first_run = True

    return

label splashscreen:

    if persistent.sayoricursor:
        $ config.mouse = {"default": [
                            ("gui/mouse/s_head.png", 0, 0),
                            ]}
    else:
        $ config.mouse = None


    python:
        firstrun = ""
        try:
            firstrun = renpy.file("firstrun").read(1)
        except:
            with open(config.basedir + "/game/firstrun", "wb") as f:
                pass
    if not firstrun:
        if persistent.first_run and not persistent.do_not_delete:
            $ quick_menu = False
            scene black
            "你似乎删除了 firstrun 文件，并且我们发现还有之前的存档。"
            menu:
                "是否删除存档并重置游戏？"
                "是的，删除存档":
                    "正在删除存档...{nw}"
                    python:
                        delete_all_saves()
                        renpy.loadsave.location.unlink_persistent()
                        renpy.persistent.should_save_persistent = False
                        renpy.utter_restart()
                "不，继续游戏":
                    pass

        python:
            if not firstrun:
                with open(config.basedir + "/game/firstrun", "w") as f:
                    f.write("1")
            filepath = renpy.file("firstrun").name
            open(filepath, "a").close()

    call splashscreen_warning

    python:
        basedir = config.basedir.replace('\\', '/')

    if persistent.autoload and not _restart:
        jump autoload

    # see diff for ghostmenu code!

    $ config.allow_skipping = False

    show white
    $ splash_message = splash_message_default
    $ renpy.music.play(config.main_menu_music)

    if persistent.playthrough == 2 and renpy.random.randint(0, 3) == 0:
        $ splash_message = renpy.random.choice(splash_messages)
    show splash_warning "[splash_message]" with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash_warning with Dissolve(0.5, alpha=True)
    $ config.allow_skipping = True
    return

label warningscreen:
    hide intro
    show warning
    pause 3.0

label after_load:
    $ config.allow_skipping = allow_skipping
    $ _dismiss_pause = config.developer
    $ persistent.ghost_menu = False
    $ style.say_dialogue = style.normal

    if anticheat != persistent.anticheat:
        stop music
        scene black
        "存档无法加载。"
        "您是不是想作弊？XD"
        $ m_name = "Monika"
        show monika 1 at t11
        if persistent.playername == "":
            m "您真可笑。"
        else:
            m "[persistent.playername]，您真可笑。"
        $ renpy.utter_restart()
    else:
        if not persistent.first_load:
            $ persistent.first_load = True
            call screen dialog("提示：“跳过”按钮可以跳过已读文字。\n我知道多刷二周目很枯燥，所以一定要用好跳过啊！", ok_action=Return())

    return


label autoload:
    python:
        if "_old_game_menu_screen" in globals():
            _game_menu_screen = _old_game_menu_screen
            del _old_game_menu_screen
        if "_old_history" in globals():
            _history = _old_history
            del _old_history
        renpy.context()._menu = False
        renpy.context()._main_menu = False
        main_menu = False
        _in_replay = None
    $ renpy.pop_call()
    jump expression persistent.autoload

label before_main_menu:
    $ config.main_menu_music = audio.t4
    return

label quit:
    return
