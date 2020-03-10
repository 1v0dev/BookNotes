% rebase('base.tpl', page = 'List')

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
        <div class="tab-content" id="notes-list">
        </div>
    </div>
</div>

<script>
    $(document).ready(function(){
        $('.category-link').on('click',function(){
            var dataURL = $(this).attr('data-href');
            $('#notes-list').load(dataURL);
        });
        $('.category-link').first().click()
    });
</script>



