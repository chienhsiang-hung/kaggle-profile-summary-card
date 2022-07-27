from http.server import BaseHTTPRequestHandler
from crawler import kaggle_crawler

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    user = path.split('?')[1]
    userAvatarUrl, displayName, country, city, occupation, organization, performanceTier, performanceTierCategory, userJoinDate, userAchieveUrl = kaggle_crawler(user)
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    html = '''

<!DOCTYPE html>
<html style="max-width:540px; max-height:242.78px">
<head>
    <meta property="og:url" content="https://chienhsiang-hung.github.io/"/>
    <meta name="author" content="Hung, Chien-Hsiang"/>
    
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.9.0/css/all.css">
</head>
<body>

<div class="card mb-3" style="max-width:540px; cursor:pointer;" onclick="nav_to_kaggle()">
  <div class="card-header">
    <img src="https://www.kaggle.com/static/images/site-logo.svg" width="82" >
  </div>
  <div class="row g-0">
    <div class="col-md-4">
      <img src="'''+userAvatarUrl+'''" class="img-fluid rounded-start" alt="...">
    </div>
    <div class="col-md-5">
      <div class="card-body">
        <h5 class="card-title">'''+displayName+'''</h5>
        <p class="card-text">'''+occupation+''' at '''+organization+'''</p>
        <p class="card-text">'''+city+''', '''+country+'''</p>
        <p class="card-text"><small class="text-muted">Joined at '''+userJoinDate+'''</small></p>
      </div>
    </div>
    <div class="col-md-3" style="text-align: center;">
        <img src="'''+userAchieveUrl+'''" class="img-fluid rounded-start" alt="...">
        <h6 style="color:#95628f;">'''+performanceTierCategory+''' '''+performanceTier+'''</h6>
      </div>
  </div>
</div>

<script>
    function nav_to_kaggle() {
        window.open('https://www.kaggle.com/chienhsianghung', '_blank').focus();
    }
</script>
</body>
</html>

    '''
    self.wfile.write(html.encode('utf-8'))
    return {
      "statusCode": 200, 
      "headers": {'content-type': 'text/html'},
      "body": 'hello word'
    }