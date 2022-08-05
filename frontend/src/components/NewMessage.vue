<template>
  <navbar-header></navbar-header>
  <section class="uk-section" uk-height-viewport="expand: true">
    <div class="uk-container uk-container-small">
      <div class="uk-flex uk-flex-center">
        <div class="uk-width-large uk-margin-large-top">
          <h2 class="uk-text-center">{{ who() }}</h2>
          <form @submit.prevent="sendMessage" method="post">
            <div class="uk-flex uk-margin-small-top">
              <div class="uk-width-expand">
                <select class="uk-select" v-model="to" placeholder="Message Title" ref="to">
                  <option value="">Select User</option>
                  <option v-for="user in users" :key="user.id" :value="user.id">{{ user.username }}</option>
                </select>
              </div>
            </div>
            <div class="uk-flex uk-margin-small-top">
              <div class="uk-width-expand">
                <input class="uk-input" type="text" v-model="title" ref="title" placeholder="Message Title" />
              </div>
            </div>
            <div class="uk-flex uk-margin-small-top">
              <div class="uk-width-expand">
                <textarea class="uk-textarea" type="text" v-model="message" ref="message" placeholder="Message Body"
                  rows="8">
                </textarea>
              </div>
            </div>
            <div class="uk-margin-small-top">
              <div class="uk-align-right">
                <button class="uk-button uk-button-primary">Send</button>
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>

  </section>
</template>

<script>
import { getAllUsers, sendNewMessage } from '@/services/api.js';
import NavbarHeader from '@/components/Navbar.vue';
import { useToast } from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';

export default {
  name: "new-message",
  data() {
    return {
      to: '',
      users: [],
      title: '',
      message: '',
      by: '',
      fixed: false
    }
  },
  components: {
    NavbarHeader
  },
  methods: {
    async initUsers() {
      this.users = await getAllUsers();
    },
    who() {
      if (this.to) {
        const username = this.users.filter(u => u.id == this.to)[0]?.username;
        return "To " + username;
      }
      return "New Message";
    },
    async sendMessage() {
      const formData = {
        to: this.to,
        by: this.by,
        title: this.title,
        message: this.message
      };
      const result = await sendNewMessage(formData);
      const $toast = useToast();
      if (result.status === 200) {
        $toast.success(result.message, {
          position: "top-right",
        });
        this.$router.push({ name: 'sent-messages' });
      } else {
        $toast.error(result.message, {
          position: "top-right"
        });
      }

    }
  },
  mounted() {
    if (this.$route.params?.to) {
      this.fixed = true;
      this.to = this.$route.params.to
    }
    this.by = Number(localStorage.getItem('cb_user_id'));
    this.initUsers();
  }
}
</script>