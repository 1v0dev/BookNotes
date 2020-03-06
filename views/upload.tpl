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
        <nav class="navbar navbar-light bg-light">
            <ul class="navbar-nav mr-auto">
                <li><a href="/">Random</a></li>
                <li><a href="/upload">Upload</a></li>
            </ul>
        </nav>

        <div class="container" style="padding-top: 50px">

            <form action="/upload/boox" method="post" enctype="multipart/form-data">
                <div class="form-group">
                    <label for="fileUpload">Choose Boox notes file</label>
                    <input type="file" class="form-control" id="fileUpload" name="boox_file">
                </div>
                <button type="submit" class="btn btn-primary">Upload</button>
            </form>

            <p>{{message if message else ''}}</p>
        </div>
    </body>
</html>