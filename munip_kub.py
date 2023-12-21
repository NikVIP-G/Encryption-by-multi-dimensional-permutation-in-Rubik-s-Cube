def U(m_kub: list):
    new_kub_0 = [
        [m_kub[0][0][0], m_kub[0][0][1], m_kub[0][0][2]],
        [m_kub[0][1][0], m_kub[0][1][1], m_kub[0][1][2]],
        [m_kub[1][2][2], m_kub[1][1][2], m_kub[1][0][2]]
    ]

    new_kub_1 = [
        [m_kub[1][0][0], m_kub[1][0][1], m_kub[4][0][0]],
        [m_kub[1][1][0], m_kub[1][1][1], m_kub[4][0][1]],
        [m_kub[1][2][0], m_kub[1][2][1], m_kub[4][0][2]]
    ]

    new_kub_2 = [
        [m_kub[2][2][0], m_kub[2][1][0], m_kub[2][0][0]],
        [m_kub[2][2][1], m_kub[2][1][1], m_kub[2][0][1]],
        [m_kub[2][2][2], m_kub[2][1][2], m_kub[2][0][2]]
    ]

    new_kub_3 = [
        [m_kub[0][2][0], m_kub[3][0][1], m_kub[3][0][2]],
        [m_kub[0][2][1], m_kub[3][1][1], m_kub[3][1][2]],
        [m_kub[0][2][2], m_kub[3][2][1], m_kub[3][2][2]]
    ]

    new_kub_4 = [
        [m_kub[3][2][0], m_kub[3][1][0], m_kub[3][0][0]],
        [m_kub[4][1][0], m_kub[4][1][1], m_kub[4][1][2]],
        [m_kub[4][2][0], m_kub[4][2][1], m_kub[4][2][2]]
    ]

    m_kub[0] = new_kub_0
    m_kub[1] = new_kub_1
    m_kub[2] = new_kub_2
    m_kub[3] = new_kub_3
    m_kub[4] = new_kub_4

    return m_kub


def nU(m_kub: list):
    new_kub_2 = [
        [m_kub[2][0][2], m_kub[2][1][2], m_kub[2][2][2]],
        [m_kub[2][0][1], m_kub[2][1][1], m_kub[2][2][1]],
        [m_kub[2][0][0], m_kub[2][1][0], m_kub[2][2][0]]
    ]

    new_kub_0 = [
        [m_kub[0][0][0], m_kub[0][0][1], m_kub[0][0][2]],
        [m_kub[0][1][0], m_kub[0][1][1], m_kub[0][1][2]],
        [m_kub[3][0][0], m_kub[3][1][0], m_kub[3][2][0]]
    ]

    new_kub_1 = [
        [m_kub[1][0][0], m_kub[1][0][1], m_kub[0][2][2]],
        [m_kub[1][1][0], m_kub[1][1][1], m_kub[0][2][1]],
        [m_kub[1][2][0], m_kub[1][2][1], m_kub[0][2][0]]
    ]

    new_kub_3 = [
        [m_kub[4][0][2], m_kub[3][0][1], m_kub[3][0][2]],
        [m_kub[4][0][1], m_kub[3][1][1], m_kub[3][1][2]],
        [m_kub[4][0][0], m_kub[3][2][1], m_kub[3][2][2]]
    ]

    new_kub_4 = [
        [m_kub[1][0][2], m_kub[1][1][2], m_kub[1][2][2]],
        [m_kub[4][1][0], m_kub[4][1][1], m_kub[4][1][2]],
        [m_kub[4][2][0], m_kub[4][2][1], m_kub[4][2][2]]
    ]

    m_kub[0] = new_kub_0
    m_kub[1] = new_kub_1
    m_kub[2] = new_kub_2
    m_kub[3] = new_kub_3
    m_kub[4] = new_kub_4

    return m_kub


