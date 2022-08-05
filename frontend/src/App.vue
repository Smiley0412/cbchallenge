<template>
  <router-view />
</template>

<script>
import { useToast } from 'vue-toast-notification';
import 'vue-toast-notification/dist/theme-sugar.css';

export default {
  name: 'App',
  created() {
    const token = localStorage.getItem("cb_token")
    this.connection = new WebSocket(`${process.env.VUE_APP_SOCKET_ENDPOINT}?token=${token}`)

    const _self = this;
    this.connection.onmessage = function (event) {
      const message = JSON.parse(event.data);
      const $toast = useToast();
      $toast.success(message.text, {
        position: "top-right",
        onClick: () => {
          _self.$router.push({ path: `/message/${message.id}` });
        }
      });
    }

    this.connection.onopen = function (event) {
      console.log(event);
    }
  },
}
</script>
