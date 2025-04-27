// script.js
// Efeitos sutis de animação e rolagem suave

// Scroll suave para âncoras internas
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function (e) {
    const target = document.querySelector(this.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});

// Animação de fade-in para a seção principal ao carregar
window.addEventListener('DOMContentLoaded', () => {
  const aboutSection = document.querySelector('.about');
  if (aboutSection) {
    aboutSection.style.opacity = 0;
    aboutSection.style.transform = 'translateY(30px)';
    setTimeout(() => {
      aboutSection.style.transition = 'opacity 0.8s, transform 0.8s';
      aboutSection.style.opacity = 1;
      aboutSection.style.transform = 'translateY(0)';
    }, 200);
  }
});
