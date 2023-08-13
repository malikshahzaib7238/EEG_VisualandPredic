<template>
    <div>
        <nav class="navbar navbar-expand-lg bg-body-tertiary">
            <div class="container-fluid">
              <a class="navbar-brand" href="/pwelcome">EEG Visualizer</a>
              <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
                <span class="navbar-toggler-icon"></span>
              </button>
              <div class="collapse navbar-collapse" id="navbarText">
                <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                  <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="/pabout">About</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" href="/visualize">Visualize</a>
                  </li>
                </ul>
                <div class="d-flex">
                  <span class="navbar-text">
                    Logged in as Patient
                  </span>
                  <ul class="navbar-nav me-auto mb-2 mb-lg-0">
                    <li class="nav-item">
                      <a class="nav-link ms-3" aria-current="page" href="/">Log Out</a>
                    </li>
                    <li class="nav-item">
                      <a class="nav-link" href="/pcontact">Contact Us</a>
                    </li>
                  </ul>
                  
                </div>
              </div>
            </div>
            </nav>
          
            <div class="welcome-container text-center">
                <div class="content">
                  <h1 class="main-title">EEG Predictor</h1>
                  <p class="description">
                    Welcome to the EEG Visualizer. Press the button below to get started
                  </p>
                  <div class="buttons-container">
                    <router-link to="/visualize">
                      <button class="btn ghost">Visualize Now</button>
                    </router-link>
                  </div>
                </div>
              </div>
            </div>
          </template>
  
  <script>
  export default {
    // Component options go here
  };
  </script>
  
  <style scoped>
  /* Your styles here */
  .navbar {
    padding: 5px 0;
    font-size: 14px;
  }
  .welcome-container {
    border-radius: 12px;
    padding:25px;
    margin: 25dvh 36dvh;
    min-height: 30dvh;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
   /* Adjust the value if you have a fixed navbar height */
  }
  .description{
    padding-top: 5px;
  }
  </style>
  