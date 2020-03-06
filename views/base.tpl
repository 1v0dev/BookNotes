<!doctype html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
          integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">

    <title>Book Notes</title>
</head>

<body>
<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
    <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
            <li class="nav-item"><a class="nav-link {{'active' if page == 'Random' else '' }}" href="/">Random</a></li>
            <li class="nav-item"><a class="nav-link {{'active' if page == 'List' else '' }}" href="/list">List</a></li>
            <li class="nav-item"><a class="nav-link {{'active' if page == 'Upload' else '' }}" href="/upload">Upload</a></li>
        </ul>
    </div>
</nav>

<div class="container" style="padding: 50px 5% 0 5%">
    {{!base}}
</div>
</body>
</html>