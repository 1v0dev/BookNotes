<ul>
    % for note in notes:
    <li>
        <blockquote class="blockquote">
            <p class="mb-0">{{note['text']}}</p>
            <footer class="blockquote-footer text-right">{{note['location']}}</footer>
        </blockquote>
    </li>
    % end
</ul>



