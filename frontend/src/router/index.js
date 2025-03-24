import { createRouter, createWebHistory } from 'vue-router'
import AppLayout from '@/common/components/AppLayout.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: AppLayout,
  },
  // Add more routes here as needed
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
