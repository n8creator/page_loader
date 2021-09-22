from bs4 import BeautifulSoup

#  Фикстура из файла tests/fixtures/expected/site-com-blog-about.html
input = """
<!DOCTYPE html>
<html lang="ru">
 <head>
  <meta charset="utf-8"/>
  <title>
   Блог Тото
  </title>
  <link href="https://cdn2.site.com/blog/assets/style.css" media="all" rel="stylesheet"/>
  <link href="site-com-blog-about_files/site-com-blog-about-assets-styles.css" media="all" rel="stylesheet">
   <script src="https://getbootstrap.com/docs/4.5">
   </script>
   <link href="site-com-blog-about_files/site-com-blog-about.html" rel="canonical"/>
  </link>
 </head>
 <body>
  <img alt="Моя фотография" src="site-com-blog-about_files/site-com-photos-me.jpg"/>
  <p>
   Перейти ко всем записям в
   <a href="/blog">
    блоге
   </a>
  </p>
  <script src="site-com-blog-about_files/site-com-assets-scripts.js">
  </script>
 </body>
</html>
"""


soup = BeautifulSoup(input, "html.parser")
print(soup.prettify())
