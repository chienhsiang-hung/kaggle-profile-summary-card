import imgkit
# from html2image import Html2Image
# from weasyprint import HTML


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
      <img src="https://storage.googleapis.com/kaggle-avatars/images/6294032-kg.png" class="img-fluid rounded-start" alt="...">
    </div>
    <div class="col-md-5">
      <div class="card-body">
        <h5 class="card-title">Chien-Hsiang Hung</h5>
        <p class="card-text">IT Manager, DDI at WAM</p>
        <p class="card-text">Taipei, Taiwan</p>
        <p class="card-text"><small class="text-muted">Joined at 2020-12-02</small></p>
      </div>
    </div>
    <div class="col-md-3" style="text-align: center;">
        <img src="https://www.kaggle.com/static/images/tiers/expert@192.png" class="img-fluid rounded-start" alt="...">
        <h6 style="color:#95628f;">Competitions Expert</h6>
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

if __name__ == '__main__':
    
    # hti = Html2Image()
    # hti.screenshot(html_str=html, save_as='html_to_image_test_html2img.png', size=(2000, 1000))
    
    # html = HTML(string=html)
    # html.write_png('weasyprint.png')

    imgkit.from_string(html, "test/html_to_image/html_to_img_test_imgkit.svg")