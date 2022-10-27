import networkx as nx


def questao_1():
    lista = [910, 211, 680, 837, 51, 690, 964, 635, 353, 956, 451, 539, 304, 853, 107, 128, 587, 668, 598, 282, 944, 115, 478, 617, 28, 655, 210, 652, 132, 593, 437, 6, 476, 425, 64, 126, 722, 673, 412, 177, 813, 836, 468, 622, 737, 26, 808, 35, 582, 875, 327, 427, 123, 325, 774, 854, 326, 274, 81, 278, 364, 422, 308, 277, 952, 186, 152, 595, 399, 529, 868, 819, 572, 563, 474, 909, 717, 711, 243, 538, 800, 829, 549, 77, 738, 442, 506, 455, 156, 855, 91, 634, 985, 19, 98, 994, 160, 408, 519, 24, 164, 438, 393, 109, 263, 482, 656, 175, 381, 27, 632, 57, 694, 610, 526, 316, 154, 461, 131, 970, 860, 502, 865, 958, 209, 194, 305, 120, 330, 653, 811, 250, 151, 433, 986, 74, 900, 410, 612, 628, 678, 76, 742, 803, 383, 180, 111, 7, 47, 597, 349, 980, 727, 701, 137, 491, 552, 979, 624, 254, 504, 525, 317, 926, 368, 139, 916, 602, 992, 735, 261, 801, 471, 533, 646, 170, 884, 17, 540, 530, 385, 697, 618, 795, 454, 397, 185, 765, 935, 743, 817, 666, 69, 887, 223, 554, 157, 889, 674, 544, 745, 378, 553, 660, 122, 342, 328, 648, 88, 591, 925, 918, 279, 881, 467, 38, 908, 943, 96, 732, 228, 993, 311, 933, 838, 435, 787, 839, 940, 882, 830, 790, 273, 976, 42, 184, 212, 480, 256, 43, 661, 2, 520, 110, 379, 118, 191, 719, 272, 347, 265, 689, 252, 650, 713, 63, 452, 922, 897, 95, 750, 37, 41, 710, 740, 782, 704, 545, 703, 268, 344, 59, 363, 441, 124, 85, 496, 78, 171, 807, 757, 755, 230, 453, 288, 869, 835, 70, 874, 214, 463, 466, 396, 736, 589, 188, 199, 685, 400, 18, 583, 798, 310, 217, 129, 14, 723, 465, 20, 739, 234, 100, 558, 579, 695, 812, 416, 967, 296, 236, 30, 434, 542, 818, 318, 633, 762, 844, 767, 809, 990, 404, 149, 300, 623, 334, 430, 249, 354, 575, 181, 758, 796, 959, 486, 505, 192, 574, 148, 684, 117, 153, 322, 448, 754, 823, 220, 203, 824, 902, 915, 626, 833, 899, 9, 380, 559, 222, 547, 759, 447, 718, 614, 534, 346, 609, 336, 94, 457, 82, 440, 45, 968, 0, 179, 155, 403, 772, 921, 955, 802, 603, 560, 79, 343, 753, 4, 781, 333, 620, 708, 125, 61, 424, 446, 927, 977, 639, 667, 600, 647, 991, 12, 536, 100, 431, 367, 561, 382, 683, 692, 88, 663, 398, 205, 677, 832, 565, 470, 522, 515, 963, 323, 786, 686, 960, 294, 75, 102, 951, 140, 919, 71, 119, 721, 585, 608, 52, 238, 229, 289, 654, 892, 691, 224, 493, 253, 200, 89, 239, 54, 923, 219, 744, 292, 580, 460, 340, 942, 643, 201, 849, 93, 930, 10, 532, 816, 419, 570, 492, 629, 941, 822, 568, 636, 548, 324, 747, 245, 826, 842, 621, 260, 246, 49, 974, 670, 886, 939, 22, 966, 166, 195, 339,
             987, 764, 33, 599, 631, 443, 116, 971, 766, 873, 356, 682, 73, 86, 87, 68, 779, 846, 32, 730, 320, 511, 664, 259, 21, 369, 688, 527, 576, 510, 880, 630, 531, 948, 371, 90, 321, 39, 567, 165, 15, 293, 581, 924, 391, 436, 866, 780, 473, 58, 426, 606, 657, 388, 485, 459, 105, 97, 389, 799, 763, 142, 760, 196, 83, 843, 903, 62, 361, 784, 53, 815, 773, 702, 726, 651, 788, 699, 859, 516, 550, 315, 418, 469, 284, 169, 376, 637, 3, 929, 741, 856, 449, 928, 489, 13, 934, 429, 978, 360, 108, 401, 247, 338, 662, 698, 988, 106, 458, 372, 319, 731, 345, 845, 226, 25, 487, 872, 893, 577, 888, 362, 776, 407, 669, 414, 499, 34, 158, 792, 248, 675, 806, 557, 586, 374, 768, 982, 193, 957, 858, 237, 241, 578, 890, 619, 659, 23, 789, 590, 594, 366, 693, 225, 337, 706, 644, 481, 850, 862, 879, 206, 183, 298, 176, 276, 912, 411, 359, 518, 638, 65, 954, 415, 329, 937, 733, 551, 420, 847, 218, 498, 462, 546, 138, 752, 512, 270, 423, 645, 309, 615, 479, 287, 341, 207, 251, 357, 66, 136, 281, 601, 556, 144, 891, 709, 797, 145, 640, 949, 998, 996, 820, 114, 946, 283, 625, 56, 584, 938, 658, 17, 197, 793, 394, 494, 198, 406, 267, 771, 439, 215, 373, 36, 386, 235, 969, 475, 405, 751, 665, 335, 841, 84, 848, 535, 208, 231, 814, 834, 588, 907, 303, 514, 642, 432, 607, 804, 286, 370, 613, 679, 314, 488, 716, 501, 99, 178, 972, 785, 456, 596, 100, 676, 355, 331, 387, 150, 995, 805, 500, 871, 172, 101, 931, 508, 883, 262, 707, 604, 204, 592, 831, 40, 264, 11, 135, 573, 756, 932, 67, 50, 714, 725, 864, 794, 375, 627, 1, 911, 989, 5, 464, 167, 258, 141, 672, 127, 472, 769, 307, 896, 358, 255, 825, 280, 242, 947, 161, 332, 299, 761, 182, 240, 611, 905, 45, 571, 146, 513, 365, 392, 728, 528, 523, 962, 477, 72, 562, 483, 973, 168, 777, 269, 189, 569, 216, 133, 791, 749, 981, 233, 159, 936, 213, 715, 997, 147, 524, 266, 734, 705, 174, 953, 778, 444, 775, 521, 840, 60, 232, 913, 24, 428, 649, 348, 8, 920, 351, 202, 450, 876, 121, 44, 275, 901, 671, 227, 746, 112, 712, 55, 302, 244, 413, 190, 555, 297, 484, 543, 605, 257, 313, 965, 517, 352, 162, 945, 681, 395, 999, 720, 537, 983, 914, 143, 291, 878, 828, 134, 295, 861, 541, 687, 221, 906, 103, 700, 961, 975, 92, 566, 495, 29, 46, 113, 31, 445, 390, 696, 904, 306, 301, 863, 377, 851, 729, 550, 821, 895, 384, 402, 163, 497, 104, 870, 917, 312, 173, 507, 724, 867, 48, 748, 187, 857, 417, 271, 641, 898, 285, 877, 409, 490, 783, 16, 564, 770, 509, 80, 350, 503, 894, 885, 950, 421, 810, 852, 984, 616, 827, 290, 130]
    G = nx.DiGraph()
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] > lista[j]:
                G.add_edge(lista[i], lista[j])

    longest_path = nx.dag_longest_path(G)
    print(longest_path)
    print(len(longest_path))


