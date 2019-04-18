"""
---プログラム概要---
1.display.html表示
2.csvにセンサデータを書き込む
3.csvのデータを返す
"""



from flask import Flask, request, render_template
app = Flask(__name__)
file_path = "./sensor_data.csv"
my_port = 16046


# 1.display.html表示
@app.route('/', methods=['GET'])
def get_html():
  return render_template('./index_iot.html')


# 2.csvにセンサデータを書き込む
@app.route('/lux', methods=['POST'])
def update_lux():
  time = request.form["time"]
  lux = request.form["lux"]
  try:
    f = open(file_path, 'w')
    f.write(time + "," + lux)
    return "succeeded to write"
  except Exception as e:
    print(e)
    return "failed to write"
  finally:
    f.close()


# 3.csvのデータを返す
@app.route('/lux', methods=['GET'])
def get_lux():
  try:
    f = open(file_path, 'r')
    for row in f:
      lux = row
    return lux
  except Exception as e:
    print(e)
    return e
  finally:
    f.close()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=my_port)