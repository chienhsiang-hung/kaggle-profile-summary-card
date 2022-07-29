import requests
import shutil
import base64
import time

print(time.asctime())
url = 'https://storage.googleapis.com/kaggle-avatars/images/6294032-kg.png'
resp = requests.get(url, stream=True)
if resp.status_code == 200:
    # resp.raw.decode_content = True

    svg = '''
<svg width="540" height="250" xmlns="http://www.w3.org/2000/svg" xmlns:svg="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
 <!-- Created with SVG-edit - https://github.com/SVG-Edit/svgedit-->
 <g class="layer">
  <title>Layer 1</title>
  <rect fill="#ffffff" height="239" id="svg_4" rx="10" ry="10" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" transform="matrix(1 0 0 1 0 0)" width="531" x="4" y="5"/>
  <rect fill="#e5e5e5" height="57" id="svg_6" rx="10" ry="10" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" width="529" x="5" y="7"/>
  <image height="104" id="svg_3" transform="matrix(1 0 0 1 0 0)" width="104" x="422" xlink:href="https://www.kaggle.com/static/images/tiers/expert@192.png" y="78"/>
  <image height="41.46" id="svg_2" width="123" x="13" xlink:href="https://www.kaggle.com/static/images/site-logo.svg" y="15"/>
  <line fill="none" id="svg_7" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" transform="matrix(1 0 0 1 0 0)" x1="7" x2="534" y1="65" y2="66"/>
  <image height="171" id="svg_10" transform="matrix(1 0 0 1 0 0)" width="171" x="6" xlink:href="data:img/png; base64,'''+base64.b64encode(resp.content).decode()+'''" y="71"/>
  <text fill="#000000" font-family="Sans-serif" font-size="19" font-weight="bold" id="svg_12" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="189.67" xml:space="preserve" y="106">Chien-Hsiang, Hung</text>
  <text fill="#333333" font-family="Sans-serif" font-size="17" id="svg_14" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="189" xml:space="preserve" y="137">IT manger, DDI at WAM</text>
  <text fill="#333333" font-family="Sans-serif" font-size="17" id="svg_15" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" x="189.67" xml:space="preserve" y="178">Taipei, Taiwan</text>
  <text fill="#999999" font-family="Sans-serif" font-size="14" id="svg_1" stroke="#666666" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="start" transform="matrix(1 0 0 1 0 0)" x="189" xml:space="preserve" y="217">Joined at 2022-12-02</text>
  <text fill="#95628f" font-family="Sans-serif" font-size="16" font-weight="bold" id="svg_5" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="middle" transform="matrix(1 0 0 1 0 0)" x="474" xml:space="preserve" y="204">Competitions</text>
  <text fill="#95628f" font-family="Sans-serif" font-size="16" font-weight="bold" id="svg_8" stroke="#000000" stroke-linecap="round" stroke-linejoin="round" stroke-width="0" text-anchor="middle" x="472.95" xml:space="preserve" y="225.5">Expert</text>
 </g>
</svg>
'''
    with open('test\img_to_svg\img_to_svg_test.svg', 'w') as f:
        f.write(svg)
print(time.asctime())


