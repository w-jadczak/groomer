import { defineStore } from "pinia"
import { jwtDecode } from "jwt-decode"
import {useStorage} from "@vueuse/core";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: useStorage('token', null as string | null),
    user: useStorage('user', null as User | null),
    isAuthenticated: useStorage('isAuthenticated', false)
  }),

  actions: {
    loadUserFromToken() {
      if (this.token) {
        try {
          this.user = jwtDecode(this.token) as User
          this.isAuthenticated = true
        } catch (error) {
          console.error("Invalid token", error)
          this.logout()
        }
      }
    },

    login(token: string) {
      this.token = token
      localStorage.setItem("token", token)
      this.loadUserFromToken()
    },

    logout() {
      this.token = null
      this.user = null
      this.isAuthenticated = false
    },
    init(){
      if(this.token && !this.user){
        this.loadUserFromToken()
      }
    }
  },
})
