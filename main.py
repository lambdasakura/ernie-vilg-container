import paddlehub as hub
import os
import datetime
import shutil
from pathlib import Path
import tempfile

# ernie_vilg実行プログラム
# https://github.com/PaddlePaddle/PaddleHub/tree/develop/modules/image/text_to_image/ernie_vilg#3api

module = hub.Module(name="ernie_vilg")
saved_path = os.path.join(os.getcwd(), "output")
Path(saved_path).mkdir(parents=True, exist_ok=True)

## このプログラムがgenerate_imageを何回するかを決める
## 1回で6枚生成される。つまり、生成される画像の枚数 = generate_count * 6 が毎回生成される。
generate_count = 3

prompt = ""
style="卡通"

with tempfile.TemporaryDirectory() as dname:
  for i in range(generate_count):
    print("generate_image: prompt={}, style={}".format(prompt, style))
    module.generate_image(
        text_prompts=[ prompt ], 
        style=style,
        output_dir=dname)
      
    ## ernie_vilgは同じファイルが既にあっても上書き保存してしまうので、生成された画像をrenameして別のディレクトリに保存する
    filelist = os.listdir(dname)
    print(filelist)
    for f in filelist:
      now = datetime.datetime.now()
      src_filename = os.path.join(dname, f)
      dst_filename = os.path.join(saved_path, prompt+ '_' + now.strftime('%Y%m%d_%H%M%S_%f') + '.png')
      print("move {} to {}".format(src_filename, dst_filename))
      new_path = shutil.move(src_filename, dst_filename)

