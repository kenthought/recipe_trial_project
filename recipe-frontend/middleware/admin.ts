import { authStore } from "~/stores/authStore";

//Restrict basic user from viewing admin dashboard
export default defineNuxtRouteMiddleware(async (to, from) => {
  const auth = authStore();
  await auth.fetchUser()
  if (!auth.user?.is_superuser) return navigateTo("/", {replace: true});
});
