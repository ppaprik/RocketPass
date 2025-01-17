<template>
    <div class="about-container">
      <h1>{{ aboutData.title }}</h1>
      <p>{{ aboutData.description }}</p>
      <p><strong>Founded:</strong> {{ aboutData.foundingDate }}</p>
      <p><strong>Headquarters:</strong> {{ aboutData.headquarters }}</p>
      <p><strong>Vision:</strong> {{ aboutData.vision }}</p>
      <h2>Missions</h2>
      <ul>
        <li v-for="mission in aboutData.missions" :key="mission">{{ mission }}</li>
      </ul>
      <h2>Team</h2>
      <ul>
        <li v-for="member in aboutData.team" :key="member.name">
          <strong>{{ member.name }} ({{ member.role }}):</strong> {{ member.bio }}
        </li>
      </ul>
    </div>
  </template>
  
  <script>
  export default {
    name: 'AboutRocketPass',
    props: {
      aboutData: {
        type: Object,
        required: true
      }
    }
  };
  </script>
  
  <style scoped>
  .about-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    padding: 2rem;
  }
  
  h2 {
    font-size: 2rem;
    margin-bottom: 1rem;
  }
  
  p, li {
    font-size: 1.2rem;
    line-height: 1.5;
  }
  
  ul {
    list-style: none;
    padding: 0;
  }
  </style>
  