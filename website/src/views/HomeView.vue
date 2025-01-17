<template>
    <div class="home-container">
      <canvas id="star-canvas"></canvas>
      <div class="content-left">
        <h1 class="title">RocketPass</h1>
      </div>
      <div class="content-right">
        <div class="about-section">
          <h2>About RocketPass</h2>
          <p>RocketPass is your gateway to the stars! We provide exclusive space travel experiences that allow you to explore the cosmos like never before.</p>
        </div>
        <div class="social-media">
          <h2>Follow Us</h2>
          <ul>
            <li><a href="https://www.facebook.com/RocketPass"><i class="fab fa-facebook-f"></i></a></li>
            <li><a href="https://www.twitter.com/RocketPass"><i class="fab fa-twitter"></i></a></li>
            <li><a href="https://www.instagram.com/RocketPass"><i class="fab fa-instagram"></i></a></li>
          </ul>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'HomeView',
    mounted() {
      this.createStarAnimation();
    },
    methods: {
      createStarAnimation() {
        const canvas = document.getElementById('star-canvas');
        const context = canvas.getContext('2d');
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
  
        const stars = [];
        const numStars = 1000;
  
        for (let i = 0; i < numStars; i++) {
          stars.push({
            x: Math.random() * canvas.width,
            y: Math.random() * canvas.height,
            radius: Math.random() * 1.5,
            dx: (Math.random() - 0.5) * 0.5,
            dy: (Math.random() - 0.5) * 0.5
          });
        }
  
        function drawStars() {
          context.clearRect(0, 0, canvas.width, canvas.height);
          context.fillStyle = 'white';
          context.beginPath();
          stars.forEach(star => {
            context.moveTo(star.x, star.y);
            context.arc(star.x, star.y, star.radius, 0, Math.PI * 2, true);
          });
          context.fill();
          updateStars();
        }
  
        function updateStars() {
          stars.forEach(star => {
            star.x += star.dx;
            star.y += star.dy;
  
            if (star.x < 0 || star.x > canvas.width) star.dx *= -1;
            if (star.y < 0 || star.y > canvas.height) star.dy *= -1;
          });
        }
  
        function animate() {
          drawStars();
          requestAnimationFrame(animate);
        }
  
        animate();
      }
    }
  };
  </script>
  
  <style scoped>
  .home-container {
    display: flex;
    margin-top: 2rem;
    border-radius: 5rem;
    width: 100%;
    height: 77vh;
    background: linear-gradient(to right, darkblue, darkviolet);
    color: white;
    position: relative;
  }
  
  #star-canvas {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    z-index: 0;
  }
  
  .content-left {
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
  }
  
  .title {
    font-size: 5rem;
    font-weight: bold;
  }
  
  .content-right {
    flex: 1;
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding: 2rem;
    border-radius: 5rem;
    background-color: rgba(0, 0, 0, 0.5); /* Adding a semi-transparent background for better readability */
    backdrop-filter: blur(1px); /* Adding a blur effect */
    z-index: 1;
 }


  .social-media {
    margin-top: 4rem;
  }

  .about-section h2,
  .social-media h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }
  
  .about-section p,
  .social-media ul {
    font-size: 1.2rem;
    line-height: 1.5;
  }
  
  .social-media ul {
    list-style: none;
    padding: 0;
    display: flex;
    justify-content: center;
    gap: 1rem;
  }
  
  .social-media li {
    font-size: 1.2rem;
  }
  
  .social-media a {
    text-decoration: none;
    color: white;
    padding: 0.5rem;
    border-radius: 0.3rem;
    transition: background-color 0.3s ease;
  }
  
  .social-media a:hover {
    background-color: rgba(255, 255, 255, 0.3);
  }
  
  .social-media i {
    font-size: 2rem;
  }
  </style>
  