def D(m_kub: list):
    new_kub_0 = [
        [m_kub[3][0][2], m_kub[3][1][2], m_kub[3][2][2]],
        [m_kub[0][1][0], m_kub[0][1][1], m_kub[0][1][2]],
        [m_kub[0][2][0], m_kub[0][2][1], m_kub[0][2][2]]
    ]

    new_kub_1 = [
        [m_kub[0][0][2], m_kub[1][0][1], m_kub[1][0][2]],
        [m_kub[0][0][1], m_kub[1][1][1], m_kub[1][1][2]],
        [m_kub[0][0][0], m_kub[1][2][1], m_kub[1][2][2]]
    ]

    new_kub_3 = [
        [m_kub[3][0][0], m_kub[3][0][1], m_kub[4][2][2]],
        [m_kub[3][1][0], m_kub[3][1][1], m_kub[4][2][1]],
        [m_kub[3][2][0], m_kub[3][2][1], m_kub[4][2][0]]
    ]

    new_kub_4 = [
        [m_kub[4][0][0], m_kub[4][0][1], m_kub[4][0][2]],
        [m_kub[4][1][0], m_kub[4][1][1], m_kub[4][1][2]],
        [m_kub[1][0][0], m_kub[1][1][0], m_kub[1][2][0]]
    ]

    new_kub_5 = [
        [m_kub[5][0][2], m_kub[5][1][2], m_kub[5][2][2]],
        [m_kub[5][0][1], m_kub[5][1][1], m_kub[5][2][1]],
        [m_kub[5][0][0], m_kub[5][1][0], m_kub[5][2][0]]
    ]

    m_kub[0] = new_kub_0
    m_kub[1] = new_kub_1
    m_kub[4] = new_kub_4
    m_kub[3] = new_kub_3
    m_kub[5] = new_kub_5

    return m_kub


def nD(m_kub: list):
    new_kub_0 = [
        [m_kub[1][2][0], m_kub[1][1][0], m_kub[1][0][0]],
        [m_kub[0][1][0], m_kub[0][1][1], m_kub[0][1][2]],
        [m_kub[0][2][0], m_kub[0][2][1], m_kub[0][2][2]]
    ]

    new_kub_1 = [
        [m_kub[4][2][0], m_kub[1][0][1], m_kub[1][0][2]],
        [m_kub[4][2][1], m_kub[1][1][1], m_kub[1][1][2]],
        [m_kub[4][2][2], m_kub[1][2][1], m_kub[1][2][2]]
    ]

    new_kub_3 = [
        [m_kub[3][0][0], m_kub[3][0][1], m_kub[0][0][0]],
        [m_kub[3][1][0], m_kub[3][1][1], m_kub[0][0][1]],
        [m_kub[3][2][0], m_kub[3][2][1], m_kub[0][0][2]]
    ]

    new_kub_4 = [
        [m_kub[4][0][0], m_kub[4][0][1], m_kub[4][0][2]],
        [m_kub[4][1][0], m_kub[4][1][1], m_kub[4][1][2]],
        [m_kub[3][2][2], m_kub[3][1][2], m_kub[3][0][2]]
    ]

    new_kub_5 = [
        [m_kub[5][2][0], m_kub[5][1][0], m_kub[5][0][0]],
        [m_kub[5][2][1], m_kub[5][1][1], m_kub[5][0][1]],
        [m_kub[5][2][2], m_kub[5][1][2], m_kub[5][0][2]]
    ]

    m_kub[0] = new_kub_0
    m_kub[1] = new_kub_1
    m_kub[4] = new_kub_4
    m_kub[3] = new_kub_3
    m_kub[5] = new_kub_5

    return m_kub


