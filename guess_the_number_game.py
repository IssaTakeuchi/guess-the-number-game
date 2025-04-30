import sys
import random

def main():
    if len(sys.argv) != 3:
        print("使い方：python スクリプト名.py <最小値> <最大値>")
        return #プログラムを終了
    
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("エラー：最小値と最大値は整数で入力してください。")
        return #プログラムを終了
    
    if num1 > num2:
        print("エラー：最小値、最大値の順に入力してください。")
        return #プログラムを終了
    
    random_int = random.randint(num1,num2)

    for _ in range(3):
        try:
            input_str = input("整数を入力してください。")
            integer_variable = int(input_str)
        except ValueError:
            print("エラー：整数を入力してください。")
            continue #入力が整数でなければ次の試行へ

        if random_int == integer_variable:
            print("お見事！！")
            return #成功したら終了
        else :
            print("try again..")

    print(f"残念！正解は {random_int} でした。") #3回失敗後に表示

if __name__ == "__main__":
    main()
    
