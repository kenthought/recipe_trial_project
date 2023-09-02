import { authStore } from "~/stores/authStore"

export default defineNuxtPlugin(async (nuxtApp) => {
    const auth = authStore();

    if(!auth.isLoggedIn) {
        auth.fetchUser()
    }
})