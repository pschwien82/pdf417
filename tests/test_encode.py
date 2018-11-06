# -*- coding: utf-8 -*-

from pdf417.encoding import encode, encode_high, to_bytes

TEST_DATA = '\n'.join([
    'HRVHUB30',
    'HRK',
    '000000010000000',
    'Ivan Habunek',
    'Savska cesta 13',
    '10000 Zagreb',
    'Big Fish Software d.o.o.',
    'Savska cesta 13',
    '10000 Zagreb',
    'HR6623400091110651272',
    '00',
    'HR123456',
    'ANTS',
    'Razvoj paketa za bar kodove\n'
])


def test_encode_high():

    # High level encoding
    expected = [
        130, 227, 637, 601, 843, 25, 479, 227, 328, 765, 902, 1, 624, 142, 113,
        522, 200, 900, 865, 479, 267, 630, 416, 868, 237, 1, 613, 130, 865, 479,
        567, 21, 550, 26, 64, 559, 26, 841, 115, 479, 841, 0, 0, 808, 777, 6, 514,
        58, 765, 871, 818, 206, 868, 177, 258, 236, 868, 567, 425, 592, 17, 146,
        118, 537, 448, 537, 448, 535, 479, 567, 21, 550, 26, 64, 559, 26, 841, 115,
        479, 841, 0, 0, 808, 777, 6, 514, 58, 765, 877, 539, 902, 31, 251, 786, 557,
        565, 1, 372, 900, 865, 479, 840, 25, 479, 227, 841, 63, 125, 205, 479, 13,
        588, 865, 479, 537, 25, 644, 296, 450, 304, 570, 805, 26, 30, 536, 314, 104,
        634, 865, 479, 73, 714, 436, 412, 39, 661, 428, 120
    ]

    assert encode_high(to_bytes(TEST_DATA), 6, 2) == expected


def test_encode_low():

    # Low level encoding
    expected = [
        [130728, 119920, 82192, 93980, 67848, 99590, 66798, 110200, 128318, 260649],
        [130728, 129678, 101252, 127694, 75652, 113982, 97944, 129720, 129678, 260649],
        [130728, 86496, 66846, 104188, 106814, 96800, 93944, 102290, 119934, 260649],
        [130728, 128190, 73160, 96008, 102812, 67872, 115934, 73156, 119520, 260649],
        [130728, 120588, 104224, 129720, 129938, 119200, 81084, 101252, 120588, 260649],
        [130728, 125892, 113798, 88188, 71822, 129766, 108158, 113840, 120784, 260649],
        [130728, 85880, 120638, 66758, 119006, 96008, 66758, 120256, 85560, 260649],
        [130728, 128176, 128352, 99048, 123146, 128280, 115920, 110492, 128176, 260649],
        [130728, 129634, 99166, 67438, 81644, 127604, 67404, 111676, 85054, 260649],
        [130728, 107422, 91664, 121136, 73156, 78032, 79628, 99680, 107452, 260649],
        [130728, 119692, 125744, 107396, 85894, 70600, 123914, 70600, 119692, 260649],
        [130728, 129588, 77902, 105628, 67960, 113798, 88188, 71822, 107390, 260649],
        [130728, 82208, 120638, 108348, 117798, 120638, 66758, 119006, 106672, 260649],
        [130728, 128070, 101252, 123018, 128352, 128352, 99048, 123146, 128070, 260649],
        [130728, 82206, 108792, 72094, 84028, 99166, 69442, 97048, 82108, 260649],
        [130728, 124350, 81384, 89720, 91712, 67618, 112848, 69712, 104160, 260649],
        [130728, 83928, 129720, 116966, 97968, 81084, 101252, 127450, 83928, 260649],
        [130728, 124392, 128456, 67960, 121150, 98018, 85240, 82206, 124388, 260649],
        [130728, 126222, 112152, 96008, 120560, 77928, 73160, 96008, 111648, 260649],
        [130728, 82918, 70600, 125702, 78322, 121744, 116762, 103328, 82918, 260649],
        [130728, 74992, 80048, 73296, 129766, 128450, 97072, 116210, 93424, 260649],
        [130728, 93744, 106800, 101784, 73160, 96008, 125116, 126828, 112440, 260649],
        [130728, 127628, 120948, 102632, 120582, 78074, 128532, 85966, 127628, 260649]
    ]

    assert list(encode(TEST_DATA, 6, 2)) == expected


def test_encode_unicode():
    # These two should encode to the same string
    uc = u"love 💔"
    by = b"love \xf0\x9f\x92\x94"

    expected = [
        [130728, 120256, 108592, 115526, 126604,
         103616, 66594, 126094, 128318, 260649],
        [130728, 125456, 83916, 107396, 83872,
         97968, 77702, 98676, 128352, 260649],
        [130728, 86496, 128114, 90190, 98038,
         72124, 72814, 81040, 86256, 260649]]

    assert encode(uc) == expected
    assert encode(by) == expected
