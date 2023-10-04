N = int(input())
scores = list(map(int, input().split()))

ch_scores = []
M = max(scores)

for score in scores:
    new_score = (score/M)*100  # (각각의 점수/점수의 최대값) * 100

    ch_scores.append(new_score)  # 조정한 점수로 새 리스트 작성.

print(sum(ch_scores)/N)

    