def R(m_kub: list):
    new_kub_0 = [
        [m_kub[0][0][0], m_kub[0][0][1], m_kub[2][0][2]],
        [m_kub[0][1][0], m_kub[0][1][1], m_kub[2][1][2]],
        [m_kub[0][2][0], m_kub[0][2][1], m_kub[2][2][2]]
    ]

    new_kub_2 = [
        [m_kub[2][0][0], m_kub[2][0][1], m_kub[4][0][2]],
        [m_kub[2][1][0], m_kub[2][1][1], m_kub[4][1][2]],
        [m_kub[2][2][0], m_kub[2][2][1], m_kub[4][2][2]]
    ]

    new_kub_3 = [
        [m_kub[3][2][0], m_kub[3][1][0], m_kub[3][0][0]],
        [m_kub[3][2][1], m_kub[3][1][1], m_kub[3][0][1]],
        [m_kub[3][2][2], m_kub[3][1][2], m_kub[3][0][2]]
    ]

    new_kub_4 = [
        [m_kub[4][0][0], m_kub[4][0][1], m_kub[5][0][2]],
        [m_kub[4][1][0], m_kub[4][1][1], m_kub[5][1][2]],
        [m_kub[4][2][0], m_kub[4][2][1], m_kub[5][2][2]]
    ]

    new_kub_5 = [
        [m_kub[5][0][0], m_kub[5][0][1], m_kub[0][0][2]],
        [m_kub[5][1][0], m_kub[5][1][1], m_kub[0][1][2]],
        [m_kub[5][2][0], m_kub[5][2][1], m_kub[0][2][2]]
    ]

    m_kub[0] = new_kub_0
    m_kub[2] = new_kub_2
    m_kub[4] = new_kub_4
    m_kub[3] = new_kub_3
    m_kub[5] = new_kub_5

    return m_kub


def nR(m_kub: list):
    new_kub_0 = [
        [m_kub[0][0][0], m_kub[0][0][1], m_kub[5][0][2]],
        [m_kub[0][1][0], m_kub[0][1][1], m_kub[5][1][2]],
        [m_kub[0][2][0], m_kub[0][2][1], m_kub[5][2][2]]
    ]

    new_kub_2 = [
        [m_kub[2][0][0],m_kub[2][0][1],m_kub[0][0][2]],
        [m_kub[2][1][0],m_kub[2][1][1],m_kub[0][1][2]],
        [m_kub[2][2][0],m_kub[2][2][1],m_kub[0][2][2]]
    ]

    new_kub_3 = [
        [m_kub[3][0][2],m_kub[3][1][2],m_kub[3][2][2]],
        [m_kub[3][0][1],m_kub[3][1][1],m_kub[3][2][1]],
        [m_kub[3][0][0],m_kub[3][1][0],m_kub[3][2][0]]
    ]

    new_kub_4 = [
        [m_kub[4][0][0], m_kub[4][0][1], m_kub[2][0][2]],
        [m_kub[4][1][0], m_kub[4][1][1], m_kub[2][1][2]],
        [m_kub[4][2][0], m_kub[4][2][1], m_kub[2][2][2]]
    ]

    new_kub_5 = [
        [m_kub[5][0][0], m_kub[5][0][1], m_kub[4][0][2]],
        [m_kub[5][1][0], m_kub[5][1][1], m_kub[4][1][2]],
        [m_kub[5][2][0], m_kub[5][2][1], m_kub[4][2][2]]
    ]

    m_kub[0] = new_kub_0
    m_kub[2] = new_kub_2
    m_kub[4] = new_kub_4
    m_kub[3] = new_kub_3
    m_kub[5] = new_kub_5

    return m_kub


