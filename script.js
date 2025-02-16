document.addEventListener('DOMContentLoaded', () => {
  const lessonsContainer = document.getElementById('lessons-container');

  // Array of lesson details
  const lessons = [
    {
      title: "Lesson 1: AI-Powered Real-Time Food Calorie Detector (Colab)",
      colab: "https://colab.research.google.com/drive/1REeBprZQTnfYETnE-CnaiTx188hANqa-?usp=sharing",
      github: "https://github.com/repo/lesson1",
      template: "https://template.com/lesson1",
      resources: "https://resources.com/lesson1",
    },
    {
      title: "Lesson 2: AI-Powered Movie Recommendation System (Colab)",
      colab: "https://colab.research.google.com/drive/1aA7gdc_d91Bt09RTYv5iSHIFZz7KyQRS?usp=sharing",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },
    {
      title: "Lesson 3: AI-Powered Text Extractor and Summarizer (Colab)",
      colab: "https://colab.research.google.com/drive/1ITYTfkCJo14_RYxLrxPnx1KYC4CKTl9Y?usp=sharing",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },
    {
      title: "Lesson 4: AI-Powered Language Tutor (Colab)",
      colab: "https://colab.research.google.com/drive/1-jY_UuELsohwbVz2lZtRje1enuOE0zXM?usp=sharing",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },
    {
      title: "Lesson 5: AI-Powered Image Generator (Colab)",
      colab: "https://colab.research.google.com/drive/1pg7h4m87JIvjW_sJK9kCOSBdmKwFF_nL?usp=sharing",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },
    {
      title: "Lesson 6: AI-Powered Art Style Transfer (Colab)",
      colab: "https://colab.research.google.com/drive/1dicRbQzkgUKtujyOKz0zFXca0twqW038?usp=sharing",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },

    {
      title: "Lesson 7: Cat-Dog Breed Classifier (Colab)",
      colab: "https://colab.research.google.com/drive/1N80u0fsRWzP_Z-jLm8Sh00BYlYdZP91y?usp=sharing",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },

    {
      title: "Lesson 8: Real vs. AI-Generated Face Classifier (Colab)",
      colab: "https://colab.research.google.com/drive/1Gr1BwdCklKtOhlUGOy8-8mGDO2v2M_u7?usp=sharing",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },

    {
      title: "Lesson 9: Face Scan Pro (Colab)",
      colab: "https://colab.research.google.com/drive/1E0jFPxcFkZ4sStEymvYsfLhprV2ZKl9l?usp=sharing",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },

    {
      title: "Lesson 10: Sentiment Analyzer Part-1 (Colab)",
      colab: "https://colab.research.google.com/drive/1BO6f3Ni7XqHs1P7utGAruZYi2BmASdAR?usp=sharing",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },

    {
      title: "Lesson 11: Sentiment Analyzer Part-2 (Colab)",
      colab: "https://colab.research.google.com/drive/1BO6f3Ni7XqHs1P7utGAruZYi2BmASdAR?usp=sharing",
      github: "https://github.com/repo/lesson2",
      template: "https://template.com/lesson2",
      resources: "https://resources.com/lesson2",
    },

    {
      title: "Lesson 12: Show and Tell ",
      colab: "",
      github: "",
      template: "",
      resources: "",
    },

    {
      title: "Lesson 13: Sign Language Predictor (Vs - Git)",
      colab: "",
      github: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson13/Sign_language_interpreter.py",
      template: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson13/sign_language_template.py",
      resources: "https://github.com/Scodingcurriculum/Ai/tree/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson13",
    },

    {
      title: "Lesson 14: Train and Predict Part - 1 (Vs - Git)",
      colab: "",
      github: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson14-15/train_and_predict.py",
      template: "https://template.com/lesson2",
      resources: "https://github.com/Scodingcurriculum/Ai/tree/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson14-15",
    },

    {
      title: "Lesson 15: Train and Predict Part - 2 (Vs - Git)",
      colab: "",
      github: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson14-15/train_and_predict.py",
      template: "https://template.com/lesson2",
      resources: "https://github.com/Scodingcurriculum/Ai/tree/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson14-15",
    },

    {
      title: "Lesson 16: Heart Attack Prediction (Vs - Git)",
      colab: "",
      github: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson16/heartattack_predictor.py.py",
      template: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson16/heartattackpredictor_template.py",
      resources: "https://github.com/Scodingcurriculum/Ai/tree/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson16",
    },

    {
      title: "Lesson 17: AI Color Quest (Vs - Git)",
      colab: "",
      github: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson17/detectcolors.py",
      template: "https://template.com/lesson2",
      resources: "https://github.com/Scodingcurriculum/Ai/tree/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson17",
    },

    {
      title: "Lesson 18: AI Navigator Part - 1 (Vs - Git)",
      colab: "",
      github: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson18-19/Reinforcement.py",
      template: "https://template.com/lesson2",
      resources: "https://github.com/Scodingcurriculum/Ai/tree/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson18-19",
    },

    {
      title: "Lesson 19: AI Navigator Part - 2 (Vs - Git)",
      colab: "",
      github: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson18-19/Reinforcement.py",
      template: "https://template.com/lesson2",
      resources: "https://github.com/Scodingcurriculum/Ai/tree/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson18-19",
    },

    {
      title: "Lesson 20: AI Sentiment Driven Journal Part-1 (Vs - Git)",
      colab: "",
      github: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson20-21/SentimentAnalyzer.py",
      template: "https://template.com/lesson2",
      resources: "https://github.com/Scodingcurriculum/Ai/tree/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson20-21",
    },

    {
      title: "Lesson 21: AI Sentiment Driven Journal Part-2 (Vs - Git)",
      colab: "",
      github: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson20-21/SentimentAnalyzer.py",
      template: "https://template.com/lesson2",
      resources: "https://github.com/Scodingcurriculum/Ai/tree/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson20-21",
    },

    {
      title: "Lesson 22: Face Lock System Part - 1 (Vs - Git)",
      colab: "",
      github: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson22-23/Security_system.py",
      template: "https://template.com/lesson2",
      resources: "https://github.com/Scodingcurriculum/Ai/tree/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson22-23",
    },

    {
      title: "Lesson 23: Face Lock System Part-2 (Vs - Git)",
      colab: "",
      github: "https://github.com/Scodingcurriculum/Ai/blob/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson22-23/Security_system.py",
      template: "https://template.com/lesson2",
      resources: "https://github.com/Scodingcurriculum/Ai/tree/308de22908cd2bf8330e7a4318766afc9f28b7ab/Vs%20Codes/Lesson22-23",
    },

    {
      title: "Lesson 24: Show and Tell ",
      colab: "",
      github: "",
      template: "",
      resources: "",
    }


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