def questao_2():
    G = nx.DiGraph()
    lista = [(0, 2), (0, 3), (0, 4), (0, 5), (0, 13), (0, 14), (0, 15), (0, 19), (0, 20), (0, 25), (0, 26), (0, 27), (0, 28), (0, 29), (1, 5), (1, 7), (1, 9), (1, 11), (1, 25), (2, 6), (2, 8), (2, 10), (2, 11), (2, 13), (2, 16), (2, 19), (2, 20), (2, 21), (2, 24), (2, 29), (3, 4), (3, 6), (3, 7), (3, 10), (3, 11), (3, 12), (3, 13), (3, 18), (3, 19), (3, 21), (4, 5), (4, 6), (4, 8), (4, 9), (4, 16), (4, 17), (4, 20), (4, 22), (4, 28), (5, 10), (5, 13), (5, 14), (5, 21), (5, 22), (5, 25), (5, 26), (6, 7), (6, 8), (6, 9), (6, 10), (6, 12), (6, 14), (6, 15), (6, 20), (6, 23), (6, 25), (6, 26), (7, 9), (7, 10), (7, 12), (7, 13),
             (7, 14), (7, 15), (7, 17), (7, 19), (7, 20), (7, 21), (7, 23), (7, 24), (7, 27), (8, 16), (8, 20), (8, 22), (8, 25), (9, 10), (9, 12), (9, 19), (9, 21), (9, 22), (9, 23), (9, 25), (9, 26), (9, 28), (10, 13), (10, 25), (10, 27), (10, 29), (11, 16), (11, 18), (11, 19), (11, 22), (11, 23), (11, 24), (11, 25), (11, 26), (11, 27), (12, 15), (12, 18), (12, 20), (13, 17), (13, 28), (14, 21), (14, 25), (15, 17), (15, 20), (16, 18), (16, 27), (17, 19), (17, 21), (17, 24), (17, 25), (17, 26), (18, 22), (18, 23), (18, 24), (19, 21), (19, 23), (19, 24), (19, 29), (20, 21), (20, 23), (23, 27), (24, 26), (26, 29), (27, 28)]
    for tupla in lista:
        G.add_edge(tupla[0], tupla[1])

    ordenacao_topologica = [v for v in reversed(
        list(nx.dfs_postorder_nodes(G)))]
    
    print(ordenacao_topologica)


