if __name__ == "__main__":
    with open("D:/work_space/ML_practice/data/训练数据-ccf_first_round_user_shop_behavior.csv") as f:
        cnt = 0
        lines = []
        for line in f:
            lines.append(line)
            cnt += 1
            if cnt == 100:
                break
        for line in lines:
            print(line)