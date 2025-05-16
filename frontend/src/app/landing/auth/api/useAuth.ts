import {useAuthStore} from "../../../../common/stores/useAuthStore";
import axios from 'axios'

const API_URL = import.meta.env.VITE_API_URL

export async function login(username: string, password: string){
  try{
    const response = await axios.post(`${API_URL}/auth/login/`, {
      username,
      password,
      })

    const token = response.data.access
    const authStore = useAuthStore()
    authStore.login(token)
    return true
    }
    catch (error){
    console.log('Login failed', error)
      throw error
    }
  }

export function logout(){
  const authStore = useAuthStore()
  authStore.logout()
}

export function useAuth(){
  const authStore = useAuthStore()
  return{
    isAuthenticated: () => authStore.isAuthenticated,
    getUser: () => authStore.user,
    login,
    logout,
  }
}