def L(m_kub: list):
    new_kub_0 = [
        [m_kub[5][0][0], m_kub[0][0][1], m_kub[0][0][2]],
        [m_kub[5][1][0], m_kub[0][1][1], m_kub[0][1][2]],
        [m_kub[5][2][0], m_kub[0][2][1], m_kub[0][2][2]]
    ]

    new_kub_2 = [
        [m_kub[0][0][0], m_kub[2][0][1], m_kub[2][0][2]],
        [m_kub[0][1][0], m_kub[2][1][1], m_kub[2][1][2]],
        [m_kub[0][2][0], m_kub[2][2][1], m_kub[2][2][2]]
    ]

    new_kub_1 = [
        [m_kub[1][2][0], m_kub[1][1][0], m_kub[1][0][0]],
        [m_kub[1][2][1], m_kub[1][1][1], m_kub[1][0][1]],
        [m_kub[1][2][2], m_kub[1][1][2], m_kub[1][0][2]]
    ]

    new_kub_4 = [
        [m_kub[2][0][0], m_kub[4][0][1], m_kub[4][0][2]],
        [m_kub[2][1][0], m_kub[4][1][1], m_kub[4][1][2]],
        [m_kub[2][2][0], m_kub[4][2][1], m_kub[4][2][2]]
    ]

    new_kub_5 = [
        [m_kub[4][0][0], m_kub[5][0][1], m_kub[5][0][2]],
        [m_kub[4][1][0], m_kub[5][1][1], m_kub[5][1][2]],
        [m_kub[4][2][0], m_kub[5][2][1], m_kub[5][2][2]]
    ]

    m_kub[0] = new_kub_0
    m_kub[1] = new_kub_1
    m_kub[4] = new_kub_4
    m_kub[2] = new_kub_2
    m_kub[5] = new_kub_5

    return m_kub


def nL(m_kub: list):
    new_kub_0 = [
        [m_kub[2][0][0], m_kub[0][0][1], m_kub[0][0][2]],
        [m_kub[2][1][0], m_kub[0][1][1], m_kub[0][1][2]],
        [m_kub[2][2][0], m_kub[0][2][1], m_kub[0][2][2]]
    ]

    new_kub_2 = [
        [m_kub[4][0][0], m_kub[2][0][1], m_kub[2][0][2]],
        [m_kub[4][1][0], m_kub[2][1][1], m_kub[2][1][2]],
        [m_kub[4][2][0], m_kub[2][2][1], m_kub[2][2][2]]
    ]

    new_kub_1 = [
        [m_kub[1][0][2], m_kub[1][1][2], m_kub[1][2][2]],
        [m_kub[1][0][1], m_kub[1][1][1], m_kub[1][2][1]],
        [m_kub[1][0][0], m_kub[1][1][0], m_kub[1][2][0]]
    ]

    new_kub_4 = [
        [m_kub[5][0][0], m_kub[4][0][1], m_kub[4][0][2]],
        [m_kub[5][1][0], m_kub[4][1][1], m_kub[4][1][2]],
        [m_kub[5][2][0], m_kub[4][2][1], m_kub[4][2][2]]
    ]

    new_kub_5 = [
        [m_kub[0][0][0], m_kub[5][0][1], m_kub[5][0][2]],
        [m_kub[0][1][0], m_kub[5][1][1], m_kub[5][1][2]],
        [m_kub[0][2][0], m_kub[5][2][1], m_kub[5][2][2]]
    ]

    m_kub[0] = new_kub_0
    m_kub[2] = new_kub_2
    m_kub[4] = new_kub_4
    m_kub[1] = new_kub_1
    m_kub[5] = new_kub_5

    return m_kub


