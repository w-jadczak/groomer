import { defineStore } from "pinia"
import { jwt_decode } from "jwt-decode"

export const useAuthStore = defineStore("auth", {
  state: () => ({
    token: localStorage.getItem("token") || null,
    user: null as User | null,
    isAuthenticated: false,
  }),

  actions: {
    loadUserFromToken() {
      if (this.token) {
        try {
          this.user = jwt_decode(this.token) as User
          this.isAuthenticated = true
        } catch (error) {
          console.error("Invalid token", error)
          this.logout()
        }
      }
    },
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
    localStorage.removeItem("token")
  },
})
