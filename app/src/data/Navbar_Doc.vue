<template>
  <nav class="navbar navbar-expand-lg bg-body-tertiary">
    <div class="container-fluid">
      <a class="navbar-brand" href="#">EEG Visualizer</a>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarText">
        <ul class="navbar-nav me-auto mb-2 mb-lg-0">
          <li class="nav-item">
            <a class="nav-link active" aria-current="page" href="/about">About</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="/visualize">Visualize</a>
          </li>
        </ul>
        <span class="navbar-text">
          Logged in as Patient
        </span>
      </div>
    </div>
  </nav>
  </template>
  
  <script>
  import { ref } from 'vue';
  import { useRoute, useRouter } from 'vue-router';
  
  export default {
    name: 'NavbarDoc',
    setup() {
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
      };
    },
  };
  </script>
  
  <style scoped>
  /* Your styles here */
  </style>
  