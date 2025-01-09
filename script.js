document.addEventListener('DOMContentLoaded', () => {
  const lessonsContainer = document.getElementById('lessons-container');
  const lessons = 24;

  for (let i = 1; i <= lessons; i++) {
    const card = document.createElement('div');
    card.className = 'lesson-card p-6 shadow-lg text-white';

    card.innerHTML = `
      <h3 class="text-2xl font-bold mb-4">Lesson ${i}</h3>
      <ul>
        <li><a href="#" target="_blank" class="text-blue-400 hover:underline">Google Colab</a></li>
        <li><a href="#" target="_blank" class="text-blue-400 hover:underline">GitHub Repo</a></li>
        <li><a href="#" target="_blank" class="text-blue-400 hover:underline">Template</a></li>
        <li><a href="#" target="_blank" class="text-blue-400 hover:underline">Afterclass Resources</a></li>
      </ul>
    `;

    lessonsContainer.appendChild(card);
  }

  // Toggle Theme
  const toggleTheme = () => {
    const theme = document.documentElement.getAttribute('data-theme');
    document.documentElement.setAttribute('data-theme', theme === 'dark' ? 'light' : 'dark');
  };

  document.getElementById('toggle-theme').addEventListener('click', toggleTheme);
  document.getElementById('toggle-theme-mobile').addEventListener('click', toggleTheme);

  // Mobile Navbar Toggle
  document.getElementById('menu-toggle').addEventListener('click', () => {
    document.getElementById('mobile-nav').classList.toggle('hidden');
  });
});