def F(m_kub: list):
    new_kub_1 = [
        [m_kub[1][0][0], m_kub[1][0][1], m_kub[1][0][2]],
        [m_kub[1][1][0], m_kub[1][1][1], m_kub[1][1][2]],
        [m_kub[5][0][0], m_kub[5][0][1], m_kub[5][0][2]]
    ]

    new_kub_2 = [
        [m_kub[2][0][0], m_kub[2][0][1], m_kub[2][0][2]],
        [m_kub[2][1][0], m_kub[2][1][1], m_kub[2][1][2]],
        [m_kub[1][2][0], m_kub[1][2][1], m_kub[1][2][2]]
    ]

    new_kub_4 = [
        [m_kub[4][2][0], m_kub[4][1][0], m_kub[4][0][0]],
        [m_kub[4][2][1], m_kub[4][1][1], m_kub[4][0][1]],
        [m_kub[4][2][2], m_kub[4][1][2], m_kub[4][0][2]]
    ]

    new_kub_3 = [
        [m_kub[3][0][0], m_kub[3][0][1], m_kub[3][0][2]],
        [m_kub[3][1][0], m_kub[3][1][1], m_kub[3][1][2]],
        [m_kub[2][2][0], m_kub[2][2][1], m_kub[2][2][2]]
    ]

    new_kub_5 = [
        [m_kub[3][2][0], m_kub[3][2][1], m_kub[3][2][2]],
        [m_kub[5][1][0], m_kub[5][1][1], m_kub[5][1][2]],
        [m_kub[5][2][0], m_kub[5][2][1], m_kub[5][2][2]]
    ]

    m_kub[3] = new_kub_3
    m_kub[1] = new_kub_1
    m_kub[4] = new_kub_4
    m_kub[2] = new_kub_2
    m_kub[5] = new_kub_5

    return m_kub


def nF(m_kub: list):
    new_kub_1 = [
        [m_kub[1][0][0], m_kub[1][0][1], m_kub[1][0][2]],
        [m_kub[1][1][0], m_kub[1][1][1], m_kub[1][1][2]],
        [m_kub[2][2][0], m_kub[2][2][1], m_kub[2][2][2]]
    ]

    new_kub_2 = [
        [m_kub[2][0][0], m_kub[2][0][1], m_kub[2][0][2]],
        [m_kub[2][1][0], m_kub[2][1][1], m_kub[2][1][2]],
        [m_kub[3][2][0], m_kub[3][2][1], m_kub[3][2][2]]
    ]

    new_kub_4 = [
        [m_kub[4][0][2], m_kub[4][1][2], m_kub[4][2][2]],
        [m_kub[4][0][1], m_kub[4][1][1], m_kub[4][2][1]],
        [m_kub[4][0][0], m_kub[4][1][0], m_kub[4][2][0]]
    ]

    new_kub_3 = [
        [m_kub[3][0][0], m_kub[3][0][1], m_kub[3][0][2]],
        [m_kub[3][1][0], m_kub[3][1][1], m_kub[3][1][2]],
        [m_kub[5][0][0], m_kub[5][0][1], m_kub[5][0][2]]
    ]

    new_kub_5 = [
        [m_kub[1][2][0], m_kub[1][2][1], m_kub[1][2][2]],
        [m_kub[5][1][0], m_kub[5][1][1], m_kub[5][1][2]],
        [m_kub[5][2][0], m_kub[5][2][1], m_kub[5][2][2]]
    ]

    m_kub[3] = new_kub_3
    m_kub[1] = new_kub_1
    m_kub[4] = new_kub_4
    m_kub[2] = new_kub_2
    m_kub[5] = new_kub_5

    return m_kub


