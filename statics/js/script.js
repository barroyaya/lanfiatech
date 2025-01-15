document.addEventListener('DOMContentLoaded', function() {
    const buttons = document.querySelectorAll('.filter');
    const items = document.querySelectorAll('.media-item');

    buttons.forEach(btn => {
        btn.addEventListener('click', () => {
            const filter = btn.getAttribute('data-filter');
            items.forEach(item => {
                if(filter === 'all') {
                    item.style.display = 'block';
                } else {
                    item.style.display = item.getAttribute('data-type') === filter ? 'block' : 'none';
                }
            });
        });
    });
});
