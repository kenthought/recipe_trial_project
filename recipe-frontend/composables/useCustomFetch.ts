import type { UseFetchOptions } from 'nuxt/app'
import { getCookie, setCookie, removeCookie } from "typescript-cookie";

type Token = {
    refresh: string,
    access: string
  }

// Customized useFetch for rotating tokens
export function useCustomFetch<T> (path: string, options: UseFetchOptions<T> = {}) {
    let headers: any = {}
    let refreshToken: string  = "";

    // Checks if process is in SSR or CSR and fetch Cookies
    // useCookie for SSR and getCookie for CSR
    if(process.server) {
        const temp : any = useCookie("refresh")
        refreshToken = temp.value as string
    }

    if(process.client) {
        refreshToken = getCookie("refresh") as string
    }

    if (refreshToken != null) {
        const tokenParts = JSON.parse(atob(refreshToken.split(".")[1]));
        const now = Math.ceil(Date.now() / 1000);

        // Checks if access token is expired
        // If yes refresh the token. Store the refresh and access in
        // Cookies
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
                }
                if(process.client) {
                    setCookie("access", token.access)
                    setCookie("refresh", token.refresh)
                }
            })
        }  else {
            console.log('Refresh token is expired', tokenParts.exp, now);
            removeCookie("user_id");
            removeCookie("refresh");
            removeCookie("access");
            window.location.href = '/auth/login';
            
            return;
        }

        // Checks if process is in SSR or CSR. Fetch refresh and access 
        // cookie by getCookie if the process is CSR or useCookie in SSR
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
            // console.log("client header:", headers)
        }
    }  else {
        console.log('Refresh token not available.');
        removeCookie("user_id");
        removeCookie("refresh");
        removeCookie("access");
        window.location.href = '/auth/login';
        return;
     }

    return useFetch("http://127.0.0.1:8000/api/" + path, {
    watch: false,
    ...options,
    headers: { 
        ...headers
        },
  })
}
