document.addEventListener('DOMContentLoaded', function () {
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('content');
    const sidebarCollapse = document.getElementById('sidebarCollapse');
    const themeToggle = document.getElementById('themeToggle');
    const body = document.body;

    // Sidebar Toggle
    sidebarCollapse.addEventListener('click', function () {
        sidebar.classList.toggle('active');
        content.classList.toggle('active');
    });

    // Mobile: Auto-close sidebar when clicking outside on small screens
    document.addEventListener('click', function (e) {
        if (window.innerWidth <= 768) {
            if (!sidebar.contains(e.target) && !sidebarCollapse.contains(e.target) && sidebar.classList.contains('active')) {
                sidebar.classList.remove('active');
            }
        }
    });

    // Theme Toggle
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme) {
        body.setAttribute('data-theme', currentTheme);
        updateThemeIcon(currentTheme);
    }

    if (themeToggle) {
        themeToggle.addEventListener('click', function () {
            let theme = 'light';
            if (body.getAttribute('data-theme') !== 'dark') {
                body.setAttribute('data-theme', 'dark');
                theme = 'dark';
            } else {
                body.removeAttribute('data-theme');
            }
            localStorage.setItem('theme', theme);
            updateThemeIcon(theme);
        });
    }

    function updateThemeIcon(theme) {
        const icon = themeToggle.querySelector('i');
        if (theme === 'dark') {
            icon.classList.remove('fa-moon');
            icon.classList.add('fa-sun');
        } else {
            icon.classList.remove('fa-sun');
            icon.classList.add('fa-moon');
        }
    }

    // Chart.js Initialization (Dummy Data)
    if (document.getElementById('marketChart')) {
        const ctx = document.getElementById('marketChart').getContext('2d');
        const marketChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [{
                    label: 'Website Visits',
                    data: [120, 190, 300, 500, 200, 350],
                    borderColor: '#4e73df',
                    backgroundColor: 'rgba(78, 115, 223, 0.1)',
                    borderWidth: 2,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    y: { beginAtZero: true }
                }
            }
        });
    }

    if (document.getElementById('sourcesChart')) {
        const ctx2 = document.getElementById('sourcesChart').getContext('2d');
        const sourcesChart = new Chart(ctx2, {
            type: 'doughnut',
            data: {
                labels: ['Organic', 'Direct', 'Referral', 'Social'],
                datasets: [{
                    data: [55, 30, 15, 10],
                    backgroundColor: ['#4e73df', '#1cc88a', '#36b9cc', '#f6c23e'],
                    hoverBackgroundColor: ['#2e59d9', '#17a673', '#2c9faf', '#dda20a'],
                    hoverBorderColor: "rgba(234, 236, 244, 1)",
                }]
            },
            options: {
                maintainAspectRatio: false,
                plugins: {
                    legend: { position: 'bottom' }
                }
            }
        });
    }
});
