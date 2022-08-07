<template>
  <navbar-header></navbar-header>
  <section class="uk-section" uk-height-viewport="expand: true">
    <div class="uk-container uk-overflow-auto">
      <table class="uk-table uk-table-hover uk-table-middle uk-table-divider">
        <thead>
          <tr>
            <th class="uk-table-shrink"></th>
            <th class="uk-width-small">From</th>
            <th class="uk-table-expand">Message</th>
            <th class="uk-width-small">Received At</th>
            <th class="uk-table-shrink">Action</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="message in messages" :key="message.id">
            <td><input class="uk-checkbox" type="checkbox" data-id="{message.id}"></td>
            <td>{{ message.sent_from }}</td>
            <td class="uk-table-link" style="max-width: 0;">
              <router-link class="uk-link-reset" :to="'/message/' + message.id"
                style="text-overflow: ellipsis; overflow: hidden; white-space: nowrap;">
                <span>
                  {{ message.title }} -
                </span>
                <span class="uk-text-muted">
                  {{ message.message }}
                </span>
              </router-link>
            </td>
            <td>{{ beforeNow(message.created) }}</td>
            <td class="uk-text-truncate">
              <button class="uk-button-small" @click="removeMessage(message.id)">
                <span uk-icon="trash"></span>
              </button>
            </td>
          </tr>
          <tr v-if="!messages.length">
            <td colspan="5" class="uk-text-center uk-text-large uk-text-bold">No messages</td>
          </tr>
        </tbody>
      </table>
    </div>
  </section>
</template>

<script>
import { getMessagesList, removeMessage } from '@/services/api.js';
import moment from 'moment';
import NavbarHeader from '@/components/Navbar.vue';
import { useToast } from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';


export default {
  name: "receipt-message-list",
  components: {
    NavbarHeader
  },
  data() {
    return {
      messages: []
    }
  },
  methods: {
    async getAllMessages(params) {
      this.messages = await getMessagesList(params);
    },
    beforeNow(time) {
      const created = new moment(time);
      const now = new moment();
      if (now.diff(created, 'second') < 60) {
        return now.diff(created, 'second') + ' seconds ago';
      } else if (now.diff(created, 'minute') < 60) {
        return now.diff(created, 'minute') + ' minutes ago';
      } else if (now.diff(created, 'hour') < 24) {
        return now.diff(created, 'hour') + ' hours ago';
      } else {
        return now.diff(created, 'day') + ' days ago';
      }
    },
    async removeMessage(id) {
      const result = await removeMessage(id);
      const $toast = useToast();
      if (result.status === 200) {
        this.messages = this.messages.filter(m => m.id !== id);
        $toast.success(result.message, {
          position: "top-right"
        });
      } else {
        Object.values(result.message).map(m => {
          const msg = typeof m === 'string' ? m : m[0]
          $toast.error(msg, {
            position: "top-right"
          });
        });
      }
    }
  },
  mounted() {
    this.getAllMessages({});
  },
}
</script>