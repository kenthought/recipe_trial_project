import { authStore } from "~/stores/authStore";

// Checkes whether the user is logged in. If not redirect to login page
export default defineNuxtRouteMiddleware((to, from) => {
  const auth = authStore();
  if (!auth.isLoggedIn) return navigateTo("/auth/login", {replace: true});
});
