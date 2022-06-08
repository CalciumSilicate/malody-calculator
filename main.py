from copy import deepcopy


def make_choice(l, default: int = None, text=None):
    raw_l = deepcopy(l)
    l = list(l)
    l.extend([False, True])
    for x in range(len(l)):
        if l[x] is True and default is not None:
            i = '使用默认设置({})'.format(default)
        elif l[x] is False:
            i = '退出选择'
        elif l[x] not in [True, False]:
            i = l[x]
        else:
            i = None
        if i is not None:
            print('{}、{}'.format(x, i))
    a = input('请输入选择{}>>>'.format('' if text is None else '({})'.format(text)))
    if a in l:
        return [a, l.index(a), l]
    try:
        a = int(a)
    except:
        return [a]

    if a < 0 or a >= len(l):
        print('输入有误，请重新选择')
        make_choice(raw_l, default=default)
    elif l[a] is True:
        if default is None:
            print('输入有误，请重新选择')
            make_choice(raw_l, default=default)
        else:
            return [l[default], default, l]
    elif l[a] is False:
        raise Exception
    else:
        return [l[a], a, l]


dan_list = {
    'Regular-0': [492, 529, 595, 681],
    'Regular-1': [695, 621, 718, 1279],
    'Regular-2': [1397, 1090, 805, 1212],
    'Regular-3': [1055, 1489, 1288, 1789],
    'Regular-4': [1865, 1434, 1284, 1839],
    'Regular-5': [1282, 1706, 1473, 1939],
    'Regular-6': [1694, 1636, 1803, 2115],
    'Regular-7': [1701, 1799, 2132, 1899],
    'Regular-8': [2237, 2081, 2280, 2000],
    'Regular-9': [2374, 1889, 2142, 1810],
    'Regular-10': [2034, 1740, 2270, 2166],
    'Extra-1': [1952, 2013, 1953, 2111],
    'Extra-2': [2107, 1953, 2386, 2674],
    'Extra-3': [2518, 2636, 2326, 2511],
    'Extra-4': [2634, 2212, 2336, 2602],
    'Extra-5': [2734, 2417, 3089, 2974],
    'Extra-6': [2483, 2276, 2921, 3194],
    'Extra-7': [2846, 2260, 2333, 3347],
    'Extra-8': [3789, 3663, 2424, 3255],
    'Extra-9': [3888, 3030, 3581, 3700],
    'Extra-Final': [2828, 3362, 3393, 5100],
    'Custom': False
}

mode = make_choice(['计算单曲ACC', '通过单曲ACC估计段位ACC'])[1]
cho = make_choice(list(dan_list.keys()))
dan = cho[0]
if dan == 'Custom':
    N_a = int(input('请输入第1首的物量>>>'))
    N_b = int(input('请输入第2首的物量>>>'))
    N_c = int(input('请输入第3首的物量>>>'))
    N_d = int(input('请输入第4首的物量>>>'))
else:
    N_a, N_b, N_c, N_d = dan_list[dan][0], dan_list[dan][1], dan_list[dan][2], dan_list[dan][3]
print('物量分别为:{} {} {} {}\n总物量为:{}'.format(N_a, N_b, N_c, N_d, sum([N_a, N_b, N_c, N_d])))
if mode:
    A_a = float(input('请输入第1首单曲ACC>>>'))
    A_b = float(input('请输入第2首单曲ACC>>>'))
    A_c = float(input('请输入第3首单曲ACC>>>'))
    A_d = float(input('请输入第4首单曲ACC>>>'))
    A_A = A_a
    A_B = (A_a * N_a + A_b * N_b) / (N_a + N_b)
    A_C = (A_a * N_a + A_b * N_b + A_c * N_c) / (N_a + N_b + N_c)
    A_D = (A_a * N_a + A_b * N_b + A_c * N_c + A_d * N_d) / (N_a + N_b + N_c + N_d)
    if cho[1] >= 3:
        print('Jack: {}%，结束时{}%\nTech: {}%，结束时{}%\nSpeed: {}%，结束时{}%\nStream: {}%，结束时{}%\nTotal: {}%'.format(
            round(A_a, 2), round(A_A, 2), round(A_b, 2), round(A_B, 2), round(A_c, 2), round(A_C, 2), round(A_d, 2),
            round(A_D, 2), A_D).replace('Jack', 'Jack' if dan != 'Custom' else '1').replace('Tech', 'Tech' if dan != 'Custom' else '2').replace('Speed', 'Speed' if dan != 'Custom' else '3').replace('Stream', 'Stream' if dan != 'Custom' else '4'))
    else:
        print('1: {}%\n2: {}%\n3: {}%\n4: {}%\nTotal: {}%'.format(A_a, A_b, A_c, A_d, A_D))

else:
    A_A = float(input('请输入出第1首时ACC>>>'))
    A_B = float(input('请输入出第2首时ACC>>>'))
    A_C = float(input('请输入出第3首时ACC>>>'))
    A_D = float(input('请输入最终ACC>>>'))
    A_a = A_A
    A_b = (A_B * sum([N_a, N_b]) - A_a * N_a) / N_b
    A_c = (A_C * sum([N_a, N_b, N_c]) - A_a * N_a - A_b * N_b) / N_c
    A_d = (A_D * sum([N_a, N_b, N_c, N_d]) - A_a * N_a - A_b * N_b - A_c * N_c) / N_d
    if cho[1] >= 3:
        print('Jack: {}%\nTech: {}%\nSpeed: {}%\nStream: {}%\nTotal: {}%'.format(round(A_a, 2), round(A_b, 2),
                                                                                 round(A_c, 2), round(A_d, 2), A_D))
    else:
        print('1: {}%\n2: {}%\n3: {}%\n4: {}%\nTotal: {}%'.format(A_a, A_b, A_c, A_d, A_D))
input('按下回车以退出...')
