<template>
  <section class="uk-section">
    <div class="uk-container uk-container-small">
      <div class="uk-flex uk-flex-center">
        <div class="uk-width-large uk-margin-large-top">
          <h2 class="uk-text-center">Welcome!</h2>
          <form @submit.prevent="signup" method="post" class="uk-form-stacked">
            <div class="uk-margin-small-top uk-width-1-1@s">
              <label class="uk-form-label">username</label>
              <div class="uk-form-controls">
                <input class="uk-input" type="text" v-model="username" required>
              </div>
            </div>
            <div class="uk-margin-small-top uk-width-1-1@s">
              <label class="uk-form-label">email</label>
              <div class="uk-form-controls">
                <input class="uk-input" type="text" v-model="email" required>
              </div>
            </div>
            <div class="uk-margin-small-top uk-width-1-1@s">
              <label class="uk-form-label">password</label>
              <div class="uk-form-controls">
                <input class="uk-input" type="text" v-model="password" required>
              </div>
            </div>
            <div class="uk-margin-top uk-width-1-1@s">
              <button type="submit"
                class="uk-button uk-button-primary uk-width-1-1 uk-border-rounded uk-text-uppercase">Signup</button>
            </div>
          </form>
          <div class="uk-flex uk-flex-center uk-margin-top">
            <span class="uk-margin-small-right">If you have a account, please go to </span>
            <router-link to="/login">Login Page</router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { signup } from '@/services/api.js';
import { useToast } from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';

export default {
  name: 'auth-signup',
  data() {
    return {
      email: "",
      username: "",
      password: ""
    };
  },
  methods: {
    async signup() {
      const formData = {
        email: this.email,
        username: this.username,
        password: this.password
      }
      const registration = await signup(formData);
      const $toast = useToast();
      if (registration.status === 200) {
        $toast.success(registration.message, {
          position: "top-right",
        });
        this.$router.push({ name: 'auth-login' });
      } else {
        Object.values(registration.message).map(m => {
          const msg = typeof m === 'string' ? m : m[0]
          $toast.error(msg, {
            position: "top-right"
          });
        });
      }
    },
  }
}
</script>