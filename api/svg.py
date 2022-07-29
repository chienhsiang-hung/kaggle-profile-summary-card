from http.server import BaseHTTPRequestHandler
from util.crawler import kaggle_crawler

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    user = path.split('?')[1]
    userAvatarUrl, displayName, country, city, occupation, organization, performanceTier, performanceTierCategory, userJoinDate, userAchieveUrl, colorAchieve = kaggle_crawler(user)      

    self.send_response(200)
    self.send_header('Content-type', 'image/svg+xml')
    self.end_headers()
    
    # handle no user error
    if not colorAchieve:
      html = '''
        <svg width="540" height="250" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <!-- Created with SVG-edit - https://github.com/SVG-Edit/svgedit-->
        <g class="layer">
          <title>Layer 1</title>
          <rect fill="#ffffff" height="239" id="svg_4" rx="10" ry="10" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" transform="matrix(1 0 0 1 0 0)" width="531" x="4" y="5"/>
          <rect fill="#e5e5e5" height="57" id="svg_6" rx="10" ry="10" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" width="529" x="5" y="7"/>
          <image height="41.46" id="svg_2" width="123" x="13" xlink:href="https://www.kaggle.com/static/images/site-logo.svg" y="15"/>
          <line fill="none" id="svg_7" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" transform="matrix(1 0 0 1 0 0)" x1="7" x2="534" y1="65" y2="66"/>
          <text fill="#000000" font-family="Sans-serif" font-size="17" id="svg_14" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="21" xml:space="preserve" y="95">no user found, please enter the right username</text>
          <text fill="#000000" font-family="Sans-serif" font-size="17" id="svg_1" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" style="cursor: move;" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="21" xml:space="preserve" y="125">contact the author</text>
          <text fill="#000000" font-family="Sans-serif" font-size="17" font-weight="bold" id="svg_3" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" x="164" xml:space="preserve" y="125">chienhsiang-hung.github.io</text>
        </g>
        </svg>
      '''

    else:
      html = '''
        <svg width="540" height="250" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <!-- Created with SVG-edit - https://github.com/SVG-Edit/svgedit-->
        <g class="layer">
          <title>Layer 1</title>
          <rect fill="#ffffff" height="239" id="svg_4" rx="10" ry="10" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" transform="matrix(1 0 0 1 0 0)" width="531" x="4" y="5"/>
          <rect fill="#e5e5e5" height="57" id="svg_6" rx="10" ry="10" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" width="529" x="5" y="7"/>
          <image height="104" id="svg_3" transform="matrix(1 0 0 1 0 0)" width="104" x="422" xlink:href="'''+userAchieveUrl+'''" y="78"/>
          <image height="41.46" id="svg_2" width="123" x="13" xlink:href="https://www.kaggle.com/static/images/site-logo.svg" y="15"/>
          <line fill="none" id="svg_7" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" transform="matrix(1 0 0 1 0 0)" x1="7" x2="534" y1="65" y2="66"/>
          <image height="171" id="svg_10" transform="matrix(1 0 0 1 0 0)" width="171" x="6" xlink:href="'''+userAvatarUrl+'''" y="71"/>
          <text fill="#000000" font-family="Sans-serif" font-size="19" font-weight="bold" id="svg_12" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="189.67" xml:space="preserve" y="106">'''+displayName+'''</text>
          <text fill="#333333" font-family="Sans-serif" font-size="17" id="svg_14" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="189" xml:space="preserve" y="137">'''+occupation+''' at '''+organization+'''</text>
          <text fill="#333333" font-family="Sans-serif" font-size="17" id="svg_15" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" x="189.67" xml:space="preserve" y="178">'''+city+''', '''+country+'''</text>
          <text fill="#999999" font-family="Sans-serif" font-size="14" id="svg_1" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="189" xml:space="preserve" y="217">Joined at '''+userJoinDate+'''</text>
          <text fill="'''+colorAchieve+'''" font-family="Sans-serif" font-size="16" font-weight="bold" id="svg_5" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="middle" transform="matrix(1 0 0 1 0 0)" x="474" xml:space="preserve" y="204">'''+performanceTierCategory+'''</text>
          <text fill="'''+colorAchieve+'''" font-family="Sans-serif" font-size="16" font-weight="bold" id="svg_8" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="middle" x="472.95" xml:space="preserve" y="225.5">'''+performanceTier+'''</text>
        </g>
        </svg>
      '''

    self.wfile.write(html.encode('utf-8'))
    return