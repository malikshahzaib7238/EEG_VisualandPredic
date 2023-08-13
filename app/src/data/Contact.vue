 <template>
  <div>
    <nav class="navbar navbar-expand-lg bg-body-tertiary">
      <div class="container-fluid">
        <a class="navbar-brand" href="/welcome">EEG Visualizer</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarText" aria-controls="navbarText" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarText">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            <li class="nav-item">
              <a class="nav-link active" aria-current="page" href="/about">About</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/predict">Predict</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/visualize">Visualize</a>
            </li>
            <li class="nav-item">
              <a class="nav-link" href="/view">View Files</a>
            </li>
          </ul>
          <div class="d-flex">
            <span class="navbar-text">
              Logged in as Doctor
            </span>
            <ul class="navbar-nav me-auto mb-2 mb-lg-0">
              <li class="nav-item">
                <a class="nav-link ms-3" aria-current="page" href="/">Log Out</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/contact">Contact Us</a>
              </li>
            </ul>
            
          </div>
        </div>
      </div>
      </nav>
      <div class="container">
        <div class="form-container">
          <h4 class="form-title">Contact Us</h4>
          <form @submit.prevent="handleSubmit">
            <div class="form-group">
              <label for="name">Name</label>
              <input
                id="name"
                v-model="name"
                type="text"
                class="input"
                required
              />
            </div>
            <div class="form-group">
              <label for="email">Email</label>
              <input
                id="email"
                v-model="email"
                type="email"
                class="input"
                required
              />
            </div>
            <div class="form-group">
              <label for="message">Message</label>
              <textarea
                id="message"
                v-model="message"
                class="input"
                required
                rows=6
              ></textarea>
            </div>
            <button
              type="submit"
              class="btn-submit"
            >
              Submit
            </button>
          </form>
        </div>
    
        <!-- Contact Information -->
        <div class="contact-info">
          <p><strong>Name:</strong> Malik Shahzaib</p>
          <p><strong>Email:</strong> malikshahzaib7238@gmail.com</p>
          <p><strong>Phone:</strong> +92-123-456-789</p>
        </div>
      </div>
      </div>
    </template>
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        name: "",
        email: "",
        message: "",
        hover: false,
      };
    },
    methods: {
      async handleSubmit() {
        const formData = {
          name: this.name,
          email: this.email,
          message: this.message,
        };
  
        try {
          const response = await axios.post('submit-form', formData);
  
          if (response.status === 200) {
            console.log('Form data sent successfully!');
            // Clear form fields
            this.name = "";
            this.email = "";
            this.message = "";
          } else {
            console.error('Failed to send form data.');
          }
        } catch (error) {
          console.error('An error occurred:', error);
        }
      },
    },
  };
  </script>
  
  
<style scoped>

.navbar{
  padding:5px 0;
  font-size: 14px;
}
.container {
  padding-top: 10dvh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 95dvh;
}
.content-container {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-top: 20px;
}

.contact-info {
  width: 30%;
  padding: 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  border: 2px solid #000000;
  border-radius: 12px;
  background-color: #FFFFFFCC;
}

/* Adjust the message textarea height */
.input-message {
  height: 120px;
}
.form-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  max-width: 600px;
  margin: 0 auto;
  padding: 16px;
  border: 2px solid #000000;
  border-radius: 12px;
  box-shadow: 1px 1px 4px rgba(0, 0, 0, 0.2);
  background-color: #FFFFFFCC;
}

.form-title {
  font-size: 1.5rem;
  margin-bottom: 16px;
  color: black;
}

.input {
  width: 100%;
  padding: 8px;
  border: 2px solid #ccc;
  border-radius: 4px;

}

.btn-submit {
  background-color: #000;
  color: #fff;
  padding: 8px 16px;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn-submit:hover {
  background-color: #111;
}

.contact-info {
  margin-top: 16px;
  padding: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  border: 2px solid #000000;
  border-radius: 12px;
  background-color: #FFFFFFCC;
}
</style>