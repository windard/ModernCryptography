# -*- coding: utf-8 -*-


def get_total_path(length=2):
    """
    这道题我会，😂， 简直太会了
    :param length:
    :return:
    """
    dp =[[0 for _ in range(length+1)] for _ in range(length+1)]
    for i in range(length+1):
        for j in range(length+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j]+dp[i][j-1]
    return dp[length][length]


if __name__ == '__main__':

    print(get_total_path(2))
    print(get_total_path(20))
