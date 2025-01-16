import sys
import os

HEADER = """@relation alphabet

@attribute pixel_01 numeric
@attribute pixel_02 numeric
@attribute pixel_03 numeric
@attribute pixel_04 numeric
@attribute pixel_05 numeric
@attribute pixel_06 numeric
@attribute pixel_07 numeric
@attribute pixel_08 numeric
@attribute pixel_09 numeric
@attribute pixel_10 numeric
@attribute pixel_11 numeric
@attribute pixel_12 numeric
@attribute pixel_13 numeric
@attribute pixel_14 numeric
@attribute pixel_15 numeric
@attribute pixel_16 numeric
@attribute pixel_17 numeric
@attribute pixel_18 numeric
@attribute pixel_19 numeric
@attribute pixel_20 numeric
@attribute pixel_21 numeric
@attribute pixel_22 numeric
@attribute pixel_23 numeric
@attribute pixel_24 numeric
@attribute pixel_25 numeric
@attribute pixel_26 numeric
@attribute pixel_27 numeric
@attribute pixel_28 numeric
@attribute pixel_29 numeric
@attribute pixel_30 numeric
@attribute pixel_31 numeric
@attribute pixel_32 numeric
@attribute pixel_33 numeric
@attribute pixel_34 numeric
@attribute pixel_35 numeric
@attribute class {A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z}

@data"""



def convert_to_binary(lines):
    binary_data = []
    
    # 5x7 の文字データ（35文字）を入力
    for line in lines:
        line = line.rstrip().ljust(5, '0')
        binary_data.extend("1" if char == "#" else "0" for char in line)
    
    return ",".join(binary_data)



if __name__ == "__main__":
    file_path = 'my_test_alphabet.arff'
    if 2 <= len(sys.argv): # 引数があった場合それを使う
        file_path = sys.argv[1]

    if not os.path.exists(file_path):
        # ファイルが存在しない場合、新規作成してテンプレートを書き込む
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(HEADER)
        print(f"ファイル '{file_path}' を新しく作成しました。")

    while True:
        lines = []
        label = input('解答=')
        for _ in range(7):
            lines.append(sys.stdin.readline())
        binary = convert_to_binary(lines)

        print('保存する場合は\'s\'終了する場合は\'e\'を入力してください。(保存して終了\'se\')')
        cmd = input()
        if 's' in cmd:
            with open(file_path, "a", encoding="utf-8") as file:
                file.write(f'\n{binary},{label}')
            print(f"ファイル '{file_path}' に {label} を追記しました。")
        if 'e' in cmd:
            break
