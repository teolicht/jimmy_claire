#! /usr/bin/env python3

bold, dim, underlined, blink, reverse, hidden, reset, res_bold   = 1, 2, 4, 5, 7, 8, 0, 21
res_dim, res_underlined, res_blink, res_reverse, res_hidden      = 22, 24, 25, 27, 28

black, red, green, yellow, blue, magenta, cyan, light_gray               = 0, 1, 2, 3, 4, 5, 6, 7
dark_gray, light_red, light_green, light_yellow, light_blue              = 8, 9, 10, 11, 12
light_magenta, light_cyan, white, grey_0, navy_blue, dark_blue           = 13, 14, 15, 16, 17, 18
blue_3a, blue_3b, blue_1, dark_green, deep_sky_blue_4a                   = 19, 20, 21, 22, 23
deep_sky_blue_4b, deep_sky_blue_4c, dodger_blue_3, dodger_blue_2         = 24, 25, 26, 27
green_4, spring_green_4, turquoise_4, deep_sky_blue_3a                   = 28, 29, 30, 31
deep_sky_blue_3b, dodger_blue_1, green_3a, spring_green_3a               = 32, 33, 34, 35
dark_cyan, light_sea_green, deep_sky_blue_2, deep_sky_blue_1             = 36, 37, 38, 39
green_3b, spring_green_3b, spring_green_2a, cyan_3                       = 40, 41, 42, 43
dark_turquoise, turquoise_2, green_1, spring_green_2b                    = 44, 45, 46, 47
spring_green_1, medium_spring_green, cyan_2, cyan_1, dark_red_1          = 48, 49, 50, 51, 52
deep_pink_4a, purple_4a, purple_4b, purple_3, blue_violet                = 53, 54, 55, 56, 57
orange_4a, grey_37, medium_purple_4, slate_blue_3a                       = 58, 59, 60, 61
slate_blue_3b, royal_blue_1, chartreuse_4, dark_sea_green_4a             = 62, 63, 64, 65
pale_turquoise_4, steel_blue, steel_blue_3, cornflower_blue              = 66, 67, 68, 69
chartreuse_3a, dark_sea_green_4b, cadet_blue_2, cadet_blue_1             = 70, 71, 72, 73
sky_blue_3, steel_blue_1a, chartreuse_3b, pale_green_3a                  = 74, 75, 76, 77
sea_green_3, aquamarine_3, medium_turquoise, steel_blue_1b               = 78, 79, 80, 81
chartreuse_2a, sea_green_2, sea_greem_1a, sea_green_1b                   = 82, 83, 84, 85
aquamarine_1a, dark_slate_gray_2, dark_red_2, deep_pink_4b               = 86, 87, 88, 89
dark_magenta_1, dark_magenta_2, dark_violet_1a, purple_1a                = 90, 91, 92, 93
orange_4b, light_pink_4, plum_4, medium_purple_3a                        = 94, 95, 96, 97
medium_purple_3b, slate_blue_1, yellow_4a, wheat_4, grey_53              = 98, 99, 100, 101, 102
light_slate_grey, medium_purple, light_slate_blue, yellow_4b             = 103, 104, 105, 106
dark_olive_green_3a, dark_green_sea, light_sky_blue_3a                   = 107, 108, 109
light_sky_blue_3b, sky_blue_2, chartreuse_2b, dark_olive_green_3b        = 110, 111, 112, 113
pale_green_3b, dark_sea_green_3a, dark_slate_gray_3, sky_blue_1          = 114, 115, 116, 117
chartreuse_1, light_green_2, light_green_3, pale_green_1a                = 118, 119, 120, 121
aquamarine_1b, dark_slate_gray_1, red_3a, deep_pink_4c                   = 122, 123, 124, 125
medium_violet_red, magenta_3a, dark_violet_1b, purple_1b                 = 126, 127, 128, 129
dark_orange_3a, indian_red_1a, hot_pink_3a, medium_orchid_3              = 130, 131, 132, 133
medium_orchid, medium_purple_2a, dark_goldenrod, light_salmon_3a         = 134, 135, 136, 137
rosy_brown, grey_63, medium_purple_2b, medium_purple_1, gold_3a          = 138, 139, 140, 141, 142
dark_khaki, navajo_white_3, grey_69, light_steel_blue_3                  = 143, 144, 145, 146
light_steel_blue, yellow_3a, dark_olive_green_3, dark_sea_green_3b       = 147, 148, 149, 150
dark_sea_green_2, light_cyan_3, light_sky_blue_1, green_yellow           = 151, 152, 153, 154
dark_olive_green_2, pale_green_1b, dark_sea_green_5b                     = 155, 156, 157
dark_sea_green_5a, pale_turquoise_1, red_3b, deep_pink_3a                = 158, 159, 160, 161
deep_pink_3b, magenta_3b, magenta_3c, magenta_2a, dark_orange_3b         = 162, 163, 164, 165, 166
indian_red_1b, hot_pink_3b, hot_pink_2, orchid, medium_orchid_1a         = 167, 168, 169, 170, 171
orange_3, light_salmon_3b, light_pink_3, pink_3, plum_3, violet          = 172, 173, 174, 175, 176, 177
gold_3b, light_goldenrod_3, tan, misty_rose_3, thistle_3, plum_2         = 178, 179, 180, 181, 182, 183
yellow_3b, khaki_3, light_goldenrod_2a, light_yellow_3, grey_84          = 184, 185, 186, 187, 188
light_steel_blue_1, yellow_2, dark_olive_green_1a, dark_olive_green_1b   = 189, 190, 191, 192
dark_sea_green_1, honeydew_2, light_cyan_1, red_1, deep_pink_2           = 193, 194, 195, 196, 197
deep_pink_1a, deep_pink_1b, magenta_2b, magenta_1, orange_red_1          = 198, 199, 200, 201, 202
indian_red_1c, indian_red_1d, hot_pink_1a, hot_pink_1b                   = 203, 204, 205, 206
medium_orchid_1b, dark_orange, salmon_1, light_coral, pale_violet_red_1  = 207, 208, 209, 210, 211
orchid_2, orchid_1, orange_1, sandy_brown, light_salmon_1, light_pink_1  = 212, 213, 214, 215, 216, 217
pink_1, plum_1, gold_1, light_goldenrod_2b, light_goldenrod_2c           = 218, 219, 220, 221, 222
navajo_white_1, misty_rose_1, thistle_1, yellow_1, light_goldenrod_1     = 223, 224, 225, 226, 227
khaki_1, wheat_1, cornsilk_1, grey_100, grey_3, grey_7, grey_11, grey_15 = 228, 229, 230, 231, 232, 233, 234, 235
grey_19, grey_23, grey_27, grey_30, grey_35, grey_39, grey_42, grey_46   = 236, 237, 238, 239, 240, 241, 242, 243
grey_50, grey_54, grey_58, grey_62, grey_66, grey_70, grey_74, grey_78   = 244, 245, 246, 247, 248, 249, 250, 251
grey_82, grey_85, grey_89, grey_93                                       = 252, 253, 254, 255