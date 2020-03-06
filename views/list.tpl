% rebase('base.tpl', page = 'List')

<ul>
    % for note in notes:
    <li>
        <blockquote class="blockquote">
            <h4>{{note['book_title']}}</h4>
            <p class="mb-0">{{note['text']}}</p>
            <footer class="blockquote-footer text-right">{{note['location']}}</footer>
        </blockquote>
    </li>
    % end
</ul>