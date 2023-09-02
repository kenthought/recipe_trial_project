import { authStore } from "~/stores/authStore";

export default defineNuxtRouteMiddleware((to, from) => {
  const auth = authStore();
  if (auth.isLoggedIn) return navigateTo("/dashboard", {replace: true});
});
