from http.server import BaseHTTPRequestHandler
from util.crawler import kaggle_crawler

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    user = path.split('?')[1]
    userAvatarUrl, displayName, country, city, occupation, organization, performanceTier, performanceTierCategory, userJoinDate, userAchieveUrl, colorAchieve = kaggle_crawler(user)      

    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    
    # handle no user error
    if not colorAchieve:
      html = '''
        <svg width="540" height="155" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <!-- Created with SVG-edit - https://github.com/SVG-Edit/svgedit-->
        <g class="layer">
          <title>Layer 1</title>
          <rect fill="#ffffff" height="144" id="svg_4" rx="10" ry="10" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" width="531" x="4" y="4"/>
          <rect fill="#e5e5e5" height="57" id="svg_6" rx="10" ry="10" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" width="529" x="5" y="7"/>
          <image height="41.46" id="svg_2" width="123" x="13" xlink:href="https://www.kaggle.com/static/images/site-logo.svg" y="15"/>
          <line fill="none" id="svg_7" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" transform="matrix(1 0 0 1 0 0)" x1="7" x2="534" y1="65" y2="66"/>
          <text fill="#000000" font-family="Sans-serif" font-size="17" id="svg_14" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="21" xml:space="preserve" y="95">no user found, please enter the right username</text>
          <text fill="#000000" font-family="Sans-serif" font-size="17" id="svg_1" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="21" xml:space="preserve" y="125">contact the author
          <a fill="#0d6efd" id="svg_3">@Hsiang</a></text>
        </g>
        </svg>
      '''

    else:
      html = '''

<!DOCTYPE html>
<html style="max-width:540px; max-height:242.78px">
<head>
    <meta property="og:url" content="https://chienhsiang-hung.github.io/kaggle-profile-summary-card/"/>
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
        <h6 style="color:'''+colorAchieve+''';">'''+performanceTierCategory+''' '''+performanceTier+'''</h6>
      </div>
  </div>
</div>

<script>
    function nav_to_kaggle() {
        window.open('https://www.kaggle.com/'''+user+'''', '_blank').focus();
    }
</script>
</body>
</html>


<svg width="540" height="250" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <!-- Created with SVG-edit - https://github.com/SVG-Edit/svgedit-->
 <g class="layer">
  <title>Layer 1</title>
  <rect fill="#ffffff" height="239" id="svg_4" rx="10" ry="10" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" transform="matrix(1 0 0 1 0 0)" width="531" x="4" y="5"/>
  <rect fill="#e5e5e5" height="57" id="svg_6" rx="10" ry="10" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" width="529" x="5" y="7"/>
  <image height="104" id="svg_3" transform="matrix(1 0 0 1 0 0)" width="104" x="422" xlink:href="https://www.kaggle.com/static/images/tiers/expert@192.png" y="78"/>
  <image height="41.46" id="svg_2" width="123" x="13" xlink:href="https://www.kaggle.com/static/images/site-logo.svg" y="15"/>
  <line fill="none" id="svg_7" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" transform="matrix(1 0 0 1 0 0)" x1="7" x2="534" y1="65" y2="66"/>
  <image height="171" id="svg_10" transform="matrix(1 0 0 1 0 0)" width="171" x="6" xlink:href="https://storage.googleapis.com/kaggle-avatars/images/6294032-kg.png" y="71"/>
  <text fill="#000000" font-family="Sans-serif" font-size="19" font-weight="bold" id="svg_12" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="189.67" xml:space="preserve" y="106">Chien-Hsiang, Hung</text>
  <text fill="#333333" font-family="Sans-serif" font-size="17" id="svg_14" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="189" xml:space="preserve" y="137">IT manger, DDI at WAM</text>
  <text fill="#333333" font-family="Sans-serif" font-size="17" id="svg_15" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" x="189.67" xml:space="preserve" y="178">Taipei, Taiwan</text>
  <text fill="#999999" font-family="Sans-serif" font-size="14" id="svg_1" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="189" xml:space="preserve" y="217">Joined at 2022-12-02</text>
  <text fill="#95628f" font-family="Sans-serif" font-size="16" font-weight="bold" id="svg_5" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="middle" transform="matrix(1 0 0 1 0 0)" x="474" xml:space="preserve" y="204">Competitions</text>
  <text fill="#95628f" font-family="Sans-serif" font-size="16" font-weight="bold" id="svg_8" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="middle" x="472.95" xml:space="preserve" y="225.5">Expert</text>
 </g>
</svg>

    '''

    self.wfile.write(html.encode('utf-8'))

    return