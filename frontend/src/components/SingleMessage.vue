<template>
  <navbar-header></navbar-header>
  <section class="uk-section" uk-height-viewport="expand: true">
    <div class="uk-container uk-container-small" v-if="message">
      <div class="uk-margin-large-top">
        <h2 class="uk-text-center">{{ who(message) }}</h2>
        <hr />
        <p class="uk-text-large uk-text-underline">{{ message.title }}</p>
        <hr />
        <p class="uk-text-large">{{ message.message }}</p>
        <hr />
      </div>
      <div class="uk-margin-top">
        <router-link class="uk-button uk-button-secondary uk-align-right" :to="replyTo(message)">Reply
        </router-link>
      </div>
    </div>
  </section>
</template>

<script>
import { getSingleMessage } from '@/services/api.js';
import NavbarHeader from '@/components/Navbar.vue';
import { useToast } from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';

export default {
  name: "single-message",
  components: {
    NavbarHeader
  },
  data() {
    return {
      user: null,
      message: null
    }
  },
  methods: {
    async getSingleMessage(params) {
      const result = await getSingleMessage(params);
      if (result.status === 200) {
        this.message = result.data;
      } else {
        const $toast = useToast();
        Object.values(result.message).map(m => {
          const msg = typeof m === 'string' ? m : m[0]
          $toast.error(msg, {
            position: "top-right"
          });
        });
      }
    },
    who(message) {
      if (this.user == message.to) {
        return "From " + message.sent_from;
      } else if (this.user == message.by) {
        return "To " + message.sent_to;
      } else {
        return "";
      }
    },
    replyTo(message) {
      if (this.user == message.to) {
        return "/new/" + message.by;
      } else if (this.user == message.by) {
        return "/new/" + message.to;
      } else {
        return "/new";
      }
    }
  },
  mounted() {
    this.user = localStorage.getItem("cb_user_id");
    this.getSingleMessage(this.$route.params?.id);
  }
}
</script>