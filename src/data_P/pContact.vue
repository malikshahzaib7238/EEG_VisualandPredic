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
            <div class="container bg-white">
                <div class="form-container p-6 rounded-lg shadow-md">
                  <h4 class="form-title text-lg font-semibold mb-4">Contact Us</h4>
                  <form @submit.prevent="handleSubmit">
                    <div class="form-group mb-4">
                      <input
                        id="name"
                        type="text"
                        placeholder="Name"
                        class="form-input mt-1 block w-full"
                        v-model="name"
                        required
                      />
                    </div>
                    <div class="form-group mb-4">
                      <input
                        id="email"
                        type="email"
                        placeholder="Email"
                        class="form-input mt-1 block w-full"
                        v-model="email"
                        required
                      />
                    </div>
                    <div class="form-group mb-4">
                      <textarea
                        id="message"
                        placeholder="Message"
                        class="form-input mt-1 block w-full"
                        v-model="message"
                        required
                        rows="4"
                      ></textarea>
                    </div>
                    <button
                      type="submit"
                      class="submit-button bg-blue-500 hover:bg-blue-600 text-white font-semibold py-2 px-4 rounded transition duration-300"
                      :class="{ 'submitting': hover }"
                      @mouseover="hover = true"
                      @mouseleave="hover = false"
                    >
                      {{ hover ? 'Submitting...' : 'Submit' }}
                    </button>
                  </form>
                </div>
            
                <!-- Contact Information -->
                <div class="contact-info mt-8 text-center">
                  <p><strong>Name:</strong> Malik Shahzaib</p>
                  <p><strong>Email:</strong> malikshahzaib7238@gmail.com</p>
                  <p><strong>Phone:</strong> +92-123-456-789</p>
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
  </style>
  