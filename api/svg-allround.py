from http.server import BaseHTTPRequestHandler

import util
from util.crawler import summary_crawler
from util.datauri import img_to_datauri


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    path = self.path
    user = path.split('?')[1]
    (
        userAvatarUrl, displayName,
        competitionsAchieveUrl, competitionscolorAchieve,
        scriptsSummaryAchieveUrl, scriptscolorAchieve,
        discussionsSummaryAchieveUrl, discussionscolorAchieve,
        datasetsAchieveUrl, datasetscolorAchieve,
        followers, following, userJoinDate
    ) = summary_crawler(user)    

    self.send_response(200)
    self.send_header('Content-type', 'image/svg+xml')
    self.end_headers()
    
    # handle no user error
    if not displayName:
      html = '''
        
        <svg width="540" height="155" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
        <!-- Created with SVG-edit - https://github.com/SVG-Edit/svgedit-->
        <g class="layer">
          <title>Layer 1</title>
          <rect fill="#ffffff" height="140" id="svg_4" rx="10" ry="10" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" width="531" x="4" y="5"/>
          <rect fill="#e5e5e5" height="57" id="svg_6" rx="10" ry="10" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" transform="matrix(1 0 0 1 0 0)" width="529" x="5" y="7"/>
          <image height="41.46" id="svg_2" width="123" x="13" xlink:href="'''+util.kaggle_svg_dataurl+'''" y="15"/>
          <line fill="none" id="svg_7" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" transform="matrix(1 0 0 1 0 0)" x1="7" x2="534" y1="65" y2="66"/>
          <text fill="#000000" font-family="Sans-serif" font-size="17" id="svg_14" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="21" xml:space="preserve" y="95">no user found, please enter the right username</text>
          <text fill="#000000" font-family="Sans-serif" font-size="17" id="svg_1" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="21" xml:space="preserve" y="125">contact the author</text>
          <text fill="#000000" font-family="Sans-serif" font-size="17" font-weight="bold" id="svg_3" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" x="164" xml:space="preserve" y="125">chienhsiang-hung.github.io</text>
        </g>
        </svg>
      '''

    else:
      userAvatarUrl = img_to_datauri(userAvatarUrl)
      competitionsAchieveUrl = img_to_datauri(competitionsAchieveUrl)
      scriptsSummaryAchieveUrl = img_to_datauri(scriptsSummaryAchieveUrl)
      discussionsSummaryAchieveUrl = img_to_datauri(discussionsSummaryAchieveUrl)
      datasetsAchieveUrl = img_to_datauri(datasetsAchieveUrl)

      html = '''
          <svg width="540" height="250" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
          <!-- Created with SVG-edit - https://github.com/SVG-Edit/svgedit-->
          <g class="layer">
            <title>Layer 1</title>
            <rect fill="#ffffff" height="239" id="svg_4" rx="10" ry="10" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" transform="matrix(1 0 0 1 0 0)" width="531" x="4" y="5"/>
            <rect fill="#e5e5e5" height="57" id="svg_6" rx="10" ry="10" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" width="529" x="5" y="7"/>
            <image height="41.46" id="svg_2" width="123" x="13" xlink:href="'''+util.kaggle_svg_dataurl+'''" y="15"/>
            <line fill="none" id="svg_7" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" transform="matrix(1 0 0 1 0 0)" x1="7" x2="534" y1="65" y2="66"/>
            <image height="171" id="svg_10" transform="matrix(1 0 0 1 0 0)" width="171" x="6" xlink:href="data:image/png; base64,'''+userAvatarUrl+'''" y="71"/>
            <text fill="#000000" font-family="Sans-serif" font-size="19" font-weight="bold" id="svg_12" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="189.67" xml:space="preserve" y="98">'''+displayName+'''</text>
            <text fill="#999999" font-family="Sans-serif" font-size="14" id="svg_1" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" x="392" xml:space="preserve" y="28">Joined at '''+userJoinDate+'''</text>
            <image height="46" id="svg_3" width="46" x="210" xlink:href="data:image/png; base64,'''+competitionsAchieveUrl+'''" y="122"/>
            <image height="46" id="svg_8" width="46" x="295" xlink:href="data:image/png; base64,'''+scriptsSummaryAchieveUrl+'''" y="122"/>
            <image height="46" id="svg_9" width="46" x="380" xlink:href="data:image/png; base64,'''+discussionsSummaryAchieveUrl+'''" y="122"/>
            <image height="46" id="svg_11" width="46" x="465" xlink:href="data:image/png; base64,'''+datasetsAchieveUrl+'''" y="122"/>
            <text fill="'''+competitionscolorAchieve+'''" font-family="Sans-serif" font-size="12" font-weight="bold" id="svg_5" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="middle" transform="matrix(1 0 0 1 0 0)" x="235" xml:space="preserve" y="197">Competitions</text>
            <text fill="'''+scriptscolorAchieve+'''" font-family="Sans-serif" font-size="12" font-weight="bold" id="svg_13" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="middle" transform="matrix(1 0 0 1 0 0)" x="320.84" xml:space="preserve" y="197">Datasets</text>
            <text fill="'''+discussionscolorAchieve+'''" font-family="Sans-serif" font-size="12" font-weight="bold" id="svg_14" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="middle" transform="matrix(1 0 0 1 0 0)" x="399.84" xml:space="preserve" y="197">Notebooks</text>
            <text fill="'''+datasetscolorAchieve+'''" font-family="Sans-serif" font-size="12" font-weight="bold" id="svg_15" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="middle" transform="matrix(1 0 0 1 0 0)" x="486.84" xml:space="preserve" y="197">Discussion</text>
            <text fill="#333333" font-family="Sans-serif" font-size="15" id="svg_16" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" x="300" xml:space="preserve" y="230">Followers '''+str(followers)+'''</text>
            <text fill="#333333" font-family="Sans-serif" font-size="15" id="svg_17" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" x="415" xml:space="preserve" y="230">Following '''+str(following)+'''</text>
          </g>
          </svg>
      '''

    self.wfile.write(html.encode('utf-8'))
    return