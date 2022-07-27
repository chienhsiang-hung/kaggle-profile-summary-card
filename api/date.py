from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    user = path.split('?')[1]
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    # self.wfile.write(str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')).encode())
    # self.wfile.write(f'hi {user}'.encode())
    # self.wfile.write("<h1>this is h1 tag</h1>".encode('utf-8'))
    html = '''

<!DOCTYPE html>
<html>
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/all.css">
    <style>

    </style>
</head>
<body>

<div class="card mb-3" style="max-width: 540px;">
  <div class="card-header">
    <img src="https://www.kaggle.com/static/images/site-logo.svg" width="82" >
  </div>
  <div class="row g-0">
    <div class="col-md-4">
      <img src="https://storage.googleapis.com/kaggle-avatars/images/6294032-kg.png" class="img-fluid rounded-start" alt="...">
    </div>
    <div class="col-md-5">
      <div class="card-body">
        <h5 class="card-title">'''+user+'''</h5>
        <p class="card-text">IT Manager, DDI at WAM</p>
        <p class="card-text">Taipei, Taiwan</p>
        <p class="card-text"><small class="text-muted">Joined 2 years ago · last seen in the past day</small></p>
      </div>
    </div>
    <div class="col-md-3" style="text-align: center;">
        <img src="https://www.kaggle.com/static/images/tiers/expert@192.png" class="img-fluid rounded-start" alt="...">
        <h6 style="color:#95628f;">Competitions Expert</h6>
      </div>
  </div>
</div>

</body>
</html>

    '''
    self.wfile.write(html.encode('utf-8'))
    return {
      "statusCode": 200, 
      "headers": {'content-type': 'text/html'},
      "body": 'hello word'
    }