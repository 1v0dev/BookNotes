% rebase('base.tpl', page = 'List')

<div class="row pb-3">
    <div class="col-3">
        <h5 class="text-center">Category</h5>
    </div>
    <div class="col-9">
        <h5 class="text-center">Notes</h5>
    </div>
</div>
<div class="row">
    <div class="col-3">
        <div class="nav flex-column nav-pills" id="v-pills-tab" role="tablist" aria-orientation="vertical">
            % for category in categories:
                <a class="nav-link category-link" data-toggle="pill" href="#" role="tab" aria-controls="v-pills-home"
                   data-href="/list/{{category['_id']}}" aria-selected="true">{{category['title']}}</a>
            % end
        </div>
    </div>
    <div class="col-9">
        <div class="d-none justify-content-center" id="loading-spinner">
            <div class="spinner-border text-primary m-5" role="status">
                <span class="sr-only">Loading...</span>
            </div>
        </div>
        <div class="tab-content" id="notes-list">
        </div>
    </div>
</div>

<script>
    $(function() {
        $('.category-link').on('click', function() {
            let dataURL = $(this).attr('data-href');
            $('#loading-spinner').removeClass('d-none').addClass('d-flex');
            $('#notes-list').empty().load(dataURL, function () {
                $('#loading-spinner').removeClass('d-flex').addClass('d-none');
            });
        }).first().trigger( "click" );
    });
</script>



