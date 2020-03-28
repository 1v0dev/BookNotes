% rebase('base.tpl', page = 'Upload')

<form action="/upload/boox" method="post" enctype="multipart/form-data">
    <div class="form-group">
        <label for="fileUpload">Choose Boox notes file</label>
        <input type="file" class="form-control-file" id="fileUpload" name="boox_file">
    </div>
    <button type="submit" class="btn btn-primary">Upload</button>
</form>
<br />
<a href="/export/png">Export to PNG</a>
<p>{{message if message else ''}}</p>