from flask import Flask, request, render_template
app = Flask(__name__)
file_path = "./sensor_data.csv"
my_port = 16046

@app.route('/', methods = ['Get'])
def get_html():
    return render_template('./index.html')

@app.route('/lux', methods = ['POST'])
def update_lux():
    time = request.form["time"]
    lux = request.form["lux"]
    try:
        #追記モードに変更
        f = open(file_path, 'a')
        f.write(time + "," + lux + '\n')

        #100行越えたら新しく更新して1行目から書き込む

        f2 = open(file_path, 'r')
        list2 = []
        for row in f2:
            list2.append(row)
        #f.write('aaa')
        if sum(1 for line in open(file_path)) >= 5 :
            f3 = open(file_path, 'w')
            f4 = open(file_path, 'a')

            for row in list2[-6:] :
                f3.write(row)
            
            f4.write(time + "," + lux + '\n')  
          
        return "suceeded to write" 
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()

@app.route('/lux', methods = ['Get'])
def get_lux():
    try: #描画するデータを送信
        f = open(file_path, 'r')
        list = []
        for row in f:
            list.append(row)
            #lux = row
        lux = ','.join(list[-7:])
        return  lux
    except Exception as e:
            print(e)
            return e
    finally:
            f.close()

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = my_port)
        