def nB(m_kub: list):
    new_kub_1 = [
        [m_kub[5][2][0], m_kub[5][2][1], m_kub[5][2][2]],
        [m_kub[1][1][0], m_kub[1][1][1], m_kub[1][1][2]],
        [m_kub[1][2][0], m_kub[1][2][1], m_kub[1][2][2]]
    ]

    new_kub_2 = [
        [m_kub[1][0][0], m_kub[1][0][1], m_kub[1][0][2]],
        [m_kub[2][1][0], m_kub[2][1][1], m_kub[2][1][2]],
        [m_kub[2][2][0], m_kub[2][2][1], m_kub[2][2][2]]
    ]

    new_kub_0 = [
        [m_kub[0][0][2], m_kub[0][1][2], m_kub[0][2][2]],
        [m_kub[0][0][1], m_kub[0][1][1], m_kub[0][2][1]],
        [m_kub[0][0][0], m_kub[0][1][0], m_kub[0][2][0]]
    ]

    new_kub_3 = [
        [m_kub[2][0][0], m_kub[2][0][1], m_kub[2][0][2]],
        [m_kub[3][1][0], m_kub[3][1][1], m_kub[3][1][2]],
        [m_kub[3][2][0], m_kub[3][2][1], m_kub[3][2][2]]
    ]

    new_kub_5 = [
        [m_kub[5][0][0], m_kub[5][0][1], m_kub[5][0][2]],
        [m_kub[5][1][0], m_kub[5][1][1], m_kub[5][1][2]],
        [m_kub[3][0][0], m_kub[3][0][1], m_kub[3][0][2]]
    ]

    m_kub[3] = new_kub_3
    m_kub[1] = new_kub_1
    m_kub[0] = new_kub_0
    m_kub[2] = new_kub_2
    m_kub[5] = new_kub_5

    return m_kub


def B(m_kub: list):
    new_kub_1 = [
        [m_kub[2][0][0], m_kub[2][0][1], m_kub[2][0][2]],
        [m_kub[1][1][0], m_kub[1][1][1], m_kub[1][1][2]],
        [m_kub[1][2][0], m_kub[1][2][1], m_kub[1][2][2]]
    ]

    new_kub_2 = [
        [m_kub[3][0][0], m_kub[3][0][1], m_kub[3][0][2]],
        [m_kub[2][1][0], m_kub[2][1][1], m_kub[2][1][2]],
        [m_kub[2][2][0], m_kub[2][2][1], m_kub[2][2][2]]
    ]

    new_kub_0 = [
        [m_kub[0][2][0], m_kub[0][1][0], m_kub[0][0][0]],
        [m_kub[0][2][1], m_kub[0][1][1], m_kub[0][0][1]],
        [m_kub[0][2][2], m_kub[0][1][2], m_kub[0][0][2]]
    ]

    new_kub_3 = [
        [m_kub[5][2][0], m_kub[5][2][1], m_kub[5][2][2]],
        [m_kub[3][1][0], m_kub[3][1][1], m_kub[3][1][2]],
        [m_kub[3][2][0], m_kub[3][2][1], m_kub[3][2][2]]
    ]

    new_kub_5 = [
        [m_kub[5][0][0], m_kub[5][0][1], m_kub[5][0][2]],
        [m_kub[5][1][0], m_kub[5][1][1], m_kub[5][1][2]],
        [m_kub[1][0][0], m_kub[1][0][1], m_kub[1][0][2]]
    ]

    m_kub[3] = new_kub_3
    m_kub[1] = new_kub_1
    m_kub[0] = new_kub_0
    m_kub[2] = new_kub_2
    m_kub[5] = new_kub_5

    return m_kub


def x(m_kub: list):
    new_kub_2 = [
        [m_kub[2][0][0], m_kub[4][0][1], m_kub[2][0][2]],
        [m_kub[2][1][0], m_kub[4][1][1], m_kub[2][1][2]],
        [m_kub[2][2][0], m_kub[4][2][1], m_kub[2][2][2]]
    ]

    new_kub_0 = [
        [m_kub[0][0][0], m_kub[2][0][1], m_kub[0][0][2]],
        [m_kub[0][1][0], m_kub[2][1][1], m_kub[0][1][2]],
        [m_kub[0][2][0], m_kub[2][2][1], m_kub[0][2][2]]
    ]

    new_kub_5 = [
        [m_kub[5][0][0], m_kub[0][0][1], m_kub[5][0][2]],
        [m_kub[5][1][0], m_kub[0][1][1], m_kub[5][1][2]],
        [m_kub[5][2][0], m_kub[0][2][1], m_kub[5][2][2]]
    ]

    new_kub_4 = [
        [m_kub[4][0][0], m_kub[5][0][1], m_kub[4][0][2]],
        [m_kub[4][1][0], m_kub[5][1][1], m_kub[4][1][2]],
        [m_kub[4][2][0], m_kub[5][2][1], m_kub[4][2][2]]
    ]

    m_kub[4] = new_kub_4
    m_kub[0] = new_kub_0
    m_kub[2] = new_kub_2
    m_kub[5] = new_kub_5

    return m_kub


