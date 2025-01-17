<template>
  <div class="offset">
    <div class="about-container">
      <!-- Title and Description -->
      <h1>{{ aboutData.title }}</h1>
      <p class="description">{{ aboutData.description }}</p>

      <!-- Info Section -->
      <div class="info-section">
        <div class="info-block">
          <h2>Founded</h2>
          <p>{{ aboutData.foundingDate }}</p>
        </div>
        <div class="info-block">
          <h2>Headquarters</h2>
          <p>{{ aboutData.headquarters }}</p>
        </div>
        <div class="info-block">
          <h2>Vision</h2>
          <p>{{ aboutData.vision }}</p>
        </div>
      </div>

      <!-- Missions Section -->
      <div class="missions-section">
        <h2>Missions</h2>
        <ul>
          <li v-for="mission in aboutData.missions" :key="mission">
            {{ mission }}
          </li>
        </ul>
      </div>

      <!-- Team Section -->
      <div class="team-section">
        <h2>Team</h2>
        <ul>
          <li v-for="member in aboutData.team" :key="member.name">
            <strong>{{ member.name }} ({{ member.role }}):</strong> {{ member.bio }}
          </li>
        </ul>
      </div>

      <!-- Contact Information -->
      <div class="contact-section">
        <h2>Contact Information</h2>
        <p><b>Email:</b> {{ aboutData.contactInfo.email }}</p>
        <p><b>Phone:</b> {{ aboutData.contactInfo.phone }}</p>
        <p><b>Address:</b> {{ aboutData.contactInfo.address }}</p>
      </div>

      <!-- Social Media Links -->
      <div class="social-media-section">
        <h2>Social Media</h2>
        <ul>
          <li v-for="social in aboutData.contactInfo.socialMedia" :key="social.platform">
            <a :href="social.link" target="_blank">
              <span v-if="social.platform == 'facebook'" class="fab fa-facebook-f"></span>
              <span v-else-if="social.platform == 'instagram'" class="fab fa-instagram"></span>
              <span v-else-if="social.platform == 'twitter'" class="fab fa-twitter"></span>
            </a>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'AboutRocketPass',
  props: {
    aboutData: {
      type: Object,
      required: true,
    },
  },
}
</script>

<style scoped>
/* Container Styles */
.offset {
  margin-top: 4rem;
  margin-bottom: 6rem;
}

.about-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
  background: linear-gradient(135deg, rgb(0, 0, 93), rgb(49, 0, 70));
  color: #fff;
  border-radius: 10px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}

/* Titles and Descriptions */
h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
}

b {
  font-weight: bold;
}

.description {
  font-size: 1.2rem;
  margin-bottom: 2rem;
  line-height: 1.6;
  max-width: 800px;
}

/* Info Section */
.info-section {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  margin-bottom: 2rem;
  gap: 1rem;
}

.info-block {
  background-color: rgba(255, 255, 255, 0.1);
  padding: 1rem 2rem;
  border-radius: 10px;
  backdrop-filter: blur(5px);
  flex: 1 1 30%;
  max-width: 30%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* Section Headers */
h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

/* Lists and Items */
ul {
  list-style: none;
  padding: 0;
}

li {
  font-size: 1.2rem;
  line-height: 1.6;
  margin-bottom: 0.5rem;
}

/* Links */
a {
  color: #1e90ff;
  text-decoration: none;
  display: inline-flex;
  justify-content: center;
  align-items: center;
  font-size: 2rem;
  margin: 0 0.5rem;
}

a:hover {
  text-decoration: underline;
}

/* Spacing for Sections */
.missions-section,
.team-section,
.contact-section,
.social-media-section {
  margin-bottom: 2rem;
  width: 70%;
}

.social-media-section ul {
  display: flex;
  justify-content: center;
}

/* Responsive Design */
@media (max-width: 768px) {
  .info-section {
    flex-direction: column;
    align-items: center;
  }

  .info-block {
    width: 100%;
    max-width: 300px;
  }
}
</style>
