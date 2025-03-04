import { createRouter, createWebHistory } from 'vue-router';
import HelloWorld from '../components/HelloWorld.vue';

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HelloWorld,
  },
  // Add more routes here as needed
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
