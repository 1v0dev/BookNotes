% rebase('base.tpl', page = 'List')

<div class="row pb-3">
    <div class="col-3">
        <h5 class="text-center">
            Category
            <button type="button" class="btn btn-light" data-toggle="modal" data-target="#newCatModal">
                +
            </button>
        </h5>
    </div>
    <div class="col-9">
        <h5 class="text-center">Notes</h5>
    </div>
</div>
<div class="row">
    <div class="col-3">
        <div class="nav flex-column nav-pills" role="tablist" aria-orientation="vertical">
            % for category in categories:
            <a class="nav-link category-link" data-toggle="pill" href="#" role="tab" aria-controls="v-pills-home"
               data-href="/list/{{category['_id']}}" aria-selected="true">{{category['title']}}</a>
            % end
        </div>
    </div>
    <div class="col-9">
        <div class="d-none justify-content-center" id="loadingSpinner">
            <div class="spinner-border text-primary m-5" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>
        <div class="tab-content overflow-auto" id="notesList">
        </div>
    </div>
</div>

<!-- Modal -->
<div class="modal fade" id="newCatModal" tabindex="-1" role="dialog" aria-labelledby="newCatLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title" id="newCatLabel">New Category</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">&times;</span>
                </button>
            </div>
            <form action="/new/category" method="post">
                <div class="modal-body">
                    <div class="form-group">
                        <label for="categoryTitle">Title</label>
                        <input type="text" class="form-control" id="categoryTitle" name="categoryTitle"
                               aria-describedby="emailHelp" required>
                    </div>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    <button type="submit" class="btn btn-primary">Save</button>
                </div>
            </form>
        </div>
    </div>
</div>

<script>
    $(function () {
        $('.category-link').on('click', function () {
            let dataURL = $(this).attr('data-href');
            $('#loadingSpinner').removeClass('d-none').addClass('d-flex');
            $('#notesList').empty().load(dataURL, function () {
                $('#loadingSpinner').removeClass('d-flex').addClass('d-none');
            });
        }).first().trigger("click");
    });
</script>