def nx(m_kub: list):
    new_kub_2 = [
        [m_kub[2][0][0], m_kub[0][0][1], m_kub[2][0][2]],
        [m_kub[2][1][0], m_kub[0][1][1], m_kub[2][1][2]],
        [m_kub[2][2][0], m_kub[0][2][1], m_kub[2][2][2]]
    ]

    new_kub_0 = [
        [m_kub[0][0][0], m_kub[5][0][1], m_kub[0][0][2]],
        [m_kub[0][1][0], m_kub[5][1][1], m_kub[0][1][2]],
        [m_kub[0][2][0], m_kub[5][2][1], m_kub[0][2][2]]
    ]

    new_kub_5 = [
        [m_kub[5][0][0], m_kub[4][0][1], m_kub[5][0][2]],
        [m_kub[5][1][0], m_kub[4][1][1], m_kub[5][1][2]],
        [m_kub[5][2][0], m_kub[4][2][1], m_kub[5][2][2]]
    ]

    new_kub_4 = [
        [m_kub[4][0][0], m_kub[2][0][1], m_kub[4][0][2]],
        [m_kub[4][1][0], m_kub[2][1][1], m_kub[4][1][2]],
        [m_kub[4][2][0], m_kub[2][2][1], m_kub[4][2][2]]
    ]

    m_kub[4] = new_kub_4
    m_kub[0] = new_kub_0
    m_kub[2] = new_kub_2
    m_kub[5] = new_kub_5

    return m_kub


def y(m_kub: list):
    new_kub_1 = [
        [m_kub[1][0][0], m_kub[4][1][0], m_kub[1][0][2]],
        [m_kub[1][1][0], m_kub[4][1][1], m_kub[1][1][2]],
        [m_kub[1][2][0], m_kub[4][1][2], m_kub[1][2][2]]
    ]

    new_kub_0 = [
        [m_kub[0][0][0], m_kub[0][0][1], m_kub[0][0][2]],
        [m_kub[1][2][1], m_kub[1][1][1], m_kub[1][0][1]],
        [m_kub[0][2][0], m_kub[0][2][1], m_kub[0][2][2]]
    ]

    new_kub_3 = [
        [m_kub[3][0][0], m_kub[0][1][0], m_kub[3][0][2]],
        [m_kub[3][1][0], m_kub[0][1][1], m_kub[3][1][2]],
        [m_kub[3][2][0], m_kub[0][1][2], m_kub[3][2][2]]
    ]

    new_kub_4 = [
        [m_kub[4][0][0], m_kub[4][0][1], m_kub[4][0][2]],
        [m_kub[3][2][1], m_kub[3][1][1], m_kub[3][0][1]],
        [m_kub[4][2][0], m_kub[4][2][1], m_kub[4][2][2]]
    ]

    m_kub[4] = new_kub_4
    m_kub[0] = new_kub_0
    m_kub[1] = new_kub_1
    m_kub[3] = new_kub_3

    return m_kub


