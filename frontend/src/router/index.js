import { createWebHistory, createRouter } from "vue-router";
import Login from "@/views/Login.vue";
import Signup from "@/views/Signup.vue";
import Home from "@/views/Home.vue";
import NotFound from "@/views/NotFound.vue";
import ReceiptMessageList from '@/components/ReceiptMessageList.vue';
import SentMessageList from '@/components/SentMessageList.vue';
import SingleMessage from '@/components/SingleMessage.vue';
import NewMessage from '@/components/NewMessage.vue';

const routes = [
  {
    path: "/",
    name: "app-home",
    component: Home,
    children: [
      {
        path: "/",
        name: "receipt-messages",
        component: ReceiptMessageList
      },
      {
        path: "/sent",
        name: "sent-messages",
        component: SentMessageList
      },
      {
        path: "/message/:id",
        name: "single-message",
        component: SingleMessage
      },
      {
        path: "/new",
        name: "new-message",
        component: NewMessage
      },
      {
        path: "/new/:to",
        name: "new-message-to",
        component: NewMessage
      }
    ]
  },
  {
    path: "/login",
    name: "auth-login",
    component: Login,
  },
  {
    path: "/signup",
    name: "auth-signup",
    component: Signup,
  },
  {
    path: "/:pathMatch(.*)*",
    name: "page-not-found",
    component: NotFound
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, _, next) => {
  const isLoggedIn = localStorage.getItem('cb_token');
  if (!isLoggedIn && to.name !== "auth-login" && to.name !== "auth-signup") {
    console.log(isLoggedIn, to);
    return next({ name: "auth-login" });
  }
  return next();
})

export default router;