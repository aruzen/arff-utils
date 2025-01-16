import sys
from PIL import Image

def read_file(file_path):
    """ 指定されたファイルを読み込み、内容を表示する """
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print(f"エラー: ファイル '{file_path}' が見つかりません。")
    except Exception as e:
        print(f"エラー: {e}")



def print_arff_char(line):
    data = line.split(",")
    print(f"解答={data[-1]}")
    for y in range(7):
        for x in range(5):
            print(' ' if data[x+y*5] == '0' else '#', end='')
        print()



def generate_image(line, output_file="output.png"):
    data = line.split(",")
    width, height = 7, 9  # 文字のサイズ（5x7）

    # 白黒画像を作成
    img = Image.new("1", (width, height), "white")
    pixels = img.load()

    for y in range(height-2):
        for x in range(width-2):
            pixels[x+1, y+1] = 0 if data[x + y * (width - 2)] == '1' else 1  # 1:黒, 0:白
    
    img = img.resize((width * 20, height * 20), Image.NEAREST)  # 拡大して見やすくする
    img.save(output_file)



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python read_file.py <ファイル名> <出力先ディレクトリ>")

    txt = read_file(sys.argv[1])
    output = '.' if len(sys.argv) < 3 else sys.argv[2]
    _, _, txt = txt.partition("@data")
    
    for i, line in enumerate(txt.split("\n")[1:]):
        if len(line) < 70:
            continue
        print_arff_char(line)
        generate_image(line, f'{output}/{line[-1]}-{i}.png')
        print()

