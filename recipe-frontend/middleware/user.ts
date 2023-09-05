import { authStore } from "~/stores/authStore";

// Restrict logged in user from accessing login page
export default defineNuxtRouteMiddleware((to, from) => {
  const auth = authStore();
  if (auth.isLoggedIn) return navigateTo("/", {replace: true});
});
