<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css"
          integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
    <title>Book Notes</title>
</head>

<body>
<div class="container" style="height: 1872px; width: 1404px; margin-top: 500px; margin-left: 152px">
    <blockquote class="blockquote text-justify" style="width: 1100px; font-size: 220%">
        <h1>{{note['category']['title']}}</h1>
        <br />
        <p class="mb-0">{{note['text']}}</p>
        <footer class="blockquote-footer text-right">{{note['location']}}</footer>
    </blockquote>
</div>
</body>
</html>