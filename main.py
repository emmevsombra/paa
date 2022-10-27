from collections import defaultdict


class Graph:
    def __init__(self, digraph=True):
        self.graph = defaultdict(list)
        self.n = 0
        self.t = 0
        self.is_digraph = digraph

    def addEdge(self, u, v):
        self.graph[u].append(v)
        if not self.is_digraph:
            self.graph[v].append(u)
        elif(v not in self.graph):
            self.graph[v] = list()
        self.n = len(self.graph.keys())

    def dfs_util(self, u):
        self.visited[u] = True
        self.t += 1
        self.t_i[u] = self.t

        for v in self.graph[u]:
            if not visited[v]:
                self.parent[v] = u
                self.dfs_util(v)

        self.t += 1
        self.t_f[u] = self.t
        self.topologic_order.insert(0, u)

    def dfs(self):
        self.visited = [False] * self.n
        self.t_i = [-1] * self.n
        self.t_f = [-1] * self.n
        self.parent = [-1] * self.n
        self.topologic_order = []

        for i in range(self.n):
            if not self.visited[i]:
                self.dfs_util(i)

    @property
    def get_topologic_order(self):
        self.dfs()
        return self.topologic_order

    def __str__(self):
        return str(self.get_topologic_order)


def main():
    lista = [910, 211, 680, 837, 51, 690, 964, 635, 353, 956, 451, 539, 304, 853, 107, 128, 587, 668, 598, 282, 944, 115, 478, 617, 28, 655, 210, 652, 132, 593, 437, 6, 476, 425, 64, 126, 722, 673, 412, 177, 813, 836, 468, 622, 737, 26, 808, 35, 582, 875, 327, 427, 123, 325, 774, 854, 326, 274, 81, 278, 364, 422, 308, 277, 952, 186, 152, 595, 399, 529, 868, 819, 572, 563, 474, 909, 717, 711, 243, 538, 800, 829, 549, 77, 738, 442, 506, 455, 156, 855, 91, 634, 985, 19, 98, 994, 160, 408, 519, 24, 164, 438, 393, 109, 263, 482, 656, 175, 381, 27, 632, 57, 694, 610, 526, 316, 154, 461, 131, 970, 860, 502, 865, 958, 209, 194, 305, 120, 330, 653, 811, 250, 151, 433, 986, 74, 900, 410, 612, 628, 678, 76, 742, 803, 383, 180, 111, 7, 47, 597, 349, 980, 727, 701, 137, 491, 552, 979, 624, 254, 504, 525, 317, 926, 368, 139, 916, 602, 992, 735, 261, 801, 471, 533, 646, 170, 884, 17, 540, 530, 385, 697, 618, 795, 454, 397, 185, 765, 935, 743, 817, 666, 69, 887, 223, 554, 157, 889, 674, 544, 745, 378, 553, 660, 122, 342, 328, 648, 88, 591, 925, 918, 279, 881, 467, 38, 908, 943, 96, 732, 228, 993, 311, 933, 838, 435, 787, 839, 940, 882, 830, 790, 273, 976, 42, 184, 212, 480, 256, 43, 661, 2, 520, 110, 379, 118, 191, 719, 272, 347, 265, 689, 252, 650, 713, 63, 452, 922, 897, 95, 750, 37, 41, 710, 740, 782, 704, 545, 703, 268, 344, 59, 363, 441, 124, 85, 496, 78, 171, 807, 757, 755, 230, 453, 288, 869, 835, 70, 874, 214, 463, 466, 396, 736, 589, 188, 199, 685, 400, 18, 583, 798, 310, 217, 129, 14, 723, 465, 20, 739, 234, 100, 558, 579, 695, 812, 416, 967, 296, 236, 30, 434, 542, 818, 318, 633, 762, 844, 767, 809, 990, 404, 149, 300, 623, 334, 430, 249, 354, 575, 181, 758, 796, 959, 486, 505, 192, 574, 148, 684, 117, 153, 322, 448, 754, 823, 220, 203, 824, 902, 915, 626, 833, 899, 9, 380, 559, 222, 547, 759, 447, 718, 614, 534, 346, 609, 336, 94, 457, 82, 440, 45, 968, 0, 179, 155, 403, 772, 921, 955, 802, 603, 560, 79, 343, 753, 4, 781, 333, 620, 708, 125, 61, 424, 446, 927, 977, 639, 667, 600, 647, 991, 12, 536, 100, 431, 367, 561, 382, 683, 692, 88, 663, 398, 205, 677, 832, 565, 470, 522, 515, 963, 323, 786, 686, 960, 294, 75, 102, 951, 140, 919, 71, 119, 721, 585, 608, 52, 238, 229, 289, 654, 892, 691, 224, 493, 253, 200, 89, 239, 54, 923, 219, 744, 292, 580, 460, 340, 942, 643, 201, 849, 93, 930, 10, 532, 816, 419, 570, 492, 629, 941, 822, 568, 636, 548, 324, 747, 245, 826, 842, 621, 260, 246, 49, 974, 670, 886, 939, 22, 966, 166, 195, 339,
             987, 764, 33, 599, 631, 443, 116, 971, 766, 873, 356, 682, 73, 86, 87, 68, 779, 846, 32, 730, 320, 511, 664, 259, 21, 369, 688, 527, 576, 510, 880, 630, 531, 948, 371, 90, 321, 39, 567, 165, 15, 293, 581, 924, 391, 436, 866, 780, 473, 58, 426, 606, 657, 388, 485, 459, 105, 97, 389, 799, 763, 142, 760, 196, 83, 843, 903, 62, 361, 784, 53, 815, 773, 702, 726, 651, 788, 699, 859, 516, 550, 315, 418, 469, 284, 169, 376, 637, 3, 929, 741, 856, 449, 928, 489, 13, 934, 429, 978, 360, 108, 401, 247, 338, 662, 698, 988, 106, 458, 372, 319, 731, 345, 845, 226, 25, 487, 872, 893, 577, 888, 362, 776, 407, 669, 414, 499, 34, 158, 792, 248, 675, 806, 557, 586, 374, 768, 982, 193, 957, 858, 237, 241, 578, 890, 619, 659, 23, 789, 590, 594, 366, 693, 225, 337, 706, 644, 481, 850, 862, 879, 206, 183, 298, 176, 276, 912, 411, 359, 518, 638, 65, 954, 415, 329, 937, 733, 551, 420, 847, 218, 498, 462, 546, 138, 752, 512, 270, 423, 645, 309, 615, 479, 287, 341, 207, 251, 357, 66, 136, 281, 601, 556, 144, 891, 709, 797, 145, 640, 949, 998, 996, 820, 114, 946, 283, 625, 56, 584, 938, 658, 17, 197, 793, 394, 494, 198, 406, 267, 771, 439, 215, 373, 36, 386, 235, 969, 475, 405, 751, 665, 335, 841, 84, 848, 535, 208, 231, 814, 834, 588, 907, 303, 514, 642, 432, 607, 804, 286, 370, 613, 679, 314, 488, 716, 501, 99, 178, 972, 785, 456, 596, 100, 676, 355, 331, 387, 150, 995, 805, 500, 871, 172, 101, 931, 508, 883, 262, 707, 604, 204, 592, 831, 40, 264, 11, 135, 573, 756, 932, 67, 50, 714, 725, 864, 794, 375, 627, 1, 911, 989, 5, 464, 167, 258, 141, 672, 127, 472, 769, 307, 896, 358, 255, 825, 280, 242, 947, 161, 332, 299, 761, 182, 240, 611, 905, 45, 571, 146, 513, 365, 392, 728, 528, 523, 962, 477, 72, 562, 483, 973, 168, 777, 269, 189, 569, 216, 133, 791, 749, 981, 233, 159, 936, 213, 715, 997, 147, 524, 266, 734, 705, 174, 953, 778, 444, 775, 521, 840, 60, 232, 913, 24, 428, 649, 348, 8, 920, 351, 202, 450, 876, 121, 44, 275, 901, 671, 227, 746, 112, 712, 55, 302, 244, 413, 190, 555, 297, 484, 543, 605, 257, 313, 965, 517, 352, 162, 945, 681, 395, 999, 720, 537, 983, 914, 143, 291, 878, 828, 134, 295, 861, 541, 687, 221, 906, 103, 700, 961, 975, 92, 566, 495, 29, 46, 113, 31, 445, 390, 696, 904, 306, 301, 863, 377, 851, 729, 550, 821, 895, 384, 402, 163, 497, 104, 870, 917, 312, 173, 507, 724, 867, 48, 748, 187, 857, 417, 271, 641, 898, 285, 877, 409, 490, 783, 16, 564, 770, 509, 80, 350, 503, 894, 885, 950, 421, 810, 852, 984, 616, 827, 290, 130]
    maior_subsequencia_decrescente(lista)


def maior_subsequencia_crescente(lista):
    # Gerando DAG
    g = Graph()
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[i] < lista[j]:
                g.addEdge(i, j)
    # Ordenação topológica
    ord_topologica = g.get_topologic_order
    print(ord_topologica)


def maior_subsequencia_decrescente(lista):
    # Gerando DAG
    g = Graph()
    for i in range(len(lista)):
        for j in range(i, len(lista)):
            if lista[i] > lista[j]:
                g.addEdge(i, j)
    # Ordenação topológica
    ord_topologica = g.get_topologic_order
    print(ord_topologica)


if __name__ == "__main__":
    main()