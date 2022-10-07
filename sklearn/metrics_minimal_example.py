# An example I use in tutorials I develop
from sklearn.metrics import accuracy_score, precision_score, recall_score

ground_truth = [1, 1, 1, 0, 1, 0, 0, 0, 1, 1]
score_list = [0.8, 0.75, 0.68, 0.1, 0.9, 0.22, 0.66, 0.12, 0.64, 0.61]

thr_list = [i/10 for i in range(0, 11)]

for thr in thr_list:
    y_pred = [1*(s >= thr) for s in score_list]
    acc_calculated = accuracy_score(ground_truth, y_pred)
    precision_calculated = precision_score(
        ground_truth, y_pred, zero_division=0)
    recall_calculated = recall_score(ground_truth, y_pred, zero_division=0)
    print(f'{thr}: {acc_calculated}, {recall_calculated}, {precision_calculated}')