def questao_3():
    G = nx.DiGraph()
    arcos = [(0, 9, 6), (0, 12, 39), (0, 13, 89), (0, 15, 68), (0, 22, 46), (0, 24, 37), (0, 26, 59), (0, 27, 27), (0, 29, 67), (0, 30, 63), (0, 31, 95), (0, 32, 54), (0, 33, 44), (0, 36, 20), (0, 37, 26), (0, 39, 43), (0, 42, 26), (0, 43, 43), (0, 45, 14), (0, 47, 38), (0, 48, 25), (0, 49, 98), (1, 4, 79), (1, 11, 57), (1, 12, 15), (1, 13, 53), (1, 16, 94), (1, 17, 91), (1, 20, 70), (1, 21, 26), (1, 22, 36), (1, 26, 2), (1, 27, 48), (1, 29, 13), (1, 34, 58), (1, 35, 88), (1, 36, 66), (1, 38, 32), (1, 40, 39), (1, 41, 84), (1, 45, 43), (1, 47, 40), (1, 49, 30), (2, 3, 24), (2, 8, 11), (2, 9, 39), (2, 10, 27), (2, 16, 53), (2, 17, 41), (2, 18, 20), (2, 21, 15), (2, 26, 22), (2, 27, 17), (2, 29, 59), (2, 33, 98), (2, 36, 80), (2, 38, 22), (2, 41, 72), (2, 42, 12), (3, 6, 62), (3, 7, 28), (3, 9, 2), (3, 10, 60), (3, 11, 55), (3, 12, 9), (3, 13, 100), (3, 17, 93), (3, 19, 29), (3, 21, 3), (3, 22, 34), (3, 25, 36), (3, 32, 80), (3, 33, 97), (3, 38, 9), (3, 42, 54), (3, 43, 42), (3, 44, 26), (3, 46, 36), (3, 49, 18), (4, 5, 52), (4, 8, 54), (4, 9, 48), (4, 10, 59), (4, 11, 71), (4, 12, 36), (4, 13, 67), (4, 17, 38), (4, 19, 90), (4, 22, 12), (4, 24, 22), (4, 29, 4), (4, 31, 100), (4, 33, 34), (4, 34, 11), (4, 35, 29), (4, 37, 51), (4, 40, 83), (4, 42, 99), (4, 45, 48), (4, 47, 30), (5, 6, 45), (5, 7, 36), (5, 9, 68), (5, 12, 12), (5, 14, 20), (5, 15, 13), (5, 16, 18), (5, 17, 16), (5, 20, 72), (5, 23, 100), (5, 24, 57), (5, 26, 13), (5, 27, 72), (5, 29, 84), (5, 31, 54), (5, 33, 86), (5, 34, 15), (5, 36, 100), (5, 39, 8), (5, 40, 34), (5, 42, 67), (5, 47, 41), (5, 48, 23), (5, 49, 48), (6, 17, 43), (6, 19, 37), (6, 22, 95), (6, 25, 25), (6, 27, 54), (6, 29, 45), (6, 31, 41), (6, 32, 28), (6, 34, 40), (6, 40, 90), (6, 43, 16), (6, 45, 86), (6, 49, 61), (7, 9, 13), (7, 10, 96), (7, 11, 19), (7, 13, 72), (7, 14, 87), (7, 16, 43), (7, 19, 42), (7, 20, 52), (7, 21, 14), (7, 24, 26), (7, 26, 41), (7, 27, 45), (7, 31, 8), (7, 36, 17), (7, 39, 91), (7, 41, 100), (7, 44, 99), (7, 46, 27), (8, 18, 61), (8, 21, 96), (8, 24, 89), (8, 26, 42), (8, 27, 20), (8, 28, 25), (8, 30, 32), (8, 32, 11), (8, 34, 33), (8, 35, 36), (8, 37, 43), (8, 40, 91), (8, 42, 82), (8, 44, 57), (8, 46, 77), (8, 49, 25), (9, 10, 10), (9, 12, 12), (9, 13, 78), (9, 16, 85), (9, 17, 57), (9, 18, 53), (9, 20, 30), (9, 21, 13), (9, 22, 42), (9, 25, 99), (9, 26, 55), (9, 27, 43), (9, 30, 90), (9, 34, 36), (9, 37, 34), (9, 40, 93), (9, 41, 55), (9, 42, 28), (9, 43, 7), (9, 47, 47), (10, 12, 47), (10, 14, 74), (10, 15, 75), (10, 16, 82), (10, 17, 25), (10, 18, 40), (10, 23, 46), (10, 24, 48), (10, 25, 4), (10, 29, 30), (10, 31, 37), (10, 33, 45), (10, 36, 26), (10, 37, 49), (10, 40, 8), (10, 42, 71), (10, 44, 55), (10, 45, 61), (10, 46, 81), (10, 47, 43), (11, 12, 51), (11, 13, 77), (11, 17, 55), (11, 19, 21), (11, 25, 52), (11, 28, 13), (11, 30, 56), (11, 31, 24), (11, 36, 53), (11, 38, 95), (11, 41, 69), (11, 42, 32), (11, 43, 79), (11, 44, 44), (11, 45, 94), (11, 47, 88), (11, 48, 12), (12, 13, 17), (12, 15, 45), (12, 16, 26), (12, 21, 51), (12, 23, 34), (12, 24, 48), (12, 28, 51), (12, 29, 12), (12, 30, 8), (12, 31, 38), (12, 33, 71), (12, 34, 81), (12, 35, 22), (12, 36, 38), (12, 38, 23), (12, 39, 49), (12, 43, 68), (12, 45, 58), (12, 48, 90), (12, 49, 52), (13, 16, 82), (13, 17, 23), (13, 22, 97), (13, 26, 14), (13, 28, 80), (13, 33, 34), (13, 36, 86), (13, 39, 41), (13, 41, 37), (13, 45, 58), (14, 17, 33), (14, 22, 29), (14, 23, 33), (14, 24, 28), (14, 26, 57), (14, 30, 25), (14, 32, 85), (14, 33, 35),
             (14, 34, 28), (14, 36, 8), (14, 37, 43), (14, 39, 61), (14, 42, 95), (14, 44, 49), (14, 47, 87), (14, 48, 100), (14, 49, 55), (15, 18, 55), (15, 19, 87), (15, 20, 57), (15, 22, 12), (15, 23, 76), (15, 26, 47), (15, 28, 50), (15, 29, 88), (15, 30, 10), (15, 33, 34), (15, 36, 99), (15, 41, 66), (15, 49, 79), (16, 21, 28), (16, 24, 20), (16, 28, 38), (16, 29, 77), (16, 33, 36), (16, 37, 31), (16, 40, 84), (16, 42, 14), (16, 44, 63), (16, 48, 96), (17, 20, 54), (17, 21, 31), (17, 24, 25), (17, 26, 25), (17, 28, 85), (17, 29, 4), (17, 36, 8), (17, 37, 22), (17, 44, 28), (17, 45, 18), (17, 46, 19), (17, 47, 86), (17, 48, 68), (18, 22, 82), (18, 25, 39), (18, 28, 15), (18, 29, 88), (18, 33, 22), (18, 35, 62), (18, 36, 99), (18, 37, 6), (18, 39, 85), (18, 43, 82), (18, 44, 12), (18, 46, 83), (19, 20, 95), (19, 23, 15), (19, 26, 74), (19, 27, 37), (19, 35, 85), (19, 36, 30), (19, 37, 52), (19, 38, 16), (19, 42, 41), (19, 43, 11), (19, 47, 20), (19, 49, 94), (20, 21, 39), (20, 22, 46), (20, 24, 52), (20, 25, 78), (20, 28, 57), (20, 29, 67), (20, 30, 54), (20, 31, 18), (20, 33, 94), (20, 34, 20), (20, 39, 74), (20, 41, 45), (20, 44, 84), (20, 47, 4), (20, 48, 92), (21, 24, 75), (21, 27, 78), (21, 30, 14), (21, 31, 81), (21, 33, 3), (21, 34, 60), (21, 36, 82), (21, 37, 44), (21, 43, 79), (21, 44, 16), (21, 45, 71), (21, 48, 28), (22, 29, 79), (22, 32, 32), (22, 33, 44), (22, 40, 57), (22, 41, 92), (22, 46, 90), (22, 47, 49), (22, 48, 43), (23, 26, 59), (23, 27, 38), (23, 28, 84), (23, 32, 62), (23, 35, 71), (23, 38, 81), (23, 40, 93), (23, 43, 60), (23, 44, 97), (23, 47, 24), (23, 48, 14), (23, 49, 37), (24, 26, 73), (24, 34, 75), (24, 35, 92), (24, 36, 13), (24, 38, 19), (24, 40, 68), (24, 41, 2), (24, 42, 48), (24, 44, 49), (24, 48, 51), (25, 27, 26), (25, 28, 5), (25, 32, 76), (25, 34, 87), (25, 35, 45), (25, 39, 40), (25, 40, 23), (25, 41, 50), (25, 42, 89), (25, 44, 92), (25, 45, 33), (25, 49, 58), (26, 27, 85), (26, 29, 5), (26, 30, 28), (26, 33, 29), (26, 35, 79), (26, 37, 99), (26, 39, 84), (26, 40, 32), (26, 42, 99), (26, 44, 26), (26, 47, 17), (26, 48, 49), (26, 49, 19), (27, 28, 94), (27, 35, 13), (27, 36, 100), (27, 38, 53), (27, 41, 78), (27, 44, 28), (27, 46, 21), (27, 47, 37), (28, 29, 45), (28, 30, 13), (28, 32, 2), (28, 33, 68), (28, 34, 37), (28, 36, 10), (28, 41, 95), (28, 47, 95), (29, 34, 64), (29, 36, 25), (29, 39, 61), (29, 41, 76), (29, 42, 38), (29, 43, 92), (29, 48, 96), (30, 33, 30), (30, 34, 57), (30, 37, 36), (30, 40, 89), (30, 41, 36), (30, 43, 50), (30, 44, 60), (30, 46, 81), (30, 47, 44), (30, 49, 48), (31, 35, 41), (31, 37, 24), (31, 40, 44), (31, 43, 84), (31, 44, 45), (31, 46, 89), (31, 47, 28), (32, 33, 19), (32, 34, 72), (32, 38, 73), (32, 42, 80), (32, 45, 93), (33, 36, 45), (33, 39, 6), (33, 45, 79), (33, 46, 35), (33, 47, 5), (33, 48, 13), (34, 36, 55), (34, 37, 86), (34, 38, 12), (34, 42, 56), (34, 43, 22), (34, 48, 84), (34, 49, 61), (35, 36, 3), (35, 37, 9), (35, 41, 2), (35, 44, 82), (35, 45, 41), (35, 46, 41), (35, 48, 86), (36, 39, 7), (36, 40, 77), (36, 43, 58), (36, 45, 77), (36, 47, 54), (36, 48, 30), (37, 38, 20), (37, 40, 80), (37, 42, 9), (37, 44, 89), (37, 46, 71), (38, 39, 73), (38, 40, 65), (38, 41, 43), (38, 42, 94), (38, 43, 34), (38, 46, 4), (38, 48, 54), (39, 44, 76), (40, 43, 98), (40, 46, 19), (40, 47, 34), (40, 49, 8), (41, 42, 20), (41, 44, 20), (41, 45, 15), (41, 47, 74), (42, 45, 8), (42, 47, 45), (42, 49, 34), (43, 44, 86), (43, 46, 4), (43, 48, 69), (44, 48, 63), (46, 47, 18), (46, 48, 93), (46, 49, 23)]

    for tupla in arcos:
        G.add_edge(tupla[0], tupla[1], weight=tupla[2])

    longest_path = nx.dag_longest_path(G)
    print(longest_path)
    print(len(longest_path))


if __name__ == "__main__":
    questao_2()