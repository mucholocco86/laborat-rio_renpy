image bp_mc_strip_1:
    "bp_mc_strip_1_ep10" with Dissolve(0.5, alpha=True)
image bp_mc_strip_2:
    "bp_mc_strip_2_ep10" with Dissolve(0.5, alpha=True)

image bp_camila_strip_1:
    "bp_camila_strip_1a_ep10" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_camila_strip_1b_ep10" with Dissolve(0.5, alpha=True)
image bp_camila_strip_2:
    "bp_camila_strip_2a_ep10" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_camila_strip_2b_ep10" with Dissolve(0.5, alpha=True)
image bp_sage_strip_1:
    "bp_sage_strip_1a_ep10" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_sage_strip_1b_ep10" with Dissolve(0.5, alpha=True)
image bp_sage_strip_2:
    "bp_sage_strip_2a_ep10" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_sage_strip_2b_ep10" with Dissolve(0.5, alpha=True)
image bp_josy_strip_1:
    "bp_josy_strip_1a_ep10" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_josy_strip_1b_ep10" with Dissolve(0.5, alpha=True)
image bp_josy_strip_2:
    "bp_josy_strip_2a_ep10" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_josy_strip_2b_ep10" with Dissolve(0.5, alpha=True)
image bp_isabella_strip_1:
    "bp_isabella_strip_1a_ep10" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_isabella_strip_1b_ep10" with Dissolve(0.5, alpha=True)
image bp_isabella_strip_2:
    "bp_isabella_strip_2b_ep10" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_isabella_strip_2a_ep10" with Dissolve(0.5, alpha=True)
image bp_mc_strip_bella_2:
    "bp_mc_strip_bella_2a_ep10" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_mc_strip_bella_2b_ep10" with Dissolve(0.5, alpha=True)

image bp_camila_swat_ep10:
    "bp_mc_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_camila_swat"
    linear 0.1 xoffset -2 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 3 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset -1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 0 * persistent.scale_factor yoffset 0
image bp_jill_swat_ep10:
    "bp_mc_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_jill_swat"
    linear 0.1 xoffset -2 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 3 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset -1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 0 * persistent.scale_factor yoffset 0
image bp_sage_swat_ep10:
    "bp_mc_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_sage_swat"
    linear 0.1 xoffset -2 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 3 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset -1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 0 * persistent.scale_factor yoffset 0
image bp_josy_swat_ep10:
    "bp_mc_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_josy_swat"
    linear 0.1 xoffset -2 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 3 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset -1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 0 * persistent.scale_factor yoffset 0
image bp_isabella_swat_ep10:
    "bp_mc_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_isabella_swat"
    linear 0.1 xoffset -2 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 3 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset -1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 0 * persistent.scale_factor yoffset 0
image bp_player_swat_ep10:
    "bp_cpu_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_swat_ep10"
    linear 0.1 xoffset -2 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 3 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset -1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 0 * persistent.scale_factor yoffset 0
image bp_player_swat_bella_ep10:
    "bp_cpu_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_swat_bella_ep10"
    linear 0.1 xoffset -2 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 3 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset -1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 0 * persistent.scale_factor yoffset 0
image bp_player_bounce_6:
    "bp_mc_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_6"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_5:
    "bp_mc_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_5"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_4:
    "bp_mc_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_4"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_3:
    "bp_mc_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_3"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_2:
    "bp_mc_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_2"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_1:
    "bp_mc_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_1"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_6:
    "bp_cpu_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_6"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_5:
    "bp_cpu_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_5"
image bp_cpu_bounce_4:
    "bp_cpu_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_4"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_3:
    "bp_cpu_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_3"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_2:
    "bp_cpu_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_2"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_1:
    "bp_cpu_bounce_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_1"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_bella_6:
    "bp_mc_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_bella_6"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_bella_5:
    "bp_mc_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_bella_5"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_bella_4:
    "bp_mc_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_bella_4"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_bella_3:
    "bp_mc_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_bella_3"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_bella_2:
    "bp_mc_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_bella_2"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_bella_1:
    "bp_mc_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_bella_1"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_bella_6:
    "bp_cpu_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_bella_6"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_bella_5:
    "bp_cpu_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_bella_5"
image bp_cpu_bounce_bella_4:
    "bp_cpu_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_bella_4"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_bella_3:
    "bp_cpu_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_bella_3"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_bella_2:
    "bp_cpu_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_bella_2"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_bella_1:
    "bp_cpu_bounce_bella_ep10" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_bella_1"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0

image bp_player_bounce_bella_ep11_6:
    "bp_mc_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_bella_ep11_6"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_bella_ep11_5:
    "bp_mc_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_bella_ep11_5"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_bella_ep11_4:
    "bp_mc_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_bella_ep11_4"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_bella_ep11_3:
    "bp_mc_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_bella_ep11_3"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_bella_ep11_2:
    "bp_mc_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_bella_ep11_2"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_player_bounce_bella_ep11_1:
    "bp_mc_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_mc_hit_bella_ep11_1"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0

image bp_cpu_bounce_bella_ep11_6:
    "bp_cpu_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_bella_ep11_6"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_bella_ep11_5:
    "bp_cpu_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_bella_ep11_5"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_bella_ep11_4:
    "bp_cpu_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_bella_ep11_4"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_bella_ep11_3:
    "bp_cpu_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_bella_ep11_3"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_bella_ep11_2:
    "bp_cpu_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_bella_ep11_2"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_cpu_bounce_bella_ep11_1:
    "bp_cpu_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_cpu_hit_bella_ep11_1"
    linear 0.1 xoffset 0 yoffset -2 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 3 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset -1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 1 * persistent.scale_factor
    linear 0.1 xoffset 0 yoffset 0
image bp_isabella_swat_ep11:
    "bp_mc_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_isabella_swat_ep11a"
    linear 0.1 xoffset -2 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 3 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset -1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 0 yoffset 0
image bp_player_swat_bella_ep11:
    "bp_cpu_bounce_bella_ep11" with Dissolve(0.5, alpha=True)
    pause 1
    "bp_player_swat_bella_ep11a"
    linear 0.1 xoffset -2 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 3 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset -1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 1 * persistent.scale_factor yoffset 0
    linear 0.1 xoffset 0 yoffset 0
image bp_isabella_strip_ep11_1:
    "bp_isabella_strip_ep11_1a" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_isabella_strip_ep11_1b" with Dissolve(0.5, alpha=True)
image bp_isabella_strip_ep11_2:
    "bp_isabella_strip_ep11_2a" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_isabella_strip_ep11_2b" with Dissolve(0.5, alpha=True)

image bp_mc_strip_bella_ep11_1:
    "bp_mc_strip_bella_ep11_1a" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_mc_strip_bella_ep11_1b" with Dissolve(0.5, alpha=True)
image bp_mc_strip_bella_ep11_2:
    "bp_mc_strip_bella_ep11_2a" with Dissolve(0.5, alpha=True)
    pause 3
    "bp_mc_strip_bella_ep11_2b" with Dissolve(0.5, alpha=True)
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