def ny(m_kub: list):
    new_kub_1 = [
        [m_kub[1][0][0], m_kub[0][1][2], m_kub[1][0][2]],
        [m_kub[1][1][0], m_kub[0][1][1], m_kub[1][1][2]],
        [m_kub[1][2][0], m_kub[0][1][0], m_kub[1][2][2]]
    ]

    new_kub_0 = [
        [m_kub[0][0][0], m_kub[0][0][1], m_kub[0][0][2]],
        [m_kub[3][0][1], m_kub[3][1][1], m_kub[3][2][1]],
        [m_kub[0][2][0], m_kub[0][2][1], m_kub[0][2][2]]
    ]

    new_kub_3 = [
        [m_kub[3][0][0], m_kub[4][1][2], m_kub[3][0][2]],
        [m_kub[3][1][0], m_kub[4][1][1], m_kub[3][1][2]],
        [m_kub[3][2][0], m_kub[4][1][0], m_kub[3][2][2]]
    ]

    new_kub_4 = [
        [m_kub[4][0][0], m_kub[4][0][1], m_kub[4][0][2]],
        [m_kub[1][0][1], m_kub[1][1][1], m_kub[1][2][1]],
        [m_kub[4][2][0], m_kub[4][2][1], m_kub[4][2][2]]
    ]

    m_kub[4] = new_kub_4
    m_kub[0] = new_kub_0
    m_kub[1] = new_kub_1
    m_kub[3] = new_kub_3

    return m_kub


def z(m_kub: list):
    new_kub_1 = [
        [m_kub[1][0][0], m_kub[1][0][1], m_kub[1][0][2]],
        [m_kub[5][1][2], m_kub[5][1][1], m_kub[5][1][0]],
        [m_kub[1][2][0], m_kub[1][2][1], m_kub[1][2][2]]
    ]

    new_kub_2 = [
        [m_kub[2][0][0], m_kub[2][0][1], m_kub[2][0][2]],
        [m_kub[1][1][0], m_kub[1][1][1], m_kub[1][1][2]],
        [m_kub[2][2][0], m_kub[2][2][1], m_kub[2][2][2]]
    ]

    new_kub_3 = [
        [m_kub[3][0][0], m_kub[3][0][1], m_kub[3][0][2]],
        [m_kub[2][1][0], m_kub[2][1][1], m_kub[2][1][2]],
        [m_kub[3][2][0], m_kub[3][2][1], m_kub[3][2][2]]
    ]

    new_kub_5 = [
        [m_kub[5][0][0], m_kub[5][0][1], m_kub[5][0][2]],
        [m_kub[3][1][2], m_kub[3][1][1], m_kub[3][1][0]],
        [m_kub[5][2][0], m_kub[5][2][1], m_kub[5][2][2]]
    ]

    m_kub[1] = new_kub_1
    m_kub[2] = new_kub_2
    m_kub[3] = new_kub_3
    m_kub[5] = new_kub_5

    return m_kub


def nz(m_kub: list):
    new_kub_1 = [
        [m_kub[1][0][0], m_kub[1][0][1], m_kub[1][0][2]],
        [m_kub[2][1][0], m_kub[2][1][1], m_kub[2][1][2]],
        [m_kub[1][2][0], m_kub[1][2][1], m_kub[1][2][2]]
    ]

    new_kub_2 = [
        [m_kub[2][0][0], m_kub[2][0][1], m_kub[2][0][2]],
        [m_kub[3][1][0], m_kub[3][1][1], m_kub[3][1][2]],
        [m_kub[2][2][0], m_kub[2][2][1], m_kub[2][2][2]]
    ]

    new_kub_3 = [
        [m_kub[3][0][0], m_kub[3][0][1], m_kub[3][0][2]],
        [m_kub[5][1][2], m_kub[5][1][1], m_kub[5][1][0]],
        [m_kub[3][2][0], m_kub[3][2][1], m_kub[3][2][2]]
    ]

    new_kub_5 = [
        [m_kub[5][0][0], m_kub[5][0][1], m_kub[5][0][2]],
        [m_kub[1][1][2], m_kub[1][1][1], m_kub[1][1][0]],
        [m_kub[5][2][0], m_kub[5][2][1], m_kub[5][2][2]]
    ]

    m_kub[1] = new_kub_1
    m_kub[2] = new_kub_2
    m_kub[3] = new_kub_3
    m_kub[5] = new_kub_5

    return m_kub
