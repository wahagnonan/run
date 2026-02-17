document.addEventListener('DOMContentLoaded', function () {
    function initCarousel(container, options) {
        const imgs = Array.from(container.querySelectorAll('img'));
        if (!imgs.length) return;

        let current = imgs.findIndex(i => i.classList.contains('active'));
        if (current < 0) current = 0;

        function show(index) {
            index = (index + imgs.length) % imgs.length;
            imgs.forEach((img, i) => {
                img.classList.toggle('active', i === index);
                img.style.opacity = i === index ? '1' : '0';
            });
            current = index;
        }

        const parent = container.parentElement || document;
        const prevBtn = parent.querySelector('.kit-prev') || parent.querySelector('.hero-prev');
        const nextBtn = parent.querySelector('.kit-next') || parent.querySelector('.hero-next');

        prevBtn && prevBtn.addEventListener('click', function () {
            show(current - 1);
            resetTimer();
        });
        nextBtn && nextBtn.addEventListener('click', function () {
            show(current + 1);
            resetTimer();
        });

        let timer = null;
        const interval = options && options.interval ? options.interval : 4000;

        function startTimer() {
            timer = setInterval(function () { show(current + 1); }, interval);
        }
        function stopTimer() { if (timer) { clearInterval(timer); timer = null; } }
        function resetTimer() { stopTimer(); startTimer(); }

        container.addEventListener('mouseenter', stopTimer);
        container.addEventListener('mouseleave', startTimer);

        // Keyboard navigation when focused
        container.setAttribute('tabindex', '0');
        container.addEventListener('keydown', function (e) {
            if (e.key === 'ArrowLeft') { show(current - 1); resetTimer(); }
            if (e.key === 'ArrowRight') { show(current + 1); resetTimer(); }
        });

        // init
        show(current);
        startTimer();
    }

    const hero = document.getElementById('hero-carousel');
    if (hero) initCarousel(hero, { interval: 5000 });

    const kit = document.getElementById('kit-carousel');
    if (kit) initCarousel(kit, { interval: 4500 });
});
