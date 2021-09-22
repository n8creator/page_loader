from bs4 import BeautifulSoup


data = """
<!DOCTYPE html>
<html lang="ru">

<head>
    <meta charset="utf-8">
    <title>Профессии на Хекслете: изучайте программирование с нуля</title>
    <link href="ru-hexlet-io-favicon.ico" rel="shortcut icon" type="image/x-icon">
    <link href="ru-hexlet-io-professions_files/ru-hexlet-io-assets-application.css" media="all" rel="stylesheet" />
    <link href="ru-hexlet-io-professions_files/ru-hexlet-io-professions.html" rel="canonical">
    <link href="https://en.hexlet.io/professions" hreflang="en" rel="alternate">
</head>

<body>
    <!-- Google Tag Manager (noscript) -->
    <noscript>
        <iframe height="0" src="https://www.googletagmanager.com/ns.html?id=GTM-WK88TH"
            style="display:none;visibility:hidden" width="0">
        </iframe>
    </noscript>
    <!-- End Google Tag Manager (noscript) -->
    <nav class="navbar navbar-expand-lg navbar-light bg-white hexlet-navbar border-bottom">
        <div class="collapse navbar-collapse" id="navbarResponsive">
            <ul class="navbar-nav mr-auto">
                <li class="nav-item">
                    <a class="nav-link hexlet-navbar-link px-3 active" href="/professions">
                        <div class="my-2">
                            Профессии
                        </div>
                    </a>
                </li>
                <li class="nav-item">
                    <a class="nav-link hexlet-navbar-link px-3" href="/courses">
                        <div class="my-2">
                            Курсы
                        </div>
                    </a>
                </li>
            </ul>
        </div>
    </nav>
    <main class="mb-5">
        <section class="container-xl mt-5">
            <h1 class="display-4 font-weight-normal mb-3">Профессии на Хекслете</h1>
            <p class="lead font-weight-normal">
                Профессии — готовые учебные программы, которые помогут освоить программирование с нуля.
            </p>
        </section>
        <section class="container-xl mt-5 pt-lg-4">
            <div class="row row-cols-1 row-cols-sm-2 row-cols-lg-3">
                <div class="col mb-4">
                    <div class="card shadow-sm x-shadow-fade-in h-100">
                        <div class="card-header">
                            <div class="text-center py-3">
                                <img alt="Профессия Фронтенд-программист" class="lazyload"
                                    src="ru-hexlet-io-professions_files/ru-hexlet-io-assets-professions-frontend.png" width="150" height="150">
                            </div>
                        </div>
                        <div class="card-body d-flex flex-column">
                            <h2 class="h4 font-weight-bold my-4">
                                Фронтенд-программист
                            </h2>
                            <div class="mt-auto d-flex">
                                <div class="d-sm-none d-md-block mt-auto small text-nowrap text-truncate mr-2">
                                    8 месяцев
                                </div>
                                <div class="ml-auto text-nowrap">
                                    <a class="stretched-link x-link-without-decoration text-muted"
                                        href="/professions/frontend" title="Фронтенд-программист">
                                        <span class="mr-2">
                                            Программа обучения
                                        </span>
                                        <span class="fad fa-arrow-right">
                                        </span>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col mb-4">
                    <div class="card shadow-sm x-shadow-fade-in h-100">
                        <div class="card-header">
                            <div class="text-center py-3">
                                <img alt="Профессия Python-программист" class="lazyload"
                                    src="ru-hexlet-io-professions_files/ru-hexlet-io-assets-professions-python.png" width="150" height="150">
                            </div>
                        </div>
                        <div class="card-body d-flex flex-column">
                            <h2 class="h4 font-weight-bold my-4">
                                Python-программист
                            </h2>
                            <div class="mt-auto d-flex">
                                <div class="d-sm-none d-md-block mt-auto small text-nowrap text-truncate mr-2">
                                    8 месяцев
                                </div>
                                <div class="ml-auto text-nowrap">
                                    <a class="stretched-link x-link-without-decoration text-muted"
                                        href="/professions/python" title="Python-программист">
                                        <span class="mr-2">
                                            Программа обучения
                                        </span>
                                        <span class="fad fa-arrow-right">
                                        </span>
                                    </a>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>
    <script src="ru-hexlet-io-professions_files/ru-hexlet-io-assets-application.js"></script>
    <script src="https://js.stripe.com/v3/"></script>

</body>

</html>
"""


soup = BeautifulSoup(data, "lxml")
print(soup.prettify())
