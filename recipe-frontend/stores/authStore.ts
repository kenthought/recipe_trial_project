import {defineStore} from "pinia"
import { setCookie } from "typescript-cookie"

type User = {
    id: number,
    email: string,
    first_name: string,
    middle_name:string,
    last_name:string,
    is_staff: number
    is_superuser: number
}

type Credentials = {
    email: string,
    password: string,
}

type Token = {
  refresh: string,
  access: string
}

export const authStore = defineStore('auth', () => {
    const user = reactive(ref<User | null>(null))
    const userCookie = useCookie("user");
    const isLoggedIn = computed(() => !!userCookie.value)

    const fetchUser = async () => {
      const user_id = useCookie("user_id");
      const {data, error} : any = await useCustomFetch("users/" + user_id.value)
      console.log("Data:", data.value)
      console.log("Error:", error.value)
      user.value = data;
      userCookie.value = JSON.stringify(user.value)
    }
    
    const login = async (credentials: Credentials) => {
          let fetchedUser: User = {} as User;

          const login : any = await useFetch("http://127.0.0.1:8000/api/token/", {
            method: "POST",
            body: credentials,
            headers: {
              "Content-Type": "application/json",
              accept: "application/json",
            }
          })
            .then(response => {
              const fetch: unknown =  response.data.value;
              const refreshData: Token = fetch as Token;
              const tokenParts = JSON.parse(atob(refreshData.refresh.split(".")[1]));
              fetchedUser = tokenParts as User;
              const access = useCookie("access");
              access.value = refreshData.access;
              const refresh = useCookie("refresh");
              refresh.value = refreshData.refresh;
              const user_id = useCookie("user_id");
              user_id.value = fetchedUser.id.toString();

              fetchUser();
              window.location.href = '/dashboard';
      }).catch(error => {
              console.log("loginError:", error)
            })

        return login
      };


    return {user, login, isLoggedIn, fetchUser}
  })