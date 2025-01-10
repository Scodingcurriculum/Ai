document.addEventListener('DOMContentLoaded', () => {
  const lessonsContainer = document.getElementById('lessons-container');

  // Array of lesson details
  const lessons = [
    {
      title: "Lesson 1: AI-Powered Real-Time Food Calorie Detector",
      colab: "https://colab.research.google.com/drive/1REeBprZQTnfYETnE-CnaiTx188hANqa-?usp=sharing",
      github: "https://github.com/repo/lesson1",
      template: "https://template.com/lesson1",
      resources: "https://resources.com/lesson1",
    },
    {
      title: "Lesson 2: AI-Powered Movie Recommendation System",
      colab: "https://colab.research.google.com/drive/1aA7gdc_d91Bt09RTYv5iSHIFZz7KyQRS?usp=sharing",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },
    {
      title: "Lesson 3: AI-Powered Text Extractor and Summarizer",
      colab: "https://colab.research.google.com/drive/1ITYTfkCJo14_RYxLrxPnx1KYC4CKTl9Y?usp=sharing",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },
    {
      title: "Lesson 4: AI-Powered Language Tutor",
      colab: "https://colab.link/lesson2",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },
    {
      title: "Lesson 5: AI-Powered Image Generator",
      colab: "https://colab.link/lesson2",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },
    {
      title: "Lesson 6: AI-Powered Art Style Transfer",
      colab: "https://colab.link/lesson2",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },

    {
      title: "Lesson 7: Cat-Dog Breed Classifier",
      colab: "https://colab.link/lesson2",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },

    {
      title: "Lesson 8: Real vs. AI-Generated Face Classifier",
      colab: "https://colab.link/lesson2",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },
    // Add more lessons here
  ];

  // Dynamically generate lesson cards
  lessons.forEach((lesson) => {
    const card = document.createElement('div');
    card.className = 'lesson-card p-6 shadow-lg text-white';

    card.innerHTML = `
      <h3 class="text-2xl font-bold mb-4">${lesson.title}</h3>
      <ul>
        <li><a href="${lesson.colab}" target="_blank" class="text-blue-400 hover:underline">Google Colab</a></li>
        <li><a href="${lesson.github}" target="_blank" class="text-blue-400 hover:underline">GitHub Repo</a></li>
        <li><a href="${lesson.template}" target="_blank" class="text-blue-400 hover:underline">Template</a></li>
        <li><a href="${lesson.resources}" target="_blank" class="text-blue-400 hover:underline">Afterclass Resources</a></li>
      </ul>
    `;

    lessonsContainer.appendChild(card);
  });

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
