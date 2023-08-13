<template>
    <nav class="navbar bg-body-tertiary mb-4">
      <div class="container-fluid">
        <router-link to="/" class="navbar-brand">
          EEG Predictor
        </router-link>
        <button
          class="navbar-toggler"
          type="button"
          data-bs-toggle="collapse"
          data-bs-target="#navbarNav"
          aria-controls="navbarNav"
          aria-expanded="false"
          aria-label="Toggle navigation"
        >
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
          <ul class="navbar-nav mr-auto">
            <li class="nav-item">
              <router-link to="/about" class="btn btn-outline-primary me-2">
                About
              </router-link>
            </li>
            <li class="nav-item">
              <router-link to="/graph" class="btn btn-outline-primary me-2">
                Visualize
              </router-link>
            </li>
          </ul>
        </div>
        <p class="navbar-text me-2">Logged in as: Patient</p>
        <button class="btn btn-outline-primary me-2" @click="handleLogout">
          Logout
        </button>
        <router-link to="/contactus" class="btn btn-outline-primary">
          Contact Us
        </router-link>
      </div>
    </nav>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  
  export default {
    name: 'Navbar',
    props: {
      userType: String, // Pass the user type as a prop
    },
    setup(props) {
      const route = useRoute();
      const router = useRouter();
      const loggedIn = ref(true); // Set it to your actual login status
  
      const handleLogout = () => {
        localStorage.removeItem('loggedIn');
        // Replace the route with the login page
        router.replace({ name: 'Login' });
      };
  
      return {
        loggedIn,
        handleLogout,
        userType: props.userType,
      };
    },
  };
  </script>
  
  <style scoped>
  /* Your styles here */
  </style>
  