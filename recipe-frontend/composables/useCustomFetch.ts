import type { UseFetchOptions } from 'nuxt/app'
import { getCookie, setCookie, removeCookie } from "typescript-cookie";

type Token = {
    refresh: string,
    access: string
  }

export function useCustomFetch<T> (path: string, options: UseFetchOptions<T> = {}) {
    let headers: any = {}
    let refreshToken: string  = "";

    if(process.server) {
        const temp : any = useCookie("refresh")
        refreshToken = temp.value as string

        console.log("Server:", refreshToken)
    }

    if(process.client) {
        refreshToken = getCookie("refresh") as string
        console.log("Client:", refreshToken)
    }

    if (refreshToken != null) {
        const tokenParts = JSON.parse(atob(refreshToken.split(".")[1]));
        const now = Math.ceil(Date.now() / 1000);

        if(tokenParts.exp > now) {
            useFetch("http://127.0.0.1:8000/api/token/refresh/", { 
                method: "POST",
                body: { refresh: refreshToken }
            }).then(response => {
                const fetch: unknown = response.data.value;
                const token: Token = fetch as Token
                if(process.server) {
                    const access = useCookie("access");
                    access.value = token.access;
                    const refresh = useCookie("refresh");
                    refresh.value = token.refresh;
                    console.log("server:", token.refresh)
                }
                if(process.client) {
                    setCookie("access", token.access)
                    setCookie("refresh", token.refresh)
                    console.log("client:", token.refresh)
                }
            })
        }  else {
            console.log('Refresh token is expired', tokenParts.exp, now);
            removeCookie("access");
            removeCookie("refresh");
            removeCookie("user");
            removeCookie("user_id");
            window.location.href = '/login';
            
            return;
        }

        if(process.server) {
            const access = useCookie("access");
            headers = {
                Authorization: "JWT " + access.value,
                "Content-Type": "application/json",
                accept: "application/json",
            }

            console.log("server header:", headers)
        }

        if(process.client) {
            headers = {
                Authorization: "JWT " + getCookie("access"),
                "Content-Type": "application/json",
                accept: "application/json",
            }
            console.log("client header:", headers)
        }
    }  else {
        console.log('Refresh token not available.');
        removeCookie("access");
        removeCookie("refresh");
        removeCookie("user");
        removeCookie("user_id");
        window.location.href = '/login';
        return;
     }

     if(process.server) {
        headers = {
            ...headers,
            ...useRequestHeaders(['cookie'])
        }
     }

    return useFetch("http://127.0.0.1:8000/api/" + path, {
    watch: false,
    ...options,
    headers: { 
        ...headers
        },
  })
}
