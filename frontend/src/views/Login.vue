<template>
  <section class="uk-section">
    <div class="uk-container uk-container-small">
      <div class="uk-flex uk-flex-center">
        <div class="uk-width-large uk-margin-large-top">
          <h2 class="uk-text-center">Welcome!</h2>
          <form @submit.prevent="join" method="post" class="uk-form-stacked">
            <div class="uk-margin-small-top uk-width-1-1@s">
              <label class="uk-form-label">username</label>
              <div class="uk-form-controls">
                <input class="uk-input" type="text" v-model="username" required>
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
                class="uk-button uk-button-primary uk-width-1-1 uk-border-rounded uk-text-uppercase">Login</button>
            </div>
          </form>
          <div class="uk-flex uk-flex-center uk-margin-top">
            <span class="uk-margin-small-right">If you don't have a account, please go to </span>
            <router-link to="/signup">Signup Page</router-link>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { login } from '@/services/api.js';
import { useToast } from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';

export default {
  name: 'auth-login',
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    async join() {
      const formData = {
        username: this.username,
        password: this.password
      }
      const authorization = await login(formData);
      const $toast = useToast();
      if (authorization.status === 200) {
        $toast.success(authorization.message, {
          position: "top-right",
        });
        this.$router.push({ name: 'receipt-messages' });
      } else {
        Object.values(authorization.message).map(m => {
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