<div class="custom-control custom-switch ml-3">
    <input type="checkbox" class="custom-control-input" id="category_random_toggle"
           {{'checked' if category['show_random'] == True else '' }} data-href="/list/{{category['_id']}}/toggle/random">
    <label class="custom-control-label" for="category_random_toggle">Show category in random</label>
</div>

<ul class="mt-3">
    % for note in notes:
    <li>
        <blockquote class="blockquote">
            <p class="mb-0">{{note['text']}}</p>
            <footer class="blockquote-footer text-right">{{note['location']}}</footer>
        </blockquote>
    </li>
    % end
</ul>

<script>
    $(function() {
        $('#category_random_toggle').on('click', function() {
            let dataURL = $(this).attr('data-href');
            let checked = $(this).attr('checked');
            $.post(dataURL, { show_random: !checked});
        })
    });
</script>