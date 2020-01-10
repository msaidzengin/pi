from mpmath import mp
import json

alanKodu = [392, 510, 512, 522, 562, 564, 592, 594, 800, 811, 822, 850, 888, 898, 900]
turkTelekom = [501, 505, 506, 507, 551, 552, 553, 554, 555, 559]
turkcell = [530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 561]
vodafone = [540, 541, 542, 543, 544, 545, 546, 547, 548, 549]
kktcTelsim = [54285, 54286, 54287, 54288]
kktcTurkcell = [53383, 53384, 53385, 53386, 53387]
sehirKodu = [322, 323, 416, 417, 272, 273, 472, 473, 382, 383, 358, 359, 312, 313, 242, 243, 478, 479, 466, 467, 256, 257, 266, 267, 378, 379, 488, 489, 458, 459, 228, 229, 426, 427, 434, 435, 374, 375, 248, 249, 224, 225, 286, 287, 376, 377, 364, 365, 258, 259, 412, 413, 380, 381, 284, 285, 850, 424, 425, 446, 447, 442, 443, 222, 223, 342, 343, 454, 455, 456, 457, 438, 439, 326, 327, 476, 477, 246, 247, 216, 217, 212, 213, 232, 233, 344, 345, 370, 371, 338, 339, 474, 475, 366, 367, 352, 353, 318, 319, 288, 289, 386, 387, 348, 349, 262, 263, 332, 333, 274, 275, 422, 423, 236, 237, 482, 483, 324, 325, 252, 253, 436, 437, 384, 385, 388, 389, 452, 453, 328, 329, 464, 465, 264, 265, 362, 363, 484, 485, 368, 369, 346, 347, 414, 415, 486, 487, 282, 283, 356, 357, 462, 463, 428, 429, 276, 277, 432, 433, 226, 227, 354, 355, 372, 373]

allPhones = turkTelekom + turkcell + vodafone

mp.dps = 1000000
pi = str(mp.pi)[2:]

searchLen = 3
foundPhones = []

for i in range(len(pi) - searchLen - 7):

    number = pi[i: i+searchLen]

    if int(number) in allPhones:
        foundPhones.append({
            'phone': pi[i: i+10],
            'index': i
        })


with open('result1m.json', 'w') as out:
    json.dump(foundPhones , out)
