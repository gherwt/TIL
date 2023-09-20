import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):

    N = int(input())
    sell_prices = list(map(int, input().split()))

    total_buy = 0
    benefits = 0
    count = 0
    max_price = 0

    for i in range(N-1, -1, -1):
        if max_price > sell_prices[i]:  # 마지막 것부터 비교
            count += 1
            total_buy += sell_prices[i]
        elif sell_prices[i] > max_price:
            benefits += max_price * count - total_buy
            count = 0
            total_buy = 0
            max_price = sell_prices[i]

    result = benefits + ((max_price * count) - total_buy)

    if result < 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {result}')


    # max value 찾는 문제이다.
    # 이윤들의 합 중 가장 큰 값을 찾는다.
    # 나올 수 있는 가짓 수를 다 생각해야한다.
    # 뒤에서부터 보기
    # 뒤에서부터 가격을 비교 앞에보다 비싸면 산다.
    # sum 하고 count 한 다음에 count * 뒤에서부터 비교한 가격 - sum
    # 이렇게 max 값 구하기

    # 사재기를 하겠다.
    # N일동안 문걸의 매매가를 예측하여 알고 있당.
    # 하루에 1개만 사겠다.
    # 팔떄는 한꺼번에 판매 가능
    # 1, 2,구매 -> 3일째에 판매.
    # n-1 까지 더하고 마지막 n 값에 n-1 곱함 그리고 1~ n-1 은